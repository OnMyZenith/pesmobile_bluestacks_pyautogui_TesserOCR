from PIL import Image

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
scoutPositions = (a, c, e)              #Gonna remove this