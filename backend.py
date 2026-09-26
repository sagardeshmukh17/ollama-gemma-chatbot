from urllib import response

import ollama

MODEL_NAME = "gemma:latest"

def ask_ollama(question):
    response = ollama.chat(
        model = MODEL_NAME,
        messages = [
            {
                "role":"user",
                "content": question
            }
        ]
    )
    return response["message"] ["content"]

