import os

from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv


load_dotenv()

# Set for proxy
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class CodeGenModel:
    def __init__(self):
        # Initialize the LLM
        self.llm = LLM(
            model="openai/Llama-3.2-3B-Instruct",
            base_url="http://127.0.0.1:8080/v1",
        )

    def generate_code(self, prompt):
        # Define the agent
        code_agent = Agent(
            role="Code Generator",
            backstory="A specialized AI agent designed to generate Python 3.11 code based on user prompts.",
            goal="Generate Python 3.11 code based on the provided prompt.",
            llm=self.llm
        )

        # Define the task
        task = Task(
            description=prompt,
            agent=code_agent,
            expected_output="Python 3.11 code for the described function"
        )

        # Create the crew
        crew = Crew(
            agents=[code_agent],
            tasks=[task]
        )

        result = crew.kickoff()
        return result
