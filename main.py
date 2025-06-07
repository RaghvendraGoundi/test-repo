from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import PyPDF2

app = FastAPI()

@app.get("/")
def read_root():    
    return JSONResponse(status_code=200, content={"message": "Welcome to the PDF Text Extractor API"})

@app.get("/extract-text")
def extract_text():
    try:
        return JSONResponse(status_code=200, content={"text": "This is a sample text"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
