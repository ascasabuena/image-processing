import cv2
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('GillClassifier.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)
    cv2.imshow('preview',frame)
    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()