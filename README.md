# 🧠 AI Debate Arena

### Multi-Agent Reasoning System using CrewAI + Groq (LLaMA 3.1)

> An intelligent debate simulation system where autonomous AI agents argue opposing viewpoints and a judge agent evaluates them based on logic, evidence, and persuasion.

---

## 🚀 Overview

AI Debate Arena is a **multi-agent system** built using CrewAI that simulates structured debates.
It leverages modern LLMs to generate **high-quality arguments**, perform **critical reasoning**, and deliver a **final verdict** based purely on argument strength.

This project demonstrates:

* Multi-agent collaboration
* Structured reasoning
* Prompt engineering
* Real-world AI orchestration

---

## 🧩 System Architecture

```
User Input (Topic)
        ↓
Debater Agent (FOR)
        ↓
Debater Agent (AGAINST)
        ↓
Judge Agent (Evaluation)
        ↓
Final Decision + Reasoning
```

---

## 🤖 Agents

### 🟢 Debater Agent

* Generates arguments **for and against**
* Focuses on:

  * Logical structure
  * Real-world examples
  * Persuasive reasoning

### ⚖️ Judge Agent

* Evaluates both sides objectively
* Uses:

  * Clarity
  * Logic
  * Evidence
  * Persuasiveness

---

## 🛠️ Tech Stack

* Python
* CrewAI (multi-agent orchestration)
* Groq API (LLaMA 3.1)
* LiteLLM
* Streamlit

---

## ⚙️ Installation

```bash
git clone https://github.com/Prateek13052003/ai-debate-crewai.git
cd ai-debate-crewai
python -m venv .venv
source .venv/bin/activate
pip install crewai litellm streamlit
```

---

## 🔑 Environment Setup

```bash
export GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run via CLI

```bash
crewai run
```

---

## 🌐 Run Web Interface

```bash
streamlit run app.py
```

---

## 📊 Execution Output

### 🔹 Task Execution Flow

![Execution](./assets/Execution.png)

---

### 🔹 Agent Reasoning Phase

![Reasoning](./assets/task2.png)

---

### 🔹 Final Judgment Output

![Final Output](./assets/task3.png)

---

## 🧠 Example Result

> After evaluating both sides, the system concludes that
> **the argument against strict regulation of LLMs is more convincing**,
> due to deeper reasoning, stronger examples, and better handling of trade-offs.

---

## 💡 Key Highlights

* ⚡ Real-time multi-agent reasoning
* 🧠 Structured argument generation
* ⚖️ Objective evaluation system
* 🔁 Modular & extensible architecture
* 🌐 UI-ready (Streamlit integration)

---

## 🔬 What Makes This Project Strong

This project demonstrates:

* Agent-based system design
* Prompt engineering
* LLM orchestration
* Decision-making pipelines
* Scalable AI architecture

---

## 📈 Future Enhancements

* Multi-round debates
* Memory-enabled agents
* Multi-judge voting system
* Chat-style UI
* Deployment (Render / AWS / Docker)

---

## 👨‍💻 Author

**Prateek Choudhary**
🔗 https://github.com/Prateek13052003

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐
It helps a lot!
