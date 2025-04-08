import cv2,os,sys,numpy

video=cv2.VideoCapture("Cars.mp4")
haarfile="cars.xml"
car_Cascade=cv2.CascadeClassifier(haarfile)
while True:
    ret,frames=video.read()
    im2=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars=car_Cascade.detectMultiScale(im2,1.1,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(200,130,130),5)
    cv2.imshow("frames",frames)
    k=cv2.waitKey(10)
    if k==27:
        break
cv2.destroyAllWindows()