import os
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTH_KEY = os.getenv("GIGACHAT_AUTH_KEY")
TOKEN_URL = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
API_URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

def get_token():
    headers = {
        "Authorization": f"Bearer {AUTH_KEY}",
        "RqUID": "6f0e3a2c-8b1d-4f5e-9a3c-1d2e3f4a5b6c",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"scope": "GIGACHAT_API_PERS"}
    response = requests.post(TOKEN_URL, headers=headers, data=data, verify=False)
    return response.json()["access_token"]

def ask_gpt(prompt):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload, verify=False)
    return response.json()["choices"][0]["message"]["content"]