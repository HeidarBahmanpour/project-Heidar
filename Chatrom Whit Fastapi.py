from fastapi import FastAPI, WebSocket

app = FastAPI()


                                #  WebSocket  لیستی از اتصال‌های 
websocket_connections = []


# روت برای صفحه وب
@app.get("/")
def read_root():
    return {"message": "Welcome to the home chat room!"}



                                #  WebSocket روت برای برقراری اتصال 
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    websocket_connections.append((client_id, websocket))


try:
    while True:
            data = await websocket.receive_text()


                                  # ارسال پیام به همه اتصال‌ها
            for conn_id, conn in websocket_connections:
                await conn.send_text(f"Client {client_id} says: {data}")
        except Exception as e:
            
    print(f"WebSocket Error: {e}")
finally:
                                # حذف اتصال از لیست بعد از قطع شدن
        websocket_connections.remove((client_id, websocket))
