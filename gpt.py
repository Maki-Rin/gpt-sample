import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(message: list) -> str:
    print("Generating...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=message,
            )
        return response['choices'][0]['message']['content']
    except:
        print("Error")