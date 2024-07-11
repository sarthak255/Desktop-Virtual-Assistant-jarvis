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
from image_generation import generate_image
from 3d_rendering import render_3d_scene
from encryption import encrypt_data, decrypt_data, generate_key
from advanced_scheduler import add_advanced_task, clear_schedule
from project_management import init_trello, create_trello_board, add_card_to_list
from content_aware_response import generate_content_aware_response
from multi_term_conversation import multi_term_conversation
from data_anonymization import anonymize_data
from semantic_search import semantic_search
from real_time_data_fetching import fetch_weather_data
from visual_recognition import recognize_faces
from augmented_reality import augmented_reality_effect
from screen_reader import read_screen_text

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
        elif command == "generate image":
            generate_image()
        elif command == "render 3d":
            scene_file = input("Enter path to Blender scene file: ")
            output_file = input("Enter output file name: ")
            render_3d_scene(scene_file, output_file)
        elif command == "encrypt data":
            data = input("Enter data to encrypt: ")
            key = generate_key()
            encrypted_data = encrypt_data(data, key)
            print(f"Encrypted Data: {encrypted_data}")
        elif command == "decrypt data":
            encrypted_data = input("Enter data to decrypt: ")
            key = input("Enter encryption key: ")
            decrypted_data = decrypt_data(encrypted_data.encode(), key.encode())
            print(f"Decrypted Data: {decrypted_data}")
        elif command == "advanced schedule task":
            task = input("Enter task: ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            add_advanced_task(task, start_time, end_time)
            print(f"Scheduled task '{task}' from {start_time} to {end_time}")
        elif command == "project management":
            api_key = input("Enter Trello API key: ")
            api_secret = input("Enter Trello API secret: ")
            token = input("Enter Trello token: ")
            token_secret = input("Enter Trello token secret: ")
            client = init_trello(api_key, api_secret, token, token_secret)
            board_name = input("Enter board name: ")
            board = create_trello_board(client, board_name)
            list_name = input("Enter list name: ")
            card_name = input("Enter card name: ")
            description = input("Enter card description: ")
            add_card_to_list(board, list_name, card_name, description)
        elif command == "content aware response":
            prompt = input("Enter prompt: ")
            response = generate_content_aware_response(prompt)
            print(f"Response: {response}")
        elif command == "multi-term conversation":
            context = input("Enter context: ")
            user_input = input("Enter user input: ")
            response = multi_term_conversation(context, user_input)
            print(f"Response: {response}")
        elif command == "anonymize data":
            data = {
                "name": input("Enter name: "),
                "address": input("Enter address: "),
                "email": input("Enter email: "),
                "phone": input("Enter phone: ")
            }
            anonymized_data = anonymize_data(data)
            print(f"Anonymized Data: {anonymized_data}")
        elif command == "semantic search":
            corpus = [
                "The weather is nice today.",
                "How is the weather tomorrow?",
                "It will rain today.",
                "Sunny weather expected tomorrow."
            ]
            query = input("Enter query: ")
            hits = semantic_search(corpus, query)
            print(f"Search Results: {hits}")
        elif command == "fetch weather":
            location = input("Enter location: ")
            weather_data = fetch_weather_data(location)
            print(f"Weather Data: {weather_data}")
        elif command == "visual recognition":
            image_path = input("Enter path to image: ")
            recognize_faces(image_path)
        elif command == "augmented reality":
            image_path = input("Enter path to image: ")
            overlay_path = input("Enter path to overlay: ")
            augmented_reality_effect(image_path, overlay_path)
        elif command == "screen reader":
            text = input("Enter text to read: ")
            read_screen_text(text)
        elif command == "exit":
            print("Shutting down the assistant...")
            break
        else:
            print("Unknown command. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
