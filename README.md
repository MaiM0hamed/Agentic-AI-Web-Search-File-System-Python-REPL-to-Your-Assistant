# Sidekick Agent – Experimental AI Coworker

Sidekick is an experimental AI sidekick application designed to act as a powerful coworker.  
It can search the web, browse pages, read and write files, execute Python code, send notifications, and retrieve knowledge from Wikipedia using an agent-based architecture.

**Important:**  
This project is experimental and intentionally powerful. Use with caution.

---

## Project Overview

Sidekick is an AI-powered assistant built using **LangChain**, **LangGraph**, and **Gradio**.

It is designed as a canvas rather than a finished product.  
The goal is to provide a flexible foundation that can be customized, extended, and experimented with.

The agent operates with multiple tools and can autonomously decide when and how to use them in order to achieve user-defined goals.

---

## Key Features

- Web search using SerpAPI  
- Browser automation via Playwright (Chromium)  
- File system access (restricted to a sandboxed directory)  
- Wikipedia knowledge retrieval  
- Python code execution (not sandboxed; use carefully)  
- Push notifications using Pushover  
- Agent graph architecture with Worker and Evaluator roles  
- Interactive user interface built with Gradio  

---

## Project Structure

```text
sidekick/
│
├── sidekick_tools.py   # Tool definitions (search, browser, files, python, etc.)
├── sidekick.py         # Core agent logic, state, graph, worker and evaluator
├── app.py              # Gradio UI and application entry point
└── .env                # Environment variables and API keys
