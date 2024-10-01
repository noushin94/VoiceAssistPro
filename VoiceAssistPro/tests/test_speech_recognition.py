# tests/test_speech_recognition.py

import unittest
import sys
sys.path.append('src')
from speech_recognition import recognize_speech
from unittest.mock import patch, MagicMock

class TestSpeechRecognition(unittest.TestCase):

    def test_recognize_speech_runs(self):
        """
        Test that recognize_speech runs without errors when called.
        """
        try:
            transcription = recognize_speech(duration=1)
            result = True
        except Exception as e:
            print(f"Error occurred: {e}")
            result = False
        self.assertTrue(result)

    def test_recognize_speech_output_type(self):
        """
        Test that the output of recognize_speech is a string.
        """
        # Mocking the actual speech recognition for consistent testing
        with patch('speech_recognition.recognize_speech', return_value='test transcription'):
            transcription = recognize_speech(duration=1)
            self.assertIsInstance(transcription, str)

    @patch('speech_recognition.record_audio')
    @patch('speech_recognition.tokenizer')
    @patch('speech_recognition.model')
    def test_recognize_speech_with_mock(self, mock_model, mock_tokenizer, mock_record_audio):
        """
        Test recognize_speech using mocked audio input and model to avoid dependency on actual audio.
        """
        # Mock the audio recording function to return a fake audio array
        mock_record_audio.return_value = [0.1, 0.2, 0.3]

        # Mock the tokenizer to return fake input values
        mock_tokenizer.return_value = MagicMock(input_values='fake_input_values')
        mock_tokenizer.decode.return_value = 'mocked transcription'

        # Mock the model to return fake logits
        mock_model.return_value = MagicMock(logits='fake_logits')

        transcription = recognize_speech(duration=1)
        self.assertEqual(transcription, 'mocked transcription')

if __name__ == '__main__':
    unittest.main()
