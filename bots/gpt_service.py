import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"))


def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="google/gemma-3-4b-it:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content