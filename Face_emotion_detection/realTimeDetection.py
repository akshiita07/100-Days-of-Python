import cv2
from keras.models import model_from_json
import numpy as np

json_file=open("Face_emotion_detection/emotionDetector.json","r")
model_json=json_file.read()
json_file.close()
model=model_from_json(model_json)
model.load_weights("Face_emotion_detection/emotionDetector.h5")

# open our camera using cv2:
haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)

# function to extract feature from a single image
def feature_extract(image):
    feature=np.array(image)
    feature=feature.reshape(1,48,48,1)
    return feature/255.0

webcam=cv2.VideoCapture(0)

label={0:'angry',1:'disgust',2:'fear',3:'happy',4:'neutral',5:'sad',6:'surprise'}

while True:
    i,im=webcam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(im,1.3,5)
    
    try:
        for (p,q,r,s) in faces:
            image=gray[q:q+s,p:p+r]
            cv2.rectangle(im,(p,q),(p+r,q+s),(255,0,0),2)
            image=cv2.resize(image,(48,48))
            img=feature_extract(image)
            pred=model.predict(img)
            pred_label=label[pred.argmax()]
            cv2.putText(im,'% s' %(pred_label),(p-10,q-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255))
        
        cv2.imshow("Output",im)
        cv2.waitKey(27)
            
    except cv2.error:
        print("Some error occurred")