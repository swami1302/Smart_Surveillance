import cv2,imutils
import time

cap = cv2.VideoCapture('D:\python\people_detection\in.avi')


human_cascade = cv2.CascadeClassifier('D:\python\people_detection\\2_casscadeAlgo\haarcascade_fullbody.xml')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=800)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray,1.9,1)
    c=1
    # Display the resulting frame
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(139, 34, 104), 2)
         '''cv2.rectangle(frame, (x, y - 20), (w,y), (139, 34, 104), -1)
         cv2.putText(frame, f'P{c}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)'''
         c += 1
         
         
    cv2.putText(frame, f'Total Persons : {c - 1}', (20, 500), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255,255), 2)
    cv2.imshow('frame',frame)
    time.sleep(0.05)
    key=cv2.waitKey(1)
    if key==81 or key==113: #--> Q or q ASCII value is 113 or 81
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()