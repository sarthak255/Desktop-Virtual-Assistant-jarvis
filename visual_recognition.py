import cv2

# Function to recognize faces in an image
def recognize_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the visual recognition function
if __name__ == "__main__":
    image_path = "path_to_image.jpg"
    recognize_faces(image_path)
