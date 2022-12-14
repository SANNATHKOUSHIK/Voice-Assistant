import cv2
import mediapipe as mp
import time
from module import handdetector
import numpy as np
import pyautogui
import math

wscreen, hscreen = pyautogui.size()
cam = cv2.VideoCapture(0)
wcam, hcam = 640, 480
clx, cly = 0, 0
plx, ply = 0, 0
current_time = 0
ptime = 0
detector = handdetector(detectioncon=0.75)
value = 100

while True:
    ret, frame = cam.read()
    frame = detector.findhands(frame)
    current_time = time.time()
    corlist = detector.findcordinates(frame)
    if len(corlist) != 0:
        x1, y1 = corlist[8][1:]
        x2, y2 = corlist[4][1:]
        X, Y = corlist[12][1:]
        status = detector.fingerstatus(frame)
        cv2.rectangle(frame, (value, value), (wcam - value, hcam - value), (0, 0, 0), 2)

        if status[1] == 1 and status[0] == 1:
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cX , cY = (x2 + X)//2, (y2 + Y)//2
            x3 = np.interp(cx, (value, wcam - value), (0, wscreen))
            y3 = np.interp(cy, (value, hcam - value), (0, hscreen))
            clx = plx + (x3-plx)/2
            cly = ply + (y3-ply)/2
            pyautogui.moveTo(wscreen - clx, cly)
            cv2.circle(frame, (x1, y1), 7, (0, 0, 0), cv2.FILLED)
            plx, ply = clx, cly
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.circle(frame, (x2, y2), 7, (0, 0, 0), cv2.FILLED)
            cv2.circle(frame, (cx, cy), 7, (0, 0, 0), cv2.FILLED)
            # cv2.circle(frame, (X, Y), 7, (0, 0, 0), cv2.FILLED)
            # cv2.line(frame, (X, Y), (x2, y2),(0,0,0), 2)
            # cv2.circle(frame, (cX, cY), 7, (0, 0, 0), cv2.FILLED)
            # length2 = math.hypot(X-x2, Y-y2)
            length = math.hypot(x2-x1, y2-y1)
            if int(length) < 40:
                pyautogui.leftClick()
                pyautogui.leftClick()

    # fps = 1 / (current_time - ptime)
    # ptime = current_time
    #
    # cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
