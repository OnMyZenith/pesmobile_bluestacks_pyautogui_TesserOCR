import pyautogui as pyg
import time
from PIL import Image
import os

pyg.PAUSE = 0
pyg.FAILSAFE = True

folder = time.strftime("%Y-%m-%d %H'%M''%S",time.localtime())
path = './logs/'+folder
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
imgCF_SS_Hervey = Image.open('./assets/CF_SS_Hervey.png')
imgCF_Jarvis = Image.open('./assets/CF_Jarvis.png')
imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgGP = Image.open('./assets/GP.png')
imgRenew = Image.open('./assets/Renew.png')

imgStar1 = Image.open('./assets/scouts/Star1.png')
imgStar2 = Image.open('./assets/scouts/Star2.png')
imgStar3 = Image.open('./assets/scouts/Star3.png')
imgStar4 = Image.open('./assets/scouts/Star4.png')
imgStar5 = Image.open('./assets/scouts/Star5.png')

imgAbility_185cmormore = Image.open('./assets/scouts/Ability_185cmormore.png')
imgAbility_25to29yearold = Image.open('./assets/scouts/Ability_25to29yearold.png')
imgAbility_30plus = Image.open('./assets/scouts/Ability_30plus.png')
imgAbility_Acceleration = Image.open('./assets/scouts/Ability_Acceleration.png')
imgAbility_BallControl = Image.open('./assets/scouts/Ability_BallControl.png')
imgAbility_BallWinning = Image.open('./assets/scouts/Ability_BallWinning.png')
imgAbility_Curl = Image.open('./assets/scouts/Ability_Curl.png')
imgAbility_DefensiveAwareness = Image.open('./assets/scouts/Ability_DefensiveAwareness.png')
imgAbility_Dribbling = Image.open('./assets/scouts/Ability_Dribbling.png')
imgAbility_Finishing = Image.open('./assets/scouts/Ability_Finishing.png')
imgAbility_GKAwareness = Image.open('./assets/scouts/Ability_GKAwareness.png')
imgAbility_GKCatching = Image.open('./assets/scouts/Ability_GKCatching.png')
imgAbility_GKClearing = Image.open('./assets/scouts/Ability_GKClearing.png')
imgAbility_GKReach = Image.open('./assets/scouts/Ability_GKReach.png')
imgAbility_GKReflexes = Image.open('./assets/scouts/Ability_GKReflexes.png')
imgAbility_Heading = Image.open('./assets/scouts/Ability_Heading.png')
imgAbility_Jump = Image.open('./assets/scouts/Ability_Jump.png')
imgAbility_KickingPower = Image.open('./assets/scouts/Ability_KickingPower.png')
imgAbility_Leftfoot = Image.open('./assets/scouts/Ability_Leftfoot.png')
imgAbility_LoftedPass = Image.open('./assets/scouts/Ability_LoftedPass.png')
imgAbility_LowPass = Image.open('./assets/scouts/Ability_LowPass.png')
imgAbility_OffensiveAwareness = Image.open('./assets/scouts/Ability_OffensiveAwareness.png')
imgAbility_PhysicalContact = Image.open('./assets/scouts/Ability_PhysicalContact.png')
imgAbility_PlaceKicking = Image.open('./assets/scouts/Ability_PlaceKicking.png')
imgAbility_Rightfoot = Image.open('./assets/scouts/Ability_Rightfoot.png')
imgAbility_Speed = Image.open('./assets/scouts/Ability_Speed.png')
imgAbility_Stamina = Image.open('./assets/scouts/Ability_Stamina.png')
imgAbility_U24 = Image.open('./assets/scouts/Ability_U24.png')
imgArea_Africa = Image.open('./assets/scouts/Area_Africa.png')
imgArea_Americas = Image.open('./assets/scouts/Area_Americas.png')
imgArea_AsiaOceania = Image.open('./assets/scouts/Area_AsiaOceania.png')
imgArea_Europe = Image.open('./assets/scouts/Area_Europe.png')
imgLeague_Argentinian = Image.open('./assets/scouts/League_Argentinian.png')
imgLeague_Brazilian = Image.open('./assets/scouts/League_Brazilian.png')
imgLeague_Chiliean = Image.open('./assets/scouts/League_Chiliean.png')
imgLeague_Dutch = Image.open('./assets/scouts/League_Dutch.png')
imgLeague_English = Image.open('./assets/scouts/League_English.png')
imgLeague_FreeAgent = Image.open('./assets/scouts/League_FreeAgent.png')
imgLeague_French = Image.open('./assets/scouts/League_French.png')
imgLeague_Italian = Image.open('./assets/scouts/League_Italian.png')
imgLeague_OtherAsia = Image.open('./assets/scouts/League_OtherAsia.png')
imgLeague_OtherEurope = Image.open('./assets/scouts/League_OtherEurope.png')
imgLeague_OtherLatinAmerica = Image.open('./assets/scouts/League_OtherLatinAmerica.png')
imgLeague_Portuguese = Image.open('./assets/scouts/League_Portuguese.png')
imgLeague_Spanish = Image.open('./assets/scouts/League_Spanish.png')
imgPos_AMF = Image.open('./assets/scouts/Pos_AMF.png')
imgPos_CB = Image.open('./assets/scouts/Pos_CB.png')
imgPos_CF = Image.open('./assets/scouts/Pos_CF.png')
imgPos_CMF = Image.open('./assets/scouts/Pos_CMF.png')
imgPos_DMF = Image.open('./assets/scouts/Pos_DMF.png')
imgPos_LB = Image.open('./assets/scouts/Pos_LB.png')
imgPos_LMF = Image.open('./assets/scouts/Pos_LMF.png')
imgPos_LWF = Image.open('./assets/scouts/Pos_LWF.png')
imgPos_RB = Image.open('./assets/scouts/Pos_RB.png')
imgPos_RMF = Image.open('./assets/scouts/Pos_RMF.png')
imgPos_RWF = Image.open('./assets/scouts/Pos_RWF.png')
imgPos_SS = Image.open('./assets/scouts/Pos_SS.png')
imgPos_UtilityPlayers = Image.open('./assets/scouts/Pos_UtilityPlayers.png')
imgFavouriteTactics = Image.open('./assets/scouts/FavouriteTactics.png')

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

regionNegotiationSkills = [(275, 225, 400, 370), (275, 455, 400, 600), (275, 685, 400, 830)]
regionScoutNames = [(425, 240, 750, 450), (425, 470, 750, 680), (425, 700, 750, 910)]

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

Star1 = button('1*', imgStar1, regionNegotiationSkills)
Star2 = button('2*', imgStar2, regionNegotiationSkills)
Star3 = button('3*', imgStar3, regionNegotiationSkills)
Star4 = button('4*', imgStar4, regionNegotiationSkills)
Star5 = button('5*', imgStar5, regionNegotiationSkills)

allNegotiationSkills = [Star1, Star2, Star3, Star4, Star5]


Ability_185cmormore = button('Ability_185cmormore',imgAbility_185cmormore, regionScoutNames)
Ability_25to29yearold = button('Ability_25to29yearold',imgAbility_25to29yearold, regionScoutNames)
Ability_30plus = button('Ability_30plus',imgAbility_30plus, regionScoutNames)
Ability_Acceleration = button('Ability_Acceleration',imgAbility_Acceleration, regionScoutNames)
Ability_BallControl = button('Ability_BallControl',imgAbility_BallControl, regionScoutNames)
Ability_BallWinning = button('Ability_BallWinning',imgAbility_BallWinning, regionScoutNames)
Ability_Curl = button('Ability_Curl',imgAbility_Curl, regionScoutNames)
Ability_DefensiveAwareness = button('Ability_DefensiveAwareness',imgAbility_DefensiveAwareness, regionScoutNames)
Ability_Dribbling = button('Ability_Dribbling',imgAbility_Dribbling, regionScoutNames)
Ability_Finishing = button('Ability_Finishing',imgAbility_Finishing, regionScoutNames)
Ability_GKAwareness = button('Ability_GKAwareness',imgAbility_GKAwareness, regionScoutNames)
Ability_GKCatching = button('Ability_GKCatching',imgAbility_GKCatching, regionScoutNames)
Ability_GKClearing = button('Ability_GKClearing',imgAbility_GKClearing, regionScoutNames)
Ability_GKReach = button('Ability_GKReach',imgAbility_GKReach, regionScoutNames)
Ability_GKReflexes = button('Ability_GKReflexes',imgAbility_GKReflexes, regionScoutNames)
Ability_Heading = button('Ability_Heading',imgAbility_Heading, regionScoutNames)
Ability_Jump = button('Ability_Jump',imgAbility_Jump, regionScoutNames)
Ability_KickingPower = button('Ability_KickingPower',imgAbility_KickingPower, regionScoutNames)
Ability_Leftfoot = button('Ability_Leftfoot',imgAbility_Leftfoot, regionScoutNames)
Ability_LoftedPass = button('Ability_LoftedPass',imgAbility_LoftedPass, regionScoutNames)
Ability_LowPass = button('Ability_LowPass',imgAbility_LowPass, regionScoutNames)
Ability_OffensiveAwareness = button('Ability_OffensiveAwareness',imgAbility_OffensiveAwareness, regionScoutNames)
Ability_PhysicalContact = button('Ability_PhysicalContact',imgAbility_PhysicalContact, regionScoutNames)
Ability_PlaceKicking = button('Ability_PlaceKicking',imgAbility_PlaceKicking, regionScoutNames)
Ability_Rightfoot = button('Ability_Rightfoot',imgAbility_Rightfoot, regionScoutNames)
Ability_Speed = button('Ability_Speed',imgAbility_Speed, regionScoutNames)
Ability_Stamina = button('Ability_Stamina',imgAbility_Stamina, regionScoutNames)
Ability_U24 = button('Ability_U24',imgAbility_U24, regionScoutNames)
Area_Africa = button('Area_Africa',imgArea_Africa, regionScoutNames)
Area_Americas = button('Area_Americas',imgArea_Americas, regionScoutNames)
Area_AsiaOceania = button('Area_AsiaOceania',imgArea_AsiaOceania, regionScoutNames)
Area_Europe = button('Area_Europe',imgArea_Europe, regionScoutNames)
League_Argentinian = button('League_Argentinian',imgLeague_Argentinian, regionScoutNames)
League_Brazilian = button('League_Brazilian',imgLeague_Brazilian, regionScoutNames)
League_Chiliean = button('League_Chiliean',imgLeague_Chiliean, regionScoutNames)
League_Dutch = button('League_Dutch',imgLeague_Dutch, regionScoutNames)
League_English = button('League_English',imgLeague_English, regionScoutNames)
League_FreeAgent = button('League_FreeAgent',imgLeague_FreeAgent, regionScoutNames)
League_French = button('League_French',imgLeague_French, regionScoutNames)
League_Italian = button('League_Italian',imgLeague_Italian, regionScoutNames)
League_OtherAsia = button('League_OtherAsia',imgLeague_OtherAsia, regionScoutNames)
League_OtherEurope = button('League_OtherEurope',imgLeague_OtherEurope, regionScoutNames)
League_OtherLatinAmerica = button('League_OtherLatinAmerica',imgLeague_OtherLatinAmerica, regionScoutNames)
League_Portuguese = button('League_Portuguese',imgLeague_Portuguese, regionScoutNames)
League_Spanish = button('League_Spanish',imgLeague_Spanish, regionScoutNames)
Pos_AMF = button('Pos_AMF',imgPos_AMF, regionScoutNames)
Pos_CB = button('Pos_CB',imgPos_CB, regionScoutNames)
Pos_CF = button('Pos_CF',imgPos_CF, regionScoutNames)
Pos_CMF = button('Pos_CMF',imgPos_CMF, regionScoutNames)
Pos_DMF = button('Pos_DMF',imgPos_DMF, regionScoutNames)
Pos_LB = button('Pos_LB',imgPos_LB, regionScoutNames)
Pos_LMF = button('Pos_LMF',imgPos_LMF, regionScoutNames)
Pos_LWF = button('Pos_LWF',imgPos_LWF, regionScoutNames)
Pos_RB = button('Pos_RB',imgPos_RB, regionScoutNames)
Pos_RMF = button('Pos_RMF',imgPos_RMF, regionScoutNames)
Pos_RWF = button('Pos_RWF',imgPos_RWF, regionScoutNames)
Pos_SS = button('Pos_SS',imgPos_SS, regionScoutNames)
Pos_UtilityPlayers = button('Pos_UtilityPlayers',imgPos_UtilityPlayers, regionScoutNames)
FavouriteTactics = button('FavouriteTactics',imgFavouriteTactics, regionScoutNames)

allScoutNames = [FavouriteTactics, Ability_185cmormore, Ability_25to29yearold, Ability_30plus, Ability_Acceleration, Ability_BallControl, Ability_BallWinning, Ability_Curl, Ability_DefensiveAwareness, Ability_Dribbling, Ability_Finishing, Ability_GKAwareness, Ability_GKCatching, Ability_GKClearing, Ability_GKReach, Ability_GKReflexes, Ability_Heading, Ability_Jump, Ability_KickingPower, Ability_Leftfoot, Ability_LoftedPass, Ability_LowPass, Ability_OffensiveAwareness, Ability_PhysicalContact, Ability_PlaceKicking, Ability_Rightfoot, Ability_Speed, Ability_Stamina, Ability_U24, Area_Africa, Area_Americas, Area_AsiaOceania, Area_Europe, League_Argentinian, League_Brazilian, League_Chiliean, League_Dutch, League_English, League_FreeAgent, League_French, League_Italian, League_OtherAsia, League_OtherEurope, League_OtherLatinAmerica, League_Portuguese, League_Spanish, Pos_AMF, Pos_CB, Pos_CF, Pos_CMF, Pos_DMF, Pos_LB, Pos_LMF, Pos_LWF, Pos_RB, Pos_RMF, Pos_RWF, Pos_SS, Pos_UtilityPlayers]

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
    f.write(str(text)+'\n')


f = open(path +'/log.txt', 'a')

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
    print2Both("\nException Occurred\n")
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

def findScounts(allSkillOrNameScouts):
    threeSkillOrNameScouts=[]
    for i in range(3):
        foundButton = False
        for j in allSkillOrNameScouts:
            if(name:=checkInRow(j, i)):
                threeSkillOrNameScouts.append(name)
                foundButton = True
                break

        if not foundButton:
            threeSkillOrNameScouts.append('new')
        
        print2Both("\nFinished with box "+str(i+1)+"\n")
        if i <2:
            print2Both("Currently on Page no. :"+str(page+1)+" out of "+str(int(number/3+0.7))+'\n')
    return threeSkillOrNameScouts


def scountsFromOnePage():
    global scouts
    global page
    threeNegotiationSkills = findScounts(allNegotiationSkills)
    threeScoutNames = findScounts(allScoutNames)

    # while True:
    #     try:
    #         pos = threeScoutNames.index('FavouriteTactics')
    #         threeScoutNames.pop(pos)
    #         threeNegotiationSkills.pop(pos)
    #         clickOnPoint(scoutPositions[pos])
    #     except ValueError:
    #         break
    
    page+=1

    for i in range(scoutsCountedTwice, len(threeScoutNames)):
        scouts.append([threeNegotiationSkills[i], threeScoutNames[i], page])
        
    print2Both("Finished with Page no. :"+str(page)+" out of "+str(int(number/3+0.7)))

    print2Both("\n\nScouts identified on Page :\n")
    for i in range(len(threeScoutNames)-scoutsCountedTwice):
        print2Both("\n\t"+str(scouts[3*page-3+i]))

    lt()
    time.sleep(1)
    pyg.screenshot(path+'/Page'+str(page)+'.png')

def analyzeScouts(totalNumber):
    time1= time.time()
    global number
    global scoutsCountedTwice
    global scouts
    global page
    page=0
    number = totalNumber
    scouts = []
    scoutsCountedTwice = 0
    isFinalPage = False

    while(totalNumber>0):
        if totalNumber<=3:
            scoutsCountedTwice = 3 - totalNumber
            isFinalPage = True

        scountsFromOnePage()

        if not isFinalPage:
            scrollDownSlow()
            time.sleep(2)

        totalNumber-=3
    lt()
    print2Both('Time taken to analyze '+str(number)+' scouts : '+str(int((time.time()-time1)/60))+' minutes and '+str(int((time.time()-time1)%60))+' seconds.')
    print2Both("\n\nTotal Scouts :"+str(scouts)+"\n\n")

    f = open(path +'/scouts.txt', 'a')
    for i in range(number):
        f.write(str(scouts[i][0])+', '+str(scouts[i][1])+"\n")
    f.close()
    

def checkInRow(bt, row):
    print2Both('Checking for '+bt.name+'in box '+str(row+1)+str(bt.region[row]))
    point = pyg.locateCenterOnScreen(bt.img, region=bt.region[row] , confidence=.98)

    if(point):
        print2Both("Found "+bt.name+'in box '+str(row+1)+str(bt.region[row]))
        return bt.name
    else:
        print2Both("Couldn't find "+bt.name+'in box '+str(row+1)+str(bt.region[row]))
        return None

restarting = False
run()
f.close()