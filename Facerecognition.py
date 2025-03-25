import cv2,os,sys,numpy

haarfile="haarcascade_frontalface_default.xml"
datasets="datasets"
subfolder="Derry"
path=os.path.join(datasets,subfolder)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)=(130,100)

#CascadeClassifier used to detect object
face_cascade=cv2.CascadeClassifier(haarfile)
webcam=cv2.VideoCapture(0)
for i in range(30):
    (_,im)=webcam.read()
    im2=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(im2,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(200,130,130),5)
        face=im2[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(width,height))
        cv2.imwrite("%s/%s.png"%(path,(i+1)),face_resize)
    cv2.imshow("image",im)
    k=cv2.waitKey(10)
    if k==27:
        break