import pyautogui, time,  winsound, sys

def ContRen():

                pyautogui.mouseDown(50, 917)
                time.sleep(1)
                pyautogui.moveTo(50, 228, duration=3)
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)
ContRen()