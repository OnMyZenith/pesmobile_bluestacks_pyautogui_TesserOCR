import pyautogui, time
def test():
    time.sleep(3)
    i = 1
    while i < 49:
        pyautogui.mouseDown(50, 917)
        time.sleep(2)
        pyautogui.moveTo(50, 228, duration=3)
        time.sleep(2)
        pyautogui.mouseUp()
        time.sleep(2)
        i = i + 1
    #pyautogui.click(pyautogui.locateCenterOnScreen('test.png'))

test()