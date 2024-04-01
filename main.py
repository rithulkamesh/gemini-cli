import asyncio
import time
from web.gemini import Gemini
from dotenv import dotenv_values


async def main():
    config = dotenv_values(".env")
    g = Gemini()

    if not config["EMAIL"] or not config["PASSWORD"]:
        print("malformed (or missing) email or password in env")
        return

    g.initialize(config["EMAIL"], config["PASSWORD"])
    g.send_message("Give me a sample markdown example")
    time.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
