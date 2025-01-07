#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

app = FastAPI()

class User(BaseModel):
        username: str
            password: str

            users_db = {
                        "testuser": {"username": "testuser", "password": "password123"}
                        }

            def create_token(username: str):
                    expiration = datetime.utcnow() + timedelta(hours=1)
                        payload = {"sub": username, "exp": expiration}
                            return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

                        @app.post("/login")
                        def login(user: User):
                                if user.username in users_db and users_db[user.username]["password"] == user.password:
                                            token = create_token(user.username)
                                                    return {"access_token": token}
                                                    raise HTTPException(status_code=401, detail="Invalid credentials")

                                                @app.get("/verify")
                                                def verify_token(token: str):
                                                        try:
                                                                    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                                                                            return {"username": decoded["sub"]}
                                                                            except jwt.ExpiredSignatureError:
                                                                                        raise HTTPException(status_code=401, detail="Token expired")
                                                                                        except jwt.InvalidTokenError:
                                                                                                    raise HTTPException(status_code=401, detail="Invalid token")

