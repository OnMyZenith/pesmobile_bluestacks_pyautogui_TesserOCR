import pyautogui as pyg
import time
from PIL import Image
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
imgCF_SS_Hervey = Image.open('./assets/CF_SS_Hervey.png')
imgCF_Jarvis = Image.open('./assets/CF_Jarvis.png')
imgSquadContRen = Image.open('./assets/SquadContRen.png')
imgGP = Image.open('./assets/GP.png')
imgRenew = Image.open('./assets/Renew.png')

imgAge_25to29yearold = Image.open('./assets/scouts/Age_25to29yearold.png')
imgAge_30plus = Image.open('./assets/scouts/Age_30plus.png')
imgAge_U24 = Image.open('./assets/scouts/Age_U24.png')
imgArea_Africa = Image.open('./assets/scouts/Area_Africa.png')
imgArea_Americas = Image.open('./assets/scouts/Area_Americas.png')
imgArea_AsiaOceania = Image.open('./assets/scouts/Area_AsiaOceania.png')
imgArea_Europe = Image.open('./assets/scouts/Area_Europe.png')
imgFavouriteTactics_ = Image.open('./assets/scouts/FavouriteTactics_.png')
imgHeight_185cmormore = Image.open('./assets/scouts/Height_185cmormore.png')
imgKeyAttributes_Acceleration = Image.open('./assets/scouts/KeyAttributes_Acceleration.png')
imgKeyAttributes_BallControl = Image.open('./assets/scouts/KeyAttributes_BallControl.png')
imgKeyAttributes_BallWinning = Image.open('./assets/scouts/KeyAttributes_BallWinning.png')
imgKeyAttributes_Curl = Image.open('./assets/scouts/KeyAttributes_Curl.png')
imgKeyAttributes_DefensiveAwareness = Image.open('./assets/scouts/KeyAttributes_DefensiveAwareness.png')
imgKeyAttributes_Dribbling = Image.open('./assets/scouts/KeyAttributes_Dribbling.png')
imgKeyAttributes_Finishing = Image.open('./assets/scouts/KeyAttributes_Finishing.png')
imgKeyAttributes_GKAwareness = Image.open('./assets/scouts/KeyAttributes_GKAwareness.png')
imgKeyAttributes_GKCatching = Image.open('./assets/scouts/KeyAttributes_GKCatching.png')
imgKeyAttributes_GKClearing = Image.open('./assets/scouts/KeyAttributes_GKClearing.png')
imgKeyAttributes_GKReach = Image.open('./assets/scouts/KeyAttributes_GKReach.png')
imgKeyAttributes_GKReflexes = Image.open('./assets/scouts/KeyAttributes_GKReflexes.png')
imgKeyAttributes_Heading = Image.open('./assets/scouts/KeyAttributes_Heading.png')
imgKeyAttributes_Jump = Image.open('./assets/scouts/KeyAttributes_Jump.png')
imgKeyAttributes_KickingPower = Image.open('./assets/scouts/KeyAttributes_KickingPower.png')
imgKeyAttributes_LoftedPass = Image.open('./assets/scouts/KeyAttributes_LoftedPass.png')
imgKeyAttributes_LowPass = Image.open('./assets/scouts/KeyAttributes_LowPass.png')
imgKeyAttributes_OffensiveAwareness = Image.open('./assets/scouts/KeyAttributes_OffensiveAwareness.png')
imgKeyAttributes_PhysicalContact = Image.open('./assets/scouts/KeyAttributes_PhysicalContact.png')
imgKeyAttributes_PlaceKicking = Image.open('./assets/scouts/KeyAttributes_PlaceKicking.png')
imgKeyAttributes_Speed = Image.open('./assets/scouts/KeyAttributes_Speed.png')
imgKeyAttributes_Stamina = Image.open('./assets/scouts/KeyAttributes_Stamina.png')
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
imgStrongerFoot_Left = Image.open('./assets/scouts/StrongerFoot_Left.png')
imgStrongerFoot_Right = Image.open('./assets/scouts/StrongerFoot_Right.png')

imgFavouriteTactics = Image.open('./assets/scouts/FavouriteTactics.png')
imgLeague = Image.open('./assets/scouts/League.png')
imgArea = Image.open('./assets/scouts/Area.png')
imgPos = Image.open('./assets/scouts/Pos.png')
imgKeyAttributes = Image.open('./assets/scouts/KeyAttributes.png')
imgAge = Image.open('./assets/scouts/Age.png')
imgHeight = Image.open('./assets/scouts/Height.png')
imgStrongerFoot = Image.open('./assets/scouts/StrongerFoot.png')

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
regionCF_SS_Hervey = (380, 275, 1800, 800)
regionCF_Jarvis = (380, 275, 1800, 800)
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
regionScoutNames = [(425, 240, 750, 450), (425, 470, 750, 680), (425, 700, 750, 910)]

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
CF_SS_Hervey = button('CF_SS_Hervey', imgCF_SS_Hervey, regionCF_SS_Hervey)
CF_Jarvis = button('CF_Jarvis', imgCF_Jarvis, regionCF_Jarvis)
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

Age_25to29yearold = button('Age_25to29yearold',imgAge_25to29yearold, regionScoutNames)
Age_30plus = button('Age_30plus',imgAge_30plus, regionScoutNames)
Age_U24 = button('Age_U24',imgAge_U24, regionScoutNames)
Area_Africa = button('Area_Africa',imgArea_Africa, regionScoutNames)
Area_Americas = button('Area_Americas',imgArea_Americas, regionScoutNames)
Area_AsiaOceania = button('Area_AsiaOceania',imgArea_AsiaOceania, regionScoutNames)
Area_Europe = button('Area_Europe',imgArea_Europe, regionScoutNames)
FavouriteTactics_ = button('FavouriteTactics_',imgFavouriteTactics_, regionScoutNames)
Height_185cmormore = button('Height_185cmormore',imgHeight_185cmormore, regionScoutNames)
KeyAttributes_Acceleration = button('KeyAttributes_Acceleration',imgKeyAttributes_Acceleration, regionScoutNames)
KeyAttributes_BallControl = button('KeyAttributes_BallControl',imgKeyAttributes_BallControl, regionScoutNames)
KeyAttributes_BallWinning = button('KeyAttributes_BallWinning',imgKeyAttributes_BallWinning, regionScoutNames)
KeyAttributes_Curl = button('KeyAttributes_Curl',imgKeyAttributes_Curl, regionScoutNames)
KeyAttributes_DefensiveAwareness = button('KeyAttributes_DefensiveAwareness',imgKeyAttributes_DefensiveAwareness, regionScoutNames)
KeyAttributes_Dribbling = button('KeyAttributes_Dribbling',imgKeyAttributes_Dribbling, regionScoutNames)
KeyAttributes_Finishing = button('KeyAttributes_Finishing',imgKeyAttributes_Finishing, regionScoutNames)
KeyAttributes_GKAwareness = button('KeyAttributes_GKAwareness',imgKeyAttributes_GKAwareness, regionScoutNames)
KeyAttributes_GKCatching = button('KeyAttributes_GKCatching',imgKeyAttributes_GKCatching, regionScoutNames)
KeyAttributes_GKClearing = button('KeyAttributes_GKClearing',imgKeyAttributes_GKClearing, regionScoutNames)
KeyAttributes_GKReach = button('KeyAttributes_GKReach',imgKeyAttributes_GKReach, regionScoutNames)
KeyAttributes_GKReflexes = button('KeyAttributes_GKReflexes',imgKeyAttributes_GKReflexes, regionScoutNames)
KeyAttributes_Heading = button('KeyAttributes_Heading',imgKeyAttributes_Heading, regionScoutNames)
KeyAttributes_Jump = button('KeyAttributes_Jump',imgKeyAttributes_Jump, regionScoutNames)
KeyAttributes_KickingPower = button('KeyAttributes_KickingPower',imgKeyAttributes_KickingPower, regionScoutNames)
KeyAttributes_LoftedPass = button('KeyAttributes_LoftedPass',imgKeyAttributes_LoftedPass, regionScoutNames)
KeyAttributes_LowPass = button('KeyAttributes_LowPass',imgKeyAttributes_LowPass, regionScoutNames)
KeyAttributes_OffensiveAwareness = button('KeyAttributes_OffensiveAwareness',imgKeyAttributes_OffensiveAwareness, regionScoutNames)
KeyAttributes_PhysicalContact = button('KeyAttributes_PhysicalContact',imgKeyAttributes_PhysicalContact, regionScoutNames)
KeyAttributes_PlaceKicking = button('KeyAttributes_PlaceKicking',imgKeyAttributes_PlaceKicking, regionScoutNames)
KeyAttributes_Speed = button('KeyAttributes_Speed',imgKeyAttributes_Speed, regionScoutNames)
KeyAttributes_Stamina = button('KeyAttributes_Stamina',imgKeyAttributes_Stamina, regionScoutNames)
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
StrongerFoot_Left = button('StrongerFoot_Left',imgStrongerFoot_Left, regionScoutNames)
StrongerFoot_Right = button('StrongerFoot_Right',imgStrongerFoot_Right, regionScoutNames)

FavouriteTacticsList = [FavouriteTactics_]
AreaList = [Area_Africa, Area_Americas, Area_AsiaOceania, Area_Europe]
LeagueList = [League_Argentinian, League_Brazilian, League_Chiliean, League_Dutch, League_English, League_FreeAgent, League_French, League_Italian, League_OtherAsia, League_OtherEurope, League_OtherLatinAmerica, League_Portuguese, League_Spanish]
AgeList = [Age_U24, Age_25to29yearold, Age_30plus]
HeightList = [Height_185cmormore]
PosList = [Pos_AMF, Pos_CB, Pos_CF, Pos_CMF, Pos_DMF, Pos_LB, Pos_LMF, Pos_LWF, Pos_RB, Pos_RMF, Pos_RWF, Pos_SS, Pos_UtilityPlayers]
StrongerFootList = [StrongerFoot_Left, StrongerFoot_Right]
KeyAttributesList = [KeyAttributes_Acceleration, KeyAttributes_BallControl, KeyAttributes_BallWinning, KeyAttributes_Curl, KeyAttributes_DefensiveAwareness, KeyAttributes_Dribbling, KeyAttributes_Finishing, KeyAttributes_GKAwareness, KeyAttributes_GKCatching, KeyAttributes_GKClearing, KeyAttributes_GKReach, KeyAttributes_GKReflexes, KeyAttributes_Heading, KeyAttributes_Jump, KeyAttributes_KickingPower, KeyAttributes_LoftedPass, KeyAttributes_LowPass, KeyAttributes_OffensiveAwareness, KeyAttributes_PhysicalContact, KeyAttributes_PlaceKicking, KeyAttributes_Speed, KeyAttributes_Stamina]

FavouriteTactics = button(FavouriteTacticsList,imgFavouriteTactics, regionScoutNames)
League = button(LeagueList,imgLeague, regionScoutNames)
Area = button(AreaList,imgArea, regionScoutNames)
Pos = button(PosList,imgPos, regionScoutNames)
KeyAttributes = button(KeyAttributesList,imgKeyAttributes, regionScoutNames)
Age = button(AgeList,imgAge, regionScoutNames)
Height = button(HeightList,imgHeight, regionScoutNames)
StrongerFoot = button(StrongerFootList,imgStrongerFoot, regionScoutNames)

allScoutCategories = [FavouriteTactics, League, Area, Pos, KeyAttributes, Age, Height, StrongerFoot]

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
    waitForOneHalf = 150
    matchNumber  = 0
    lt()
    print2Both("Starting AutoSim in 5 seconds\n\n")
    time.sleep(5)

    while(1):
        lt()

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

        changedMatchNumber = False

        if check(ToMatch):
            matchNumber += 1
            changedMatchNumber = True
            pyg.screenshot('./logs/MatchScreenshots/'+folderName+'MatchNumber_'+str(matchNumber)+'_1.png')
            print2Both("Took a Screenshot of Campaign Summary")
            click(ToMatch, False, waitLong)     #Wait 10 secs for SNF and OK to show up if thery're going to
            time.sleep(15)                      #Wait 10 secs for Matchmaking to Finish
            pyg.screenshot('./logs/MatchScreenshots/'+folderName+'MatchNumber_'+str(matchNumber)+'_2.png')
            print2Both("Took a Screenshot of Matchmaking")

        if check(SquadNotFine):
            if changedMatchNumber:
                os.remove('./logs/MatchScreenshots/'+folderName+'MatchNumber_'+str(matchNumber)+'_1.png')
                os.remove('./logs/MatchScreenshots/'+folderName+'MatchNumber_'+str(matchNumber)+'_2.png')
                matchNumber -= 1
            if(check(ok)):
                click(ok, True, waitLong)
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
        numberOfScoutsLeft = int(input("Enter total number of Scouts  (Must be atleast 3) : "))
        analyzeScouts(numberOfScoutsLeft)


def printException(exception,shouldRestart):
    global restarting
    restarting = shouldRestart
    print2Both("\n\nException Occurred\n")
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

def avoidErrorRecursive(a,b,c):
    global found
    global gotOSError
    try:
        if pyg.pixelMatchesColor(a, b, c):
            found = True
    except OSError:
        gotOSError+=1
        avoidErrorRecursive(a,b,c)

def addScoutsOfPage():
    global scouts
    global page
    global found
    threeScoutNames=[]
    threeNegotiationSkills = []

# ############################
#     try:
#         pyg.pixel(10,10)
#     except OSError:
#         pass
# ############################

    for i in range(3):
        foundOneHalfOfOneScout = None
        foundCategory = None

        for j in allScoutCategories:
            if(foundCategory:=checkInRow(j, i)):
                break

        if foundCategory:
            for j in foundCategory:
                print(j)
                if(foundOneHalfOfOneScout:=checkInRow(j, i)):
                    threeScoutNames.append(foundOneHalfOfOneScout)
                    break

        if not foundOneHalfOfOneScout:
            threeScoutNames.append('new')
        
        for idx, k in  enumerate(starsX):
            found = False
            for j in range(regionNegotiationSkills[i][1], regionNegotiationSkills[i][3], 3):
                # if pyg.pixelMatchesColor(k, j, (254,203, 0)):
                #     found = True
                #     break
                avoidErrorRecursive(k, j, (254,203, 0))
            if not found:
                break
        threeNegotiationSkills.append(idx+1)

        print2Both("\nFinished with box "+str(i+1)+"\n")
        if i <2:
            print2Both("Currently on Page no. :"+str(page+1)+" out of "+str(int(totalNumber/3+0.7))+'\n')

    page+=1

    for i in range(scoutsCountedTwice, len(threeScoutNames)):
        scouts.append([threeNegotiationSkills[i], threeScoutNames[i], page])
        
    print2Both("Finished with Page no. :"+str(page)+" out of "+str(int(totalNumber/3+0.7)))

    print2Both("\n\nScouts identified on Page :\n")
    for i in range(len(threeScoutNames)-scoutsCountedTwice):
        print2Both("\n\t"+str(scouts[3*page-3+i]))

    lt()
    time.sleep(1)
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
            time.sleep(3)

        numberOfScoutsLeft-=3
    lt()
    print2Both('Time taken to analyze '+str(totalNumber)+' scouts : '+str(int((time.time()-time1)/60))+' minutes and '+str(int((time.time()-time1)%60))+' seconds.')
    print2Both("\n\nTotal Scouts :"+str(scouts)+"\n\n")
    print2Both("\n\nTotal times got OSError :"+str(gotOSError)+"\n\n")


    f = open(path +'/scouts.txt', 'a')
    for i in range(totalNumber):
        f.write(str(scouts[i][0])+', '+str(scouts[i][1])+"\n")
    f.close()
    

def checkInRow(bt, row):
    print2Both('Checking for '+str(bt.name)+' in box '+str(row+1)+str(bt.region[row]))
    point = pyg.locateCenterOnScreen(bt.img, region=bt.region[row] , confidence=.98)

    if(point):
        print2Both("Found "+str(bt.name)+' in box '+str(row+1)+str(bt.region[row]))
        return bt.name
    else:
        print2Both("Couldn't find "+str(bt.name)+' in box '+str(row+1)+str(bt.region[row]))
        return None

restarting = False
run()
f.close()