from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket
from starlette.exceptions import WebSocketException


async def homepage(request):
    return HTMLResponse("<h1>WebSockets<h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except WebSocketException:
        print("Web Socket Disconnected")
    finally:
        await websocket.close()


# async def app(scope, receive, send):
#     websocket = WebSocket(scope=scope, receive=receive, send=send)
#     await websocket.accept()
#     await websocket.send_text('Hello, world!')
#     await websocket.close()

app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
