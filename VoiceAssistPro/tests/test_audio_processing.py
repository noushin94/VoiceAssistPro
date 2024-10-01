import unittest
import numpy as np
import sys
sys.path.append('src')
from audio_processing import (
    normalize_audio,
    remove_silence,
    pre_emphasis_filter,
    reduce_noise,
)
from config import SAMPLE_RATE

class TestAudioProcessing(unittest.TestCase):

    def setUp(self):
        # Create a sample audio signal: a sine wave with added noise
        t = np.linspace(0, 1, SAMPLE_RATE)
        self.audio = 0.5 * np.sin(2 * np.pi * 440 * t)  # 440 Hz tone
        # Add silence at the beginning and end
        self.silent_audio = np.concatenate((
            np.zeros(int(0.1 * SAMPLE_RATE)),  # 0.1 sec silence
            self.audio,
            np.zeros(int(0.1 * SAMPLE_RATE))   # 0.1 sec silence
        ))
        # Create noisy audio
        np.random.seed(0)  # For reproducibility
        noise = 0.05 * np.random.randn(len(self.audio))
        self.noisy_audio = self.audio + noise

    def test_normalize_audio(self):
        normalized_audio = normalize_audio(self.audio)
        max_amplitude = np.max(np.abs(normalized_audio))
        self.assertAlmostEqual(max_amplitude, 1.0, places=5)

    def test_remove_silence(self):
        trimmed_audio = remove_silence(self.silent_audio)
        # Check that the length is shorter after removing silence
        self.assertTrue(len(trimmed_audio) < len(self.silent_audio))
        # Check that the trimmed audio matches the original audio
        np.testing.assert_array_almost_equal(trimmed_audio, self.audio, decimal=5)

    def test_pre_emphasis_filter(self):
        emphasized_audio = pre_emphasis_filter(self.audio)
        # Check that the output length is the same
        self.assertEqual(len(emphasized_audio), len(self.audio))
        # Check that the first sample remains the same
        self.assertEqual(emphasized_audio[0], self.audio[0])

    def test_reduce_noise(self):
        reduced_noise_audio = reduce_noise(self.noisy_audio, SAMPLE_RATE)
        # Ensure the output has the same length
        self.assertEqual(len(reduced_noise_audio), len(self.noisy_audio))
        # Check that noise is reduced by comparing standard deviations
        original_noise_std = np.std(self.noisy_audio - self.audio)
        reduced_noise_std = np.std(reduced_noise_audio - self.audio)
        self.assertTrue(reduced_noise_std < original_noise_std)

if __name__ == '__main__':
    unittest.main()
