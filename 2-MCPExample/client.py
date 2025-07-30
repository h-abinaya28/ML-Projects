from http import client
import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import httpx


from dotenv import load_dotenv
load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000",
                "transport": "streamable-http",
            }
        }
    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    http_client = httpx.Client(verify=False)
    model = ChatGroq(
        model="qwen-qwq-32b",
        api_key=os.getenv("GROQ_API_KEY"),
        http_client=http_client
    )
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.invoke(
        {"messages": [{"role": "user", "content": "What is 5 + 3?"}]}
    )

    math_response["messages"][-1].content.pretty_print()


asyncio.run(main())
