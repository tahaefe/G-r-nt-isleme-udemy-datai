# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:22:07 2021

@author: efeet
"""

import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("61.jpg", 0 )
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("orijinal Img")

# x gradyan
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize =5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("sobelx Img")


# y gradyan
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize =5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("sobely Img")

# laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("laplacian Img")
