
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from textblob import TextBlob

# Download required NLTK data files (only needs to be run once)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load SpaCy English model
nlp = spacy.load('en_core_web_sm')

# Load stop words
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stop words, and lemmatizing.

    Args:
        text (str): The input text.

    Returns:
        list: A list of preprocessed tokens.
    """
    # Tokenization
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    # Lemmatization using SpaCy
    doc = nlp(' '.join(filtered_tokens))
    lemmas = [token.lemma_ for token in doc]
    return lemmas

def recognize_intent(text):
    """
    Recognize the intent of the text.

    Args:
        text (str): The input text.

    Returns:
        str: The recognized intent.
    """
    lemmas = preprocess_text(text)
    if any(word in lemmas for word in ['weather', 'temperature', 'forecast']):
        return 'get_weather'
    elif any(word in lemmas for word in ['time', 'clock']):
        return 'get_time'
    elif any(word in lemmas for word in ['news', 'headline', 'update']):
        return 'get_news'
    elif any(word in lemmas for word in ['play', 'music', 'song']):
        return 'play_music'
    else:
        return 'unknown_intent'

def extract_entities(text):
    """
    Extract named entities from the text.

    Args:
        text (str): The input text.

    Returns:
        list: A list of extracted entities.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def analyze_sentiment(text):
    """
    Analyze the sentiment of the text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with polarity and subjectivity scores.
    """
    blob = TextBlob(text)
    sentiment = {
        'polarity': blob.sentiment.polarity,       # -1 (negative) to 1 (positive)
        'subjectivity': blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
    }
    return sentiment

def generate_response(intent, entities=None):
    """
    Generate an appropriate response based on the recognized intent.

    Args:
        intent (str): The recognized intent.
        entities (list): A list of extracted entities.

    Returns:
        str: The generated response.
    """
    if intent == 'get_weather':
        return "Sure, I'll fetch the weather information for you."
    elif intent == 'get_time':
        return "The current time is displayed on your device."
    elif intent == 'get_news':
        return "Here are the latest news headlines."
    elif intent == 'play_music':
        return "Playing your favorite songs."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

def process_text(text):
    """
    Process the input text by recognizing intent, extracting entities,
    analyzing sentiment, and generating a response.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary containing the processing results.
    """
    intent = recognize_intent(text)
    entities = extract_entities(text)
    sentiment = analyze_sentiment(text)
    response = generate_response(intent, entities)

    return {
        'intent': intent,
        'entities': entities,
        'sentiment': sentiment,
        'response': response
    }
