import requests
import json



url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer -----> APIKEY <------"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Quais as principais caracteristicas de um bom analista de dados?"}]
}

response = requests.post(url, headers = headers, data = json.dumps(data))
print(response.json())