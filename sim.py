import pyautogui as pyg
import time
from PIL import Image

f = open('./logs/sim_log.txt', 'a')

pyg.PAUSE = 0
pyg.FAILSAFE = True

img2ndHalf = Image.open('./assets/2ndHalf.png')
imgBack = Image.open('./assets/Back.png')
imgCF_Goios = Image.open('./assets/CF_Goios.png')
imgCF_Jarvis = Image.open('./assets/CF_Jarvis.png')
imgConfirm = Image.open('./assets/Confirm.png')
imgGP = Image.open('./assets/GP.png')
imgJuve = Image.open('./assets/Juve.png')
imgNext = Image.open('./assets/Next.png')
imgOK = Image.open('./assets/OK.png')
imgProceed = Image.open('./assets/Proceed.png')
imgRenew = Image.open('./assets/Renew.png')
imgRetry = Image.open('./assets/Retry.png')
imgSign = Image.open('./assets/Sign.png')
imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgSquadNotFine = Image.open('./assets/SquadNotFine.png')
imgSwitchSquad = Image.open('./assets/SwitchSquad.png')
imgSwitchTo1 = Image.open('./assets/SwitchTo1.png')
imgSwitchTo2 = Image.open('./assets/SwitchTo2.png')
imgToMatch = Image.open('./assets/ToMatch.png')

regionOK = (900, 550, 1020, 950)


def print2Both(text):
    print(text)
    f.write(text+'\n')


def clickIfFound(buttonName, img, REGION):
    print2Both('Looking for '+buttonName+'\n')
    point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)
    while(point):
        print2Both("Found "+buttonName+"and entered loop\n")
        pyg.mouseDown(point)
        lastClickTime=time.time()
        time.sleep(2)
        pyg.mouseUp()
        print2Both("Clicked "+buttonName+" for 2secs and now waiting 5secs before rechecking and retrying if needed\n")
        time.sleep(5)
        point = None
        point = pyg.locateCenterOnScreen(img, region=REGION, confidence=.98)






print2Both('\n\n\n\n')
print2Both(time.ctime()+'\n\n\n')
print2Both("Starting Autoplay in 10 seconds\n\n")
time.sleep(10)
lastClickTime=time.time()

while(1):
    clickIfFound('OK', imgOK, regionOK)




    if(time.time()-clickIfFound.lastClickTime()>0):
        print2Both("Something went wrong")


f.close()
