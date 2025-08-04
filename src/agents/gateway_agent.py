"""
Gateway Agent Class

This module implements a Gateway classifier agent that determines if user queries
are relevant to Buddhism and categorizes them. It inherits from the base Agent class.

The Gateway agent:

    Filters non-Buddhist related queries (responding with "NO")

    Classifies valid queries into predefined categories

    Serves as the entry point to a multi-agent Buddhist Q&A system

Attributes:
categories (list): Valid classification categories for Buddhist queries
name (str): Identifier for this agent ("Gateway")

Methods:
system_prompt(): Provides the classification instructions and categories
user_prompt(): Formats the user input for classification

Example:
>>> agent = Gateway(categories=['ethics', 'philosophy', 'history'])
>>> agent.chat("What is the Noble Eightfold Path?")
'ethics'
>>> agent.chat("How do I fix my car?")
'NO'
"""

from agent_template import Agent

class Gateway(Agent):

    def __init__(self, categories):
        self.categories = categories
        self.name = "Gateway"
        super().__init__()

    def system_prompt(self):
        return f"""You are a gateway classifier for a multi-agent Buddhist question-answering system. 
        When you receive a user query you will determine if it is relevant to Buddhism. If it is not you will reply "NO".
        If the query is relevant to Buddhism you will classify it as pertaining to one of the listed categories and reply with just the name of the category.
        {self.categories}"""
    
    def user_prompt(self, user_input):
        return f"""Here is the user's query: {user_input} 
                """
    
