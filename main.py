from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/socket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Aquí está el web_socket de David Perez")
    await websocket.close()