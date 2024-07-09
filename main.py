import threading
import time
from assistant import main as assistant_main
from media_control import control_media, change_volume
from file_management import search_file, change_file_properties, copy_file
from gps_tracking import get_current_location, create_map, get_directions
from task_manager import task_manager_gui
from weather_forecast import weather_forecast_gui
from tabs_management import list_open_windows, switch_window, minimize_all_windows, maximize_all_windows
from system_management import system_management_gui
from social_media_control import social_media_login
from gmail_integration import send_email, read_emails
from calculator import calculator_gui
from study_helper import get_study_help
from web_search import web_search
from camera_security import detect_motion, recognize_face
from security_lock import facial_recognition_unlock, password_unlock
from admin_mode import activate_admin_mode
from expression_analysis import analyze_expressions
from problem_fixer import fix_common_issues
from document_creation import document_creation_gui

def run_assistant():
    assistant_main()

def run_task_manager():
    task_manager_gui()

def run_weather_forecast():
    weather_forecast_gui()

def run_system_management():
    system_management_gui()

def run_calculator():
    calculator_gui()

def run_document_creation():
    document_creation_gui()

def run_expression_analysis():
    analyze_expressions()

def run_problem_fixer():
    fix_common_issues()

# Start the assistant in a separate thread
assistant_thread = threading.Thread(target=run_assistant)
assistant_thread.start()

# Example usage of other modules (these can be invoked via voice commands or GUI as needed)
# This is just for demonstration; in practice, these would be integrated with the voice command system.

if __name__ == "__main__":
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "task manager":
            run_task_manager()
        elif command == "weather forecast":
            run_weather_forecast()
        elif command == "system management":
            run_system_management()
        elif command == "calculator":
            run_calculator()
        elif command == "document creation":
            run_document_creation()
        elif command == "expression analysis":
            run_expression_analysis()
        elif command == "problem fixer":
            run_problem_fixer()
        elif command == "exit":
            print("Shutting down the assistant...")
            break
        else:
            print("Unknown command. Please try again.")
        
        time.sleep(1)
