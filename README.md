# DevAgents: Multi-Agent AI System for End-to-End Software Creation

## 📖 Overview
DevAgents is an intelligent multi-agent framework. It simulates a virtual software development company where each Large Language Model (LLM)-powered agent plays a specialized role. These agents collaborate through natural language communication to complete all stages of software creation—ideation, planning, development, testing, and documentation.

## 👥 Agent Roles and Responsibilities

- 🧠 **Chief Executive Officer (CEO)**: Sets the vision and oversees the overall project direction.
- 📦 **Chief Product Officer (CPO)**: Defines software specifications based on the task and ensures alignment with product goals.
- 🛠️ **Chief Technology Officer (CTO)**: Designs the system architecture and selects suitable technologies for implementation.
- 👨‍💻 **Programmer**: Converts the design into functional code using best practices.
- 🔍 **Reviewer**: Performs in-depth code reviews to ensure correctness, security, and maintainability.
- ✅ **Tester**: Creates and runs test cases to validate functionality and identify bugs.
- 🎨 **Art Designer**: Designs UI elements and visuals to enhance user experience when applicable.

These agents operate in a structured sequence and communicate with each other via natural language prompts to simulate a real-world software development lifecycle.

## 🔧 Key Features
- 🧩 Modular, role-based multi-agent collaboration
- 🧠 Powered by LLMs (OpenRouter-compatible)
- 🔄 Supports end-to-end software development automation
- 🛠️ Fully customizable workflow for different use cases and research

## ⚙️ Setup and Execution

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/sireeshasuguru/DevAgents.git
cd DevAgents
```

### 2. 🐍 Create a Virtual Environment
Make sure Python 3.9 or higher is installed:
```bash
python -m venv devagent_env

# Windows:
devagent_env\Scripts\activate

# macOS/Linux:
source devagent_env/bin/activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🔐 Set Up Environment Variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL=deepseek/deepseek-r1:free
```
✅ Ensure `.env` is listed in `.gitignore` to protect your credentials.

### 5. 🚀 Run the Project
To initiate software creation:
```bash
python run.py --task "Create a Python-based Calculator" --name "Calculator"
```

### 6. 📂 View Output
Generated projects are stored in the `WareHouse/` directory:
```bash
cd WareHouse/Calculator_DefaultOrganization_YYYYMMDD
```
Inside, you'll find:
- ✅ Full source code
- 📜 Documentation files
- 🔁 Agent interaction logs

---

DevAgents empowers developers, researchers, and students to explore AI-driven software engineering through a collaborative and modular agent-based system.

Happy Building! 🚀
