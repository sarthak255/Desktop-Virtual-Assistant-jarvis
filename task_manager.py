# src/task_manager.py
# pip install psutil

import psutil
from tkinter import Tk, Listbox, Scrollbar, Button, END

# Function to get a list of processes
def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append(proc.info)
    return processes

# Function to kill a process
def kill_process(pid):
    p = psutil.Process(pid)
    p.terminate()

# GUI for task manager
def task_manager_gui():
    root = Tk()
    root.title("Task Manager")

    scrollbar = Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(root, yscrollcommand=scrollbar.set)
    processes = get_processes()
    for process in processes:
        listbox.insert(END, f"{process['pid']} - {process['name']} - {process['username']}")
    listbox.pack(side="left", fill="both")

    def on_kill():
        selected = listbox.curselection()
        if selected:
            process_info = listbox.get(selected[0])
            pid = int(process_info.split(' - ')[0])
            kill_process(pid)
            listbox.delete(selected[0])

    kill_button = Button(root, text="Kill Process", command=on_kill)
    kill_button.pack()

    scrollbar.config(command=listbox.yview)
    root.mainloop()

# Test the task manager GUI
if __name__ == "__main__":
    task_manager_gui()
