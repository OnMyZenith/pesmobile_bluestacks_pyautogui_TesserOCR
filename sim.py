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

imgstar1 = Image.open('./assets/scouts/star1.png')
imgstar2 = Image.open('./assets/scouts/star2.png')
imgstar3 = Image.open('./assets/scouts/star3.png')
# imgstar4 = Image.open('./assets/scouts/star4.png')
# imgstar5 = Image.open('./assets/scouts/star5.png')

# imgArea_Europe = Image.open('./assets/scouts/Area_Europe.png')
# imgArea_Americas = Image.open('./assets/scouts/Area_Americas.png')
# imgArea_AsiaOceania = Image.open('./assets/scouts/Area_AsiaOceania.png')
# imgArea_Africa = Image.open('./assets/scouts/Area_Africa.png')
# imgAbility_LowPass = Image.open('./assets/scouts/Ability_LowPass.png')
# imgAbility_30plus = Image.open('./assets/scouts/Ability_30plus.png')
# imgAbility_U24 = Image.open('./assets/scouts/Ability_U24.png')
# imgAbility_GKClearing = Image.open('./assets/scouts/Ability_GKClearing.png')
# imgAbility_GKReach = Image.open('./assets/scouts/Ability_GKReach.png')
# imgAbility_GKCatching = Image.open('./assets/scouts/Ability_GKCatching.png')
# imgAbility_LoftedPass = Image.open('./assets/scouts/Ability_LoftedPass.png')
# imgAbility_25to29yearold = Image.open('./assets/scouts/Ability_25to29yearold.png')
# imgAbility_OffensiveAwareness = Image.open('./assets/scouts/Ability_OffensiveAwareness.png')
# imgAbility_PlaceKicking = Image.open('./assets/scouts/Ability_PlaceKicking.png')
# imgAbility_BallWinning = Image.open('./assets/scouts/Ability_BallWinning.png')
# imgAbility_BallControl = Image.open('./assets/scouts/Ability_BallControl.png')
# imgAbility_GKReflexes = Image.open('./assets/scouts/Ability_GKReflexes.png')
# imgAbility_GKAwareness = Image.open('./assets/scouts/Ability_GKAwareness.png')
# imgAbility_Dribbling = Image.open('./assets/scouts/Ability_Dribbling.png')
# imgAbility_Finishing = Image.open('./assets/scouts/Ability_Finishing.png')
# imgAbility_Heading = Image.open('./assets/scouts/Ability_Heading.png')
# imgAbility_PhysicalContact = Image.open('./assets/scouts/Ability_PhysicalContact.png')
# imgAbility_Curl = Image.open('./assets/scouts/Ability_Curl.png')
# imgAbility_Jump = Image.open('./assets/scouts/Ability_Jump.png')
# imgAbility_Leftfoot = Image.open('./assets/scouts/Ability_Leftfoot.png')
# imgAbility_DefensiveAwareness = Image.open('./assets/scouts/Ability_DefensiveAwareness.png')
# imgAbility_UtilityPlayers = Image.open('./assets/scouts/Ability_UtilityPlayers.png')
# imgAbility_Acceleration = Image.open('./assets/scouts/Ability_Acceleration.png')
# imgAbility_Speed = Image.open('./assets/scouts/Ability_Speed.png')
# imgAbility_Stamina = Image.open('./assets/scouts/Ability_Stamina.png')
# imgAbility_KickingPower = Image.open('./assets/scouts/Ability_KickingPower.png')
# imgAbility_185cmormore = Image.open('./assets/scouts/Ability_185cmormore.png')
# imgAbility_Rightfoot = Image.open('./assets/scouts/Ability_Rightfoot.png')
# imgPos_CF = Image.open('./assets/scouts/Pos_CF.png')
# imgPos_SS = Image.open('./assets/scouts/Pos_SS.png')
# imgPos_RWF = Image.open('./assets/scouts/Pos_RWF.png')
# imgPos_LWF = Image.open('./assets/scouts/Pos_LWF.png')
# imgPos_AMF = Image.open('./assets/scouts/Pos_AMF.png')
# imgPos_CMF = Image.open('./assets/scouts/Pos_CMF.png')
# imgPos_CB = Image.open('./assets/scouts/Pos_CB.png')
# imgPos_DMF = Image.open('./assets/scouts/Pos_DMF.png')
# imgPos_RMF = Image.open('./assets/scouts/Pos_RMF.png')
# imgPos_LMF = Image.open('./assets/scouts/Pos_LMF.png')
# imgPos_RB = Image.open('./assets/scouts/Pos_RB.png')
# imgPos_LB = Image.open('./assets/scouts/Pos_LB.png')
# imgLeague_French = Image.open('./assets/scouts/League_French.png')
# imgLeague_Italian = Image.open('./assets/scouts/League_Italian.png')
# imgLeague_English = Image.open('./assets/scouts/League_English.png')
# imgLeague_Spanish = Image.open('./assets/scouts/League_Spanish.png')
# imgLeague_Dutch = Image.open('./assets/scouts/League_Dutch.png')
# imgLeague_Argentinian = Image.open('./assets/scouts/League_Argentinian.png')
# imgLeague_Portuguese = Image.open('./assets/scouts/League_Portuguese.png')
# imgLeague_Brazilian = Image.open('./assets/scouts/League_Brazilian.png')
# imgLeague_Chiliean = Image.open('./assets/scouts/League_Chiliean.png')
# imgLeague_FreeAgent = Image.open('./assets/scouts/League_FreeAgent.png')
# imgLeague_OtherAsia = Image.open('./assets/scouts/League_OtherAsia.png')
# imgLeague_OtherLatinAmerica = Image.open('./assets/scouts/League_OtherLatinAmerica.png')
# imgLeague_OtherEurope = Image.open('./assets/scouts/League_OtherEurope.png')

imgArea_Americas = Image.open('./assets/scouts/Area_Americas.png')
imgArea_AsiaOceania = Image.open('./assets/scouts/Area_AsiaOceania.png')
imgArea_Europe = Image.open('./assets/scouts/Area_Europe.png')
imgLeague_Argentinian = Image.open('./assets/scouts/League_Argentinian.png')
imgLeague_Dutch = Image.open('./assets/scouts/League_Dutch.png')
imgLeague_French = Image.open('./assets/scouts/League_French.png')
imgLeague_Italian = Image.open('./assets/scouts/League_Italian.png')
imgLeague_OtherLatinAmerica = Image.open('./assets/scouts/League_OtherLatinAmerica.png')
imgPos_AMF = Image.open('./assets/scouts/Pos_AMF.png')

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
regionCF_SS_Hervey = (380, 275, 1800, 800)
regionCF_Jarvis = (380, 275, 1800, 800)
regionSquadContRen = (770, 409, 856, 453)
regionGP = (675, 558, 775, 663)
regionRenew = (1105, 590, 1290, 660)

regionScouts = [(240, 215, 752, 454), (240, 455, 752, 680), (240, 681, 752, 945)]

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
CF_SS_Hervey = button('CF_SS_Hervey', imgCF_SS_Hervey, regionCF_SS_Hervey)
CF_Jarvis = button('CF_Jarvis', imgCF_Jarvis, regionCF_Jarvis)
SquadContRen = button('SquadContRen', imgSquadContRen, regionSquadContRen)
gp = button('GP', imgGP, regionGP)
Renew = button('Renew', imgRenew, regionRenew)

i = 0

Star1 = button('1*', imgstar1, regionScouts)
Star2 = button('2*', imgstar2, regionScouts)
Star3 = button('3*', imgstar3, regionScouts)
# Star4 = button('4*', imgstar4, regionScouts)
# Star5 = button('5*', imgstar5, regionScouts)

# allNegotiationSkills = [Star1, Star2, Star3, Star4, Star5]

allNegotiationSkills = [Star1, Star2, Star3]


# Area_Europe = button('Area_Europe',imgArea_Europe, regionScouts)
# Area_Americas = button('Area_Americas',imgArea_Americas, regionScouts)
# Area_AsiaOceania = button('Area_AsiaOceania',imgArea_AsiaOceania, regionScouts)
# Area_Africa = button('Area_Africa',imgArea_Africa, regionScouts)
# Ability_LowPass = button('Ability_LowPass',imgAbility_LowPass, regionScouts)
# Ability_30plus = button('Ability_30plus',imgAbility_30plus, regionScouts)
# Ability_U24 = button('Ability_U24',imgAbility_U24, regionScouts)
# Ability_GKClearing = button('Ability_GKClearing',imgAbility_GKClearing, regionScouts)
# Ability_GKReach = button('Ability_GKReach',imgAbility_GKReach, regionScouts)
# Ability_GKCatching = button('Ability_GKCatching',imgAbility_GKCatching, regionScouts)
# Ability_LoftedPass = button('Ability_LoftedPass',imgAbility_LoftedPass, regionScouts)
# Ability_25to29yearold = button('Ability_25to29yearold',imgAbility_25to29yearold, regionScouts)
# Ability_OffensiveAwareness = button('Ability_OffensiveAwareness',imgAbility_OffensiveAwareness, regionScouts)
# Ability_PlaceKicking = button('Ability_PlaceKicking',imgAbility_PlaceKicking, regionScouts)
# Ability_BallWinning = button('Ability_BallWinning',imgAbility_BallWinning, regionScouts)
# Ability_BallControl = button('Ability_BallControl',imgAbility_BallControl, regionScouts)
# Ability_GKReflexes = button('Ability_GKReflexes',imgAbility_GKReflexes, regionScouts)
# Ability_GKAwareness = button('Ability_GKAwareness',imgAbility_GKAwareness, regionScouts)
# Ability_Dribbling = button('Ability_Dribbling',imgAbility_Dribbling, regionScouts)
# Ability_Finishing = button('Ability_Finishing',imgAbility_Finishing, regionScouts)
# Ability_Heading = button('Ability_Heading',imgAbility_Heading, regionScouts)
# Ability_PhysicalContact = button('Ability_PhysicalContact',imgAbility_PhysicalContact, regionScouts)
# Ability_Curl = button('Ability_Curl',imgAbility_Curl, regionScouts)
# Ability_Jump = button('Ability_Jump',imgAbility_Jump, regionScouts)
# Ability_Leftfoot = button('Ability_Leftfoot',imgAbility_Leftfoot, regionScouts)
# Ability_DefensiveAwareness = button('Ability_DefensiveAwareness',imgAbility_DefensiveAwareness, regionScouts)
# Ability_UtilityPlayers = button('Ability_UtilityPlayers',imgAbility_UtilityPlayers, regionScouts)
# Ability_Acceleration = button('Ability_Acceleration',imgAbility_Acceleration, regionScouts)
# Ability_Speed = button('Ability_Speed',imgAbility_Speed, regionScouts)
# Ability_Stamina = button('Ability_Stamina',imgAbility_Stamina, regionScouts)
# Ability_KickingPower = button('Ability_KickingPower',imgAbility_KickingPower, regionScouts)
# Ability_185cmormore = button('Ability_185cmormore',imgAbility_185cmormore, regionScouts)
# Ability_Rightfoot = button('Ability_Rightfoot',imgAbility_Rightfoot, regionScouts)
# Pos_CF = button('Pos_CF',imgPos_CF, regionScouts)
# Pos_SS = button('Pos_SS',imgPos_SS, regionScouts)
# Pos_RWF = button('Pos_RWF',imgPos_RWF, regionScouts)
# Pos_LWF = button('Pos_LWF',imgPos_LWF, regionScouts)
# Pos_AMF = button('Pos_AMF',imgPos_AMF, regionScouts)
# Pos_CMF = button('Pos_CMF',imgPos_CMF, regionScouts)
# Pos_CB = button('Pos_CB',imgPos_CB, regionScouts)
# Pos_DMF = button('Pos_DMF',imgPos_DMF, regionScouts)
# Pos_RMF = button('Pos_RMF',imgPos_RMF, regionScouts)
# Pos_LMF = button('Pos_LMF',imgPos_LMF, regionScouts)
# Pos_RB = button('Pos_RB',imgPos_RB, regionScouts)
# Pos_LB = button('Pos_LB',imgPos_LB, regionScouts)
# League_French = button('League_French',imgLeague_French, regionScouts)
# League_Italian = button('League_Italian',imgLeague_Italian, regionScouts)
# League_English = button('League_English',imgLeague_English, regionScouts)
# League_Spanish = button('League_Spanish',imgLeague_Spanish, regionScouts)
# League_Dutch = button('League_Dutch',imgLeague_Dutch, regionScouts)
# League_Argentinian = button('League_Argentinian',imgLeague_Argentinian, regionScouts)
# League_Portuguese = button('League_Portuguese',imgLeague_Portuguese, regionScouts)
# League_Brazilian = button('League_Brazilian',imgLeague_Brazilian, regionScouts)
# League_Chiliean = button('League_Chiliean',imgLeague_Chiliean, regionScouts)
# League_FreeAgent = button('League_FreeAgent',imgLeague_FreeAgent, regionScouts)
# League_OtherAsia = button('League_OtherAsia',imgLeague_OtherAsia, regionScouts)
# League_OtherLatinAmerica = button('League_OtherLatinAmerica',imgLeague_OtherLatinAmerica, regionScouts)
# League_OtherEurope = button('League_OtherEurope',imgLeague_OtherEurope, regionScouts)

# allScoutNames = [Area_Europe, Area_Americas, Area_AsiaOceania, Area_Africa, Ability_LowPass, Ability_30plus, Ability_U24, Ability_GKClearing, Ability_GKReach, Ability_GKCatching, Ability_LoftedPass, Ability_25to29yearold, Ability_OffensiveAwareness, Ability_PlaceKicking, Ability_BallWinning, Ability_BallControl, Ability_GKReflexes, Ability_GKAwareness, Ability_Dribbling, Ability_Finishing, Ability_Heading, Ability_PhysicalContact, Ability_Curl, Ability_Jump, Ability_Leftfoot, Ability_DefensiveAwareness, Ability_UtilityPlayers, Ability_Acceleration, Ability_Speed, Ability_Stamina, Ability_KickingPower, Ability_185cmormore, Ability_Rightfoot, Pos_CF, Pos_SS, Pos_RWF, Pos_LWF, Pos_AMF, Pos_CMF, Pos_CB, Pos_DMF, Pos_RMF, Pos_LMF, Pos_RB, Pos_LB, League_French, League_Italian, League_English, League_Spanish, League_Dutch, League_Argentinian, League_Portuguese, League_Brazilian, League_Chiliean, League_FreeAgent, League_OtherAsia, League_OtherLatinAmerica, League_OtherEurope]

League_Italian = button('League_Italian',imgLeague_Italian, regionScouts)
League_French = button('League_French',imgLeague_French, regionScouts)
League_Dutch = button('League_Dutch',imgLeague_Dutch, regionScouts)
League_Argentinian = button('League_Argentinian',imgLeague_Argentinian, regionScouts)
Area_Europe = button('Area_Europe',imgArea_Europe, regionScouts)
Area_Americas = button('Area_Americas',imgArea_Americas, regionScouts)
Area_AsiaOceania = button('Area_AsiaOceania',imgArea_AsiaOceania, regionScouts)
Pos_AMF = button('Pos_AMF',imgPos_AMF, regionScouts)

allScoutNames = [Pos_AMF, Area_AsiaOceania, Area_Americas, Area_Europe, League_Argentinian, League_Dutch, League_French, League_Italian]

a = (600, 350)              #       a       #              b
b = (1200, 350)             #               #
c = (600, 575)              #       c       #              d
d = (1200, 575)             #               #
e = (600, 800)              #       e       #              f
f = (1200, 800)
selectButtonPosition = (1200, 1010)
actionButtonPosition = (1200, 1010)

squad1 = (selectButtonPosition, d, e, 1, a, b, c, d, e, f, 1, b, c, f, actionButtonPosition)
squad2 = (selectButtonPosition, d, f, 1, a, b, c, d, e, f, 1, b, d, e, actionButtonPosition)
scoutPositions = (a, c, e)


def print2Both(text):
    print(text)
    f.write(text+'\n')

f = open('./logs/log.txt', 'a')

def lt():
    print2Both('\n\n------------------------------------------------------------\n\n')
    print2Both(time.ctime()+'\n\n\n')

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
            time.sleep(waitAfterClick)
            point = pyg.locateCenterOnScreen(bt.img, region=bt.region, confidence=.98)
    elif(point):
        print2Both("ClickLoop: Found "+bt.name)
        pyg.mouseDown(point)
        time.sleep(2)
        pyg.mouseUp()
        print2Both("ClickLoop: Clicked "+bt.name + " and now waiting " + str(waitAfterClick)+" seconds and before moving on")
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


def scrollDownSlow(pages=1):
    while(pages):
        pyg.mouseDown(50, 917)
        time.sleep(1)
        pyg.moveTo(50, 228, duration=3)
        time.sleep(2)
        pyg.mouseUp()
        time.sleep(1)
        pages = pages-1


def select(squad):
    for i in squad:
        if(i == 1):
            scrollDownSlow()
            continue
        clickOnPoint(i)


def renew(squad):
    while(True):
        lt()
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
    global wait
    wait = 10
    click(SquadNotFine, True, wait)
    click(Juve, True, wait)
    click(SwitchSquad, True, wait)

    while(True):
        if(check(SwitchTo1)):
            click(SwitchTo1, True, wait)
            break
        elif(check(SwitchTo2)):
            click(SwitchTo2, True, wait)
            break

    click(Confirm, True, wait)
    click(ok, True, wait)
    click(Back, True, wait)


def autosim():
    lt()
    print2Both("Starting AutoSim in 5 seconds\n\n")
    time.sleep(5)

    while(1):
        lt()
        waitForOneHalf = 150
        wait = 4
        click(ok, False, wait)
        click(secondHalf, False, waitForOneHalf)
        click(Next, False, wait)
        click(Confirm, False, waitForOneHalf)
        click(Proceed, False, wait)
        click(Retry, False, wait)
        click(Sign, False, wait)

        if(check(SquadNotFine)):
            if(check(ok)):
                click(ok, True, wait)
            snfSwitch()

        click(ToMatch, False, 10)

        if(check(SquadNotFine)):
            if(check(ok)):
                click(ok, True, wait)
            snfSwitch()


def ContRen():
    lt()
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
    lt()
    print2Both("\n\nContracts Maxxed out.....Aborting\n\n")


def selectScouts(pages):
    scrollDownSlow(pages)
    while(True):
        select(scoutPositions)
        scrollDownSlow()


def start():
    global task
    if(not restarting):
        lt()
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
        totalNumber = int(input("Enter total number of Scouts  (Must be atleast 3) : "))
        analyzeScouts(totalNumber)


def printException(exception,shouldRestart):
    global restarting
    restarting = shouldRestart
    lt()
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

def checkInRow(bt, row):
    print2Both('CheckLoop: Checking for '+bt.name+'in row no. '+str(row+1))
    point = pyg.locateCenterOnScreen(bt.img, region=bt.region[row], confidence=.98)

    if(point):
        print2Both("CheckLoop: Found "+bt.name+'in row no. '+str(row+1))
        return bt.name
    else:
        print2Both("CheckLoop: Couldn't find "+bt.name+'in row no. '+str(row+1))
        return None


def findScounts(allSkillOrNameScouts):
    threeSkillOrNameScouts=[]
    for row in range(3):
        for j in allSkillOrNameScouts:
            if(name:=checkInRow(j, row)):
                threeSkillOrNameScouts.append(name)
                break
            else:
                threeSkillOrNameScouts.append('New')
    return threeSkillOrNameScouts


def scountsFromOnePage():
    global scouts
    scouts = []
    threeNegotiationSkills = findScounts(allNegotiationSkills)
    threeScoutNames = findScounts(allScoutNames)

    for i in range(scoutsCountedTwice, 3):
        scouts.append([threeNegotiationSkills[i], threeScoutNames[i]])

def analyzeScouts(totalNumber):
    global i
    global scoutsCountedTwice
    scoutsCountedTwice = 0
    isFinalPage = False

    while(totalNumber>0):
        if totalNumber<3:
            scoutsCountedTwice = 3 - totalNumber
            isFinalPage = True

        scountsFromOnePage()

        if not isFinalPage:
            scrollDownSlow()
            time.sleep(3)

        totalNumber-=3
    print2Both(scouts)



restarting = False
run()
f.close()