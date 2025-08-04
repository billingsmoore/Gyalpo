# HistoryExpert Agent Class

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

\>>> history_expert = HistoryExpert()

\>>> response = history_expert.chat("How did Buddhism spread to Tibet?")

\>>> print(response)

[Provides detailed historical account of Buddhism's transmission to Tibet]