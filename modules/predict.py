import cv2 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"
def main(imgage):
    img= cv2.imread(imgage)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes=pytesseract.image_to_string(img, lang='eng')
    for x,b in enumerate(boxes.splitlines()):
            if x!=0 :
                b=b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]) , int(b[7]) ,int(b[8]),int(b[9])
                    cv2.rectangle(img, (x,y) , (x+w , y+h) , (0,0,255),2)
                    cv2.putText(img , b[11] , (x,y) , cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),1)
    return img