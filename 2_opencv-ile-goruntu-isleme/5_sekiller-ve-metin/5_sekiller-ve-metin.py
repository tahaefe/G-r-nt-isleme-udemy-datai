# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:59:21 2021

@author: efeet
"""


import cv2
import numpy as np

# resim oluştur
img = np.zeros((512,512,3), np.uint8) #siyah resim
print(img.shape)

cv2.imshow("Siyah", img)

# çizgi
# çizgi resim, başlangıç nok, bitiş nok, renk
cv2.line(img, (100,100), (100,500), (0,255,0), 3) # BGR = Opencv blu green red gösterir
cv2.imshow("cizgi", img)

# dikdörtgen
# (resim, başlangıç, bitiş, renk)
cv2.rectangle(img, (0,0), (256,256), (0,0,255), cv2.FILLED)
cv2.imshow("Dikdortgen", img)

# çember
# (resim, merkez, yarı çap, renk)
cv2.circle(img, (300,300), 45, (255,0,0), cv2.FILLED)
cv2.imshow("cember", img)

# metin
# # (resim, başlangıç, font,kalınlık, renk)
cv2.putText(img, "resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("metin", img)