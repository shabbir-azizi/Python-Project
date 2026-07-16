import json
from openai import OpenAI

client = OpenAI()


def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a professional software engineer and hiring manager.

Analyze the following resume based on the user's career goal.

Career Goal:
{user_goal}

Resume:
{resume_text}

Instructions:
1. Extract the candidate's relevant skills.
2. Identify the important missing skills for the chosen career goal.
3. Create a step-by-step learning roadmap.
4. Generate 5 interview questions related to the career goal.
5. Ignore unrelated skills.
6. Return ONLY valid JSON.

Output format:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert software engineer, technical recruiter, and career coach."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content.strip()

        start = content.find("{")
        end = content.rfind("}") + 1

        json_text = content[start:end]

        return json.loads(json_text)

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }