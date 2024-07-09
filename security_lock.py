# src/security_lock.py
import cv2
import face_recognition
from tkinter import Tk, Label, Entry, Button, StringVar

# Function for facial recognition
def facial_recognition_unlock(known_face_encodings):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                cap.release()
                cv2.destroyAllWindows()
                return True
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return False

# Function for password unlock
def password_unlock(correct_password):
    def check_password():
        if password_var.get() == correct_password:
            root.destroy()
            return True
        else:
            label.config(text="Incorrect password. Try again.")
    
    root = Tk()
    root.title("Password Unlock")

    label = Label(root, text="Enter Password:")
    label.pack()
    
    password_var = StringVar()
    password_entry = Entry(root, textvariable=password_var, show="*")
    password_entry.pack()

    submit_button = Button(root, text="Submit", command=check_password)
    submit_button.pack()

    root.mainloop()

# Test the security lock functions
if __name__ == "__main__":
    known_image = face_recognition.load_image_file("known_face.jpg")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    
    if facial_recognition_unlock([known_face_encoding]):
        print("Facial recognition successful. Unlocked.")
    else:
        print("Facial recognition failed. Enter password.")
        if password_unlock("your_password"):
            print("Password correct. Unlocked.")
        else:
            print("Access denied.")
