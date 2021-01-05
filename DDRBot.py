from pyautogui import *
import pyautogui 
import time
import keyboard

## This code is written to FC any map on DDR (Link used : http://p.eagate.573.jp/game/eacddr/vic/app/2020051402/index.html)

## The numbers below are manually aquired (wont work on different screens)
## Arrow1: 438 301
## Arrow2: 577 342
## Arrow3: 678 266
## Arrow4: 816 303

#Colors are at the tips of the arrows
#Gray: 72 72 72
#White: 255 255 255

#Current logic used: If the tips of the arrows arent white or gray, click the arrow
## It can be made much better by many ways but it just is not worth it atm



def click(Arrow):
    if(Arrow) == 1:
        keyboard.press_and_release("left")
    if(Arrow) == 2:
        keyboard.press_and_release("down")
    if(Arrow) == 3:
        keyboard.press_and_release("up")
    if(Arrow) == 4:
        keyboard.press_and_release("right")

try:
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(438,301)[0] != 72 and pyautogui.pixel(438,301)[0] != 255:
            click(1)
        if pyautogui.pixel(577,342)[0] != 72 and pyautogui.pixel(577,342)[0] != 255:
            click(2)
        if pyautogui.pixel(678,266)[0] != 72 and pyautogui.pixel(678,266)[0] != 255:
            click(3)
        if pyautogui.pixel(816,303)[0] != 72 and pyautogui.pixel(816,303)[0] != 255:
            click(4)        
except :
    pass 