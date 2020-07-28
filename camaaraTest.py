import cv2
import numpy as np
import imutils
from imutils.video import VideoStream

#cap = cv2.VideoCapture(0)

resolution = (1024, 1024)
vs = VideoStream(src=0, resolution=resolution,
                         framerate=30).start()


while True:
    frame = vs.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (h, w) = frame.shape
    line_pice = w//16

    cv2.line(frame,(0,h//2),(w,h//2),(255,0,0),1)

    for i in range(1,16):
        cv2.line(frame,(line_pice*i,h//2-10),(line_pice*i,h//2+10),(0,255,0),1)
        color = frame[h//2+1,line_pice*i+1]
        #print(color ,end = '  ' )
        print_color = (255, 255, 255)
        if color > 150:
            print_color = (0,0,0)
            
        cv2.putText(frame,format(color), (line_pice*i-10, h//2+20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, print_color, 1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):  # press q to exit
        break

cv2.destroyAllWindows()
vs.stop()
