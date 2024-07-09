# src/expression_analysis.py
# pip install mediapipe dlib

import cv2
import mediapipe as mp
import dlib

# Initialize mediapipe face and hand detection
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands

# Initialize dlib for facial expression analysis
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to analyze facial expressions
def analyze_facial_expressions(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        # Analyze facial landmarks for expressions (smiling, frowning, etc.)
        # For simplicity, only analyzing the mouth area for smiling
        if landmarks.part(48).y - landmarks.part(66).y > 5:
            return "Smiling"
    return "Neutral"

# Function to analyze hand expressions
def analyze_hand_expressions(frame):
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Analyze hand landmarks for gestures (e.g., thumbs up, waving)
                if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                    return "Thumbs Up"
    return "Neutral"

# Function to analyze expressions
def analyze_expressions():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        facial_expression = analyze_facial_expressions(frame)
        hand_expression = analyze_hand_expressions(frame)
        print(f"Facial Expression: {facial_expression}, Hand Expression: {hand_expression}")
        cv2.imshow("Frame", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Test the expression analysis function
if __name__ == "__main__":
    analyze_expressions()
