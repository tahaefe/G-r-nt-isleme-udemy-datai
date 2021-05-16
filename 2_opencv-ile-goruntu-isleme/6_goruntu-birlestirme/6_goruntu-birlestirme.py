# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:18:37 2021

@author: efeet
"""


import cv2
import numpy as np

# resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("orjinal", img)

# yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal",hor)

# dikey
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)