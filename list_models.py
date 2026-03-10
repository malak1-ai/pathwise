import requests

OPENROUTER_API_KEY = "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"

def list_models():
    url = "https://openrouter.ai/api/v1/models"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        models = response.json().get('data', [])
        print(f"Found {len(models)} models.")
        for model in models:
            if 'free' in model.get('id', ''):
                print(f"- {model.get('id')}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    list_models()
