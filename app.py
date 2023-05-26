from flask import Flask, request, render_template, send_file
from PIL import Image
import cv2
import csv
import os
import numpy as np
from datetime import datetime
from ultralytics import YOLO
import pytesseract

# C:\Program Files\Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r'--oem 3 --psm 6 outputbase digits'

# Settings
class_name = 'railway-train-id'
detection_color = (255, 50, 255)
model = YOLO("models/railway-train-id.pt", "v8")

# Vals to resize frames
frame_wid = 640
frame_hyt = 480

# Function to Add new Wagon_ID to the Database
def add_record(wagon_id, datetime):
    # Check Wagon ID for Validness:
    if len(wagon_id) < 8:
        return

    # Check if the Wagon_id already exists or not
    with open('records.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == wagon_id:
                print(f"Wagon ID {wagon_id} already exists.")
                return

    # Get the last ID from the existing records (auto-increment)
    try:
        with open('records.csv', 'r') as file:
            reader = csv.DictReader(file)
            records = list(reader)
            last_id = int(records[-1]['id'])
    except IndexError:
        last_id = 0

    # Increment the ID and append the new record
    new_id = last_id + 1
    new_record = {'id': str(new_id), 'wagon_id': wagon_id, 'datetime': datetime}

    with open('records.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'wagon_id', 'datetime'])
        writer.writerow(new_record)

    print(f"Record with ID {new_id} added successfully.")


# Process Image Function
def process_image_func(image):
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Resize the frame to optimize the run
    frame = cv2.resize(frame, (frame_wid, frame_hyt))
    result = frame
    accuracy_score = 0
    id_number = 0

    # Convert tensor array to numpy
    detect_params = model.predict(source=[frame], conf=0.45, save=False)
    DP = detect_params[0].numpy()
    print(DP)

    if len(DP) != 0:
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            # Cropping wagon number from the main Image
            result = frame[int(bb[1]):int(bb[3]), int(bb[0]):int(bb[2])]

            # Processing image number through OCR engine
            boxes = pytesseract.image_to_data(result, config=myconfig)
            for x, b in enumerate(boxes.splitlines()):
                if x != 0:
                    b = b.split()
                    if len(b) == 12:
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        cv2.rectangle(result, (x, y), (w + x, h + y), (0, 0, 255), 1)
                        cv2.putText(result, b[11], (x + 45, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (50, 50, 255),
                                    1)
                        accuracy_score = b[10]
                        id_number = b[11]
                        add_record(id_number, datetime.now().strftime("%D/%M/%Y %H:/%M:%S"))

    return result, accuracy_score, id_number


# Flask Web App things...
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html', process_image='url')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return 'No image file uploaded'

    file = request.files['image']

    if file.filename == '':
        return 'No selected image'

    try:
        image = Image.open(file)
        processed_image, accuracy_score, number_id = process_image_func(image)

        # Save the processed image to a temporary file
        temp_filename = 'processed_image.jpg'
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(app.static_folder, temp_filename), processed_image)

        return render_template('result.html', filename=temp_filename, accuracy_score=accuracy_score, number_id=number_id)
    except Exception as e:
        return f'Error processing image: {str(e)}'

@app.route('/display_image/<filename>')
def display_image(filename):
    return send_file(filename, mimetype='image/jpeg')

@app.route('/table')
def display_table():
    records = []
    with open('records.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)

    return render_template('table.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
