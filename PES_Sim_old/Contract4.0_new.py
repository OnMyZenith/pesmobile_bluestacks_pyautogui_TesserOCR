import pyautogui, time,  winsound, sys

def ContRen():

    print(time.asctime(time.localtime(time.time())))
    print()
    print("Starting ContRen in 3 seconds")
    print()
    time.sleep(3)
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
            
            #loop for entire Squad2 for one contract
            while i < 1:

                c = 0

                while c < 1:

                    print("Clicking on Select")
                    pyautogui.mouseDown(1200, 1010)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    
                    c = 1

                pyautogui.mouseDown(600, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(600, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(600, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  
                
                pyautogui.mouseDown(1400, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(1400, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(1400, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  
                
                pyautogui.mouseDown(50, 917)
                time.sleep(1)
                pyautogui.moveTo(50, 228, duration=3)
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)

                pyautogui.mouseDown(600, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(600, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(600, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(1400, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(1400, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                c = 0

                while c < 1:

                    print("Clicking on Action")
                    pyautogui.mouseDown(1200, 1010)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    
                    c = 1

                c = 0

                while c < 1:

                    print("Clicking on SquadContRen")
                    pyautogui.mouseDown(950, 430)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    
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
                                time.sleep(3)

                                e = 1

                            
                            elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                print("Found RenewedOK_Alt")
                                print("Clicking on RenewedOK_Alt")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()
                                time.sleep(3)

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
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        print("All Contracts Extended by 10 matches")
                        print()
                        print()

                        e = 0
                        
                        while e < 1:
                            print("Scrolling to top to start selecting again")
                            pyautogui.mouseDown(50, 300)
                            pyautogui.moveTo(50, 800, duration=0.5)
                            pyautogui.mouseUp()
                            time.sleep(3)
                            pyautogui.mouseDown(50, 300)
                            pyautogui.moveTo(50, 800, duration=0.5)
                            pyautogui.mouseUp()
                            time.sleep(3)
                            
                            e = 1
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

                        i = 1

                        z = 1

                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        print("All Contracts Maxed")
                        print()
                        print()

        elif (pyautogui.locateCenterOnScreen('CF_SS_Hervey.png') is not None):
            print("Found Squad1")
            print()
            print()
            #winsound.Beep(700, 100)

            i = 0
            
            #loop for entire Squad1 for one contract
            while i < 1:

                c = 0

                while c < 1:

                    print("Clicking on Select")
                    pyautogui.mouseDown(1200, 1010)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    
                    c = 1

                pyautogui.mouseDown(600, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(600, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(600, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  
                
                pyautogui.mouseDown(1400, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(1400, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(1400, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  
                
                pyautogui.mouseDown(50, 917)
                time.sleep(1)
                pyautogui.moveTo(50, 228, duration=3)
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)

                pyautogui.mouseDown(600, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(600, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)  

                pyautogui.mouseDown(1400, 350)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)                

                pyautogui.mouseDown(1400, 575)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)   
                
                pyautogui.mouseDown(50, 917)
                time.sleep(1)
                pyautogui.moveTo(50, 228, duration=3)
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)

                pyautogui.mouseDown(600, 800)
                time.sleep(1)
                pyautogui.mouseUp()
                time.sleep(1)

                c = 0

                while c < 1:

                    print("Clicking on Action")
                    pyautogui.mouseDown(1200, 1010)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(3)
                    
                    c = 1

                c = 0

                while c < 1:

                    print("Clicking on SquadContRen")
                    pyautogui.mouseDown(950, 430)
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    
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
                                time.sleep(3)

                                e = 1

                            
                            elif (pyautogui.locateCenterOnScreen('RenewedOK_Alt.png') is not None):
                                print("Found RenewedOK_Alt")
                                print("Clicking on RenewedOK_Alt")
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RenewedOK_Alt.png'))
                                #winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp()
                                time.sleep(3)

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
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        print("All Contracts Extended by 10 matches")
                        print()
                        print()

                        e = 0
                        
                        while e < 1:
                            print("Scrolling to top to start selecting again")
                            pyautogui.mouseDown(50, 300)
                            pyautogui.moveTo(50, 800, duration=0.5)
                            pyautogui.mouseUp()
                            time.sleep(3)
                            pyautogui.mouseDown(50, 300)
                            pyautogui.moveTo(50, 800, duration=0.5)
                            pyautogui.mouseUp()
                            time.sleep(3)
                            e = 1
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

                        i = 1

                        z = 1

                        print()
                        print()
                        print(time.asctime(time.localtime(time.time())))
                        print()
                        print()
                        print("All Contracts Maxed")
                        print()
                        print()
        
        else:
            print("Couldn't recognise Squad number, Scrolling to top to check again")
            pyautogui.mouseDown(50, 300)
            pyautogui.moveTo(50, 800, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(3)
            pyautogui.mouseDown(50, 300)
            pyautogui.moveTo(50, 800, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(4)
    print()
    print()

ContRen()