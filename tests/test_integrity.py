import copy
import json
from pathlib import Path
import unittest

from conversation_analysis.prepare import parse_turns, sha256, verify_bytes
from conversation_analysis.verify_evidence import load_corpus, verify

ROOT = Path(__file__).resolve().parents[1]


class ParserTests(unittest.TestCase):
    def test_both_interviewer_labels_and_exact_offsets(self):
        text = 'AI: Start?\nUser: First line\nsecond line.\n\nAssistant: Follow-up?\nUser: Fine.'
        turns = parse_turns(text)
        self.assertEqual([t['role'] for t in turns], ['interviewer', 'participant', 'interviewer', 'participant'])
        self.assertEqual(turns[1]['text'], 'First line\nsecond line.')
        for turn in turns:
            self.assertEqual(text[turn['source_start']:turn['source_end']], turn['text'])

    def test_empty_turn_is_retained(self):
        turns = parse_turns('Assistant: Question?\nUser:\nAssistant: Still there?')
        self.assertEqual(len(turns), 3)
        self.assertEqual(turns[1]['text'], '')

    def test_unrecognized_prefix_fails(self):
        with self.assertRaises(ValueError):
            parse_turns('Participant: Unknown label.')
        with self.assertRaises(ValueError):
            parse_turns('Lost context\nUser: Answer')

    def test_crlf_and_unicode_preserved(self):
        text = 'Assistant: Why?\r\nUser: It\u2019s useful.\r\n'
        turn = parse_turns(text)[1]
        self.assertEqual(turn['text'], 'It\u2019s useful.')
        self.assertEqual(text[turn['source_start']:turn['source_end']], turn['text'])

    def test_changed_source_checksum_rejected(self):
        verify_bytes(b'original', sha256(b'original'))
        with self.assertRaises(ValueError):
            verify_bytes(b'changed', sha256(b'original'))


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.corpus = load_corpus(ROOT / 'examples/synthetic-conversations.jsonl')
        self.ledger = json.loads((ROOT / 'examples/synthetic-evidence.json').read_text(encoding='utf-8'))

    def test_all_authored_example_evidence(self):
        self.assertEqual(verify(self.corpus, self.ledger), 10)

    def test_wrong_speaker_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        ledger[0]['role'] = 'interviewer'
        with self.assertRaisesRegex(ValueError, 'speaker'):
            verify(self.corpus, ledger)

    def test_paraphrase_rejected_as_quote(self):
        ledger = copy.deepcopy(self.ledger)
        ledger[0]['quote'] = 'AI does all my emails.'
        with self.assertRaisesRegex(ValueError, 'exact'):
            verify(self.corpus, ledger)

    def test_quote_from_different_turn_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        ledger[0]['turn_id'] = 't0004'
        with self.assertRaises(ValueError):
            verify(self.corpus, ledger)

    def test_valid_offsets_accepted(self):
        ledger = copy.deepcopy(self.ledger)
        turn = self.corpus[0]['turns'][1]['text']
        ledger[0]['quote_start'] = turn.index(ledger[0]['quote'])
        ledger[0]['quote_end'] = ledger[0]['quote_start'] + len(ledger[0]['quote'])
        self.assertEqual(verify(self.corpus, ledger), 10)

    def test_wrong_or_incomplete_offsets_rejected(self):
        for start, end in [(1, 2), (-1, 5), (0, 100000), (0, None), (False, 5)]:
            ledger = copy.deepcopy(self.ledger)
            ledger[0]['quote_start'], ledger[0]['quote_end'] = start, end
            with self.assertRaisesRegex(ValueError, 'offsets'):
                verify(self.corpus, ledger)

    def test_unknown_locator_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        ledger[0]['conversation_id'] = 'unknown'
        with self.assertRaisesRegex(ValueError, 'locator'):
            verify(self.corpus, ledger)

    def test_empty_evidence_rejected(self):
        with self.assertRaises(ValueError):
            verify(self.corpus, [])
        ledger = copy.deepcopy(self.ledger)
        ledger[0]['quote'] = ' '
        with self.assertRaises(ValueError):
            verify(self.corpus, ledger)

    def test_ambiguous_duplicate_locator_rejected(self):
        corpus = copy.deepcopy(self.corpus)
        corpus[0]['turns'].append(corpus[0]['turns'][0])
        with self.assertRaisesRegex(ValueError, 'Duplicate turn'):
            verify(corpus, self.ledger)
        with self.assertRaisesRegex(ValueError, 'Duplicate conversation'):
            verify(self.corpus + [self.corpus[0]], self.ledger)


if __name__ == '__main__':
    unittest.main()
