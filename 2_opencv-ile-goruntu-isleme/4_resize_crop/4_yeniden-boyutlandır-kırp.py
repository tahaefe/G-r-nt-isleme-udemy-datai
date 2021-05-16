# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:43:48 2021

@author: efeet
"""

import cv2

#
img = cv2.imread("lenna.png")
print("Resim Boyutu: ", img.shape)
cv2.imshow("orijinal", img)


imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("imgResized", imgResized)

# kırp
imgCropped = img[:200,:300]
cv2.imshow("Kırpılan Resim",imgCropped)