import cv2
import numpy as np

# creating a video capture object and read from input file
cap = cv2.VideoCapture('patan_video.mp4')

#detecting face in the video
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read until video is completed

while (True):
    #capture frame by freme
    ret, frame = cap.read()
    #converting the video into the gray video without colour
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    #detect faces in the vido
    faces = face_cascade.detectMultiScale(gray, 1.3 ,5)

    #draw the rectangle box around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle (frame, (x,y), (x+w, y+h),(0,255,0), 3)


    #displaying the resulting frame
    cv2.imshow('Frame',frame)

    #press q on keyboard to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

#when everything is done realease the video capture object
cap.release()

#closes all the frames
cv2.destroyAllWindows()