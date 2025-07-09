import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(message):
    prompt = f"You are a polite LinkedIn user. Reply to the following message professionally:\n\nMessage: {message}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example use
message = "Hi, we are hiring Python developers. Are you interested?"
reply = generate_reply(message)
print("AI Reply:", reply)