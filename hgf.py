import datefinder
import datetime
import playsound
import cv2
from win10toast import ToastNotifier
import os

l = ToastNotifier()
ol = open('alarm.txt', 'r')
lol = ol.read()
ol.close()
def alarm(lol):
    dtime = datefinder.find_dates(lol)
    for mat in dtime:
        print(mat)
    sting_al = str(mat)
    tmiea = sting_al[11:]
    hour = tmiea[:-6]
    hour = int(hour)
    min = tmiea[3:-3]
    min = int(min)
    if tmiea == datetime.datetime.now():
        l.show_toast("Alarm", "It's time.....")
    while True:
        if hour == datetime.datetime.now().hour:
            if min == datetime.datetime.now().minute:
               # playsound("alaram\\nimda.mp3")
                if min < datetime.datetime.now().minute:
                    break
        if cv2.waitKey(1) == ord('q'):
            break


alarm(lol)
os.remove('alarm.txt')