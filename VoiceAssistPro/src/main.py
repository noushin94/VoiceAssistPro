
import sys
from speech_recognition import recognize_speech
from speech_synthesis import synthesize_speech
from nlp_processing import process_text
from config import DURATION

def main():
    print("Welcome to VoiceAssist Pro!")
    while True:
        print("\nOptions:")
        print("1. Speak to the assistant")
        print("2. Enter text")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            text = recognize_speech(duration=DURATION)
            print(f"You said: {text}")
            nlp_results = process_text(text)
            print(f"Intent: {nlp_results['intent']}")
            print(f"Entities: {nlp_results['entities']}")
            print(f"Sentiment: {nlp_results['sentiment']}")
            response = nlp_results['response']
            print(f"Assistant: {response}")
            synthesize_speech(response)
        elif choice == '2':
            text = input("Enter your text: ")
            nlp_results = process_text(text)
            print(f"Intent: {nlp_results['intent']}")
            print(f"Entities: {nlp_results['entities']}")
            print(f"Sentiment: {nlp_results['sentiment']}")
            response = nlp_results['response']
            print(f"Assistant: {response}")
            synthesize_speech(response)
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
