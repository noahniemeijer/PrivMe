import asyncio
from websockets.asyncio.client import connect


async def main():
    async with connect("ws://localhost:8765") as websocket:
        while 1:
            msg = str(input())
            await websocket.send(msg)
            message = await websocket.recv()


if __name__ == "__main__":
    asyncio.run(main())
