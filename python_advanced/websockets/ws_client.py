#!/usr/bin/env python

"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as websocket:
        await websocket.send(text)
        message = await websocket.recv()
        return message

def main():
    response = asyncio.run(connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket"))
    print(response, end="")

if __name__ == "__main__":
    main()
