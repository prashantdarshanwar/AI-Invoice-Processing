from fastapi import FastAPI

from app.database import engine
from app.model import Base
from app.routes.invoice import router as invoice_router
from app.routes.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Invoice AI MVP"
)

app.include_router(
    invoice_router,
    prefix="/invoice",
    tags=["Invoice"]
)

app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)


@app.get("/")
def home():
    return {
        "message": "Invoice AI System Running"
    }