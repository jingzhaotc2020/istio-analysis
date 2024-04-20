from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/forward_request/")
async def create_item(request: Request, request_data: dict):
    print('/forward_request/请求',request.headers)
    url = request_data.get('url')
    method = request_data.get('method')
    response = requests.request(method=method, url=url)
    print('代理发来的响应',response.headers)
    return response.text

import socket
# print(socket.gethostname())

@app.get("/")
async def create_item(request: Request):
    print('/请求',request.headers)
    return 'hello', socket.gethostname()

@app.get("{full_path:path}")  #匹配所有路径，返回路径信息
async def capture_routes(full_path: str):
    return full_path