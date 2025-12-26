# Agentic-AI-Web-Search-File-System-Python-REPL-to-Your-Assistant
Sidekick Agent – Experimental AI Coworker

Sidekick is an experimental AI agent application designed to act as a powerful coworker.
It is capable of searching the web, navigating pages, reading and writing files, executing Python code, sending notifications, and retrieving knowledge from Wikipedia using a tool-augmented agent architecture.

This project is intended as a flexible foundation rather than a finished product.

Project Overview

The Sidekick application is built using LangChain, LangGraph, and Gradio.
It demonstrates how an AI agent can be equipped with multiple tools and allowed to reason about when and how to use them to complete real tasks.

The system is designed as a canvas that can be extended, modified, and customized based on user needs.

Key Capabilities

Web search using SerpAPI

Browser automation using Playwright (Chromium)

File system read/write access within a restricted sandbox directory

Wikipedia knowledge retrieval through the public Wikipedia API

Python code execution through a Python REPL tool

Push notifications using the Pushover API

Agent workflow based on a worker–evaluator architecture

Interactive user interface built with Gradio

Project Structure
sidekick/
│
├── sidekick_tools.py   # Definition and setup of all tools
├── sidekick.py         # Core agent logic, state definition, and graph construction
├── app.py              # Gradio application and user interface
└── .env                # Environment variables and API keys

Tools Module (sidekick_tools.py)

This module centralizes all tools used by the agent.

Included tools:

Web Search Tool
Uses SerpAPI to perform internet searches and return structured results.

Browser Tool
Uses Playwright to control a Chromium browser for automated navigation.
The browser has no access to stored cookies, passwords, or authentication data.

File Management Tool
Based on the LangChain File Management Toolkit.
Access is restricted to a predefined sandbox directory to prevent unrestricted file system access.

Wikipedia Tool
Uses Wikipedia’s public API to retrieve encyclopedic information.

Python Execution Tool
Allows the agent to execute Python code directly on the host machine.
This tool is not sandboxed and should be removed if there are security concerns.

Push Notification Tool
Sends notifications using the Pushover API.

All tools are collected into a single list and automatically made available to the agent.

Core Agent Module (sidekick.py)

This module contains the main Sidekick class and agent logic.

Key components:

State Definition
A typed state object that tracks:

Message history

Success criteria

Evaluation feedback

Flags indicating whether user input is required

Worker Agent
Responsible for task execution and tool usage.

Evaluator Agent
Uses structured output to assess whether success criteria are met and whether additional user input is needed.

Agent Graph
Built using LangGraph to define the flow between worker execution and evaluation steps.

Because some tools require asynchronous initialization (such as Playwright), the agent setup is split between the constructor and an asynchronous setup method.

User Interface (app.py)

The user interface is built using Gradio.
It manages user input, displays agent responses, and connects the frontend to the Sidekick agent backend.

Safety and Usage Notes

This application provides the agent with significant capabilities.

Python execution is not isolated or sandboxed

Browser automation can navigate real websites

File system access is restricted but still real

If you are not comfortable with these capabilities:

Remove the Python execution tool

Remove browser automation tools

Limit the available tool set

The user is responsible for monitoring and controlling agent behavior.

Design Philosophy

Sidekick is intentionally experimental.

Prompts are expected to be refined over time

Tools can be added or removed as needed

Behavior may require iteration and tuning

The project is designed to encourage experimentation and exploration rather than provide a fully locked-down product.

Future Improvements

Additional tool integrations (calendar, external APIs)

Improved safety guardrails

Refactoring and modularization of agent logic

Enhanced monitoring and logging

Integration with MCP-based tooling
