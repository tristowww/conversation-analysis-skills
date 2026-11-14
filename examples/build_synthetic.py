"""Regenerate wholly invented example inputs and their illustrative evidence."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conversation_analysis.prepare import parse_turns, sha256

EXAMPLES = {
    'synthetic-01': (
        'Assistant: How are you using AI in your work?\n'
        'User: I use it for first drafts of routine emails. It saves me time, but I still check every name and number.\n'
        'Assistant: What would make that process easier?\n'
        'User: A one-page guide from IT showing which kinds of information we can put into the tool would help.\n'
        'Assistant: So you want AI to take over writing all your emails?\n'
        'User: No. I want to keep reviewing them. My question is what information I can safely include.'
    ),
    'synthetic-02': (
        'Assistant: Tell me about a recent experience with an AI tool.\n'
        'User: Yesterday it changed the column names in a spreadsheet formula. I spent an hour finding the mismatch.\n'
        'Assistant: What do you think should happen next?\n'
        'User: I do not have a proposed solution. I can show someone the original file and the formula it gave me.'
    ),
    'synthetic-03': (
        'AI: What is your experience with AI at work?\n'
        'User: We should fix AI.\n'
        'AI: Could you describe one situation you would like to change?\n'
        'User: I would rather skip that question and stop here.\n'
        'AI: Understood. Thank you for your time.'
    ),
}

EVIDENCE = [
    {'claim_id': 'T1', 'conversation_id': 'synthetic-01', 'turn_id': 't0002', 'role': 'participant',
     'quote': 'I use it for first drafts of routine emails.'},
    {'claim_id': 'S1', 'conversation_id': 'synthetic-01', 'turn_id': 't0002', 'role': 'participant',
     'quote': 'It saves me time, but I still check every name and number.'},
    {'claim_id': 'I1', 'conversation_id': 'synthetic-01', 'turn_id': 't0004', 'role': 'participant',
     'quote': 'A one-page guide from IT showing which kinds of information we can put into the tool would help.'},
    {'claim_id': 'A1', 'conversation_id': 'synthetic-02', 'turn_id': 't0002', 'role': 'participant',
     'quote': 'Yesterday it changed the column names in a spreadsheet formula. I spent an hour finding the mismatch.'},
    {'claim_id': 'A1', 'conversation_id': 'synthetic-02', 'turn_id': 't0004', 'role': 'participant',
     'quote': 'I do not have a proposed solution. I can show someone the original file and the formula it gave me.'},
    {'claim_id': 'X1', 'conversation_id': 'synthetic-01', 'turn_id': 't0005', 'role': 'interviewer',
     'quote': 'So you want AI to take over writing all your emails?'},
    {'claim_id': 'X1', 'conversation_id': 'synthetic-01', 'turn_id': 't0006', 'role': 'participant',
     'quote': 'No. I want to keep reviewing them. My question is what information I can safely include.'},
    {'claim_id': 'A2', 'conversation_id': 'synthetic-03', 'turn_id': 't0002', 'role': 'participant',
     'quote': 'We should fix AI.'},
    {'claim_id': 'X2', 'conversation_id': 'synthetic-03', 'turn_id': 't0004', 'role': 'participant',
     'quote': 'I would rather skip that question and stop here.'},
    {'claim_id': 'X2', 'conversation_id': 'synthetic-03', 'turn_id': 't0005', 'role': 'interviewer',
     'quote': 'Understood. Thank you for your time.'},
]


def main():
    corpus = [{'conversation_id': key, 'provenance': 'Wholly invented illustrative conversation.',
               'source_transcript_sha256': sha256(text.encode('utf-8')),
               'source_text': text, 'turns': parse_turns(text)} for key, text in EXAMPLES.items()]
    directory = Path(__file__).resolve().parent
    (directory / 'synthetic-conversations.jsonl').write_text(
        ''.join(json.dumps(row) + '\n' for row in corpus), encoding='utf-8')
    (directory / 'synthetic-evidence.json').write_text(json.dumps(EVIDENCE, indent=2) + '\n', encoding='utf-8')
    print('Wrote three invented conversations and ten illustrative evidence rows.')


if __name__ == '__main__':
    main()
