import cv2
import numpy as np

# Vals to resize frames
frame_wid = 640
frame_hyt = 480

def increase_text_quality(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Resize the frame to optimize the run
    image = cv2.resize(image, (frame_wid, frame_hyt))

    # Enhance Image Quality
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=1)

    # Perform bitwise-and operation to extract the text regions
    result = cv2.bitwise_and(image, image, mask=opening)

    # Display the original and enhanced images
    cv2.imshow('Original', image)
    cv2.imshow('Enhanced', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    increase_text_quality('test/2.jpg')


if __name__ == '__main__':
    main()