from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import queue

model = WhisperModel("base", compute_type="int8")  # fast

samplerate = 16000
block_duration = 0.5  # small chunks = low latency
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

def listen_stream():
    print("🎤 Listening (Streaming)...")

    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
        audio_buffer = []

        while True:
            data = q.get()
            audio_buffer.append(data)

            if len(audio_buffer) * block_duration >= 1.5:
                audio_np = np.concatenate(audio_buffer, axis=0).flatten()

                segments, _ = model.transcribe(audio_np, language="ta")

                text = "".join([seg.text for seg in segments]).strip()

                if text:
                    print("🗣 PARTIAL:", text)

                # reset buffer
                audio_buffer = []

                if len(text.split()) > 2:
                    return text
