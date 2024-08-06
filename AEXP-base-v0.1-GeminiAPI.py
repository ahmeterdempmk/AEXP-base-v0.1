# AIzaSyBJKOX4hjVniqssUnC2pBEaLWHmTGDac_E -> Gemini API Key

import google.generativeai as genai

genai.configure(api_key="AIzaSyBJKOX4hjVniqssUnC2pBEaLWHmTGDac_E")
model = genai.GenerativeModel('gemini-pro')

while True:
    user_prompt = input("You: ")
    if user_prompt == 'quit':
        break
    response = model.generate_content(user_prompt)
    print("AEXP-base-v0.1-GeminiAPI: ", response.text)