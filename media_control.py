# src/media_control.py
# pip install keyboard pycaw

import keyboard
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import os

# Function to change volume
def change_volume(action):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()

    if action == "up":
        volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 0.1), None)
    elif action == "down":
        volume.SetMasterVolumeLevelScalar(max(0.0, current_volume - 0.1), None)
    elif action == "mute":
        volume.SetMute(1, None)
    elif action == "unmute":
        volume.SetMute(0, None)

# Function to control media playback
def control_media(action):
    if action == "play_pause":
        keyboard.send("play/pause media")
    elif action == "stop":
        keyboard.send("stop media")
    elif action == "next":
        keyboard.send("next track")
    elif action == "previous":
        keyboard.send("previous track")

# Test the functions
if __name__ == "__main__":
    change_volume("up")
    control_media("play_pause")
