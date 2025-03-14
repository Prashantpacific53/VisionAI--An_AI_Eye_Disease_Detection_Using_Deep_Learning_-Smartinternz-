from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tqdm import tqdm
import numpy as np
import os

img_height = 256
img_width = 256

source_dir = '/content/drive/MyDrive/Infosys/data/diseaseDataset/diseaseDataset'
target_dir = '/content/drive/MyDrive/Infosys/data/extractedFeatures'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

# Create a feature extractor from VGG16
feature_extractor = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)


def extract_features(image_path):
    image = load_img(image_path, target_size=(img_height, img_width))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)

    features = feature_extractor.predict(image_array, verbose=0)
    return features

def process_and_save_image(source_path, target_base_dir):
    image_paths = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Process only image files
                image_path = os.path.join(root, file)
                image_paths.append(os.path.join(root, file))

    for image_path in tqdm(image_paths, unit="image"):
        features = extract_features(image_path)

        relative_path = os.path.relpath(image_path, source_path)
        target_path = os.path.join(target_base_dir, relative_path)

        target_folder = os.path.dirname(target_path)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        feature_file = target_path.replace('.jpg', '.npy').replace('.jpeg', '.npy').replace('.png', '.npy')
        np.save(feature_file, features)

process_and_save_image(source_dir, target_dir)