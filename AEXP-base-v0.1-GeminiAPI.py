# To work the chatbot, you should get a Gemini API key from https://aistudio.google.com/app/apikey

import google.generativeai as genai

genai.configure(api_key="ENTER YOUR API KEY")
model = genai.GenerativeModel('gemini-pro')

while True:
    user_prompt = input("You: ")
    if user_prompt == 'quit':
        break
    response = model.generate_content(user_prompt)
    print("AEXP-base-v0.1-GeminiAPI: ", response.text)