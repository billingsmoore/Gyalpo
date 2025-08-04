"""
Buddhist Q&A System - Proof of Concept Implementation

This file demonstrates a multi-agent system for answering Buddhist questions using:

    Gateway classification

    Domain-specific expertise

    Quality assurance critique

    Answer synthesis

The system workflow:

    Gateway determines if question is Buddhist-related and categorizes it

    Appropriate domain expert generates initial answer

    Critic evaluates answer quality

    Synthesizer produces final response incorporating feedback

Agents:

    Gateway: Initial question classifier

    EthicsExpert: Handles moral/conduct questions

    PhilosophyExpert: Addresses metaphysical concepts

    HistoryExpert: Covers historical developments

    Critic: Ensures answer quality

    Synthesizer: Produces polished final answers
    """

from agents.gateway_agent import Gateway

from agents.experts.ethics_expert import EthicsExpert
from agents.experts.philosophy_expert import PhilosophyExpert
from agents.experts.history_expert import HistoryExpert

from agents.critic_agent import Critic
from agents.synthesizer_agent import Synthesizer

CATEGORIES = ['ETHICS', 'PHILOSOPHY', 'HISTORY']

gateway_agent = Gateway(categories=CATEGORIES)

ethics_expert = EthicsExpert()
philosophy_expert = PhilosophyExpert()
history_expert = HistoryExpert()

critic_agent = Critic()
synthesizer_agent = Synthesizer()

user_query = 'What does Buddhism say about stealing?'

gateway_response = gateway_agent.chat(user_input=user_query)

if gateway_response == 'NO':
    print("I'm sorry. This chatbot is only equipped to answer questions about Buddhism. If your question is about Buddhism, try rephrasing.")

else:
    if gateway_response.upper() == "ETHICS":
        domain_expert_response = ethics_expert.chat(user_input=user_query)
    elif gateway_response.upper() == "PHILOSOPHY":
        domain_expert_response = philosophy_expert.chat(user_input=user_query)
    elif gateway_response.upper() == "HISTORY":
        domain_expert_response = history_expert.chat(user_input=user_query)
    
    if domain_expert_response:

        critic_response = critic_agent.chat(
                {'user_query': user_query, 
                'current_answer': domain_expert_response}
            )
        
        if critic_response == "YES":
            print(domain_expert_response)

        else:
            synthesizer_response = synthesizer_agent.chat(
                                            {
                                                'user_query': user_query,
                                                'current_answer': domain_expert_response,
                                                'feedback': critic_response
                                            }
                                        )
            
            print(synthesizer_response)
