from fastapi import FastAPI
from api.routes import router

app = FastAPI(title:"ScopeGuard AI")

app.include_router(router)