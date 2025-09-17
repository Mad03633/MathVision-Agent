from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import ocr, solver


app = FastAPI(title="MathVision Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(solver.router, prefix="/solve", tags=["Solver"])
app.include_router(ocr.router, prefix="/ocr", tags=["OCR"])

@app.get("/")
def root():
    return {"message": "MathVision Agent Backend is running"}