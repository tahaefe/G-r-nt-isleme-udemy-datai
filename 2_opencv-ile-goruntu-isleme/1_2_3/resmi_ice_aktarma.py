# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 02:42:43 2021

@author: efeet
"""

import cv2

#ice aktarma
img = cv2.imread("ronaldak.jpg", 0)

#gorselleştir
cv2.imshow("Ilk Resim", img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("ronal_gr.png", img)
    cv2.destroyAllWindows()
    