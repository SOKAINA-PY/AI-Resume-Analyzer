import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AIzaSyChoNWPA5B63rYjDuX_mApnd-CqpskK7Bg")
)


def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text