import cv2 as cv
import numpy as np
img = cv.imread('/home/user/Загрузки/2.png', 1)
cv.imwrite('/home/user/Загрузки/img2.png', img)
cimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gr",imgray)
ret, thresh = cv.threshold(imgray, 120, 255, 0)
cv.imshow('bin', thresh)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(contours)
cv.drawContours(img, contours, -1, (0,0,255), 1)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

