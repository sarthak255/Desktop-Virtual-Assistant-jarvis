import asyncio
import speech_recognition as sr
import pyttsx3
import spacy
import webbrowser
import tkinter as tk
import threading
import smtplib
from email.mime.text import MIMEText
import pickle
import requests
import datetime
import pyautogui
import vlc
from pytube import YouTube
import os
import subprocess
import pywhatkit as kit
import shutil
import sounddevice as sd
import wavio
import pygetwindow as gw
import pandas as pd
from docx import Document
from googlesearch import search as google_search
from googletrans import Translator
from gtts import gTTS
from telethon import TelegramClient
import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import face_recognition
import cv2
import numpy as np
import torch
import openai

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

# Initialize speech recognition and synthesis
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")
translator = Translator()


# Load preferences for personalization
def load_preferences():
    try:
        with open("preferences.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


preferences = load_preferences()


def save_preferences(preferences):
    with open("preferences.pkl", "wb") as f:
        pickle.dump(preferences, f)


# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            speak("Sorry, my speech service is down.")
            return None


# Function to synthesize speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to process commands using ChatGPT
def process_command(command):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"User command: {command}\nAssistant response:",
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Function to create programs for developer boards
def create_program(board, task):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create a program for {board} to {task}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Task automation functions
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def check_weather(location):
    api_key = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        weather_desc = response["weather"][0]["description"]
        speak(f"The current temperature in {location} is {temp} degrees Celsius with {weather_desc}.")
    else:
        speak("Sorry, I couldn't fetch the weather details.")


def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}.")


def send_email(recipient, subject, body):
    sender = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())


def control_media(action):
    player = vlc.MediaPlayer("path_to_media_file")
    if action == "play":
        player.play()
    elif action == "pause":
        player.pause()
    elif action == "stop":
        player.stop()
    elif action == "increase volume":
        current_volume = player.audio_get_volume()
        player.audio_set_volume(current_volume + 10)
    elif action == "decrease volume":
        current_volume = player.audio_get_volume()
        player.audio_set_volume(current_volume - 10)
    elif action == "mute":
        player.audio_toggle_mute()
    elif action == "unmute":
        player.audio_toggle_mute()
    elif action == "fast forward":
        player.set_time(player.get_time() + 10000)
    elif action == "rewind":
        player.set_time(player.get_time() - 10000)


def control_brightness(action):
    if action == "increase brightness":
        pyautogui.press("brightnessup")
    elif action == "decrease brightness":
        pyautogui.press("brightnessdown")


def check_social_media(platform):
    if platform == "twitter":
        webbrowser.open("https://twitter.com")
    elif platform == "facebook":
        webbrowser.open("https://facebook.com")
    elif platform == "instagram":
        webbrowser.open("https://instagram.com")


def open_software(name):
    if name.lower() == "notepad":
        os.system("notepad.exe")
    elif name.lower() == "calculator":
        os.system("calc.exe")
    elif name.lower() == "browser":
        webbrowser.open("http://www.google.com")


def close_software(name):
    if name.lower() == "notepad":
        os.system("taskkill /im notepad.exe /f")
    elif name.lower() == "calculator":
        os.system("taskkill /im calc.exe /f")


def take_screenshot(name, location):
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(location, f"{name}.png"))
    speak("Screenshot taken and saved.")


def record_audio(filename, duration):
    fs = 44100  # Sample rate
    seconds = duration  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, myrecording, fs, sampwidth=2)
    speak("Audio recording saved.")


def record_video(filename, duration):
    command = f"ffmpeg -t {duration} -f gdigrab -framerate 30 -i desktop {filename}"
    subprocess.call(command, shell=True)
    speak("Video recording saved.")


def search_file(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            file_path = os.path.join(root, filename)
            speak(f"File found at {file_path}")
            return file_path
    speak("File not found.")
    return None


def create_document(doc_type, content):
    if doc_type == "word":
        doc = Document()
        doc.add_paragraph(content)
        doc.save("document.docx")
        speak("Word document created.")
    elif doc_type == "text":
        with open("document.txt", "w") as f:
            f.write(content)
        speak("Text document created.")
    elif doc_type == "excel":
        df = pd.DataFrame({"Content": [content]})
        df.to_excel("document.xlsx", index=False)
        speak("Excel sheet created.")
    elif doc_type == "presentation":
        speak("Creating presentations is not supported yet.")


def improve_programming_language(language, content):
    if language == "python":
        # Example: Using PEP8 guidelines to format code
        formatted_content = content.replace("    ", "\t")  # Simplified example
        with open("improved_code.py", "w") as f:
            f.write(formatted_content)
        speak("Python code improved.")


def image_search(query):
    urls = list(google_search(query, num_results=5))
    for url in urls:
        webbrowser.open(url)
    speak("Here are the top image search results.")


def voice_typing():
    while True:
        command = recognize_speech()
        if command:
            pyautogui.write(command)


def switch_tabs():
    pyautogui.hotkey('ctrl', 'tab')


def minimize_all_tabs():
    pyautogui.hotkey('win', 'm')


def maximize_all_tabs():
    pyautogui.hotkey('win', 'shift', 'm')


def generate_image_from_text(text):
    url = "https://api.dallemini.ai/generate"  # Hypothetical DALL-E mini API endpoint
    response = requests.post(url, json={"text": text})
    image_url = response.json().get("image_url")
    webbrowser.open(image_url)
    speak("Image generated from text.")


def scan_for_viruses():
    if os.name == "nt":  # Windows
        os.system("start ms-settings:windowsdefender")
    elif os.name == "posix":  # Linux
        os.system("clamscan -r /")
    speak("Scanning for viruses.")


def translate_text(text, dest_lang):
    translation = translator.translate(text, dest=dest_lang)
    speak(f"Translation: {translation.text}")
    return translation.text


def translate_speech(dest_lang):
    text = recognize_speech()
    if text:
        translation = translator.translate(text, dest=dest_lang)
        tts = gTTS(translation.text, lang=dest_lang)
        tts.save("translated_speech.mp3")
        os.system("mpg321 translated_speech.mp3")
        speak(f"Translation: {translation.text}")


def read_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    speak(content)


def edit_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)
    speak("File edited.")


def greet_user():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        greet = "Good morning!"
    elif 12 <= hour < 18:
        greet = "Good afternoon!"
    else:
        greet = "Good evening!"
    speak(greet)


# Telegram functions
api_id = 'your_telegram_api_id'
api_hash = 'your_telegram_api_hash'
phone = 'your_phone_number'

telegram_client = TelegramClient('session_name', api_id, api_hash)


async def telegram_send_message(recipient, message):
    await telegram_client.start(phone)
    await telegram_client.send_message(recipient, message)
    await telegram_client.disconnect()


def send_telegram_message(recipient, message):
    with telegram_client:
        telegram_client.loop.run_until_complete(telegram_send_message(recipient, message))


# Discord functions
class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def send_message(self, channel_name, message):
        for guild in self.guilds:
            for channel in guild.text_channels:
                if channel.name == channel_name:
                    await channel.send(message)
                    return


discord_client = DiscordClient()


def send_discord_message(token, channel_name, message):
    discord_client.run(token)
    asyncio.run(discord_client.send_message(channel_name, message))


# YouTube functions
def download_youtube_video(url):
    yt = YouTube(url)
    yt.streams.first().download()
    speak("YouTube video downloaded.")


# Facebook and Instagram functions
driver = webdriver.Chrome()


def login_facebook(username, password):
    driver.get("https://www.facebook.com")
    user_input = driver.find_element_by_id("email")
    user_input.send_keys(username)
    pass_input = driver.find_element_by_id("pass")
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)
    speak("Logged into Facebook.")


def login_instagram(username, password):
    driver.get("https://www.instagram.com")
    user_input = driver.find_element_by_name("username")
    user_input.send_keys(username)
    pass_input = driver.find_element_by_name("password")
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)
    speak("Logged into Instagram.")


# Virtual machine management
def start_virtual_machine(vm_name):
    os.system(f"virsh start {vm_name}")
    speak(f"Started virtual machine {vm_name}")


def stop_virtual_machine(vm_name):
    os.system(f"virsh shutdown {vm_name}")
    speak(f"Stopped virtual machine {vm_name}")


# Fixing system errors
def fix_system_errors():
    if os.name == "nt":  # Windows
        os.system("sfc /scannow")
    elif os.name == "posix":  # Linux/Mac
        os.system("sudo apt-get update && sudo apt-get upgrade")
    speak("System errors fixed.")


# Function to create scripts for developer boards
def create_script(board, task):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create a script for {board} to {task}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Function to handle voice lock system
def lock_system():
    speak("Please say 'wakeup' to unlock the system.")
    voice_activation()
    while True:
        speak("Please say the password.")
        password = recognize_speech()
        if password and "open sesame" in password.lower():
            speak("System unlocked.")
            break
        else:
            speak("Incorrect password. Try again.")


# Function for voice activation
def voice_activation():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Say 'wakeup' to activate the assistant...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                if "wakeup" in text.lower():
                    greet_user()
                    speak("I am awake. How can I help you?")
                    break
            except sr.UnknownValueError:
                continue


# Function to listen for "Jarvis" to enter listening mode
def listen_for_jarvis():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                if "jarvis" in text.lower():
                    speak("Listening...")
                    command = recognize_speech()
                    if command:
                        execute_command(command)
            except sr.UnknownValueError:
                continue


# Command execution function
def execute_command(command):
    response = process_command(command)
    if "remember" in command:
        key, value = command.replace("remember", "").strip().split(" as ")
        preferences[key] = value
        save_preferences(preferences)
        speak(f"Remembered {key} as {value}.")
    elif "what is" in command:
        key = command.replace("what is", "").strip()
        if key in preferences:
            speak(f"{key} is {preferences[key]}.")
        else:
            speak(f"I don't know what {key} is.")
    elif "send email" in command:
        recipient = "recipient@example.com"
        subject = "Test Email"
        body = "This is a test email from JARVIS."
        send_email(recipient, subject, body)
        speak("Email has been sent.")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        search_web(query)
    elif "check weather" in command:
        location = command.replace("check weather in", "").strip()
        check_weather(location)
    elif "time" in command:
        get_time()
    elif "open" in command and "browser" in command:
        webbrowser.open("http://www.google.com")
    elif "play" in command or "pause" in command or "stop" in command or "increase volume" in command or "decrease volume" in command or "mute" in command or "unmute" in command or "fast forward" in command or "rewind" in command:
        control_media(command)
    elif "increase brightness" in command or "decrease brightness" in command:
        control_brightness(command)
    elif "check" in command and ("twitter" in command or "facebook" in command or "instagram" in command):
        platform = command.split()[-1]
        check_social_media(platform)
    elif "open" in command:
        software = command.replace("open", "").strip()
        open_software(software)
    elif "close" in command:
        software = command.replace("close", "").strip()
        close_software(software)
    elif "take screenshot" in command:
        parts = command.replace("take screenshot", "").strip().split(" and save in ")
        name = parts[0].strip()
        location = parts[1].strip()
        take_screenshot(name, location)
    elif "record audio" in command:
        duration = int(command.split()[-1])
        record_audio("audio.wav", duration)
    elif "record video" in command:
        duration = int(command.split()[-1])
        record_video("video.mp4", duration)
    elif "search file" in command:
        filename = command.replace("search file", "").strip()
        search_file(filename)
    elif "create document" in command:
        parts = command.replace("create document", "").strip().split(" with content ")
        doc_type = parts[0].strip()
        content = parts[1].strip() if len(parts) > 1 else ""
        create_document(doc_type, content)
    elif "improve programming" in command:
        parts = command.replace("improve programming", "").strip().split(" with content ")
        language = parts[0].strip()
        content = parts[1].strip() if len(parts) > 1 else ""
        improve_programming_language(language, content)
    elif "image search" in command:
        query = command.replace("image search", "").strip()
        image_search(query)
    elif "voice type" in command:
        voice_typing()
    elif "switch tab" in command:
        switch_tabs()
    elif "minimize all" in command:
        minimize_all_tabs()
    elif "maximize all" in command:
        maximize_all_tabs()
    elif "generate image" in command:
        text = command.replace("generate image", "").strip()
        generate_image_from_text(text)
    elif "scan for viruses" in command:
        scan_for_viruses()
    elif "translate text" in command:
        parts = command.replace("translate text", "").strip().split(" to ")
        text = parts[0].strip()
        dest_lang = parts[1].strip()
        translate_text(text, dest_lang)
    elif "translate speech" in command:
        dest_lang = command.replace("translate speech to", "").strip()
        translate_speech(dest_lang)
    elif "send telegram" in command:
        parts = command.replace("send telegram", "").strip().split(" to ")
        recipient = parts[1].strip()
        message = parts[0].strip()
        send_telegram_message(recipient, message)
    elif "send discord" in command:
        parts = command.replace("send discord", "").strip().split(" to ")
        channel_name = parts[1].strip()
        message = parts[0].strip()
        token = "your_discord_bot_token"
        send_discord_message(token, channel_name, message)
    elif "download youtube" in command:
        url = command.replace("download youtube", "").strip()
        download_youtube_video(url)
    elif "login facebook" in command:
        parts = command.replace("login facebook", "").strip().split(" with ")
        username = parts[0].strip()
        password = parts[1].strip()
        login_facebook(username, password)
    elif "login instagram" in command:
        parts = command.replace("login instagram", "").strip().split(" with ")
        username = parts[0].strip()
        password = parts[1].strip()
        login_instagram(username, password)
    elif "start virtual machine" in command:
        vm_name = command.replace("start virtual machine", "").strip()
        start_virtual_machine(vm_name)
    elif "stop virtual machine" in command:
        vm_name = command.replace("stop virtual machine", "").strip()
        stop_virtual_machine(vm_name)
    elif "fix system errors" in command:
        fix_system_errors()
    elif "read file" in command:
        filepath = command.replace("read file", "").strip()
        read_file(filepath)
    elif "edit file" in command:
        parts = command.replace("edit file", "").strip().split(" with content ")
        filepath = parts[0].strip()
        content = parts[1].strip()
        edit_file(filepath, content)
    elif "greet me" in command:
        greet_user()
    elif "create program for" in command:
        parts = command.replace("create program for", "").strip().split(" to ")
        board = parts[0].strip()
        task = parts[1].strip()
        program = create_program(board, task)
        speak(f"Here's a program for {board} to {task}: {program}")
    elif "create script for" in command:
        parts = command.replace("create script for", "").strip().split(" to ")
        board = parts[0].strip()
        task = parts[1].strip()
        script = create_script(board, task)
        speak(f"Here's a script for {board} to {task}: {script}")
    else:
        speak(response)


# GUI setup
def create_gui():
    root = tk.Tk()
    root.title("JARVIS Assistant")

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text="JARVIS")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack()

    def on_enter(event):
        command = entry.get()
        entry.delete(0, tk.END)
        execute_command(command)

    entry.bind("<Return>", on_enter)

    def listen():
        lock_system()
        while True:
            listen_for_jarvis()

    # Start voice recognition in a separate thread
    threading.Thread(target=listen, daemon=True).start()

    root.mainloop()


if __name__ == "__main__":
    create_gui()
