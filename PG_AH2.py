import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.05)
time.sleep(1)
pg.typewrite('donovan mitchell dunk on lonzo ball\n',0.05)
time.sleep(3)
pg.click(865, 410)
time.sleep(2)
pg.click(1306, 507)
time.sleep(2)
