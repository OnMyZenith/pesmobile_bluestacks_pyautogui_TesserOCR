import pyautogui, time,  winsound

def t():
    time.sleep(5)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    winsound.Beep(500, 500)

    print("Couldn't recognise Squad number, Scrolling to top to check again")
    pyautogui.mouseDown(50, 300)
    pyautogui.moveTo(50, 800, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(3)
t()