import os
import requests

api_key = os.environ.get("NVIDIA_API_KEY")

base_url = "https://integrate.api.nvidia.com/v1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "meta/llama-3.1-405b-instruct",
    "messages": [{"role": "user", "content": "hi"}],
    "temperature": 0.2,
    "top_p": 0.7,
    "max_tokens": 1024,
    "stream": False
}

response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")


