import cv2
import numpy as np

img = cv2.imread("images/image.jpg")

#img = cv2.flip(img, -1)

def rotate(img_param, angle):
    height,width = img.shape[:2]
    point = (width // 2, height //2)

    mat = cv2.getRotationMatrix2D(point,angle,0.5)
    return cv2.warpAffine(img_param,mat,(width,height))

#img = rotate(img, 90)

def transform(img_param,x,y):
    mat = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img_param,mat,(img_param.shape[1],img_param.shape[0]))

img = cv2.resize(img,(img.shape[1] // 2,img.shape[0] // 2))
img = transform(img,30,200)
cv2.imshow("Result",img)

cv2.waitKey(0)