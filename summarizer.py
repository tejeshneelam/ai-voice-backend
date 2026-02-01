from openai import OpenAI

# Create OpenAI client (API key should be in environment variable)
client = OpenAI()

def summarize_text(text: str) -> str:
    """
    Takes text input and returns a structured summary
    """
    prompt = f"""
You are an AI assistant.

Summarize the following voice note.
Return output in this format only:

Key Points:
- point 1
- point 2

Action Items:
- action 1
- action 2

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
