import subprocess
import tempfile
import os
from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

DURATION = 6


def listen():
    print("🎤 Speak now...")

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_path = temp_file.name
    temp_file.close()

    cmd = [
        "timeout",
        str(DURATION),
        "parec",
        "--channels=1",
        "--rate=44100",
        "--format=s16le",
        "--file-format=wav",
        temp_path
    ]

    subprocess.run(cmd)

    segments, _ = model.transcribe(
        temp_path,
        language="ta",
        beam_size=8,
        vad_filter=False
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    os.remove(temp_path)

    text = text.strip()
    print("\n📝 You said:", text)

    return text
