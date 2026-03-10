# 🚀 PathWise: AI-Driven Career Growth Architect

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

**PathWise** is an intelligent career development platform that leverages Large Language Models (LLMs) to provide professionals with a structured roadmap for career advancement. By analyzing your current role and industry, PathWise architecturally maps out essential skills, actionable development solutions, and a curated reading list to bridge the gap between where you are and where you want to be.

---

## 🌟 Key Features

- **AI-Powered Skill Mapping**: Uses OpenRouter (Llama-3/Gemma) to identify top-tier growth skills.
- **Actionable Roadmaps**: Provides specific training platforms, labs, and techniques for skill acquisition.
- **Curated Knowledge Library**: Recommends industry-standard literature for deep conceptual understanding.
- **Modern Architecture**: Features a high-performance Flask backend with a responsive, glassmorphism-inspired UI.
- **Dynamic Content Aggregation**: Intelligently parses AI responses to ensure unique and high-relevance output.

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.13, Flask, Requests, Regex (Parsing) |
| **Frontend** | HTML5 (Semantic), Vanilla CSS (Glassmorphism), Vanilla JavaScript |
| **AI Integration** | OpenRouter API (Accessing 350+ Global Models) |
| **Design System** | Custom CSS Grid, Inter Typography, Dynamic Micro-animations |

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- A valid [OpenRouter API Key](https://openrouter.ai/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/pathwise.git
   cd pathwise
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Access:**
   Open `app.py` and replace the `OPENROUTER_API_KEY` placeholder with your secure key (or use environment variables for production).

### Running the Application

Start the development server:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## 🏗️ Project Structure

```text
pathwise/
├── static/
│   ├── css/
│   │   └── style.css      # Core design system & glassmorphism components
│   └── js/
│       └── script.js     # Async API handling & dynamic DOM rendering
├── templates/
│   └── index.html        # Main application entry point
├── app.py                # Flask server & OpenRouter Integration logic
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
```

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">Built with ❤️ for professionals worldwide by PathWise Team.</p>
