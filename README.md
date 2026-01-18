Real-Time Face Detection using OpenCV (Python)

A simple and beginner-friendly real-time face detection system using Python and OpenCV.
This project uses OpenCV’s Haar Cascade Classifier to detect human faces through a webcam and display bounding boxes with labels.

📸 Demo

1. Detects faces from live webcam feed

2. Draws a rectangle around detected faces

3. Displays text: “Face Detected”

4. Press q to exit the camera window.

🚀 Features

1. Real-time face detection

2. Pre-trained Haar Cascade model

3. Works with laptop or USB webcam

4. Lightweight & fast

5. Beginner-friendly code structure

🛠️ Tech Stack

1. Language: Python

2. Library: OpenCV (cv2)

3. Model: Haar Cascade (frontal face)

📂 Project Structure
face-detection-opencv/
│
├── face_detection.py
└── README.md

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/face-detection-opencv.git
cd face-detection-opencv

2️⃣ Install Dependencies
pip install opencv-python

▶️ Run the Project
python face_detection.py

⚙️ How It Works

1. Loads Haar Cascade XML model from OpenCV

2. Opens webcam using cv2.VideoCapture(0)

3. Reads frames continuously

4. Converts frames to grayscale

5. Detects faces using detectMultiScale()

6. Draws rectangles and labels on detected faces

7. Exits when q is pressed

⌨️ Controls
Key	Action
q	Quit application
📝 Notes

1.Ensure webcam permissions are enabled

2.Close other apps using the camera

3.If camera doesn’t open, try:

cv2.VideoCapture(1)

📈 Future Enhancements

1.Face recognition (name identification)

2.Save detected face images

3.Deep learning-based detection (CNN, DNN)

4.GUI integration (Tkinter / PyQt)
