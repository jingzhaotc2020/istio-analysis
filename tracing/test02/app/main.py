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

follow_headers = ['x-request-id',
    'x-request-id',
    'x-b3-traceid',
    'x-b3-spanid',
    'x-b3-parentspanid',
    'x-b3-sampled',
    'x-b3-flags',
]

@app.post("/forward_request/")
async def create_item(request: Request, request_data: dict):
    print('/forward_request/请求',request.headers)
    url = request_data.get('url')
    method = request_data.get('method')

    headers = dict()
    for ihdr in follow_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val

    response = requests.request(method=method, url=url, headers=headers)
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