from logging import exception
import cv2
import time

video = cv2.VideoCapture(#video_path)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while video.isOpened():
    ret , frame = video.read()


    if ret == False:
        print("Video Acilamadi")

    else:
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, (1360,720)) # ekran çok büyüktü biraz küçülttüm
        rect , humans = hog.detectMultiScale(resize,   padding=(1,1), scale=1.09)
        for (x,y,w,h) in rect:
            cv2.rectangle(resize ,(x,y),(x+w , y+h), (255,255,255), 1)
            cv2.putText(resize, "Hello", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        cv2.imshow("deneme" ,resize)

    if cv2.waitKey(1) & 0xFF == ord("q"):break

video.release()
cv2.destroyAllWindows()




