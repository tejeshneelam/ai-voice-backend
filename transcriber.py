import whisper

# Load the Whisper model once
model = whisper.load_model("tiny")

def transcribe_audio(audio_path: str) -> str:
    """
    Takes path of an audio file and returns transcribed text
    """
    result = model.transcribe(audio_path)
    return result["text"]
