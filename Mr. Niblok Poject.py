i = 0
import pyautogui as pg
import webbrowser
import time
webbrowser.open("amazon.com")
time.sleep(10)
while i < 5:
    pg.hotkey('tab')
    i += 1
time.sleep(1)
pg.typewrite("Vinyl Records", 0.1)
