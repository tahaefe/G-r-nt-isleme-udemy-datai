# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:36:25 2021

@author: efeet
"""

import cv2
import numpy as np

# içe aktar resim
img = cv2.imread("kart.png")
cv2.imshow("orijinal", img)

width = 400
height = 500

pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0, height], [width, 0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("yeni resim", imgOutput)