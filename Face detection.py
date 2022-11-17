#Face detection
import cv2


face_cascade = cv2.CascadeClassifier(r'C:\Users\Student\Pictures\AS_3421\cod.xml')
#incarcam imaginea 
img = cv2.imread(r'C:\Users\Student\Pictures\AS_3421\face.jpg')
#filtru gri 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#detectam fetele
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#desenam patratul in care se afla fata
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
