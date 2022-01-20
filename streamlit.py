import streamlit as st
from PIL import Image
import cv2 
import numpy as np
import pytesseract
import os
from modules.predict import main
def load_image(image_file):
    img = Image.open(image_file)
    return img

image_file = st.file_uploader("up load file :", type=["png" , "jpg" , "jpeg"])
if image_file is not None :
    file_details = {"filename":image_file.name ,
                    "filetype" : image_file.type,
                    "filesize": image_file.size}
    st.write(file_details) 
    with open(os.path.join("fileDir", image_file.name), "wb") as f:
        f.write((image_file).getbuffer())
    click = st.button("Process")
    if  click:
        st.header("result: ")
        img=main(image_file)
        st.image(img)

