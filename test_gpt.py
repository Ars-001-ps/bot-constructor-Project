from dotenv import load_dotenv
import os

load_dotenv()

print("Ключ загружен:", os.getenv("OPENAI_API_KEY")[:10] + "...")  # покажет первые 10 символов

from bots.gpt_service import ask_gpt

answer = ask_gpt("привет, как дела?")
print(answer)