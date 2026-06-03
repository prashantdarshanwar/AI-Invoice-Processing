import re


class InvoiceExtractor:

    @staticmethod
    def extract(text: str):

        # Invoice Number
        invoice_match = re.search(
            r"INV-\d+",
            text,
            re.IGNORECASE
        )

        invoice_number = (
            invoice_match.group()
            if invoice_match
            else None
        )

        # Invoice Date
        date_match = re.search(
            r"Invoice Date:\s*(\d{2}/\d{2}/\d{4})",
            text,
            re.IGNORECASE
        )

        invoice_date = (
            date_match.group(1)
            if date_match
            else None
        )

        # Total Amount
        amount_match = re.search(
            r"Total Amount:\s*([\d.]+)",
            text,
            re.IGNORECASE
        )

        amount = (
            float(amount_match.group(1))
            if amount_match
            else None
        )

        # Vendor
        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        vendor = lines[0] if lines else None

        # Confidence Score
        confidence_score = 50

        if vendor:
            confidence_score += 10

        if invoice_number:
            confidence_score += 20

        if amount:
            confidence_score += 10

        if invoice_date:
            confidence_score += 10

        return {
            "vendor": vendor,
            "invoice_number": invoice_number,
            "amount": amount,
            "invoice_date": invoice_date,
            "confidence_score": confidence_score
        }


def extract_invoice_data(text: str):
    return InvoiceExtractor.extract(text)