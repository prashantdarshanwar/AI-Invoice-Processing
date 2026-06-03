class InvoiceValidator:

    @staticmethod
    def validate(data):

        errors = []

        # Invoice Number Validation
        invoice_number = data.get(
            "invoice_number"
        )

        if not invoice_number:
            errors.append(
                "Invoice Number Missing"
            )

        # Amount Validation
        amount = data.get(
            "amount"
        )

        if amount is None:
            errors.append(
                "Amount Missing"
            )

        elif amount <= 0:
            errors.append(
                "Invalid Amount"
            )

        # Vendor Validation
        vendor = data.get(
            "vendor"
        )

        if not vendor:
            errors.append(
                "Vendor Missing"
            )

        # Invoice Date Validation
        invoice_date = data.get(
            "invoice_date"
        )

        if not invoice_date:
            errors.append(
                "Invoice Date Missing"
            )

        return errors


def validate_invoice(data):
    return InvoiceValidator.validate(data)