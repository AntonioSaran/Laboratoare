import pyautogui 
import time
import keyboard 
pozitie_initiala_x=337
pozitie_initiala_y=450

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

def coordonate():
    print(pyautogui.position())
   

col=1
#cautare_google()

while not keyboard.is_pressed('esc'):
    coordonate()




