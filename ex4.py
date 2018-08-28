
#image resize using image pyramid
import cv2
import numpy as pd
img=cv2.imread("flower.jpg")
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow("original image",img)
cv2.imshow("smaller image",smaller)
cv2.imshow("larger image",larger)
cv2.waitKey()
cv2.destroyAllWindows()

