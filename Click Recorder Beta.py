import pyautogui as pag
import pandas as pd
import keyboard
import time

def sleep(var1):
	time.sleep(var1)


locList = pd.DataFrame(columns=[])
endLoop = 2
while endLoop == 2:
    try:
        if keyboard.is_pressed("alt"):     #    alt is pressed, it will record that mouse location
            locX, locY = pag.position()
            locList = locList.append([[locX, locY]], ignore_index=True)
            endLoop = 2
            sleep(.5)
        elif keyboard.is_pressed("esc"):   #    press escape to end program
            endLoop = 1
            break
    except:
        pass
print(locList)
