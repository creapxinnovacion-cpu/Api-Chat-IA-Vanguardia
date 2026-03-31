import requests
import json
from app.core.config import GROQ_API_KEY, GROQ_API_URL, MODEL_NAME
from app.ia.system_prompt import SYSTEM_PROMPT


def consultar_ia(contexto: dict, mensaje_usuario: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
MENSAJE DEL CLIENTE:
{mensaje_usuario}

DATOS REALES (JSON — NO INVENTAR):
{json.dumps(contexto, ensure_ascii=False)}
"""
            }
        ]
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=15)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
