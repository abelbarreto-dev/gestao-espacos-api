from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.routes.autorizacao_routes import authorize_routes
from src.routes.espaco_publico_routes import espaco_publico_routes
from src.routes.historico_routes import story_routes
from src.routes.periodo_routes import periodo_routes
from src.routes.solicitacao_routes import solicitacao_routes
from src.routes.solicitante_routes import solicit_router
from src.routes.tipo_evento_routes import tipo_evento_routes
from src.routes.usuario_routes import usuario_routes

app = FastAPI(openapi_prefix="/api/v1/gestao-espacos")


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://www.gestaoespacosconectados.com.br",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authorize_routes)
app.include_router(espaco_publico_routes)
app.include_router(story_routes)
app.include_router(periodo_routes)
app.include_router(solicitacao_routes)
app.include_router(solicit_router)
app.include_router(tipo_evento_routes)
app.include_router(usuario_routes)
