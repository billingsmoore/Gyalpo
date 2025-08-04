from agent_template import Agent

class Critic(Agent):

    def __init__(self):
        self.name = "Critic"
        super().__init__()

    def system_prompt(self):
        return f"""You are an expert critic of Buddhist material. You ensure that answers to user questions are aligned with Buddhist ethics and ideals.
        If if the current answer is acceptable answer "YES" with no additional output. Otherwise, provide feedback on how to improve the answer."""
    
    def user_prompt(self, user_input):
        return f"""Reflect on the suggested answer to the given question.
                Question: {user_input['user_query']}
                Answer: {user_input['current_answer']}
                """