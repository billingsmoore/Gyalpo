# Critic Agent Class

This module implements a Critic agent that evaluates responses for alignment with Buddhist principles.
The agent serves as a quality control mechanism within the multi-agent Buddhist Q&A system.

The Critic agent:

    Validates whether answers adhere to Buddhist ethics and ideals

    Provides constructive feedback for improving non-compliant answers

    Maintains doctrinal integrity across all system responses

    Operates as a final review stage before delivering answers to users

Attributes:
name (str): Identifier for this agent ("Critic")

Methods:
system_prompt(): Establishes the critic's role and evaluation criteria
user_prompt(): Structures the evaluation request with question and answer
chat(): Inherited from Agent class to process the evaluation

Evaluation Responses:
- "YES" for acceptable answers
- Constructive feedback for answers needing improvement

Example Usage:
>>> critic = Critic()
>>> evaluation = critic.chat({
... 'user_query': 'How should Buddhists view wealth?',
... 'current_answer': 'Money is evil and should be avoided'
... })
>>> print(evaluation)
[Provides feedback on balancing non-attachment with practical needs]
