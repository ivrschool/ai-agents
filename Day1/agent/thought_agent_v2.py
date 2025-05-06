import os
import re
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("FIREWORKS_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.fireworks.ai/inference/v1")

class ThoughtAgent:
    def __init__(self, model="accounts/fireworks/models/llama-v3p1-405b-instruct", temperature=0.7):
        self.model = model
        self.temperature = temperature

    def _generate_response(self, prompt: str) -> str:
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

    def get_thoughts(self, count=10, prompt_type="today") -> list:
        topic = "today" if prompt_type == "today" else "tomorrow"
        prompt = f"Give me {count} short, original, motivational 'thought of {topic}' quotes."
        response = self._generate_response(prompt)
        return [line.strip('-•1234567890. ') for line in response.split('\n') if line.strip()]

    def get_custom_thoughts(self, topic: str, count=5) -> list:
        prompt = f"Give me {count} motivational quotes or thoughts related to the topic: '{topic}'"
        response = self._generate_response(prompt)
        return [line.strip('-•1234567890. ') for line in response.split('\n') if line.strip()]
