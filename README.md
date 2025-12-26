🧠 Sidekick Agent – Experimental AI Coworker

An experimental AI sidekick application that acts as a powerful coworker capable of searching the web, browsing pages, reading and writing files, executing Python code, sending notifications, and retrieving knowledge from Wikipedia — all through an agent-based architecture.

⚠️ Important: This project is experimental and intentionally powerful. Use with caution.

🚀 Project Overview

Sidekick is an AI-powered assistant built using LangChain, LangGraph, and Gradio.
It is designed as a canvas, not a finished product — a flexible foundation that you can customize, extend, and experiment with.

The agent operates with multiple tools and can autonomously decide when and how to use them to achieve user goals.

✨ Key Features

🔍 Web Search using SerpAPI

🌐 Browser Automation via Playwright (Chromium)

📂 File System Access (sandboxed directory only)

🧠 Wikipedia Knowledge Retrieval

🐍 Python Code Execution (unsandboxed – use carefully)

🔔 Push Notifications using Pushover

🧩 Agent Graph Architecture with Worker & Evaluator roles

🖥️ Interactive UI built with Gradio

🏗️ Project Structure
sidekick/
│
├── sidekick_tools.py   # All tool definitions (search, browser, files, python, etc.)
├── sidekick.py         # Core agent logic, state, graph, worker & evaluator
├── app.py              # Gradio UI and app entry point
└── .env                # API keys and environment variables

🛠️ Tools Included
1. Web Search Tool

Uses SerpAPI for fast and reliable web search

Returns structured search results for the agent

2. Browser Tool

Uses Playwright (Chromium) for automated web navigation

No access to cookies, saved passwords, or authentication data

3. File Management Tool

Based on LangChain File Management Toolkit

Restricted to a specific sandbox/ directory

Allows reading and writing files safely

4. Wikipedia Tool

Uses Wikipedia’s public API

Enables factual lookups and background research

5. Python REPL Tool ⚠️

Allows the agent to execute arbitrary Python code

Not sandboxed

Can be removed if you’re not comfortable with this level of access

6. Push Notification Tool

Sends notifications via Pushover

Useful for alerts, task completion, or monitoring long operations

🧠 Agent Architecture

The system is built using a graph-based agent workflow:

Worker Agent

Executes tasks

Uses tools

Produces outputs

Evaluator Agent

Assesses whether success criteria are met

Determines if user input is required

Provides structured feedback

The agent state includes:

Message history

Success criteria

Evaluation feedback

Flags for user input

⚠️ Safety & Usage Notes

This agent has real capabilities and real access

Python execution is not isolated

Browser automation is powerful but controlled

File access is sandboxed, but still real

👉 If you are unsure:

Remove the Python tool

Remove browser tools

Start with limited capabilities

You are responsible for how this agent is used.

🎨 Philosophy

This project is not a polished product — it’s a starting point.

Experiment with prompts

Add or remove tools

Customize agent behavior

Iterate until it fits your workflow

Think of it as your own personal AI coworker, built and controlled by you.

🔮 Future Extensions

Add calendar integration

Connect to external APIs

Integrate MCP-based tools

Improve safety guardrails

Refactor agent modules

Add logging & monitoring

