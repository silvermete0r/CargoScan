import cv2
import csv
import numpy as np
from datetime import datetime
from ultralytics import YOLO
import pytesseract
# C:\Program Files\Tesseract-OCR

# Settings
class_name = 'railway-train-id'
detection_color = (255,50,255)
model = YOLO("models/railway-train-id.pt", "v8")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
myconfig = r'--oem 1 --psm 6 outputbase digits'

# Vals to resize frames
frame_wid = 640
frame_hyt = 480

# Function to Add new Wagon_ID to the Database
def add_record(wagon_id, datetime):
    # Check Wagon ID for the Validness:
    if len(wagon_id)<8:
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


# Main Loop ()
while True:
    frame = cv2.imread('test/6.jpg')

    # Resize the frame to optimize the run
    frame = cv2.resize(frame, (frame_wid, frame_hyt)) 
    result = None

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

            # cv2.rectangle(frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_color, 3)
            
            # Cropping wagon number from the main Image
            result = frame[int(bb[1]):int(bb[1])+int(bb[3]),int(bb[0]):int(bb[0])+int(bb[2])]

            # Processing image number through OCR engine
            hImg, wImg, _ = result.shape
            boxes = pytesseract.image_to_data(result, config=myconfig)
            for x,b in enumerate(boxes.splitlines()):
                if x!=0:
                    b = b.split()
                    if len(b) == 12:
                        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                        cv2.rectangle(result,(x,y),(w+x,h+y),(0,0,255),1)
                        cv2.putText(result,b[11],(x+45,y+h+30),cv2.FONT_HERSHEY_COMPLEX,0.8,(50,50,255),1)
                        add_record(b[11],datetime.now().strftime("%D/%M/%Y %H:/%M:%S"))
                        print(b)

    # Display the Results
    if result is not None:
        cv2.imshow("CargoScan: Detected Wagon ID", result)
    else:
        cv2.imshow("CargoScan: Wagon ID has not been detected!", frame)

    # Terminate run when "ESC" is pressed
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Closing all windows
cv2.destroyAllWindows()
