from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(title="ScopeGuard AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://scopeguard-ai-eight.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)