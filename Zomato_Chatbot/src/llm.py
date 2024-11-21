from openai import OpenAI
from src.prompt import system_instruction
from dotenv import load_dotenv
import os
load_dotenv()

# Initialize OpenAI client with API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ensure API key is not None
if api_key is None:
    raise ValueError("API key not found. Check your .env file or environment variables.")


messages = [
    {"role" : "system", "content": system_instruction}
]

def ask_order(message, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model = model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content