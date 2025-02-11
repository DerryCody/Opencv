import cv2

Night=cv2.imread("NightSky.jpg",cv2.IMREAD_COLOR)

Ruin=cv2.imread("Ruins.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Ruins",Ruin)
cv2.imshow("Night",Night)
blend=cv2.addWeighted(Night,0.2,Ruin,0.8,1)

cv2.imshow("blendedimage",blend)
cv2.waitKey(0)
cv2.destroyAllWindows()