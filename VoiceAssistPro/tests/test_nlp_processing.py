
import unittest
import sys
sys.path.append('src')
from nlp_processing import (
    preprocess_text,
    recognize_intent,
    extract_entities,
    analyze_sentiment,
    generate_response,
    process_text
)

class TestNLPProcessing(unittest.TestCase):

    def test_preprocess_text(self):
        text = "Hello, how are you?"
        tokens = preprocess_text(text)
        self.assertIsInstance(tokens, list)
        self.assertTrue(len(tokens) > 0)

    def test_recognize_intent(self):
        text = "What's the weather like today?"
        intent = recognize_intent(text)
        self.assertEqual(intent, 'get_weather')

    def test_extract_entities(self):
        text = "Schedule a meeting with John on Friday."
        entities = extract_entities(text)
        self.assertIn(('John', 'PERSON'), entities)
        self.assertIn(('Friday', 'DATE'), entities)

    def test_analyze_sentiment(self):
        text = "I love this new app!"
        sentiment = analyze_sentiment(text)
        self.assertGreater(sentiment['polarity'], 0)

    def test_generate_response(self):
        intent = 'get_time'
        response = generate_response(intent)
        self.assertIsInstance(response, str)

    def test_process_text(self):
        text = "Play some music"
        results = process_text(text)
        self.assertEqual(results['intent'], 'play_music')
        self.assertIsInstance(results['response'], str)

if __name__ == '__main__':
        unittest.main()
