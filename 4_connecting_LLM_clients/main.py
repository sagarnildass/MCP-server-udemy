import asyncio
from dotenv import load_dotenv, find_dotenv
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

load_dotenv(find_dotenv())

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=[
        "/media/sagarnildass/d16f4193-0a7d-4eb8-8b71-235a0fc1224e/home/sagarnildass/python_notebooks/Udemy/MCP_servers/4_connecting_LLM_clients/servers/math_server.py"
    ]
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)

            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3 ?")]})
            print(result["messages"][-1].content)
    
if __name__ == "__main__":
    asyncio.run(main())

