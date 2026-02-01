from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from transcriber import transcribe_audio
from summarizer import summarize_text

app = FastAPI(title="AI Voice Note Summarizer")

# ✅ ADD THIS (CORS CONFIG)
origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize-audio")
async def summarize_audio(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcription = transcribe_audio(file_path)
    summary = summarize_text(transcription)

    os.remove(file_path)

    return {
        "transcription": transcription,
        "summary": summary
    }
