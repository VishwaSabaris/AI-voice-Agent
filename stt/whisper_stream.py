from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import queue

model = WhisperModel(
    "small",              # better than tiny
    compute_type="int8",  # fast
)

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

def listen():

    print("🎤 Listening...")

    audio_buffer = []

    with sd.InputStream(samplerate=16000, channels=1, callback=callback):

        while True:
            data = q.get()
            audio_buffer.append(data)

            if len(audio_buffer) >= 10:
                audio_np = np.concatenate(audio_buffer, axis=0).flatten()

                segments, _ = model.transcribe(
                    audio_np,
                    language="ta",
                    beam_size=2,
                    vad_filter=True,  # 🔥 removes noise
                    initial_prompt="Coimbatore, Peelamedu, biryani, fried rice"
                )

                text = " ".join([seg.text for seg in segments]).strip()

                if text:
                    return text

                audio_buffer = []
