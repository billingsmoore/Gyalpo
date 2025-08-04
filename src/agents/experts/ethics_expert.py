"""
EthicsExpert Agent Class

This module implements a specialized expert agent for Buddhist ethics, extending the base Agent class.
The agent retrieves and synthesizes information from a dedicated ethics knowledge base to answer questions
about Buddhist moral philosophy and conduct.

The EthicsExpert agent:

    Maintains a specialized vector database of Buddhist ethics knowledge

    Provides authoritative responses on Buddhist moral principles and precepts

    Handles questions about right conduct, virtues, and ethical dilemmas from a Buddhist perspective

    Inherits core chat functionality while specializing in ethical domain knowledge

Attributes:
name (str): Identifier for this agent ("Ethics Expert")
domain (str): The specialized domain (Buddhist Ethics)
db_path (str): Path to the ethics-specific Chroma database
embedding_function: SentenceTransformer embeddings model
db: Chroma vector database instance for ethics knowledge

Methods:
system_prompt(): Provides the expert identity and role description
user_prompt(): Formats queries with retrieved ethical context
get_context(): Retrieves relevant ethical documents from the vector database

Example Usage:
>>> ethics_expert = EthicsExpert()
>>> response = ethics_expert.chat("Is lying ever justified in Buddhism?")
>>> print(response)
[Provides detailed ethical analysis of lying according to Buddhist principles]
"""

from agent_template import Agent
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

class EthicsExpert(Agent):
    def __init__(self, db_path='agents/experts/expert_dbs/ethics_db', domain='Buddhist Ethics'):
        # Initialize Chroma DB
        self.name = 'Ethics Expert'
        self.domain = domain
        self.embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory=db_path, embedding_function=self.embedding_function)

        super().__init__()


    def system_prompt(self):
        return f"""You are an expert in {self.domain}. You provide summaries of important context to answer user questions."""

    def user_prompt(self, user_input):

        context = self.get_context(user_input)

        return f"""Use the the provided context for a response to the user query.
                user_query: {user_input} 
                context: {context}
                """

    def get_context(self, query, k=3):
        # Search the Chroma DB for relevant documents
        results = self.db.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results])