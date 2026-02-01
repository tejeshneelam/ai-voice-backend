from openai import OpenAI

# Create OpenAI client (API key should be in environment variable)
client = OpenAI()

def transcribe_audio(audio_path: str) -> str:
    """
    Takes path of an audio file and returns transcribed text
    """
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text
