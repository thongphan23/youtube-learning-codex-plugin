# Chat Output Contract

YouTube Learning is judged in the chat. The user should not have to open several files to know whether the analysis is deep enough.

## Default

For `learn-video`, deliver the full analysis in the chat by default.

Supporting files are allowed, but only after the chat contains the substantive answer.

## Required Chat Structure

Use this order unless the user asks otherwise:

1. **Nguồn đã đọc**: video, transcript, metadata, speaker sources, and limits.
2. **Người chia sẻ là ai**: role, field, and 5+ verified achievements.
3. **Vì sao nên nghe người này**: why this speaker matters for this topic, including likely bias.
4. **Các ý tưởng cốt lõi**: up to 3 Socratic worldview sections.
5. **Tổng hợp**: table or compact map.
6. **Ứng dụng cho người học**: specific benefits, decisions, and next actions.
7. **Câu hỏi suy ngẫm**: 3-5 questions.
8. **QA và ranh giới nguồn**: pass/fail and uncertainty.
9. **File phụ trợ**: only if created.

## Depth Rule

Do not compress serious learning into a short executive summary unless asked. A good answer should be long enough for the user to judge:

- factual depth;
- reasoning depth;
- usefulness;
- applicability;
- source boundaries.

## File Rule

Bad:

```text
Mình đã lưu phân tích ở file A, B, C.
```

Good:

```text
Here is the full analysis...

Supporting files:
- ...
```

