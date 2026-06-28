---
name: index
description: "Route YouTube Learning requests: decode YouTube videos into worldviews, analyze speakers, discover credible videos for an article, and prepare Brain2 learning atoms."
---

# YouTube Learning Router

Use this skill when the user invokes `@YouTube Learning`, mentions `/youtube-learn`, `/Youtube-learning`, `/youtube-discover`, gives a YouTube link for learning, or asks for credible YouTube videos to support an article or thesis.

## Plugin Purpose

YouTube Learning turns video into durable understanding. It treats a transcript as evidence, not the final product. The goal is to extract:

1. Speaker context: who is speaking, why they are credible, and what situation shaped the talk.
2. Surface claims: what was actually said, with quotes and timestamps when available.
3. Hidden beliefs: the worldview that makes those claims feel natural to the speaker.
4. Limits: where the worldview works, where it breaks, and what it misses.
5. Application: how the learning can change action, content, persuasion, or personal operating principles.
6. Reuse: Brain2 notes, worldview atoms, article angles, or a curated video library when appropriate.

## Routing

Route to the smallest focused skill:

- `learn-video`: decode a YouTube video, talk, lecture, podcast, interview, transcript, or speaker worldview.
- `discover-videos`: find credible YouTube videos for an article, draft, thesis, lesson, or content idea.

## Borrowed Design Patterns

From Product Design:

- Router first, focused skills second.
- Confirm the brief when the requested output is ambiguous.
- Keep source capture, analysis, synthesis, QA, and handoff as distinct phases.

From Build Web Apps:

- Use explicit contracts, scripts, and verification checks instead of one-off prose.
- Prefer repeatable local artifacts for serious work.
- Report pass/fail evidence instead of vague completion claims.

## Hard Rules

- Do not fabricate transcripts, quotes, speaker biography, channel identity, view counts, Brain2 matches, or personal viewing claims.
- Every English quote in a Vietnamese answer must have a close Vietnamese translation immediately below it.
- If transcript tools fail, ask the user for a transcript or summarize from user-provided notes; do not pretend full-video access.
- If speaker research uses web, cite or name the sources used.
- If Brain2 or vault tools are unavailable, say so before using memory or general reasoning.
- Speaker Profile may be drafted automatically, but durable Worldview Library entries require user approval unless the user explicitly asked to save all.

## Output Boundary

For quick asks, answer in chat.

For serious learning runs, create or update a folder under:

```text
/Users/rio/content/youtube-learning/<slug>/
```

Minimum useful files:

```text
source.md
speaker-profile.md
worldview-analysis.md
brain2-check.md
application.md
qa.md
```

Use `scripts/youtube_learning.py scaffold <slug>` when a folder is needed.

