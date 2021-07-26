import pyautogui, time
def RelSc():
        
    x = int(input('Enter the number of pages to skip (A value greater than 0):'))

    i = 1
    
    while i < x:
        pyautogui.mouseDown(50, 917)
        time.sleep(1)
        pyautogui.moveTo(50, 228, duration=3)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        i = i + 1

    i = 0
    
    while i < 50-x:
        
        pyautogui.mouseDown(50, 917)
        time.sleep(1)
        pyautogui.moveTo(50, 228, duration=3)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.mouseDown(1100, 350)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.mouseDown(1100, 575)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        pyautogui.mouseDown(1100, 800)
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)

        i = i + 1   

RelSc()