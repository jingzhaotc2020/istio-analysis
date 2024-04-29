from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import socket

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def create_item(request: Request):
    await asyncio.sleep(5)
    return 'hello', socket.gethostname()

@app.get("{full_path:path}")  #匹配所有路径，返回路径信息和hostname信息
async def capture_routes(full_path: str):
    return full_path, socket.gethostname()