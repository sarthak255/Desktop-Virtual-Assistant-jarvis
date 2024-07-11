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
- **GPU Utilization**: `tensorflow-gpu`
- **End-to-End Encryption**: `cryptography`
- **Project Management Integration**: `py-trello`
- **Data Anonymization**: `faker`
- **Semantic Search**: `sentence-transformers`

## Hardware Requirements
### Minimum Requirements
- **CPU**: Dual-core processor
- **RAM**: 4GB
- **Storage**: 500MB available space
- **Camera**: Integrated or external webcam for facial recognition and security features
- **GPU**: Integrated GPU

### Recommended Requirements
- **CPU**: Quad-core processor
- **RAM**: 8GB or more
- **Storage**: 1GB available space
- **Camera**: High-definition webcam
- **GPU**: Dedicated GPU with CUDA support (for tasks like 3D modeling, rendering, and image generation)

## Installation Instructions
1. **Clone the Repository**
    ```bash
    git clone https://github.com/sarthak255/Desktop-Virtual-Assistant-jarvis.git
    cd Desktop-Virtual-Assistant-jarvis
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
8. **Program Creation**: JARVIS can create starter code for various platforms (Android, Windows, Linux, Mac) and languages.
9. **GPU Utilization for Tasks**: JARVIS can use integrated and dedicated GPUs for performing tasks such as 3D modeling, rendering, and image generation.
10. **End-to-End Encryption**: Encrypt and decrypt data securely.
11. **Advanced Scheduling**: Schedule tasks with start and end times.
12. **Project Management Integration**: Integrate with Trello for project management.
13. **Content Aware Responses**: Generate content-aware responses using OpenAI API.
14. **Multi-Term Conversations**: Maintain multi-term conversations.
15. **Data Anonymization**: Anonymize personal data.
16. **Semantic Search**: Perform semantic search using sentence transformers.
17. **Real-time Data Fetching**: Fetch real-time data such as weather information.
18. **Visual Recognition**: Recognize faces in images.
19. **Augmented Reality**: Apply augmented reality effects.
20. **Screen Reader Integration**: Integrate a screen reader for accessibility.
21. **Secure Personal Storage**: 25GB password-protected storage for confidential data.

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
For further assistance, please contact the project maintainers at `sarthakgoel62@gmail.com` / `yushgoel2004@gmail.com`.
