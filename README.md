# VisionAI: AI-Powered Eye Disease Analysis

![VisionAI Banner](https://via.placeholder.com/1200x400?text=VisionAI+Banner)

## 🌟 Overview
VisionAI is an AI-powered system designed for **eye disease detection, diagnosis, and clinical decision support**. It leverages deep learning techniques to analyze eye images and identify potential diseases with high accuracy. The system aims to assist healthcare professionals in early detection and effective treatment planning.

## 📌 Features
- **Deep Learning-Based Diagnosis**: Uses EfficientNetB3 for high-accuracy predictions.
- **Image Preprocessing & Segmentation**: Enhances image quality and isolates key regions.
- **Multi-Class Classification**: Detects multiple eye diseases from retinal images.
- **Interactive Dashboard**: Visualizes predictions and confidence scores.
- **Clinical Decision Support**: Helps ophthalmologists with automated insights.

## 🏗️ Project Structure
```
VisionAI/
│-- data/                   # Dataset folder
│-- models/                 # Trained model files
│-- notebooks/              # Jupyter Notebooks for training and testing
│-- src/                    # Core source code
│   ├── preprocessing.py    # Image enhancement & normalization
│   ├── segmentation.py     # Region of Interest (ROI) isolation
│   ├── model.py           # EfficientNetB3 training script
│-- app/                    # Deployment code
│-- README.md               # Project documentation
```

## 📥 Installation
```bash
git clone https://github.com/yourusername/VisionAI.git
cd VisionAI
pip install -r requirements.txt
```

## 🔍 Dataset
- **Source**: [Kaggle - Eye Diseases Classification](https://www.kaggle.com/datasets/gunavenkatdoddi/eye-diseases-classification)
- **Size**: 4,217 images across 4 classes
- **Classes**: 
  - Normal
  - Cataract
  - Glaucoma
  - Retina Disease

## 🧠 Model Training
```bash
python src/model.py --epochs 50 --batch_size 32 --lr 0.001
```

## 🚀 Deployment
```bash
streamlit run app/app.py
```
And
```
right click on the .html file to run on live server

```

## 📊 Results & Performance
- **Training Accuracy**: ~95%
- **Validation Accuracy**: ~93%
- **Precision/Recall/F1 Score**: Available in `notebooks/evaluation.ipynb`

## 👨‍💻 Contributors
- **Prashant** - Lead Developer
- **Siddharaj**
- **Arun**
- **Lokesh**

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact
For queries, reach out us via open an issue in the repository.

---
⭐ **If you find this project useful, please consider starring the repo!** ⭐
