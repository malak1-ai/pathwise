import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-skills", methods=["POST"])
def get_skills():
    data = request.json
    job = data.get("job")
    industry = data.get("industry")

    if not job or not industry:
        return jsonify({"error": "Job and industry are required."}), 400

    prompt = f"Provide a list of 5 essential skills for a {job} in the {industry} industry. For each skill, provide: 1. A small explanation (max 2 sentences) of why it's important for growth. 2. 2-3 specific solutions or ways to develop this skill. 3. 1-2 recommended books to learn it. Return the result as a JSON list of objects with 'skill', 'explanation', 'solutions', and 'books' keys."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "PathWise"
    }

    payload = {
        "model": "openrouter/free",
        "messages": [
            {"role": "system", "content": "You are a career growth advisor. Provide 5 skills in STRICT JSON format: [{\"skill\": \"name\", \"explanation\": \"text\", \"solutions\": [\"solution1\", \"solution2\"], \"books\": [\"book1\", \"book2\"]}, ...]. Do not include any other text."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        content = result['choices'][0]['message']['content'].strip()
        
        # Enhanced JSON extraction
        import re
        json_match = re.search(r'\[\s*{.*}\s*\]', content, re.DOTALL)
        if json_match:
            content = json_match.group(0)
            
        return jsonify({"skills": content})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": f"Failed to fetch skills: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
