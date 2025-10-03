from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ai_services import AIServices
from app.core.config import settings


router = APIRouter()
ai = AIServices(ocr_engine=settings.OCR_ENGINE)

@router.post("/image")
async def ocr_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    content = await file.read()
    max_bytes = settings.MAX_IMAGE_MB * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=413, detail=f"Image larger than {settings.MAX_IMAGE_MB} MB.")
    try:
        text = ai.ocr_image_bytes(content)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR failed: {e}")