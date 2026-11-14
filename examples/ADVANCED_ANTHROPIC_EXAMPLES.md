# Matching, saturation, outliers, and question coverage

These four worked examples extend the [original seven-skill walkthrough](ANTHROPIC_WORKED_EXAMPLE.md) using the **same three real Anthropic interviews**. The sample was selected before the original reading and is unchanged. All 69 turns were read again for this extension. There is no new semantic sample or independent human rating.

The [sample manifest](anthropic-sample.json) records the dates, scope, and selection. Evidence codes below resolve to the [37-row source ledger](anthropic-evidence.json), with exact text, role, turn, offsets, and transcript hash. Short excerpts remain under the publisher's CC-BY data statement; attribution and changes are in [DATA.md](../docs/DATA.md).

## 8. Agent-user behavioral matching

The [matching skill](../skills/agent-user-behavioral-matching/SKILL.md) separates linguistic reuse from behavior that responds to an expressed need. We inspect direction and meaning preservation rather than treating similarity as a success score.

| Source-linked window | Direction and feature | Observation | What remains unknown |
| --- | --- | --- | --- |
| C14 -> C15 -> C16 | Agent responding to user; terminology and qualification | The participant calls their learning "bucket filling" and is unsure whether it has appeared in the work. The agent echoes the term, then says the knowledge "will eventually feed into your compositions." The next answer concerns industry risks. | Local lexical matching is visible. The reflection strengthens the participant's expectation; it does not establish that the stronger claim was accepted. Rapport, helpfulness, and creative outcomes are unmeasured. |
| W13 -> W14 | User responding to agent; reuse of an offered interaction description | The agent offers back-and-forth versus upfront context. The participant answers with upfront context and says they do not usually go back and forth. | The answer reuses offered language, but this is also a direct response to supplied options. It does not establish spontaneous style accommodation or a general preference for shorter interview questions. |
| S12 -> S13 -> S14 | Agent responding to user; technical concept reuse and added premise | The agent retains the participant's single-metric idea but adds a possible accuracy benefit. The next response addresses medical-team involvement. | Concept reuse does not establish faithful adaptation: the accuracy possibility is interviewer-authored. No reported user preference licenses the added claim. |

These local observations do not estimate conversation-wide matching. The text does not supply voice, gaze, response latency, or an independent baseline for linguistic convergence. Whether the agent appropriately adapts its level of detail to each person's preference remains unresolved.

## 9. Conversational saturation

The [saturation skill](../skills/conversational-saturation/SKILL.md) tracks what later turns add to a stated question. Here the question concerns AI use, experiences, and desired changes. A contribution can refine meaning without adding a new topic label.

| Window | Information already present | Contribution of the later participant turn | Review judgment |
| --- | --- | --- | --- |
| W18 -> W19 -> W20 | A positive sales anecdote and reported satisfaction. | After a probe about what differed, the participant describes detailed context and personalization. | Adds a participant-proposed explanation. It is relevant new detail, not evidence that personalization caused the reported result. |
| C10 -> C11 -> C12 | A film-score analysis outside client work. | After a question about who drove the insights, the participant describes their own perspective, supplied articles, and suggested connections. | Adds information about contribution and experience within the same activity. |
| C12 -> C13 -> C14 | Enjoyable exploration and a refined perspective. | Asked about changes to work, the participant is unsure whether the learning has appeared in it. | Adds a consequential qualification. Counting only new themes would miss this information gain. |
| S16 -> S17 -> S18 | A brief report of historical back-testing. | A later hypothetical invitation elicits a specific wish for understandable transparency and drift monitoring. | A short earlier answer does not imply exhaustion. The later turn adds an unmet need on a new topic; it does not establish saturation of the earlier validation topic. |
| W24 -> W25 -> W26 | General future hope; an invitation to add anything else. | The participant says, "No, that is all." | No additional substantive information appears, and closure is explicit. This supports ending the observed exchange, not a claim that every possible probe would yield nothing. |

No fixed saturation threshold or automatic stop rule is inferred. The sample cannot establish thematic saturation across interviews. An explicit wish to stop would take precedence over an analyst's desire for more information.

## 10. Outlier and contrasting-case analysis

The [outlier skill](../skills/outlier-analysis/SKILL.md) keeps a measurement flag separate from a substantive exception or a source problem.

### A. A reproducible statistical review screen

Before computing the diagnostic, the extension plan specified participant-message word counts, **within each publisher cohort**, with inclusive quartiles and a strict upper fence of `Q3 + 1.5 * IQR`. Zero-word slots are retained. The [output](../results/response-length-review.json) records the tokenizer, aggregate counts, selected-case checks, and limitations.

| Reference cohort | Participant messages | Median words | Upper fence, words | Messages above fence |
| --- | ---: | ---: | ---: | ---: |
| Workforce | 12,076 | 53 | 178.5 | 443 |
| Creatives | 1,259 | 69 | 233 | 32 |
| Scientists | 1,160 | 58 | 215 | 34 |

In the three selected interviews, maximum participant-message lengths are **46, 50, and 47 words**, respectively. None crosses its cohort's upper fence. We retain that result rather than selecting a new case merely to produce a flag. The 509 corpus-wide flags identify messages for possible review; their meanings have not been inspected in this walkthrough.

This screen is descriptive. It does not control for question function or conversation position, and turns are dependent within interviews. No flagged response is deleted or labeled disengaged, inaccurate, or low quality. The scan covers all 1,250 interviews numerically; semantic reading remains limited to the selected three.

### B. Cases that challenge an interpretation

| Interpretation to examine | Contrasting evidence | Revised interpretation and disposition |
| --- | --- | --- |
| The scientist adopted the method because of expected technical superiority; the interviewer's question invites that explanation (S09). | The participant says adoption was "likely" driven by investor expectations (S10), while later describing useful segmentation (S12). | Keep the tentative account of adoption separate from reported usefulness. It neither proves investor motives nor establishes comparative accuracy. Retain the case and the uncertainty. |
| A positive account of creative exploration establishes a realized effect on compositions. | The participant describes a useful experience but remains unsure about changes to the work (C12, C14). | Limit the positive claim to the reported experience and perspective. Do not infer demonstrated client-work outcomes. Retain the qualification. |

These are countercases to an interpretation, not claims that the speakers are unusual people or that their accounts are rare in the corpus. Neither requires a numerical outlier flag.

## 11. Research-question coverage and response quality

The [coverage skill](../skills/research-question-coverage/SKILL.md) starts with a goal source. The high-level goals below paraphrase the publisher's [Research goals section](https://www.anthropic.com/research/anthropic-interviewer#research-goals). The operational subquestions are authored for this walkthrough, not an unpublished Anthropic rubric. We use contribution descriptions rather than a numerical quality score.

| Public goal and analyst-authored subquestion | Relevant participant evidence and elicitation | Contribution and remaining limit |
| --- | --- | --- |
| Workforce: use and interaction patterns. **How and when does this participant use AI?** | W04, W06, W12, W14 describe frequency, scenario prompting, a trigger, and interaction pattern. W13 supplies explicit alternatives. | Direct relevant evidence. The account is prompted and self-reported; no usage log verifies frequency or effectiveness. |
| Workforce: preferences and evolving relationship. **What does the participant prefer to retain or change?** | W10 reports no task they prefer to do alone if AI can help; W16 describes colleagues' influence; W22 describes working with AI; W24 supplies a broad future hope. | Evidence located, including contextual variation. These answers do not define a detailed feature requirement or prove a stable preference outside this interview. |
| Creatives: integration into process. **Where do tools fit, and what did the participant contribute?** | C06, C08, C10 describe uses and an example; C11 asks about contribution, followed by C12. | Direct examples with participant involvement. The described example is outside client work, so its scope should remain explicit. |
| Creatives: experienced impact and future roles. **What benefits, concerns, or uncertainties are expressed?** | C12 reports a favorable experience. C13 asks about change; C14 qualifies realized impact. C16 and C18 cover concern and uncertain expectations. | Relevant qualification is useful evidence, not a failed answer. Realized effects on compositions remain unresolved; industry concern and personal benefit have different targets. |
| Scientists: patterns and perceived value. **Where was AI used, and what was the reason and value described?** | S06 and S08 describe use; S09 asks why the method seemed better; S10 gives a tentative alternative explanation; S12 describes usefulness. | Brief S10 directly addresses the decision question, despite challenging its premise. Neither that attribution nor the performance claim is independently verified. |
| Scientists: trust and barriers. **What validation, human-role constraint, or unmet need is described?** | S14 describes team involvement. S15 asks about validation; S16 names a method. S17 invites a desired capability; S18 names transparency and monitoring. | Relevant but incomplete for assessing reliability: results, methods, and acceptance criteria are absent. A further reliability assessment would need more evidence; this is not proof the participant or study failed. |

The matrix identifies evidence for these operational questions. It does not certify exhaustive coverage of the publisher's broad study goals. Fluency, agreement, response length, and a confident interviewer summary are not substitutes for relevant participant evidence.

## Reproduce the checks

```bash
python -m conversation_analysis.prepare --download
python scripts/check_anthropic_example.py
python scripts/summarize_response_lengths.py --check
python -m unittest discover -s tests -v
```

Source checks verify quotations, speakers, offsets, record hashes, and frozen sample selection. The numeric check reproduces the declared screen from the checksummed CSVs. These checks do not independently validate the interpretations or establish that adding a skill improves analysis. [Method references](../docs/METHOD_REFERENCES.md) explain the distinctions behind the four skills.
