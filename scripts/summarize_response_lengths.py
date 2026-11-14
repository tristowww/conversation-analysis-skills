"""Reproduce corpus length aggregates and review flags for selected interviews."""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conversation_analysis.prepare import prepare, REVISION
from conversation_analysis.response_lengths import analyze


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Compare with the committed output without rewriting it.')
    args = parser.parse_args()
    corpus, _ = prepare(ROOT / '.local-data/anthropic')
    manifest = json.loads((ROOT / 'examples/anthropic-sample.json').read_text(encoding='utf-8'))
    result = analyze(corpus, {c['conversation_id'] for c in manifest['selected']})
    result['source_revision'] = REVISION
    output = ROOT / 'results/response-length-review.json'
    if args.check:
        if json.loads(output.read_text(encoding='utf-8')) != result:
            raise ValueError('Committed response-length diagnostic does not match the pinned source.')
    else:
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
