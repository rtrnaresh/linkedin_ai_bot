from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def auto_reply_messages(driver):
    print("💬 Auto-reply system ready (stub demo)")
    messages = ["Hi, are you available for a freelance project?", "Hello! Can you share your resume?"]

    for msg in messages:
        reply = generate_reply(msg)
        print(f"📥 Received: {msg}")
        print(f"📤 Replied: {reply}")
