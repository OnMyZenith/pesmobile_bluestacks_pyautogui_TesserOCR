import pyautogui, time,  winsound

def sim():
    time.sleep(5)
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = True
    winsound.Beep(500, 500)

    i = 1
    
    while i == 1 :
        
        if (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('SquadNotFine.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SquadNotFine.png'))
                time.sleep(10)

            c = 0

            while c < 1:

                if (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Juve.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Juve.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Juve.png'))
                        time.sleep(10) 

                    c = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            d = 0

            while d < 1:

                if (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchSquad.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchSquad.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SwitchSquad.png'))
                        time.sleep(10)
                        #waiting longer coz dont wanna click again and end up
                        #clicking switchto2, although ie what we will do next
                        # a=0 wont flip, and we'll never get to snfconfirm
                        #doing the same for every sleep coz many screens shere this problem

                    d = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)
           
            a = 0
            
            while a < 1:
                
                if (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo2.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo2.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SwitchTo2.png'))
                        time.sleep(10)
                   
                    a = 1

                elif (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SwitchTo1.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SwitchTo1.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SwitchTo1.png'))
                        time.sleep(10)

                    a = 1
                
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            e = 0

            while e < 1:

                if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                        time.sleep(10) 

                    e = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            f = 0

            while f < 1:

                if (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFOK.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFOK.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SNFOK.png'))
                        time.sleep(10) 

                    f = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)
           
            b = 0

            while b < 1:

                if (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('SNFBack.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFBack.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SNFBack.png'))
                        time.sleep(10) 

                    b = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)
    
        if (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
            winsound.Beep(500, 100)
                    
            while (pyautogui.locateCenterOnScreen('ToMatch.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ToMatch.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ToMatch.png'))
                time.sleep(10)
            
            if (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                winsound.Beep(500, 100)
                    
                while (pyautogui.locateCenterOnScreen('InOK.png') is not None):
                    pyautogui.mouseDown(pyautogui.locateCenterOnScreen('InOK.png'))
                    winsound.Beep(2000, 100)
                    time.sleep(2)
                    pyautogui.mouseUp(pyautogui.locateCenterOnScreen('InOK.png'))
                    time.sleep(10)

            else:
                if (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                    winsound.Beep(500, 100)
                        
                    while (pyautogui.locateCenterOnScreen('ScoutSlot.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ScoutSlot.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ScoutSlot.png'))
                        time.sleep(10)           

                o = 0

                while o < 1:

                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                            time.sleep(10) 

                        o = 1                
                        
                    elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                            time.sleep(15)

                p = 0

                while p < 1:

                    if (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('SNFConfirm.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('SNFConfirm.png'))
                            time.sleep(10)

                        time.sleep(30)

                        if (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            winsound.Beep(500, 100)
                            
                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                                time.sleep(15)

                        time.sleep(210)

                        p = 1                
                        
                    elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                            time.sleep(15)

                q = 0

                while q < 1:

                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                            time.sleep(10) 

                        q = 1                
                        
                    elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                            time.sleep(15)
                            
                    else:
                        time.sleep(20)

                r = 0

                while r < 1:

                    if (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('2ndHalf.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2ndHalf.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('2ndHalf.png'))
                            time.sleep(10)
                        
                        time.sleep(30)

                        if (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            winsound.Beep(500, 100)
                            
                            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                                winsound.Beep(2000, 100)
                                time.sleep(2)
                                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                                time.sleep(15)

                        time.sleep(210)

                        r = 1                
                        
                    elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                            time.sleep(15)

                s = 0

                while s < 1:

                    if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                            time.sleep(10) 

                        s = 1
                        
                    elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        winsound.Beep(500, 100)
                        
                        while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                            pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                            winsound.Beep(2000, 100)
                            time.sleep(2)
                            pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                            time.sleep(15)
                            
                    else:
                        time.sleep(20)

        if (pyautogui.locateCenterOnScreen('Next.png') is not None):
            winsound.Beep(500, 100)
                    
            while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                time.sleep(10)

        if (pyautogui.locateCenterOnScreen('PContExpOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('PContExpOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('PContExpOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('PContExpOK.png'))
                time.sleep(10)

            l = 0
            
            while l < 1:
        
                if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                        time.sleep(10)
                    
                    l = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            m = 0
             
            while m < 1:
        
                if (pyautogui.locateCenterOnScreen('Proceed.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('Proceed.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Proceed.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Proceed.png'))
                        time.sleep(10)
                    
                    m = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

        if (pyautogui.locateCenterOnScreen('ExtAchOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('ExtAchOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ExtAchOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ExtAchOK.png'))
                time.sleep(10)

            t = 0
            
            while t < 1:
        
                if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                        time.sleep(10)
                    
                    t = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

        if (pyautogui.locateCenterOnScreen('ContExpOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('ContExpOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExpOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ContExpOK.png'))
                time.sleep(10)

            g = 0
            
            while g < 1:
        
                if (pyautogui.locateCenterOnScreen('Sign.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('Sign.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Sign.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Sign.png'))
                        time.sleep(10)
                    
                    g = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            h = 0
            
            while h < 1:
        
                if (pyautogui.locateCenterOnScreen('ContExtOK.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('ContExtOK.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ContExtOK.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ContExtOK.png'))
                        time.sleep(10)
                    
                    h = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            j = 0
            
            while j < 1:
        
                if (pyautogui.locateCenterOnScreen('ReqUpOK.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('ReqUpOK.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('ReqUpOK.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('ReqUpOK.png'))
                        time.sleep(10)
                    
                    j = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

            n = 0

            while n < 1:
        
                if (pyautogui.locateCenterOnScreen('Next.png') is not None):
                    winsound.Beep(500, 100)
                            
                    while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                        time.sleep(10)
                    
                    n = 1

                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)
                  
        if (pyautogui.locateCenterOnScreen('Next.png') is not None):
            winsound.Beep(500, 100)
                    
            while (pyautogui.locateCenterOnScreen('Next.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Next.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Next.png'))
                time.sleep(10)

        if (pyautogui.locateCenterOnScreen('OKCampPro.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('OKCampPro.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampPro.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('OKCampPro.png'))
                time.sleep(10)
            
            k = 0

            while k < 1:

                if (pyautogui.locateCenterOnScreen('OKCampBon.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('OKCampBon.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('OKCampBon.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('OKCampBon.png'))
                        time.sleep(10) 

                    k = 1                
                    
                elif (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                    winsound.Beep(500, 100)
                    
                    while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                        pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                        winsound.Beep(2000, 100)
                        time.sleep(2)
                        pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                        time.sleep(15)

        if (pyautogui.locateCenterOnScreen('TSUpOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('TSUpOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('TSUpOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('TSUpOK.png'))
                time.sleep(10)

        if (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('RedOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('RedOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('RedOK.png'))
                time.sleep(10)

        if (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
            winsound.Beep(500, 100)
            
            while (pyautogui.locateCenterOnScreen('2YelOK.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('2YelOK.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('2YelOK.png'))
                time.sleep(10)
   
        if (pyautogui.locateCenterOnScreen('Retry.png') is not None):
            winsound.Beep(500, 100)
                    
            while (pyautogui.locateCenterOnScreen('Retry.png') is not None):
                pyautogui.mouseDown(pyautogui.locateCenterOnScreen('Retry.png'))
                winsound.Beep(2000, 100)
                time.sleep(2)
                pyautogui.mouseUp(pyautogui.locateCenterOnScreen('Retry.png'))
                time.sleep(15)

sim()