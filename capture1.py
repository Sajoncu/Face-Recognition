import cv2
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

#Id = input('enter your id: ')
sampleNum = 1

while(True):
    if sampleNum >=150:
        break
    ret, img = cam.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = img
    faces = detector.detectMultiScale(gray, 1.5, 8)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        sampleNum = sampleNum+1
        
        cv2.imwrite("images/sajon/"+str(sampleNum)+".jpg",cv2.resize(gray[y:y+h,x:x+w],(300,300)))

        cv2.imshow('frame',img)

    if cv2.waitKey(100) & 0xFF == ord('q'):#waitKey is for delay in video capture
        break
    #elif sampleNum >= 150:#how many picture capture?
        #break

cam.release()
cv2.destroyAllWindows()
