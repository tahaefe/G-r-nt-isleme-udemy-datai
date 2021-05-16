# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

currentDir = os.getcwd()
print(currentDir)

os.chdir("D:\\efeet\\Documents")
print(os.getcwd())

dataikodlar = "DATAİKODLAR"
os.mkdir(dataikodlar)

os.chdir("D:\\efeet\\Documents"+"\\"+dataikodlar)

