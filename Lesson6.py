import cv2
import numpy
import time

path="Images2/video.mp4"
videop=cv2.VideoCapture(path)
background=0
time.sleep(1)
counter=0

for i in range(60):
    returnval,background=videop.read()
    if returnval==False:
        continue
background=numpy.flip(background,axis=1)
while(videop.isOpened()):
    returnval,image=videop.read()
    if not returnval:
        break
    else:
        counter=counter+1
    image=numpy.flip(image,axis=1)
    imagec=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lwr=numpy.array([100,40,40])
    hgr=numpy.array([100,255,255])
    mask1=cv2.inRange(imagec,lwr,hgr)
    lwr=numpy.array([155,40,40])
    hgr=numpy.array([180,255,255])
    mask2=cv2.inRange(imagec,lwr,hgr)
    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
    mask1=cv2.dilate(mask1,numpy.ones((3,3),numpy.uint8),iterations=1)
    mask2=cv2.bitwise_not(mask1)
    result1=cv2.bitwise_and(background,background,mask=mask1)
    result2=cv2.bitwise_and(image,image,mask=mask2)
    final_result=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("Video",final_result)
    k=cv2.waitKey(10)
    if k==27:
        break