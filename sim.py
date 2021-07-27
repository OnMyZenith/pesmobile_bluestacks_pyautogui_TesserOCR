import pyautogui as pyg
import time
from PIL import Image

f = open('./logs/sim_log.txt', 'a')

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


def print2Both(text):
    print(text)
    f.write(text+'\n')


def check(buttonName, img, REGION):
    global foundButton
    foundButton = False
    print2Both('Checking for '+buttonName)
    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(point is not None):
        print2Both("Found "+buttonName)
        foundButton = True
    else:
        print2Both("Couldn't find "+buttonName)
        foundButton = False


def click(buttonName, img, REGION, haveToClick, waitAfterClick):
    print2Both('Looking for '+buttonName)
    global lastClickTime

    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    if(haveToClick):
        while(point is None):
            print2Both("Waiting for "+buttonName)
            time.sleep(2)
            point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

        while(point):
            print2Both("Found "+buttonName+" and entered loop")
            pyg.mouseDown(point)
            lastClickTime = time.time()
            time.sleep(2)
            pyg.mouseUp()
            print2Both("Clicked "+buttonName +" and now waiting "+str(waitAfterClick)+" seconds before rechecking and retrying if needed")
            time.sleep(waitAfterClick)
            point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)

    elif(point):
        print2Both("Found "+buttonName)
        pyg.mouseDown(point)
        lastClickTime = time.time()
        time.sleep(2)
        pyg.mouseUp()
        print2Both("Clicked "+buttonName +" and now waiting "+str(waitAfterClick)+" seconds and moving on")
        time.sleep(waitAfterClick)


print2Both('\n\n\n\n')
print2Both(time.ctime()+'\n\n\n')
print2Both("Starting Autoplay in 5 seconds\n\n")
time.sleep(5)
lastClickTime = time.time()

while(1):
    waitForOneHalf=150
    wait = 2
    click('OK', imgOK, regionOK, False, wait)
    click('2ndHalf', img2ndHalf, region2ndHalf, False, waitForOneHalf)
    click('Next', imgNext, regionNext, False, wait)
    click('Confirm', imgConfirm, regionConfirm, False, waitForOneHalf)
    click('Proceed', imgProceed, regionProceed, False, wait)
    click('Retry', imgRetry, regionRetry, False, wait)
    click('Sign', imgSign, regionSign, False, wait)
    wait = 5
    click('ToMatch', imgToMatch, regionToMatch, False, 5)  #have to make sure ther's an OK between ToMatch and SNF
    click('OK', imgOK, regionOK, False, 5)                 #or could end in a loop ToMatch(clicked)-->SNF(not clicked coz OK is blocking it)---->OK(clicked)--->ToMatch(clicked)
    

    check("SquadNotFine", imgSquadNotFine, regionSquadNotFine)
    time.sleep(5)
    check("SquadNotFine", imgSquadNotFine, regionSquadNotFine)  #Doing this check twice just in case got a false pos 1st time('OK' could be blocking it now)
    
    wait = 10
    if(foundButton):

        click('SquadNotFine', imgSquadNotFine, regionSquadNotFine, True, wait) 
        click('Juve', imgJuve, regionJuve, True, wait) 
        click('SwitchSquad', imgSwitchSquad, regionSwitchSquad, True, wait) 

        while(True):
            check('SwitchTo1', imgSwitchTo1, regionSwitchTo1) 
            
            if(foundButton):
                click('SwitchTo1',imgSwitchTo1,regionSwitchTo1, True, wait) 
                break
            else:
                click('SwitchTo2',imgSwitchTo2,regionSwitchTo2, True, wait) 
                break

            
        click('Confirm', imgConfirm, regionConfirm, True, wait) 
        click('OK', imgOK, regionOK, True, wait) 
        click('Back', imgBack, regionBack, True, wait) 

    if(time.time()-lastClickTime > 600):
        print2Both('\n\n'+time.ctime()+'\n')
        print2Both("Something's not right\n\n")

    if(time.time()-lastClickTime > 1200):
        print2Both('\n\n'+time.ctime()+'\n')
        print2Both("Something went Wrong....Aborting\n\n")
        break

f.close()