# EthicsExpert Agent Class

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
\>>> ethics_expert = EthicsExpert()

\>>> response = ethics_expert.chat("Is lying ever justified in Buddhism?")

\>>> print(response)

[Provides detailed ethical analysis of lying according to Buddhist principles]