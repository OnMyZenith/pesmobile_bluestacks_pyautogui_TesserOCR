import pyautogui, time,  winsound

def t():
    time.sleep(1)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    winsound.Beep(600, 500)
    winsound.Beep(600, 500)

    pyautogui.mouseDown(50, 300)
    pyautogui.moveTo(50, 800, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(3)
    pyautogui.mouseDown(50, 300)
    pyautogui.moveTo(50, 800, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(7)


t()