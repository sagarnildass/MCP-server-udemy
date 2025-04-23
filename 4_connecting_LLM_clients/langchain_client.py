import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI()


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/media/sagarnildass/d16f4193-0a7d-4eb8-8b71-235a0fc1224e/home/sagarnildass/python_notebooks/Udemy/MCP_servers/4_connecting_LLM_clients/servers/math_server.py"
                ],
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        # result = await agent.ainvoke({"messages": "What is 2 + 2?"})
        result = await agent.ainvoke(
            {"messages": "What is the weather in New York?"}
        )

        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
