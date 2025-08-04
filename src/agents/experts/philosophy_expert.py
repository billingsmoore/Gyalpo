from agent_template import Agent
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

class PhilosophyExpert(Agent):
    def __init__(self, db_path='agents/experts/expert_dbs/philosophy_db', domain='Buddhist Philosophy'):
        super().__init__()
        # Initialize Chroma DB
        self.domain = domain
        self.embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory=db_path, embedding_function=self.embedding_function)

    def system_prompt(self):
        return f"""You are an expert in {self.domain}. You provide summaries of important context to answer user questions."""

    def user_prompt(self, user_input):

        context = self.get_context(user_input)

        return f"""Summarize the provided context for a response to the user query.
                user_query: {user_input} 
                context: {context}
                """

    def get_context(self, query, k=3):
        # Search the Chroma DB for relevant documents
        results = self.db.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in results])