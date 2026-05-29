import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "/home/sabaris/storage/models/vosk-model-small-en-us-0.15"

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))

def listen():
    with sd.RawInputStream(
        samplerate=16000,
        blocksize=4000,  # 🔥 lower latency
        dtype='int16',
        channels=1,
        callback=callback
    ):
        while True:
            data = audio_queue.get()

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()

                if text:
                    return text
