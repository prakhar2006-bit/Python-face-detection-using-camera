import cv2

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)

camera = cv2.VideoCapture(0)

while True:
    status, image = camera.read()
    if not status:
        break

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(gray, 1.3, 10)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 25, 25), 2)
        cv2.putText(
            image,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 10),
            2
        )

    cv2.imshow("Faces", image)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()