Sidekick Agent – Experimental AI Coworker

Sidekick is an experimental AI sidekick application designed to act as a powerful coworker.
It can search the web, browse pages, read and write files, execute Python code, send notifications, and retrieve knowledge from Wikipedia using an agent-based architecture.

Important:
This project is experimental and intentionally powerful. Use with caution.

Project Overview

Sidekick is an AI-powered assistant built using LangChain, LangGraph, and Gradio.

It is designed as a canvas, not a finished product.
The goal is to provide a flexible foundation that can be customized, extended, and experimented with.

The agent operates with multiple tools and can autonomously decide when and how to use them in order to achieve user-defined goals.

Key Features

Web search using SerpAPI

Browser automation via Playwright (Chromium)

File system access (restricted to a sandboxed directory)

Wikipedia knowledge retrieval

Python code execution (not sandboxed; use carefully)

Push notifications using Pushover

Agent graph architecture with Worker and Evaluator roles

Interactive user interface built with Gradio

Project Structure
sidekick/
│
├── sidekick_tools.py   # Tool definitions (search, browser, files, python, etc.)
├── sidekick.py         # Core agent logic, state, graph, worker and evaluator
├── app.py              # Gradio UI and application entry point
└── .env                # Environment variables and API keys

Tools Included
Web Search Tool

Uses SerpAPI to perform fast and reliable web searches.
Returns structured search results that the agent can reason over.

Browser Automation Tool

Uses Playwright (Chromium) for automated web navigation.
The browser does not have access to cookies, saved passwords, or authentication data.

File Management Tool

Based on the LangChain File Management Toolkit.
Access is restricted to a specific sandbox/ directory to prevent unrestricted file system access.
Allows safe reading and writing of files.

Wikipedia Tool

Uses Wikipedia’s public API.
Enables factual lookups and background research.

Python REPL Tool

Allows the agent to execute arbitrary Python code on the host machine.
This tool is not sandboxed and should be removed if this level of access is not acceptable.

Push Notification Tool

Sends notifications via the Pushover API.
Useful for alerts, task completion notifications, and monitoring long-running operations.

Agent Architecture

The system is built using a graph-based agent workflow.

Worker Agent

Executes tasks

Uses available tools

Produces outputs

Evaluator Agent

Assesses whether success criteria are met

Determines whether additional user input is required

Provides structured feedback

Agent State

The agent state tracks:

Message history

Success criteria

Evaluation feedback

Flags indicating whether user input is needed

Safety and Usage Notes

This agent has real capabilities and real access.

Python execution is not isolated

Browser automation is powerful but controlled

File access is sandboxed but operates on real files

If you are unsure or uncomfortable:

Remove the Python execution tool

Remove browser automation tools

Start with a limited set of capabilities

You are responsible for how this agent is used.

Design Philosophy

This project is not a polished product.
It is intended as a starting point.

You are encouraged to:

Experiment with prompts

Add or remove tools

Customize agent behavior

Iterate until it fits your workflow

Think of Sidekick as your own AI coworker that you build and control.
