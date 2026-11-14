"""Prepare a pinned public interview release; no model or qualitative coding."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request

REVISION = 'c9e1ec1e6b093712b9c42235c7303ece647490e9'
BASE = 'https://huggingface.co/datasets/Anthropic/AnthropicInterviewer'
SOURCES = {
    'workforce': (1000, '09ff307d42ebc8ed0b0ba25f41ffe2e50e9baa0b3c1ab4133ee528118817aab4'),
    'creatives': (125, 'd4e865b9959671990ceb51089c7494dbeed7560f9a623da873e6eb0f1b6506b4'),
    'scientists': (125, '338677e4a4ec17824cb5bfbc9242c8a37e7041157d34fb65e7e6fb58ea3f407a'),
}
MARKER = re.compile(r'^(Assistant|AI|User):[ \t]*', re.MULTILINE)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def verify_bytes(raw: bytes, expected: str) -> None:
    if sha256(raw) != expected:
        raise ValueError('Source checksum mismatch; refusing to prepare changed data.')


def parse_turns(text: str) -> list[dict]:
    markers = list(MARKER.finditer(text))
    if not markers or text[:markers[0].start()].strip():
        raise ValueError('Transcript has an unrecognized opening speaker label.')
    turns = []
    for index, match in enumerate(markers):
        start = match.end()
        end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        # Retain offsets into the exact CSV text; remove only separator newlines.
        while end > start and text[end - 1] in '\r\n':
            end -= 1
        turns.append({
            'turn_id': f't{index + 1:04d}',
            'role': 'participant' if match.group(1) == 'User' else 'interviewer',
            'source_role': match.group(1),
            'text': text[start:end],
            'source_start': start,
            'source_end': end,
        })
    return turns


def download(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for cohort, (_, expected) in SOURCES.items():
        path = directory / f'{cohort}.csv'
        url = f'{BASE}/resolve/{REVISION}/interview_transcripts/{cohort}_transcripts.csv'
        raw = path.read_bytes() if path.exists() else urllib.request.urlopen(url, timeout=60).read()
        verify_bytes(raw, expected)
        path.write_bytes(raw)


def prepare(source: Path) -> tuple[list[dict], dict]:
    corpus, seen = [], set()
    report = {
        'dataset': 'Anthropic/AnthropicInterviewer', 'revision': REVISION,
        'scope': 'Source integrity and structural preparation only; no qualitative labels.',
        'cohorts': {}, 'sources': [],
        'parser_limits': [
            'A line-start speaker label inside a quoted response can be ambiguous.',
            'Structural checks do not establish speaker accuracy or substantive validity.',
        ],
    }
    for cohort, (expected_count, expected_hash) in SOURCES.items():
        raw = (source / f'{cohort}.csv').read_bytes()
        verify_bytes(raw, expected_hash)
        reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''))
        if not {'transcript_id', 'text'}.issubset(reader.fieldnames or []):
            raise ValueError('Missing required CSV columns.')
        counts = Counter()
        for row_number, row in enumerate(reader, 1):
            source_id, text = row['transcript_id'], row['text']
            if not source_id or not text:
                raise ValueError('Missing transcript ID or text.')
            key = f'{cohort}:{source_id}'
            if key in seen:
                raise ValueError('Duplicate conversation ID within cohort.')
            seen.add(key)
            turns = parse_turns(text)
            corpus.append({
                'conversation_id': key, 'cohort': cohort,
                'source_row': row_number, 'source_revision': REVISION,
                'source_file_sha256': expected_hash,
                'source_transcript_sha256': sha256(text.encode('utf-8')),
                'source_text': text, 'turns': turns,
            })
            counts['conversations'] += 1
            counts['messages'] += len(turns)
            counts['participant_messages'] += sum(t['role'] == 'participant' for t in turns)
            counts['interviewer_messages'] += sum(t['role'] == 'interviewer' for t in turns)
            counts['empty_messages'] += sum(not t['text'].strip() for t in turns)
            counts['empty_participant_messages'] += sum(
                t['role'] == 'participant' and not t['text'].strip() for t in turns)
            counts['conversations_with_consecutive_same_role'] += any(
                a['role'] == b['role'] for a, b in zip(turns, turns[1:]))
            for turn in turns:
                if text[turn['source_start']:turn['source_end']] != turn['text']:
                    raise ValueError('Turn offset integrity failure.')
        if counts['conversations'] != expected_count:
            raise ValueError('Unexpected cohort size for pinned release.')
        report['cohorts'][cohort] = dict(counts)
        report['sources'].append({
            'cohort': cohort, 'sha256': expected_hash, 'bytes': len(raw),
            'url': f'{BASE}/resolve/{REVISION}/interview_transcripts/{cohort}_transcripts.csv',
        })
    report['conversations'] = len(corpus)
    report['messages'] = sum(c['messages'] for c in report['cohorts'].values())
    report['participant_messages'] = sum(c['participant_messages'] for c in report['cohorts'].values())
    report['interviewer_messages'] = sum(c['interviewer_messages'] for c in report['cohorts'].values())
    report['empty_messages'] = sum(c['empty_messages'] for c in report['cohorts'].values())
    report['duplicate_conversation_ids'] = 0
    report['exact_turn_spans_verified'] = True
    return corpus, report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--source', type=Path, default=Path('.local-data/anthropic'))
    parser.add_argument('--output', type=Path, default=Path('.local-data/prepared.jsonl'))
    parser.add_argument('--audit', type=Path, default=Path('results/data-audit.json'))
    args = parser.parse_args()
    if args.download:
        download(args.source)
    corpus, report = prepare(args.source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.audit.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in corpus), encoding='utf-8')
    args.audit.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('conversations', 'messages', 'participant_messages', 'empty_messages')}))


if __name__ == '__main__':
    main()
