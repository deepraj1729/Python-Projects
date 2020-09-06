import cv2
import datetime

cap = cv2.VideoCapture(0)
ret , frame1 = cap.read()
ret , frame2 = cap.read()

count = 0
init_time = datetime.datetime.now()
print(init_time)
text = 'NONE'

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilate = cv2.dilate(thresh, None, iterations = 3)

    contours,_ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    for contour in contours:
        (x,y,w,h)= cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1000:
            continue
            
        else :
            text = 'Detected'
            count+=1

        cv2.rectangle( frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, 'Motion status: {}'.format(text), (10,20),font , 0.5, (0,0,255),1)
   
    #cv2.drawContours(frame1,contours, -1, (0,255,0),2)

    cv2.putText(frame1, datetime.datetime.now().strftime('%A %D %B %Y %I:%M:%S%p'),
        (10,frame1.shape[0]-10), font , 0.5,(0,0,255),1)

    cv2.imshow("Security Webcam",frame1)
    frame1 = frame2

    ret , frame2 = cap.read()

    key = cv2.waitKey(40) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        break

print("Count =  ",count)
final_time = datetime.datetime.now()
print(final_time) 

cv2.destroyAllWindows()
cap.release()
