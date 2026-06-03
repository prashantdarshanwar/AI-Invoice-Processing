from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from app.database import Base
from app.database import Base


class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    vendor = Column(
        String,
        nullable=True
    )

    invoice_number = Column(
        String,
        unique=True,
        nullable=True
    )

    amount = Column(
        Float,
        nullable=True
    )

    invoice_date = Column(
        String,
        nullable=True
    )

    confidence_score = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="Pending"
    )