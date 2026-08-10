import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)


def evaluate_interview(questions, answers):
    """
    Sends the complete interview to Gemini in ONE API request.
    Returns a list of evaluations.
    """

    interview_data = []

    for question, answer in zip(questions, answers):
        interview_data.append({"question": question, "answer": answer})

    prompt = f"""
You are an expert technical and HR interviewer.

Evaluate the candidate's complete interview.

Interview:

{json.dumps(interview_data, indent=2)}

For EACH question:

1. Give a score from 0 to 10.
2. Give specific feedback.
3. Check whether the answer actually addresses the question.
4. Identify meaningless/random/gibberish answers.
5. Consider spelling and grammar separately from the actual quality of the idea.
6. Be fair and constructive.

Return ONLY valid JSON in exactly this structure:

[
    {{
        "score": 8,
        "feedback": "Specific feedback here."
    }}
]

There must be exactly one evaluation for each question.
Do not include markdown.
Do not include ```json.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash", contents=prompt
        )

        if not response.text:
            return None

        data = json.loads(response.text)

        if len(data) != len(questions):
            return None

        return data

    except Exception as error:
        print("\n⚠️ AI evaluation is temporarily unavailable.")
        print("Your interview can still be completed.")
        print(f"Reason: {error}")

        return None
