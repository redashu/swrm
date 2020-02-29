import  cv2
cam=cv2.VideoCapture(0)
#  load  first  camera
facedataload=cv2.CascadeClassifier('face.xml')
#  loading  face data

while  3  >  2 :
	status,frame=cam.read()
# status of camera  , frame 
	face=facedataload.detectMultiScale(frame)
	print(status)
	print(face)
	for (x,y,h,w) in  face:

		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
	cv2.imshow('live',frame)
	cv2.waitKey(40)


