from playsound import playsound
import datefinder
import threading
from win10toast import ToastNotifier
import time
import os
import pyttsx3


l = ToastNotifier()
# quer = open('timer.txt', 'r')
# query = quer.read()
# quer.close()


def timer(query):
    ttime = datefinder.find_dates(query)
    for m in ttime:
        print(m)
    sting_al = str(m)
    tmiea = sting_al[11:]
    hour = tmiea[:-6]
    hour = int(hour)
    min = tmiea[3:-3]
    min = int(min)
    sec = tmiea[6:]
    sec = int(sec)
    l.show_toast("Timer", "Background timer is running.....")
    while True:
        if min != 0:
            if sec == 0:
                sec = 60
                min -= 1
        if hour != 0:
            if min == 0:
                min = 60
                hour -= 1
        elif hour == 0 and min == 0 and sec == 0:
            break
        os.system("cls")
        sec = sec - 1
        print(f"{hour}:{min}:{sec}")
        time.sleep(1)

    print("time up")
    playsound("alarm\\alarm.wav")


timer("set alarm for 5 seconds")
#os.remove('timer.txt')
engine = pyttsx3.init()
engine.say("time up")