#!/usr/bin/env python3

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def echo(websocket):
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        print("Interacting with closed conenction")


async def main():
    server = await serve(echo, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
