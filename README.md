Day 1 – Agentic AI Foundations
Aim

To implement and compare a Chatbot, Rule-Based Workflow, and AI Agent using Python and Groq.

Technologies
Python
Groq API
Qwen 3.8 27B
OpenAI-compatible API
Systems
1. Chatbot

Directly sends the question to the LLM without tools or private data.

2. Rule-Based Workflow

Uses predefined Python rules to answer questions.

3. AI Agent

Uses an LLM with tools:

get_course_fee
calculator
Key Observations
System	Observation
Chatbot	Can hallucinate private fee information
Workflow	Reliable but rigid
Agent	Flexible and uses tools for multi-step tasks
Agent Result
AI202 → Rs. 18,000
CS101 + AI202 after 10% scholarship → Rs. 27,000
DS303 vs CS101 → Rs. 3,000 more
Budget challenge → CS101 + DS303 = Rs. 27,000
Key Learning

Chatbot = LLM
Workflow = Fixed rules
Agent = LLM + Tools + Loop

Project Structure
Day1/
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
├── challenge.py
├── check_setup.py
├── config.py
├── requirements.txt
└── outputs/
Security

API keys are stored in .env and are not uploaded to GitHub.
