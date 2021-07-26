import pyautogui, time,  winsound, sys

def ContRen():

    sys.stdout=open("ContractOutput.txt", "a")
    print(time.asctime(time.localtime(time.time())))
    print()
    print("Starting ContRen in 10 seconds")
    print()
    time.sleep(10)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    winsound.Beep(500, 500)
    print("Starting Global While loop z = 0")

    z = 0

    while z < 1:

        print("Checking Squad Number")
        if (pyautogui.locateCenterOnScreen('CF_Jarvis.png') is not None):
            print("Found Squad2")
            print()
            print()
            winsound.Beep(700, 100)

            i = 0
            
            #loop for Squad2
            while i < 1:
                
                a = 0
                
                #loop for first page of Squad2          
                while a < 1:

                    b = 0
                    
                    #loop for one player of first page of Squad2
                    while b < 1:

                        d = 0

                        #loop for one contract of one player of first page of Squad2
                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CF_Jarvis.png') is not None):
                                    print("Attempting Click on CF_Jarvis")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_Jarvis.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CF_Jarvis was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    #After RenewedOK the loop of GP ends with the loop of one contract renewal
                                    c = 1

                                    print("CF_Jarvis--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    #After ContLimOK the loop of ContLimOK ends with the loop of one contract renewal
                                    #and the loop of contract renewal of one player
                                    c = 1

                                    d = 1

                                    print("CF_Jarvis--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('LWF_SS_Lavernia.png') is not None):
                                    print("Attempting Click on LWF_SS_Lavernia")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LWF_SS_Lavernia.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("LWF_SS_Lavernia was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("LWF_SS_Lavernia--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("LWF_SS_Lavernia--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('AMF_Redmond.png') is not None):
                                    print("Attempting Click on AMF_Redmond")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('AMF_Redmond.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("AMF_Redmond was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("AMF_Redmond--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("AMF_Redmond--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CMF_Llonch.png') is not None):
                                    print("Attempting Click on CMF_Llonch")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Llonch.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CMF_Llonch was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CMF_Llonch--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CMF_Llonch--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CMF_Bordas.png') is not None):
                                    print("Attempting Click on CMF_Bordas")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Bordas.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CMF_Bordas was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CMF_Bordas--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CMF_Bordas--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('DMF_Rimonte.png') is not None):
                                    print("Attempting Click on DMF_Rimonte")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('DMF_Rimonte.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("DMF_Rimonte was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("DMF_Rimonte--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("DMF_Rimonte--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

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

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('RB_Torrealba.png') is not None):
                                    print("Attempting Click on RB_Torrealba")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RB_Torrealba.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("RB_Torrealba was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("RB_Torrealba--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")

                                    c = 1

                                    d = 1

                                    print("RB_Torrealba--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('LB_Coulfield.png') is not None):
                                    print("Attempting Click on LB_Coulfield")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LB_Coulfield.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("LB_Coulfield was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("LB_Coulfield--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("LB_Coulfield--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CB_Legoida.png') is not None):
                                    print("Attempting Click on CB_Legoida")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Legoida.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CB_Legoida was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CB_Legoida--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CB_Legoida--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CB_Candemir.png') is not None):
                                    print("Attempting Click on CB_Candemir")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Candemir.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CB_Candemir was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CB_Candemir--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CB_Candemir--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

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

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('GK_Luiz.png') is not None):
                                    print("Attempting Click on GK_Luiz")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GK_Luiz.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("GK_Luiz was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("GK_Luiz--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")

                                    c = 1

                                    d = 1

                                    print("GK_Luiz--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
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
            winsound.Beep(700, 100)

            i = 0
            
            while i < 1:
                
                a = 0
                
                while a < 1:

                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CF_SS_Hervey.png') is not None):
                                    print("Attempting Click on CF_SS_Hervey")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_SS_Hervey.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CF_SS_Hervey was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CF_SS_Hervey--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CF_SS_Hervey--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CF_Goios.png') is not None):
                                    print("Attempting Click on CF_Goios")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CF_Goios.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CF_Goios was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CF_Goios--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CF_Goios--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('AMF_Castledine.png') is not None):
                                    print("Attempting Click on AMF_Castledine")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('AMF_Castledine.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("AMF_Castledine was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("AMF_Castledine--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("AMF_Castledine--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CMF_Bassano.png') is not None):
                                    print("Attempting Click on CMF_Bassano")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Bassano.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CMF_Bassano was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CMF_Bassano--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CMF_Bassano--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CMF_Vrany.png') is not None):
                                    print("Attempting Click on CMF_Vrany")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CMF_Vrany.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CMF_Vrany was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CMF_Vrany--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CMF_Vrany--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('DMF_Boia.png') is not None):
                                    print("Attempting Click on DMF_Boia")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('DMF_Boia.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("DMF_Boia was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("DMF_Boia--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("DMF_Boia--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

                    #loop of first page ends as DMF_Rimonte is maxed out
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

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('RB_Parada.png') is not None):
                                    print("Attempting Click on RB_Parada")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RB_Parada.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("RB_Parada was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("RB_Parada--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")

                                    c = 1

                                    d = 1

                                    print("RB_Parada--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('LB_Soric.png') is not None):
                                    print("Attempting Click on LB_Soric")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('LB_Soric.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("LB_Soric was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("LB_Soric--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("LB_Soric--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CB_Rekarte.png') is not None):
                                    print("Attempting Click on CB_Rekarte")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Rekarte.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CB_Rekarte was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CB_Rekarte--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CB_Rekarte--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
                    b = 0
                    
                    while b < 1:

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('CB_Gois.png') is not None):
                                    print("Attempting Click on CB_Gois")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('CB_Gois.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("CB_Gois was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("CB_Gois--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")
                                    
                                    c = 1

                                    d = 1

                                    print("CB_Gois--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")

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

                        d = 0

                        while d < 1:

                            c = 0

                            while c < 1:

                                while (pyautogui.locateCenterOnScreen('GK_Nordfeldt.png') is not None):
                                    print("Attempting Click on GK_Nordfeldt")
                                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GK_Nordfeldt.png'))
                                    winsound.Beep(2000, 100)
                                    time.sleep(2)
                                    pyautogui.mouseUp()
                                    print("Waiting 10 seconds before checking and trying again")
                                    time.sleep(10)

                                print("GK_Nordfeldt was clicked")

                                c = 1

                            c = 0

                            while c < 1:

                                print("Looking for ContRen")
                                if (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                    print("Found ContRen")
                                    winsound.Beep(700, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContRen.png') is not None):
                                        print("Attempting Click on ContRen")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContRen.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContRen was clicked")
                                    c = 1                
                                    
                                else:
                                    print("Couldn't find ContRen, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for ContRen")

                            c = 0
                            
                            while c < 1:

                                print("Looking for GP or ContLimOK")
                                if (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                    print("Found GP")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('GP.png') is not None):
                                        print("Attempting Click on GP")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('GP.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("GP was clicked")

                                    e = 0

                                    while e < 1:

                                        print("Looking for Renew")
                                        if (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                            print("Found Renew")
                                            winsound.Beep(700, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('Renew.png') is not None):
                                                print("Attempting Click on Renew")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Renew.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)

                                            print("Renew was clicked")
                                            e = 1
                                            
                                        else:
                                            print("Couldn't find Renew, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for Renew")

                                    e = 0
                                    
                                    while e < 1:

                                        print("Looking for RenewedOK or RenewedOK_Alt")
                                        if (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                            print("Found RenewedOK")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK.png') is not None):
                                                print("Attempting Click on RenewedOK")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK was clicked")
                                            e = 1

                                        
                                        elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                            print("Found RenewedOK_Alt")
                                            winsound.Beep(500, 100)
                                            
                                            while (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                                print("Attempting Click on RenewedOK_Alt")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 10 seconds before checking and trying again")
                                                time.sleep(10) 

                                            print("RenewedOK_Alt was clicked")
                                            e = 1

                                        else:
                                            print("Couldn't find RenewedOK or RenewedOK_Alt, looking for Retry, reporting and clicking if found")
                                            
                                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                                print("Found Retry, attemting click")
                                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                                winsound.Beep(2000, 100)
                                                time.sleep(2)
                                                pyautogui.mouseUp()
                                                print("Waiting 15 seconds before checking and trying again")
                                                time.sleep(15)
                                            
                                            print("Going back to look for RenewedOK or RenewedOK_Alt")
                                    
                                    c = 1

                                    print("GK_Nordfeldt--Contract Extended by 10 matches")
                                    print()
                                    print()
                                    d = 1


                                elif (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                    print("Found ContLimOK")
                                    winsound.Beep(500, 100)
                                    
                                    while (pyautogui.locateCenterOnScreen('ContLimOK.png') is not None):
                                        print("Attempting Click on ContLimOK")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContLimOK.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("ContLimOK was clicked")

                                    c = 1

                                    d = 1

                                    print("GK_Nordfeldt--Contract Maxed")
                                    print()
                                    print()
                                    while (pyautogui.locateCenterOnScreen('X.png') is not None):
                                        print("Attempting Click on X")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('X.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 10 seconds before checking and trying again")
                                        time.sleep(10) 

                                    print("X was clicked")
                                    print()
                                    print()
                                    print()
                                    print() 
                                    
                                    b = 1

                                else:
                                    print("Couldn't find GP or ContLimOK, looking for Retry, reporting and clicking if found")
                                    
                                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                        print("Found Retry, attemting click")
                                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                        winsound.Beep(2000, 100)
                                        time.sleep(2)
                                        pyautogui.mouseUp()
                                        print("Waiting 15 seconds before checking and trying again")
                                        time.sleep(15)
                                    
                                    print("Going back to look for GP or ContLimOK")
                    
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
            time.sleep(3)

    print()
    print()
    sys.stdout.close()

ContRen()