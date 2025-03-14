import cv2
import numpy as np
import os

# Function to preprocess the image
def preprocess_image(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur for noise reduction
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Normalize the image pixel values
    norm_img = cv2.normalize(blur, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Enhance contrast using histogram equalization
    enhanced_img = cv2.equalizeHist(norm_img)

    return enhanced_img

# Function to segment the image using thresholding
def segment_image(img):
    # Apply a binary threshold to the grayscale image
    _, segmented_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    return segmented_img

# Paths to save processed and segmented images
processed_folder = 'C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\processed\\'
segmented_folder = 'C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\segmented\\'

# Create the directories if they don't exist
os.makedirs(processed_folder, exist_ok=True)
os.makedirs(segmented_folder, exist_ok=True)

# Load an example image
img = cv2.imread('C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\raw\\test\\NRG\\EyePACS-TRAIN-NRG-2982.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Preprocess the image
    processed_img = preprocess_image(img)

    # Segment the preprocessed image
    segmented_img = segment_image(processed_img)

    # Display the original, processed, and segmented images
    cv2.imshow("Original Image", img)
    cv2.imshow("Processed Image", processed_img)
    cv2.imshow("Segmented Image", segmented_img)

    # Save the processed and segmented images in their respective folders
    processed_image_path = os.path.join(processed_folder, 'processed_EyePACS-TRAIN-NRG-2982.jpg')
    segmented_image_path = os.path.join(segmented_folder, 'segmented_EyePACS-TRAIN-NRG-2982.jpg')

    # Save images
    cv2.imwrite(processed_image_path, processed_img)
    cv2.imwrite(segmented_image_path, segmented_img)

    print(f"Processed image saved at: {processed_image_path}")
    print(f"Segmented image saved at: {segmented_image_path}")

    # Display the original and processed images
cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", processed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
