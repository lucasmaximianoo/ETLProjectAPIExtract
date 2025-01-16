import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Quais as principais caracteristicas de um bom analista de dados?"}]
}

response = requests.post(url, headers = headers, data = json.dumps(data))

# Verificando o status da resposta
if response.status_code == 200:
    try:
        # Tentar acessar a resposta
        print(response.json()["choices"][0]["message"]["content"])
        
    except KeyError:
        print("Erro: A estrutura do JSON retornado não contém a chave 'choices'.")
        print(response.json())  # Exibe a resposta completa para análise
else:
    print(f"Erro na API: status code {response.status_code}")
    print(response.json())  # Exibe a resposta de erro da API