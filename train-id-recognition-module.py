import cv2
import numpy as np
from ultralytics import YOLO

# Set Class Name
class_name = 'railway-train-id'

# Set Color
detection_color = (255,50,255)

# Load a pretrained YOLOv8n model
model = YOLO("models/railway-train-id.pt", "v8")

# Vals to resize video frames
frame_wid = 640
frame_hyt = 480

# cap = cv2.VideoCapture(0)  #'0' -> webcam \ '1' -> video-cam-1
cap = cv2.VideoCapture("test/video.mp4")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    _, frame = cap.read()

    if not _:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # frame = cv2.imread('data/second/second1403.jpg')

    # Resize the frame to optimize the run
    frame = cv2.resize(frame, (frame_wid, frame_hyt))

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()
    print(DP)

    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i] 
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            cv2.rectangle(frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_color, 3)

            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText( frame, class_name + " " + str(round(conf, 3)) + "%", (int(bb[0]), int(bb[1]) - 10), font, 1, (255, 255, 255), 2)

    # Display the Results
    cv2.imshow("CargoScan", frame)

    # Terminate run when "ESC" is pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()