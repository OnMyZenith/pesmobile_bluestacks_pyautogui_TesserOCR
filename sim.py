import pyautogui as pyg
import time
from PIL import Image, ImageGrab
from tesserocr import PyTessBaseAPI
import os

pyg.PAUSE = 0
pyg.FAILSAFE = True

folderName = time.strftime("%Y-%m-%d %H'%M''%S",time.localtime())
path = './logs/'+folderName
os.mkdir(path)

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
imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgGP = Image.open('./assets/GP.png')
imgRenew = Image.open('./assets/Renew.png')

imgEx = Image.open('./assets/Ex.png')
imgLoginBonus_Confirm = Image.open('./assets/LoginBonus_Confirm.png')
imgLoginBonus = Image.open('./assets/LoginBonus.png')
imgFrontpage_Match = Image.open('./assets/Frontpage_Match.png')
imgFrontpage_Campaign = Image.open('./assets/Frontpage_Campaign.png')
imgFrontpage_Campaign_SimMatch = Image.open('./assets/Frontpage_Campaign_SimMatch.png')
imgTitlePage = Image.open('./assets/TitlePage.png')
imgAbandon = Image.open('./assets/Abandon.png')

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
regionIdentifyPlayer = (380, 275, 1800, 800)
regionSquadContRen = (770, 409, 856, 453)
regionGP = (675, 558, 775, 663)
regionRenew = (1105, 590, 1290, 660)

regionEx = (1806, 43, 1873, 112)
regionLoginBonus_Confirm = (1066, 655, 1314, 729)
regionLoginBonus = (1170, 215, 1575, 490)
regionFrontpage_Match = (167, 138, 350, 200)
regionFrontpage_Campaign = (1368, 849, 1483, 959)
regionFrontpage_Campaign_SimMatch = (1016, 156, 1150, 306)
regionTitlePage = (456, 683, 608, 818)
regionAbandon = (587, 649, 858, 736)

regionNegotiationSkills = [(275, 225, 400, 370), (275, 455, 400, 600), (275, 685, 400, 830)]
regionScoutNames = [(425, 240, 1000, 450), (425, 470, 1000, 680), (425, 700, 1000, 910)]

starsX = [301, 327, 355, 377]

class button:
    def __init__(self, name, img, region) -> None:
        self.name = name
        self.img = img
        self.region = region

secondHalf = button('2ndHalf', img2ndHalf, region2ndHalf)
Back = button('Back', imgBack, regionBack)
Confirm = button('Confirm', imgConfirm, regionConfirm)
Juve = button('Juve', imgJuve, regionJuve)
Next = button('Next', imgNext, regionNext)
ok = button('OK', imgOK, regionOK)
Proceed = button('Proceed', imgProceed, regionProceed)
Retry = button('Retry', imgRetry, regionRetry)
Sign = button('Sign', imgSign, regionSign)
SquadNotFine = button('SquadNotFine', imgSquadNotFine, regionSquadNotFine)
SwitchSquad = button('SwitchSquad', imgSwitchSquad, regionSwitchSquad)
SwitchTo1 = button('SwitchTo1', imgSwitchTo1, regionSwitchTo1)
SwitchTo2 = button('SwitchTo2', imgSwitchTo2, regionSwitchTo2)
ToMatch = button('ToMatch', imgToMatch, regionToMatch)
SquadContRen = button('SquadContRen', imgSquadContRen, regionSquadContRen)
gp = button('GP', imgGP, regionGP)
Renew = button('Renew', imgRenew, regionRenew)

Ex = button('Ex', imgEx, regionEx)
LoginBonus_Confirm = button('LoginBonus_Confirm', imgLoginBonus_Confirm, regionLoginBonus_Confirm)
LoginBonus = button('LoginBonus', imgLoginBonus, regionLoginBonus)
Frontpage_Match = button('Frontpage_Match', imgFrontpage_Match, regionFrontpage_Match)
Frontpage_Campaign = button('Frontpage_Campaign', imgFrontpage_Campaign, regionFrontpage_Campaign)
Frontpage_Campaign_SimMatch = button('Frontpage_Campaign_SimMatch', imgFrontpage_Campaign_SimMatch, regionFrontpage_Campaign_SimMatch)
TitlePage = button('TitlePage', imgTitlePage, regionTitlePage)
Abandon = button('Abandon', imgAbandon, regionAbandon)

a = (600, 350)              #       a       #              b
b = (1200, 350)             #               #
c = (600, 575)              #       c       #              d
d = (1200, 575)             #               #
e = (600, 800)              #       e       #              f
f = (1200, 800)
selectButtonPosition = (1200, 1010)
actionButtonPosition = (1200, 1010)
scoutPositions = (a, c, e)

allTactics = ['Attacking Styles', 'Build Up', 'Attacking Areas', 'Positioning', 'Defensive Styles', 'Containment Area', 'Pressuring']
allScouts = ['Attacking Styles', 'Build Up', 'Attacking Areas', 'Positioning', 'Defensive Styles', 'Containment Area', 'Pressuring', 'Acceleration', 'Control', 'Winning', 'Curl', 'Defensive Awareness', 'Dribbling', 'Finishing', 'GK Awareness', 'GK Catching', 'GK Clearing', 'GK Reach', 'GK Reflexes', 'Heading', 'Jump', 'Kicking', 'Left', 'Lofted', 'Low', 'Offensive', 'Physical', 'Place', 'Right', 'Speed', 'Stamina', '24', '185', 'AMF', 'CB', 'CF', 'CMF', 'DMF', 'LB', 'LMF', 'LWF', 'RB', 'RMF', 'RWF', 'SS', 'Utility', '30', 'Argentina', 'Brazil', 'Chile', 'Netherlands', 'England', 'Free Agent', 'France', 'Italy', 'Portugal', 'Spain', '(Asia', '[Asia', '(Europe', '[Europe', '(Latin', '[Latin', 'year', 'Africa', 'Oceania', 'Europe', 'Americas']

allScoutsAlias = ['Control', 'Winning', 'Kicking', 'Left', 'Lofted', 'Low', 'Offensive', 'Physical', 'Place', 'Right', '24', '185', 'Utility', '30', 'Argentina', 'Brazil', 'Chile', 'Netherlands', 'England', 'Free Agent', 'France', 'Italy', 'Portugal', 'Spain', '(Asia', '(Europe', '(Latin', '[Asia', '[Europe', '[Latin', 'year', 'Oceania', 'Americas']
allScoutsReal = ['Ball Control', 'Ball Winning', 'Kicking Power', 'Left foot', 'Lofted Pass', 'Low Pass', 'Offensive Awareness', 'Physical Contact', 'Place Kicking', 'Right foot', 'U-24', '185cm or Taller', 'Utility Players', '30+', 'Argentinian League', 'Brazilian League', 'Chiliean League', 'Dutch League', 'English League', 'FREE AGENT', 'French League', 'Italian League', 'Portuguese League', 'Spanish League', 'Other (Asia)', 'Other (Europe)', 'Other (Latin America)', 'Other (Asia)', 'Other (Europe)', 'Other (Latin America)', '25-29 year old', 'Asia-Oceania', 'N/S American']

imgCF_SS_Hervey = Image.open('./assets/CF_SS_Hervey.png')
imgCF_Jarvis = Image.open('./assets/CF_Jarvis.png')
CF_SS_Hervey = button('CF_SS_Hervey', imgCF_SS_Hervey, regionIdentifyPlayer)
CF_Jarvis = button('CF_Jarvis', imgCF_Jarvis, regionIdentifyPlayer)

squad1 = (selectButtonPosition, d, e, 1, a, b, c, d, e, f, 1, b, c, f, actionButtonPosition)
squad2 = (selectButtonPosition, d, f, 1, a, b, c, d, e, f, 1, b, d, e, actionButtonPosition)

def print2Both(text):
    print(text)
    f.write(str(text)+'\n')


f = open(path +'/log.txt', 'a')

def lineTime():
    print2Both('\n\n------------------------------------------------------------\n\n')
    print2Both(time.ctime()+'\n\n\n')

def line():
    print2Both('\n\n------------------------------------------------------------\n\n')

def check(bt):
    print2Both('CheckLoop: Checking for '+bt.name)
    point = pyg.locateCenterOnScreen(bt.img, region=bt.region, confidence=.98)

    if(point):
        print2Both("CheckLoop: Found "+bt.name)
        return bt.name
    else:
        print2Both("CheckLoop: Couldn't find "+bt.name)
        return None


def click(bt, haveToClick, waitAfterClick):
    print2Both('ClickLoop: Looking for '+bt.name)

    point = pyg.locateCenterOnScreen(bt.img, region=bt.region, confidence=.98)

    if(haveToClick):
        while(point is None):
            print2Both("ClickLoop: Waiting for "+bt.name)
            time.sleep(2)
            point = pyg.locateCenterOnScreen(bt.img, region=bt.region, confidence=.98)

        while(point):
            print2Both("ClickLoop: Found "+bt.name+" and entered loop")
            pyg.mouseDown(point)
            time.sleep(2)
            pyg.mouseUp()
            print2Both("ClickLoop: Clicked "+bt.name + " and now waiting " + str(waitAfterClick)+" seconds before rechecking and retrying if needed")
            time.sleep(waitAfterClick)  #Sometimes the button has same look for some time after its clicked so wait before checking if its clicked
            point = pyg.locateCenterOnScreen(bt.img, region=bt.region, confidence=.98)
    elif(point):
        print2Both("ClickLoop: Found "+bt.name)
        pyg.mouseDown(point)
        time.sleep(2)
        pyg.mouseUp()
        print2Both("ClickLoop: Clicked "+bt.name + " and now waiting " + str(waitAfterClick)+" seconds to save resource before moving on")
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


def scrollDownSlow(page=1):
    while(page):
        pyg.mouseDown(50, 917)
        time.sleep(1)
        pyg.moveTo(50, 228, duration=3)
        time.sleep(2)
        pyg.mouseUp()
        time.sleep(1)
        page -= 1


def select(squad):
    for i in squad:
        if(i == 1):
            scrollDownSlow()
            continue
        clickOnPoint(i)


def renew(squad):
    while(True):
        lineTime()
        global contDone
        contDone = False
        select(squad)
        wait = 4
        click(SquadContRen, True, wait)
        while(True):
            if(check(ok)):
                click(ok, True, wait)
                contDone = True
                break
            elif(check(gp)):
                click(gp, True, wait)
                break
        if(contDone):
            break
        click(Renew, True, wait)
        while(True):
            if(check(Retry)):
                click(Retry, True, wait)
                break
            elif(check(ok)):
                click(ok, True, wait)
                break
        scrollUp()


def snfSwitch():
    click(SquadNotFine, True, waitLong)
    click(Juve, True, waitLong)
    click(SwitchSquad, True, waitLong)

    while(True):
        if(check(SwitchTo1)):
            click(SwitchTo1, True, waitLong)
            break
        elif(check(SwitchTo2)):
            click(SwitchTo2, True, waitLong)
            break

    click(Confirm, True, waitLong)
    click(ok, True, waitLong)
    click(Back, True, waitLong)


def autosim():
    global waitLong
    global waitShort
    waitLong = 15       #Wait for button to go away in "true" "have to click" loops, Sometimes the button has same look for some time after its clicked so wait before checking if its clicked
    waitShort= 10       #Wait to save resource
    waitForOneHalf = 210
    matchNumber  = 0
    lineTime()
    print2Both("Starting AutoSim in 5 seconds\n\n")
    time.sleep(5)

    while(1):
        lineTime()
        # WaitLong on these buttons because scrolling on frontpage takes longer
        click(Ex, False, waitLong)
        click(LoginBonus_Confirm, False, waitLong)
        click(LoginBonus, False, waitLong)
        click(Frontpage_Match, False, waitLong)
        click(Frontpage_Campaign, False, waitLong)
        click(Frontpage_Campaign_SimMatch, False, waitLong)
        click(TitlePage, False, waitLong)
        click(Abandon, False, waitLong)

        click(ok, False, waitShort)
        click(secondHalf, False, waitForOneHalf)
        click(Next, False, waitShort)
        click(Confirm, False, 100 + waitForOneHalf)
        click(Proceed, False, waitShort)
        click(Retry, False, waitShort)
        click(Sign, False, waitShort)

        changedMatchNumber = False

        if check(ToMatch):
            matchNumber += 1
            changedMatchNumber = True
            pyg.screenshot('./logs/MatchScreenshots/'+folderName+' Match Number_'+str(matchNumber)+'_1.png')
            print2Both("Took a Screenshot of Campaign Summary")
            click(ToMatch, False, 15 + waitLong)     #Wait 30 secs for SNF and OK to show up if thery're going to for Matchmaking to Finish
            pyg.screenshot('./logs/MatchScreenshots/'+folderName+' Match Number_'+str(matchNumber)+'_2.png')
            print2Both("Took a Screenshot of Matchmaking")

            if check(SquadNotFine):
                if changedMatchNumber:
                    os.remove('./logs/MatchScreenshots/'+folderName+' Match Number_'+str(matchNumber)+'_1.png')
                    os.remove('./logs/MatchScreenshots/'+folderName+' Match Number_'+str(matchNumber)+'_2.png')
                    matchNumber -= 1

                time.sleep(waitShort)
                if(check(ok)):
                    click(ok, True, waitLong)
                snfSwitch()


def ContRen():
    lineTime()
    print2Both("Starting Contract Renewal in 5 seconds\n\n")
    time.sleep(5)

    while(True):
        print2Both('Checking Squad No....')
        if(check(CF_SS_Hervey)):
            print2Both("Found Squad 1")
            renew(squad1)
            break

        elif(check(CF_Jarvis)):
            print2Both("Found Squad 2")
            renew(squad2)
            break

        else:
            scrollUp()
    lineTime()
    print2Both("\n\nContracts Maxxed out.....Aborting\n\n")


def selectScouts(pages):
    scrollDownSlow(pages)
    while(True):
        select(scoutPositions)
        scrollDownSlow()


def start():
    global task
    if(not restarting):
        lineTime()
        print2Both("\n\nAutoSim : 1\nRenew Contracts : 2\nSelect Scouts : 3\nAnalyze Scouts : 4")
        task = int(input('>> '))

    if(task == 1):
        autosim()
    elif(task == 2):
        ContRen()
    elif(task == 3):
        pages = int(input("Enter no. of pages to skip : "))
        selectScouts(pages)
    elif(task == 4):
        numberOfScoutsLeft = int(input("Enter total number of Scouts  (Must be atleast 3) : "))
        analyzeScouts(numberOfScoutsLeft)


def printException(exception,shouldRestart):
    global restarting
    restarting = shouldRestart
    print2Both("\n\nException Occurred\n")
    lineTime()
    print2Both(repr(exception))
    if(shouldRestart):
        print2Both("\nRestarting in 5 seconds\n")
        time.sleep(5)
        run()
    else:
        print2Both("\nAborting\n")

def run():
    try:
        start()
    except pyg.FailSafeException as e:
        printException(e,False)
    except KeyboardInterrupt as e:
        printException(e,False)
    except OSError as e:
        printException(e,True)
    except BaseException as e:
        printException(e,True)

def avoidErrorUsingRecursion(a,b,c):
    global found
    global gotOSError
    try:
        if pyg.pixelMatchesColor(a, b, c):
            found = True
    except OSError:
        gotOSError+=1
        avoidErrorUsingRecursion(a,b,c)
def addScoutsOfPage():
    global scoutsCountedTwice
    global scouts
    global page
    global found
    threeScoutNames=[]
    threeNegotiationSkills = []

    for i in range(3):
        grabbedText = None
        oneScoutName = None
        isTactic = False

        if scoutsCountedTwice:
            scoutsCountedTwice -= 1
            print2Both("\nSkipping scout that's aready counted on last page\n")
            line()
            continue
        
        with PyTessBaseAPI() as api:
            api.SetImage(ImageGrab.grab(bbox=regionScoutNames[i]))
            grabbedText = api.GetUTF8Text()

        print2Both(grabbedText)

        for one in allScouts:
            if grabbedText.find(one) != -1:
                oneScoutName = one
                break
        
        for a in allTactics:
            if oneScoutName == a:
                isTactic = True

        if isTactic:
            clickOnPoint(scoutPositions[i])
            print2Both("\nSelecting and skipping index of Tactics in box : "+str(i+1)+"\n")
            continue

        if oneScoutName is None:
            oneScoutName = grabbedText

        print2Both("Recognized scout : ---"+oneScoutName+"---")
        # print2Both(api.AllWordConfidences())            #Crashes for some reason :(
        threeScoutNames.append(oneScoutName)
        
        for idx, k in  enumerate(starsX):
            found = False
            for j in range(regionNegotiationSkills[i][1], regionNegotiationSkills[i][3], 2):
                avoidErrorUsingRecursion(k, j, (254,203, 0))
            if not found:
                break
            if idx==3 & found is True:      ###Basically for 5* scout
                idx = 4                     ###idx only goes from 0 to 3
        threeNegotiationSkills.append(idx+1)

        print2Both("\nFinished with box "+str(i+1)+"\n")
        if i <2:
            print2Both("Currently on Page no. :"+str(page+1)+" out of "+str(int(totalNumber/3+0.7))+'\n')
    
        line()

    page+=1

    for i in range(len(threeScoutNames)):
        scouts.append([threeNegotiationSkills[i], threeScoutNames[i], page])
        
    print2Both("Finished with Page no. :"+str(page)+" out of "+str(int(totalNumber/3+0.7)))

    print2Both("\n\nScouts identified on Page :\n")
    for i in range(len(threeScoutNames)-1, -1, -1):
        print2Both("\n\t"+str(scouts[len(scouts)-1-i]))

    lineTime()
    pyg.screenshot(path+'/Page'+str(page)+'.png')

def analyzeScouts(numberOfScoutsLeft):
    time1= time.time()
    global totalNumber
    global scoutsCountedTwice
    global scouts
    global gotOSError
    gotOSError = 0
    global page
    page=0
    totalNumber = numberOfScoutsLeft
    scouts = []
    scoutsCountedTwice = 0
    isFinalPage = False

    while(numberOfScoutsLeft>0):
        if numberOfScoutsLeft<=3:
            scoutsCountedTwice = 3 - numberOfScoutsLeft
            isFinalPage = True

        addScoutsOfPage()

        if not isFinalPage:
            scrollDownSlow()
            time.sleep(2)

        numberOfScoutsLeft-=3

    lineTime()
    print2Both('Time taken to analyze '+str(len(scouts))+' scouts : '+str(int((time.time()-time1)/60))+' minutes and '+str(int((time.time()-time1)%60))+' seconds.')
    print2Both("\n\nTotal Scouts (Alias used for some):"+str(scouts)+"\n\n")
    print2Both("\n\nTotal times got OSError :"+str(gotOSError)+"\n\n")

    f1 = open(path +'/scouts_Alias.txt', 'a')
    for i in range(len(scouts)):
        f1.write(str(scouts[i][0])+', '+str(scouts[i][1])+"\n")
    f1.close()

    for i in range(len(allScoutsAlias)):
        for j in range(len(scouts)):
            if scouts[j][1] == allScoutsAlias[i]:
                scouts[j][1] = allScoutsReal[i]

    lineTime()
    print2Both("\n\nTotal Scouts :"+str(scouts)+"\n\n")

    f1 = open(path +'/scouts.txt', 'a')
    for i in range(len(scouts)):
        f1.write(str(scouts[i][0])+', '+str(scouts[i][1])+"\n")
    f1.close()

restarting = False
run()
f.close()