---
name: learn-video
description: "Decode a YouTube video, transcript, talk, lecture, podcast, or interview into speaker context, worldviews, limits, applications, and optional Brain2 atoms."
---

# Learn Video

Use this skill when the user gives a YouTube URL, transcript, podcast interview, talk, lecture, or asks to learn from a speaker.

## Required References

Before running a serious decode, read:

- `../../references/source-policy.md`
- `../../references/output-contracts.md`
- `../../references/brain2-vault-contract.md` when Brain2 storage or comparison is requested.
- `../../references/quality-rubric.md` before final handoff.

## Phase 1: Source Capture

Collect the best available evidence:

1. Metadata: URL, title, channel, upload date, description, and oEmbed author identity when possible.
2. Transcript: prefer user-provided transcript; otherwise try available transcript tools, browser transcript panel, `yt-dlp` captions, or official podcast/transcript pages.
3. Speaker context: search reliable web sources when the speaker is not already known from provided context.

If transcript capture fails, stop and ask for transcript or a summary. Do not continue as if the full talk was read.

Useful helper:

```bash
python3 /Users/rio/plugins/youtube-learning/scripts/youtube_learning.py oembed "https://www.youtube.com/watch?v=..."
```

## Phase 2: Speaker Portrait

Write a short but grounded speaker portrait:

- Full name, nationality when known, current role, core field.
- Top 3-5 concrete achievements.
- What makes the speaker unusual among strong peers.
- One representative quote only if sourced.
- Why this person is worth listening to for this topic.
- Context of the appearance: who they spoke with, where, and why that context matters.

Do not guess biographical facts. Mark unknowns.

## Phase 3: Belief Archaeology

Choose at most 3 worldviews. For each worldview, use this exact structure:

### Worldview #[N]: [short name]

**Surface evidence**

> "[English quote]"
> -> "[Vietnamese close translation]"

Explain what the speaker said, decided, or noticed in context.

**Hidden belief**

Write one Vietnamese sentence that is simple enough to remember after one reading. Avoid abstract philosophy language.

**Why this belief must be true in their head**

Explain what assumption underneath the quote makes the claim coherent. State what mainstream belief it rejects.

**True when**

Give 2 concrete examples that a high-school student can understand.

**False when**

Give 1-2 cases where applying this worldview would create bad results.

**Application for Thong Phan or the user**

Give one specific action in one domain: influence, persuasion, content, learning, product, or life.

## Phase 4: Synthesis

Provide:

- A table of the 3 core beliefs and their clearest behavior.
- Contrast with mainstream thinking.
- Internal tension: what contradiction exists inside the worldview and how the speaker handles it.

## Phase 5: Brain2 Check

When Brain2 is relevant and tools are available, search Brain2 for:

- Reinforcing ideas.
- Contradicting ideas.
- Extensions.
- Personal stories or prior decisions that make the worldview usable.

Classify each match as reinforce, contradiction, extension, or new.

## Phase 6: Reflection Questions

End with 3 questions:

1. What in this worldview feels uncomfortable?
2. If this worldview were fully adopted, what would change first?
3. Where is this worldview wrong or incomplete?

Ask which worldview the user wants to save to the Worldview Library.

## Phase 7: Atomization

If saving is requested:

- Draft or update Speaker Profile automatically.
- Ask before saving Worldview Library atoms unless the user explicitly asked to save all.
- Follow `../../references/brain2-vault-contract.md`.

## QA Checklist

- At most 3 worldviews.
- Each worldview has surface evidence, hidden belief, true cases, false cases, and application.
- Hidden belief is plain Vietnamese, not academic jargon.
- English quotes have Vietnamese close translation.
- Speaker facts are sourced or marked unknown.
- Transcript gaps are disclosed.
- Brain2 availability and result boundary are stated.

