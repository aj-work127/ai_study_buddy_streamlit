def explain_prompt(q: str) -> str:
    return f"""
Explain the concept below for a beginner.

FORMAT STRICTLY AS:
Definition:
(one paragraph)

Explanation:
(2–3 short paragraphs)

Example:
(one simple example)

Concept:
{q}
"""

def summary_prompt(q: str) -> str:
    return f"""
Summarize the topic below.

RULES:
- Bullet points only
- Maximum 6 bullets
- Each bullet ≤ 12 words

Topic:
{q}
"""

def exam_prompt(q: str) -> str:
    return f"""
Answer the question below as in an exam.

FORMAT STRICTLY AS:
Definition:
(one concise definition)

Key Points:
1.
2.
3.

Example:
(one relevant example)

Question:
{q}
"""

def steps_prompt(q: str) -> str:
    return f"""
Explain the task below step by step.

RULES:
- Numbered steps only
- Each step ≤ 2 lines
- No extra explanation

Task:
{q}
"""

PROMPT_MAP = {
    "Explain": explain_prompt,
    "Summary": summary_prompt,
    "Exam": exam_prompt,
    "Steps": steps_prompt,
}