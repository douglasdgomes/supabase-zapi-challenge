import requests

from config.settings import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_CLIENT_TOKEN
)

URL = (
    f"https://api.z-api.io/instances/"
    f"{ZAPI_INSTANCE_ID}/token/"
    f"{ZAPI_TOKEN}/send-text"
)

def send_message(phone: str, message: str) -> dict:
    payload = {
        "phone": phone,
        "message": message
    }

    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(
        URL,
        json=payload,
        headers=headers,
        timeout=30
    )

    if not response.ok:
        print(response.text)

    response.raise_for_status()

    return response.json()