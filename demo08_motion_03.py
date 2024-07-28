
import cv2
import datetime

camera = cv2.VideoCapture(0)
background = None
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

while True:
    grabbed, frame = camera.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 灰度图像
    gray_frame = cv2.GaussianBlur(gray_frame, (25, 25), 3)

    if background is None:
        background = gray_frame
        continue

    diff = cv2.absdiff(background, gray_frame)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[0]
    diff = cv2.dilate(diff, es, iterations=2)

    cv2.putText(frame,"Motion: Undetected", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('video', frame)
    cv2.imshow('diff', gray_frame)

    key = cv2.waitKey(1) & 0xFFf
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()