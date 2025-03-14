import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to segment the image
def segment_image(image):
    # Normalize the image
    normalized_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Convert to grayscale
    gray_image = cv2.cvtColor(normalized_image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding for segmentation
    _, segmented_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    return gray_image, segmented_image

# Folder paths
input_folder = r'C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\raw\\test\\NRG\\'
segmented_folder = r'C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\segmented\\'

# Create the segmented folder if it does not exist
os.makedirs(segmented_folder, exist_ok=True)

# List all the image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

# Process each image in the folder
for i, filename in enumerate(image_files):
    file_path = os.path.join(input_folder, filename)

    # Load the image
    image = cv2.imread(file_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Image not found at {file_path}")
        continue

    # Segment the image
    gray_image, segmented_image = segment_image(image)

    # Save the segmented image in the segmented folder
    save_path = os.path.join(segmented_folder, filename)
    cv2.imwrite(save_path, segmented_image)

    # Display the first image in the folder
    if i == 0:
        plt.figure(figsize=(10, 5))
        
        # Show original image
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image")
        
        # Show grayscale image
        plt.subplot(1, 3, 2)
        plt.imshow(gray_image, cmap='gray')
        plt.title("Grayscale Image")
        
        # Show segmented image
        plt.subplot(1, 3, 3)
        plt.imshow(segmented_image, cmap='gray')
        plt.title("Segmented Image (Binary)")
        
        plt.show()

print(f"All images processed and saved in the 'segmented' folder.")
