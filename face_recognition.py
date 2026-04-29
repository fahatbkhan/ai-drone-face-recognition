import cv2
import face_recognition

# Load known image
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        if True in match:
            print("Authorized Face Detected → Trigger Payload")

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()