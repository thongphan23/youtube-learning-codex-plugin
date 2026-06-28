---
name: discover-videos
description: "Find and rank credible YouTube videos for an article, thesis, lesson, or draft, with channel verification and Vietnamese explanations."
---

# Discover Videos

Use this skill when the user gives an article, thesis, lesson, draft, Facebook post, or content idea and asks for YouTube videos to support, challenge, or deepen it.

## Required References

Read before running:

- `../../references/source-policy.md`
- `../../references/output-contracts.md`
- `../../references/quality-rubric.md`

## Input Gate

If the user only invokes the plugin without article/thesis text, ask for the article or the core thesis.

If input is under 100 words, ask whether they want to add context unless the thesis is already precise.

If input is over 3000 words, use the opening, conclusion, headings, and any explicit thesis statement first.

## Phase 1: Extract Search Concepts

Extract 5-8 English keyphrases:

- Main argument.
- Named concepts.
- Psychological, behavioral, technical, or philosophical principles.
- Unique angle.

Avoid generic terms like content, success, life, work, people.

## Phase 2: Generate Search Queries

Create queries across six content types:

- Expert interview.
- Deep dive.
- Science or research.
- How-to.
- Getting started.
- Personal story or real experience.

Prefer English queries. Do not use boolean-heavy search strings unless the available search tool handles them well.

## Phase 3: Search And Verify

Use available tools in this order:

1. Local video library if configured.
2. Web/search tools scoped to YouTube.
3. YouTube oEmbed for channel identity.
4. YouTube Data API only when the user has configured it.

Hard filters:

- Keep normal watch URLs.
- Reject Shorts unless the user asks for Shorts.
- Reject videos whose channel identity cannot be verified when the output claims channel credibility.
- Do not invent view counts. Show them only when fetched from reliable metadata.

Use helper commands when useful:

```bash
python3 /Users/rio/plugins/youtube-learning/scripts/youtube_learning.py oembed "https://www.youtube.com/watch?v=..."
python3 /Users/rio/plugins/youtube-learning/scripts/youtube_learning.py validate-library /absolute/path/to/video-library.json
```

## Phase 4: Rank

Score candidates by:

- Relevance to thesis.
- Channel credibility.
- Content type diversity.
- Concrete evidence in title, description, highlights, or transcript.
- Usefulness for the target audience.

If strict filtering returns too few videos, report the constraint and ask whether to widen the channel gate.

## Phase 5: Explain

Write Vietnamese explanations that begin from what the video appears to cover, not from fake personal experience.

Never write:

- "tui da xem"
- "tui nghe xong"
- "tui bo ra X gio"
- Any claim that the user or writer watched it unless true.

Avoid floating English when Vietnamese works:

- insight -> goc nhin
- mindset -> tu duy
- framework -> khung or he thong
- research -> nghien cuu
- recommend -> goi y

Keep proper nouns like YouTube, Huberman, Kurzgesagt, Lex Fridman.

## Output Contract

For article-support output, use plain text:

```text
Neu muon dao sau hon nhung gi vua doc, day la may video dang xem:

1. [Title]
[Channel] ([view count if verified])
[URL]

[Two-sentence Vietnamese explanation.]

---
```

For research-mode output, use a table:

```text
| # | Video | Channel | Why it matters | Caveat |
```

## Save To Library

If the user asks to save or a library path is configured, save only verified metadata:

- URL.
- Title.
- Channel.
- Keyphrases.
- Explanation.
- Added date.
- Verification method.

Do not save unsourced claims.

