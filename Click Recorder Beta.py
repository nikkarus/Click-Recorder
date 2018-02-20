import pyautogui as pag
import pandas as pd
import keyboard
import time
import openpyxl as xl
import pandas as pd
from pandas import ExcelWriter


def sleep(var1):
	time.sleep(var1)

locList = pd.DataFrame()
endLoop = 2
while endLoop == 2:
    try:
        if keyboard.is_pressed("alt"):     #    alt is pressed, it will record that mouse location
            locX, locY = pag.position()
            locList = locList.append([[locX, locY]], ignore_index=True)
            endLoop = 2
            sleep(.2)
        elif keyboard.is_pressed("esc"):   #    press escape to end program
            endLoop = 1
            break
    except:
        pass
locList.columns = ['X', 'Y']
print(locList)

recordName = input("Please input what you would like to call this sheet:")

writer = ExcelWriter(str(recordName)+ ' ' + 'Click Recording' + '.xlsx')
locList.to_excel(writer, 'Sheet1', index=False)
writer.save()

