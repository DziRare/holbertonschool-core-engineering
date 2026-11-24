#!/usr/bin/env python3

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

CONNECTED_CLIENTS = set()


async def echo(websocket):
    CONNECTED_CLIENTS.add(websocket)
    print(CONNECTED_CLIENTS)

    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        print(f"Disconnected {websocket}")
    finally:
        CONNECTED_CLIENTS.remove(websocket)


async def main():
    server = await serve(echo, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
