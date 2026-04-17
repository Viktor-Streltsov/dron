import cv2

cap = cv2.VideoCapture('video.mp4')

print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        # cv2.imshow("frame", frame)

        if cv2 .waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print("error")
        break

cap.release()
cv2.destroyAllWindows()