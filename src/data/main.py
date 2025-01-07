#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class DataItem(BaseModel):
        id: str
            name: str
                description: str

                data_store = {}

                @app.post("/data")
                def create_item(item: DataItem):
                        if item.id in data_store:
                                    raise HTTPException(status_code=400, detail="Item already exists")
                                    data_store[item.id] = item
                                        return {"message": "Item created", "item": item}

                                    @app.get("/data/{item_id}")
                                    def get_item(item_id: str):
                                            if item_id in data_store:
                                                        return data_store[item_id]
                                                        raise HTTPException(status_code=404, detail="Item not found")

                                                    @app.delete("/data/{item_id}")
                                                    def delete_item(item_id: str):
                                                            if item_id in data_store:
                                                                        del data_store[item_id]
                                                                                return {"message": "Item deleted"}
                                                                                raise HTTPException(status_code=404, detail="Item not found")

