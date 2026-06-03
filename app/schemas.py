from pydantic import BaseModel
from typing import Optional


# ==========================
# Base Schema
# ==========================

class InvoiceBase(BaseModel):
    vendor: Optional[str] = None
    invoice_number: Optional[str] = None
    amount: Optional[float] = None
    invoice_date: Optional[str] = None
    status: Optional[str] = "Pending"
    confidence_score: Optional[float] = 0.0


# ==========================
# Create Invoice
# ==========================

class InvoiceCreate(InvoiceBase):
    pass


# ==========================
# Response Schema
# ==========================

class InvoiceResponse(InvoiceBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# Update Status
# ==========================

class InvoiceStatusUpdate(BaseModel):
    status: str


# ==========================
# Dashboard Response
# ==========================

class DashboardStats(BaseModel):
    total_invoices: int
    approved: int
    pending: int
    rejected: int