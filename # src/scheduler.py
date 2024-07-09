# src/scheduler.py
# pip install schedule

import schedule
import time
import pyttsx3

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
def add_task(task, time):
    schedule.every().day.at(time).do(perform_task, task)
    speak(f"Scheduled task '{task}' at {time}")

# Function to clear all scheduled tasks
def clear_schedule():
    schedule.clear()
    speak("Cleared all scheduled tasks")

# Function to edit an existing task (remove old task and add a new one)
def edit_task(old_task, new_task, time):
    clear_schedule()
    add_task(new_task, time)

# Test the scheduling functions
if __name__ == "__main__":
    add_task("check emails", "09:00")
    add_task("have a meeting", "14:00")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
