# src/tabs_management.py
# pip install pygetwindow keyboard

import pygetwindow as gw
import keyboard

# Function to list all open windows
def list_open_windows():
    windows = gw.getAllWindows()
    return [window.title for window in windows]

# Function to switch to a specific window
def switch_window(window_title):
    window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()

# Function to minimize/maximize all windows
def minimize_all_windows():
    windows = gw.getAllWindows()
    for window in windows:
        window.minimize()

def maximize_all_windows():
    windows = gw.getAllWindows()
    for window in windows:
        window.maximize()

# Test the functions
if __name__ == "__main__":
    open_windows = list_open_windows()
    print("Open Windows:", open_windows)
    if open_windows:
        switch_window(open_windows[0])
        minimize_all_windows()
        maximize_all_windows()
