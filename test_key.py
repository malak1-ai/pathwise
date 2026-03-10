import requests

OPENROUTER_API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "openrouter/free",
    "messages": [{"role": "user", "content": "Say hello"}]
}

try:
    response = requests.post(URL, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
