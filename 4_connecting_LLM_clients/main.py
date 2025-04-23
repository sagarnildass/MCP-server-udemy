import asyncio
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

async def main():
    print("Hello, world!")
    
if __name__ == "__main__":
    asyncio.run(main())

