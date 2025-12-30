from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    name: str = Field(description="The name of the source")
    url: str = Field(description="The url of the source")   

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer: str = Field(description="The answer to the question")
    sources: list[Source] = Field(description="The sources used to answer the question")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages": HumanMessage(content="what is the temperature in dallas texas today?")})
    print(response)

if __name__ == "__main__":
    main()
