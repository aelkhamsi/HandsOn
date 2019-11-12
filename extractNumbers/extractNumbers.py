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
        cv2.imwrite("6.jpg",frame)
        break

## Main Operation    
k = 0
ch = "0"
while True:
    ret, frame = cap.read()
    frame = frame[0:320,100:500]
    copyframe = frame.copy()
    fgmask = bgModel.apply(frame,learningRate = 0.00001)
    kernel = np.ones((7, 7), np.uint8)
    fgmask = cv2.erode(fgmask,kernel,iterations = 1)
    
    
    res = cv2.bitwise_and(frame,frame, mask=fgmask)
    
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    
    retval , thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    thresh = cv2.medianBlur(thresh,5)
    
    
    _,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if contours != []:    
        # Maximum countour area
        maxArea = 0
        ind = 0
        for i in range(len(contours)):
            if cv2.contourArea(contours[i])>maxArea:
                maxArea = cv2.contourArea(contours[i])
                ind = i
        cnt = contours[ind][:]
    
        # Convexity Defects
        hull = cv2.convexHull(cnt, returnPoints = False)
        defects = cv2.convexityDefects(cnt,hull)
    
        if type(defects) != type(None):
            count = 0
            bool = False
            for i in range(defects.shape[0]):
            
                s,e,f,_ = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    bool = True
                    if count == 0 :
                        cv2.circle(frame, start, 5, [0, 0, 255], -1)
                        cv2.circle(frame, end, 5, [0, 0, 255], -1)
                        count += 2
                    else:
                        cv2.circle(frame, end, 5, [0, 0, 255], -1)
                        count += 1
            #treat the case of a finger tip/no fingers
            if bool == False:
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                centroid = (cx,cy)
                
            
                topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
                #print(topmost)
            
                a = math.sqrt((centroid[0] - topmost[0]) ** 2 + (centroid[1] - topmost[1]) ** 2)
                if a>100:
                    cv2.circle(frame, topmost, 5, [0, 0, 255], -1)
                    count += 1
            #printing the number of fingers        
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,str(count),(340,100), font, 2,(0,0,255),3,cv2.LINE_AA)
            #printing th cumulative int string
            #k += 1
            #if k%20 == 0:
                #if str(count) != ch[len(ch)-1]:
                    #ch = ch + str(count)
                    
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(frame,ch,(10,50), font, 2,(0,0,255),2,cv2.LINE_AA)
        
        # Convex hull
        hull = cv2.convexHull(cnt)
    
        # Drawing
        cv2.drawContours(frame,[hull],0,(155,155,0),2)
        cv2.drawContours(frame, [cnt],0, (0,255,0),2)

    cv2.imshow("frame",frame)
    cv2.imshow("copyframe",copyframe)
    cv2.imshow("gray",gray)
    cv2.imshow("fgmask",res)
    cv2.imshow("thresh",thresh)
    
## Keyboard command

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("1.jpg",frame)

    if cv2.waitKey(1) & 0xFF==27:
        break
 



cap.release()
cv2.destroyAllWindows()
