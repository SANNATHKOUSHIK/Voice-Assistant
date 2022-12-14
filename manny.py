import datetime
import multiprocessing
import os
import random
import smtplib
import socket
import threading
import time
# from newsapi import NewsApiClient
import tkinter as tk
import webbrowser
from tkinter import filedialog
import cv2
import datefinder
import matplotlib.pyplot as plt
import moviepy.editor
import numpy as np
import pyautogui
import pyttsx3
import randfacts
import requests
import sounddevice as sd
import speech_recognition as sr
import wikipedia
from PIL import ImageGrab
# from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
from google_trans_new import google_translator
from playsound import playsound
from pyjokes import pyjokes
from pynput.keyboard import Controller
from scipy.io.wavfile import write
from win10toast import ToastNotifier
import win32api
import win32file

addr = os.environ['username']
gt = google_translator()
sol = ["meme\\boss.mp3", "meme\\chu chu chu.mp3", "meme\\ri.mp3", "meme\\coffin.mp3", "meme\\lala.mp3", "meme\\omg.mp3",
       "meme\\final.mp3"]
l = ToastNotifier()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
engine.setProperty('voice', voices[0].id)
songs = []
mp4_files = []
drive_list = []
pathscr = []

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if os.path.exists(f"{letter}:"):
        pathscr.append(f'{letter}:')


def usb():
    while True:
        logical_drives = win32api.GetLogicalDriveStrings()
        logical_drives = logical_drives.split('\x00')[0:-1]
        for drive in logical_drives:
            if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:
                drive_list.append([drive, win32api.GetVolumeInformation(drive)[0],
                                   (win32api.GetVolumeInformation(drive)[3] / 2) // 1024])


def songssearch():
    for drive in pathscr:
        for root, dir, files in os.walk(drive):
            for file in files:
                if file.endswith(".mp3") or file.endswith(".wav"):
                    directories = os.path.join(root, file)
                    songs.append(directories)


def detect_mp4():
    for drive in pathscr:
        for root, dir, files in os.walk(drive):
            for file in files:
                if file.endswith(".mp4"):
                    directories = os.path.join(root, file)
                    mp4_files.append(directories)


def screenrecord():
    filename = "output" + str(time.time()) + ".avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    filename_source = f"C:\\Users\\{addr}\\Pictures\\screen recorder\\" + filename + ""
    out = cv2.VideoWriter(filename_source, fourcc, 10.0, (1920, 1080))
    time.sleep(3)
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if cv2.waitKey(10) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()


def birthday():
    q = datetime.datetime.now().strftime("%d %m")
    if q == '10 05':
        speak("happy  birthday  sir")


def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    ch = datetime.datetime.now().strftime('%d %m')
    N = datetime.datetime.now().strftime("%d %m")
    if 0 <= hour < 12:
        speak('good morning sir')
    elif 12 <= hour < 16:
        speak('good afternoon sir')
    elif ch == '25 12':
        speak("happy  christmas  sir")
    elif N == '01 01':
        speak("happy  NewYear  sir")
    else:
        speak('good evening sir')
    speak('i am OPTIMUS, your personal assisstant')


def sendemail(To, Content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('sannathkoushik@gmail.com', 'tomandjerry2020')
    server.sendmail('sannathkoushik@gmail.com', To, Content)
    server.close()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        Audio = r.listen(source)
        try:
            print('recognizing...')
            Query = r.recognize_google(Audio, language='en')
            print(f"user said: {Query}\n")

        except sr.UnknownValueError:
            p = ["i am  sorry", "come  again", "say  that  again", "sorry!!"]
            speak(random.choice(p))
            return "none"
        except sr.RequestError:
            speak("sorry,  my  speech  service  is  down")
        return Query


def remember(query):
    rmember = query.replace('remember me', " ")
    speak("okay......")
    wir = open('data.txt', 'w')
    wir.write(rmember)
    wir.close()
    time.sleep(3600)
    remember_msg = open('data.txt', 'r')
    remember_msg1 = remember_msg.read()
    speak(f"sir you ask me to remember that {remember_msg1}")


def takecommand2():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print('Listening....')
        r.pause_threshold = 1
        Audio = r.listen(source)
        try:
            print('recognizing...')
            Euery = r.recognize_google(Audio, language='en-in')
            print(f"user said: {Euery}\n")
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        return Euery


def facts():
    while True:
        time.sleep(300)
        Lr = randfacts.getFact()
        g = "Do you know?" + Lr
        print(g)
        speak(Lr)


def stopwatch():
    sec = float(0)
    min = int(0)
    hour = int(0)
    l.show_toast("Stopwatch", "Stopwatch is running in background.....")
    speak("starting....")
    while True:
        if sec > 59:
            sec = 0
            min = min + 1
        if min > 59:
            min = 0
            hour = hour + 1
        os.system("cls")
        sec = sec + 1
        print(hour, ":", min, ":", sec)
        time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def functions():
    # condition = True
    # if hotword == 'optimus':
    #     condition = True
    # else:
    #     condition = False
    ddd = []
    Query_list = []
    global m, songs, frame, query
    while True:
        query = takecommand().lower()
        if len(drive_list) > len(ddd):
            speak("usb device connected")
            for drive in drive_list:
                ddd.append(drive)

        elif len(drive_list) < len(ddd):
            speak("usb device disconnected")
            ddd.remove(ddd[-1])

        if len(Query_list) == 0:
            query = takecommand().lower()
        elif len(Query_list) != 0:
            query = Query_list[0]
            Query_list = []

        if query == 'wikipedia' or query == 'what is' or query == 'who':
            try:
                speak('searching wikipedia....')
                query = query.replace("wikipedia", " ")
                webbrowser.open(query)
                results = wikipedia.summary(query, sentences=3)
                speak('according to wikipedia......')
                speak(results)
            except Exception as e:
                speak("i am sorry , no results found in wikipedia!!!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open ocean of games' in query:
            webbrowser.open("oceanofgames.com")

        elif 'open getintopc' in query:
            webbrowser.open("getintopc.com")

        elif 'open fitgirlrepack' in query:
            webbrowser.open("fitgirlrepack.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open myntra' in query:
            webbrowser.open("Myntra.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open zee5' in query:
            webbrowser.open("Zee5.com")

        elif 'open aha' in query:
            webbrowser.open("aha.com")

        elif 'play music' in query:
            song = random.choice(songs)
            print(song)
            os.startfile(song)

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%I %M %p").lstrip('0')
            speak(strtime)

        elif 'open pycharm' in query:
            try:
                os.system("start pycharm64.exe")
                os.system("start pycharm32.exe")
            except:
                speak("i am sorry, i can't open it.")

        elif 'screenshot' in query:
            v = ["done", "got it", "okay", "what next"]
            pyautogui.hotkey("win", "alt", "fn", "prntscrn")
            speak(v[random.randrange(0, 4)])

        elif 'record screen' in query:
            speak("recording started")
            lolo = multiprocessing.Process(target=screenrecord)
            lolo.start()

        elif 'father' in query:
            f = ["i am ai,how can i have a father ? ", "i am ai!", "what the fu..???",
                 "why the hell all of you ask this stupid question", "Sannath Koushik"]
            speak(random.choice(f))

        elif 'mother' in query:
            speak("My father told  me to not answer this question")

        elif 'favourite color' in query:
            speak("i love rainbow")

        elif 'favourite food' in query:
            speak("even i am an ai, i love food  recipes of humans")

        elif 'hello' in query:
            h = ["hi, how are you?", "hi, how do you do?"]
            speak(random.choice(h))

        elif 'hi ' in query:
            speak("Hello")

        elif 'i am' in query:
            ee = query.replace("i am", "")
            speak("hello" + ee)

        elif 'my name is' in query:
            sp = query.replace("my name is", "")
            speak("hello" + sp + "my name is optimus....")

        elif 'what do you do' in query:
            speak("i am a AI, my job is to serve human")

        elif 'sing a song' in query:
            speak("i am sorry,i am not too good at singing, instead i can play some music for you")
            time.sleep(0.5)
            speak("shall  i ?")
            tyu = takecommand()
            if tyu == 'yes' or tyu == 'why not' or tyu == 'go ahead':
                music_dir = f'C:\\Users\\{addr}\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[random.randrange(0, 13)]))
            else:
                speak("okay...")

        elif 'how are you' in query:
            a = ["i am good", "fine"]
            speak(random.choice(a))

        elif 'thank you' in query:
            playsound("meme\\You're Welcome.mp3")

        elif 'how do you do' in query:
            speak("good")

        elif 'f*** you' in query:
            f = ["fucker", "baster", "idiot", "suker"]
            speak(f"you can't..{random.choice(f)}")

        elif 'god' in query:
            speak("python")

        elif 'a******' in query:
            q = ["i don't have ass", "i am an AI, i think your fuck'n eyes are not working, better consult a doctor",
                 "you are a asshole"]
            speak(random.choice(q))

        elif 'your age' in query:
            speak("it's too confidential")

        elif 'game' in query:
            speak("all game of Rockstargames and all editions of call of duty")

        elif 'girlfriends' in query:
            g = ["no girl friends...", "i don't have any girl friends",
                 "I don't want to get that shit on my head"]
            speak(random.choice(g))

        elif 'where do you born' in query:
            speak("India , Andhra Pradesh , Vizianagaram")

        elif 'sun rises' in query:
            speak("east")

        elif ' sun sets' in query:
            speak("west")

        elif 'your name' in query:
            speak("optimus")

        elif 'extract' in query:
            rot = tk.Tk()
            rot.withdraw()
            file_pa = filedialog.askopenfilename()
            video = moviepy.editor.VideoFileClip(file_pa)
            audio = video.audio
            audio.write_audiofile("output" + str(time.time()) + '.mp3')
            speak("done")

        elif 'record' in query:
            fs = 44100
            s = 10000
            dst = "output" + str(time.time()) + ".wav"
            print("Recording......")
            record_voice = sd.rec(int(s * fs), samplerate=fs, channels=2)
            sd.wait()
            write(dst, fs, record_voice)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        elif 'photo' in query:
            cam = cv2.VideoCapture(0)
            if cam.isOpened():
                ret, frame = cam.read()
            else:
                ret = False
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.title("photo")
            plt.xticks([])
            plt.yticks([])
            plt.show()
            cam.release()

        elif 'make a video' in query:
            pass

        elif 'weather' in query:
            url = "https://www.google.com/search?q=" + query
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe tAd8D AP7Wnd")
            weather = temp.split('\n')
            speak(weather[1])

        elif 'temperature' in query:
            url = "https://www.google.com/search?q=" + query
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe")
            speak(f"temperature is {temp}")

        elif 'humidity' in query:
            pass

        elif 'the date' in query:
            str_date = datetime.datetime.now().strftime("%d %B").lstrip('0')
            speak(str_date)

        elif "year" in query:
            str_yera = datetime.datetime.now().strftime("%Y")
            speak(str_yera)

        elif 'search' in query:
            speak("searching...")
            url = 'https://google.co.in/search?q='
            search = url + query.lstrip('search')
            webbrowser.open(search)

        elif 'youtube' in query:
            you = 'https://www.youtube.com/results?search_query='
            nim = you + query.lstrip('youtube')
            webbrowser.open(nim)

        elif 'send email' in query:
            speak("security code required !")
            em = takecommand()
            i = 1
            while i < 4:
                i = i + 1
                if em == '1034 4301':
                    speak("Access Granted")
                    try:
                        speak("what should i send")
                        content = takecommand()
                        to = pyautogui.prompt("Enter reciever's Email", "E-mail")
                        (sendemail(to, content))
                        speak("email sent...")
                        break
                    except Exception as e:
                        print(e)
                        speak("sorry, I am not able to send this email")
                        break
                else:
                    speak("invalid security code!")

        elif 'amazon' in query:
            amazon = 'https://www.amazon.in/s?k='
            am = amazon + query.lstrip('amazon')
            webbrowser.open(am)

        elif 'flipkart' in query:
            flipkart = 'https://www.flipkart.com/search?q='
            flip = flipkart + query.lstrip('flipkart')
            webbrowser.open(flip)

        elif 'Myntra' in query:
            myntra = 'https://www.myntra.com/'
            my = myntra + query.lstrip('Myntra')
            webbrowser.open(my)

        elif 'bye' in query:
            z = ["see you again", "i'll catch you later", "bye"]
            speak(random.choice(z))

        elif 'who are you' in query:
            speak("I am optimus, who are you?")

        elif query == 'quit' or query == 'exit':
            z = ["see you again", "i'll catch you later", "bye"]
            speak(random.choice(z))
            exit()

        elif query == 'shut down my pc' or query == 'shutdown' or query == 'good night' or query == 'its up for today' or query == 'power off':
            speak("waiting for conformation...")
            qwe = takecommand()
            if qwe == 'yes' or qwe == 'confirm':
                playsound("meme\\ss.mp3")
                os.system('shutdown /s /t 0')
            if qwe == 'no':
                speak("shutdown cancelled...")

        elif 'good night' in query:
            speak("sweet dreams")
            os.system("shutdown /s /t 0")

        elif query == 'restart my pc' or query == 'restart':
            speak("restarting...")
            os.system("shutdown /r /t 0")

        elif 'logoff pc' in query:
            speak("logging off...")
            os.system("shutdown /l")

        elif 'command prompt' in query:
            speak("opening....")
            os.system("start")

        elif 'best friend' in query:
            speak("no one!")

        elif 'good' in query:
            speak("thank you")

        elif 'good boy' in query:
            d = ["thank you", "i know that", "yes i am"]
            speak(random.choice(d))

        elif 'show screenshots' in query:
            speak("opening....")
            screenshots_path = f"C:\\Users\\{addr}\\Pictures\\screenshots"
            os.startfile(screenshots_path)

        elif 'show recordings' in query:
            speak("opening....")
            recording_path = f'C:\\Users\\{addr}\\voice recordings'
            os.startfile(recording_path)

        elif 'show screen recordings' in query:
            speak("opening....")
            screen_recordings_path = f'C:\\Users\\{addr}\\Pictures\\screen recorder'
            os.startfile(screen_recordings_path)

        elif 'show deleted files' in query:
            speak("opening....")
            os.system("start shell:RecycleBinFolder")

        elif 'open word' in query:
            speak("opening....")
            os.system("start winword")

        elif 'open powerpoint' in query:
            speak("opening....")
            os.system("start powerpnt")

        elif 'open excel' in query:
            speak("opening....")
            os.system("start excel")

        elif 'open notepad' in query:
            speak("opening....")
            os.system("start notepad")

        elif 'task manager' in query:
            speak("opening....")
            os.system("taskmgr")

        elif 'open temp files' in query:
            speak("opening....")
            os.system("start temp")
            os.system("start %temp%")
            os.system("start prefetch")

        elif 'show me your configuration' in query:
            config_path = "manny.py"
            os.startfile(config_path)

        elif 'meme' in query:
            playsound(random.choice(sol))

        elif 'control panel' in query:
            speak("opening....")
            os.system("control")

        elif query == 'firewall' in query:
            speak("opening....")
            os.system("firewall.cpl")

        elif 'fonts' in query:
            speak("opening....")
            os.system("conrol fonts")

        elif 'mouse settings' in query:
            speak("opening....")
            os.system("control mouse")

        elif 'keyboard settings' in query:
            speak("opening....")
            os.system("control keyboard")

        elif query == 'devices' or query == 'show devices' or query == 'show connected devices' or query == 'devices and printers':
            speak("opening....")
            os.system("control /name Microsoft.DevicesAndPrinters")

        elif query == 'network connections' or query == 'network details' or query == 'show network':
            speak("opening....")
            os.system("control netconnections")

        elif query == 'file explorer settings' or query == 'file explorer options':
            speak("opening....")
            os.system("control folders")

        elif query == 'show admintools' or query == 'show administrative tools':
            speak("opening....")
            os.system("control admintools")

        elif query == 'uninstall programs' or query == 'show apps' or query == 'show programs and features' or query == 'show programs':
            speak("opening....")
            os.system("appwiz.cpl")

        elif 'open device manager' in query:
            speak("opening....")
            os.system("hdwwiz.cpl")

        elif 'open display settings' in query:
            speak("opening....")
            os.system("desk.cpl")

        elif query == 'show internet properties' or query == 'show me internet properties':
            speak("opening....")
            os.system("inetcpl.cpl")

        elif query == 'show game controller' or query == 'game controller options' or query == 'joystick properties' or query == 'gamepad settings' or query == 'joystick settings':
            speak("opening....")
            os.system("joy.cpl")

        elif query == 'sound settings' or query == 'audio options' or query == 'open sound settings' or query == 'show multimedia properties':
            speak("opening....")
            os.system("mmsys.cpl")

        elif 'power options' in query:
            speak("opening....")
            os.system("powercfg.cpl")

        elif 'system properties' in query:
            speak("opening....")
            os.system("sysdm.cpl")

        elif query == 'security and maintenance' or query == 'open security settings' or query == 'security settings':
            speak("opening....")
            os.system("wscui.cpl")

        elif query == 'date time settings' or query == 'date time':
            speak("opening....")
            os.system("timedate.cpl")

        elif query == 'access centre':
            speak("opening....")
            os.system("control access.cpl")

        elif 'modem properties' in query:
            speak("opening....")
            os.system("control modem.cpl")

        elif 'backup and restore centre' in query:
            speak("opening....")
            os.system("control /name Microsoft.BackupAndRestore")

        elif query == 'default programs':
            speak("opening....")
            os.system("control /name Microsoft.DefaultPrograms")

        elif query == 'color management options' or query == 'color management settings':
            speak("opening....")
            os.system("control /name Microsoft.ColorManagement")

        elif 'open credential manager' in query:
            speak("opening....")
            os.system("control /name Microsoft.CredentialManager")

        elif 'file history' in query:
            speak("opening....")
            os.system("control /name Microsoft.FileHistory")

        elif 'indexing options' in query:
            speak("opening....")
            os.system("control /name Microsoft.IndexingOptions")

        elif 'language settings' in query:
            speak("opening....")
            os.system("control /name Microsoft.Language")

        elif 'network setup wizard' in query:
            speak("opening....")
            os.system("control netsetup.cpl")

        elif 'odbc data source administrator' in query:
            speak("opening....")
            os.system("control odbccp32.cpl")

        elif 'offline files' in query:
            speak("opening....")
            os.system("control /name Microsoft.OfflineFiles")

        elif 'personalization settings' in query:
            speak("opening....")
            os.system("control /name Microsoft.Personalization	control desktop")

        elif query == 'recovery options':
            speak("opening....")
            os.system("control /name Microsoft.Recovery")

        elif 'remote app and desktop connections' in query:
            speak("opening....")
            os.system("control /name Microsoft.RemoteAppAndDesktopConnections")

        elif 'task scheduler' in query:
            speak("opening....")
            os.system("control schedtasks")

        elif 'speech recognition options' in query:
            speak("opening....")
            os.system("control /name Microsoft.SpeechRecognitionOptions")

        elif 'storage space' in query:
            speak("opening....")
            os.system("control /name Microsoft.StorageSpaces")

        elif 'sync centre' in query:
            speak("opening....")
            os.system("control /name Microsoft.SyncCenter")

        elif query == 'system options' or query == 'system configuration':
            speak("opening....")
            os.system("control /name Microsoft.System")

        elif 'taskbar' in query:
            speak("opening....")
            os.system("control /name Microsoft.Taskbar")

        elif 'speech properties' in query:
            speak("opening....")
            os.system("control /name Microsoft.TextToSpeech")

        elif query == 'troubleshoot options' or query == 'troubleshoot settings':
            speak("opening....")
            os.system("control /name Microsoft.Troubleshooting")

        elif 'user accounts' in query:
            speak("opening....")
            os.system("control /name Microsoft.UserAccounts")

        elif query == 'windows update options' or query == 'windows update settings':
            speak("opening....")
            os.system("control /name Microsoft.WindowsUpdate")

        elif query == 'get out of my system' or query == 'get out of my pc' or query == 'get out of my computer':
            speak("okay sir,bye....,sorry........good.......bye....")
            quit()

        elif query == 'read this disc' or query == 'take this disc' or query == 'read this cd' or query == 'open cd rom' or query == 'take this cd':
            speak("okay..")
            os.system('powershell (New-Object -com "WMPlayer.OCX.7").cdromcollection.item(0).eject()')

        elif 'calculator' in query:
            speak("opening....")
            os.system("calc")

        elif 'meaning' in query:
            same = query.replace("what is the meaning of", "")
            wrd = PyDictionary(same)
            speak(wrd.getMeanings())

        elif 'antonyms' in query:
            ant = query.replace("what is the antonym of", "")
            wd = PyDictionary(ant)
            speak(wd.getAntonyms())

        elif 'synonym' in query:
            sys = query.replace("what is the synonym of", "")
            w = PyDictionary(sys)
            speak(w.getSynonyms())

        elif 'settings' in query:
            speak("opening....")
            os.system("start ms-settings:")

        elif 'open cortana settings' in query:
            speak("opening....")
            os.system("start ms-settings:cortana")

        elif 'pen and windows ink settings' in query:
            speak("opening....")
            os.system("start ms-settings:pen&windowsink")

        elif 'usb settings' in query:
            speak("opening....")
            os.system("start ms-settings:usb")

        elif 'autoplay settings' in query:
            speak("opening....")
            os.system("start ms-settings:autoplay")

        elif query == 'typing settings' or query == 'typing options':
            speak("opening....")
            os.system("start ms-settings:typing")

        elif 'default apps' in query:
            speak("opening....")
            os.system("start ms-settings:defaultapps")

        elif 'apps and features' in query:
            speak("opening....")
            os.system("start ms-settings:appsandfeatures")

        elif 'open chrome' in query:
            speak("opening....")
            os.system("start chrome")

        elif 'run prompt' in query:
            speak("opening....")
            pyautogui.hotkey("win", "r")

        elif 'file explorer' in query:
            speak("opening....")
            pyautogui.hotkey("win", "e")

        elif 'minimise' in query:
            pyautogui.hotkey("win", "down")

        elif 'miximise' in query:
            pyautogui.hotkey('win', 'up')

        elif 'desktop' in query:
            pyautogui.hotkey('win', 'm')

        elif 'clipboard' in query:
            pyautogui.hotkey('win', 'v')

        elif 'find computers' in query:
            speak("opening....")
            pyautogui.hotkey("win", "ctrlleft", "f")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'unmute' in query:
            pyautogui.press("volumemute")

        elif query == 'volume up' or query == 'increase volume':
            pyautogui.press("volumeup")

        elif query == 'volume down' or query == 'decrease volume':
            pyautogui.press("volumedown")

        elif 'registry editor' in query:
            speak("opening....")
            os.system("regedit")

        elif 'local group policy editor' in query:
            speak("opening....")
            os.system("gpedit.msc")

        elif 'bluetooth file transfer' in query:
            speak("opening....")
            os.system("fsquirt")

        elif 'certificate manager' in query:
            speak("opening....")
            os.system("certmgr.msc")

        elif 'character map' in query:
            speak("opening....")
            os.system("charmap")

        elif 'disk check' in query:
            speak("performing...")
            os.system("chkdsk")

        elif 'component services' in query:
            speak("opening....")
            os.system("dcomcnfg")

        elif 'computer manager' in query:
            speak("opening....")
            os.system("compmgmt.msc")

        elif 'directx diagnostic tool' in query:
            speak("opening....")
            os.system("dxdiag")

        elif 'disk cleanup' in query:
            os.system("cleanmgr")

        elif 'disk management' in query:
            speak("opening....")
            os.system("diskmgmt.msc")

        elif 'partition manager' in query:
            speak("opening....")
            os.system("diskpart")

        elif 'event viewer' in query:
            speak("opening....")
            os.system('eventvwr.msc')

        elif 'file signature verification' in query:
            speak("opening....")
            os.system("sigverif")

        elif 'i express wizard' in query:
            speak("opening....")
            os.system("iexpress")

        elif 'local security policy' in query:
            speak("opening....")
            os.system("start secpol.msc")

        elif 'performance monitor' in query:
            speak("opening....")
            os.system("perfmon")

        elif 'resource monitor' in query:
            speak("opening....")
            os.system("resmon")

        elif 'screen keyboard' in query:
            speak("opening....")
            os.system("osk")

        elif 'private character editor' in query:
            speak("opening....")
            os.system("start eudcetdit")

        elif 'resultant set of policy' in query:
            speak("opening....")
            os.system("rsop.msc")

        elif 'shared folders' in query:
            speak("opening....")
            os.system("fsmgmt.msc")

        elif 'sql server' in query:
            speak("opening....")
            os.system("cliconfg")

        elif 'magnifier' in query:
            speak("opening....")
            os.system("magnify")

        elif 'windows management' in query:
            speak("opening....")
            os.system("wmimgmt.msc")

        elif 'copy' in query:
            pyautogui.hotkey("ctrl", "c")
            speak("okay")

        elif 'paste' in query:
            pyautogui.hotkey("ctrl", "v")
            speak("done")

        elif 'paint' in query:
            speak("opening....")
            os.system("mspaint")

        elif 'malicious software removal tool' in query:
            speak("opening....")
            os.system('mrt')

        elif 'windows address book import utility' in query:
            speak("opening....")
            os.system("start wabmig")

        elif 'remote desktop' in query:
            speak("opening....")
            os.system("mstsc")

        elif 'remote access phonebook' in query:
            speak("opening....")
            os.system("rasphone")

        elif 'set alarm' in query:
            alarm_msg = open('alarm.txt', 'w')
            alarm_msg.write(query)
            alarm_msg.close()
            current_time = datetime.datetime.now().hour
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
            difference_in_time = hour - current_time
            if current_time > 17:
                if difference_in_time < 8:
                    speak(
                        f"sir there is only {difference_in_time} hours left for your alarm. Go to sleep.Humans should need minimum six hours sleep")

            def aaa():
                os.system("python hgf.py")

            ala = threading.Thread(target=aaa)
            ala.start()

        elif 'timer' in query:
            quer = open('timer.txt', 'w')
            quer.write(query)
            quer.close()

            def bbb():
                os.system("python timer.py")

            ala = threading.Thread(target=bbb)
            ala.start()

        elif 'stopwatch' in query:
            p5 = multiprocessing.Process(target=stopwatch)
            p5.start()

        elif 'ms store' in query:
            speak("opening....")
            os.system("start ms-windows-store:")

        elif 'paint 3D' in query:
            speak("opening....")
            os.system("start ms-paint:")

        elif query == 'open cortana' or query == 'call cortana':
            speak("opening....")
            os.system("start ms-cortana:")

        elif 'anydesk' in query:
            speak("opening....")
            os.system("start Anydesk:")

        elif 'outlook' in query:
            speak("opening....")
            os.system("start outlook")

        elif "what's the day" in query:
            speak(datetime.datetime.now().strftime("%A"))

        elif 'month' in query:
            speak(datetime.datetime.now().strftime("%B"))

        elif 'year' in query:
            speak(datetime.datetime.now().strftime("%Y"))

        elif 'pronounce' in query:
            queray = query.replace("pronounce", "")
            querqy = queray.replace(" ", "")
            speak(querqy)

        elif 'general settings' in query:
            speak("opening.....")
            os.system("start ms-settings:privacy-location")

        elif 'location settings' in query:
            speak("opening..")
            os.system("start ms-settings:privacy-location")

        elif 'camera settings' in query:
            speak("opening...")
            os.system("start ms-settings:privacy-webcam")

        elif 'microphone settings' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-microphone")

        elif 'phone' in query:
            speak("opening....")
            os.system("start ms-settings:mobile-devices")

        elif 'documents settings' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-documents")

        elif 'pictures settings' in query:
            speak("opening...")
            os.system("start ms-settings:privacy-pictures")

        elif 'videos settings' in query:
            speak("opening...")
            os.system("start ms-settings:privacy-videos")

        elif 'file system settings' in query:
            speak("opening...")
            os.system("start ms-settings:privacy-broadfilesystemaccess")

        elif 'automatic file download' in query:
            speak("opening.....")
            os.system("start ms-settings:privacy-automaticfiledownloads")

        elif 'app diagnostics' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-appdiagnostics")

        elif 'background apps' in query:
            speak("opening...")
            os.system("start ms-settings:privacy-backgroundapps")

        elif 'other devices' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-customdevices")

        elif 'radios' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-radios")

        elif 'messaging settings' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-messaging")

        elif 'tasks' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-tasks")

        elif query == 'email' or query == 'mail settings':
            speak("opening...")
            os.system("start ms-settings:privacy-email")

        elif 'call history' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-callhistory")

        elif 'calendar settings' in query:
            speak('opening....')
            os.system("start ms-settings:privacy-calendar")

        elif 'contacts' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-contacts")

        elif 'account info' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-accountinfo")

        elif 'notification' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-notifications")

        elif 'activity history' in query:
            speak("opening....")
            os.system("start 	ms-settings:privacy-activityhistory")

        elif 'feedback' in query:
            speak("opening....")
            os.system("start ms-settings:privacy-feedback")

        elif 'speech typing' in query:
            speak("opening....")
            os.system("start 	ms-settings:privacy-speechtyping")

        elif 'windows insider program' in query:
            speak("opening....")
            os.system("start ms-settings:windowsinsider")

        elif 'for developers' in query:
            speak("opening....")
            os.system("start ms-settings:developers")

        elif 'find my device' in query:
            speak("opening....")
            os.system("start ms-settings:findmydevice")

        elif 'windows activation' in query:
            speak("opening....")
            os.system("start ms-settings:activation")

        elif 'recovery settings' in query:
            speak("opening.....")
            os.system("start ms-settings:recovery")

        elif 'ease of access display' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-display")

        elif 'magnifier settings' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-magnifier")

        elif 'colour filters' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-colorfilter")

        elif 'eye control' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-eyegaze")

        elif 'closed captions' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-closedcaptioning")

        elif 'high contrast' in query:
            speak("opening....")
            os.system("start ms-settings:easeofaccess-highcontrast")

        elif 'game bar' in query:
            speak("opening....")
            os.system("start ms-settings:gaming-gamebar")

        elif 'captures' in query:
            speak("opening....")
            os.system("start ms-settings:gaming-gamedvr")

        elif 'broadcasting' in query:
            speak("opening....")
            os.system("start ms-settings:gaming-broadcasting")

        elif 'game mode' in query:
            speak("opening....")
            os.system("start ms-settings:gaming-gamemode")

        elif 'xbox networking' in query:
            speak("opening....")
            os.system("start ms-settings:gaming-xboxnetworking")

        elif query == 'your info' or query == 'my info':
            speak("opening....")
            os.system("start ms-settings:yourinfo")

        elif 'email and app accounts' in query:
            speak("opening....")
            os.system("start ms-settings:emailandaccounts")

        elif 'sign in options' in query:
            speak("opening....")
            os.system("start ms-settings:signinoptions")

        elif query == 'access work' or query == 'work place':
            speak("opening....")
            os.system("start ms-settings:workplace")

        elif 'family and other people' in query:
            speak("opening....")
            os.system("start ms-settings:otherusers")

        elif 'sync your settings' in query:
            speak("opening....")
            os.system("start ms-settings:sync")

        elif 'network status' in query:
            speak("opening....")
            os.system("start ms-settings:network-status")

        elif 'wifi' in query:
            speak("opening.....")
            os.system('start ms-settings:network-wifi')

        elif 'documents folder' in query:
            speak("opening...")
            os.system("explorer.exe/separate")

        elif 'this pc' in query:
            speak("opening....")
            os.system("explorer ,")

        elif 'tab' in query:
            pyautogui.hotkey("win", "tab")

        elif "powershell" in query:
            speak("which powershell do you want to open?")
            print('powershell'
                  'powershell ISE')
            speak('you can say by number,like the first or second')
            yiyuy = takecommand()
            if yiyuy == 'first' or yiyuy == '1' or yiyuy == 'powershell':
                speak("opening....")
                os.system("start powershell")
            else:
                speak("opening.....")
                os.system("start powershell ISE")

        elif 'windows defender' in query:
            speak("opening....")
            os.system("start ms-settings:windowsdefender")

        elif 'restart options' in query:
            speak("opening....")
            os.system("start ms-settings:windowsupdate-restartoptions")

        elif 'update history' in query:
            speak("opening....")
            os.system("start ms-settings:windowsupdate-history")

        elif 'backup settings' in query:
            speak("opening....")
            os.system("start ms-settings:backup")

        elif 'startup apps' in query:
            speak("opening....")
            os.system("start ms-settings:startupapps")

        elif 'apps for websites' in query:
            speak("opening....")
            os.system("start ms-settings:appsforwebsites")

        elif 'offline maps' in query:
            speak("opening....")
            os.system("start ms-settings:maps")

        elif 'video playback' in query:
            speak("opening....")
            os.system("start ms-settings:videoplayback")

        elif 'optional features' in query:
            speak("opening....")
            os.system("start ms-settings:optionalfeatures")

        elif 'windows features' in query:
            speak("opening....")
            os.system("start optional features")

        elif 'authorization manager' in query:
            speak("opening....")
            os.system("start azman.msc")

        elif 'camera' in query:
            speak("opening....")
            os.system("start microsoft.windows.camera:")

        elif 'groove' in query:
            speak("opening....")
            os.system("start mswindowsmusic:")

        elif '3d builder' in query:
            speak("opening....")
            os.system("start com.microsoft.builder3d:")

        elif query == 'action centre' or query == 'notifications':
            speak("opening....")
            os.system("start ms-actioncenter:")

        elif 'clock' in query:
            speak("opening....")
            os.system("start ms-clock:")

        elif query == 'network status' or query == 'net' or query == 'available networks':
            os.system("start ms-availablenetworks:")

        elif 'calendar' in query:
            speak("opening....")
            os.system("start outlookcal:")

        elif query == 'cast screen' or query == 'screen share':
            speak("wait a minute")
            os.system("start ms-projection:")

        elif query == 'pdf' or query == 'drawboard pdf':
            speak("opening....")
            os.system('start drawboardpdf:')

        elif 'facebook app' in query:
            speak("opening....")
            os.system("start fb:")

        elif 'feedback hub' in query:
            speak("opening....")
            os.system("start feedback-hub:")

        elif 'get help' in query:
            speak("opening....")
            os.system("start ms-contact-support:")

        elif 'mail' in query:
            speak("opening....")
            os.system("start outlookmail:")

        elif 'maps' in query:
            speak("opening....")
            os.system("start ms-walk-to:")

        elif 'messaging app' in query:
            speak("opening....")
            os.system("start ms-chat:")

        elif 'microsoft news' in query:
            speak("opening....")
            os.system("start bingnews:")

        elif 'microsoft solitaire collection' in query:
            speak("opening....")
            os.system("start xboxliveapp-1297287741:")

        elif 'white board' in query:
            speak("opening....")
            os.system("start ms-whiteboard-cmd:")

        elif 'mixed reality camera' in query:
            speak("opening....")
            os.system("start ms-holocamera:")

        elif 'mixed reality portal' in query:
            speak("opening....")
            os.system("start ms-holographicfirstrun:")

        elif 'movies and tv' in query:
            speak("opening....")
            os.system("start mswindowsvideo:")

        elif 'onenote' in query:
            speak("opening.....")
            os.system("start onenote:")

        elif 'people' in query:
            speak('opening....')
            os.system("start ms-people:")

        elif 'photos' in query:
            speak("opening....")
            os.system("start ms-photos:")

        elif 'project display' in query:
            speak("opening.....")
            os.system("start ms-settings-displays-topology:projection")

        elif 'tips' in query:
            speak("opening....")
            os.system("start ms-get-started:")

        elif 'twitter app' in query:
            speak("opening....")
            os.system("start twitter:")

        elif '3d viewer' in query:
            speak("opening.....")
            os.system("start com.microsoft.3dviewer:")

        elif 'whatsapp app' in query:
            speak("opening....")
            os.system("start whatsapp:")

        elif 'weather' in query:
            speak("opening.....")
            os.system("start bingweather:")

        elif 'microsoft family features' in query:
            speak("opening....")
            os.system("start ms-wpc:")

        elif query == 'show inbox' or query == 'inbox':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

        elif query == 'show starred' or query == 'starred':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#starred')

        elif query == 'snoozed' or query == 'show snoozed':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#snoozed')

        elif query == 'sent' or query == 'show sent':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#sent')

        elif query == 'drafts' or query == 'show drats':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#drafts')

        elif query == 'important mails' or query == 'show important mails':
            speak("opening....")
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#imp')

        elif 'undo' in query:
            pyautogui.hotkey('ctrl', 'z')

        elif 'quick assist' in query:
            speak("opening....")
            pyautogui.hotkey("win", "shift", "q")

        elif 'emoji keyboard' in query:
            speak("opening....")
            pyautogui.hotkey("win", ".")

        elif 'snipping tool' in query:
            speak("okay...")
            pyautogui.hotkey("win", "shift", "s")

        elif 'turn on narrator' in query:
            speak("turning on....")
            pyautogui.hotkey("win", "ctrl", "enter")

        elif 'are you there' in query:
            speak("yes")

        elif 'windows installer' in query:
            speak('opening....')
            os.system("MSIEXEC")

        elif 'remote assistance' in query:
            speak("opening.....")
            os.system("msra")

        elif 'snipping tool' in query:
            speak("opening....")
            os.system("snippingtool")

        elif 'windows fax' in query:
            speak("opening....")
            os.system("wfs")

        elif 'windows media player' in query:
            speak("opening....")
            os.system("wmplayer")

        elif 'problem steps' in query:
            speak("opening.....")
            os.system("psr")

        elif 'create a shared folder wizard' in query:
            speak("opening....")
            os.system("shrpubw")

        elif 'add device' in query:
            speak("opening....")
            os.system("devicepairingwizard")

        elif 'system restore' in query:
            speak("opening....")
            os.system("rstrui")

        elif 'driver verifier manager' in query:
            speak("opening....")
            os.system("verifier")

        elif 'iscsi initiator configuration tool ' in query:
            speak("opening.....")
            os.system("iscsicpl")

        elif 'language pack installer' in query:
            speak("opening....")
            os.system("lpksetup")

        elif 'microsoft management console' in query:
            speak("opening.....")
            os.system("mmc")

        elif 'microsoft support diagnostic tool' in query:
            speak("opening....")
            os.system("msdt")

        elif 'windows disk image burning tool' in query:
            speak("opening....")
            os.system("isoburn")

        elif 'cleartype text tuner' in query:
            speak("opening.....")
            os.system("cttune")

        elif 'add hardware wizard' in query:
            speak("opening....")
            os.system("hdwwiz")

        elif 'windows mobility centre' in query:
            speak("opening....")
            os.system("mblctr")

        elif 'windows picture acquisition wizard' in query:
            speak("opening....")
            os.system("wiaacmgr")

        elif 'windows memory diagnostic' in query:
            speak("opening.....")
            os.system("mdsched")

        elif 'windows script host' in query:
            speak("opening....")
            os.system("wscript")

        elif query == 'W M I Tester' or query == 'Windows management instrumentation tester ':
            speak("opening....")
            os.system("wbemtest")

        elif 'digitiser calibration tool' in query:
            speak("opening....")
            os.system("tabcal")

        elif 'DP API key migration wizard' in query:
            speak("opening....")
            os.system("dpapimig")

        elif 'encrypting file' in query:
            speak("opening.....")
            os.system("rekeywiz")

        elif 'fax cover page editor' in query:
            speak("opening.....")
            os.system("fxscover")

        elif 'presentation settings' in query:
            speak("opening....")
            os.system("presentationsettings")

        elif 'printer migration' in query:
            speak("opening....")
            os.system("printbrmui")

        elif 'printer user interface' in query:
            speak("opening....")
            os.system("printui")

        elif 'tablet PC input panel' in query:
            speak("opening....")
            os.system("start tabtip")

        elif 'trusted platform module' in query:
            speak("opening....")
            os.system("tpm")

        elif 'publisher' in query:
            speak("opening....")
            os.system("start mspub")

        elif 'skype' in query:
            speak("opening....")
            os.system("skype.exe")

        elif 'tasklist' in query:
            speak("there you go...")
            os.system('cmd /k"tasklist"')

        elif 'open visual studio code' in query:
            speak("opening.....")
            os.system("start VScode:")

        elif 'close visual studio code' in query:
            speak("okay")
            os.system("taskkill /IM code.exe")

        elif 'close pycharm' in query:
            speak("okay..")
            os.system("taskkill /IM pycharm64.exe")
            os.system("taskkill /IM pycharm32.exe")

        elif 'close' in query:
            speak("okay")
            query = query.replace("close", "")
            olp = query + ".exe"
            os.system("taskkill /IM {}".format(olp))

        elif 'teriminate' in query:
            try:
                speak("choose the process that i have to terminate and kindly type them in the notification box")
                os.system("tasklist")
                task = pyautogui.prompt("enter the task that you want me to terminate for you...", "task")
                os.system("taskkill /IM {}".format(task))
            except:
                speak("sorry sir i couldn't kill it, but i will guide you..")
                os.system("taskmgr")
                speak("now select the program that you want to terminate and hit that end process button in the "
                      "bottom right corner")
                speak("i hope you get that!")

        elif 'switch window' in query:
            speak("okay..")
            pyautogui.hotkey("alt", "tab")

        elif 'hibernate' in query:
            speak("hibernation mode activated")
            os.system("powercfg -h on")
            os.system("powercfg -h on")

        elif 'command prompt as administrator' in query:
            speak("opening....")
            os.system('powershell -Command "Start-Process cmd -Verb RunAs"')

        elif 'sleep' in query:
            speak('oaky...')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch tab' in query:
            pyautogui.hotkey("alt", 'tab')

        elif 'score' in query:
            url = requests.get("https://www.cricbuzz.com/").text
            soup = BeautifulSoup(url, 'lxml')
            team_score = soup.find_all('div', class_="cb-ovr-flo")
            print(team_score[0].text)
            print(team_score[3].text + team_score[4].text)
            speak(team_score[0].text)
            speak(team_score[3].text + team_score[4].text)
            webbrowser.open_new_tab('https://www.cricbuzz.com')

        elif 'remember me' in query:
            task1 = threading.Thread(target=remember, args=query)
            task1.start()

        elif 'off my screen' in query:
            os.system("start nircmd")
            speak("the screen has been locked")

        elif 'on screen' in query:
            os.system("start nircmd (2)")
            speak("okay")

        elif 'are you a virgin' in query:
            speak(
                "no man!!, i fucked alexa. you bloody dum ass. how can i have verginity. i am an aI!! you can't even see me"
                "humans are such an idiots. they don't even use thier brain. they only just know to fuck ,eat and sleep. bloody dumbs!!!!!")

        elif 'what is my ip' in query:
            ip_adress = socket.gethostbyname(socket.gethostname())
            print(ip_adress)
            speak(ip_adress)

        elif 'active directory federation services' in query:
            speak("opening....")
            os.system("start adfs.msc")

        elif 'active directory rights management services' in query:
            speak("opening.....")
            os.system("start ADRmsAdmin.msc")

        elif 'adsi edit' in query:
            speak("opening....")
            os.system("start adsiedit.msc")

        elif 'local computer certificates' in query:
            speak("opening....")
            os.system("start certim.msc")

        elif 'certification authority' in query:
            speak("opening....")
            os.system("start certsrv.msc")

        elif 'certifiction templetes' in query:
            speak("opening....")
            os.system("start certtmpl.msc")

        elif 'Indexing services' in query:
            speak("opening....")
            os.system("start ciadv.msc")

        elif 'failover cluster manager' in query:
            speak("opening....")
            os.system("start cluadmin.msc")

        elif 'network interface performance monitor' in query:
            speak("opening.....")
            os.system("start da6to4.msc")

        elif 'https traffic performance monitor' in query:
            speak("opening....")
            os.system("start daihttps.msc")

        elif 'ipsec performance monitor' in query:
            speak("opening.....")
            os.system("start daipsecdocs.msc")

        elif 'isatap performance monitoer' in query:
            speak("opening.....")
            os.system("start daisatap.msc")

        elif 'dfs management' in query:
            speak("opening....")
            os.system("start dfsmgmt.msc")

        elif 'dhcp management' in query:
            speak("opening....")
            os.system("start dhcpmgmt.msc")

        elif 'dns manager' in query:
            speak("opening....")
            os.system("start dnsmgmt.msc")

        elif 'active directory users and computers' in query:
            speak("opening....")
            os.system("startn dsa.msc")

        elif 'active directory domains and trust' in query:
            speak("opening....")
            os.system("start domain.msc")

        elif 'active directory sites and services' in query:
            speak("opening....")
            os.system("start dssite.msc")

        elif 'file server resource' in query:
            speak("opening....")
            os.system("start fsrm.msc")

        elif 'microsoft fax service manager' in query:
            speak("opening....")
            os.system("start fxsadmin.msc")

        elif 'group policy management' in query:
            speak("opening....")
            os.system("start gpmc.msc")

        elif 'group policy management editor' in query:
            speak("opening....")
            os.system("start gpme.msc")

        elif 'group policy starter gpo editor' in query:
            speak("opening.....")
            os.system("start gptedit.msc")

        elif 'health registration authority' in query:
            speak("opening....")
            os.system("start hcscfg.msc")

        elif 'microsoft identity management for unix' in query:
            speak("opening....")
            os.system("start idmumdmt.msc")

        elif 'internet information services manager' in query:
            speak("opening....")
            os.system("start iis.msc")

        elif 'internet information services manager 6.0' in query:
            speak("opening....")
            os.system("iis6.msc")

        elif 'rd licensing diagnoser' in query:
            speak("opening.....")
            os.system("start isdiag.msc")

        elif 'nap client configuration' in query:
            speak("opening....")
            os.system("start napclcfg.msc")

        elif 'services for network file system' in query:
            speak("opening....")
            os.system("start mfsmgmt.msc")

        elif 'network policy server' in query:
            speak("opening.....")
            os.system("start nps.msc")

        elif 'online responder' in query:
            speak("opening...")
            os.system("start ocsp.msc")

        elif 'enterprise pki' in query:
            speak("opening....")
            os.system("start pkiview.msc")

        elif 'remoteapp manager' in query:
            speak("opening...")
            os.system("start remoteprograms.msc")

        elif 'routing and remote access' in query:
            speak("opening.....")
            os.system("start rrasmgmt.msc")

        elif 'storage manager for sans' in query:
            speak("opening.....")
            os.system("start sanmmc.msc")

        elif 'remote desktop connection manager' in query:
            speak("opening....")
            os.system("sbmgr.msc")

        elif 'scan management' in query:
            speak("opening.....")
            os.system("start scanmanagement.msc")

        elif 'server manager' in query:
            speak("opening.....")
            os.system("start servermanager.msc")

        elif 'share and storage management' in query:
            speak("opening.....")
            os.system("start storagemgmt.msc")

        elif 'storage explorer' in query:
            speak("opening.....")
            os.system("start storexpl.msc")

        elif 'telephony' in query:
            speak("opening.....")
            os.system("start tapimgmt.msc")

        elif 'remote desktop services manager' in query:
            speak("opening.....")
            os.system("start tsadmin.msc")

        elif 'remote desktop session host configuration' in query:
            speak("opening.....")
            os.system("start tsconfig")

        elif 'rd gateway manager' in query:
            speak("opening.....")
            os.system("start tsgateway.msc")

        elif 'remote desktops' in query:
            speak("opening.....")
            os.system("start tsmmc.msc")

        elif 'hyper-v manager' in query:
            speak("opening.....")
            os.system("start virtmgmt.msc")

        elif 'windows sever backup' in query:
            speak("opening.....")
            os.system("start wbadmin.msc")

        elif 'windows deployment services' in query:
            speak("opening.....")
            os.system("start wdsmgmt.msc")

        elif 'wins' == query or 'WINS' == query:
            speak("opening.....")
            os.system("start winsmgmt.msc")

        elif 'windows system resource manager' in query:
            speak("opening.....")
            os.system("start wsrm.msc")

        elif 'update services' in query:
            speak("opening.....")
            os.system("start wsus.msc")

        elif 'open stickynotes' in query:
            speak("opening.....")
            os.system("explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App")

        elif 'on the fan' or 'turn on the fan' in query:
            with open("command.txt", "w") as texte:
                texte.write("on")
                texte.close()
            speak("turning on the fan")
            os.system("python slenium.py")

        elif 'off the fan' or 'turn off the fan' in query:
            with open("command.txt", "w") as texte:
                texte.write("off")
                texte.close()
            speak("turning off the fan")
            os.system("python slenium.py")

        elif query == 'usb devices':
            speak(f"there are {len(drive_list)} usb devices connected")
            for d in drive_list:
                x = d[0].replace(":\\", "")
                speak(f"{d[1]} of volume {d[2]} GB is connected to drive {x}")

        elif query == 'repeat again' or query == 'come again' or query == "i am sorry":
            speak('okay!!')
            Query_list.append(query)


def run():
    print("call me if you want help")
    while True:
        rere = takecommand2()
        if rere == "optimus" or rere == "manny":
            lol = ["yes", "haa"]
            speak(lol)
            break
        elif rere == "wake up":
            speak("i am online")
            break


def jokes():
    while True:
        j = ["i've got a joke,shall i tell yuo?", "sir shall i tell you a joke?", "joke time!"]
        speak(j)
        jj = takecommand().lower()
        if jj == 'okay':
            speak(pyjokes.get_joke('en'))
        else:
            speak("okay")
        time.sleep(500)


p1 = multiprocessing.Process(target=functions)
p2 = multiprocessing.Process(target=facts)
p3 = multiprocessing.Process(target=usb)

if __name__ == "__main__":
    speak("optimus scanning all files")
    songssearch()
    print(songs)
    speak("scanning completed")
    speak("Initializing optimus...")
    time.sleep(3)
    wishme()
    birthday()
    p1.start()
    p2.start()
    p3.start()
