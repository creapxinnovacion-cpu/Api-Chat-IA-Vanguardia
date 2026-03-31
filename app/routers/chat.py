from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.propiedades import buscar_propiedades
from app.ia.groq_client import consultar_ia
from app.core.contactos import CONTACTOS_OFICIALES

router = APIRouter(prefix="/chat", tags=["Chat Vanguardia-IA"])


class ChatRequest(BaseModel):
    mensaje: str
    tipo: Optional[str] = None
    ubicacion: Optional[str] = None


def usuario_pide_contacto(texto: str) -> bool:
    palabras = [
        "contacto", "correo", "email",
        "facebook", "instagram",
        "whatsapp", "redes", "hablar"
    ]
    texto = texto.lower()
    return any(p in texto for p in palabras)


@router.post("/")
def chat_vanguardia(data: ChatRequest):
    try:
        if usuario_pide_contacto(data.mensaje):
            return {
                "agente": "Vanguardia-IA",
                "tipo": "contacto",
                "mensaje": "📞 Canales oficiales de Vanguardia-IA",
                "links": CONTACTOS_OFICIALES
            }

        propiedades = buscar_propiedades(
            tipo=data.tipo,
            ubicacion=data.ubicacion
        )

        if not propiedades:
            return {
                "agente": "Vanguardia-IA",
                "respuesta": "Actualmente no contamos con propiedades disponibles.",
                "total_propiedades": 0
            }

        contexto = {"propiedades": propiedades}

        respuesta = consultar_ia(contexto, data.mensaje)

        return {
            "agente": "Vanguardia-IA",
            "respuesta": respuesta,
            "total_propiedades": len(propiedades)
        }

    except Exception as e:
        print(f"Error interno en /chat: {e}")
        raise HTTPException(status_code=500, detail="Ha ocurrido un error interno en el servidor.")
