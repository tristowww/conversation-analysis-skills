"""Verify the real worked example against checksummed public source CSVs."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conversation_analysis.prepare import prepare, REVISION, SOURCES
from conversation_analysis.verify_evidence import verify


def check_sample(corpus, manifest, ledger):
    if manifest['source_revision'] != REVISION:
        raise ValueError('Worked example uses an unexpected release.')
    expected = [next(c for c in corpus if c['cohort'] == cohort and c['source_row'] == 1)
                for cohort in SOURCES]
    selected = manifest['selected']
    if [c['conversation_id'] for c in expected] != [c['conversation_id'] for c in selected]:
        raise ValueError('Selected interviews do not match the declared first-row rule.')
    for original, recorded in zip(expected, selected):
        actual_hash = hashlib.sha256(original['source_text'].encode('utf-8')).hexdigest()
        if (actual_hash != recorded['source_transcript_sha256'] or
                original['source_row'] != recorded['source_row'] or
                original['cohort'] != recorded['cohort'] or
                len(original['turns']) != recorded['turns']):
            raise ValueError('Sample provenance mismatch.')
    by_id = {c['conversation_id']: c for c in expected}
    evidence_ids = [e['evidence_id'] for e in ledger]
    if len(set(evidence_ids)) != len(evidence_ids):
        raise ValueError('Duplicate evidence ID.')
    for row in ledger:
        if row['conversation_id'] not in by_id:
            raise ValueError('Evidence comes from outside the declared sample.')
        if row['source_transcript_sha256'] != by_id[row['conversation_id']]['source_transcript_sha256']:
            raise ValueError('Evidence transcript hash mismatch.')
        if 'quote_start' not in row or 'quote_end' not in row:
            raise ValueError('Real-data evidence requires exact quote offsets.')
    verify(expected, ledger)
    return {'interviews': len(expected), 'complete_turns': sum(len(c['turns']) for c in expected),
            'evidence_rows': len(ledger)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / '.local-data/anthropic')
    args = parser.parse_args()
    # Re-read and checksum the original release, rather than trusting a prepared cache.
    corpus, _ = prepare(args.source)
    manifest = json.loads((ROOT / 'examples/anthropic-sample.json').read_text(encoding='utf-8'))
    ledger = json.loads((ROOT / 'examples/anthropic-evidence.json').read_text(encoding='utf-8'))
    print(json.dumps(check_sample(corpus, manifest, ledger)))
    print('Exact source evidence verified. Interpretations have not received independent human review.')


if __name__ == '__main__':
    main()
