# src/assistant.py
import speech_recognition as sr
import pyttsx3
import openai
import os

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# OpenAI API key (replace with your actual key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection")
        return ""

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to get response from ChatGPT
def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main loop
def main():
    while True:
        query = recognize_speech()
        if query:
            response = chatgpt_response(query)
            print(f"ChatGPT: {response}")
            speak(response)

if __name__ == "__main__":
    main()
