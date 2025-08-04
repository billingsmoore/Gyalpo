"""
PhilosophyExpert Agent Class

This module implements a specialized expert agent for Buddhist philosophy, extending the base Agent class.
The agent provides authoritative explanations of core Buddhist philosophical concepts by retrieving and
synthesizing information from a dedicated knowledge base.

The PhilosophyExpert agent:

    Maintains a specialized vector database of Buddhist philosophical knowledge

    Explains key concepts like emptiness, dependent origination, and non-self

    Provides comparative analysis of different Buddhist philosophical schools

    Delivers nuanced explanations of complex metaphysical concepts

Attributes:
domain (str): The specialized domain ("Buddhist Philosophy")
db_path (str): Path to the philosophy-specific Chroma database
(default: 'agents/experts/expert_dbs/philosophy_db')
embedding_function: SentenceTransformer embeddings model (all-MiniLM-L6-v2)
db: Chroma vector database instance for philosophical knowledge

Methods:
system_prompt(): Establishes the agent's expertise in Buddhist philosophy
user_prompt(): Structures queries with retrieved philosophical context
get_context(): Retrieves relevant philosophical documents from vector database

Example Usage:

\>>> philosophy_expert = PhilosophyExpert()

\>>> response = philosophy_expert.chat("Explain the concept of sunyata")

\>>> print(response)

[Provides detailed explanation of emptiness in Madhyamaka philosophy]
"""