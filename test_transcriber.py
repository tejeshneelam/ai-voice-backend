from transcriber import transcribe_audio

# Path to your test audio file
audio_file = "sample.wav"

# Call the function and print result
text = transcribe_audio(audio_file)
print("Transcribed Text:")
print(text)
