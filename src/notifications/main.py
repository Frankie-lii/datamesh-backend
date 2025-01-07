#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

class Notification(BaseModel):
        recipient: str
            message: str

            @app.post("/notify")
            async def send_notification(notification: Notification):
                    # Simulate async notification sending
                        await asyncio.sleep(2)
                            return {"status": "Notification sent", "notification": notification}

