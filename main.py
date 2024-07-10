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
from developer_board_programming import program_developer_board
from telephony_sms import send_sms, make_call, handle_incoming_call
from chatbot import get_chatbot_response
from api_key_management import generate_api_key, search_api_key
from scheduler import add_task, clear_schedule, edit_task
from program_creation import create_program

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

def main():
    assistant_thread = threading.Thread(target=run_assistant)
    assistant_thread.start()

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
        elif command == "program developer board":
            code = """
            void setup() {
                pinMode(13, OUTPUT);
            }

            void loop() {
                digitalWrite(13, HIGH);
                delay(1000);
                digitalWrite(13, LOW);
                delay(1000);
            }
            """
            program_developer_board("arduino", code)
        elif command == "send sms":
            to_number = input("Enter recipient number: ")
            message = input("Enter message: ")
            sms_sid = send_sms(to_number, message)
            print(f"SMS sent with SID: {sms_sid}")
        elif command == "make call":
            to_number = input("Enter recipient number: ")
            call_sid = make_call(to_number, "your_twilio_number", "http://demo.twilio.com/docs/voice.xml")
            print(f"Call initiated with SID: {call_sid}")
        elif command == "chat":
            user_input = input("You: ")
            response = get_chatbot_response(user_input)
            print(f"JARVIS: {response}")
        elif command == "generate api key":
            platform = input("Enter platform: ")
            api_key = generate_api_key(platform)
            if api_key:
                print(f"Generated API key for {platform}: {api_key}")
            else:
                api_key_link = search_api_key(platform)
                print(f"Found API key link for {platform}: {api_key_link}")
        elif command == "schedule task":
            task = input("Enter task: ")
            task_time = input("Enter time (HH:MM): ")
            add_task(task, task_time)
            print(f"Scheduled task '{task}' at {task_time}")
        elif command == "edit task":
            old_task = input("Enter old task: ")
            new_task = input("Enter new task: ")
            task_time = input("Enter time (HH:MM): ")
            edit_task(old_task, new_task, task_time)
            print(f"Edited task '{old_task}' to '{new_task}' at {task_time}")
        elif command == "clear schedule":
            clear_schedule()
            print("Cleared all scheduled tasks")
        elif command == "create program":
            platform = input("Enter platform (android/windows/linux/mac): ")
            language = input("Enter programming language: ")
            project_name = input("Enter project name: ")
            create_program(platform, language, project_name)
        elif command == "exit":
            print("Shutting down the assistant...")
            break
        else:
            print("Unknown command. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
