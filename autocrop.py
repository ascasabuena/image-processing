# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:25:11 2019

@author: ascas
"""

import cv2
import glob as gb

images = gb.glob('gills/fresh/*.*')
faceCascade = cv2.CascadeClassifier('GillDetector.xml')

n=0
for file in images:
    print(file[12:])
    frame = cv2.imread(file)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x , y),(x+w,y+h),(0,255,0),2)
        
        gill = cv2.resize(frame[y:y+h, x:x+w],(300,300))
        cv2.imwrite(str(n)+file[12:], gill)
        n = n + 1 
        
        
        