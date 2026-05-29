from gtts import gTTS
import os
import tempfile


def speak(text):
    try:
        print(f"🤖 AI: {text}")

        tts = gTTS(text=text, lang="ta")

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        audio_path = temp_file.name
        tts.save(audio_path)

        # convert mp3 to wav
        wav_path = audio_path.replace(".mp3", ".wav")
        os.system(f"ffmpeg -y -i {audio_path} {wav_path} >/dev/null 2>&1")

        # play using working PulseAudio player
        os.system(f"paplay {wav_path}")

        os.remove(audio_path)
        os.remove(wav_path)

    except Exception as e:
        print("TTS Error:", e)
