# Synthesizer Agent Class

This module implements a Synthesizer agent that integrates multiple inputs to produce refined,
high-quality answers to Buddhist questions. The agent serves as the final composition stage in
the multi-agent Q&A system.

The Synthesizer agent:

    Combines context from expert agents with critic feedback

    Produces well-structured, comprehensive answers

    Ensures coherence and clarity in final responses

    Maintains appropriate tone and depth for Buddhist teachings

Attributes:
name (str): Identifier for this agent ("Synthesizer")

Methods:
system_prompt(): Establishes the synthesizer's role and capabilities
user_prompt(): Structures the synthesis request with all relevant inputs
chat(): Inherited from Agent class to generate the final answer

Input Structure:
Requires dictionary containing:
- user_query: The original question
- context: Relevant knowledge from experts (optional)
- current_answer: Previous answer draft (optional)
- feedback: Critic's suggestions (optional)

Example Usage:
>>> synthesizer = Synthesizer()
>>> final_answer = synthesizer.chat({
... 'user_query': 'What is the Middle Way?',
... 'context': 'The Buddha's teaching between extremes...',
... 'current_answer': 'Avoiding extremes',
... 'feedback': 'Should include examples of extremes'
... })
>>> print(final_answer)
[Provides polished explanation of the Middle Way with examples]