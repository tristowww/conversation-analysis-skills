# One conversation, several research questions

Every conversation and quotation on this page is invented. The interpretations below are authored examples of applying the skills, not outputs from a measured AI run or independent human coding.

## Start with the dialogue

**Interviewer:** How are you using AI in your work?

**Participant:** I use it for first drafts of routine emails. It saves me time, but I still check every name and number.

**Interviewer:** What would make that process easier?

**Participant:** A one-page guide from IT showing which kinds of information we can put into the tool would help.

**Interviewer:** So you want AI to take over writing all your emails?

**Participant:** No. I want to keep reviewing them. My question is what information I can safely include.

Full invented input: [synthetic-conversations.jsonl](synthetic-conversations.jsonl), conversation `synthetic-01`.

## Keep the questions separate

| Skill | Illustrative interpretation | Evidence and qualification |
| --- | --- | --- |
| Topics | Routine email drafting, verification, and information-sharing guidance are candidate topics. | `T1`, `S1`, `I1`. These overlap in one interview; they do not represent three respondents. |
| Sentiment | The participant values time savings and qualifies that benefit with an ongoing need to verify details. | `S1`. Positive about speed; cautious about unchecked output. A task-specific scheme might code the broader assessment as mixed. |
| Respondent intent | The guide suggestion requests practical support; the final reply corrects the interviewer's interpretation. | `I1`, `X1`. A request for guidance does not imply a request for full automation. |
| Actionability | A guide about permitted information is a bounded proposal to investigate. | `I1`. The source names IT, but does not establish ownership, feasibility, policy, cost, or priority. |
| Interviewer interaction | The interviewer introduces full automation; the participant explicitly rejects that premise. | `X1`, including both speakers. The exchange supports a correction finding, not a claim that the interview caused disengagement. |

The [JSON evidence ledger](synthetic-evidence.json) links these claim IDs to exact source turns and speaker roles. An executable check verifies the quoted text. A researcher still needs to review the category definitions and interpretation.

## Two useful boundary cases

In `synthetic-02`, a participant describes a formula changing spreadsheet column names, the time spent locating the mismatch, and the availability of the original file. They explicitly have no solution to propose. This is still a bounded investigative lead (`A1`); actionability does not require a participant-designed fix.

In `synthetic-03`, "We should fix AI" provides too little detail for a bounded next step (`A2`). The later request to skip and stop is explicit, and the interviewer closes (`X2`). A change word does not establish specificity, and the request to stop does not establish why the participant wanted to end.

## Supporting outputs

**Example evidence synthesis:** The first two invented interviews illustrate different support needs: information-sharing guidance and investigation of a concrete output error. Both examples preserve a role for human review. They offer cases to inspect, not an estimate of how common either issue is.

**Example conversation editorial:** The participant in `synthetic-01` describes using AI to draft routine emails while checking names and numbers `[synthetic-01:t0002]`. They suggest guidance about what information can be entered `[synthetic-01:t0004]`. When the interviewer interprets this as a desire for full automation, the participant corrects that account and restates their concern about permitted information `[synthetic-01:t0005]` `[synthetic-01:t0006]`.

## Check the quotes

```bash
python -m conversation_analysis.verify_evidence --corpus examples/synthetic-conversations.jsonl --ledger examples/synthetic-evidence.json
```

Passing this check confirms the ten ledger rows' text and attribution. It does not validate the seven analysis methods or the judgments illustrated here.
