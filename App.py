from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers import AiRouters


APP = FastAPI()
APP.include_router(AiRouters.Router)

APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "*" por ["http://127.0.0.1:5500&quot;] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

@APP.get("/")
def index():
    return {"mensaje": "API RUNNING"}

