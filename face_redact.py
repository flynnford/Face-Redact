import cv2
import sys

def blur_faces(image_path):
    # Load the face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Could not open the image file!")
        return
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    print(f"Found {len(faces)} face(s)")
    
    # Blur each face
    for (x, y, w, h) in faces:
        face_region = image[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
        image[y:y+h, x:x+w] = blurred_face
    
    # Save the result
    output_path = image_path.replace('.', '_blurred.')
    cv2.imwrite(output_path, image)
    print(f"Saved blurred image to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python face_redact.py <image_path>")
        print("Example: python face_redact.py photo.jpg")
    else:
        image_path = sys.argv[1]
        blur_faces(image_path)