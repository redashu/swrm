import  cv2
cam=cv2.VideoCapture('sw.avi')
#  load  first  camera


while  3  >  2 :
	status,frame=cam.read()
# status of camera  , frame 
	print(status)
	cv2.imshow('live',frame)
	cv2.waitKey(40)


