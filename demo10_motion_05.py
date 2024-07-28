
import cv2
import datetime

from demo05_wx_notice_01 import wxTool
from settings import app_id, app_secret


camera = cv2.VideoCapture(0)
background = None
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
is_send_msg = False

while True:
    grabbed, frame = camera.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 灰度图像
    gray_frame = cv2.GaussianBlur(gray_frame, (25, 25), 3)

    if background is None:
        background = gray_frame
        continue

    diff = cv2.absdiff(background, gray_frame)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.dilate(diff, es, iterations=2)

    contours, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    is_detect = False
    for c in contours:
        if cv2.contourArea(c) < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        is_detect = True
        if not is_send_msg:
            is_send_msg = True
            wxTool = wxTool(app_id, app_secret)
            wxTool.post_data('oyptN63RmNTWDkqwsU-0X11GT748')



    if is_detect:
        show_text = 'Notion: Detected'
        show_color = (0, 0, 255)
    else:
        show_text = 'Notion: Not Detected'
        show_color = (0, 255, 0)

    cv2.putText(frame, show_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, show_color, 1)

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, show_color, 1)

    cv2.imshow('video', frame)
    cv2.imshow('diff', gray_frame)

    key = cv2.waitKey(1) & 0xFFf
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()