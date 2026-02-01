from transcriber import transcribe_audio
from summarizer import summarize_text

# Step 1: Audio → Text
audio_path = "sample.wav"
print("Transcribing audio...")
transcript = transcribe_audio(audio_path)

print("\nTRANSCRIPTION:")
print(transcript)

# Step 2: Text → Summary
print("\nGenerating summary...")
summary = summarize_text(transcript)

print("\nFINAL SUMMARY:")
print(summary)
