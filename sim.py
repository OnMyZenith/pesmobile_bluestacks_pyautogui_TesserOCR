import pyautogui as pyg
import time
from PIL import Image

pyg.PAUSE = 0
pyg.FAILSAFE = True

img2ndHalf = Image.open('./assets/2ndHalf.png')
imgBack = Image.open('./assets/Back.png')
imgConfirm = Image.open('./assets/Confirm.png')
imgJuve = Image.open('./assets/Juve.png')
imgNext = Image.open('./assets/Next.png')
imgOK = Image.open('./assets/OK.png')
imgProceed = Image.open('./assets/Proceed.png')
imgRetry = Image.open('./assets/Retry.png')
imgSign = Image.open('./assets/Sign.png')
imgSquadNotFine = Image.open('./assets/SquadNotFine.png')
imgSwitchSquad = Image.open('./assets/SwitchSquad.png')
imgSwitchTo1 = Image.open('./assets/SwitchTo1.png')
imgSwitchTo2 = Image.open('./assets/SwitchTo2.png')
imgToMatch = Image.open('./assets/ToMatch.png')
imgCF_SS_Hervey = Image.open('./assets/CF_SS_Hervey.png')
imgCF_Jarvis = Image.open('./assets/CF_Jarvis.png')
imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgGP = Image.open('./assets/GP.png')
imgRenew = Image.open('./assets/Renew.png')
imgOK = Image.open('./assets/OK.png')

region2ndHalf = (1560, 970, 1715, 1060)
regionBack = (0, 980, 109, 1050)
regionConfirm = (1630, 975, 1715, 1045)
regionJuve = (50, 320, 225, 500)
regionNext = (1690, 980, 1740, 1046)
regionOK = (900, 550, 1020, 950)
regionProceed = (1090, 628, 1190, 690)
regionRetry = (1100, 660, 1280, 740)
regionSign = (900, 990, 960, 1040)
regionSquadNotFine = (470, 65, 690, 225)
regionSwitchSquad = (948, 184, 1055, 274)
regionSwitchTo1 = (0, 800, 200, 890)
regionSwitchTo2 = (478, 505, 847, 920)
regionToMatch = (1609, 990, 1680, 1040)
regionCF_SS_Hervey = (432, 277, 640, 340)
regionCF_Jarvis = (430, 275, 622, 341)
regionSquadContRen = (770, 409, 856, 453)
regionGP = (675, 558, 775, 663)
regionRenew = (1105, 590, 1290, 660)
regionOK = (900, 550, 1020, 950)

a = (600, 350)              # a                          b
b = (1200, 350)             #
c = (600, 575)              # c                          d
d = (1200, 575)             #
e = (600, 800)              # e                          f
f = (1200, 800)             #
selectButtonPosition = (1200, 1010)
actionButtonPosition = (1200, 1010)

squad1 = (selectButtonPosition, a, b, c, d, e, f, 1, a, b, c, d, 1, e, actionButtonPosition)
squad2 = (selectButtonPosition, a, b, c, d, e, f, 1, a, b, c, d, e, actionButtonPosition)


def print2Both(text):
    global f
    print(text)
    f.write(text+'\n')


def notRunning():
    if(time.time()-lastClickTime > 1200):
        print2Both('\n\n'+time.ctime()+'\n')
        print2Both("Something went Wrong....Aborting\n\n")
        return True


def check(buttonName, img, REGION):
    print2Both('Checking for '+buttonName)
    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(point):
        print2Both("Found "+buttonName)
        return True
    else:
        print2Both("Couldn't find "+buttonName)
        return False


def click(buttonName, img, REGION, haveToClick, waitAfterClick):
    print2Both('Looking for '+buttonName)
    global lastClickTime

    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(haveToClick):
        while(point is None):
            print2Both("Waiting for "+buttonName)
            time.sleep(2)
            point = pyg.locateCenterOnScreen(
                img, region=REGION, confidence=.98)

        while(point):
            print2Both("Found "+buttonName+" and entered loop")
            pyg.mouseDown(point)
            lastClickTime = time.time()
            time.sleep(2)
            pyg.mouseUp()
            print2Both("Clicked "+buttonName + " and now waiting " +
                       str(waitAfterClick)+" seconds before rechecking and retrying if needed")
            time.sleep(waitAfterClick)
            point = pyg.locateCenterOnScreen(
                img, region=REGION, confidence=.98)
    elif(point):
        print2Both("Found "+buttonName)
        pyg.mouseDown(point)
        lastClickTime = time.time()
        time.sleep(2)
        pyg.mouseUp()
        print2Both("Clicked "+buttonName + " and now waiting " +
                   str(waitAfterClick)+" seconds and moving on")
        time.sleep(waitAfterClick)


def clickOnPoint(coordinate):
    pyg.mouseDown(coordinate)
    time.sleep(1)
    pyg.mouseUp()
    time.sleep(1)


def scrollUp():
    print2Both("Scrolling to top")
    pyg.mouseDown(50, 300)
    pyg.moveTo(50, 800, duration=0.5)
    pyg.mouseUp()
    time.sleep(3)
    pyg.mouseDown(50, 300)
    pyg.moveTo(50, 800, duration=0.5)
    pyg.mouseUp()
    time.sleep(4)


def scrollDownSlow():
    pyg.mouseDown(50, 917)
    time.sleep(1)
    pyg.moveTo(50, 228, duration=3)
    time.sleep(2)
    pyg.mouseUp()
    time.sleep(1)


def select(squad):
    for i in squad:
        if(i == 1):
            scrollDownSlow()
            continue
        clickOnPoint(i)


def renew(squad):
    while(True):
        contDone = False
        select(squad)
        wait = 4
        click('SquadContRen', imgSquadContRen, regionSquadContRen, True, wait)
        while(True):
            if(check('OK', imgOK, regionOK)):
                click('OK', imgOK, regionOK, True, wait)
                contDone = True
                break
            elif(check('GP', imgGP, regionGP)):
                click('GP', imgGP, regionGP, True, wait)
                break
        if(contDone):
            break
        click('Renew', imgRenew, regionRenew, True, wait)
        while(True):
            if(check('Retry', imgRetry, regionRetry)):
                click('Retry', imgRetry, regionRetry, True, wait)
                break
            elif(check('OK', imgOK, regionOK)):
                click('OK', imgOK, regionOK, True, wait)
                break
        scrollUp()


def snfSwitch():
    global wait
    wait = 10
    click('SquadNotFine', imgSquadNotFine, regionSquadNotFine, True, wait)
    click('Juve', imgJuve, regionJuve, True, wait)
    click('SwitchSquad', imgSwitchSquad, regionSwitchSquad, True, wait)

    while(True):
        if(check('SwitchTo1', imgSwitchTo1, regionSwitchTo1)):
            click('SwitchTo1', imgSwitchTo1, regionSwitchTo1, True, wait)
            break
        elif(check('SwitchTo2', imgSwitchTo2, regionSwitchTo2)):
            click('SwitchTo2', imgSwitchTo2, regionSwitchTo2, True, wait)
            break

    click('Confirm', imgConfirm, regionConfirm, True, wait)
    click('OK', imgOK, regionOK, True, wait)
    click('Back', imgBack, regionBack, True, wait)


def autosim():
    global f
    f = open('./logs/sim_log.txt', 'a')
    print2Both(
        '\n\n------------------------------------------------------------\n\n')
    print2Both(time.ctime()+'\n\n\n')
    print2Both("Starting Autoplay in 5 seconds\n\n")
    time.sleep(5)
    global lastClickTime
    lastClickTime = time.time()  # giving it an initial value

    while(1):
        waitForOneHalf = 150
        wait = 2
        click('OK', imgOK, regionOK, False, wait)
        click('2ndHalf', img2ndHalf, region2ndHalf, False, waitForOneHalf)
        click('Next', imgNext, regionNext, False, wait)
        click('Match Confirm', imgConfirm, regionConfirm, False, waitForOneHalf)
        click('Proceed', imgProceed, regionProceed, False, wait)
        click('Retry', imgRetry, regionRetry, False, wait)
        click('Sign', imgSign, regionSign, False, wait)

        if(check("SquadNotFine", imgSquadNotFine, regionSquadNotFine)):
            if(check('OK', imgOK, regionOK)):
                click('OK', imgOK, regionOK, True, wait)
            snfSwitch()

        click('ToMatch', imgToMatch, regionToMatch, False, 10)

        if(check("SquadNotFine", imgSquadNotFine, regionSquadNotFine)):
            if(check('OK', imgOK, regionOK)):
                click('OK', imgOK, regionOK, True, wait)
            snfSwitch()

        print2Both(
            '\n\n------------------------------------------------------------\n\n')
        print2Both(time.ctime()+'\n\n\n')
        if(notRunning()):
            break
    f.close()


def ContRen():
    global f
    f = open('./logs/contRen_log.txt', 'a')
    print2Both('\n\n------------------------------------------------------------\n\n')
    print2Both(time.ctime()+'\n\n\n')
    print2Both("Starting Contract Renewal in 5 seconds\n\n")
    time.sleep(5)

    while(1):
        print2Both('Checking Squad No....')
        while(True):
            if(check('CF_SS_Hervey', imgCF_SS_Hervey, regionCF_SS_Hervey)):
                print2Both("Found Squad 1")
                renew(squad1)
                break

            elif(check('CF_Jarvis', imgCF_Jarvis, regionCF_Jarvis)):
                print2Both("Found Squad 2")
                renew(squad2)
                break

            else:
                scrollUp()

        print2Both(
            '\n\n------------------------------------------------------------\n\n')
    f.close()


def start():
    task = int(input("AutoPlay : 1\nRenew Contracts : 2\n::"))
    if(task == 2):
        ContRen()
    elif(task == 1):
        autosim()
    else:
        start()

start()