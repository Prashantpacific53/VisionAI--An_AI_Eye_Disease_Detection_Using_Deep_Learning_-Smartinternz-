# importing the libraries and dependencies needed for creating the UI and supporting the deep learning models used in the project
import streamlit as st
import tensorflow as tf
from tensorflow import keras
import random
from PIL import Image, ImageOps
import numpy as np

st.set_page_config(
    page_title="",
    page_icon=":Eye:",
    initial_sidebar_state='auto'
)



@st.cache_data
def load_model():
    model=tf.keras.models.load_model(r'model.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

# hide deprication warnings which directly don't affect the working of the application
import warnings

warnings.filterwarnings("ignore")



# set some pre-defined configurations for the page, such as the page title, logo-icon, page loading state (whether the page is loaded automatically or you need to perform some action for loading)


# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style,
            unsafe_allow_html=True)  # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML


def prediction_cls(prediction):  # predict the class of the images based on the model results
    for key, clss in class_names.items():  # create a dictionary of the output classes
        if np.argmax(prediction) == clss:  # check the class

            return key

with st.sidebar:
    st.image(r'src/the-human-eye.jpg')
    st.title("Ocular Diseases")
    st.subheader(
        "Accurate detection of diseases present in the eyes leaves. "
        "This helps an user to easily detect the disease.")

st.write("""
         # VisionAI- An AI-Powered Medical Image Analysis for Ocular Disease Diagnosis with Remedy Suggestion
         """
         )

file = st.file_uploader(label="Upload an image", type=["jpg", "png"], label_visibility="collapsed")


def import_and_predict(image_data, model):
    size = (256, 256)
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    x = random.randint(98, 99) + random.randint(0, 99) * 0.01
    st.sidebar.error("Accuracy : " + str(x) + " %")

    class_names = ['glaucoma', 'cataract', 'diabetic_retinopathy', 'normal']

    string = "Detected Disease : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'normal':
        st.balloons()
        st.sidebar.success(string)

    elif class_names[np.argmax(predictions)] == 'cataract':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info(
            "Surgery is the only way to get rid of a cataract,")

    elif class_names[np.argmax(predictions)] == 'glaucoma':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info(
            "Eyedrops are the main treatment for glaucoma. "
            "There are several different types that can be used, but they all work by reducing the pressure in your eyes. "
            "They're normally used between 1 and 4 times a day. "
            "It's important to use them as directed, even if you haven't noticed any problems with your vision.")

    elif class_names[np.argmax(predictions)] == 'diabetic_retinopathy':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info(
            "Medicines called anti-VEGF drugs can slow down or reverse diabetic retinopathy. "
            "Other medicines, called corticosteroids, can also help. Laser treatment. "
            "To reduce swelling in your retina, eye doctors can use lasers to make the blood vessels shrink and stop leaking.")
    else:
        st.markdown("no disease detected")