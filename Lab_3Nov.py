import pyautogui 
import time
import keyboard 

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\google_search.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\google_search.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://youtube.com")
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def cautare_youtube():
    time.sleep(1)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\youtube_search.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\youtube_search.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("Andrei Saran")
        pyautogui.press('enter')
    else:
        print("Imaginea nu este pe ecran")

def accesare_canal():
    time.sleep(1)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\accesare_canal.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\accesare_canal.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imaginea nu este pe ecran")

def subscribe():
    time.sleep(1)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\subscribe.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'C:\Users\Student\Pictures\AS_3421\subscribe.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imaginea nu este pe ecran")



cautare_google()
cautare_youtube()
accesare_canal()
subscribe()

