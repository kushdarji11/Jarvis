import cv2
import numpy as np

camera_input = cv2.VideoCapture(0);

identifier = input("Enter User ID:");
sample = 0
while(True):
    ret,img = camera_input.read()
    
    sample = sample + 1
    path = ''
    cv2.imwrite("D:/pics/UserImg_"+str(identifier)+"."+str(sample)+".jpg",img)
    cv2.imshow('Face',img)

    if(sample>0):
            break;
camera_input.release()
cv2.destroyAllWindows()
                
