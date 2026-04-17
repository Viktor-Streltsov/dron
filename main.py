import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("output.jpg", fourcc, 25.0, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    print('running')

    if ret:
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow('frame', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()