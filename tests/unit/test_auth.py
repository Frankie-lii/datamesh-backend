#!/usr/bin/env python3
import pytest
from src.auth.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_login_success():
        response = client.post("/login", json={"username": "testuser", "password": "password123"})
            assert response.status_code == 200
                assert "access_token" in response.json()

                def test_login_failure():
                        response = client.post("/login", json={"username": "wronguser", "password": "wrongpassword"})
                            assert response.status_code == 401

