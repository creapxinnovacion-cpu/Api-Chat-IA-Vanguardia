import re

CONTACT_KEYWORDS = [
    "whatsapp", "whatapp", "wsp",
    "facebook", "fb",
    "instagram", "ig",
    "correo", "email", "contacto", "teléfono"
]

def usuario_pide_contacto(texto: str) -> bool:
    texto = texto.lower()
    return any(palabra in texto for palabra in CONTACT_KEYWORDS)
