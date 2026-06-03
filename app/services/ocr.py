import fitz
import pytesseract

from PIL import Image


# Windows Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRService:

    @staticmethod
    def extract_from_image(image_path: str) -> str:
        """
        Extract text from image file
        """

        try:

            image = Image.open(image_path)

            text = pytesseract.image_to_string(
                image
            )

            return text

        except Exception as e:

            print(
                f"Image OCR Error: {e}"
            )

            return ""

    @staticmethod
    def extract_from_pdf(pdf_path: str) -> str:
        """
        Extract text from PDF
        """

        text = ""

        try:

            pdf = fitz.open(pdf_path)

            for page in pdf:

                page_text = page.get_text()

                text += page_text

            pdf.close()

            return text

        except Exception as e:

            print(
                f"PDF OCR Error: {e}"
            )

            return ""


def extract_text(file_path: str) -> str:
    """
    Common OCR function used by invoice route
    """

    if file_path.lower().endswith(".pdf"):

        text = OCRService.extract_from_pdf(
            file_path
        )

        print("\n===== OCR PDF TEXT =====")
        print(text)
        print("========================\n")

        return text

    elif file_path.lower().endswith(
        (".png", ".jpg", ".jpeg", ".bmp")
    ):

        text = OCRService.extract_from_image(
            file_path
        )

        print("\n===== OCR IMAGE TEXT =====")
        print(text)
        print("==========================\n")

        return text

    raise ValueError(
        f"Unsupported file type: {file_path}"
    )