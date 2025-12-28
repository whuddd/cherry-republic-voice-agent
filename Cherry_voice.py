from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
import json
from difflib import get_close_matches

# Load environment variables
load_dotenv()

class CherryVoice:
    def __init__(self):
        # Initialize ElevenLabs client
        self.client = ElevenLabs(
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )
        # Default voice settings
        self.voice_id = "JBFqnCBsd6RMkjVDRZzb"  # We can change this after testing different voices
        self.model_id = "eleven_turbo_v2"
        # better model, more credits though
        # self.model_id = "eleven_multilingual_v2"
        
        # Load FAQ database
        self.load_faqs()
        
    def load_faqs(self):
        """Load FAQs from JSON file"""
        try:
            with open('data/faq.json', 'r') as file:
                self.faq_data = json.load(file)
            print("FAQ database loaded successfully!")
        except Exception as e:
            print(f"Error loading FAQ database: {str(e)}")
            self.faq_data = {"faqs": []}
    
    def find_best_match(self, question):
        """Find the best matching FAQ for the given question"""
        all_questions = []
        question_to_faq = {}
        
        # Create a mapping of questions to their FAQ entries
        for faq in self.faq_data["faqs"]:
            for q in faq["questions"]:
                all_questions.append(q.lower())
                question_to_faq[q.lower()] = faq
        
        # Find closest matching question
        matches = get_close_matches(question.lower(), all_questions, n=1, cutoff=0.6)
        
        if matches:
            return question_to_faq[matches[0]]
        return None

    def speak(self, text):
        """Generate and save audio for the given text"""
        try:
            # Convert generator to bytes
            audio_stream = self.client.text_to_speech.convert(
                text=text,
                voice_id=self.voice_id,
                model_id=self.model_id,
                output_format="mp3_44100_128",
            )
            
            # Create outputs directory if it doesn't exist
            os.makedirs('outputs', exist_ok=True)
            
            # Create a unique filename based on the text
            filename = f"outputs/response_{abs(hash(text))}.mp3"
            
            # Save the audio stream to a file
            audio_data = b''
            for chunk in audio_stream:
                audio_data += chunk
                
            with open(filename, 'wb') as f:
                f.write(audio_data)
            
            print(f"\nAudio saved to: {filename}")
            print("You can play this file using your media player")
            return True
        except Exception as e:
            print(f"Error generating speech: {str(e)}")
            return False
    
    def answer_question(self, question):
        """Find and speak the answer to a question"""
        faq = self.find_best_match(question)
        if faq:
            print(f"Found matching FAQ in category: {faq['category']}")
            self.speak(faq["answer"])
        else:
            fallback_response = "I apologize, but I'm not quite sure about that one. Feel free to ask about our store hours, products, shipping, or samples - I'd be happy to help with those!"
            self.speak(fallback_response)
#Real one that goes through different quesitons
# def test_faq_system():
#     """Test the FAQ system with some sample questions"""
#     cherry = CherryVoice()
    
#     print("\nTesting FAQ system...")
#     test_questions = [
#         "What time do you open?",
#         "What's your best product?",
#         "Do you ship to California?",
#         "Can I try some samples?"
#     ]
    
#     for question in test_questions:
#         print(f"\nTesting question: {question}")
#         cherry.answer_question(question)
#         input("Press Enter to continue to the next question...")

#Limited voice test because of API credit limits
def test_faq_system():
    cherry = CherryVoice()
    question = "What time do you open?"
    cherry.answer_question(question)

if __name__ == "__main__":
    test_faq_system()
