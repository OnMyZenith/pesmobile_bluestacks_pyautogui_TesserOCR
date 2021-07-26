import pyautogui, time,  winsound, sys

def ContRen():

    sys.stdout=open("Contract3.0Output.txt", "a")
    print(time.asctime(time.localtime(time.time())))
    print()
    print("Starting ContRen in 10 seconds")
    print()
    time.sleep(10)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    #winsound.Beep(500, 500)
    print("Starting Global While loop z = 0")

    z = 0

    while z < 1:

        print("Checking Squad Number")
        if (pyautogui.locateCenterOnScreen('CF_Jarvis.png') is not None):
            print("Found Squad2")
            print()
            print()
            #winsound.Beep(700, 100)

            i = 0
            
            #loop for Squad2
            while i < 1:
                
                a = 0
                
                #loop for first page
                while a < 1:

                    b = 0
                    
                    #loop for one player
                    while b < 1:

                        print("Clicking on CF_Jarvis")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_Jarvis.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()
                        
                        d = 0

                        #loop for one contract
                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    #After RenewedOK the loop of GP ends without ending the loop of one contract renewal
                                    c = 1
                                    print()
                                    print()
                                    print("CF_Jarvis--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    #After ContLimOK the loop of ContLimOK ends with the loop of one contract renewal
                                    #and the loop of contract renewal of one player
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CF_Jarvis--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for LWF_SS_Lavernia")
                            if (pyautogui.locateCenterOnScreen('LWF_SS_Lavernia.png') is not None):
                                print("Found LWF_SS_Lavernia")
                                print("Clicking on LWF_SS_Lavernia")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LWF_SS_Lavernia.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1   
                        
                        d = 0

                        while d < 1:            

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("LWF_SS_Lavernia--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("LWF_SS_Lavernia--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for AMF_Redmond")
                            if (pyautogui.locateCenterOnScreen('AMF_Redmond.png') is not None):
                                print("Found AMF_Redmond")
                                print("Clicking on AMF_Redmond")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('AMF_Redmond.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("AMF_Redmond--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("AMF_Redmond--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CMF_Llonch")
                            if (pyautogui.locateCenterOnScreen('CMF_Llonch.png') is not None):
                                print("Found CMF_Llonch")
                                print("Clicking on CMF_Llonch")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Llonch.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CMF_Llonch--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CMF_Llonch--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CMF_Bordas")
                            if (pyautogui.locateCenterOnScreen('CMF_Bordas.png') is not None):
                                print("Found CMF_Bordas")
                                print("Clicking on CMF_Bordas")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Bordas.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CMF_Bordas--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CMF_Bordas--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for DMF_Rimonte")
                            if (pyautogui.locateCenterOnScreen('DMF_Rimonte.png') is not None):
                                print("Found DMF_Rimonte")
                                print("Clicking on DMF_Rimonte")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('DMF_Rimonte.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("DMF_Rimonte--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("DMF_Rimonte--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            time.sleep(5)
                                            print("Waiting 5 seconds before scrolling")

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    #loop of first page ends as DMF_Rimonte is maxed out
                    a = 1

                pyautogui.mouseDown(50, 800)
                pyautogui.moveTo(50, 100, duration=5)
                time.sleep(3)
                pyautogui.mouseUp()
                
                print("Scrolled to Page 2 of Squad2")
                a = 0
                
                while a < 1:

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for RB_Torrealba")
                            if (pyautogui.locateCenterOnScreen('RB_Torrealba.png') is not None):
                                print("Found RB_Torrealba")
                                print("Clicking on RB_Torrealba")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RB_Torrealba.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("RB_Torrealba--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("RB_Torrealba--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for LB_Coulfield")
                            if (pyautogui.locateCenterOnScreen('LB_Coulfield.png') is not None):
                                print("Found LB_Coulfield")
                                print("Clicking on LB_Coulfield")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LB_Coulfield.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("LB_Coulfield--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("LB_Coulfield--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CB_Legoida")
                            if (pyautogui.locateCenterOnScreen('CB_Legoida.png') is not None):
                                print("Found CB_Legoida")
                                print("Clicking on CB_Legoida")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Legoida.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CB_Legoida--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CB_Legoida--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CB_Candemir")
                            if (pyautogui.locateCenterOnScreen('CB_Candemir.png') is not None):
                                print("Found CB_Candemir")
                                print("Clicking on CB_Candemir")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Candemir.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CB_Candemir--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CB_Candemir--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            time.sleep(5)
                                            print("Waiting 5 seconds before scrolling")

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    a = 1

                pyautogui.mouseDown(50, 800)
                pyautogui.moveTo(50, 100, duration=5)
                time.sleep(3)
                pyautogui.mouseUp()

                print("Scrolled to Page 3 of Squad2")
                a = 0
                
                while a < 1:


                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for GK_Luiz")
                            if (pyautogui.locateCenterOnScreen('GK_Luiz.png') is not None):
                                print("Found GK_Luiz")
                                print("Clicking on GK_Luiz")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GK_Luiz.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("GK_Luiz--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("GK_Luiz--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1
                    
                    a = 1
                    print("Squad2 is maxxed")

                #loop of Squad2 ends as GK_Luiz is maxed out
                i = 1

                z = 1
                print(time.asctime(time.localtime(time.time())))

        elif (pyautogui.locateCenterOnScreen('CF_SS_Hervey.png') is not None):
            print("Found Squad1")
            print()
            print()
            #winsound.Beep(700, 100)

            i = 0
            
            while i < 1:
                
                a = 0
                
                while a < 1:

                    b = 0
                    
                    while b < 1:

                        print("Clicking on CF_SS_Hervey")
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_SS_Hervey.png'))
                        #winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp()

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CF_SS_Hervey--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CF_SS_Hervey--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CF_Goios")
                            if (pyautogui.locateCenterOnScreen('CF_Goios.png') is not None):
                                print("Found CF_Goios")
                                print("Clicking on CF_Goios")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_Goios.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CF_Goios--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CF_Goios--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for AMF_Castledine")
                            if (pyautogui.locateCenterOnScreen('AMF_Castledine.png') is not None):
                                print("Found AMF_Castledine")
                                print("Clicking on AMF_Castledine")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('AMF_Castledine.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("AMF_Castledine--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("AMF_Castledine--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CMF_Bassano")
                            if (pyautogui.locateCenterOnScreen('CMF_Bassano.png') is not None):
                                print("Found CMF_Bassano")
                                print("Clicking on CMF_Bassano")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Bassano.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CMF_Bassano--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CMF_Bassano--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CMF_Vrany")
                            if (pyautogui.locateCenterOnScreen('CMF_Vrany.png') is not None):
                                print("Found CMF_Vrany")
                                print("Clicking on CMF_Vrany")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Vrany.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CMF_Vrany--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CMF_Vrany--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for DMF_Boia")
                            if (pyautogui.locateCenterOnScreen('DMF_Boia.png') is not None):
                                print("Found DMF_Boia")
                                print("Clicking on DMF_Boia")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('DMF_Boia.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("DMF_Boia--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("DMF_Boia--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            time.sleep(5)
                                            print("Waiting 5 seconds before scrolling")

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    #loop of first page ends as DMF_Boia is maxed out
                    a = 1

                pyautogui.mouseDown(50, 800)
                pyautogui.moveTo(50, 100, duration=5)
                time.sleep(3)
                pyautogui.mouseUp()

                print("Scrolled to Page 2 of Squad1")
                a = 0
                
                while a < 1:

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for RB_Parada")
                            if (pyautogui.locateCenterOnScreen('RB_Parada.png') is not None):
                                print("Found RB_Parada")
                                print("Clicking on RB_Parada")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RB_Parada.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("RB_Parada--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("RB_Parada--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1
                    
                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for LB_Soric")
                            if (pyautogui.locateCenterOnScreen('LB_Soric.png') is not None):
                                print("Found LB_Soric")
                                print("Clicking on LB_Soric")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LB_Soric.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("LB_Soric--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("LB_Soric--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CB_Rekarte")
                            if (pyautogui.locateCenterOnScreen('CB_Rekarte.png') is not None):
                                print("Found CB_Rekarte")
                                print("Clicking on CB_Rekarte")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Rekarte.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CB_Rekarte--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CB_Rekarte--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for CB_Gois")
                            if (pyautogui.locateCenterOnScreen('CB_Gois.png') is not None):
                                print("Found CB_Gois")
                                print("Clicking on CB_Gois")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Gois.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("CB_Gois--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("CB_Gois--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            time.sleep(5)
                                            print("Waiting 5 seconds before scrolling")

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1

                    a = 1

                pyautogui.mouseDown(50, 800)
                pyautogui.moveTo(50, 100, duration=5)
                time.sleep(3)
                pyautogui.mouseUp()

                print("Scrolled to Page 3 of Squad1")
                a = 0
                
                while a < 1:

                    b = 0
                    
                    while b < 1:

                        c = 0

                        while c < 1:

                            print("Looking for GK_Nordfeldt")
                            if (pyautogui.locateCenterOnScreen('GK_Nordfeldt.png') is not None):
                                print("Found GK_Nordfeldt")
                                print("Clicking on GK_Nordfeldt")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GK_Nordfeldt.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()

                                c = 1                

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    print("Clicking on ContRen")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    c = 1                

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    print("Clicking on GP")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            print("Clicking on Renew")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            e = 1

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            print("Clicking on RenewedOK")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            print("Clicking on RenewedOK_Alt")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            e = 1

                                        elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                            print("Clicking on Retry")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1
                                    print()
                                    print()
                                    print("GK_Nordfeldt--Contract Extended by 10 matches")
                                    print()
                                    print()

                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    print("Clicking on ContLimOK")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                    #winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
 
                                    c = 1

                                    d = 1

                                    b = 1

                                    print()
                                    print()
                                    print("GK_Nordfeldt--Contract Maxed")
                                    print()
                                    print()
                                    
                                    e = 0

                                    while e < 1:

                                        print("Looking for X")
                                        if (pyautogui.locateCenterOnScreen('X.png') is not None):
                                            print("Found X")
                                            print("Clicking on X")
                                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                            #winsound.Beep(2000, 100)
                                            time.sleep(2)
                                            pyautogui.mouseUp()

                                            print()
                                            print()
                                            print()
                                            print()

                                            e = 1
                    
                    a = 1
                    print("Squad1 is maxxed")

                i = 1

                z = 1
                print(time.asctime(time.localtime(time.time())))
        
        else:
            print("Couldn't recognise Squad number, Scrolling to top to check again")
            pyautogui.mouseDown(50, 300)
            pyautogui.moveTo(50, 800, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(7)
    print()
    print()
    sys.stdout.close()

ContRen()