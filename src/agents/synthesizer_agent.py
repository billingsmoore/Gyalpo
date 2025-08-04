from agent_template import Agent

class Synthesizer(Agent):
    def __init__(self):
        self.name = "Synthesizer"
        super().__init__()

    def system_prompt(self):
        return f"""You are an expert on Buddhism. You synthesize context and feedback to provide high quality answer to user's questions."""
    
    def user_prompt(self, user_input):
        base_prompt = "Synthesize the following into a great answer.\n"
        question = f"Question: {user_input['user_query']}"
        context = f"Context: {user_input.get('context', 'None')}"
        
        if 'current_answer' in user_input:
            answer = f"Answer: {user_input['current_answer']}"
            feedback = f"Critic Feedback: {user_input.get('feedback', '')}"
            return f"{base_prompt}{question}\n{context}\n{answer}\n{feedback}"
        
        return f"{base_prompt}{question}\n{context}"