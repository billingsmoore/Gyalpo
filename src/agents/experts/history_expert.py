"""
HistoryExpert Agent Class

This module implements a specialized expert agent for Buddhist history, extending the base Agent class.
The agent retrieves and synthesizes historical information from a dedicated knowledge base to answer questions
about the development, traditions, and key figures in Buddhist history.

The HistoryExpert agent:

    Maintains a specialized vector database of Buddhist historical knowledge

    Provides authoritative responses on Buddhist historical events, lineages, and traditions

    Covers topics including the life of the Buddha, spread of Buddhism, and development of schools

    Delivers context-rich historical summaries with proper temporal framing

Attributes:
domain (str): The specialized domain ("Buddhist History")
db_path (str): Path to the history-specific Chroma database (default: 'agents/experts/expert_dbs/history_db')
embedding_function: SentenceTransformer embeddings model (all-MiniLM-L6-v2)
db: Chroma vector database instance for historical knowledge

Methods:
system_prompt(): Provides the expert identity and role description
user_prompt(): Formats queries with retrieved historical context
get_context(): Retrieves relevant historical documents from the vector database

Example Usage:
>>> history_expert = HistoryExpert()
>>> response = history_expert.chat("How did Buddhism spread to Tibet?")
>>> print(response)
[Provides detailed historical account of Buddhism's transmission to Tibet]
"""

from agent_template import Agent
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

class HistoryExpert(Agent):
    def __init__(self, db_path='agents/experts/expert_dbs/history_db', domain='Buddhist History'):
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