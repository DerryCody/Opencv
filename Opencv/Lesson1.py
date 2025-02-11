import cv2

pikachu=cv2.imread("Images/pika.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("pikachuimage",pikachu)
cv2.waitKey(0)
cv2.destroyAllWindows()

pikachu=cv2.imread("Images/pika.png",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("Images/greypikachu.png",pikachu)
cv2.imshow("pikachuimage",pikachu)
cv2.waitKey(0)
cv2.destroyAllWindows()

pikachu2=cv2.imread("Images/pika.png",cv2.IMREAD_COLOR)
B,G,R=cv2.split(pikachu2)
cv2.imshow("pikachugreenimage",G)
cv2.imshow("pikachuredimage",R)
cv2.imshow("pikachublueimage",B)
cv2.waitKey(0)
cv2.destroyAllWindows()