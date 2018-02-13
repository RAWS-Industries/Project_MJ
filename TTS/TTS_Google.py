import subprocess
from gtts import gTTS
import os

def speak(text, lang):
    tts = gTTS(text, lang)
    tts.save("hello4.mp3")

    subprocess.call(["afplay", "hello4.mp3"])

    os.remove ("hello4.mp3")