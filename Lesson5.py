import cv2
import os
from PIL import Image
path="/Users/candice/Desktop/Python Work/Opencv/Images2"
os.chdir("/Users/candice/Desktop/Python Work/Opencv/Images2")
meanwidth=0
meanheight=0
numberofimg=len(os.listdir('.'))
for file in os.listdir(('.')):
  if file.endswith(".jpg") or file.endswith(".png") or file.endswith("jpeg"):
    image=Image.open(os.path.join(path,file))
    width,height=image.size
    meanwidth=meanwidth+width
    meanheight=meanheight+height
meanwidth=meanwidth//numberofimg
meanheight=meanheight//numberofimg
print(meanwidth)
print(meanheight)
for file in os.listdir(('.')):
  if file.endswith(".jpg") or file.endswith(".png") or file.endswith("jpeg"):
    img=Image.open(os.path.join(path,file))
    rimg=img.resize((meanwidth,meanheight),Image.Resampling.LANCZOS)
    rimg.save(file,"JPEG",quality=95)
    print(img.filename.split("//"),[-1],"is resized")
def create():
  video1="video1.mp4"
  os.chdir("/Users/candice/Desktop/Python Work/Opencv/Images2")
  images=[]
  for file in os.listdir(('.')):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith("jpeg"):
      images.append(img)
  frame=cv2.imread(os.path.join(".",images[0].filename))
  height,width,layers=frame.shape
  fourcc=cv2.VideoWriter_fourcc(*"mp4v")
  video=cv2.VideoWriter(video1,fourcc,1,(width,height))
  for image in images:
    video.write(cv2.imread(os.path.join(".",image.filename)))
  cv2.destroyAllWindows()
create()
    