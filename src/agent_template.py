"""
This file is the basic Agent Class template. All agents in the pipeline should be instances of this class.

This module defines the abstract base class (ABC) for all agents in the pipeline.
All concrete agent implementations should inherit from this class and implement
the required abstract methods.

The class provides:

    Standardized agent initialization

    Basic chat functionality using Ollama models

    Automatic interaction logging

    Abstract methods for system and user prompts that must be implemented by subclasses

Attributes:
    sys_message (dict): System message configuration with role and content
    user_message_default (str): Default user message if none is provided

Methods:
    chat(): Handles the core chat interaction with the LLM
    system_prompt(): Abstract method for agent's system instructions
    user_prompt(): Abstract method for processing user input

Usage:

class MyAgent(Agent):
    def system_prompt(self):
    return "Custom system instructions"

    def user_prompt(self, input):
        return f"Processed: {input}"

agent = MyAgent()
response = agent.chat("Hello")

"""

import abc
import ollama
from utils.logging_utils import log_interaction

class Agent(abc.ABC):
    def __init__(self):
        self.sys_message = {'role': 'system', 'content': self.system_prompt()}
        self.user_message_default = "Introduce yourself."

    @abc.abstractmethod
    def system_prompt(self):
        """Return the system prompt content"""
        pass
    
    @abc.abstractmethod
    def user_prompt(self):
        pass

    def chat(self, user_input=None, model="gemma3n"):

        if user_input:
            user_content = self.user_prompt(user_input)
        else:
            user_content = self.user_message_default

        # print(user_content) # for debugging

        user_message = {'role': 'user', 'content': user_content}

        response = ollama.chat(model=model, messages=[self.sys_message, user_message])

        # Log the interaction
        log_interaction(
            agent_name=self.name,
            user_input=user_message['content'],
            response=str(response['message']['content'].strip()),
        )

        return response['message']['content'].strip()