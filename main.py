from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import PyPDF2

app = FastAPI()

@app.get("/extract-text")
def extract_text():
    pdf_path = os.path.join("pdfs", "cover.pdf")
    if not os.path.exists(pdf_path):
        return JSONResponse(status_code=404, content={"error": "PDF not found"})

    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return {"text": text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
