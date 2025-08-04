"""
This file contains a minimal proof of concept implementation that demonstrate multiple agents and retreivel augmentation.
"""

from agents.experts.ethics_expert import EthicsExpert
from agents.gateway_agent import Gateway

CATEGORIES = ['ethics', 'philosophy', 'history']

gateway_agent = Gateway(categories=CATEGORIES)
ethics_agent = EthicsExpert()

user_query = 'What does Buddhism say about stealing?'

gateway_response = gateway_agent.chat(user_input=user_query)
if gateway_response == 'NO':
    print("I'm sorry. This chatbot is only equipped to answer questions about Buddhism. If your question is about Buddhism, try rephrasing.")
else:
    if gateway_response.upper() == "ETHICS":
        response = ethics_agent.chat(user_input=user_query)

print(response)