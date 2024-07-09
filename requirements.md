# JARVIS Desktop Virtual Assistant - Requirements

## Overview
This document outlines the software, hardware, and package requirements for the JARVIS Desktop Virtual Assistant. JARVIS is a full-fledged desktop virtual assistant designed to operate on Windows, Linux, and MacOS.

## Software Requirements
### Operating Systems
- **Windows**: Windows 10 or later
- **Linux**: Ubuntu 18.04 or later, other major distributions
- **MacOS**: macOS Mojave (10.14) or later

### Programming Languages and Tools
- **Python**: Version 3.8 or later
- **Blender**: For 3D model creation

### Required Libraries and Packages
- **Speech Recognition**: `SpeechRecognition`
- **Text-to-Speech**: `pyttsx3`
- **OpenAI API**: `openai`
- **Keyboard Control**: `keyboard`
- **Audio Control**: `pycaw`
- **File Management**: `os`, `shutil`
- **GUI Development**: `tkinter`
- **Geolocation and Mapping**: `geopy`, `folium`, `googlemaps`
- **System Monitoring**: `psutil`
- **HTTP Requests**: `requests`
- **Window Management**: `pygetwindow`
- **Computer Vision**: `opencv-python`
- **Facial Recognition**: `face_recognition`
- **Hand and Face Analysis**: `mediapipe`, `dlib`
- **Document Creation**: `python-docx`
- **Web Automation**: `selenium`
- **NLP for User Expression Analysis**: `transformers`, `torch`
- **Developer Board Programming**: `pyserial`, `arduino-python`
- **Telephony and SMS**: `twilio`
- **Integrated Chatbot**: `chatterbot`
- **API Key Management**: `beautifulsoup4`, `mechanize`
- **Task Scheduling**: `schedule`

## Hardware Requirements
### Minimum Requirements
- **CPU**: Dual-core processor
- **RAM**: 4GB
- **Storage**: 500MB available space
- **Camera**: Integrated or external webcam for facial recognition and security features

### Recommended Requirements
- **CPU**: Quad-core processor
- **RAM**: 8GB or more
- **Storage**: 1GB available space
- **Camera**: High-definition webcam

## Installation Instructions
1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-repo/JARVIS_Assistant.git
    cd JARVIS_Assistant
    ```

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Main Script**
    ```bash
    python src/main.py
    ```

## Usage
Activate the assistant and use voice commands to interact with various features.

## Additional Features
1. **NLP for User Expression Analysis**: JARVIS has a high level of NLP to understand user expressions and react accordingly.
2. **Developer Board Programming**: JARVIS can help program different developer boards (Arduino, USB, etc.) and languages (C, C++, Java, HTML, Python, React, Node.js, Kotlin, etc.).
3. **Telephony and SMS**: JARVIS can make phone calls, receive/reject calls, make conference calls, send/read SMS, and handle video calls.
4. **Integrated Chatbot**: JARVIS includes an integrated chatbot for communication.
5. **API Key Management**: JARVIS can generate API keys for multiple platforms and search the internet for API keys if needed.
6. **Automatic Greeting**: JARVIS greets the user based on the time of day.
7. **Task Scheduling**: JARVIS can create and edit schedules for performing tasks.

## Environment Variables
- **OpenAI API Key**: Set your OpenAI API key as an environment variable.
    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    ```
- **Google Maps API Key**: Set your Google Maps API key as an environment variable.
    ```bash
    export GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ```

## Troubleshooting
- **Issue**: Installation fails due to missing packages.
  **Solution**: Ensure you are using Python 3.8 or later and have `pip` installed. Run `pip install --upgrade pip` and try again.
- **Issue**: Webcam not detected.
  **Solution**: Ensure your webcam drivers are up-to-date and the device is properly connected.
- **Issue**: Features not working as expected.
  **Solution**: Check for any errors in the console and refer to the specific module documentation for troubleshooting steps.

## Contact
For further assistance, please contact the project maintainers at `sarthakgoel62@gmail.com` or `yushgoel2004@gmail.com` .
