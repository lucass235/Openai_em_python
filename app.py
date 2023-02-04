# uso da api do openai
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getennaov("OPENAI_API_KEY")

model_engine = "text-davinci-002"

for i in range(10):
    prompt = input("Pergunta: ")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = completions.choices[0].text
    print("Resposta:", answer)
