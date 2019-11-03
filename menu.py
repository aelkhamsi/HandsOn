import numpy as np
import cv2
import math
import time
import serial

bgSubThreshold = 20
cap = cv2.VideoCapture(0)

#port = "COM3"
#baud = 9600
 
#ser = serial.Serial(port, baud)
    # open the serial port
#if ser.isOpen():
     #print(ser.name + ' is open...')
     
## Background Model
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame,(100,0),(500,320),(0,255,0),2)
    cv2.imshow("frame",frame)
    frame = frame[0:320,100:500]
    if cv2.waitKey(30) & 0xFF == ord('b'):
        bgModel = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
        break

## Main Operation    
k = 0
ch = ' '

[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,esc,sup,ok] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

while True:
    
    ret, frame = cap.read()
    frame = frame[0:320,100:500]
    fgmask = bgModel.apply(frame,learningRate = 0.00001)
    kernel = np.ones((7, 7), np.uint8)
    fgmask = cv2.erode(fgmask,kernel,iterations = 1)
    
    
    res = cv2.bitwise_and(frame,frame, mask=fgmask)
    
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    
    retval , thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    thresh = cv2.medianBlur(thresh,5)
    
## Drawing Keyboard
    
    icon1 = cv2.imread("1.png")
    icon2 = cv2.imread("2.png")
    icon3 = cv2.imread("3.png")
    icon4 = cv2.imread("4.png")
    icon5 = cv2.imread("5.png")
    icon6 = cv2.imread("6.png")
    icon7 = cv2.imread("7.png")
    icon8 = cv2.imread("8.png")
    icon9 = cv2.imread("9.png")

    frame[36:100,100:164] = icon1
    frame[36:100,164:228] = icon2
    frame[36:100,228:292] = icon3
    frame[100:164,100:164] = icon4
    frame[100:164,164:228] = icon5
    frame[100:164,228:292] = icon6
    frame[164:228,100:164] = icon7
    frame[164:228,164:228] = icon8
    frame[164:228,228:292] = icon9
    
    
    
    
## Track fingertip    
    _,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if contours != []:
        #ch = " "    
        # Maximum countour area
        maxArea = 0
        ind = 0
        for i in range(len(contours)):
            if cv2.contourArea(contours[i])>maxArea:
                maxArea = cv2.contourArea(contours[i])
                ind = i
        cnt = contours[ind][:]
        
        # Topmost    
        topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
        cv2.circle(frame, topmost, 5, [255, 0, 0], -1)
        ty = topmost[0]
        tx = topmost[1]
        
        #Tracking
        
        
        
          
           
    # Drawing
    cv2.drawContours(frame, [cnt],0, (0,255,0),2)

    cv2.imshow("frame",frame)
    
    
    #cv2.imshow("gray",gray)
    #cv2.imshow("fgmask",fgmask)
    #cv2.imshow("thresh",thresh)


    if cv2.waitKey(1) & 0xFF==27:
        break
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("meenu2.jpg",frame)


cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
