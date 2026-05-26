# CrewAI + Mistral AI Demo

![CI](https://github.com/NullLabTests/crewai-mistral-demo/actions/workflows/python-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/NullLabTests/crewai-mistral-demo?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/NullLabTests/crewai-mistral-demo?style=flat-square)

![CI](https://github.com/NullLabTests/crewai-mistral-demo/actions/workflows/python-ci.yml/badge.svg)

*A production-ready demo of multi-agent AI with Mistral.*

![CrewAI + Mistral](https://img.shields.io/badge/CrewAI-0.1.0-blue?style=flat-square)
![Mistral](https://img.shields.io/badge/Mistral-Large-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🌟 **What This Demo Does**
This project showcases a **multi-agent AI workflow** using:
- **CrewAI** for agent orchestration
- **Mistral AI** (mistral-large-latest) as the LLM backend
- **Two specialized agents**:
  - **Researcher**: Identifies top AI trends for 2026
  - **Writer**: Transforms research into a detailed blog post

---

## 🚀 **Quick Start**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/crewai-mistral-demo.git
cd crewai-mistral-demo
```

### 2️⃣ **Set Up Your Mistral API Key**
Create a `.env` file in the project root:
```bash
cp .env.example .env
```
Then edit `.env` and add your Mistral API key:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```
*Get your key from [Mistral Console](https://console.mistral.ai/)*

### 3️⃣ **Install Dependencies**
```bash
pip install crewai python-dotenv
```

### 4️⃣ **Run the Demo**
```bash
python3 src/demo.py
```
*Watch as the Researcher and Writer agents collaborate to generate a blog post about AI trends for 2026!*

---

## 📁 **Project Structure**
```
crewai-mistral-demo/
├── src/
│   └── demo.py          # Main demo script with CrewAI + Mistral
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---
## 🛠️ **Customize the Demo**
### Change the Topic
Edit `src/demo.py` and modify the `research_task` description:
```python
research_task = Task(
    description="Research the impact of AI on healthcare in 2026",  # New topic
    expected_output="A list of 5 key AI applications in healthcare...",
    agent=researcher
)
```

### Add More Agents
Add an **Editor Agent** to refine the output:
```python
editor = Agent(
    role="Editor",
    goal="Polish the blog post for clarity and engagement",
    backstory="A meticulous editor with a focus on readability and impact.",
    llm=mistral_llm,
    verbose=True
)

edit_task = Task(
    description="Review the blog post and suggest improvements",
    expected_output="A refined version of the blog post with feedback",
    agent=editor,
    context=[write_task]
)

# Update the Crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    verbose=True
)
```

---
## 🔧 **Troubleshooting**
### "MISTRAL_API_KEY not found"
- Ensure you've created the `.env` file in the **project root**.
- Restart your terminal or run:
  ```bash
  source .env
  ```

### "ModuleNotFoundError: No module named 'crewai'"
- Install the missing package:
  ```bash
  pip install crewai
  ```

### Mistral API Connection Errors
- Verify your key works with this **escaped** command:
  ```bash
  curl -X POST "https://api.mistral.ai/v1/chat/completions"   -H "Authorization: Bearer $MISTRAL_API_KEY"   -H "Content-Type: application/json"   -d '{"model": "mistral-large-latest", "messages": [{"role": "user", "content": "Hello"}]}'
  ```

---
## 📚 **Learn More**
- [CrewAI Documentation](https://docs.crewai.com)
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Multi-Agent Systems Guide](https://github.com/joaomdmoura/crewAI)

---
## 🤝 **Contributing**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-idea`)
5. Open a Pull Request

---
## 📜 **License**
This project is open-source under the [MIT License](LICENSE).