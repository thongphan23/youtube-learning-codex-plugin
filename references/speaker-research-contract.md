# Speaker Research Contract

The speaker section is an authority check, not decoration. Its job is to help the learner answer:

- Who is this person in human terms?
- Why should I listen to them on this exact topic?
- Which evidence gives them authority, and what kind of authority is it?
- Where does their authority stop?
- What bias, incentive, or professional lens might shape what they say?

## Required Minimum

For a serious `learn-video` run, gather enough factual context to include at least 5 sourced achievements or high-signal facts.

Good achievement types:

- Current institutional role.
- Degrees or specialist training.
- Books authored.
- Peer-reviewed publication count or highly cited work.
- Concepts coined or major public contributions.
- Research areas with direct relevance to the video.
- Public advisory, teaching, lab, or conference roles.
- Concrete projects, datasets, papers, or frameworks.

Weak facts:

- "Is famous."
- "Has many followers."
- "Talks about AI."
- Claims found only in the video title without corroboration.

## Interpretive Requirement

Never output a dry list of titles, institutions, or achievements. Every high-signal fact must be translated into meaning for the learner.

For each role, institution, title, award, book, paper, project, or public contribution that you mention, answer these five questions:

1. What is it in plain Vietnamese?
2. Is it hard to get, rare, prestigious, broadly recognized, or only context-setting?
3. Why does it matter for the topic of this video?
4. What kind of authority does it create: direct expertise, adjacent expertise, public communication ability, lived experience, institutional access, or reputation signal?
5. What does it not prove?

If the institution is named, explain its scale or significance when evidence is available. Do not assume every university, lab, company, fellowship, or think tank is equally important.

If the title is specialized, explain it. For example, do not write only "associate professor". Explain that it is a senior academic role in many university systems, usually reached after years of research, teaching, publication, and peer evaluation. Then state whether that matters for this video.

If the achievement is a paper, book, dataset, method, public role, or advisory role, connect it to the video's topic. If it is impressive but unrelated, say so.

## Authority Types

Use this classification when useful:

- Direct authority: the speaker has done serious work exactly in the video's domain.
- Adjacent authority: the speaker's expertise is near the topic, but not identical.
- Explanatory authority: the speaker may be good at making a field understandable, even if they are not the top technical researcher in that narrow area.
- Institutional authority: the speaker has access, position, or affiliation that suggests credibility, but this still needs topic relevance.
- Reputation signal: the speaker is known, cited, invited, published, or trusted by credible groups.
- Weak authority: popularity, confidence, titles without relevance, or claims that cannot be verified.

Do not inflate adjacent or reputation authority into direct authority.

## Source Order

Prefer:

1. Official university or employer profile.
2. Official personal site.
3. Google Scholar, ORCID, DBLP, publisher pages, or book pages.
4. Podcast/show notes for context, clearly labeled as show metadata.
5. Wikipedia only as a pointer, not as sole support for unusual claims.

## Output Shape

Use:

```text
### Người chia sẻ là ai, và vì sao nên nghe

**Nói bằng tiếng người:** ...

**Bản đồ thẩm quyền**
1. [Verified fact]  
   - Nghĩa là gì: ...
   - Có khó/hiếm/quan trọng không: ...
   - Liên quan gì đến video này: ...
   - Tăng niềm tin ở điểm nào: ...
   - Không chứng minh điều gì: ...
2. ...
...

**Vì sao nên nghe người này về chủ đề này:** ...

**Nên cảnh giác ở đâu:** ...

**Nguồn đã kiểm tra:** ...
```

If only 3-4 achievements are verifiable, write:

```text
Only N achievements were verified from available sources. I checked: [sources]. I will not fill the gap with guesses.
```

## Bad And Good

Bad:

```text
He is an associate professor at X University and has published many papers.
```

Good:

```text
Ông là phó giáo sư tại X University, tức là một vai trò học thuật cấp cao hơn giảng viên mới vào nghề. Chức danh này thường đòi hỏi nhiều năm nghiên cứu, giảng dạy, công bố và được đồng nghiệp trong ngành đánh giá. Nó làm tăng độ tin cậy khi ông nói về [topic] vì [reason]. Nhưng nó không tự động chứng minh ông đúng về [limit].
```

Bad:

```text
She worked at OpenAI, wrote a book, and is a venture partner.
```

Good:

```text
Việc từng làm ở OpenAI là tín hiệu bà có kinh nghiệm gần với trung tâm phát triển AI hiện đại, nên đáng nghe khi nói về cách hệ thống AI được xây và triển khai. Nhưng nếu video bàn về tác động xã hội dài hạn, đây chỉ là thẩm quyền liền kề; cần thêm bằng chứng từ chính sách, xã hội học, kinh tế hoặc dữ liệu thực nghiệm.
```
