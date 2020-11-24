import cv2
import numpy as np 

draw = False # true if the mouse is pressed. Press m to shift into curve mode.  
mode = True # if True, draw rectangle.  
p,q = -1,-1 
a=0
b=0
c=255

# mouse callback function  

def draw_circle(event,x,y,flags,param):  
    global p,q,draw,mode  
    if(event == cv2.EVENT_LBUTTONDOWN):  
        draw = True  
        p,q = x,y  
    elif (event == cv2.EVENT_MOUSEMOVE):  
        if draw == True:  
            if mode == True:  
                cv2.rectangle(img,(p,q),(x,y),(a,b,c),-1)
            else:  
                cv2.circle(img,(x,y),15,(90,155),-1)  
    elif(event == cv2.EVENT_LBUTTONUP):  
        draw = False  
        if mode == True:  
            cv2.rectangle(img,(p,q),(x,y),(a,b,c),-1) 
             
        else:  
            cv2.circle(img,(x,y),15,(100,25,255),-1) 

# We bind the keyboard key "m" to toggle between rectangle and circle.  

img = np.zeros((1000,1500,3), np.uint8)  
cv2.namedWindow('image')  
cv2.setMouseCallback('image',draw_circle)
print("Enter m to switch between rectangle drawing or curves")  
print("Press q to quit")
while(1):  
    cv2.imshow('image',img)
    a=a+25
    b=b+35
    c=c-25  
    #cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key &
    #0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255
    k = cv2.waitKey(1) & 0xFF  
    
    if k == ord('m'):  # ord('m') returns the Unicode code point of m     i.e., ASCII value
        mode = not mode

    elif(k == ord('q')):  
        break 

cv2.destroyAllWindows() 