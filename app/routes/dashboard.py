from fastapi import APIRouter
from fastapi import Depends
from app.database import Base
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Invoice

router = APIRouter()


@router.get("/")
def get_dashboard_stats(
    db: Session = Depends(get_db)
):

    total = db.query(
        Invoice
    ).count()

    approved = db.query(
        Invoice
    ).filter(
        Invoice.status == "Approved"
    ).count()

    pending = db.query(
        Invoice
    ).filter(
        Invoice.status == "Pending"
    ).count()

    rejected = db.query(
        Invoice
    ).filter(
        Invoice.status == "Rejected"
    ).count()

    error = db.query(
        Invoice
    ).filter(
        Invoice.status == "Error"
    ).count()

    return {
        "total_invoices": total,
        "approved": approved,
        "pending": pending,
        "rejected": rejected,
        "error": error
    }