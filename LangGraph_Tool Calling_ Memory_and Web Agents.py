from typing import Annotated
from langgraph.graph import StateGraph,START, END
from langgraph.graph.message import add_message
from dotenv import load_dotenv 
from IPython.display import Image, display
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
import requests
import os
from langchain_openai import ChatOpenAI
from typing import TypedDict


from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.tools import tool

load_dotenv()

# Initialize the Google Search API Wrapper
search = GoogleSearchAPIWrapper()

search.run("What is LangGraph?")
from langchain.agents import tool

@tool
def google_search(query: str) -> str:
    """Perform a Google search and return the results."""
    return search.run(query)
