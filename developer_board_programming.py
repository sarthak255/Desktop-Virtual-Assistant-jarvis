# src/developer_board_programming.py
# pip install pyserial arduino-python

import serial
from arduino import Arduino

# Function to program an Arduino board
def program_arduino(code, port="/dev/ttyUSB0"):
    board = Arduino(port)
    board.upload(code)
    board.close()

# Function to handle programming of various developer boards
def program_developer_board(board_type, code, port="/dev/ttyUSB0"):
    if board_type.lower() == "arduino":
        program_arduino(code, port)
    # Add support for other developer boards

# Test the developer board programming function
if __name__ == "__main__":
    arduino_code = """
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
    program_developer_board("arduino", arduino_code)
