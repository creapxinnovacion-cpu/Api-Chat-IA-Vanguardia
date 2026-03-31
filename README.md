# Agente Vanguardia IA

Este es el backend para el Agente Vanguardia IA, un chatbot diseñado para asistir a los usuarios en la consulta de propiedades (bienes raíces) y conectar con asesores de la empresa. Está construido utilizando **FastAPI** y se integra con el modelo **Llama-3.1-8b** mediante la API de **Groq** para generar respuestas conversacionales contextuales.

## 🚀 Características

* **Chatbot Inmobiliario con IA:** Responde preguntas sobre propiedades apoyándose de la Inteligencia Artificial (Llama 3.1).
* **Búsqueda Estructurada:** Busca propiedades por tipo (ej., "Casa", "Apartamento") o por ubicación.
* **Integración con Canales Oficiales:** Proporciona un rápido acceso de contacto (WhatsApp, Correo, etc.) si el usuario los pide explícitamente.
* **Manejo Seguro de Errores:** Ocultación de trazas de seguridad e implementación de un timeout contra denegaciones de servicio y problemas de latencia de APIS externas.
* **CORS Configurado:** Listo para interactuar con aplicaciones en React (Vite).

## 🗂 Estructura del Proyecto

```bash
Agente-vanguardia/
│
├── app/                      # Código principal del backend
│   ├── core/                 # Configuraciones centrales y contactos
│   │   ├── config.py         # Variables de entorno y llaves
│   │   ├── contactos.py      # Datos de contacto oficiales
│   │   └── security.py       # Utilidades de seguridad (opcional)
│   ├── ia/                   # Lógica de Inteligencia Artificial
│   │   ├── groq_client.py    # Cliente API de Groq y LLM
│   │   ├── system_prompt.py  # Instrucciones base (System Prompt) para la IA
│   │   └── contacto.py       # Prompts referidos a contactos
│   ├── routers/              # Enrutadores o Endpoints (Controladores API)
│   │   ├── chat.py           # Endpoint `/chat` principal de la API
│   │   └── admin.py          # (Opcional) endpoints de administración
│   ├── services/             # Reglas de negocio y simulación de base de datos
│   │   └── propiedades.py    # Búsqueda y gestión de los recursos inmobiliarios
│   └── main.py               # Punto de entrada de la aplicación FastAPI
│
├── .env                      # Variables de Entorno Locales (Requerido, NO subido en git)
├── .gitignore                # Archivos ignorados por Git
└── requirements.txt          # Dependencias y módulos requeridos (pip)
```

## 🛠 Instalación y Configuración

**1. Clonar el repositorio y entrar a la carpeta**
```bash
git clone <URL_DEL_REPOSITORIO>
cd Agente-vanguardia
```

**2. Crear y activar el entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar las dependencias**
```bash
pip install -r requirements.txt
```

**4. Configurar las variables de entorno**
Crea un archivo llamado `.env` en la raíz de tu proyecto e incluye las siguientes variables sustituyéndolas por la tuya.

```env
GROQ_API_KEY=tu_clave_api_de_groq_aqui
MODEL_NAME=llama-3.1-8b-instant
```

> **⚠️ Advertencia de Seguridad:** ¡NUNCA subas tu archivo `.env` o la llave `GROQ_API_KEY` a GitHub! El archivo `.gitignore` ha sido configurado para prevenir esto.

## 🏃 Ejecución

Inicia el servidor backend utilizando Uvicorn:

```bash
uvicorn app.main:app --reload
```

El servidor estará corriendo en: `http://127.0.0.1:8000`

## 📖 Documentación de la API (Swagger UI)

FastAPI genera la documentación automáticamente. Puedes probar los endpoints directamente visitando:
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoint de Chat Principal
**POST** `/chat/`

**Ejemplo de Petición (JSON):**
```json
{
  "mensaje": "¿Tienes alguna casa en la playa disponible?",
  "tipo": "Casa",
  "ubicacion": "playa"
}
```

## 🔐 Correcciones de Seguridad Aplicadas:

- **`.gitignore` Añadido:** Prevención de fugas de llaves en los repositorios o versionado global.
- **Divulgación de Información Prevista:** Los errores internos del sistema ya no exponen variables ni el estado del servidor a los usuarios finales (cambiado en `/app/routers/chat.py`).
- **Prevención de Agotamiento de Recursos (DoS Parcial):** Se agregó un atributo de *timeout* (15s) en los requests hechos a las APIs de terceros (Groq) evitando el encolamiento de hilos ("threads") huérfanos del backend en `app/ia/groq_client.py`.
