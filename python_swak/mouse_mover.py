import pyautogui as pag
import random
import time

while True:
    currentMouseX, currentMouseY = pag.position()
    pag.moveTo(currentMouseX + 10, currentMouseY + 10, duration=0.5)
    time.sleep(60)
    pag.moveTo(currentMouseX - 10, currentMouseY - 10, duration=0.5)
    time.sleep(60)
