import asyncio
from websockets.asyncio.server import serve

connectedSockets = []

async def echo(websocket):
    connectedSockets.append(websocket)
    print(connectedSockets)

    async for message in websocket:

        for i in connectedSockets:
            await i.send(message)
            print(message)



async def main():
    async with serve(echo, "localhost", 8765) as server:
        await server.serve_forever()
        
async def main():
    async with connect("ws://localhost:8765") as websocket:
        while 1:
            msg = str(input())
            await websocket.send(msg)
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(main())

