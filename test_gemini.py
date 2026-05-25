from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f'API Key loaded: {api_key[:10]}...')

genai.configure(api_key=api_key)

try: 
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"  - {model.name}")
except Exception as e:
    print(f"Error: {e}")