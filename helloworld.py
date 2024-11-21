from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import toga


def button_handler(widget):
    print("hello world!")

def initialize_llm():
    return ChatOpenAI(
        model="llama3.2",
        base_url="http://127.0.0.1:8080/",
        api_key="nokey"
    )

def build(app):
    box = toga.Box()

    button = toga.Button("Hello world", on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App("Studio from SupaLlama", "ai.supallama.studio", startup=build)


if __name__ == "__main__":
    main().main_loop()
