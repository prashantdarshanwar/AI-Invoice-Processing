def check_duplicate(invoice_no, db):

    existing = db.query(Invoice)\
        .filter(
            Invoice.invoice_number == invoice_no
        ).first()

    return existing