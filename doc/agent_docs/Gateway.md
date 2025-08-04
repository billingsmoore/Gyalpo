# Gateway Agent Class

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

\>>> agent = Gateway(categories=['ethics', 'philosophy', 'history'])

\>>> agent.chat("What is the Noble Eightfold Path?")

'ethics'

\>>> agent.chat("How do I fix my car?")

'NO'