from services.ocr import OCRService
from services.extractor import InvoiceExtractor
from services.validator import InvoiceValidator


def process_invoice(path):

    if path.endswith(".pdf"):
        text = OCRService.extract_from_pdf(path)
    else:
        text = OCRService.extract_from_image(path)

    data = InvoiceExtractor.extract(text)

    errors = InvoiceValidator.validate(data)

    return {
        "data": data,
        "errors": errors
    }