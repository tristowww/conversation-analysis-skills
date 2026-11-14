# Conversation Analysis Skills

**How can an AI-assisted analyst study a conversation without losing who said what, the surrounding context, or the limits of the evidence?**

This project separates five questions: what participants discuss, how they evaluate it, what their statements do, what the feedback supports, and how the interviewer responds. Each question has a reusable Markdown skill with an explicit output and review criteria.

The public-data workflow uses [Anthropic's public Interviewer dataset](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer). It downloads a pinned release, verifies checksums, preserves both speakers, and prepares source-linked turns for analysis. The worked interpretations use **invented conversations**, so you can inspect the method without publishing a participant's words.

**[Read a worked example](examples/WORKED_EXAMPLE.md)** · [Choose a skill](#analysis-skills) · [Run with public data](docs/RUN_GUIDE.md) · [Data and attribution](docs/DATA.md) · [Actual checks and limits](docs/STATUS.md)

## Analysis skills

| Skill | Question it answers |
| --- | --- |
| [Topics](skills/topic-analysis/SKILL.md) | What are participants discussing, and where do candidate themes overlap? |
| [Sentiment](skills/sentiment-analysis/SKILL.md) | How does a participant evaluate a particular experience or practice? |
| [Respondent intent](skills/respondent-intent-analysis/SKILL.md) | Is the participant describing, questioning, praising, objecting, or requesting something? |
| [Actionability](skills/actionability-analysis/SKILL.md) | What response or investigation does the information support, and what is missing? |
| [Interviewer interaction](skills/interviewer-interaction-analysis/SKILL.md) | What does the interviewer do, and how does the participant respond in the next turn? |

Two supporting skills cover [evidence synthesis](skills/evidence-synthesis/SKILL.md) across conversations and a [conversation editorial](skills/conversation-editorial/SKILL.md) for a source-linked prose account of one interview.

These are instructions for an analyst or file-capable AI assistant. Python handles data preparation and evidence checks; it does **not** assign these qualitative labels. No provider, API key, model SDK, or automatic skill installation is required.

## Try the example

Python 3.10 or later; standard library only. Run from the repository root:

```bash
python -m unittest discover -s tests -v
python -m conversation_analysis.verify_evidence --corpus examples/synthetic-conversations.jsonl --ledger examples/synthetic-evidence.json
```

Then read the [synthetic worked example](examples/WORKED_EXAMPLE.md). It shows why a positive evaluation, a specific request, and a useful investigative lead need separate judgments. The accompanying ledger checks exact text and speaker attribution, not whether an interpretation is correct.

## Prepare the Anthropic interviews

```bash
python -m conversation_analysis.prepare --download
```

This command downloads and checks three CSV files, then writes:

- `.local-data/prepared.jsonl`: full conversations, both speakers, exact turn spans, source rows, and transcript hashes. This stays local and ignored by Git.
- `results/data-audit.json`: aggregate corpus and parsing checks, without participant text or transcript identifiers.

The initial run prepared **1,250 interviews, 30,240 messages, and 14,495 participant messages**. It retained 17 empty or whitespace-only message bodies as source-quality information rather than silently dropping them. These are structural counts, not findings about participant views.

Follow the [run guide](docs/RUN_GUIDE.md) to apply a chosen skill using your own authorized assistant and to verify its evidence ledger. The command above does not send interviews to a model or generate research findings.

## What the project demonstrates

- Separating related research questions rather than treating all conversation analysis as topic extraction.
- Preserving participant statements, interviewer prompts, uncertainty, and corrections.
- Building a reproducible bridge from a public transcript release to inspectable analysis inputs.
- Checking quotations and attribution independently of the analyst's prose.

The initial release includes a fresh full-corpus **preparation audit** and synthetic worked interpretations. It does not include a model comparison, human-coded reference set, or demonstrated improvement from using a skill. See [status and limitations](docs/STATUS.md).

## Scope and provenance

This standalone portfolio edition uses general qualitative-analysis methods and public research data. It contains no employer systems, employee-feedback corpus, private prompts, or internal study protocols. The instructions, examples, and implementation were prepared with AI assistance and are offered as research prototypes. The synthetic annotations are authored illustrations, not observed model performance or independent human ratings.

Anthropic released the source interviews; this is an independent project with attribution and no claimed endorsement. Raw public transcripts and participant identifiers are not redistributed here. Data licensing is described separately in [DATA.md](docs/DATA.md); this repository does not assign a new license to the source dataset.
