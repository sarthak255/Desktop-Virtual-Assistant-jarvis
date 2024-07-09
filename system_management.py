# src/system_management.py
import os
from tkinter import Tk, Button

# Function to adjust brightness (Linux example using xrandr)
def adjust_brightness(level):
    os.system(f"xrandr --output eDP-1 --brightness {level}")

# Function to adjust volume (Linux example using amixer)
def adjust_volume(level):
    os.system(f"amixer sset Master {level}%")

# Function to change system time (Linux example)
def change_system_time(new_time):
    os.system(f"sudo date --set '{new_time}'")

# GUI for system management
def system_management_gui():
    root = Tk()
    root.title("System Management")

    def on_brightness_up():
        adjust_brightness(1.0)  # Set to maximum brightness

    def on_brightness_down():
        adjust_brightness(0.5)  # Set to half brightness

    def on_volume_up():
        adjust_volume(100)  # Set to maximum volume

    def on_volume_down():
        adjust_volume(50)  # Set to half volume

    def on_change_time():
        new_time = "2024-07-09 12:34:56"
        change_system_time(new_time)

    brightness_up_button = Button(root, text="Brightness Up", command=on_brightness_up)
    brightness_up_button.pack()

    brightness_down_button = Button(root, text="Brightness Down", command=on_brightness_down)
    brightness_down_button.pack()

    volume_up_button = Button(root, text="Volume Up", command=on_volume_up)
    volume_up_button.pack()

    volume_down_button = Button(root, text="Volume Down", command=on_volume_down)
    volume_down_button.pack()

    change_time_button = Button(root, text="Change Time", command=on_change_time)
    change_time_button.pack()

    root.mainloop()

# Test the system management GUI
if __name__ == "__main__":
    system_management_gui()
