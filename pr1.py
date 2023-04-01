import cv2
import numpy as np


cap=cv2.VideoCapture(0) 

while True:
	ret, frame=cap.read()

	if ret:
		frame=cv2.flip(frame,1)
		
		frame2=255-frame
		gray1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		red=frame.copy()
		red[:,:,0]=0
		red[:,:,1]=0
		
		gray=cv2.merge([gray1,gray1,gray1])



		final1=cv2.hconcat([frame,red])
		final2=cv2.hconcat([frame2,gray])
		final3=cv2.vconcat([final1,final2])

		cv2.imshow('webcam',final3)


		q=cv2.waitKey(1)

		if q==ord('q'):
			break
cv2.destroyAllWindows()
cap.release()







 