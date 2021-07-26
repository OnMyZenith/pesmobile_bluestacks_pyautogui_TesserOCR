import pyautogui, time,  winsound, sys
 
f = open('asrsim4.0_output.txt','a')

def print2Both(text):
    print(text)
    f.write(text+'\n')

def sim():

    print2Both(time.ctime())
    print2Both('\n')
    print2Both("Starting AutoSim in 10 seconds")
    print2Both('\n')
    time.sleep(10)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    #winsound.Beep(500, 500)
    print2Both("Starting Global While loop i = 1")
    print2Both('\n')
    print2Both('\n')
    
    i = 1
    
    while i == 1 :
        
        print2Both('\n')
        print2Both(time.ctime())
        print2Both('\n')
        #print2Both("Waiting 10 seconds before looking for SquadNotFine")
        #Waiting 10 seconds before looking for SquadNotFine
        # coz the SNF screen comes on for a fracion of a second before 
        #the disciplinary cards popup, long enough to be detected and
        #in the code "clicked", after which it'll start looking for 
        #Juve when it has red card oK to click on.
        #
        #welp, that didn't work
        #gonna put RedOK and 2YelOK after clicking SNF, and if found,
        #make it click on SNF again.
        #gonna do the same for after ToMatch
        print2Both("Looking for SquadNotFine")
        if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
            print2Both("Found SquadNotFine")
            print2Both('\n')
            print2Both('\n')
            print2Both(time.ctime())
            print2Both('\n')
            print2Both('\n')
            #winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                print2Both("Attempting Click on SquadNotFine")
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                #winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp()
                print2Both("Waiting 10 seconds before checking and trying again")
                time.sleep(10)

            print2Both("SquadNotFine was clicked")

            print2Both("Looking for 2YelOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                print2Both("Found 2YelOK")
                print2Both('\n')
                print2Both('\n')
                print2Both(time.ctime())
                print2Both('\n')
                print2Both('\n')
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                    print2Both("Attempting Click on 2YelOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print2Both("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print2Both("2YelOK was clicked")

                c = 0

                while c < 1:

                    print2Both("Looking for SquadNotFine once again")
                    if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                        print2Both("Found SquadNotFine")
                        print2Both('\n')
                        print2Both('\n')
                        print2Both(time.ctime())
                        print2Both('\n')
                        print2Both('\n')
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                            print2Both("Attempting Click on SquadNotFine")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print2Both("SquadNotFine was clicked")

                        c = 1

            print2Both("Looking for RedOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                print2Both("Found RedOK")
                print2Both('\n')
                print2Both('\n')
                print2Both(time.ctime())
                print2Both('\n')
                print2Both('\n')
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                    print2Both("Attempting Click on RedOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print2Both("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print2Both("RedOK was clicked")

                c = 0

                while c < 1:

                    print2Both("Looking for SquadNotFine once again")
                    if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                        print2Both("Found SquadNotFine")
                        print2Both('\n')
                        print2Both('\n')
                        print2Both(time.ctime())
                        print2Both('\n')
                        print2Both('\n')
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                            print2Both("Attempting Click on SquadNotFine")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print2Both("SquadNotFine was clicked")

                        c = 1

            c = 0

            while c < 1:

                print2Both("Looking for Juve")
                if (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                    print2Both("Found Juve")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                        print2Both("Attempting Click on Juve")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Juve.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("Juve was clicked")
                    c = 1                
                    
                else:
                    print2Both("Couldn't find Juve, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for Juve")
            d = 0

            while d < 1:

                print2Both("Looking for SwitchSquad")
                if (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                    print2Both("Found SwitchSquad")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                        print2Both("Attempting Click on SwitchSquad")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchSquad.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 
                        #waiting longer coz dont wanna click again and end up
                        #clicking switchto2, although ie what we will do next
                        # a=0 wont flip, and we'll never get to snfconfirm
                        #doing the same for every sleep coz many screens shere this problem

                    print2Both("SwitchSquad was clicked")
                    d = 1                
                    
                else:
                    print2Both("Couldn't find SwitchSquad, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for SwitchSquad")
          
            a = 0
            
            while a < 1:

                print2Both("Looking for SwitchTo2 or SwitchTo1")
                if (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                    print2Both("Found SwitchTo2")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                        print2Both("Attempting Click on SwitchTo2")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo2.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("SwitchTo2 was clicked")
                    a = 1

                
                elif (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                    print2Both("Found SwitchTo1")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                        print2Both("Attempting Click on SwitchTo1")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo1.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("SwitchTo1 was clicked")
                    a = 1

                else:
                    print2Both("Couldn't find SwitchTo2 or SwitchTo1, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for SwitchTo2 or SwitchTo1")

            e = 0

            while e < 1:

                print2Both("Looking for SNFConfirm")
                if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                    print2Both("Found SNFConfirm")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        print2Both("Attempting Click on SNFConfirm")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("SNFConfirm was clicked")
                    e = 1                
                    
                else:
                    print2Both("Couldn't find SNFConfirm, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for SNFConfirm")

            f = 0

            while f < 1:

                print2Both("Looking for SNFOK")
                if (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                    print2Both("Found SNFOK")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                        print2Both("Attempting Click on SNFOK")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFOK.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("SNFOK was clicked")
                    f = 1                

                else:
                    print2Both("Couldn't find SNFOK, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for SNFOK")

            b = 0

            while b < 1:

                print2Both("Looking for SNFBack")
                if (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                    print2Both("Found SNFBack")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                        print2Both("Attempting Click on SNFBack")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFBack.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print2Both("SNFBack was clicked")
                    print2Both(time.ctime())
                    b = 1                
                    
                else:
                    print2Both("Couldn't find SNFBack, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print2Both("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print2Both("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print2Both("Going back to look for SNFBack")

        print2Both("Looking for ToMatch")
        if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
            print2Both("Found ToMatch")
            print2Both('\n')
            print2Both(time.ctime())
            print2Both('\n')
            #winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                print2Both("Attempting Click on ToMatch")
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                #winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp()
                print2Both("Waiting 10 seconds before checking and trying again")
                time.sleep(10)

            print2Both("ToMatch was clicked")

            print2Both("Looking for 2YelOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                print2Both("Found 2YelOK")
                print2Both('\n')
                print2Both('\n')
                print2Both(time.ctime())
                print2Both('\n')
                print2Both('\n')
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                    print2Both("Attempting Click on 2YelOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print2Both("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print2Both("2YelOK was clicked")

                c = 0

                while c < 1:

                    print2Both("Looking for ToMatch once again")
                    if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                        print2Both("Found ToMatch")
                        print2Both('\n')
                        print2Both('\n')
                        print2Both(time.ctime())
                        print2Both('\n')
                        print2Both('\n')
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                            print2Both("Attempting Click on ToMatch")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print2Both("ToMatch was clicked")

                        c = 1

            print2Both("Looking for RedOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                print2Both("Found RedOK")
                print2Both('\n')
                print2Both('\n')
                print2Both(time.ctime())
                print2Both('\n')
                print2Both('\n')
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                    print2Both("Attempting Click on RedOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print2Both("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print2Both("RedOK was clicked")

                c = 0

                while c < 1:

                    print2Both("Looking for ToMatch once again")
                    if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                        print2Both("Found ToMatch")
                        print2Both('\n')
                        print2Both('\n')
                        print2Both(time.ctime())
                        print2Both('\n')
                        print2Both('\n')
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                            print2Both("Attempting Click on ToMatch")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print2Both("ToMatch was clicked")

                        c = 1

            print2Both("Looking for InOK")
            if (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                print2Both("Found InOK")
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                    print2Both("Attempting Click on InOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('InOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print2Both("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

            else:
                print2Both("Looking for ScoutSlot")
                if (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                    print2Both("Found ScoutSlot")
                    #winsound.Beep(500, 100)

                    o = 0
                    
                    while o < 1:

                        while (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                            print2Both("Attempting Click on ScoutSlot")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ScoutSlot.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 
                            
                            o = 1          

                o = 0

                while o < 1:

                    print2Both("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print2Both("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print2Both("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print2Both("Next was clicked")
                        o = 1                
                        
                    else:
                        print2Both("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print2Both("Going back to look for Next")

                p = 0

                while p < 1:

                    print2Both("Looking for SNFConfirm")
                    if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        print2Both("Found SNFConfirm")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                            print2Both("Attempting Click on SNFConfirm")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print2Both("SNFConfirm was clicked")
                        
                        print2Both("Waiting 30 seconds before looking for Retry")
                        # gonna take care of that Retry that we'd have checked in the next loop
                        # Dont wanna wait 4 minutes only to find that the match never started.
                        time.sleep(30)

                        print2Both("Looking for Retry, reporting and clicking if found")
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(30)

                            print2Both("Got rid of Retry, Match should start now, hopefully(If it doesn't, will wait for 3.5 minutes before the next loop starts and takes care of this retry))")

                        print2Both("Waiting 4 minutes for First Half to end")
                        time.sleep(240)

                        p = 1                
                        
                    else:
                        print2Both("Couldn't find SNFConfirm, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print2Both("Going back to look for SNFConfirm")

                q = 0

                while q < 1:

                    print2Both("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print2Both("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print2Both("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print2Both("Next was clicked")
                        q = 1                
                        
                    else:
                        print2Both("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print2Both("Going back to look for Next")

                r = 0

                while r < 1:

                    print2Both("Looking for 2ndHalf")
                    if (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                        print2Both("Found 2ndHalf")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                            print2Both("Attempting Click on 2ndHalf")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2ndHalf.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print2Both("2ndHalf was clicked")
                        
                        print2Both("Waiting 30 seconds before looking for Retry")
                        # gonna take care of that Retry that we'd have checked in the next loop
                        # Dont wanna wait 4 minutes only to find that the 2nd Half never started.
                        time.sleep(30)

                        print2Both("Looking for Retry, reporting and clicking if found")
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(30)
                            
                            print2Both("Got rid of Retry, 2nd Half should start now, hopefully(If it doesn't, will wait for 3.5 minutes before the next loop starts and takes care of this retry))")

                        print2Both("Waiting 3.5 minutes for 2nd Half to end")
                        time.sleep(210)

                        r = 1                
                        
                    else:
                        print2Both("Couldn't find 2ndHalf, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print2Both("Going back to look for 2ndHalf")

                s = 0

                while s < 1:

                    print2Both("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print2Both("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print2Both("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print2Both("Next was clicked")
                        print2Both('\n')
                        print2Both(time.ctime())
                        print2Both('\n')

                        s = 1                
                        
                    else:
                        print2Both("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print2Both("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print2Both("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print2Both("Going back to look for Next")

        print2Both("Looking for Next, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print2Both("Found Next, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for Retry, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
            print2Both("Found Retry, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 15 seconds before checking and trying again")
            time.sleep(15)

        #OKs are mismatching, so no  loop after clicking on an OK-
        # -fundamental difference b/t asrsim3.0 and 2.0
        #if it doesen't work find a way to differenciate OKs 
        # by changing their images and including more stuff
        print2Both("Looking for PContExpOK")            
        while (pyautogui.locateCenterOnScreen('PContExpOK.png') is not None):
            print2Both("Attempting Click on PContExpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('PContExpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for Next")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print2Both("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for Proceed")
        while (pyautogui.locateCenterOnScreen('Proceed.png') is not None):
            print2Both("Attempting Click on Proceed")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Proceed.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for ExtAchOK")
        while (pyautogui.locateCenterOnScreen('ExtAchOK.png') is not None):
            print2Both("Attempting Click on ExtAchOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ExtAchOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for Next")                    
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print2Both("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for ContExpOK")
        while (pyautogui.locateCenterOnScreen('ContExpOK.png') is not None):
            print2Both("Attempting Click on ContExpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for Sign")                    
        while (pyautogui.locateCenterOnScreen('Sign.png') is not None):
            print2Both("Attempting Click on Sign")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Sign.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for ContExtOK")                 
        while (pyautogui.locateCenterOnScreen('ContExtOK.png') is not None):
            print2Both("Attempting Click on ContExtOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExtOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for ReqUpOK")                    
        while (pyautogui.locateCenterOnScreen('ReqUpOK.png') is not None):
            print2Both("Attempting Click on ReqUpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ReqUpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for Next")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print2Both("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for OKCampStay") 
        #Same as CampDemotion          
        while (pyautogui.locateCenterOnScreen('OKCampStay.png') is not None):
            print2Both("Attempting Click on OKCampStay")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampStay.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for OKCampPro")
        while (pyautogui.locateCenterOnScreen('OKCampPro.png') is not None):
            print2Both("Attempting Click on OKCampPro")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampPro.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for OKCampBon")                    
        while (pyautogui.locateCenterOnScreen('OKCampBon.png') is not None):
            print2Both("Attempting Click on OKCampBon")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampBon.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print2Both("Looking for TSUpOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('TSUpOK.png') is not None):
            print2Both("Found TSUpOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('TSUpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for RedOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
            print2Both("Found RedOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for 2YelOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
            print2Both("Found 2YelOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print2Both("Looking for Retry, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
            print2Both("Found Retry, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print2Both("Waiting 15 seconds before checking and trying again")
            time.sleep(15)
    
    print2Both('\n')
    print2Both('\n')

sim()

f.close()