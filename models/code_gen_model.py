from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI


class CodeGenModel:
    def __init__(self):
        # Initialize the LLM
        self.llm = ChatOpenAI(
            model='llama3.2',
            base_url='http://127.0.0.1:8080',  # Replace with your server's address
            api_key='nokey'  # If authentication is not required
        )

    def generate_code(self, prompt):
        # Define the agent
        code_agent = Agent(
            role="Code Generator",
            goal="Generate Python 3.10 code based on the provided prompt.",
            llm=self.llm
        )

        # Define the task
        task = Task(
            description=prompt,
            agent=code_agent
        )

        # Create the crew
        crew = Crew(
            agents=[code_agent],
            tasks=[task]
        )

        result = crew.kickoff()
        return result[0].result
