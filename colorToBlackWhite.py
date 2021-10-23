import cv2
#getting image
img=cv2.imread('D:\OneDrive\Pictures\Arkapratimghosh.jpg',cv2.IMREAD_ANYCOLOR)
#setting threshold
thresh=128
imgbw=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)[1]
#save image
cv2.imwrite('D:\OneDrive\Pictures\ArkapratimghoshBW4.jpg',imgbw)