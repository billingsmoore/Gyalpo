#Buddhist Q&A System - Proof of Concept Implementation

This file demonstrates a multi-agent system for answering Buddhist questions using:
1. Gateway classification
2. Domain-specific expertise
3. Quality assurance critique
4. Answer synthesis

The system workflow:
1. Gateway determines if question is Buddhist-related and categorizes it
2. Appropriate domain expert generates initial answer
3. Critic evaluates answer quality
4. Synthesizer produces final response incorporating feedback

Agents:
- Gateway: Initial question classifier
- EthicsExpert: Handles moral/conduct questions
- PhilosophyExpert: Addresses metaphysical concepts  
- HistoryExpert: Covers historical developments
- Critic: Ensures answer quality
- Synthesizer: Produces polished final answers
"""

from agents.gateway_agent import Gateway
from agents.experts.ethics_expert import EthicsExpert
from agents.experts.philosophy_expert import PhilosophyExpert
from agents.experts.history_expert import HistoryExpert
from agents.critic_agent import Critic
from agents.synthesizer_agent import Synthesizer

## System Configuration
CATEGORIES = ['ETHICS', 'PHILOSOPHY', 'HISTORY']

## Initialize Agent Instances
gateway_agent = Gateway(categories=CATEGORIES)
ethics_expert = EthicsExpert()
philosophy_expert = PhilosophyExpert()
history_expert = HistoryExpert()
critic_agent = Critic()
synthesizer_agent = Synthesizer()

## Example Query Processing
def process_query(user_query):
    """
    Process a user question through the full agent pipeline
    
    Args:
        user_query (str): The question to be answered
        
    Returns:
        str: The system's final response
    """
    # Step 1: Gateway Classification
    gateway_response = gateway_agent.chat(user_input=user_query)
    
    if gateway_response == 'NO':
        return "I'm sorry. This chatbot is only equipped to answer questions about Buddhism. If your question is about Buddhism, try rephrasing."
    
    # Step 2: Domain Expert Response
    expert_mapping = {
        "ETHICS": ethics_expert,
        "PHILOSOPHY": philosophy_expert, 
        "HISTORY": history_expert
    }
    
    domain_expert = expert_mapping.get(gateway_response.upper())
    if not domain_expert:
        return "Error: Unrecognized category"
        
    domain_response = domain_expert.chat(user_input=user_query)
    
    # Step 3: Quality Assurance
    critic_response = critic_agent.chat({
        'user_query': user_query,
        'current_answer': domain_response
    })
    
    # Step 4: Finalize Response
    if critic_response == "YES":
        return domain_response
    else:
        return synthesizer_agent.chat({
            'user_query': user_query,
            'current_answer': domain_response,
            'feedback': critic_response
        })

## Demonstration
if __name__ == "__main__":
    test_question = "What does Buddhism say about stealing?"
    print(f"Question: {test_question}")
    print(f"Answer: {process_query(test_question)}")
    
    # Additional test cases could be added here
    # test_question2 = "Explain the concept of karma"
    # print(process_query(test_question2))

Key Features:
- Modular agent architecture
- Clear processing pipeline
- Quality control through critique
- Context-aware response synthesis
- Easy to extend with additional experts
"""