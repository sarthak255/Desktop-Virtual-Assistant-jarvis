# src/file_management.py
import os
import shutil
from tkinter import filedialog, Tk

# Initialize Tkinter root
root = Tk()
root.withdraw()  # Hide the root window

# Function to search for a file
def search_file(filename, directory):
    for root_dir, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root_dir, filename)
    return None

# Function to change file properties
def change_file_properties(filepath, new_name=None, new_icon=None):
    if new_name:
        base, ext = os.path.splitext(filepath)
        new_path = base + new_name + ext
        os.rename(filepath, new_path)
    # Changing icon would require OS-specific code

# Function to copy a file
def copy_file(src, dest):
    shutil.copy(src, dest)

# Test the functions
if __name__ == "__main__":
    search_directory = filedialog.askdirectory(title="Select Directory")
    file_to_search = "example.txt"
    result = search_file(file_to_search, search_directory)
    if result:
        print(f"File found: {result}")
        change_file_properties(result, new_name="_backup")
        dest_directory = filedialog.askdirectory(title="Select Destination Directory")
        copy_file(result, dest_directory)
    else:
        print("File not found")
