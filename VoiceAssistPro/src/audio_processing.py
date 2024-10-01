

import numpy as np
from scipy.signal import lfilter
import noisereduce as nr

def normalize_audio(audio):
    """
    Normalize the audio signal to have a maximum amplitude of 1.

    Args:
        audio (numpy.ndarray): The input audio signal.

    Returns:
        numpy.ndarray: The normalized audio signal.
    """
    max_amplitude = np.max(np.abs(audio))
    if max_amplitude == 0:
        return audio
    normalized_audio = audio / max_amplitude
    return normalized_audio

def remove_silence(audio, threshold=0.01):
    """
    Remove silence from the beginning and end of the audio signal.

    Args:
        audio (numpy.ndarray): The input audio signal.
        threshold (float): The amplitude threshold below which is considered silence.

    Returns:
        numpy.ndarray: The trimmed audio signal.
    """
    abs_audio = np.abs(audio)
    above_threshold = np.where(abs_audio > threshold)[0]
    if above_threshold.size:
        start = above_threshold[0]
        end = above_threshold[-1] + 1
        trimmed_audio = audio[start:end]
        return trimmed_audio
    else:
        return audio  # Return original if no speech is detected

def pre_emphasis_filter(audio, pre_emphasis=0.97):
    """
    Apply a pre-emphasis filter to the audio signal.

    Args:
        audio (numpy.ndarray): The input audio signal.
        pre_emphasis (float): The pre-emphasis coefficient.

    Returns:
        numpy.ndarray: The filtered audio signal.
    """
    emphasized_audio = np.append(audio[0], audio[1:] - pre_emphasis * audio[:-1])
    return emphasized_audio

def reduce_noise(audio, sample_rate):
    """
    Reduce background noise from the audio signal using spectral gating.

    Args:
        audio (numpy.ndarray): The input audio signal.
        sample_rate (int): The sample rate of the audio signal.

    Returns:
        numpy.ndarray: The denoised audio signal.
    """
    # Use a small sample of the audio as the noise profile
    noise_sample = audio[:int(0.5 * sample_rate)]  # First half-second as noise sample
    reduced_noise_audio = nr.reduce_noise(audio_clip=audio, noise_clip=noise_sample, verbose=False)
    return reduced_noise_audio
