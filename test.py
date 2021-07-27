import pyautogui as pyg
import time
from PIL import Image


pyg.PAUSE = 0
pyg.FAILSAFE = True

img2ndHalf = Image.open('./assets/2ndHalf.png')
imgBack = Image.open('./assets/Back.png')
imgConfirm = Image.open('./assets/Confirm.png')
# imgGP = Image.open('./assets/GP.png')
imgJuve = Image.open('./assets/Juve.png')
imgNext = Image.open('./assets/Next.png')
imgOK = Image.open('./assets/OK.png')
imgProceed = Image.open('./assets/Proceed.png')
imgRetry = Image.open('./assets/Retry.png')
imgSign = Image.open('./assets/Sign.png')
# imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgSquadNotFine = Image.open('./assets/SquadNotFine.png')
imgSwitchSquad = Image.open('./assets/SwitchSquad.png')
imgSwitchTo1 = Image.open('./assets/SwitchTo1.png')
imgSwitchTo2 = Image.open('./assets/SwitchTo2.png')
imgToMatch = Image.open('./assets/ToMatch.png')

region2ndHalf = (1560, 970, 1715, 1060)
regionBack = (0, 980, 109, 1050)
regionConfirm = (1630, 975, 1715, 1045)
# regionGP = (675, 558, 775, 663)
regionJuve = (50, 320, 225, 500)
regionNext = (1690, 980, 1740, 1046)
regionOK = (900, 550, 1020, 950)
regionProceed = (1090, 628, 1190, 690)
regionRetry = (1100, 660, 1280, 740)
regionSign = (900, 990, 960, 1040)
# regionSquadContRen = (770, 409, 856, 453)
regionSquadNotFine = (470, 65, 690, 225)
regionSwitchSquad = (948, 184, 1055, 274)
regionSwitchTo1 = (0, 800, 200, 890)
regionSwitchTo2 = (478, 505, 847, 920)
regionToMatch = (1609, 990, 1680, 1040)


def check(buttonName, img, REGION):
    global foundButton
    foundButton = False
    print('Checking for '+buttonName)
    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(point is not None):
        print("Found "+buttonName)
        foundButton = True
    else:
        print("Couldn't find "+buttonName)
        foundButton = False


def click(buttonName, img, REGION, haveToClick, waitAfterClick):
    print('Looking for '+buttonName)
    global lastClickTime

    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(haveToClick):
        while(point is None):
            print("Waiting for "+buttonName)
            time.sleep(2)
            point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

        while(point):
            print("Found "+buttonName+" and entered loop")
            pyg.mouseDown(point)
            lastClickTime = time.time()
            time.sleep(2)
            pyg.mouseUp()
            print("Clicked "+buttonName +" and now waiting "+str(waitAfterClick)+" seconds before rechecking and retrying if needed")
            time.sleep(waitAfterClick)
            point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    elif(point):
        print("Found "+buttonName)
        pyg.mouseDown(point)
        lastClickTime = time.time()
        time.sleep(2)
        pyg.mouseUp()
        print("Clicked "+buttonName +" and now waiting "+str(waitAfterClick)+" seconds and moving on")
        time.sleep(waitAfterClick)

while(1):
    check("SquadNotFine", imgSquadNotFine, regionSquadNotFine)
