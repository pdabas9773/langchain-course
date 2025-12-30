from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
load_dotenv()
tavily = TavilyClient()
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for {query}")

    return tavily.search(query)

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages": HumanMessage(content="what is the weather in dallas and what is the temperature?")})
    print(response)

if __name__ == "__main__":
    main()
