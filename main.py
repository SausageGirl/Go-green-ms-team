import pyautogui
import datetime
import time
while True:
    pyautogui.press('ctrl')
    print(datetime.datetime.now())
    time.sleep(240)