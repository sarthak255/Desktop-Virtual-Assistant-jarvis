import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Function to read text from the screen
def read_screen_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Test the screen reader function
if __name__ == "__main__":
    text = "This is a test text for the screen reader."
    read_screen_text(text)
