# Worked examples from real Anthropic interviews

Three participants describe useful applications of AI alongside output limitations, uncertainty, or unmet needs. Their accounts refer to sales-strategy generation, creative exploration and mixing tools, and machine-learning scoring. Those differences matter when interpreting a shared label such as "AI."

This is an **AI-assisted qualitative walkthrough of three real interviews**, applying the first seven skills on November 13, 2026. The [four additional worked examples](ADVANCED_ANTHROPIC_EXAMPLES.md) apply agent-user matching, conversational saturation, outlier review, and research-question coverage to the same interviews on November 14. The interpretations have not received independent human review.

## Sources and selection

Before reading the content, we selected the **first data row in each cohort** of the official [Anthropic Interviewer release](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer), pinned at revision `c9e1ec1e6b093712b9c42235c7303ece647490e9`.

| Case | Public source record | Complete turns read |
| --- | --- | --- |
| W: workforce | `workforce:work_0000` | 27 |
| C: creatives | `creatives:creativity_0000` | 21 |
| S: scientists | `scientists:science_0000` | 21 |

All 69 turns, including both speakers, were read before interpreting the cases. This deterministic convenience sample supports examples, not population estimates, cohort comparisons, or thematic saturation. No fixed topic taxonomy was supplied.

The [sample manifest](anthropic-sample.json) records the selection rule, source rows, and transcript hashes. Evidence codes such as **W08** refer to the [exact-quote ledger](anthropic-evidence.json): W08 is workforce turn `t0008`, C14 is creative turn `t0014`, and S18 is scientist turn `t0018`. Each ledger row identifies speaker, quote offsets, and transcript hash. Full interviews remain in the local reproduction package.

## 1. Topic analysis

Candidate topics may overlap within an interview. They are proposed categories for these cases, not a validated taxonomy.

| Candidate topic | Definition and boundary | Supporting evidence and contrast |
| --- | --- | --- |
| Getting help with a work task | Developing ideas or supporting a task. Excludes claims of measured performance improvement. | W describes sales-strategy help when stuck (W04, W06, W12). C describes brainstorming and support tasks (C06, C08). S describes scoring and data evaluation (S06, S08), a different technical application. |
| Qualifying the reported benefit | Modifying output, limiting a positive claim, or acknowledging uncertain downstream effects. | W modifies repetitive or irrelevant strategies (W08). C enjoys exploration but is unsure whether learning has reached the work (C10, C12, C14). S reports useful segmentation (S12), without accuracy results. |
| Anticipated changes and unmet needs | Explicit future hopes, concerns, or desired capabilities. Keep concerns and requests as separate subcategories. | W hopes for general improvement (W24). C worries about music-platform saturation (C16). S names understandable transparency and drift monitoring (S18). These passages have different levels of specificity. |

The first topic groups practical uses without equating sales brainstorming, composing, and machine-learning scoring. No topic frequencies are estimated.

## 2. Sentiment analysis

For this walkthrough, `positive` means a favorable expressed evaluation, `negative` an unfavorable one, `mixed` both toward the stated target, and `insufficient` no defensible evaluation of that target.

| Target and case | Provisional judgment | Evidence and qualification |
| --- | --- | --- |
| AI sales-strategy output, W | Mixed | "Sometimes they're repetitive or not relevant for my work. However, I still use the overall strategy." (W08) A later satisfied account concerns one reported event (W18), not a verified causal effect. |
| AI-assisted creative exploration, C | Positive | "It was fun but also it helped me refine my own perspective somewhat." (C12) This was not a client project (C10). |
| Possible music-platform saturation, C | Negative/concerned | "I also am pretty concerned about how AI generated music might impact streaming platform saturation." (C16) This is a different target from the positive exploration experience. |
| Realized effect on compositions, C | Insufficient | The participant does not know whether the learning has reached the work (C14). An expectation is not an achieved outcome. |
| Usefulness of a scoring metric for segmentation, S | Positive | The participant calls a singular metric helpful (S12). Workflow usefulness does not establish model accuracy. |

Keeping targets separate preserves the creative participant's favorable experience and industry concern instead of assigning the whole person one sentiment.

## 3. Respondent intent analysis

These illustrative, non-exclusive codes describe observable communication: `account`, `evaluation`, `qualification`, `concern`, `suggestion`, and `closure`. They do not describe private motives.

| Passage | Function and elicitation | Rationale or boundary |
| --- | --- | --- |
| W04 and W06 | Account; interviewer-invited | Describes infrequent use and scenario-based prompting. Does not establish a request for automation. |
| W08 | Evaluation + account; interviewer-invited | Answers whether strategies are used as-is, then describes modifications and limitations. |
| C14 | Qualification; interviewer-invited | Answers a question about changes while preserving uncertainty about realized effects. |
| C16 | Concern; interviewer-invited | Follows an explicit invitation to discuss concerns. It is not an unprompted complaint. |
| S18 | Suggestion/desired capability; interviewer-invited | Follows a hypothetical "magic wand" question. It is an elicited wish, not an approved product requirement. |
| W26 | Closure; interviewer-invited | "No, that is all." answers an invitation to add anything else. Brevity does not establish disengagement. |

## 4. Actionability analysis

Here, `bounded response` means enough information to frame a specific response or investigation; `clarification needed` identifies a target with consequential details missing; `broad feedback` lacks a concrete next step. These judgments assess information, not priority.

| Evidence | Provisional category | Supported next inquiry and missing information |
| --- | --- | --- |
| S18: "A tool for model transparency that can be easily understood by the medical team and also allows for the operations team to monitor for model drift." | Bounded response | **Analyst proposal:** investigate transparency and monitoring requirements with the named user groups. Owner, current tools, success criteria, feasibility, budget, and implementation plan remain unknown. |
| W08: repetitive or irrelevant strategies | Clarification needed | **Analyst proposal:** ask for a concrete input/output example and the edits that made it usable. A reproducible failure and root cause remain unknown. |
| C16: anticipated platform saturation | Clarification needed | **Analyst proposal:** clarify which observed situations or platform practices inform the concern. This supports investigation, not a prescribed intervention. |
| W24: general hope that AI improves | Broad feedback | Names a desired direction without a bounded change. It does not establish which capability to prioritize. |

## 5. Interviewer interaction analysis

The preceding participant turn, interviewer move, and actual next participant reply were reviewed for each window. Observable function is separate from question quality or causal effect.

| Exchange | Observable sequence | Interpretation and limit |
| --- | --- | --- |
| W06 -> W07 -> W08 | Participant describes prompting for a strategy; interviewer asks whether output is used as-is or modified; participant reports modification and limitations. | A follow-up obtains an elaborated account in this exchange. It does not prove improved interview quality. |
| C14 -> C15 -> C16 | Participant is unsure whether learning has affected the work; interviewer says it "will eventually feed into your compositions," then asks about concerns; participant describes industry concerns. | The reflection makes eventual benefit sound more certain than the participant established. The next reply does not confirm that benefit. |
| S12 -> S13 -> S14 | Participant reports useful segmentation; interviewer adds "potentially more accurate," then asks why AI was not used elsewhere; participant discusses medical-team involvement. | The accuracy possibility belongs to the interviewer. The following reply does not establish accuracy. Later reported back-testing (S16) supplies no methods or results sufficient to resolve it. |

These observations concern language and local sequences, not interviewer motives, a full quality rating, or effects on participants.

## 6. Evidence synthesis

**The participants describe different forms of assistance.** W seeks sales-strategy ideas; C uses tools for creative exploration, support tasks, and machine-learning mixing plugins; S describes machine-learning scoring (W04, W06, C06, C08, C10, S06, S08). A single "AI use" category would hide those differences.

**Reported usefulness needs qualifications.** W modifies imperfect output and reports satisfaction with one event (W08, W18). C values exploration while remaining unsure about its realized effects on work (C12, C14). S describes helpful segmentation without a performance evaluation (S12, S16). These accounts do not establish comparative tool effectiveness.

**The evidence supports different next questions.** The scientist's transparency and monitoring wish is more specific than the workforce participant's general hope for improvement (S18, W24). The creative participant's concern addresses an industry setting (C16). This illustrates actionability; three selected records cannot establish which need is most common or important.

## 7. Conversation editorials

**W:** The participant describes infrequent AI use for sales ideas and says they modify strategies that can be repetitive or irrelevant (W04, W06, W08). They report giving context upfront rather than having much back-and-forth (W14). They describe satisfaction with one sales experience and attribute a difference to detailed context (W18, W20); this is their account, not independently measured performance. Their future hope is general improvement (W24).

**C:** The participant describes brainstorming, support uses, and machine-learning mixing plugins, including a film-score analysis outside client work as one example of their exploration (C06, C08, C10). They found that exploration enjoyable and helpful to refining their perspective, but do not know whether the learning has appeared in their work (C12, C14). They express concern about music-platform saturation and uncertainty about how their own use will evolve (C16, C18). The interviewer's expectation of eventual creative benefit retains its interviewer attribution (C15).

**S:** The participant describes machine-learning scoring and data evaluation, tentatively attributing adoption to investor expectations while reporting useful segmentation (S06, S08, S10, S12). They describe preserving medical-team involvement and report historical back-testing without performance details (S14, S16). They ask for understandable model transparency and drift monitoring (S18). The interviewer introduces a possible accuracy benefit that the participant has not established (S13).

Every parenthesized code resolves to a conversation, speaker, turn, and exact excerpt in the evidence ledger. Full-source transcript hashes are in the sample manifest. These short derived accounts omit some detail and supplement the source interviews.

## Reproduce the source checks

```bash
python -m conversation_analysis.prepare --download
python scripts/check_anthropic_example.py
python -m conversation_analysis.verify_evidence --corpus .local-data/prepared.jsonl --ledger examples/anthropic-evidence.json
```

The checks verify source-file checksums, first-row selection, transcript hashes, 37 quoted passages across both walkthroughs, speaker attribution, and quote offsets. They do not independently validate the interpretations. The original [synthetic boundary cases](SYNTHETIC_CHECKS.md) remain as code-test examples.

**Attribution:** Selected excerpts from Anthropic Interviewer, Handa et al. (2025), under the source card's CC-BY data statement (version unstated). See [data provenance and changes](../docs/DATA.md) and the [official research article](https://www.anthropic.com/research/anthropic-interviewer). Analysis and coding are newly authored with AI assistance; no publisher endorsement or independent human review is claimed.
