import schedule
import time
import pyttsx3
import datetime

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to perform a scheduled task
def perform_task(task):
    print(f"Performing task: {task}")
    speak(f"It's time to {task}")

# Function to add a new task to the schedule
def add_advanced_task(task, start_time, end_time):
    schedule.every().day.at(start_time).do(perform_task, task)
    schedule.every().day.at(end_time).do(speak, f"{task} should be completed by now.")

# Function to clear all scheduled tasks
def clear_schedule():
    schedule.clear()
    speak("Cleared all scheduled tasks")

# Test the advanced scheduling functions
if __name__ == "__main__":
    add_advanced_task("check emails", "09:00", "10:00")
    add_advanced_task("have a meeting", "14:00", "15:00")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
