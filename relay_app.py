from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

HA_URL = os.getenv("HOME_ASSISTANT_URL")
HA_TOKEN = os.getenv("HOME_ASSISTANT_TOKEN")

headers = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def relay_request(path: str, request: Request):
    url = f"{HA_URL}/api/{path}"
    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            json=await request.json(),
            params=request.query_params,
        )
        return response.json()
    except Exception as e:
        raise Exception(str(e))