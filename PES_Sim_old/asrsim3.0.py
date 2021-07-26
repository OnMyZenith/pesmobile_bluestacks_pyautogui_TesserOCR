import pyautogui, time,  winsound, sys

def sim():

    sys.stdout=open("asrsim3.0Output.txt", "a")
    print(time.asctime(time.localtime(time.time())))
    print()
    print("Starting AutoSim in 10 seconds")
    print()
    time.sleep(10)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    #winsound.Beep(500, 500)
    print("Starting Global While loop i = 1")
    print()
    print()
    
    i = 1
    
    while i == 1 :
        
        print()
        print(time.asctime(time.localtime(time.time())))
        print()
        #print("Waiting 10 seconds before looking for SquadNotFine")
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
        print("Looking for SquadNotFine")
        if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
            print("Found SquadNotFine")
            print()
            print()
            print(time.asctime(time.localtime(time.time())))
            print()
            print()
            #winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                print("Attempting Click on SquadNotFine")
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                #winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp()
                print("Waiting 10 seconds before checking and trying again")
                time.sleep(10)

            print("SquadNotFine was clicked")

            print("Looking for 2YelOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                print("Found 2YelOK")
                print()
                print()
                print(time.asctime(time.localtime(time.time())))
                print()
                print()
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                    print("Attempting Click on 2YelOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print("2YelOK was clicked")

                c = 0

                while c < 1:

                    print("Looking for SquadNotFine once again")
                    if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                        print("Found SquadNotFine")
                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                            print("Attempting Click on SquadNotFine")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print("SquadNotFine was clicked")

                        c = 1

            print("Looking for RedOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                print("Found RedOK")
                print()
                print()
                print(time.asctime(time.localtime(time.time())))
                print()
                print()
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                    print("Attempting Click on RedOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print("RedOK was clicked")

                c = 0

                while c < 1:

                    print("Looking for SquadNotFine once again")
                    if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                        print("Found SquadNotFine")
                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                            print("Attempting Click on SquadNotFine")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print("SquadNotFine was clicked")

                        c = 1

            c = 0

            while c < 1:

                print("Looking for Juve")
                if (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                    print("Found Juve")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                        print("Attempting Click on Juve")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Juve.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("Juve was clicked")
                    c = 1                
                    
                else:
                    print("Couldn't find Juve, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for Juve")
            d = 0

            while d < 1:

                print("Looking for SwitchSquad")
                if (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                    print("Found SwitchSquad")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                        print("Attempting Click on SwitchSquad")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchSquad.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 
                        #waiting longer coz dont wanna click again and end up
                        #clicking switchto2, although ie what we will do next
                        # a=0 wont flip, and we'll never get to snfconfirm
                        #doing the same for every sleep coz many screens shere this problem

                    print("SwitchSquad was clicked")
                    d = 1                
                    
                else:
                    print("Couldn't find SwitchSquad, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for SwitchSquad")
          
            a = 0
            
            while a < 1:

                print("Looking for SwitchTo2 or SwitchTo1")
                if (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                    print("Found SwitchTo2")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                        print("Attempting Click on SwitchTo2")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo2.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("SwitchTo2 was clicked")
                    a = 1

                
                elif (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                    print("Found SwitchTo1")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                        print("Attempting Click on SwitchTo1")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo1.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("SwitchTo1 was clicked")
                    a = 1

                else:
                    print("Couldn't find SwitchTo2 or SwitchTo1, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for SwitchTo2 or SwitchTo1")

            e = 0

            while e < 1:

                print("Looking for SNFConfirm")
                if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                    print("Found SNFConfirm")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        print("Attempting Click on SNFConfirm")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("SNFConfirm was clicked")
                    e = 1                
                    
                else:
                    print("Couldn't find SNFConfirm, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for SNFConfirm")

            f = 0

            while f < 1:

                print("Looking for SNFOK")
                if (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                    print("Found SNFOK")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                        print("Attempting Click on SNFOK")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFOK.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("SNFOK was clicked")
                    f = 1                

                else:
                    print("Couldn't find SNFOK, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for SNFOK")

            b = 0

            while b < 1:

                print("Looking for SNFBack")
                if (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                    print("Found SNFBack")
                    #winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                        print("Attempting Click on SNFBack")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFBack.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 10 seconds before checking and trying again")
                        time.sleep(10) 

                    print("SNFBack was clicked")
                    print(time.asctime(time.localtime(time.time())))
                    b = 1                
                    
                else:
                    print("Couldn't find SNFBack, looking for Retry, reporting and clicking if found")
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        print("Found Retry, attemting click")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        print("Waiting 15 seconds before checking and trying again")
                        time.sleep(15)
                    
                    print("Going back to look for SNFBack")

        print("Looking for ToMatch")
        if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
            print("Found ToMatch")
            print()
            print(time.asctime(time.localtime(time.time())))
            print()
            #winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                print("Attempting Click on ToMatch")
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                #winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp()
                print("Waiting 10 seconds before checking and trying again")
                time.sleep(10)

            print("ToMatch was clicked")

            print("Looking for 2YelOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                print("Found 2YelOK")
                print()
                print()
                print(time.asctime(time.localtime(time.time())))
                print()
                print()
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                    print("Attempting Click on 2YelOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print("2YelOK was clicked")

                c = 0

                while c < 1:

                    print("Looking for ToMatch once again")
                    if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                        print("Found ToMatch")
                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                            print("Attempting Click on ToMatch")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print("ToMatch was clicked")

                        c = 1

            print("Looking for RedOK, reporting and clicking if found")
            if (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                print("Found RedOK")
                print()
                print()
                print(time.asctime(time.localtime(time.time())))
                print()
                print()
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                    print("Attempting Click on RedOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

                print("RedOK was clicked")

                c = 0

                while c < 1:

                    print("Looking for ToMatch once again")
                    if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                        print("Found ToMatch")
                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                            print("Attempting Click on ToMatch")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10)

                        print("ToMatch was clicked")

                        c = 1

            print("Looking for InOK")
            if (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                print("Found InOK")
                #winsound.Beep(500, 100)
                
                while (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                    print("Attempting Click on InOK")
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('InOK.png'))
                    #winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp()
                    print("Waiting 10 seconds before checking and trying again")
                    time.sleep(10)

            else:
                print("Looking for ScoutSlot")
                if (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                    print("Found ScoutSlot")
                    #winsound.Beep(500, 100)

                    o = 0
                    
                    while o < 1:

                        while (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                            print("Attempting Click on ScoutSlot")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ScoutSlot.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 
                            
                            o = 1          

                o = 0

                while o < 1:

                    print("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print("Next was clicked")
                        o = 1                
                        
                    else:
                        print("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print("Going back to look for Next")

                p = 0

                while p < 1:

                    print("Looking for SNFConfirm")
                    if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        print("Found SNFConfirm")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                            print("Attempting Click on SNFConfirm")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print("SNFConfirm was clicked")
                        
                        print("Waiting 30 seconds before looking for Retry")
                        # gonna take care of that Retry that we'd have checked in the next loop
                        # Dont wanna wait 4 minutes only to find that the match never started.
                        time.sleep(30)

                        print("Looking for Retry, reporting and clicking if found")
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(30)

                            print("Got rid of Retry, Match should start now, hopefully(If it doesn't, will wait for 3.5 minutes before the next loop starts and takes care of this retry))")

                        print("Waiting 4 minutes for First Half to end")
                        time.sleep(240)

                        p = 1                
                        
                    else:
                        print("Couldn't find SNFConfirm, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print("Going back to look for SNFConfirm")

                q = 0

                while q < 1:

                    print("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print("Next was clicked")
                        q = 1                
                        
                    else:
                        print("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print("Going back to look for Next")

                r = 0

                while r < 1:

                    print("Looking for 2ndHalf")
                    if (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                        print("Found 2ndHalf")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                            print("Attempting Click on 2ndHalf")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2ndHalf.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print("2ndHalf was clicked")
                        
                        print("Waiting 30 seconds before looking for Retry")
                        # gonna take care of that Retry that we'd have checked in the next loop
                        # Dont wanna wait 4 minutes only to find that the 2nd Half never started.
                        time.sleep(30)

                        print("Looking for Retry, reporting and clicking if found")
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(30)
                            
                            print("Got rid of Retry, 2nd Half should start now, hopefully(If it doesn't, will wait for 3.5 minutes before the next loop starts and takes care of this retry))")

                        print("Waiting 3.5 minutes for 2nd Half to end")
                        time.sleep(210)

                        r = 1                
                        
                    else:
                        print("Couldn't find 2ndHalf, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print("Going back to look for 2ndHalf")

                s = 0

                while s < 1:

                    print("Looking for Next")
                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        print("Found Next")
                        #winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            print("Attempting Click on Next")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 10 seconds before checking and trying again")
                            time.sleep(10) 

                        print("Next was clicked")
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()

                        s = 1                
                        
                    else:
                        print("Couldn't find Next, looking for Retry, reporting and clicking if found")
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            print("Found Retry, attemting click")
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            #winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp()
                            print("Waiting 15 seconds before checking and trying again")
                            time.sleep(15)
                        
                        print("Going back to look for Next")

        print("Looking for Next, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print("Found Next, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for Retry, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
            print("Found Retry, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 15 seconds before checking and trying again")
            time.sleep(15)

        #OKs are mismatching, so no  loop after clicking on an OK-
        # -fundamental difference b/t asrsim3.0 and 2.0
        #if it doesen't work find a way to differenciate OKs 
        # by changing their images and including more stuff
        print("Looking for PContExpOK")            
        while (pyautogui.locateCenterOnScreen('PContExpOK.png') is not None):
            print("Attempting Click on PContExpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('PContExpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for Next")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for Proceed")
        while (pyautogui.locateCenterOnScreen('Proceed.png') is not None):
            print("Attempting Click on Proceed")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Proceed.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for ExtAchOK")
        while (pyautogui.locateCenterOnScreen('ExtAchOK.png') is not None):
            print("Attempting Click on ExtAchOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ExtAchOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for Next")                    
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for ContExpOK")
        while (pyautogui.locateCenterOnScreen('ContExpOK.png') is not None):
            print("Attempting Click on ContExpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for Sign")                    
        while (pyautogui.locateCenterOnScreen('Sign.png') is not None):
            print("Attempting Click on Sign")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Sign.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for ContExtOK")                 
        while (pyautogui.locateCenterOnScreen('ContExtOK.png') is not None):
            print("Attempting Click on ContExtOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExtOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for ReqUpOK")                    
        while (pyautogui.locateCenterOnScreen('ReqUpOK.png') is not None):
            print("Attempting Click on ReqUpOK")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ReqUpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for Next")
        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
            print("Attempting Click on Next")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for OKCampStay") 
        #Same as CampDemotion          
        while (pyautogui.locateCenterOnScreen('OKCampStay.png') is not None):
            print("Attempting Click on OKCampStay")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampStay.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for OKCampPro")
        while (pyautogui.locateCenterOnScreen('OKCampPro.png') is not None):
            print("Attempting Click on OKCampPro")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampPro.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for OKCampBon")                    
        while (pyautogui.locateCenterOnScreen('OKCampBon.png') is not None):
            print("Attempting Click on OKCampBon")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampBon.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10) 

        print("Looking for TSUpOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('TSUpOK.png') is not None):
            print("Found TSUpOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('TSUpOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for RedOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
            print("Found RedOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for 2YelOK, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
            print("Found 2YelOK, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 10 seconds before checking and trying again")
            time.sleep(10)

        print("Looking for Retry, reporting and clicking if found")
        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
            print("Found Retry, attemting click")
            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
            #winsound.Beep(2000, 100)
            time.sleep(2)
            pyautogui.mouseUp()
            print("Waiting 15 seconds before checking and trying again")
            time.sleep(15)
    
    print()
    print()
    sys.stdout.close()

sim()