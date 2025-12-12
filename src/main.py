#face detection on video stream

import cv2 as cv 
import numpy as np
from tkinter import messagebox
def video_face_detection(m):#m is the camera index or video file path
    #use it to do face detection on video stream from webcam or video file
    #if video file path is given then it will do face detection on that video file
    #use 0 for default camera, use 1 or 2 for external cameras

    video=cv.VideoCapture(m)
    while True:
        try:
            ret,frame=video.read()#read frame by frame,a boolean along with frame is also produced which tells if frame is read correctly or not
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert frame to gray scale
            face_cascade=cv.CascadeClassifier(r'C:\Users\DEVATHEERTH\OneDrive\Desktop\opencv project\haarcascade_fronalface.xml')
            #load the haarcascade classifier for face detection
            faces=face_cascade.detectMultiScale(gray,1.1,5)#detect faces in the frame
            #  1.1 is scale factor, 5is minNeighbors
            #USE LOWER VALUES OF MINNEIGHBORS FOR MORE DETECTIONS,BUT MORE FALSE POSITIVES(HIGH NOISY AND GROUPS OF PEOPLE VIDOES AND IMAGES )
            #USE HIGHER VALUES OF MINNEIGHBORS FOR LESS DETECTIONS,BUT LESS FALSE POSITIVES('LOW NOISE AND LESS GROUPS OF PEOPLE VIDOES AND IMAGES ')

            for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            cv.imshow('Video',frame)

            if cv.waitKey(1) & 0xFF==ord('q'):#press q to quit
                break

        except:
            messagebox.showinfo('ALERT',"END OF VIDOE FILE ")
            break 

m=eval(input("Enter camera index (0 for default camera) or video file path in quotes: "))
video_face_detection(m)#calling the function 
