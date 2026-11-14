"""Descriptive word-count review flags; never an engagement classifier."""
from collections import defaultdict
import re
import statistics

WORD = re.compile(r"\b\w+(?:['\u2019]\w+)*\b", re.UNICODE)


def word_count(text):
    return len(WORD.findall(text))


def describe(counts):
    if len(counts) < 4:
        raise ValueError('At least four messages are needed for this descriptive quartile rule.')
    if any(type(x) is not int or x < 0 for x in counts):
        raise ValueError('Word counts must be nonnegative integers.')
    q1, median, q3 = statistics.quantiles(counts, n=4, method='inclusive')
    fence = q3 + 1.5 * (q3 - q1)
    return {'participant_messages': len(counts), 'zero_word_messages': counts.count(0),
            'q1_words': q1, 'median_words': median, 'q3_words': q3,
            'upper_fence_words': fence, 'messages_above_upper_fence': sum(x > fence for x in counts)}


def analyze(corpus, selected_ids):
    groups = defaultdict(list)
    for c in corpus:
        groups[c['cohort']].extend(word_count(t['text']) for t in c['turns'] if t['role'] == 'participant')
    summaries = {cohort: describe(values) for cohort, values in sorted(groups.items())}
    selected = []
    found = set()
    for c in corpus:
        if c['conversation_id'] not in selected_ids:
            continue
        found.add(c['conversation_id'])
        rows = [{'turn_id': t['turn_id'], 'words': word_count(t['text'])}
                for t in c['turns'] if t['role'] == 'participant']
        fence = summaries[c['cohort']]['upper_fence_words']
        selected.append({'conversation_id': c['conversation_id'], 'cohort': c['cohort'],
                         'participant_messages': len(rows),
                         'maximum_words': max((r['words'] for r in rows), default=None),
                         'upper_fence_flags': [r for r in rows if r['words'] > fence]})
    if found != set(selected_ids):
        raise ValueError('A selected interview is missing from the corpus.')
    return {'method': 'Participant message words; inclusive quartiles within cohort; strictly above Q3 + 1.5 * IQR.',
            'tokenizer': WORD.pattern, 'conversations': len(corpus),
            'participant_messages': sum(len(v) for v in groups.values()),
            'zero_word_slots_retained': True, 'cohorts': summaries, 'selected_interviews': selected,
            'limits': ['Descriptive review flags, not errors or engagement/quality labels.',
                       'Turns are dependent within interviews; no significance tests are performed.',
                       'Question function and turn position are not matched by this simple screen.',
                       'Only the three selected interviews received qualitative reading; length screening does not extend semantic coverage.']}
