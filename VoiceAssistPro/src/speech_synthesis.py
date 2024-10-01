
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

def synthesize_speech(text):
    engine.say(text)
    engine.runAndWait()
