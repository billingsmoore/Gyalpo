# Gyalpo: Buddhist AI Chatbot

This repository contains the source and documentation for Gyalpo, a chatbot for Buddhist question answering. The current implementation is provisional and for proof of concept purposes.

You can read more about the general idea in [Gyalpo: Toward Effective Buddhist Question Answering With Large Language Models](https://forum.openpecha.org/t/gyalpo-toward-effective-buddhist-question-answering-with-large-language-models/421)

If you are interested in contributing, please do not hesitate to contact me at billingsmoore [at] gmail [dot] com with 'Gyalpo' in the subject line.

## State of the Project

Gyalpo is a multi-agent question-answering chatbot that relies on a 'Master Control Program'-style supervisory implementation.

The proof of concept implementation uses Gemma3n running on a local Ollama server, but this can be set very easily to a different Ollam compatible model of your choice.

The basic pipeline of the proof of concept implementation consists of the follwing agents:

1. Gateway Agent: verifies that the user input is relevant to Buddhism and decides which Domain Expert to refer the query to.
2. Domain Experts: these agents use a RAG to find and summarize additional context for the user's question

The MCP for the proof of concept implementation is relatively simple and is shown in full below:

```python
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
```

At present, the best way to contribute is to [create additional Domain Experts](./doc/CreatingNewExperts.md), or to help refine the chat logging system. Future work will be focused on implementing the fuller pipeline described in [Gyalpo: Toward Effective Buddhist Question Answering With Large Language Models](https://forum.openpecha.org/t/gyalpo-toward-effective-buddhist-question-answering-with-large-language-models/421).