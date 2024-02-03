from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2

app = Flask(__name__)
model = YOLO("runs/detect/train/weights/best.pt")
cap = cv2.VideoCapture("rtsp://50.252.187.218:554/axis-media/media.amp")

def generate_frames():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform YOLOv5 prediction
        model.predict(frame, save=True, show=False, conf=0.5)
        # frame_with_predictions = results.xyxy[0].render()[0]

        # Convert frame to JPEG
        # ret, buffer = cv2.imencode('.jpg', frame_with_predictions)
        with open('/home/kamal/python/RealTime-Traffic-vehicle-detection/runs/detect/predict/image0.jpg', 'rb') as file:
            image_bytes = file.read()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
