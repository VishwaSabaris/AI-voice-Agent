from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

model = WhisperModel("base", compute_type="int8")  # fast + CPU friendly

def listen():
    print("\n🎤 Listening (Tamil)...")

    duration = 3  # seconds
    samplerate = 16000

    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()

    audio = audio.flatten()

    segments, _ = model.transcribe(audio, language="ta")

    text = ""
    for seg in segments:
        text += seg.text

    return text.strip()
