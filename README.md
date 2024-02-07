# Real-Time Face and Eye Detection using OpenCV

This Python script utilizes OpenCV to perform real-time face and eye detection through the webcam feed. It detects faces and draws rectangles around them, and within those rectangles, it further identifies and outlines eyes.

## How to Use

1. Clone this repository or download the Python script.
2. Ensure you have a webcam connected to your system.
3. Run the script.
4. A window will open displaying the webcam feed with rectangles drawn around detected faces and eyes outlined within those rectangles.
5. Press 'q' to exit the application.

## Dependencies

- OpenCV (`pip install opencv-python`)

## Parameters

- `cap`: Captures video frames from the webcam.
- `face_cas`: Haar cascade classifier for detecting faces.
- `eye_cas`: Haar cascade classifier for detecting eyes.
- `gray`: Grayscale version of the captured frame.
- `faces`: Array containing coordinates of detected faces.
- `eyes`: Array containing coordinates of detected eyes within a face.
- `ret`: A boolean value indicating if a frame is successfully read.
- `frame`: The current video frame captured from the webcam.
- `roi_gray`: Region of interest (ROI) representing the grayscale face area.
- `roi_color`: Region of interest (ROI) representing the color face area.

## Note

- The accuracy of the detection can be adjusted by modifying the scaling factor (`1.3`) and minimum neighbors (`5`) parameters in the `detectMultiScale` function.
