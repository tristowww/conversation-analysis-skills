"""Check exact quotations and speaker attribution, not interpretation quality."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_corpus(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def verify(corpus: list[dict], ledger: list[dict]) -> int:
    index = {}
    for conversation in corpus:
        conversation_id = conversation['conversation_id']
        if conversation_id in index:
            raise ValueError('Duplicate conversation ID in corpus.')
        turns = {turn['turn_id']: turn for turn in conversation['turns']}
        if len(turns) != len(conversation['turns']):
            raise ValueError('Duplicate turn ID in conversation.')
        index[conversation_id] = turns
    if not ledger:
        raise ValueError('Empty evidence ledger.')
    for item in ledger:
        if not isinstance(item.get('claim_id'), str) or not item['claim_id'].strip():
            raise ValueError('Missing claim ID.')
        turn = index.get(item.get('conversation_id'), {}).get(item.get('turn_id'))
        if turn is None:
            raise ValueError('Evidence locator is not in corpus.')
        if item.get('role') != turn['role']:
            raise ValueError('Evidence speaker mismatch.')
        quote = item.get('quote')
        if not isinstance(quote, str) or not quote.strip() or quote not in turn['text']:
            raise ValueError('Quote is not an exact nonempty source span.')
        if 'quote_start' in item or 'quote_end' in item:
            start, end = item.get('quote_start'), item.get('quote_end')
            if (type(start) is not int or type(end) is not int or
                    start < 0 or end <= start or end > len(turn['text']) or
                    turn['text'][start:end] != quote):
                raise ValueError('Quote offsets do not identify the exact source span.')
    return len(ledger)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, required=True)
    parser.add_argument('--ledger', type=Path, required=True)
    args = parser.parse_args()
    ledger = json.loads(args.ledger.read_text(encoding='utf-8'))
    count = verify(load_corpus(args.corpus), ledger)
    print(f'Checked {count} evidence rows. Interpretation, coverage, and privacy still require review.')


if __name__ == '__main__':
    main()
