import unittest

from conversation_analysis.response_lengths import word_count, describe, analyze


class ResponseLengthTests(unittest.TestCase):
    def test_apostrophes_and_empty_slots(self):
        self.assertEqual(word_count("It's useful; it\u2019s new. 42"), 5)
        self.assertEqual(word_count('...'), 0)
        self.assertEqual(describe([0, 1, 2, 3])['zero_word_messages'], 1)

    def test_upper_fence_is_strict_and_cases_are_retained(self):
        result = describe([10] * 19 + [100])
        self.assertEqual(result['upper_fence_words'], 10)
        self.assertEqual(result['messages_above_upper_fence'], 1)
        self.assertEqual(result['participant_messages'], 20)

    def test_invalid_or_thin_reference_set_rejected(self):
        for values in ([1, 2, 3], [0, 1, 2, -1], [0, 1, 2, True]):
            with self.assertRaises(ValueError):
                describe(values)

    def test_cohorts_and_speakers_not_pooled(self):
        corpus = [{'conversation_id': 'a', 'cohort': 'a', 'turns': [
            {'role': 'participant', 'turn_id': f't{i}', 'text': 'one'} for i in range(4)] +
            [{'role': 'interviewer', 'turn_id': 't9', 'text': 'word ' * 100}]},
            {'conversation_id': 'b', 'cohort': 'b', 'turns': [
                {'role': 'participant', 'turn_id': f't{i}', 'text': 'word ' * 10} for i in range(4)]}]
        result = analyze(corpus, {'a'})
        self.assertEqual(result['participant_messages'], 8)
        self.assertEqual(result['cohorts']['a']['median_words'], 1)
        self.assertEqual(result['cohorts']['b']['median_words'], 10)
        self.assertEqual(result['selected_interviews'][0]['maximum_words'], 1)
        with self.assertRaises(ValueError):
            analyze(corpus, {'missing'})


if __name__ == '__main__':
    unittest.main()
