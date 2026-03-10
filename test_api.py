import requests
import json

OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def test_api():
    job = "Software Engineer"
    industry = "Technology"
    prompt = f"Provide a list of 5 essential skills for a {job} in the {industry} industry. For each skill, provide a small explanation (max 2 sentences) of why it's important for growth. Return the result as a JSON-like list of objects with 'skill' and 'explanation' keys."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a career growth advisor. Provide skills and short explanations in JSON format: [{\"skill\": \"name\", \"explanation\": \"text\"}, ...]"},
            {"role": "user", "content": prompt}
        ]
    }

    print("Sending request to OpenRouter...")
    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
        result = response.json()
        print("Response received successfully.")
        print(json.dumps(result, indent=2))
        
        content = result['choices'][0]['message']['content']
        print(f"\nContent:\n{content}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        if 'response' in locals():
            print(f"Response Text: {response.text}")

if __name__ == "__main__":
    test_api()
