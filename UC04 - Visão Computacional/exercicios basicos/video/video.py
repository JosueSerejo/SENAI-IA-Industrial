import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ok, frame = cap.read()
    if not ok:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 100, 200)

    cv2.imshow("Edge", edge)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()