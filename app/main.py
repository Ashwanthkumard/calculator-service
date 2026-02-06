from fastapi import FastAPI
from app.api.calculator import router as calculator_router
from app.core.health import router as health_router

app = FastAPI(title="Calculator Service")

app.include_router(health_router)
app.include_router(calculator_router)
