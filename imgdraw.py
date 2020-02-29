import  cv2
#  importing  opencv  module
dogimg=cv2.imread('dog.jpg')
#  to draw a line
cv2.line(dogimg,(0,0),(200,200),(50,150,250),3)
cv2.rectangle(dogimg,(0,0),(200,200),(255,0,0),5)
cv2.circle(dogimg,(200,200),100,(0,255,0),-1)
#        img , first cord , last cord , color , width of line 

cv2.imshow('mydog',dogimg)
cv2.imshow('mydog1',dogimg-100)
cv2.waitKey(0)  #  0 means  inft 
