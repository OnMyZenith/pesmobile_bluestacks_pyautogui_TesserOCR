import pyautogui, time, winsound

def Cont():
    time.sleep(2)
    if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
        winsound.Beep(2000, 100)
        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
        time.sleep(2)
        pyautogui.mouseUp()

Cont()