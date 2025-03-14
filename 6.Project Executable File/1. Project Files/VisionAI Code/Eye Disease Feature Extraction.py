import numpy as np
import cv2
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model

# Load the image
image_path = r'C:\\Users\\prash\\Desktop\\Medical\\mediscan\\data\\raw\\test\\NRG\\EyePACS-TRAIN-NRG-2982.jpg'
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is None:
    print(f"Error: Image not found at {image_path}")
else:
    # Resize the image to match VGG16 input size (224x224 or whatever size you want)
    resized_image = cv2.resize(image, (224, 224))

    # Convert the image to a float32 array and normalize it
    normalized_image = np.array(resized_image, dtype=np.float32)
    normalized_image = preprocess_input(normalized_image)  # Preprocessing step required for VGG16

    # Load the VGG16 model without the top fully connected layers
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Create a model that outputs features from the last convolutional layer
    feature_extractor = Model(inputs=base_model.input, outputs=base_model.output)

    # Extract features from the normalized image
    features = feature_extractor.predict(np.expand_dims(normalized_image, axis=0))

    # Print the shape of the features
    print("Extracted Features Shape:", features.shape)
