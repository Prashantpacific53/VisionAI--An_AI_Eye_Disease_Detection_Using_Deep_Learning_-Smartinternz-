import os
import cv2

def apply_preprocessing(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    equalized_image = cv2.equalizeHist(blurred_image)
    normalized_image = cv2.normalize(equalized_image, None, 0, 255, cv2.NORM_MINMAX)
    _, segmented_image = cv2.threshold(normalized_image, 128, 255, cv2.THRESH_BINARY)
    return segmented_image

def mapping_function(src_dir, dst_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Image file formats
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, src_dir)
                dst_path = os.path.join(str(dst_dir), str(relative_path), file)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                try:
                    img = cv2.imread(str(src_path))  # Read image with OpenCV
                    if img is None:
                        print(f"Error reading {src_dir}")
                        continue
                    processed_img = apply_preprocessing(img)
                    cv2.imwrite(dst_path, processed_img)  # Save the processed image
                    # show_image(processed_img)
                    print(f"Processed and saved: {dst_path}")
                except Exception as e:
                    print(f"Error processing {src_path}: {e}")
            # break


src_directory = r'MediScan-AI-Powered-Medical-Image-Analysis-for-Disease-Diagnosis_0ct_2024\mediscan-env\data\raw\dataset\cataractDataset'
dst_directory = r'MediScan-AI-Powered-Medical-Image-Analysis-for-Disease-Diagnosis_0ct_2024\mediscan-env\data\processed\cataractDataset'

mapping_function(src_directory, dst_directory)


def show_image(image):
    cv2.imshow("Frame", image)
    cv2.waitKey(200000)
    cv2.destroyAllWindows()