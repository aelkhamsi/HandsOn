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
    frame = cv2.line(frame,(40,40),(360,40),(0,0,255),3)
    frame = cv2.line(frame,(40,80),(360,80),(0,0,255),1)
    frame = cv2.line(frame,(40,120),(360,120),(0,0,255),1)
    frame = cv2.line(frame,(40,160),(360,160),(0,0,255),1)
    frame = cv2.line(frame,(40,200),(360,200),(0,0,255),3)
    frame = cv2.line(frame,(40,40),(40,200),(0,0,255),3)
    frame = cv2.line(frame,(80,40),(80,200),(0,0,255),1)
    frame = cv2.line(frame,(120,40),(120,200),(0,0,255),1)
    frame = cv2.line(frame,(160,40),(160,160),(0,0,255),1)
    frame = cv2.line(frame,(200,40),(200,200),(0,0,255),1)
    frame = cv2.line(frame,(240,40),(240,160),(0,0,255),1)
    frame = cv2.line(frame,(280,40),(280,200),(0,0,255),1)
    frame = cv2.line(frame,(320,40),(320,160),(0,0,255),1)
    frame = cv2.line(frame,(360,40),(360,200),(0,0,255),3)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'A',(50,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'B',(90,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'C',(130,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'D',(170,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'E',(210,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'F',(250,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'G',(290,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'H',(330,70), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    cv2.putText(frame,'I',(50,110), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'J',(90,110), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'K',(130,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'L',(170,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'M',(210,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'N',(250,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'O',(290,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'P',(330,110),font, 1,(255,255,255),2,cv2.LINE_AA)
    
    cv2.putText(frame,'Q',(50,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'R',(90,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'S',(130,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'T',(170,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'U',(210,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'V',(250,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'W',(290,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'X',(330,150), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    cv2.putText(frame,'Y',(50,190), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'Z',(90,190), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'ESC',(130,190), font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,'SUP',(210,190), font, 1,(100,100,255),2,cv2.LINE_AA)
    cv2.putText(frame,'OK',(290,190), font, 1,(10,200,10),2,cv2.LINE_AA)
    
    
    
    
    
## Track fingertip    
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
        
        # Topmost    
        topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
        cv2.circle(frame, topmost, 5, [255, 0, 0], -1)
        ty = topmost[0]
        tx = topmost[1]
        
        # Tracking
            #row1
        if tx>40 and tx<80 and ty>40 and ty<80: 
            if ch[-1] != 'A':
                if a%20 == 0:
                    ch = ch + 'A'
                    cv2.rectangle(frame,(40,40),(80,80),(0,255,255),-1)
                a += 1
        elif tx>40 and tx<80 and ty>80 and ty<120:
            if ch[-1] != 'B':
                if b%20 == 0:
                    ch = ch + 'B'
                    cv2.rectangle(frame,(80,40),(120,80),(0,255,255),-1)
                b += 1
        elif tx>40 and tx<80 and ty>120 and ty<160:
            if ch[-1] != 'C':
                if c%20 == 0:
                    ch = ch + 'C'
                    cv2.rectangle(frame,(120,40),(160,80),(0,255,255),-1)
                c += 1
        elif tx>40 and tx<80 and ty>160 and ty<200:
            if ch[-1] != 'D':
                if d%20 == 0:
                    ch = ch + 'D'
                    cv2.rectangle(frame,(160,40),(200,80),(0,255,255),-1)
                d += 1
        elif tx>40 and tx<80 and ty>200 and ty<240:
            if ch[-1] != 'E':
                if e%20 == 0:
                    ch = ch + 'E'
                    cv2.rectangle(frame,(200,40),(240,80),(0,255,255),-1)
                e += 1
        elif tx>40 and tx<80 and ty>240 and ty<280:
            if ch[-1] != 'F':
                if f%20 == 0:
                    ch = ch + 'F'
                    cv2.rectangle(frame,(240,40),(280,80),(0,255,255),-1)
                    cv2.putText(frame,ch,(40,38), font, 1,(255,0,0),2,cv2.LINE_AA)
                    cv2.imwrite("1548.jpg",frame)
                f += 1
        elif tx>40 and tx<80 and ty>280 and ty<320:
            if ch[-1] != 'G':
                if g%20 == 0:
                    ch = ch + 'G'
                    cv2.rectangle(frame,(280,40),(320,80),(0,255,255),-1)
                g += 1
        elif tx>40 and tx<80 and ty>320 and ty<360:
            if ch[-1] != 'H':
                if h%20 == 0:
                    ch = ch + 'H'
                    cv2.rectangle(frame,(320,40),(360,80),(0,255,255),-1)
                h += 1
            
        
            #row2
        elif tx>80 and tx<120 and ty>40 and ty<80:
            if ch[-1] != 'I':
                if i%20 == 0:
                    ch = ch + 'I'
                    cv2.rectangle(frame,(40,80),(80,120),(0,255,255),-1)
                i += 1
        elif tx>80 and tx<120 and ty>80 and ty<120:
            if ch[-1] != 'J':
                if j%20 == 0:
                    ch = ch + 'J'
                    cv2.rectangle(frame,(80,80),(120,120),(0,255,255),-1)
                j += 1
        elif tx>80 and tx<120 and ty>120 and ty<160:
            if ch[-1] != 'K':
                if k%20 == 0:
                    ch = ch + 'K'
                    cv2.rectangle(frame,(120,80),(160,120),(0,255,255),-1)
                k += 1
        elif tx>80 and tx<120 and ty>160 and ty<200:
            if ch[-1] != 'L':
                if l%20 == 0:
                    ch = ch + 'L'
                    cv2.rectangle(frame,(160,80),(200,120),(0,255,255),-1)
                l += 1
        elif tx>80 and tx<120 and ty>200 and ty<240:
            if ch[-1] != 'M':
                if m%20 == 0:
                    ch = ch + 'M'
                    cv2.rectangle(frame,(200,80),(240,120),(0,255,255),-1)
                m += 1
        elif tx>80 and tx<120 and ty>240 and ty<280:
            if ch[-1] != 'N':
                if n%20 == 0:
                    ch = ch + 'N'
                    cv2.rectangle(frame,(240,80),(280,120),(0,255,255),-1)
                n += 1
        elif tx>80 and tx<120 and ty>280 and ty<320:
            if ch[-1] != 'O':
                if o%20 == 0:
                    ch = ch + 'O'
                    cv2.rectangle(frame,(280,80),(320,120),(0,255,255),-1)
                o += 1
        elif tx>80 and tx<120 and ty>320 and ty<360:
            if ch[-1] != 'P':
                if p%20 == 0:
                    ch = ch + 'P'
                    cv2.rectangle(frame,(320,80),(360,120),(0,255,255),-1)
                p += 1
            
          
            #row3
        elif tx>120 and tx<160 and ty>40 and ty<80:
            if ch[-1] != 'Q':
                if q%20 == 0:
                    ch = ch + 'Q'
                    cv2.rectangle(frame,(40,120),(80,160),(0,255,255),-1)
                q += 1
        elif tx>120 and tx<160 and ty>80 and ty<120:
            if ch[-1] != 'R':
                if r%20 == 0:
                    ch = ch + 'R'
                    cv2.rectangle(frame,(80,120),(120,160),(0,255,255),-1)
                r += 1
        elif tx>120 and tx<160 and ty>120 and ty<160:
            if ch[-1] != 'S':
                if s%20 == 0:
                    ch = ch + 'S'
                    cv2.rectangle(frame,(120,120),(160,160),(0,255,255),-1)
                s += 1
        elif tx>120 and tx<160 and ty>160 and ty<200:
            if ch[-1] != 'T':
                if t%20 == 0:
                    ch = ch + 'T'
                    cv2.rectangle(frame,(160,120),(200,160),(0,255,255),-1)
                t += 1
        elif tx>120 and tx<160 and ty>200 and ty<240:
            if ch[-1] != 'U':
                if u%20 == 0:
                    ch = ch + 'U'
                    cv2.rectangle(frame,(200,120),(240,160),(0,255,255),-1)
                u += 1
        elif tx>120 and tx<160 and ty>240 and ty<280:
            if ch[-1] != 'V':
                if v%20 == 0:
                    ch = ch + 'V'
                    cv2.rectangle(frame,(240,120),(280,160),(0,255,255),-1)
                v += 1
        elif tx>120 and tx<160 and ty>280 and ty<320:
            if ch[-1] != 'W':
                if w%20 == 0:
                    ch = ch + 'W'
                    cv2.rectangle(frame,(280,120),(320,160),(0,255,255),-1)
                w += 1
        elif tx>120 and tx<160 and ty>320 and ty<360:
            if ch[-1] != 'X':
                if x%20 == 0:
                    ch = ch + 'X'
                    cv2.rectangle(frame,(320,120),(360,160),(0,255,255),-1)
                x += 1
            
        
            #row4
        elif tx>160 and tx<200 and ty>40 and ty<80:
            if ch[-1] != 'Y':
                if y%20 == 0:
                    ch = ch + 'Y'
                    cv2.rectangle(frame,(40,160),(80,200),(0,255,255),-1)
                y += 1
        elif tx>160 and tx<200 and ty>80 and ty<120:
            if ch[-1] != 'Z':
                if z%20 == 0:
                    ch = ch + 'Z'
                    cv2.rectangle(frame,(80,160),(120,200),(0,255,255),-1)
                z += 1
        elif tx>160 and tx<200 and ty>120 and ty<200:
            if ch[-1] != ' ':
                if esc%20 == 0:
                    ch = ch + ' '
                    cv2.rectangle(frame,(120,160),(200,200),(0,255,255),-1)
                esc += 1
        elif tx>160 and tx<200 and ty>200 and ty<280:#
            if sup%20 == 0:
                ch = ch[0:len(ch)-1]
                cv2.rectangle(frame,(200,160),(280,200),(0,255,255),-1)
            sup += 1
        elif tx>160 and tx<200 and ty>280 and ty<360:
            if ok%20 == 0:
                print(ch)
                ch = ' '
                cv2.rectangle(frame,(280,160),(360,200),(0,255,255),-1)
            ok += 1
            
    font    
    # Writing
    cv2.putText(frame,ch,(40,38), font, 1,(255,0,0),2,cv2.LINE_AA)
    # Drawing
    cv2.drawContours(frame, [cnt],0, (0,255,0),2)

    cv2.imshow("frame",frame)
    
    
    cv2.imshow("gray",gray)
    cv2.imshow("fgmask",fgmask)
    cv2.imshow("thresh",thresh)


    if cv2.waitKey(1) & 0xFF==27:
        break
 


cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
