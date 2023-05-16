import cv2
import pytesseract

# C:\Program Files\Tesseract-OCR

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('imgs/dataset-health-check.png')
# print(pytesseract.image_to_string(img))


### Instructions
# PCR Page segmentation modes:
# 0 - Orientation and script detection (OSD) only.
# 1 - Automatic page segmentation with OSD.
# 2 - Automatic page segmentation, but no OSD, or OCR. (not implemented)
# 3 - Fully automatic page segmentation, but no OSD. (Default)
# 4 - Assume a single column of text of variable sizes.
# 5 - Assume a single uniform block of vertically aligned text.
# 6 - Assume a single uniform block of text.
# 7 - Treat the image as a single text line.
# 8 - Treat the image as a single word.
# 9 - Treat the image as a single word in a circle.
# 10 - Treat the image as a single character.
# 11 - Sparse text. Find as much text as possible in no particular order.
# 12 - Sparse text with OSD.
# 13 - Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

# OCR Engine modes:
# 0 - Legacy engine only - fastest.
# 1 - Neural nets LSTM engine only - better accuracy, but slower.
# 2 - Legacy + LSTM engines - best accuracy.
# 3 - Default, based on what is available.

## Detecting Words
hImg, wImg, _ = img.shape
myconfig = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=myconfig)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img,b[11],(x+10,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(50,50,255),1) 

# ## Detecting Words
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         if len(b) == 12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(50,50,255),1) 

# # Detecting Characters
# hImg, wImg, _ = img.shape
# myconfig = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, config=myconfig)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#     cv2.putText(img,b[0],(x,hImg-y+15),cv2.FONT_HERSHEY_COMPLEX,0.7,(50,50,255),1) 

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Result', img)

# Close on ESC Key
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break

