from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException
from app.database import get_db
from app.model import Invoice

from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Invoice

from app.utils.file_handler import save_upload_file

from app.services.ocr import extract_text
from app.services.extractor import extract_invoice_data
from app.services.validator import validate_invoice

router = APIRouter()


# ==========================
# Upload Invoice
# ==========================

@router.post("/upload")
async def upload_invoice(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = await save_upload_file(file)

    text = extract_text(file_path)

    data = extract_invoice_data(text)

    errors = validate_invoice(data)

    # Duplicate Check
    existing = db.query(Invoice).filter(
        Invoice.invoice_number ==
        data.get("invoice_number")
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Duplicate Invoice"
        )

    invoice = Invoice(
        vendor=data.get("vendor"),
        invoice_number=data.get(
            "invoice_number"
        ),
        amount=data.get("amount"),
        confidence_score=data.get(
            "confidence_score",
            85.0
        ),
        status="Pending"
        if not errors
        else "Error"
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return {
        "invoice_id": invoice.id,
        "status": invoice.status,
        "data": data,
        "errors": errors
    }


# ==========================
# Get All Invoices
# ==========================

@router.get("/")
def get_all_invoices(
    db: Session = Depends(get_db)
):

    invoices = db.query(
        Invoice
    ).all()

    return invoices


# ==========================
# Get Invoice By ID
# ==========================

@router.get("/{invoice_id}")
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    invoice = db.query(
        Invoice
    ).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice Not Found"
        )

    return invoice


# ==========================
# Approve Invoice
# ==========================

@router.put("/{invoice_id}/approve")
def approve_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    invoice = db.query(
        Invoice
    ).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice Not Found"
        )

    invoice.status = "Approved"

    db.commit()
    db.refresh(invoice)

    return {
        "message": "Invoice Approved",
        "invoice": invoice
    }


# ==========================
# Reject Invoice
# ==========================

@router.put("/{invoice_id}/reject")
def reject_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    invoice = db.query(
        Invoice
    ).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice Not Found"
        )

    invoice.status = "Rejected"

    db.commit()
    db.refresh(invoice)

    return {
        "message": "Invoice Rejected",
        "invoice": invoice
    }