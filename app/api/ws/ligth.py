import asyncio
from datetime import datetime, timedelta, timezone

from bot import notify_all_users
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from repositories.wifi_repository import WifiRepository


class LightStatusMonitor:
    def __init__(self):
        self.clients = []
        self.last_ping_time = datetime.now(timezone.utc)
        self.light_status = True
        self.wifi_repository = WifiRepository()

    async def websocket_endpoint(self, websocket: WebSocket):
        await websocket.accept()
        self.clients.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                self.last_ping_time = datetime.now(timezone.utc)
                if not self.light_status:
                    self.light_status = True
                    await notify_all_users("Cвітло появилося!")
                    self.wifi_repository.create_wifi_record(is_powered=True)
                await websocket.send_text(data)
        except WebSocketDisconnect:
            self.clients.remove(websocket)

    async def check_light_status(self):
        while True:
            await asyncio.sleep(60)
            if datetime.now(timezone.utc) - self.last_ping_time > timedelta(minutes=1):
                if self.light_status:
                    self.light_status = False
                    self.wifi_repository.create_wifi_record(is_powered=False)
                    await notify_all_users("Світло пропало!")


def init_websocket_server(app: FastAPI):
    monitor = LightStatusMonitor()
    app.websocket("/ws")(monitor.websocket_endpoint)
    app.add_event_handler(
        "startup", lambda: asyncio.create_task(monitor.check_light_status())
    )
