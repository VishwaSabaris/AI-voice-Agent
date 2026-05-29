import os
import time
import torch
from TTS.api import TTS

# Storage paths
os.environ["XDG_CACHE_HOME"] = "/home/sabaris/storage/.cache"
os.environ["TTS_HOME"] = "/home/sabaris/storage/tts_models"

print("Loading Tamil TTS model...")

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using:", device)

# Tamil model (STABLE)
tts = TTS("tts_models/tam/fairseq/vits").to(device)

text = "வணக்கம், எங்கள் உணவகத்திற்கு வரவேற்கிறோம். நீங்கள் என்ன ஆர்டர் செய்ய விரும்புகிறீர்கள்?"

print("Generating audio...")

tts.tts_to_file(
    text=text,
    file_path="test_tamil.wav"
)

print("Done! File saved as test_tamil.wav")
