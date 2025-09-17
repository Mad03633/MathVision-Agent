from typing import Optional
from PIL import Image
from io import BytesIO
import pytesseract

class AIServices:
    def __init__(self, ocr_engine: str = "pytesseract"):
        self.ocr_engine = ocr_engine
    
    def ocr_image_bytes(self, content: bytes) -> str:
        if self.ocr_engine == "pytesseract":
            image = Image.open(BytesIO(content)).convert("RGB")
            text = pytesseract.image_to_string(image, lang="eng+rus+kaz")
            return text.strip()
        else:
            raise NotImplementedError("Only pytesseract OCR is implemented currently.")

    def latexify(self, text: str) -> Optional[str]:
        """
        Future LLM feature.
        """
        return None