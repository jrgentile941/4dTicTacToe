import asyncio
import websockets

async def hello():
    uri = "ws://scienceandpizza.com:80"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello())