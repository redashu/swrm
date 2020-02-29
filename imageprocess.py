import  cv2
#  importing  opencv  module
dogimg=cv2.imread('dog.jpg')
#dogimg1=cv2.imread('dog.jpg',0)
#       here  0 means  BW  ---  gray image 
#  reading  image file and convert into  BGR 
print(dogimg)
#  will print numpy  array of image
print(dogimg.shape)
#  shape of image that is rows and cols 
print(type(dogimg))
#  will print type of data 
cv2.imshow('mydog',dogimg)
cv2.imshow('dogface',dogimg[0:200,100:450])
#cv2.imshow('graydog',dogimg1)
cv2.waitKey(0)  #  0 means  inft 
