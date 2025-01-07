#!/usr/bin/env python3
import pytest
from src.data.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_item():
        response = client.post("/data", json={"id": "1", "name": "Item1", "description": "Test item"})
            assert response.status_code == 200

            def test_get_item():
                    response = client.get("/data/1")
                        assert response.status_code == 200
                            assert response.json()["name"] == "Item1"

