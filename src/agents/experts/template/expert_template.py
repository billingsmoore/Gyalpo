"""
Expert Agent Class

This module implements an Expert agent that retrieves and summarizes domain-specific
information from a vector database. It inherits from the base Agent class.

The Expert agent:

    Maintains a knowledge base using Chroma vector database

    Retrieves relevant context using semantic search

    Provides expert-level summaries for user queries

    Can be specialized for any domain by configuring the DB_PATH and DOMAIN

Attributes:
db_path (str): Path to the persistent Chroma database directory
domain (str): The expert domain this agent specializes in
embedding_function: SentenceTransformer embeddings model
db: Chroma vector database instance

Methods:
system_prompt(): Provides the expert identity and role description
user_prompt(): Formats the user input with retrieved context for summarization
get_context(): Retrieves relevant documents from the vector database

Configuration:
DB_PATH: Path to the Chroma database (must be set before use)
DOMAIN: The expert domain (must be set before use)

Example:
>>> expert = Expert(db_path='data/buddhism_db', domain='Buddhist philosophy')
>>> response = expert.chat("Explain the concept of dependent origination")
>>> print(response)
"""

from agent_template import Agent
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# CONFIG
DB_PATH = 'my/db/path'# REPLACE THIS WITH ACTUAL DB PATH
DOMAIN = 'expert domain' # REPLACE THIS WITH ACTUAL DOMAIN

class Expert(Agent):
    def __init__(self, db_path=DB_PATH, domain=DOMAIN):
        super().__init__()
        # Initialize Chroma DB
        self.domain = domain
        self.embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory=db_path, embedding_function=self.embedding_function)

    def system_prompt(self):
        return f"""You are an expert in {self.domain}. You provide summaries of important context to answer user questions."""

    def user_prompt(self, user_input):

        context = self.get_context(user_input)

        return f"""Summarize the provided context for a response to the user query.
                user_query: {user_input} 
                context: {context}
                """

    def get_context(self, query, k=3):
        # Search the Chroma DB for relevant documents
        results = self.db.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results])