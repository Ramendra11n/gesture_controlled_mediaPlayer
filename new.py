import cv2;
import numpy as np;
def nothing(x):
 pass;

def createtb():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("lower1","thresholding",0,255,nothing) 
    cv2.createTrackbar("lower2","thresholding",0,255,nothing) 
    cv2.createTrackbar("lower3","thresholding",0,255,nothing) 
    cv2.createTrackbar("upper1","thresholding",0,255,nothing) 
    cv2.createTrackbar("upper2","thresholding",0,255,nothing) 
    cv2.createTrackbar("upper3","thresholding",0,255,nothing) 
img =cv2.imread('./drive-download-20221105T090638Z-001/hand.jpg');
cv2.imshow("image",img);
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
cv2.imshow("gray scale",gray);
_,thresh_img=cv2.threshold(gray,127,255,cv2.THRESH_BINARY);
cv2.imshow("gray scale1",thresh_img);
createtb();
while True:
    a=cv2.getTrackbarPos("lower1","thresholding")
    b=cv2.getTrackbarPos("lower2","thresholding")
    c=cv2.getTrackbarPos("lower3","thresholding")
    d=cv2.getTrackbarPos("upper1","thresholding")
    e=cv2.getTrackbarPos("upper2","thresholding")
    f=cv2.getTrackbarPos("upper3","thresholding")
    
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#converting the image from brg to hsv
    lower=np.array([a,b,c]);
    upper=np.array([d,e,f])
    # print(a,b,c,d,e,f)
    img_cp=img.copy();
    thresh=cv2.inRange(img_hsv,lower,upper);
    # the lower function is used to give the  lower limit of the value and the higher value gives the upper limit of the thresholding
    # _,thresh_img=_,thresh_img=cv2.threshold(gray,T,255,cv2.THRESH_BINARY);
    cv2.imshow("gray_controlled",thresh)
    contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);
    # the chain approx simple method is basically used for the joining of two points that have been detected this basically form the line between those two points 
    # whereas the chain_approx_none dont form the lines between the two very close points 
    #retr_external is basically used for the selection of only external contours
    # the first parameter is used for the image loaction,second for the selection of contours and third for the selection of the chain method 
    cv2.drawContours(img_cp,contours,0,(255,0,0),2)
    #first parameter image location
    # second parameter contours
    # selection of the complete contours(-1 ) selects every contour,
    # the fourth paremeter gives the color of the contour line
    # the 5th parameter gives the thickness of the contours .
    cv2.imshow("contouring",img_cp)
    key=cv2.waitKey(1);
 
    if(key==ord('q')):
        break;
    

# cv2.waitKey(0);