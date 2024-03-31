import os
import asyncio
from web.gemini import Gemini
from dotenv import dotenv_values


async def main():
    config = dotenv_values(".env")
    g = Gemini(config["EMAIL"], config["PASSWORD"])
    g.initialize()

if __name__ == "__main__":
    asyncio.run(main())
