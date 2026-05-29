import time
import torch
from faster_whisper import WhisperModel

print("Loading faster-whisper...")
start_load = time.time()

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if device == "cuda" else "int8"

model = WhisperModel("small", device=device, compute_type=compute_type)
print(f"Model loaded in {time.time() - start_load:.2f} seconds on {device.upper()}.")

audio_file = "test_tamil.wav" 

print(f"Transcribing {audio_file}...")
start_transcribe = time.time()

# Force Tamil language detection
segments, info = model.transcribe(audio_file, beam_size=5, language="ta")

print("\nTranscription results:")
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

transcription_time = time.time() - start_transcribe
print(f"\nTranscription completed in {transcription_time:.2f} seconds.")
