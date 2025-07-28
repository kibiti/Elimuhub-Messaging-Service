import os
import requests

BSP_API_URL = os.getenv("BSP_API_URL")
BSP_API_KEY = os.getenv("BSP_API_KEY")

def send_message(phone_number, template_name, template_params):
    url = f"{BSP_API_URL}/messages"
    headers = {
        "Authorization": f"Bearer {BSP_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": phone_number,
        "template": {
            "name": template_name,
            "parameters": template_params
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
