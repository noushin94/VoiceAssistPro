# tests/test_speech_synthesis.py

import unittest
import sys
sys.path.append('src')
from speech_synthesis import synthesize_speech
import os

class TestSpeechSynthesis(unittest.TestCase):

    def test_synthesize_speech_with_valid_input(self):
        """
        Test that synthesize_speech runs without errors when given valid text.
        """
        try:
            synthesize_speech("Testing speech synthesis.")
            result = True
        except Exception as e:
            print(f"Error occurred: {e}")
            result = False
        self.assertTrue(result)

    def test_synthesize_speech_with_empty_input(self):
        """
        Test that synthesize_speech handles empty strings gracefully.
        """
        try:
            synthesize_speech("")
            result = True
        except Exception as e:
            print(f"Error occurred: {e}")
            result = False
        self.assertTrue(result)

    def test_synthesize_speech_with_special_characters(self):
        """
        Test that synthesize_speech can handle text with special characters.
        """
        try:
            synthesize_speech("Hello, world! @#%^&*()")
            result = True
        except Exception as e:
            print(f"Error occurred: {e}")
            result = False
        self.assertTrue(result)

    def test_synthesize_speech_output(self):
        """
        Test that synthesize_speech actually produces an audible output.
        Note: This test is limited since we can't capture audio output in a unit test.
        """
        # Since we cannot capture the audio output in a test, we check if the function runs
        # without raising an exception, which suggests that the speech synthesis engine is working.
        try:
            synthesize_speech("This is a test to check audio output.")
            result = True
        except Exception as e:
            print(f"Error occurred: {e}")
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
