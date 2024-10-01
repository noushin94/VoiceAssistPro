import numpy as np
import sounddevice as sd
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from config import SAMPLE_RATE, ASR_MODEL_NAME
import warnings
from audio_processing import (
    normalize_audio,
    remove_silence,
    pre_emphasis_filter,
    reduce_noise,
)

warnings.filterwarnings("ignore")

# Load models once to avoid reloading every time
tokenizer = Wav2Vec2Tokenizer.from_pretrained(ASR_MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(ASR_MODEL_NAME)

def record_audio(duration=5, fs=SAMPLE_RATE):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    audio = np.squeeze(audio)
    return audio

def recognize_speech(duration=5):
    # Record audio
    audio = record_audio(duration=duration)

    # Apply audio processing
    audio = normalize_audio(audio)
    audio = remove_silence(audio)
    audio = pre_emphasis_filter(audio)
    audio = reduce_noise(audio, SAMPLE_RATE)

    # Tokenize input
    input_values = tokenizer(audio, return_tensors='pt', sampling_rate=SAMPLE_RATE).input_values

    # Perform inference
    logits = model(input_values).logits

    # Get predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode the IDs to text
    transcription = tokenizer.decode(predicted_ids[0])
    return transcription.lower()
