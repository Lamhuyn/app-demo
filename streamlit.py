import streamlit as st
from PIL import Image
import cv2 
import numpy as np
import pytesseract
import os
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
        img=os.path.join("fileDir", image_file.name)
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        img= cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes=pytesseract.image_to_data(img)
        for x,b in enumerate(boxes.splitlines()):
            if x!=0 :
                b=b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]) , int(b[7]) ,int(b[8]),int(b[9])
                    cv2.rectangle(img, (x,y) , (x+w , y+h) , (0,0,255),2)
                    cv2.putText(img , b[11] , (x,y) , cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),1)
        st.image(img)



