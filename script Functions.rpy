default HolderCount = 1
init python:
    
#            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 3)
#            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 3)
#            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 4)
#            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 1)
#            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
#            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
#            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
    
# This updates a stat based on the call "$ statname = Statupdate("Rogue", statname, checked percent, amount changed, 1 if >)"  eg: $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 12)
    
    
    def Statupdate(Name, Flavor, Type, Check=100, Value=1, Greater=0):
        
        if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                Check = Check * 10                  #bumps this stat into the 1000s
        
        if Greater:                             #this checks if it's greater or less than the intended value
                if Type >= Check:
                    Type += Value                   #If it passes the check, add Value to it 
                else:
                    Value = 0                       #If not, don't add Value and set Value to 0
        else:
                if Type <= Check:
                    Type += Value  
                else:
                    Value = 0
                
        if Value:                                       #If there is any change to the stat
                        
            if Type > 1000:                              #If the value would overflow the stat, on Rogue
                if Name == "Rogue" and R_Chat[4]:
                        global R_Love
                        global R_Obed                    
                        global R_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if R_Chat[4] == 1:
                                    R_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 2:
                                    R_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if R_Chat[4] == 3:
                                    R_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif R_Chat[4] == 4:
                                    R_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if R_Chat[4] == 5:
                                    R_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 6:
                                    R_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        R_Love = 1000 if R_Love > 1000 else R_Love  #fix, check this works, not sure.
                        R_Obed = 1000 if R_Obed > 1000 else R_Obed
                        R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt
                #End Rogue content
                        
                elif Name == "Kitty" and K_Chat[4]:
                        global K_Love
                        global K_Obed                    
                        global K_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if K_Chat[4] == 1:
                                    K_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 2:
                                    K_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if K_Chat[4] == 3:
                                    K_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif K_Chat[4] == 4:
                                    K_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if K_Chat[4] == 5:
                                    K_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 6:
                                    K_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        K_Love = 1000 if K_Love > 1000 else K_Love  #fix, check this works, not sure.
                        K_Obed = 1000 if K_Obed > 1000 else K_Obed
                        K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt
                #End Kitty content
                
                elif Name == "Emma" and E_Chat[4]:
                        global E_Love
                        global E_Obed                    
                        global E_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if E_Chat[4] == 1:
                                    E_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 2:
                                    E_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if E_Chat[4] == 3:
                                    E_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif E_Chat[4] == 4:
                                    E_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if E_Chat[4] == 5:
                                    E_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 6:
                                    E_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        E_Love = 1000 if E_Love > 1000 else E_Love  #fix, check this works, not sure.
                        E_Obed = 1000 if E_Obed > 1000 else E_Obed
                        E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt
                #End Emma content

                elif Name in ModdedGirls and newgirl[Name].Chat[4]:
                        #global newgirl["Mystique"].Love
                        #global newgirl["Mystique"].Obed                    
                        #global newgirl["Mystique"].Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if newgirl[Name].Chat[4] == 1:
                                    newgirl[Name].Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif newgirl[Name].Chat[4] == 2:
                                    newgirl[Name].Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if newgirl[Name].Chat[4] == 3:
                                    newgirl[Name].Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif newgirl[Name].Chat[4] == 4:
                                    newgirl[Name].Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if newgirl[Name].Chat[4] == 5:
                                    newgirl[Name].Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif newgirl[Name].Chat[4] == 6:
                                    newgirl[Name].Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        newgirl[Name].Love = 1000 if newgirl[Name].Love > 1000 else newgirl[Name].Love  #fix, check this works, not sure.
                        newgirl[Name].Obed = 1000 if newgirl[Name].Obed > 1000 else newgirl[Name].Obed
                        newgirl[Name].Inbt = 1000 if newgirl[Name].Inbt > 1000 else newgirl[Name].Inbt
                #End Mystique content
                
                Type = 1000
                
                
            #I need to change this bit with the following line: 
#            if Flavor == "Lust" and Value >= 100 and not Trigger:
#                if Name == "Rogue":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("R_Cumming")
#                elif Name == "Kitty":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("K_Cumming")
#                elif Name == "Emma":        #calls orgasm if Lust goes over 100, breaks routine
#                    renpy.call("E_Cumming")
                    
            
            if Flavor == "Love":                        #Sets reporting text color based on Flavor
                    Color = "#c11b17"
            elif Flavor == "Obed":
                    Color = "#2554c7"
            elif Flavor == "Inbt":
                    Color = "#FFF380"
            elif Flavor == "Lust":
                    Color = "#FAAFBE"
            else:
                    Color = "#FFFFFF"
            
            if Name == "Rogue":
                    XPOS = R_SpriteLoc
            elif Name == "Kitty":
                    XPOS = K_SpriteLoc
            elif Name == "Emma":
                    XPOS = E_SpriteLoc
            elif Name in ModdedGirls:
                    XPOS = newgirl[Name].SpriteLoc
            else:
                    XPOS = 0.75
                
            CallHolder(Value, Color, XPOS)
                            
        if Type < 0:                                    #If Type ends up less than zero, set it to zero
            Type = 0
            
        return Type
  
    def CallHolder(Value, Color, XPOS):        
            global HolderCount
            
            if HolderCount == 1:                        #Shows the "+3" style feedback screen
                    renpy.show_screen("StatHolder1", Value, Color, XPOS)
            elif HolderCount == 2:
                    renpy.show_screen("StatHolder2", Value, Color, XPOS)
            elif HolderCount == 3:
                    renpy.show_screen("StatHolder3", Value, Color, XPOS)
            elif HolderCount == 4:
                    renpy.show_screen("StatHolder4", Value, Color, XPOS)        
            elif HolderCount == 5:
                    renpy.show_screen("StatHolder5", Value, Color, XPOS)
            else:           #== 6:
                    renpy.show_screen("StatHolder6", Value, Color, XPOS)
                
            HolderCount += 1 if HolderCount <= 6 else -5                             #Resets holder screens when it maxes out.
            
            return

    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)
    Shake = renpy.curry(_Shake)
    #


    
transform StatAnimation(Timer, XPOS):                         #this is the animation for the Stat ticker
    alpha 0
    pause Timer
#    xpos 0.75 ypos 0.15 alpha 1 #original version that works
    xpos XPOS ypos 0.15 alpha 1
#    linear 1 ypos 0.0 alpha 0
    parallel:
        linear 1 ypos 0.0
    parallel:
        pause .5
        linear .5 alpha 0
    
screen StatGraphic(Value, Color, Timer, XPOS):                #this displays the stat ticker when called
        showif Value > 0:
            text "+[Value]" size 30 color Color at StatAnimation(Timer, XPOS)
        else:
            text "[Value]" size 30 color Color at StatAnimation(Timer, XPOS)    
        
screen StatHolder1(Value, Color, XPOS):                       #This cycles through the possible stat ticker frameworks
        use StatGraphic(Value, Color, 0.0, XPOS)
        timer 1.0 action Hide("StatHolder1") 
screen StatHolder2(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.2, XPOS)
        timer 1.2 action Hide("StatHolder2") 
screen StatHolder3(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.4, XPOS)
        timer 1.4 action Hide("StatHolder3") 
screen StatHolder4(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.6, XPOS)
        timer 1.6 action Hide("StatHolder4")    
screen StatHolder5(Value, Color, XPOS):
        use StatGraphic(Value, Color, 0.8, XPOS)
        timer 1.8 action Hide("StatHolder5") 
screen StatHolder6(Value, Color, XPOS):
        use StatGraphic(Value, Color, 1.0, XPOS)
        timer 2.0 action Hide("StatHolder6") 
    
# End Stat update function. . .

init python:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#this function checks how many of "item" are in the player's inventory

    def Inventory_Check(Item = "item", Count = 0):      
            if Item in P_Inventory:
                Count = P_Inventory.count(Item) 
            else:
                Count = 0
            return Count
       
#This function checks how many times you've accessed a given action within the timeframe specified. Example: $ Count = Action_Check("Rogue", "recent", "sex")   
    def Action_Check(Chr = "Rogue", Time = "recent", Act = "act", Count = 0): 
            if Chr == "Rogue" and Time == "recent":
                if Act in R_RecentActions:
                    Count = R_RecentActions.count(Act) 
            elif Chr == "Rogue":
                if Act in R_DailyActions:
                    Count = R_DailyActions.count(Act) 
            elif Chr == "Kitty" and Time == "recent":
                if Act in K_RecentActions:
                    Count = K_RecentActions.count(Act) 
            elif Chr == "Kitty":
                if Act in K_DailyActions:
                    Count = K_DailyActions.count(Act) 
            elif Chr == "Emma" and Time == "recent":
                if Act in E_RecentActions:
                    Count = E_RecentActions.count(Act) 
            elif Chr == "Emma":
                if Act in E_DailyActions:
                    Count = E_DailyActions.count(Act) 
            elif Chr in ModdedGirls and Time == "recent":
                if Act in newgirl[Chr].RecentActions:
                    Count = newgirl[Chr].RecentActions.count(Act) 
            elif Chr in ModdedGirls:
                if Act in newgirl[Chr].DailyActions:
                    Count = newgirl[Chr].DailyActions.count(Act) 
                    
            return Count


    
                        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Personality(Chr = "Rogue", Type = "high", Love = 0): #Determines character personality choices. ie Personality("Rogue", "high", 0)
        if Chr == "Rogue":                              #sets the data based on Rogue's data            
                L = R_Love
                O = R_Obed
                I = R_Inbt
                if R_Chat[4]:
                    if R_Chat[4] == 1 or R_Chat[4] == 5:
                        return "Obed"  
                    elif R_Chat[4] == 2 or R_Chat[4] == 3:
                        return "Inbt" 
                    elif R_Chat[4] == 4 or R_Chat[4] == 6:
                        return "Love" 
        
        L = L - Love                            #can subtract a value to balance out love advantage
        
        if Type == "high":                      #Picks out highest stat of three
                if L >= O and L >= I:
                    return "Love"  
                elif O >= L and O >= I:
                    return "Obed"   
                else:
                    return "Inbt"
                
        if Type == "LO":                        #picks out highest of two values
                if L >= O:
                    return "Love"           
                else:
                    return "Obed" 
        if Type == "OI":
                if O >= I:
                    return "Obed"           
                else:
                    return "Inbt"
        if Type == "LI":
                if L >= I:
                    return "Love"           
                else:
                    return "Inbt"
            
        if Type == "LOI":
                if L >= O >= I:
                    return "LOI"
                elif L >= I >= O:
                    return "LIO"            
                elif O >= L >= I:
                    return "OLI"
                elif O >= I >= L:
                    return "OIL"
                elif I >= L >= O:
                    return "ILO"
                else:
                    return "IOL"
                
        return 1
                
                
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def ApprovalCheck(Chr = "Rogue", T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check = 0):  
        # $ Count = ApprovalCheck(125, Chr="Rogue")
        # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
        # TmpM is Tempmod multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location

        if Chr == "Kitty":                                     
                #sets the data based on Kitty's data
                L = K_Love
                O = K_Obed
                I = K_Inbt
                Loc = K_Loc if not Loc else Loc
        elif Chr == "Emma":                                      
                #sets the data based on Emma's data
                L = E_Love
                O = E_Obed
                I = E_Inbt
                Loc = E_Loc if not Loc else Loc
        elif Chr == "Rogue":                                 
                #sets the data based on Rogue's data
                L = R_Love
                O = R_Obed
                I = R_Inbt
                Loc = R_Loc if not Loc else Loc
        elif Chr in ModdedGirls:                                 
                #sets the data based on Rogue's data
                L = newgirl[Chr].Love
                O = newgirl[Chr].Obed
                I = newgirl[Chr].Inbt
                Loc = newgirl[Chr].Loc if not Loc else Loc
        
        if Loc == bg_current:
                #Bumps stats based on colognes
                if "mandrill" in P_Traits and C:                      
                        if L <= 500:
                            L += 500
                        else:
                            L = 1000
                elif "purple" in P_Traits and C:
                        if O <= 500:
                            O += 500
                        else:
                            O = 1000
                elif "corruption" in P_Traits and C:
                        if I <= 500:
                            I += 500
                        else:
                            I = 1000
       
        
        if Type == "LOI":
                LocalTaboo = Taboo * 10
                LocalTempmod = Tempmod * 10
                
        elif Type == "LO":                      #40 -> 240
                #culls unwanted parameters.
                #These bits multiply everything from the 0-300 range to the 0-3000 range  
                I = 0
                LocalTaboo = Taboo * 6                              
                LocalTempmod = Tempmod * 6
        elif Type == "OI":
                L = 0
                LocalTaboo = Taboo * 6
                LocalTempmod = Tempmod * 6
        elif Type == "LI":
                O = 0
                LocalTaboo = Taboo * 6      
                LocalTempmod = Tempmod * 6
                
        elif Type == "L":                       #40 -> 120
                O = 0
                I = 0
                LocalTaboo = Taboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "O":
                L = 0
                I = 0
                LocalTaboo = Taboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "I":
                O = 0
                L = 0
                LocalTaboo = Taboo * 3      
                LocalTempmod = Tempmod * 3
                
        else:            
                LocalTaboo = Taboo * 10         #40 -> 400
                LocalTempmod = Tempmod * 10
        
        TabM = 0 if TabM <= 0 else TabM #test this, makes sure TabM is positive

        if Check:
                #this returns the actual value of the tested stat.
                Check = (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo))
                return Check  
        
        if (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + (2 * Spread)):                           
                #She passes and loves it
                return 3    
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + Spread):                                  
                #She passes
                return 2
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= T:                         
                #She doesn't really want to, but can be convinced
                return 1
        else:                                                                                                   #She's out
                return 0

#end approval function //////////////////////////////////////////////////////////////////////////////

    def Room_Full(Present = []):
        # Culls parties down to 3 max
        # if Room_Full(): do something to empty it. 
        
        Present = []
        global Party
        while len(Party) > 3:    
                # If 3 or more members in the party    
                #Culls down party size to 3
                Party.remove(Party[3])   
        
        # checks to see which girls are present at a given location
        # adds members who are not currently in the party
        if R_Loc == bg_current:
            if "Rogue" not in Party:        
                Present.append("Rogue")
        if K_Loc == bg_current:
            if "Kitty" not in Party:         
                Present.append("Kitty") 
        if E_Loc == bg_current:
            if "Emma" not in Party: 
                Present.append("Emma")
        for eachnewgirl in ModdedGirls:
            if newgirl[eachnewgirl].Loc == bg_current:
                if eachnewgirl not in Party: 
                    Present.append(eachnewgirl) 
        
        if len(Party) + len(Present) >= 3:                
            return 1      
        else:
            return 0   
            
    #end RoomFull


    def HoseNum(Chr = "Rogue"): 
            #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                if Chr == "Rogue":
                            if R_Hose == "stockings":
                                return 1
                            elif R_Hose == "pantyhose":
                                return 6
                            elif R_Hose == "tights":
                                return 10
                            elif R_Hose == "ripped pantyhose":
                                return 5
                            elif R_Hose == "ripped tights":
                                return 5
                            elif R_Hose == "fishnet":
                                return 1
                            elif R_Hose == "SR7 hose":
                                return 1
                            else:
                                return 0
                                
                elif Chr == "Kitty":
                            if K_Hose == "stockings":
                                return 1
                            else:
                                return 0
                elif Chr == "Emma":
                            if E_Hose == "stockings":
                                return 1
                            else:
                                return 0
                elif Chr in ModdedGirls:
                            if newgirl[Chr].Hose == "stockings":
                                return 1
                            else:
                                return 0
                                
                #if it falls though. . .        
                return 0 
            
    def PantsNum(Chr = "Rogue"): 
            #This function determines how much pants are on, 10 for pants, 5 for shorts, <5 for less.
                if Chr == "Rogue":
                        if R_Legs == "skirt":
                            return 3
                        elif R_Legs == "skirtshort":            
                             return 3
                        elif R_Legs == "SR7 skirtshort":            
                             return 3
                        elif R_Legs == "cheerleader skirt":                 
                            return 3
                        elif R_Legs == "cheerleader skirtshort":            
                            return 3
                        elif R_Legs == "pants":
                            return 10
                        elif R_Legs == "shorts":
                            return 5
                        elif R_Legs == "blue shorts":
                            return 5
                        elif R_Legs == "red shorts":
                            return 5
                        elif R_Legs == "leather pants":
                            return 10
                        else:
                            return 0
                elif Chr == "Kitty":
                        if K_Legs == "black jeans":
                            return 10            
                        elif K_Legs == "capris":
                            return 10    
                        elif K_Legs == "yoga pants":
                            return 10 
                        elif K_Legs == "leather pants":
                            return 10 
                        elif K_Legs == "black blue pants":
                            return 10 
                        elif K_Legs == "shorts":
                            return 5
                        elif K_Legs == "blue shorts":
                            return 5
                        elif K_Legs == "white shorts":
                            return 5
                        elif K_Legs == "orange skirt":
                            return 3
                        elif K_Legs == "black skirt":
                            return 3
                        elif K_Legs == "white skirt":
                            return 3
                        else:
                            return 0
                elif Chr == "Emma":
                        if E_Legs == "pants":
                            return 10 
                        elif E_Legs == "black pants":
                            return 10   
                        elif E_Legs == "skirt":
                            return 3 
                        else:
                            return 0
                elif Chr in ModdedGirls:
                        if newgirl[Chr].Legs == "pants":
                            return 10
                        if newgirl[Chr].Legs == "workout pants":
                            return 10
                        elif newgirl[Chr].Legs == "skirt":
                            return 3
                        elif newgirl[Chr].Legs == "black skirt":
                            return 3
                        elif newgirl[Chr].Legs == "split skirt":
                            return 3
                        else:
                            return 0
                            
                #if it falls though. . .
                return 0 

    def ChestNum(Chr = "Rogue"): 
            #This function determines how much pants are on, 10 for pants, 5 for shorts, <5 for less.

                if Chr == "Rogue":
                        if R_Chest == "tank":
                            return 2
                        elif R_Chest == "buttoned tank":
                            return 2
                        elif R_Chest == "cheerleader":
                            return 2
                        elif R_Chest == "green crop top":
                            return 2
                        elif R_Chest == "black crop top":
                            return 2
                        elif R_Chest:
                            return 1

                #if nothing else:
                return 0 

    def BodySuitTopCoverage(Chr = "Rogue"): 
            #This function determines how much pants are on, 10 for pants, 5 for shorts, <5 for less.

                if Chr == "Rogue":
                        if R_BodySuit == "classic uniform":
                            return 100
                        elif R_BodySuit == "swimsuit1":
                            return 80
                        elif R_BodySuit == "swimsuit2":
                            return 50
                        

                #if nothing else:
                return 0 

    def BodySuitBottomCoverage(Chr = "Rogue"): 
            #This function determines how much pants are on, 10 for pants, 5 for shorts, <5 for less.

                if Chr == "Rogue":
                        if R_BodySuit == "classic uniform":
                            return 100
                        elif R_BodySuit == "swimsuit1":
                            return 20 # = regular panties
                        elif R_BodySuit == "swimsuit1":
                            return 10 # = regular panties
                        

                #if nothing else:
                return 0 
            
    def ClothingCheck(Chr = "Rogue", C = 0): 
            #This function counts how many items of clothing she has on and returns that number.
                if Chr == "Rogue":
                        if R_Over:
                            C += 1
                        if R_Chest:
                            C += 1
                        if R_Legs:
                            C += 1
                        if HoseNum("Rogue") >= 5:
                            C += 1
                        if R_Panties:
                            C += 1
                elif Chr == "Kitty":
                        if K_Over:
                            C += 1
                        if K_Chest:
                            C += 1
                        if K_Legs:
                            C += 1
                        if HoseNum("Kitty") >= 5:
                            C += 1
                        if K_Panties:
                            C += 1
                elif Chr == "Emma":
                        if E_Over:
                            C += 1
                        if E_Chest:
                            C += 1
                        if E_Legs:
                            C += 1
                        if HoseNum("Emma") >= 5:
                            C += 1
                        if E_Panties:
                            C += 1
                elif Chr in ModdedGirls:
                        if newgirl[Chr].Over:
                            C += 1
                        if newgirl[Chr].Chest:
                            C += 1
                        if newgirl[Chr].Legs:
                            C += 1
                        if HoseNum(Chr) >= 5:
                            C += 1
                        if newgirl[Chr].Panties:
                            C += 1
                return C 

    def GirlLikeCheck(GirlA=0,GirlB=0):
            # returns how much A likes B
            # if GirlLikeCheck("Rogue","Kitty") >= 500:
            
            if GirlA == "Rogue":  
                    if GirlB == "Kitty":
                                return R_LikeKitty
                    elif GirlB == "Emma":
                                return R_LikeEmma
                    elif GirlB in ModdedGirls:
                                return R_LikeNewGirl[GirlB]
            elif GirlA == "Kitty":  
                    if GirlB == "Rogue":
                                return K_LikeRogue
                    elif GirlB == "Emma":
                                return K_LikeEmma
                    elif GirlB in ModdedGirls:
                                return K_LikeNewGirl[GirlB]
            elif GirlA == "Emma":  
                    if GirlB == "Rogue":
                                return E_LikeRogue
                    elif GirlB == "Kitty":
                                return E_LikeKitty
                    elif GirlB in ModdedGirls:
                                return E_LikeNewGirl[GirlB]
            elif GirlA in ModdedGirls:  
                    if GirlB == "Rogue":
                                return newgirl[GirlA].LikeRogue
                    elif GirlB == "Kitty":
                                return newgirl[GirlA].LikeKitty
                    elif GirlB == "Emma":
                                return newgirl[GirlA].LikeEmma
                    elif GirlB in ModdedGirls:
                                return newgirl[GirlA].LikeNewGirl[GirlB]
            return 0
            
    def LauraBJShowing:
        if renpy.showing("Laura_BJ_Body_0") or renpy.showing("Laura_BJ_Body_1") or renpy.showing("Laura_BJ_Body_2") or renpy.showing("Laura_BJ_Body_3") or renpy.showing("Laura_BJ_Body_4") or renpy.showing("Laura_BJ_Body_5") or renpy.showing("Laura_BJ_Body_6"):
            return True
        else
            return 0


label Statup(Name=0, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Overflow=0, BStat=0, XPOS = 0.75):
        # Name is the target girl
        # "Flavor" is the thing being modified, such as Love
        # Type is the base value of that stat
        # Check is the maximum threshold, it won't raise if already above that value
        # Greater reverses the above check
        # Value is the amount raised
        # Overflow checks whether you've assigned a stat overflow
        # BStat stores the leftovers in the overflowed stat
        
        if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                #bumps this stat into the 1000s
                $ Check = Check * 10                  
        
        if Name == "Rogue":
                #sets the details based on character
                if Flavor == "Love":
                        $ Type = R_Love
                elif Flavor == "Obed":
                        $ Type = R_Obed
                elif Flavor == "Inbt":
                        $ Type = R_Inbt
                elif Flavor == "Lust":
                        $ Type = R_Lust
                $ Overflow = R_Chat[4]
                $ XPOS = R_SpriteLoc
        elif Name == "Kitty":
                if Flavor == "Love":
                        $ Type = K_Love
                elif Flavor == "Obed":
                        $ Type = K_Obed
                elif Flavor == "Inbt":
                        $ Type = K_Inbt
                elif Flavor == "Lust":
                        $ Type = K_Lust
                $ Overflow = K_Chat[4]
                $ XPOS = K_SpriteLoc
        elif Name == "Emma":
                if Flavor == "Love":
                        $ Type = E_Love
                elif Flavor == "Obed":
                        $ Type = E_Obed
                elif Flavor == "Inbt":
                        $ Type = E_Inbt
                elif Flavor == "Lust":
                        $ Type = E_Lust
                $ Overflow = E_Chat[4]
                $ XPOS = E_SpriteLoc
        elif Name == "Laura":
                if Flavor == "Love":
                        $ Type = newgirl["Laura"].Love
                elif Flavor == "Obed":
                        $ Type = newgirl["Laura"].Obed
                elif Flavor == "Inbt":
                        $ Type = newgirl["Laura"].Inbt
                elif Flavor == "Lust":
                        $ Type = newgirl["Laura"].Lust
                $ Overflow = newgirl["Laura"].Chat[4]
                $ XPOS = newgirl["Laura"].SpriteLoc
        # endset
        
        if Greater:                             
                #this checks if it's greater or less than the intended value
                #if it fails, the value is zeroed out, cancelling the rest
                if Type >= Check:
                    #If it passes the check, add Value to it 
                    $ Type += Value                   
                else:
                    #If not, don't add Value and set Value to 0
                    $ Value = 0                      
        else:
                if Type <= Check:
                    $ Type += Value  
                else:
                    $ Value = 0
        
                    
        if Value:                                       
            #If there is any change to the stat           
            if Flavor == "Love":                        
                    #Sets reporting text color based on Flavor
                    $ Color = "#c11b17"
            elif Flavor == "Obed":
                    $ Color = "#2554c7"
            elif Flavor == "Inbt":
                    $ Color = "#FFF380"
            elif Flavor == "Lust":
                    $ Color = "#FAAFBE"
            else: #Usually Focus
                    $ Color = "#FFFFFF"
                    $ CallHolder(Value, Color, XPOS)
                    return
                 
            if Type > 1000:    
                    #if the value overflows, play one value meter, then. . .
                    $ CallHolder((-(Type-1000-Value)), Color, XPOS)  
                    $ Value = Type - 1000
                    if Flavor == "Love":    
                            $ BStat = "Love"
                            if Overflow == 1:       #[Love to Obedience]
                                $ Flavor = "Obed"
                            elif Overflow == 2:     #[Love to Inhibition] 
                                $ Flavor = "Inbt"
                            else: 
                                $ Value = 0  
                    elif Flavor == "Obed":    
                            $ BStat = "Obed"
                            if Overflow == 3:       #[Obedience to Inhibition]
                                $ Flavor = "Obed"
                            elif Overflow == 4:    
                                $ Flavor = "Love"   #[Obedience to Love] 
                            else: 
                                $ Value = 0  
                    elif Flavor == "Inbt":    
                            $ BStat = "Inbt"
                            if Overflow == 5:       #[Inhibition to Obedience]
                                $ Flavor = "Obed"
                            elif Overflow == 6:    
                                $ Flavor = "Love"    #[Inhibition to Love]
                            else: 
                                $ Value = 0  
                               
                    if Flavor == "Love":                        
                            #Sets reporting text color based on Flavor
                            $ Color = "#c11b17"
                    elif Flavor == "Obed":
                            $ Color = "#2554c7"
                    elif Flavor == "Inbt":
                            $ Color = "#FFF380"
                    elif Flavor == "Lust":
                            $ Color = "#FAAFBE"
                    else:
                            $ Color = "#FFFFFF"
                    
            if Value:                
                $ CallHolder(Value, Color, XPOS)
            
            if Flavor == "Lust" and Type >= 100:
                if not Trigger:
                    #calls orgasm if Lust goes over 100, breaks routine
                    if Name == "Rogue":        
                        call R_Cumming
                    elif Name == "Kitty":     
                        call K_Cumming
                    elif Name == "Emma":    
                        call E_Cumming
                    elif Name == "Emma":    
                        call Laura_Cumming  
                    $ Value = 0
                    
        #end "if value is positive"
                    
        $ Type = 1000 if Type > 1000 else Type
        
        if Name == "Rogue":
                if Flavor == "Love":
                        $ R_Love += Value
                        $ R_Love = 1000 if R_Love > 1000 else R_Love
                elif Flavor == "Obed":
                        $ R_Obed += Value
                        $ R_Obed = 1000 if R_Obed > 1000 else R_Obed
                elif Flavor == "Inbt":
                        $ R_Inbt += Value
                        $ R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt
                elif Flavor == "Lust":
                        $ R_Lust += Value
                        $ R_Lust = 100 if R_Lust > 100 else R_Lust
                        
                if BStat == "Love":
                        $ R_Love = 1000
                elif BStat == "Obed":
                        $ R_Obed = 1000
                elif BStat == "Inbt":
                        $ R_Inbt = 1000
        elif Name == "Kitty":
                if Flavor == "Love":
                        $ K_Love += Value   
                        $ K_Love = 1000 if K_Love > 1000 else K_Love                     
                elif Flavor == "Obed":
                        $ K_Obed += Value
                        $ K_Obed = 1000 if K_Obed > 1000 else K_Obed 
                elif Flavor == "Inbt":
                        $ K_Inbt += Value
                        $ K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt 
                elif Flavor == "Lust":
                        $ K_Lust += Value
                        $ K_Lust = 100 if K_Lust > 100 else K_Lust 
                        
                if BStat == "Love":
                        $ K_Love = 1000
                elif BStat == "Obed":
                        $ K_Obed = 1000
                elif BStat == "Inbt":
                        $ K_Inbt = 1000
        elif Name == "Emma":
                if Flavor == "Love":
                        $ E_Love += Value
                        $ E_Love = 1000 if E_Love > 1000 else E_Love
                elif Flavor == "Obed":
                        $ E_Obed += Value
                        $ E_Obed = 1000 if E_Obed > 1000 else E_Obed
                elif Flavor == "Inbt":
                        $ E_Inbt += Value
                        $ E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt
                elif Flavor == "Lust":
                        $ E_Lust += Value
                        $ E_Lust = 100 if E_Lust > 100 else E_Lust
                        
                if BStat == "Love":
                        $ E_Love = 1000
                elif BStat == "Obed":
                        $ E_Obed = 1000
                elif BStat == "Inbt":
                        $ E_Inbt = 1000
        elif Name == "Laura":
                if Flavor == "Love":
                        $ newgirl["Laura"].Love += Value
                        $ newgirl["Laura"].Love = 1000 if newgirl["Laura"].Love > 1000 else newgirl["Laura"].Love
                elif Flavor == "Obed":
                        $ newgirl["Laura"].Obed += Value
                        $ newgirl["Laura"].Obed = 1000 if newgirl["Laura"].Obed > 1000 else newgirl["Laura"].Obed
                elif Flavor == "Inbt":
                        $ newgirl["Laura"].Inbt += Value
                        $ newgirl["Laura"].Inbt = 1000 if newgirl["Laura"].Inbt > 1000 else newgirl["Laura"].Inbt
                elif Flavor == "Lust":
                        $ newgirl["Laura"].Lust += Value
                        $ newgirl["Laura"].Lust = 100 if newgirl["Laura"].Lust > 100 else newgirl["Laura"].Lust
                        
                if BStat == "Love":
                        $ newgirl["Laura"].Love = 1000
                elif BStat == "Obed":
                        $ newgirl["Laura"].Obed = 1000
                elif BStat == "Inbt":
                        $ newgirl["Laura"].Inbt = 1000
                # endset
            
        return    

label RoomStatboost(Type=0,Check=0,Amount=0):
    # raises/lowers stats of all girls in the room by a fixed amount
    #ie call RoomStatboost("Love",80,2)
    if R_Loc == bg_current or "Rogue" in Nearby:
            call Statup("Rogue", Type, Check, Amount)
    if K_Loc == bg_current or "Kitty" in Nearby:
            call Statup("Kitty", Type, Check, Amount)
    if E_Loc == bg_current or "Emma" in Nearby:
            call Statup("Emma", Type, Check, Amount)
    if E_Loc == "bg teacher" and bg_current == "bg classroom":
            call Statup("Emma", Type, Check, Amount)
    if newgirl["Laura"].Loc == bg_current or "Laura" in Nearby:
            call Statup("Laura", Type, Check, Amount)
    return

label AnyFace(Girl=0,Emote = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
    #this sends a face change to any girl listed
    if Girl == "Rogue": 
                    call RogueFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
    elif Girl == "Kitty": 
                    call KittyFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
    elif Girl == "Emma": 
                    call EmmaFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
    elif Girl == "Laura": 
                    call LauraFace(Emote=Emote,B=B,M=M,Mouth=Mouth,Eyes=Eyes,Brows=Brows)
    return

label AnyLine(Girl=0,Line=". . ."):
    #This calls a line from any girl you reference
    if Girl == "Rogue":
            ch_r "[Line]"
    elif Girl == "Kitty":
            ch_k "[Line]"
    elif Girl == "Emma":
            ch_e "[Line]"
    elif Girl == "Laura":
            ch_l "[Line]"
    return

label AnyOutfit(Girl=0,OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1, Perm=0):
    #this sends a face change to any girl listed
    # "Perm" gets sent if the outfit is meant to stick
    if Girl == "Rogue": 
                    $ R_Outfit = OutfitTemp if Perm else R_Outfit
                    call RogueOutfit(OutfitTemp,Spunk,Undressed,Changed)
    elif Girl == "Kitty": 
                    $ K_Outfit = OutfitTemp if Perm else K_Outfit
                    call KittyOutfit(OutfitTemp,Spunk,Undressed,Changed)
    elif Girl == "Emma": 
                    $ E_Outfit = OutfitTemp if Perm else E_Outfit
                    call EmmaOutfit(OutfitTemp,Spunk,Undressed,Changed)
    elif Girl == "Laura": 
                    $ newgirl["Laura"].Outfit = OutfitTemp if Perm else newgirl["Laura"].Outfit
                    call LauraOutfit(OutfitTemp,Spunk,Undressed,Changed)
    return
    
label GirlLikesGirl(ChrA = "Rogue", ChrB = "Kitty", Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
        #ChrA is the subject girl, ChrB is the object girl, Modifier is sent as the amount of offense this might cause,
        # Jealousy is the temp value for how mad the girl will get
        
        if ChrA == "Rogue":                                             #If the first girl is Rogue
            if ChrB == "Kitty":                                         #If the second girl is Kitty  
                    if Auto: #this is a quick return, 
                            $ R_LikeKitty += Modifier
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/5)))
                            return
                        
                    #Establishes how jealous Rogue is likely to get
                    $ Jealousy = (R_Love - 600) if R_Love > 600 else 0              #How much her Love stat is over 600, +0-400
                    
                    $ Jealousy += 100 if "dating" in R_Traits and "poly kitty" not in R_Traits else 0 #adds Jealousy if not poly with Kitty, +0 or 100
                    
                    $ Jealousy += R_SEXP if R_Inbt <= 500 else 0                    #plus her SexP rating if she has low inhibitions, +0-200  
                    
                    $ Jealousy -= (R_Obed - 250) if R_Obed > 250 else 0             #minus how much her Obed stat is over 250, -0-750
                                                                                    # = result of up to 700 if high love, dating, and low obedience
                    $ Jealousy = 0 if Jealousy < 1 else Jealousy                    #Balances it to no less than zero
                    
                    $ Modifier += 1 if not Jealousy and R_LikeKitty >= 500 else 0   #+ modifier if she doesn't hate Kitty but has no jealousy left
                    
                     #this is for more nuanced comparisons            
                    if R_LikeKitty >= 900:          #If she really likes Kitty, then she is turned on, likes both of you more. 
                                $ R_LikeKitty += Modifier
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, (int(Modifier/2)))
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/5)))
                                $ Ok = 2
                    
                    elif R_LikeKitty >= 800:        #If she mostly likes Kitty, an is not super jealous, she likes you both more. 
                            if Jealousy <= 300:
                                $ R_LikeKitty += Modifier
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, (int(Modifier/2)))
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/2)))
                                $ Ok = 2
                            else:
                                $ R_LikeKitty -= Modifier                        
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/5)))
                                $ Ok = 1
                            
                    elif R_LikeKitty >= 600:        #If she's friends with Kitty, only low jealousy is positive
                            if Jealousy <= 100:
                                $ R_LikeKitty += Modifier                        
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, (int(Modifier/4)))                        
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/2)))
                                $ Ok = 2
                            elif Jealousy <= 300:
                                $ R_LikeKitty -= Modifier
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/2)))
                                $ Ok = 1
                            else:
                                $ R_LikeKitty -= (Modifier + (int(Jealousy/50)))
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, (-(int(Modifier)))) 
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/5)))

                    elif R_LikeKitty >= 400:        #If she is neutral to Kitty, it's all negative                 
                            if Jealousy <= 100:
                                $ R_LikeKitty -= Modifier
                                $ Ok = 1
                            else:
                                $ R_LikeKitty -= (Modifier + (int(Jealousy/100)))
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/10)))
                        
                    else:                           #If she hates Kitty, it's all very negative
                                $ R_LikeKitty -= (Modifier + (int(Jealousy/50)))
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Modifier/10))) 

                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, (int(Modifier/10)))                                                                         
                    #drops through to the final return
                            
        #End Rogue check        
        elif ChrA == "Kitty":
                if ChrB == "Rogue":                             #If the second girl is Rogue  
                    if Auto: #this is a quick return, 
                            $ K_LikeRogue += Modifier
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/5)))
                            return
                        
                    #Establishes how jealous Kitty is likely to get
                    $ Jealousy = (K_Love - 600) if K_Love > 600 else 0              #How much her Love stat is over 600, +0-400
                    
                    $ Jealousy += 100 if "dating" in K_Traits and "poly rogue" not in K_Traits else 0 #adds Jealousy if not poly with Rogue, +0 or 100
                    
                    $ Jealousy += K_SEXP if K_Inbt <= 500 else 0                    #plus her SexP rating if she has low inhibitions, +0-200  
                    
                    $ Jealousy -= (K_Obed - 200) if K_Obed > 200 else 0             #minus how much her Obed stat is over 250, -0-750
                                                                                    # = result of up to 700 if high love, dating, and low obedience
                    $ Jealousy = 0 if Jealousy < 1 else Jealousy                    #Balances it to no less than zero
                    
                    $ Modifier += 1 if not Jealousy and K_LikeRogue >= 500 else 0   #+ modifier if she doesn't hate Rogue but has no jealousy left
                    
                     #this is for more nuanced comparisons            
                    if K_LikeRogue >= 900:          #If she really likes Rogue, then she is turned on, likes both of you more. 
                                $ K_LikeRogue += Modifier
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, (int(Modifier/2)))
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/5)))
                                $ Ok = 2
                    
                    elif K_LikeRogue >= 800:        #If she mostly likes Rogue, an is not super jealous, she likes you both more. 
                            if Jealousy <= 300:
                                $ K_LikeRogue += Modifier
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, (int(Modifier/2)))
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/2)))
                                $ Ok = 2
                            else:
                                $ K_LikeRogue -= Modifier                        
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/5)))
                                $ Ok = 1
                            
                    elif K_LikeRogue >= 600:        #If she's friends with Rogue, only low jealousy is positive
                            if Jealousy <= 100:
                                $ K_LikeRogue += Modifier                        
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, (int(Modifier/4)))                        
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/2)))
                                $ Ok = 2
                            elif Jealousy <= 300:
                                $ K_LikeRogue -= Modifier
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/2)))
                                $ Ok = 1
                            else:
                                $ K_LikeRogue -= (Modifier + (int(Jealousy/50)))
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, (-(int(Modifier)))) 
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/5)))

                    elif K_LikeRogue >= 400:        #If she is neutral to Rogue, it's all negative                 
                            if Jealousy <= 100:
                                $ K_LikeRogue -= Modifier
                                $ Ok = 1
                            else:
                                $ K_LikeRogue -= (Modifier + (int(Jealousy/100)))
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/10)))
                            
                    else:                           #If she hates Rogue, it's all very negative
                                $ K_LikeRogue -= (Modifier + (int(Jealousy/50)))
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Modifier/10))) 

                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, (int(Modifier/10)))                                                                         
                    #drops through to the final return                    
        #End Kitty check
        
        return Ok

label GirlWaitAttract(Local=0,Teach=0,D20=0,Check=0):
    #This adjusts girl's liking each other based on shared activities
    #Local =1 only checks if they are in the room with you.
    $ D20 = renpy.random.randint(0, 1) 
    if E_Loc == "bg teacher":
        $ E_Loc == "bg classroom" #Sets Emma to being in class if she's teaching
        $ Teach = 1
        
    if R_Loc == K_Loc:            
            #This adjusts how much Rogue and Kitty like each other if they are in the same room 
            if not Local or R_Loc == bg_current:
                if R_Loc == "bg classroom":
                        $ R_LikeKitty += 1 if R_LikeKitty <= 70 else 0
                        $ K_LikeRogue += 1 if K_LikeRogue <= 70 else 0
                elif R_Loc == "bg dangerroom":
                        $ R_LikeKitty += (1+D20) if R_LikeKitty <= 70 else 0
                        $ K_LikeRogue += (1+D20) if K_LikeRogue <= 70 else 0
                elif R_Loc == "bg showerroom":  
                        $ R_LikeKitty += 2 if R_LikeKitty <= 90 else 0 
                        $ K_LikeRogue += 2 if K_LikeRogue <= 90 else 0
                else:
                        $ R_LikeKitty += D20 if R_LikeKitty <= 70 else 0 
                        $ K_LikeRogue += D20 if K_LikeRogue <= 70 else 0
                        
                $ R_LikeKitty += (int(K_Shame/5)) if R_LikeKitty >= 70 else 0 #Rogue likes Kitty based on how slutty Kitty looks
                $ K_LikeRogue += (int(R_Shame/5)) if K_LikeRogue >= 70 else 0 #Kitty likes Rogue based on how slutty Rogue looks                 
    if R_Loc == E_Loc:   
            #This adjusts how much Rogue and Emma like each other if they are in the same room    
            if not Local or R_Loc == bg_current:    
                if R_Loc == "bg classroom":
                        $ R_LikeEmma += 1 if R_LikeEmma <= 70 else 0
                        $ E_LikeRogue += 1 if E_LikeRogue <= 70 else 0
                elif R_Loc == "bg dangerroom":
                        $ R_LikeEmma += (1+D20) if R_LikeEmma <= 70 else 0
                        $ E_LikeRogue += (1+D20) if E_LikeRogue <= 70 else 0
                elif R_Loc == "bg showerroom":  
                        $ R_LikeEmma += 2 if R_LikeEmma <= 90 else 0 
                        $ E_LikeRogue += 3 if E_LikeRogue <= 90 else 0
                else:
                        $ R_LikeEmma += D20 if R_LikeEmma <= 70 else 0 
                        $ E_LikeRogue += D20 if E_LikeRogue <= 70 else 0
                        
                $ R_LikeEmma += (int(E_Shame/5)) if R_LikeEmma >= 70 else 0 #Rogue likes Emma based on how slutty Emma looks
                $ E_LikeRogue += (int(R_Shame/4)) if E_LikeRogue >= 70 else 0 #Emma likes Rogue based on how slutty Rogue looks                       
    if K_Loc == E_Loc:  
            #this adjusts how much Kitty and Emma like each other if they are in the same room 
            if not Local or K_Loc == bg_current:
                if K_Loc == "bg classroom":
                        $ K_LikeEmma += 1 if K_LikeEmma <= 70 else 0
                        $ E_LikeKitty += 1 if E_LikeKitty <= 70 else 0
                elif K_Loc == "bg dangerroom":
                        $ K_LikeEmma += (1+D20) if K_LikeEmma <= 70 else 0
                        $ E_LikeKitty += (1+D20) if E_LikeKitty <= 70 else 0
                elif K_Loc == "bg showerroom":  
                        $ K_LikeEmma += 2 if K_LikeEmma <= 90 else 0 
                        $ E_LikeKitty += 3 if E_LikeKitty <= 90 else 0
                else:
                        $ K_LikeEmma += D20 if K_LikeEmma <= 70 else 0 
                        $ E_LikeKitty += D20 if E_LikeKitty <= 70 else 0
                        
                $ K_LikeEmma += (int(E_Shame/5)) if K_LikeEmma >= 70 else 0 #Kitty likes Emma based on how slutty Emma looks
                $ E_LikeKitty += (int(K_Shame/4)) if E_LikeKitty >= 70 else 0 #Emma likes Kitty based on how slutty Kitty looks
    
    if Teach:
        $ E_Loc == "bg teacher" #Sets Emma to being a teacher again        
    return
    
label Faces(Character="All"):
    #This sets a default face for the girl
    if Character == "Rogue" or Character == "All":
            if R_Lust >= 50 and ApprovalCheck("Rogue", 1200):
                    $ R_Emote = "sexy"           
            elif R_Addict > 75:
                    $ R_Emote = "manic"
            elif R_Love >= R_Obed and R_Love >= 500:
                    $ R_Emote = "smile"      
            elif R_Inbt >= R_Obed and R_Inbt >= 500:
                    $ R_Emote = "smile"      
            elif R_Addict > 50:
                    $ R_Emote = "manic"
            elif (R_Love + R_Obed) < 300:
                    $ R_Emote = "angry"
            else:
                    $ R_Emote = "normal"
            call RogueFace from _call_RogueFace_256    
    
    if Character == "Kitty" or Character == "All":
            if K_Lust >= 50 and ApprovalCheck("Kitty", 1200):
                    $ K_Emote = "sexy"           
            elif K_Addict > 75:
                    $ K_Emote = "manic"
            elif K_Love >= K_Obed and K_Love >= 500:
                    $ K_Emote = "smile"      
            elif K_Inbt >= K_Obed and K_Inbt >= 500:
                    $ K_Emote = "smile"      
            elif K_Addict > 50:
                    $ K_Emote = "manic"
            elif (K_Love + K_Obed) < 300:
                    $ K_Emote = "angry"
            else:
                    $ K_Emote = "normal"
            call KittyFace from _call_KittyFace_248   
            
    if Character == "Emma" or Character == "All":
            if E_Lust >= 50 and ApprovalCheck("Emma", 1000):
                    $ E_Emote = "sexy"           
            elif E_Addict > 75:
                    $ E_Emote = "manic"
            elif E_Love >= E_Obed and E_Love >= 500:
                    $ E_Emote = "smile"      
            elif E_Inbt >= E_Obed and E_Inbt >= 500:
                    $ E_Emote = "smile"      
            elif E_Addict > 50:
                    $ E_Emote = "manic"
            elif (E_Love + E_Obed) < 300:
                    $ E_Emote = "angry"
            else:
                    $ E_Emote = "normal"
            call EmmaFace from _call_EmmaFace_440   

    if Character in ModdedGirls:
            if newgirl[Character].Lust >= 50 and ApprovalCheck(Character, 1000):
                    $ newgirl[Character].Emote = "sexy"           
            elif newgirl[Character].Addict > 75:
                    $ newgirl[Character].Emote = "manic"
            elif newgirl[Character].Love >= newgirl[Character].Obed and newgirl[Character].Love >= 500:
                    $ newgirl[Character].Emote = "smile"      
            elif newgirl[Character].Inbt >= newgirl[Character].Obed and newgirl[Character].Inbt >= 500:
                    $ newgirl[Character].Emote = "smile"      
            elif newgirl[Character].Addict > 50:
                    $ newgirl[Character].Emote = "manic"
            elif (newgirl[Character].Love + newgirl[Character].Obed) < 300:
                    $ newgirl[Character].Emote = "angry"
            else:
                    $ newgirl[Character].Emote = "normal"
            call NewGirl_Face("Mystique") from _call_NewGirl_Face_330   

    if Character == "All":
        $ allgirls = 0
        while allgirls < len(ModdedGirls):
            if newgirl[ModdedGirls[allgirls]].Lust >= 50 and ApprovalCheck(ModdedGirls[allgirls], 1000):
                    $ newgirl[ModdedGirls[allgirls]].Emote = "sexy"           
            elif newgirl[ModdedGirls[allgirls]].Addict > 75:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "manic"
            elif newgirl[ModdedGirls[allgirls]].Love >= newgirl[ModdedGirls[allgirls]].Obed and newgirl[ModdedGirls[allgirls]].Love >= 500:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "smile"      
            elif newgirl[ModdedGirls[allgirls]].Inbt >= newgirl[ModdedGirls[allgirls]].Obed and newgirl[ModdedGirls[allgirls]].Inbt >= 500:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "smile"      
            elif newgirl[ModdedGirls[allgirls]].Addict > 50:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "manic"
            elif (newgirl[ModdedGirls[allgirls]].Love + newgirl[ModdedGirls[allgirls]].Obed) < 300:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "angry"
            else:
                    $ newgirl[ModdedGirls[allgirls]].Emote = "normal"
            call NewGirl_Face(ModdedGirls[allgirls]) from _call_NewGirl_Face_331   
            $ allgirls += 1
    return
                   
label Activity_Check(Girl=0,Girl2=0,Silent=0,Removal=1,ClothesCheck=1,Mod=0,Approval=1,Tempshame=0):
        # This checks whether a girl is up for watching a given activity
        # Silent is whether it plays dialog or not, Removal is whether it auto-removes the girl on a fail,
        # ClothesCheck is whether it bothers checking clothing, 2 if skip first girl
        # Mod gets set to her Like stat -600, so 600 Like, you break even, otherwise it's a penalty
        # call Activity_Check("Rogue",0,1,0)
        if not Girl2 or ClothesCheck == 2:
                $ Mod = 0
        else:
                $ Mod = (GirlLikeCheck(Girl,Girl2)-600)
                if Girl in P_Harem and Girl2 in P_Harem: #bonus for if both in harem
                        $ Mod += 500
                        
        if ClothesCheck and Girl2:
                if Girl2 == "Rogue":
                        #sets her shame level to be accurate to current look
                        call Rogue_OutfitShame(20)
                        $ Tempshame = R_Shame
                elif Girl2 == "Kitty":
                        call Kitty_OutfitShame(20)
                        $ Tempshame = K_Shame
                elif Girl2 == "Emma":
                        call Emma_OutfitShame(20)
                        $ Tempshame = E_Shame
                elif Girl2 == "Laura":
                        call Laura_OutfitShame(20)
                        $ Tempshame = newgirl["Laura"].Shame
                
                if Tempshame <= 15 and (ApprovalCheck(Girl, 600,Bonus=Mod) or ApprovalCheck(Girl, 350, "I")):
                        #If the outfit is hot but she's ok     
                        if ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I"): 
                                $ Approval = 2   
                elif Tempshame <= 20 and (ApprovalCheck(Girl, 900,Bonus=Mod) or ApprovalCheck(Girl, 450, "I")):
                        #If the outfit is sexy but she's cool with that 
                        if ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I"): 
                                $ Approval = 2   
                elif Tempshame <= 25 and (ApprovalCheck(Girl, 1100,Bonus=Mod) or ApprovalCheck(Girl, 550, "I")):
                        #If the outfit is sexy but she's cool with that
                        if ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I"): 
                                $ Approval = 2    
                elif (ApprovalCheck(Girl, 1400,Bonus=Mod) or ApprovalCheck(Girl, 650, "I")):
                        #If the outfit is very scandelous but she's ok with that     
                        if ApprovalCheck(Girl, 1600,Bonus=Mod) or ApprovalCheck(Girl, 850, "I"): 
                                $ Approval = 2     
                        pass
                else:
                        $ Approval = 0
                        
        if not Approval:
                    # If it fails the clothing check, skip the next part
                    pass
        elif Trigger == "strip" and Trigger2 != "jackin":
                    pass #covered by the above check
        elif not Trigger:
                    pass
        elif Trigger == "lick ass":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = 3)
        elif Trigger == "anal":
                    $ Approval = ApprovalCheck(Girl,1550,Bonus=Mod, TabM = 3)
        elif Trigger == "sex":
                    $ Approval = ApprovalCheck(Girl,1400,Bonus=Mod, TabM = 3)
        elif Trigger == "lick pussy":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger2 == "jackin":            
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "blow":            
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = 2)
        elif Trigger == "titjob":              
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = 3) 
        elif Trigger == "hotdog":
                    $ Approval = ApprovalCheck(Girl,1000,Bonus=Mod, TabM = 3)                
        elif Trigger == "hand" or Trigger3 == "hand":              
                    $ Approval = ApprovalCheck(Girl,1100,Bonus=Mod, TabM = 2)
        elif Trigger == "foot":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)  
        elif Trigger == "dildo anal":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "dildo pussy":
                    $ Approval = ApprovalCheck(Girl,1250,Bonus=Mod, TabM = 2)
        elif Trigger == "insert ass":
                    $ Approval = ApprovalCheck(Girl,1300,Bonus=Mod, TabM = 2)
        elif Trigger == "fondle pussy" or Trigger == "insert pussy":
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = 2)
        elif Trigger == "suck breasts":            
                    $ Approval = ApprovalCheck(Girl,1050,Bonus=Mod, TabM = 3)
        elif Trigger == "fondle breasts":                        
                    $ Approval = ApprovalCheck(Girl,950,Bonus=Mod, TabM = 2)
        elif Trigger == "fondle ass":
                    $ Approval = ApprovalCheck(Girl,850,Bonus=Mod, TabM = 1)
                    
        elif Trigger == "masturbation": 
                    $ Approval = ApprovalCheck(Girl,1200,Bonus=Mod, TabM = 2)
                    
        elif Trigger == "kiss you":
                    $ Approval = ApprovalCheck(Girl,500,Bonus=Mod, TabM = 0)                    
        elif Trigger == "fondle thighs":
                    $ Approval = ApprovalCheck(Girl,750,Bonus=Mod, TabM = 0)
                    
        elif Trigger == "lesbian": 
                    $ Approval = ApprovalCheck(Girl,1350,Bonus=Mod, TabM = 2)                           
        
        if not Silent and not Approval:
            if Girl == "Rogue":
                    ch_r "Ain't none a this right, [R_Petname]."
            elif Girl == "Kitty":
                    ch_k "I'm[K_like]not really comfortable here?"
            elif Girl == "Emma":
                    ch_e "This has become a bit too. . . scandalous for my tastes."
            elif Girl == "Laura":
                    ch_l "This is getting weird."
        
        if Removal and not Approval:
                call Remove_Girl(Girl,2)  
                "[Girl] takes off."
                
        return Approval

# to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
label DrainWord(Character = "Rogue", Word = "word", Recent = 1, Daily = 1):
            if Character == "Kitty" or Character == "All":
                            if Word == "around" and Word in K_Traits:
                                while Word in K_Traits:
                                        $ K_Traits.remove(Word) 
                            if Word in K_RecentActions and Recent:
                                while Word in K_RecentActions:
                                        $ K_RecentActions.remove(Word) 
                            if Word in K_DailyActions and Daily:
                                while Word in K_DailyActions:
                                        $ K_DailyActions.remove(Word) 
            elif Character == "Emma" or Character == "All":
                            if Word in E_RecentActions and Recent:
                                while Word in E_RecentActions:
                                        $ E_RecentActions.remove(Word) 
                            if Word in E_DailyActions and Daily:
                                while Word in E_DailyActions:
                                        $ E_DailyActions.remove(Word) 
            elif Character == "Player":
                            if Word in P_RecentActions and Recent:
                                while Word in P_RecentActions:
                                        $ P_RecentActions.remove(Word) 
                            if Word in P_DailyActions and Daily:
                                while Word in P_DailyActions:
                                        $ P_DailyActions.remove(Word)  
            elif Character == "Rogue":
                            if Word == "around" and Word in R_Traits:
                                while Word in R_Traits:
                                        $ R_Traits.remove(Word) 
                            if Word in R_RecentActions and Recent:
                                while Word in R_RecentActions:
                                        $ R_RecentActions.remove(Word) 
                            if Word in R_DailyActions and Daily:
                                while Word in R_DailyActions:
                                        $ R_DailyActions.remove(Word)  
            elif Character in ModdedGirls or Character == "All":
                            if Word in newgirl[Character].RecentActions and Recent:
                                while Word in newgirl[Character].RecentActions:
                                        $ newgirl[Character].RecentActions.remove(Word) 
                            if Word in newgirl[Character].DailyActions and Daily:
                                while Word in newgirl[Character].DailyActions:
                                        $ newgirl[Character].DailyActions.remove(Word)    
            return



#This is intended to clear the room of non-essential characters
#the named character is the one who stays, everyone else is kicked out.
label CleartheRoom(Character = "Rogue", Passive = 0, Silent = 0, Check = 0):
            #Character is the one asking to clear the room. 
            #Passive is when the second person leaves on their own. 
            #Silent removes dialog
            # Check only checks to see if anyone is there. It will start at 1 and raise with each girl
            if Character != "Rogue" and (R_Loc == bg_current or "Rogue" in Party):     
                if not Check:
                    #if the character asking is not Rogue, this removes Rogue from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_r "I should get going, see you later, [R_Petname]."  
                    elif Character == "Kitty" and K_Loc == bg_current:
                        ch_k "[K_Like]could I talk to [Playername] alone for a sec?" 
                        ch_r "No problem, I'll see you later then." 
                    elif Character == "Emma" and E_Loc == bg_current:
                        ch_e "Kitty, would you mind if I had a word alone with [Playername]?" 
                        ch_r "No problem, I'll see you later then." 
                    else:
                        ch_r "I should get going, see you later, [R_Petname]."                          
                      
                    if "Rogue" in Party:
                            $ Party.remove("Rogue")  
                    if "leaving" in R_RecentActions:
                            call DrainWord("Rogue","leaving") from _call_DrainWord_71  
                    if "arriving" in R_RecentActions:
                            call DrainWord("Rogue","arriving") from _call_DrainWord_72 
                    if bg_current == "bg rogue":
                            #if the girl is not Rogue but you're in Rogue's room, the girl takes you to her room
                            call TaketoRoom(Character) from _call_TaketoRoom
                    else:
                            $ R_Loc = "bg rogue"
                    hide Rogue with easeoutright 
                else:
                    $ Check += 1                    
            if Character != "Kitty" and (K_Loc == bg_current or "Kitty" in Party):        
                if not Check:                        
                    #if the character asking is not Kitty, this removes Kitty from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_k "I think I'll head out, I'll see you later."  
                    elif Character == "Rogue" and R_Loc == bg_current:
                        ch_r "Kitty, could I talk to [Playername] alone for a minute?"
                        ch_k "[K_Like]sure, I'll see you later."      
                    elif Character == "Emma" and E_Loc == bg_current:
                        ch_e "Kitty, would you mind if I had a word alone with [Playername]?"
                        ch_k "[K_Like]sure, I'll see you later."                                  
                    else:
                        ch_k "I think I'll head out, I'll see you later."  
                        
                    if "Kitty" in Party:
                            $ Party.remove("Kitty")  
                    if "leaving" in K_RecentActions:
                            call DrainWord("Kitty","leaving") from _call_DrainWord_73  
                    if "arriving" in K_RecentActions:
                            call DrainWord("Kitty","arriving") from _call_DrainWord_74                   
                    if bg_current == "bg kitty":
                            #if the girl is not Kitty but you're in Kitty's room, the girl takes you to her room
                            call TaketoRoom(Character) from _call_TaketoRoom_1
                    else:
                            $ K_Loc = "bg kitty"                    
                    hide Kitty_Sprite with easeoutbottom 
                else:
                    $ Check += 1                 
                    
            if Character != "Emma" and (E_Loc == bg_current or "Emma" in Party):        
                if not Check:                        
                    #if the character asking is not Emma, this removes Emma from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_e "I think I should be going now."  
                    elif Character == "Rogue" and R_Loc == bg_current:
                        ch_r "Emma, could I talk to [Playername] alone for a minute?"
                        ch_e "Fine, I'll see you later then."  
                    elif Character == "Kitty" and K_Loc == bg_current:
                        ch_k "[K_Like]could I talk to [Playername] alone for a sec?" 
                        ch_e "Fine, I'll see you later then."         
                    else:
                        ch_e "I think I should be going now."   
                        
                    if "Emma" in Party:
                            $ Party.remove("Emma")  
                    if "leaving" in E_RecentActions:
                            call DrainWord("Emma","leaving") from _call_DrainWord_75  
                    if "arriving" in E_RecentActions:
                            call DrainWord("Emma","arriving") from _call_DrainWord_76                   
                    if bg_current == "bg emma":
                            #if the girl is not Emma but you're in Emma's room, the girl takes you to her room
                            call TaketoRoom(Character) from _call_TaketoRoom_2
                    else:
                            $ E_Loc = "bg emma"                    
                    hide Emma_Sprite with easeoutright
                else:
                    $ Check += 1    

            if Character != "Mystique" and (newgirl["Mystique"].Loc == bg_current or "Mystique" in Party):        
                if not Check:                        
                    #if the character asking is not Mystique, this removes Mystique from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_m "I think I should be going noww."  
                    elif Character == "Rogue" and R_Loc == bg_current:
                        ch_r "Mystique, could I talk to [Playername] alone for a minute?"
                        ch_m "Fine, I'll see you later then."  
                    elif Character == "Kitty" and K_Loc == bg_current:
                        ch_k "[K_Like]could I talk to [Playername] alone for a sec?" 
                        ch_m "Fine, I'll see you later then."         
                    else:
                        ch_m "I think I should be going now."   
                        
                    if "Mystique" in Party:
                            $ Party.remove("Mystique")  
                    if "leaving" in newgirl["Mystique"].RecentActions:
                            call DrainWord("Mystique","leaving") from _call_DrainWord_77  
                    if "arriving" in newgirl["Mystique"].RecentActions:
                            call DrainWord("Mystique","arriving") from _call_DrainWord_78                   
                    if bg_current == "bg Mystique":
                            #if the girl is not Mystique but you're in Mystique's room, the girl takes you to her room
                            call TaketoRoom(Character) from _call_TaketoRoom_3
                    else:
                            $ newgirl["Mystique"].Loc = "bg Mystique"                    
                    hide Mystique_Sprite with easeoutright
                else:
                    $ Check += 1   

            if Character != "Laura" and (newgirl["Laura"].Loc == bg_current or "Laura" in Party):        
                if not Check:                        
                    #if the character asking is not Laura, this removes Laura from the room
                    if Silent:
                        pass
                    elif Passive:
                        ch_l "I think I should be going noww."  
                    elif Character == "Rogue" and R_Loc == bg_current:
                        ch_r "Laura, could I talk to [Playername] alone for a minute?"
                        ch_l "Fine, I'll see you later then."  
                    elif Character == "Kitty" and K_Loc == bg_current:
                        ch_k "[K_Like]could I talk to [Playername] alone for a sec?" 
                        ch_l "Fine, I'll see you later then."         
                    else:
                        ch_l "I think I should be going now."   
                        
                    if "Laura" in Party:
                            $ Party.remove("Laura")  
                    if "leaving" in newgirl["Laura"].RecentActions:
                            call DrainWord("Laura","leaving")
                    if "arriving" in newgirl["Laura"].RecentActions:
                            call DrainWord("Laura","arriving")
                    if bg_current == "bg Laura":
                            #if the girl is not Laura but you're in Laura's room, the girl takes you to her room
                            call TaketoRoom(Character)
                    else:
                            $ newgirl["Laura"].Loc = "bg Laura"                    
                    hide Laura_Sprite with easeoutright
                else:
                    $ Check += 1   

            $ Check -= 1 if Check > 0 else 0 #removes the initial Check value
            return Check

label TaketoRoom(Girl = "Rogue"):
        if Girl == "Rogue":
                $ bg_current = "bg rogue"
                $ R_Loc = "bg rogue"
        elif Girl == "Kitty":
                $ bg_current = "bg kitty"
                $ K_Loc = "bg kitty"
        elif Girl == "Emma":                    
               $ bg_current = "bg emma"
               $ E_Loc = "bg emma"           
        elif Girl in ModdedGirls:                    
#                $ bg_current = "bg Mystique"
#                $ E_Loc = "bg Mystique"           
                $ bg_current = "bg playerroom"
                $ newgirl[Girl].Loc = "bg playerroom"
        call Set_The_Scene from _call_Set_The_Scene_107
        call CleartheRoom(Girl) from _call_CleartheRoom_13
        call Taboo_Level from _call_Taboo_Level_30
        if not Silent:
            "[Girl] brings you back to her room. . ."
        $ renpy.pop_call()
        return
        
label Round10(Options = ["none"]):    
        #Called when it's time to auto-wait/sleep
        if Current_Time == "Night":
                if bg_current == "bg rogue":
                        #If it's Rogue's room, she gets dibs
                        
                        if R_Loc != bg_current: 
                                #if you're in Rogue's room but she isn't here. . .
                                if R_Sleep >= 5: 
                                        call CleartheRoom("Rogue",1) from _call_CleartheRoom_14
                                        "She probably wouldn't mind you taking a quick nap. . ."
                                        call Wait from _call_Wait_25
                                        if R_Loc == bg_current:
                                                call DrainWord("Rogue","arriving") from _call_DrainWord_79
                                                ch_r "Morning, [R_Petname]. Sleep well?"
                                else:
                                        "She probably wouldn't appreciate you staying over, you head back to your own room."
                                        $ renpy.pop_call()
                                        jump Player_Room
                        call CleartheRoom("Rogue",1) from _call_CleartheRoom_15
                        call Rogue_Sleepover from _call_Rogue_Sleepover          
                elif bg_current == "bg kitty":         
                        #If it's Kitty's room, she gets dibs
                        
                        if K_Loc != bg_current: 
                                # if Kitty isn't around. . .
                                if K_Sleep >= 5: 
                                        call CleartheRoom("Kitty",1) from _call_CleartheRoom_16
                                        "She probably wouldn't mind you taking a quick nap. . ."
                                        call Wait from _call_Wait_26
                                        if K_Loc == bg_current:
                                                call DrainWord("Kitty","arriving") from _call_DrainWord_80
                                                ch_k "Well morning, sleepy head."
                                else:
                                        "She probably wouldn't appreciate you staying over, you head back to your own room."
                                        $ renpy.pop_call()
                                        jump Player_Room
                        call CleartheRoom("Kitty",1) from _call_CleartheRoom_17
                        call Kitty_Sleepover from _call_Kitty_Sleepover          
                elif bg_current == "bg emma":         
                        #If it's Emma's room, she gets dibs                         
                        if E_Loc != bg_current: 
                                # if Emma isn't around. . .
                                if E_Sleep >= 5: 
                                        call CleartheRoom("Emma",1) from _call_CleartheRoom_18
                                        "She probably wouldn't mind you taking a quick nap. . ."
                                        call Wait from _call_Wait_27
                                        if E_Loc == bg_current:
                                                call DrainWord("Emma","arriving") from _call_DrainWord_81
                                                ch_e "Well look whos sleeping in my bed. . ."
                                else:
                                        "She probably wouldn't appreciate you staying over, you head back to your own room."
                                        $ renpy.pop_call()
                                        jump Player_Room
                        call CleartheRoom("Emma",1) from _call_CleartheRoom_19
                        call Emma_Sleepover from _call_Emma_Sleepover 
                elif bg_current == "bg Mystique":         
                        #If it's Mystique's room, she gets dibs                         
                        if newgirl["Mystique"].Loc != bg_current: 
                                # if Mystique isn't around. . .
                                if newgirl["Mystique"].Sleep >= 5: 
                                        call CleartheRoom("Mystique",1) from _call_CleartheRoom_20
                                        "She probably wouldn't mind you taking a quick nap. . ."
                                        call Wait from _call_Wait_28
                                        if newgirl["Mystique"].Loc == bg_current:
                                                call DrainWord("Mystique","arriving") from _call_DrainWord_82
                                                ch_m "Well look whos sleeping in my bed. . ."
                                else:
                                        "She probably wouldn't appreciate you staying over, you head back to your own room."
                                        $ renpy.pop_call()
                                        jump Player_Room
                        call CleartheRoom("Mystique",1) from _call_CleartheRoom_21
                        call Mystique_Sleepover from _call_Mystique_Sleepover 
                else: 
                        #You're not in anyone else's room
                        if R_Loc == bg_current and R_Sleep >= 2 and ApprovalCheck("Rogue", 1000): 
                                    $ Options.append("Rogue")
                                    $ Options.append("Rogue")
                        if K_Loc == bg_current and K_Sleep >= 2 and ApprovalCheck("Kitty", 1000): 
                                    $ Options.append("Kitty")
                                    $ Options.append("Kitty")
                        if E_Loc == bg_current and E_Sleep >= 2 and ApprovalCheck("Emma", 1000): 
                                    $ Options.append("Emma")
                                    $ Options.append("Emma")
                        if newgirl["Mystique"].Loc == bg_current and newgirl["Mystique"].Sleep >= 2 and ApprovalCheck("Mystique", 1000): 
                                    $ Options.append("Mystique")
                                    $ Options.append("Mystique")
                                    
                        $ renpy.random.shuffle(Options)
                        if Options[0] == "none":
                                if R_Loc == bg_current and ApprovalCheck("Rogue", 1000): 
                                            $ Options[0] = "Rogue"
                                elif K_Loc == bg_current and ApprovalCheck("Kitty", 1000): 
                                            $ Options[0] = "Kitty"
                                elif E_Loc == bg_current and ApprovalCheck("Emma", 1000): 
                                            $ Options[0] = "Emma"  
                                elif newgirl["Mystique"].Loc == bg_current and ApprovalCheck("Mystique", 1000): 
                                            $ Options[0] = "Mystique"                            
                                
                        if Options[0] == "Rogue":                                
                                call CleartheRoom("Rogue",1) from _call_CleartheRoom_22
                                call Rogue_Sleepover from _call_Rogue_Sleepover_1 
                        elif Options[0] == "Kitty":    
                                call CleartheRoom("Kitty",1) from _call_CleartheRoom_23
                                call Kitty_Sleepover from _call_Kitty_Sleepover_1 
                        elif Options[0] == "Emma":    
                                call CleartheRoom("Emma",1) from _call_CleartheRoom_24
                                call Emma_Sleepover from _call_Emma_Sleepover_1 
                        elif Options[0] == "Mystique":    
                                call CleartheRoom("Mystique",1) from _call_CleartheRoom_25
                                call Mystique_Sleepover from _call_Mystique_Sleepover_1                         
                        else:   
                                call CleartheRoom("All",1) from _call_CleartheRoom_26
                                #if nobody is here, you just go to sleep
                                "It's getting late, so you go to sleep."
                                call Wait from _call_Wait_29
                #End night time
        else:
                    #if it's not night time, just wait
                    if bg_current == "bg rogue":
                            if R_Loc == bg_current:
                                ch_r "Sure, you can wait around a bit."     
                            else:
                                "You wait for Rogue to return."
                            call Wait from _call_Wait_30
                            if Current_Time == "Night" and R_Loc == bg_current:               
                                if R_Sleep or R_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [R_Petname], but you're welcome to stick around. . ."   
                                elif ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_r "It's pretty late, [R_Petname], but you can stay for a little bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_r "It's getting a little late [R_Petname]. You should head out." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Rogue's room                
                    elif bg_current == "bg kitty":
                            if K_Loc == bg_current:
                                ch_k "Sure, you can hang out for a bit."     
                            else:
                                "You wait for Kitty to return."
                            call Wait from _call_Wait_31
                            if Current_Time == "Night" and K_Loc == bg_current:               
                                if K_Sleep or K_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [K_Petname], but you can stay if you like. . ."   
                                elif ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_k "It's kinda late, [K_Petname], but you can stay for a bit."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_k "It's getting late [K_Petname]. You should get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Kitty's room    
                    elif bg_current == "bg emma":
                            if E_Loc == bg_current:
                                ch_e "You can stay for a while, if you'd like."     
                            else:
                                "You wait for Emma to return."
                            call Wait
                            if Current_Time == "Night" and E_Loc == bg_current:               
                                if E_Sleep or E_SEXP >= 30:                                                         
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [E_Petname], but I'd like you to stay. . ."   
                                elif ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI"):           
                                        #It's late but she really likes you
                                        ch_e "It's getting a bit late, [E_Petname], but you can stay."     
                                else:                                                                                   
                                        #she likes you well enough but it's late so you should go
                                        ch_e "It's getting late, [E_Petname]. I need to get some sleep." 
                                        $ renpy.pop_call()
                                        jump Campus_Map   
                            #end Emma's room           
                    else:
                        call Wait from _call_Wait_32       
        return
#Chat Function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

label Chat:
            menu:
                "Chat with Rogue" if R_Loc == bg_current: 
                        call Rogue_Chat from _call_Rogue_Chat        
                "Text Rogue" if R_Loc != bg_current: 
                        if "Rogue" in Digits:
                            "You send Rogue a text."
                            call Rogue_Chat from _call_Rogue_Chat_1  
                        else:
                            "You don't know her number, you'll have to go to her." 
                            return
                            
                "Chat with Kitty" if K_Loc == bg_current: 
                        call Kitty_Chat from _call_Kitty_Chat        
                "Text Kitty" if K_Loc != bg_current and "met" in K_History: 
                        if "Kitty" in Digits:
                            "You send Kitty a text."
                            call Kitty_Chat from _call_Kitty_Chat_1  
                        else:
                            "You don't know her number, you'll have to go to her." 
                            return
                            
                "Chat with [EmmaName]" if E_Loc == bg_current:                     
                        if "classcaught" not in E_History:
                                call Emma_Chat_Minimal from _call_Emma_Chat_Minimal
                        else:
                                call Emma_Chat from _call_Emma_Chat    
                "Chat with [EmmaName]" if E_Loc == "bg teacher" and bg_current == "bg classroom": 
                        ch_e "We can speak after class, [E_Petname]."     
                "Text [EmmaName]" if E_Loc != bg_current and "met" in E_History: 
                        if "Emma" in Digits:
                            # if E_Loc == "bg teacher" and bg_current == "bg classroom":
                            #         "She texts back, \"We can speak after class, [E_Petname].\"" 
                            #         return
                            "You send [EmmaName] a text."                 
                            if "classcaught" not in E_History:
                                    call Emma_Chat_Minimal from _call_Emma_Chat_Minimal_1
                            else:
                                    call Emma_Chat from _call_Emma_Chat_1  
                        else:
                            "You don't know her number, you'll have to go to her." 
                            return  
                
                "Chat with Mystique" if newgirl["Mystique"].Loc == bg_current:                     
                        call Mystique_Chat from _call_Mystique_Chat    

                "Text Mystique" if newgirl["Mystique"].Loc != bg_current and "met" in E_History: 
                        if "Mystique" in Digits:
                            "You send Mystique a text."                 
                            call Mystique_Chat from _call_Mystique_Chat_1  
                        else:
                            "You don't know her number, you'll have to go to her." 
                            return   

                "Chat with Laura" if newgirl["Laura"].Loc == bg_current:                     
                        call Laura_Chat

                "Text Laura" if newgirl["Laura"].Loc != bg_current and "met" in newgirl["Laura"].History: 
                        if "Laura" in Digits:
                            "You send Laura a text."                 
                            call Laura_Chat
                        else:
                            "You don't know her number, you'll have to go to her." 
                            return   

                "Never Mind":
                    pass
            return
            
# End Chat  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  

label Present_Check(Present = []):
    # Culls parties down to 2 max
    # call Present_Check(1) will _return positive if the room is filled with the current inhabitants
    # call Present Check will cull inhabitants of the room down to zero
    
    while len(Party) > 3:    
            # If two or more members in the party    
            #Culls down party size to two
            $ Party.remove(Party[3])   
    
    # checks to see which girls are present at a given location
    # If they are in the party, makes sure they are in the room
    # adds members who are not currently in the party
    if "Rogue" in Party: 
        $ R_Loc = bg_current
    elif R_Loc == bg_current:       
                    $ Present.append("Rogue")
    if "Kitty" in Party: 
        $ K_Loc = bg_current
    elif K_Loc == bg_current:       
                    $ Present.append("Kitty")
    if "Emma" in Party: 
        $ E_Loc = bg_current
    elif E_Loc == bg_current:       
                    $ Present.append("Emma")
    if "Mystique" in Party: 
        $ newgirl["Mystique"].Loc = bg_current
    elif newgirl["Mystique"].Loc == bg_current:       
                    $ Present.append("Mystique")

    if "Laura" in Party: 
        $ newgirl["Laura"].Loc = bg_current
    elif newgirl["Laura"].Loc == bg_current:       
                    $ Present.append("Laura")
        
    
    $ renpy.random.shuffle(Present) #Randomizes pool
    
    if len(Party) >= 1:
        #adds the first party member if it exists
        $ Present.append(Party[0]) 
    if len(Party) == 2:
        #adds the second party member if it exists
        $ Present.append(Party[1]) 
    if len(Party) == 3:
        #adds the third party member if it exists
        $ Present.append(Party[2]) 
    
    
    while len(Present) > 3:
            #culls the Present list down to two items (or less if the party is full)
            #Removes the rest
            if Present[0] == "Rogue": 
                    $ Present.remove("Rogue")
                    call Remove_Girl("Rogue") from _call_Remove_Girl_45
            elif Present[0] == "Kitty":      
                    $ Present.remove("Kitty")
                    call Remove_Girl("Kitty") from _call_Remove_Girl_46
            elif Present[0] == "Emma":      
                    $ Present.remove("Emma")
                    call Remove_Girl("Emma") from _call_Remove_Girl_47
            elif Present[0] == "Mystique":      
                    $ Present.remove("Mystique")
                    call Remove_Girl("Mystique") from _call_Remove_Girl_48
    
    if not Present:
            #if no one is there, quit now.
            return
    
    if Ch_Focus == "Kitty":
            # if the focus is Kitty, if Emma or Rogue are around, 
            # and Kitty isn't, swap, otherwise don't. 
            if "Kitty" in Present:
                pass        
            elif "Rogue" in Present:
                call Shift_Focus("Rogue") from _call_Shift_Focus_102
            elif "Emma" in Present:
                call Shift_Focus("Emma") from _call_Shift_Focus_103
            elif "Mystique" in Present:
                call Shift_Focus("Mystique") from _call_Shift_Focus_104
    elif Ch_Focus == "Emma":        
            # if the focus is Emma, if Kitty or Rogue are around, 
            # and Emma isn't, swap, otherwise don't. 
            if "Emma" in Present:
                pass        
            elif "Rogue" in Present:
                call Shift_Focus("Rogue") from _call_Shift_Focus_105
            elif "Kitty" in Present:
                call Shift_Focus("Kitty") from _call_Shift_Focus_106
            elif "Mystique" in Present:
                call Shift_Focus("Mystique") from _call_Shift_Focus_107
    elif Ch_Focus == "Rogue":
            # if the focus is not one of the above, if Kitty or Emma are around, 
            # and Rogue isn't, swap, otherwise don't. 
            if "Rogue" in Present:
                pass        
            elif "Kitty" in Present:
                call Shift_Focus("Kitty") from _call_Shift_Focus_108
            elif "Emma" in Present:
                call Shift_Focus("Emma") from _call_Shift_Focus_109
            elif "Mystique" in Present:
                call Shift_Focus("Mystique") from _call_Shift_Focus_110
    else: #Ch_Focus == "Mystique" or "Laura":
            # if the focus is not one of the above, if Kitty or Emma are around, 
            # and Rogue isn't, swap, otherwise don't. 
            if Ch_Focus in Present:
                pass        
            elif "Kitty" in Present:
                call Shift_Focus("Kitty") from _call_Shift_Focus_111
            elif "Emma" in Present:
                call Shift_Focus("Emma") from _call_Shift_Focus_112
            elif "Rogue" in Present:
                call Shift_Focus("Rogue") from _call_Shift_Focus_113
                    
    return




label Remove_Girl(Girl = 0, HideGirl = 1):
    # Girl is the girl being removed, this is for putting girls in a safe location if they run.   
    if Girl == "Rogue" or Girl == "All": 
            if "Rogue" in Party:        
                    $ Party.remove("Rogue")
            if "leaving" in R_RecentActions:
                    call DrainWord("Rogue","leaving") from _call_DrainWord_83  
            if "arriving" in R_RecentActions:
                    call DrainWord("Rogue","arriving") from _call_DrainWord_84 
            if bg_current == R_Loc:
                if bg_current == "bg rogue":
                    $ R_Loc = "bg campus"
                else:
                    $ R_Loc = "bg rogue"
                if HideGirl:
                    hide Rogue
                    call Rogue_Hide from _call_Rogue_Hide_1
    if Girl == "Kitty" or Girl == "All": 
            if "Kitty" in Party:        
                    $ Party.remove("Kitty")
            if "leaving" in K_RecentActions:
                    call DrainWord("Kitty","leaving") from _call_DrainWord_85  
            if "arriving" in K_RecentActions:
                    call DrainWord("Kitty","arriving") from _call_DrainWord_86   
            if bg_current == K_Loc: 
                if bg_current == "bg kitty":
                    $ K_Loc = "bg campus"
                else:
                    $ K_Loc = "bg kitty"
                if HideGirl:
                    hide Kitty_Sprite
                    call Kitty_Hide from _call_Kitty_Hide_1
    if Girl == "Emma" or Girl == "All": 
            if "Emma" in Party:        
                    $ Party.remove("Emma")
            if "leaving" in E_RecentActions:
                    call DrainWord("Emma","leaving") from _call_DrainWord_87  
            if "arriving" in E_RecentActions:
                    call DrainWord("Emma","arriving") from _call_DrainWord_88   
            if bg_current == E_Loc: 
                if bg_current == "bg emma":
                    $ E_Loc = "bg campus"
                else:
                    $ E_Loc = "bg emma"
                if HideGirl:
                    hide Emma_Sprite
                    call Emma_Hide from _call_Emma_Hide_1
    if Girl == "Mystique" or Girl == "All": 
            if "Mystique" in Party:        
                    $ Party.remove("Mystique")
            if "leaving" in newgirl["Mystique"].RecentActions:
                    call DrainWord("Mystique","leaving") from _call_DrainWord_89  
            if "arriving" in newgirl["Mystique"].RecentActions:
                    call DrainWord("Mystique","arriving") from _call_DrainWord_90   
            if bg_current == newgirl["Mystique"].Loc: 
                if bg_current == "bg Mystique":
                    $ newgirl["Mystique"].Loc = "bg campus"
                else:
                    $ newgirl["Mystique"].Loc = "bg Mystique"
                if HideGirl:
                    hide Mystique_Sprite
                    call Mystique_Hide from _call_Mystique_Hide

    if Girl == "Laura" or Girl == "All": 
            if "Laura" in Party:        
                    $ Party.remove("Laura")
            if "leaving" in newgirl["Laura"].RecentActions:
                    call DrainWord("Laura","leaving")
            if "arriving" in newgirl["Laura"].RecentActions:
                    call DrainWord("Laura","arriving")
            if bg_current == newgirl["Laura"].Loc: 
                if bg_current == "bg Laura":
                    $ newgirl["Laura"].Loc = "bg campus"
                else:
                    $ newgirl["Laura"].Loc = "bg Laura"
                if HideGirl:
                    hide Laura_Sprite
                    call Laura_Hide
    #end of Remove Girl
    return
    
# Favorte sex acts >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label Favorite_Actions(Character=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0):
                        
    if not Character or Character == "Rogue":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = R_Anal + R_DildoA + R_FondleA + R_InsertA + R_LickA        
                $ PTemp = R_Sex + R_DildoP + R_FondleP + R_InsertP + R_LickP
                $ BTemp = R_Blow
                $ TTemp = R_Tit
                $ HTemp = R_Hand
                $ FTemp = R_FondleB + R_FondleT + R_SuckB + R_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if R_PlayerFav and ApprovalCheck("Rogue", 1500): 
                        if R_PlayerFav == "anal":
                            $ ATemp += 20
                        elif R_PlayerFav == "sex":
                            $ PTemp += 20
                        elif R_PlayerFav == "blow":
                            $ BTemp += 20
                        elif R_PlayerFav == "tit":
                            $ TTemp += 20
                        elif R_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif R_PlayerFav and ApprovalCheck("Rogue", 800):
                        if R_PlayerFav == "anal":
                            $ ATemp += 5
                        elif R_PlayerFav == "sex":
                            $ PTemp += 5
                        elif R_PlayerFav == "blow":
                            $ BTemp += 5
                        elif R_PlayerFav == "tit":
                            $ TTemp += 5
                        elif R_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + R_Kissed 
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if R_Anal >= 5:
                            $ Temp = "anal"
                    elif R_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if R_Sex >= 5:
                            $ Temp = "sex"
                        elif R_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and R_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and R_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and R_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss"
                
                if not Quick:
                    $ R_Favorite = Temp
                else:
                    return Temp
    #End Rogue Stuff
    
    if not Character or Character == "Kitty":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = K_Anal + K_DildoA + K_FondleA + K_InsertA + K_LickA        
                $ PTemp = K_Sex + K_DildoP + K_FondleP + K_InsertP + K_LickP
                $ BTemp = K_Blow
                $ TTemp = K_Tit
                $ HTemp = K_Hand
                $ FTemp = K_FondleB + K_FondleT + K_SuckB + K_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if K_PlayerFav and ApprovalCheck("Kitty", 1500): 
                        if K_PlayerFav == "anal":
                            $ ATemp += 20
                        elif K_PlayerFav == "sex":
                            $ PTemp += 20
                        elif K_PlayerFav == "blow":
                            $ BTemp += 20
                        elif K_PlayerFav == "tit":
                            $ TTemp += 20
                        elif K_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif K_PlayerFav and ApprovalCheck("Kitty", 800):
                        if K_PlayerFav == "anal":
                            $ ATemp += 5
                        elif K_PlayerFav == "sex":
                            $ PTemp += 5
                        elif K_PlayerFav == "blow":
                            $ BTemp += 5
                        elif K_PlayerFav == "tit":
                            $ TTemp += 5
                        elif K_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + K_Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if K_Anal >= 5:
                            $ Temp = "anal"
                    elif K_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if K_Sex >= 5:
                            $ Temp = "sex"
                        elif K_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and K_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and K_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and K_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss"
                
                if not Quick:
                    $ K_Favorite = Temp
                else:
                    return Temp
    #End Kitty Stuff    
    if not Character or Character == "Emma":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = E_Anal + E_DildoA + E_FondleA + E_InsertA + E_LickA        
                $ PTemp = E_Sex + E_DildoP + E_FondleP + E_InsertP + E_LickP
                $ BTemp = E_Blow
                $ TTemp = E_Tit
                $ HTemp = E_Hand
                $ FTemp = E_FondleB + E_FondleT + E_SuckB + E_Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if E_PlayerFav and ApprovalCheck("Emma", 1500): 
                        if E_PlayerFav == "anal":
                            $ ATemp += 20
                        elif E_PlayerFav == "sex":
                            $ PTemp += 20
                        elif E_PlayerFav == "blow":
                            $ BTemp += 20
                        elif E_PlayerFav == "tit":
                            $ TTemp += 20
                        elif E_PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif E_PlayerFav and ApprovalCheck("Emma", 800):
                        if E_PlayerFav == "anal":
                            $ ATemp += 5
                        elif E_PlayerFav == "sex":
                            $ PTemp += 5
                        elif E_PlayerFav == "blow":
                            $ BTemp += 5
                        elif E_PlayerFav == "tit":
                            $ TTemp += 5
                        elif E_PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + E_Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if E_Anal >= 5:
                            $ Temp = "anal"
                    elif E_LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if E_Sex >= 5:
                            $ Temp = "sex"
                        elif E_LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and E_Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and E_SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and E_FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss"
                
                if not Quick:
                    $ E_Favorite = Temp
                else:
                    return Temp
    #End Emma Stuff  
    
    if not Character or Character == "Mystique":
                #ass, pussy, blow, tits, hand, fondling, kiss
                $ ATemp = newgirl["Mystique"].Anal + newgirl["Mystique"].DildoA + newgirl["Mystique"].FondleA + newgirl["Mystique"].InsertA + newgirl["Mystique"].LickA        
                $ PTemp = newgirl["Mystique"].Sex + newgirl["Mystique"].DildoP + newgirl["Mystique"].FondleP + newgirl["Mystique"].InsertP + newgirl["Mystique"].LickP
                $ BTemp = newgirl["Mystique"].Blow
                $ TTemp = newgirl["Mystique"].Tit
                $ HTemp = newgirl["Mystique"].Hand
                $ FTemp = newgirl["Mystique"].FondleB + newgirl["Mystique"].FondleT + newgirl["Mystique"].SuckB + newgirl["Mystique"].Hotdog
                                
                #This portion sets a bonus based on the player's favorite activity with her.
                if newgirl["Mystique"].PlayerFav and ApprovalCheck("Emma", 1500): 
                        if newgirl["Mystique"].PlayerFav == "anal":
                            $ ATemp += 20
                        elif newgirl["Mystique"].PlayerFav == "sex":
                            $ PTemp += 20
                        elif newgirl["Mystique"].PlayerFav == "blow":
                            $ BTemp += 20
                        elif newgirl["Mystique"].PlayerFav == "tit":
                            $ TTemp += 20
                        elif newgirl["Mystique"].PlayerFav == "hand":
                            $ HTemp += 20
                        else:
                            $ FTemp += 20
                elif newgirl["Mystique"].PlayerFav and ApprovalCheck("Emma", 800):
                        if newgirl["Mystique"].PlayerFav == "anal":
                            $ ATemp += 5
                        elif newgirl["Mystique"].PlayerFav == "sex":
                            $ PTemp += 5
                        elif newgirl["Mystique"].PlayerFav == "blow":
                            $ BTemp += 5
                        elif newgirl["Mystique"].PlayerFav == "tit":
                            $ TTemp += 5
                        elif newgirl["Mystique"].PlayerFav == "hand":
                            $ HTemp += 5
                        else:
                            $ FTemp += 5
                
                #This adds the numbers together to make a large number, then generates a random number between 1 and that total
                $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + FTemp + newgirl["Mystique"].Kissed  
                if Total <= 0:
                    $ D20F = 999
                else:
                    $ D20F = renpy.random.randint(1, Total)
                
                # This selects a favorite activity based on which number is picked.
                if D20F <= ATemp:
                    if newgirl["Mystique"].Anal >= 5:
                            $ Temp = "anal"
                    elif newgirl["Mystique"].LickA >= 5:
                            $ Temp = "lick ass"
                    else:
                            $ Temp = "insert ass"
                elif D20F <= ATemp + PTemp:
                        if newgirl["Mystique"].Sex >= 5:
                            $ Temp = "sex"
                        elif newgirl["Mystique"].LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
                elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
                elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp:
                            $ Temp = "hand"
                elif D20F <= ATemp + PTemp + BTemp + TTemp + HTemp + FTemp:
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and newgirl["Mystique"].Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and newgirl["Mystique"].SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and newgirl["Mystique"].FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
                else:
                            $ Temp = "kiss"
                
                if not Quick:
                    $ newgirl["Mystique"].Favorite = Temp
                else:
                    return Temp
    #End Emma Stuff            
    
    return

# End favorite sex acts >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Start First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Seen_First_Peen(Silent = 0, Undress = 0, GirlsNum = 0): #checked each time she sees your cock
        #GirlsNum tracks whether multiple girls have seen the cock in this scene. It's passed on to the second girls+
        if not renpy.showing("Chibi_UI"):
                show Chibi_UI
        if R_Loc == bg_current:  
                #If Rogue is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Rogue" or Partner == "Rogue") and "peen" not in R_RecentActions:
                        #If Rogue is the prinary or secondary character, and hasn't seen your cock yet, call the thing 
                        call Rogue_First_Peen(Silent,Undress) from _call_Rogue_First_Peen_1
                        $ GirlsNum += 1                        
        if K_Loc == bg_current:  
                #If Kitty is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Kitty" or Partner == "Kitty") and "peen" not in K_RecentActions:
                        #If Kitty hasn't seen your cock yet, call the thing 
                        call Kitty_First_Peen(Silent,Undress,GirlsNum) from _call_Kitty_First_Peen
                        $ GirlsNum += 1        
        if E_Loc == bg_current:  
                #If Emma is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Emma" or Partner == "Emma") and "peen" not in E_RecentActions:
                        #If Emma hasn't seen your cock yet, call the thing 
                        call Emma_First_Peen(Silent,Undress,GirlsNum) from _call_Emma_First_Peen
                        $ GirlsNum += 1  
        if newgirl["Mystique"].Loc == bg_current:  
                #If Emma is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Mystique" or Partner == "Mystique") and "peen" not in newgirl["Mystique"].RecentActions:
                        #If Mystique hasn't seen your cock yet, call the thing 
                        call Mystique_First_Peen(Silent,Undress,GirlsNum) from _call_Mystique_First_Peen
                        $ GirlsNum += 1   

        if newgirl["Laura"].Loc == bg_current:  
                #If Laura is around, check to see if she noticed your cock yet
                if (Ch_Focus == "Laura" or Partner == "Laura") and "peen" not in newgirl["Laura"].RecentActions:
                        #If Laura hasn't seen your cock yet, call the thing 
                        call Laura_First_Peen(Silent,Undress,GirlsNum)
                        $ GirlsNum += 1       
                        
        if not GirlsNum:
                #if no girls are present                
                if "cockout" in P_RecentActions:
                        return
                elif Undress:
                        "You strip nude."
                else:
                        "You whip your cock out."                
                $ P_RecentActions.append("cockout") 
        
        return

label CockOut:        
        if (Approval == 3 and Primary == "Rogue") or (Approval == 4 and Secondary == "Rogue"):
                    call Rogue_First_Peen(React=1)   
        elif (Approval == 3 and Primary == "Kitty") or (Approval == 4 and Secondary == "Kitty"):
                    call Kitty_First_Peen(React=1) 
        elif (Approval == 3 and Primary == "Emma") or (Approval == 4 and Secondary == "Emma"):
                    call Emma_First_Peen(React=1) 
        elif (Approval == 3 and Primary == "Laura") or (Approval == 4 and Secondary == "Laura"):
                    call Laura_First_Peen(React=1) 
        $ Approval = 0
        return
        
label Put_Cock_Back: #checked each time she sees your cock
        #if no girls are present
        if renpy.showing("Chibi_UI"):
                hide Chibi_UI
        if "cockout" in P_RecentActions:                 
                "You put your cock away."
                call DrainWord("Player","cockout") from _call_DrainWord_91

        return

label Get_Dressed: #checked each time she sees your cock
        #if no girls are present
        if "naked" in P_RecentActions:   
                "You get dressed."
                call DrainWord("Player","naked") 
                call DrainWord("Player","cockout")
        elif "cockout" in P_RecentActions:                 
                "You put your cock away."
                call DrainWord("Player","cockout")
        return
        
# End First Seen Peen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /     
    
# Start First Les scene / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Seen_Les(Silent = 0, Undress = 0, GirlsNum = 0): 
        return
# End First Les scene / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        

label FlashTits(Girl = "Rogue", Timing = 1, Over = 0, Under = 0):
    #This function quickly removes and replaces the girl's tops, put the girl's name in the function call.
    if Girl == "Rogue":
            $ Over = R_Over
            $ Under = R_Chest
            $ R_Over = 0
            $ R_Chest = 0  
            if Timing:
                    pause Timing     
                    $ R_Over = Over
                    $ R_Chest = Under
    elif Girl == "Kitty":
            $ Over = K_Over
            $ Under = K_Chest
            $ K_Over = 0
            $ K_Chest = 0   
            if Timing:
                    pause Timing     
                    $ K_Over = Over
                    $ K_Chest = Under
    elif Girl == "Emma":
            $ Over = E_Over
            $ Under = E_Chest
            $ E_Over = 0
            $ E_Chest = 0   
            if Timing:
                    pause Timing     
                    $ E_Over = Over
                    $ E_Chest = Under
    elif Girl == "Mystique":
            $ Over = newgirl["Mystique"].Over
            $ Under = newgirl["Mystique"].Chest
            $ newgirl["Mystique"].Over = 0
            $ newgirl["Mystique"].Chest = 0   
            if Timing:
                    pause Timing     
                    $ newgirl["Mystique"].Over = Over
                    $ newgirl["Mystique"].Chest = Under
    return

# Start Gym Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Gym_Clothes(Mode = 0, Girl = 0, GirlsNum = 0): #checked each time you enter the Gym
    #GirlsNum tracks whether multiple girls have changed clothes
    if not Girl or Girl == "Rogue":
        if R_Loc != "bg dangerroom" or Mode == "change":  
                #If Rogue has left the gym or was told to change back
                if R_Outfit == "gym":
                        if bg_current == "bg dangerroom" and "leaving" in R_RecentActions:
                                #if you're in the danger room, and so is Rogue
                                show blackscreen onlayer black
                        $ R_Outfit = R_OutfitDay
                        call RogueOutfit(Changed=1) from _call_RogueOutfit_32                        
        elif R_Outfit == "gym":
                    #If it's already gym clothes, skip this
                    pass           
        elif Mode == "pre":
                #If she was already in the gym when you got there
                if R_Loc == "bg dangerroom" and "Rogue" not in Party:
                    $ R_Outfit = "gym"
                    call RogueOutfit(Changed=1) from _call_RogueOutfit_33
        elif Mode == "auto":
                #If it's set to do it automatically by the call
                if R_Loc == "bg dangerroom" and R_Loc == bg_current:
                        show blackscreen onlayer black
                        $ R_Outfit = "gym"
                call RogueOutfit(Changed=1) from _call_RogueOutfit_34        
        elif R_Loc == bg_current:
                #If Rogue is in the gym, see if she'll change clothes                
                if ApprovalCheck("Rogue", 1200, "LO") or "sub" in R_Traits:
                    pass
                elif ApprovalCheck("Rogue", 800, "LO") and R_Custom[0]:
                    pass
                elif ApprovalCheck("Rogue", 600, "LO") and R_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no"  or "asked gym" in R_DailyActions or "no ask gym" in R_Traits:   
                    #If she decides not to ask you
                    ch_r "I'll be right back, gotta change."                       
                    show blackscreen onlayer black
                    $ R_Outfit = "gym"
                    call RogueOutfit(Changed=1) from _call_RogueOutfit_35
                else:
                    # She asks to change outfits
                    $ R_DailyActions.append("asked gym")
                    menu:
                            ch_r "Did you want me to change into my gym clothes?"
                            "Yeah, they look great.":   
                                call RogueFace("smile") from _call_RogueFace_257                          
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 1)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
                                $ Line = 1                            
                            "No, stay in that.":
                                call RogueFace("confused") from _call_RogueFace_258    
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                                $ Line = 0
                            "Whichever you like.":
                                call RogueFace("confused") from _call_RogueFace_259                                    
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                                $ Line = renpy.random.randint(0, 3)
                            "I don't care.":        
                                call RogueFace("angry") from _call_RogueFace_260   
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -2, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                                $ Line = renpy.random.randint(0, 1)
                    if Line:
                            #If she decided to change     
                            ch_r "Ok, be right back."                       
                            show blackscreen onlayer black
                            $ R_Outfit = "gym"
                            call RogueOutfit(Changed=1) from _call_RogueOutfit_36
                    #end asked
                if R_Outfit == "gym":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Rogue      
        
    if not Girl or Girl == "Kitty":
        if K_Loc != "bg dangerroom" or Mode == "change":  
                #If Kitty has left the gym or was told to change back
                if K_Outfit == "gym":
                        if bg_current == "bg dangerroom" and "leaving" in K_RecentActions:
                                #if you're in the danger room, and so is Kitty
                                show blackscreen onlayer black
                        $ K_Outfit = K_OutfitDay
                        call KittyOutfit(Changed=1) from _call_KittyOutfit_14                        
        elif K_Outfit == "gym":
                    #If it's already gym clothes, skip this
                    pass   
        elif Mode == "pre":
                #If she was already here
                if K_Loc == "bg dangerroom" and "Kitty" not in Party:
                    $ K_Outfit = "gym"
                    call KittyOutfit(Changed=1) from _call_KittyOutfit_15
        elif Mode == "auto":
                #If it's set to do it automatically by the call
                        if K_Loc == "bg dangerroom" and K_Loc == bg_current:
                                show blackscreen onlayer black
                        $ K_Outfit = "gym"
                        call KittyOutfit(Changed=1) from _call_KittyOutfit_16
        elif K_Loc == bg_current:
                #If Kitty is in the gym, see if she'll change clothes
                if ApprovalCheck("Kitty", 1300, "LO") or "sub" in K_Traits:
                    pass
                elif ApprovalCheck("Kitty", 800, "LO") and K_Custom[0]:
                    pass
                elif ApprovalCheck("Kitty", 600, "LO") and K_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no" or "asked gym" in K_DailyActions or "no ask gym" in K_Traits:   
                    #If she decides not to ask you   
                    if GirlsNum:
                        ch_k "I'll be right back too."  
                    else:
                        ch_k "I'll be back soon, gotta change."                       
                    show blackscreen onlayer black
                    $ K_Outfit = "gym"
                    call KittyOutfit(Changed=1) from _call_KittyOutfit_17
                else:
                    # She asks to change outfits
                    $ K_DailyActions.append("asked gym")
                    if GirlsNum:
                        $ Line = "Should I change too?"  
                    else:
                        $ Line = "Would you like me to change into my gym clothes?"   
                    menu:
                            ch_k "[Line]"
                            "Yeah, they look great.":  
                                call KittyFace("smile") from _call_KittyFace_249                              
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 1)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                                $ Line = 1                            
                            "No, stay in that.":
                                call KittyFace("confused") from _call_KittyFace_250    
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                                $ Line = 0
                            "Whichever you like.": 
                                call KittyFace("confused") from _call_KittyFace_251                                      
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                                $ Line = renpy.random.randint(0, 3)
                            "I don't care.":        
                                call KittyFace("angry") from _call_KittyFace_252      
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
                                $ Line = renpy.random.randint(0, 1)
                    if Line:
                            #If she decided to change     
                            ch_k "Ok, back in a bit"                       
                            show blackscreen onlayer black
                            $ K_Outfit = "gym"
                            call KittyOutfit(Changed=1) from _call_KittyOutfit_18
                    #end asked
                if K_Outfit == "gym":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Kitty   
        
    if not Girl or Girl == "Emma":
        if E_Loc != "bg dangerroom" or Mode == "change":  
                #If Emma has left the gym or was told to change back
                if E_Outfit == "gym":
                        if bg_current == "bg dangerroom" and "leaving" in E_RecentActions:
                                #if you're in the danger room, and so is Emma
                                show blackscreen onlayer black
                        $ E_Outfit = E_OutfitDay
                        call EmmaOutfit(Changed=1) from _call_EmmaOutfit_17                        
        elif E_Outfit == "gym":
                    #If it's already gym clothes, skip this
                    pass   
        elif Mode == "pre":
                #If she was already here
                if E_Loc == "bg dangerroom" and "Emma" not in Party:
                    $ E_Outfit = "gym"
                    call EmmaOutfit(Changed=1) from _call_EmmaOutfit_18
        elif Mode == "auto":
                #If it's set to do it automatically by the call
                        if E_Loc == "bg dangerroom" and E_Loc == bg_current:
                                show blackscreen onlayer black
                        $ E_Outfit = "gym"
                        call EmmaOutfit(Changed=1) from _call_EmmaOutfit_19
        elif E_Loc == bg_current:
                #If Emma is in the gym, see if she'll change clothes
                if ApprovalCheck("Emma", 1300, "LO") or "sub" in E_Traits:
                    pass
                elif ApprovalCheck("Emma", 900, "LO") and E_Custom[0]:
                    pass
                elif ApprovalCheck("Emma", 700, "LO") and E_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no" or "asked gym" in E_DailyActions or "no ask gym" in E_Traits:   
                    #If she decides not to ask you
                    if GirlsNum:
                        ch_e "I should change too."  
                    else:
                        ch_e "I need to change into something more appropriate."                       
                    show blackscreen onlayer black
                    $ E_Outfit = "gym"
                    call EmmaOutfit(Changed=1) from _call_EmmaOutfit_20
                else:
                    # She asks to change outfits
                    $ E_DailyActions.append("asked gym")
                    if GirlsNum:
                        $ Line = "Do you think I should change as well?"  
                    else:
                        $ Line = "Did you want me to change?"   
                    menu:
                            ch_e "[Line]"
                            "Yeah, they look great.":  
                                call EmmaFace("smile") from _call_EmmaFace_441                              
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 60, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                                $ Line = 1                            
                            "No, stay in that.":
                                call EmmaFace("confused") from _call_EmmaFace_442    
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                                $ Line = 0
                            "Whichever you like.": 
                                call EmmaFace("confused") from _call_EmmaFace_443                                      
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                                $ Line = renpy.random.randint(0, 3)
                            "I don't care.":        
                                call EmmaFace("angry") from _call_EmmaFace_444      
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)  
                                $ Line = renpy.random.randint(0, 1)
                    if Line:
                            #If she decided to change     
                            ch_e "Fine, I'll be right back."                       
                            show blackscreen onlayer black
                            $ E_Outfit = "gym"
                            call EmmaOutfit(Changed=1) from _call_EmmaOutfit_21
                    #end asked
                if E_Outfit == "gym":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Emma 

    if not Girl or Girl == "Mystique":
        if newgirl["Mystique"].Loc != "bg dangerroom" or Mode == "change":  
                #If Mystique has left the gym or was told to change back
                if newgirl["Mystique"].Outfit == "gym":
                        if bg_current == "bg dangerroom" and "leaving" in newgirl["Mystique"].RecentActions:
                                #if you're in the danger room, and so is Mystique
                                show blackscreen onlayer black
                        $ newgirl["Mystique"].Outfit = newgirl["Mystique"].OutfitDay
                        call MystiqueOutfit(Changed=1) from _call_MystiqueOutfit_34                        
        elif newgirl["Mystique"].Outfit == "gym":
                    #If it's already gym clothes, skip this
                    pass   
        elif Mode == "pre":
                #If she was already here
                if newgirl["Mystique"].Loc == "bg dangerroom" and "Mystique" not in Party:
                    $ newgirl["Mystique"].Outfit = "gym"
                    call MystiqueOutfit(Changed=1) from _call_MystiqueOutfit_35
        elif Mode == "auto":
                #If it's set to do it automatically by the call
                        if newgirl["Mystique"].Loc == "bg dangerroom" and newgirl["Mystique"].Loc == bg_current:
                                show blackscreen onlayer black
                        $ newgirl["Mystique"].Outfit = "gym"
                        call MystiqueOutfit(Changed=1) from _call_MystiqueOutfit_36
        elif newgirl["Mystique"].Loc == bg_current:
                #If Mystique is in the gym, see if she'll change clothes
                if ApprovalCheck("Mystique", 1300, "LO") or "sub" in newgirl["Mystique"].Traits:
                    pass
                elif ApprovalCheck("Mystique", 900, "LO") and newgirl["Mystique"].Custom[0]:
                    pass
                elif ApprovalCheck("Mystique", 700, "LO") and newgirl["Mystique"].Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no" or "asked gym" in newgirl["Mystique"].DailyActions or "no ask gym" in newgirl["Mystique"].Traits:   
                    #If she decides not to ask you
                    if GirlsNum:
                        ch_m "I should change too."  
                    else:
                        ch_m "I need to change into something more appropriate."                       
                    show blackscreen onlayer black
                    $ newgirl["Mystique"].Outfit = "gym"
                    call MystiqueOutfit(Changed=1) from _call_MystiqueOutfit_37
                else:
                    # She asks to change outfits
                    $ newgirl["Mystique"].DailyActions.append("asked gym")
                    if GirlsNum:
                        $ Line = "Do you think I should change as well?"  
                    else:
                        $ Line = "Did you want me to change?"   
                    menu:
                            ch_m "[Line]"
                            "Yeah, they look great.":  
                                call MystiqueFace("smile") from _call_MystiqueFace_331                              
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                                $ Line = 1                            
                            "No, stay in that.":
                                call MystiqueFace("confused") from _call_MystiqueFace_332    
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                                $ Line = 0
                            "Whichever you like.": 
                                call MystiqueFace("confused") from _call_MystiqueFace_333                                      
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                                $ Line = renpy.random.randint(0, 3)
                            "I don't care.":        
                                call MystiqueFace("angry") from _call_MystiqueFace_334      
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)  
                                $ Line = renpy.random.randint(0, 1)
                    if Line:
                            #If she decided to change     
                            ch_m "Fine, I'll be right back."                       
                            show blackscreen onlayer black
                            $ newgirl["Mystique"].Outfit = "gym"
                            call MystiqueOutfit(Changed=1) from _call_MystiqueOutfit_38
                    #end asked
                if newgirl["Mystique"].Outfit == "gym":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Mystique 
        
        return
# End Gym clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        


# Start Pool Clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Pool_Clothes(Mode = 0, Girl = 0, GirlsNum = 0): #checked each time you enter the Pool
    #GirlsNum tracks whether multiple girls have changed clothes
    if not Girl or Girl == "Rogue":
        if R_Loc != "bg pool" or Mode == "change":  
                #If Rogue has left the pool or was told to change back
                if R_Outfit == "swimsuit1" or R_Outfit == "swimsuit2":
                        if bg_current == "bg pool" and "leaving" in R_RecentActions:
                                #if you're in the pool, and so is Rogue
                                show blackscreen onlayer black
                        $ R_Outfit = R_OutfitDay
                        call RogueOutfit(Changed=1) from _call_RogueOutfit_37                        
        elif R_Outfit == "swimsuit1" or R_Outfit == "swimsuit2":
                    #If it's already pool clothes, skip this
                    pass           
        elif Mode == "pre":
                #If she was already in the pool when you got there
                if R_Loc == "bg pool" and "Rogue" not in Party:
                    if "exhibitionist" in R_Traits:
                        $ R_Outfit = "swimsuit2"
                    else:
                        $ R_Outfit = "swimsuit1"

                    call RogueOutfit(Changed=1) from _call_RogueOutfit_38
                    $ R_Water = 2

        elif Mode == "auto":
                #If it's set to do it automatically by the call
                if R_Loc == "bg pool" and R_Loc == bg_current:
                        show blackscreen onlayer black
                        if "exhibitionist" in R_Traits:
                            $ R_Outfit = "swimsuit2"
                        else:
                            $ R_Outfit = "swimsuit1"
                call RogueOutfit(Changed=1) from _call_RogueOutfit_39
        elif Mode == "goswim":
                #If it's set to do it automatically by the call
                if R_Over or R_Legs or R_Chest or R_Panties: #she's not walking around naked
                    if R_Loc == "bg pool" and R_Loc == bg_current:
                        ch_r "I'l be right there, let me just put on my swimsuit"
                        show blackscreen onlayer black
                        if "exhibitionist" in R_Traits:
                            $ R_Outfit = "swimsuit2"
                        else:
                            $ R_Outfit = "swimsuit1"

                    call RogueOutfit(Changed=1) from _call_RogueOutfit_40        
        elif R_Loc == bg_current:
                #If Rogue is in the pool, see if she'll change clothes                
                if ApprovalCheck("Rogue", 1200, "LO") or "sub" in R_Traits:
                    pass
                elif ApprovalCheck("Rogue", 800, "LO") and R_Custom[0]:
                    pass
                elif ApprovalCheck("Rogue", 600, "LO") and R_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no":   
                    #If she decides not to ask you
                    if "arriving" in K_RecentActions:
                        pass
                    else:
                        ch_r "I'll be right back, gotta change."                       
                        show blackscreen onlayer black
                    if "exhibitionist" in R_Traits:
                        $ R_Outfit = "swimsuit2"
                    else:
                        $ R_Outfit = "swimsuit1"
                    call RogueOutfit(Changed=1) from _call_RogueOutfit_41
                #else:
                #    # She asks to change outfits
                #    $ R_DailyActions.append("asked gym")
                #    menu:
                #            ch_r "Did you want me to change into my gym clothes?"
                #            "Yeah, they look great.":   
                #                call RogueFace("smile")                          
                #                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                #                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 1)
                #                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
                #                $ Line = 1                            
                #            "No, stay in that.":
                #                call RogueFace("confused")    
                #                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                #                $ Line = 0
                #            "Whichever you like.":
                #                call RogueFace("confused")                                    
                #                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                #                $ Line = renpy.random.randint(0, 3)
                #            "I don't care.":        
                #                call RogueFace("angry")   
                #                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -2, 1)
                #                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                #                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                #                $ Line = renpy.random.randint(0, 1)
                    #if Line:
                    #        #If she decided to change     
                    #        ch_r "Ok, be right back."                       
                    #        show blackscreen onlayer black
                    #        if "exhibitionist" in R_Traits:
                    #            $ R_Outfit = "swimsuit2"
                    #        else:
                    #            $ R_Outfit = "swimsuit1"
                    #        call RogueOutfit(Changed=1)
                    #end asked
                if R_Outfit == "swimsuit1" or R_Outfit == "swimsuit2":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Rogue      
        
    if not Girl or Girl == "Kitty":
        if K_Loc != "bg pool" or Mode == "change":  
                #If Kitty has left the pool or was told to change back
                if K_Outfit == "purple bikini" or K_Outfit == "swimsuit3":
                        if bg_current == "bg pool" and "leaving" in K_RecentActions:
                                #if you're in the pool, and so is Kitty
                                show blackscreen onlayer black
                        $ K_Outfit = K_OutfitDay
                        call KittyOutfit(Changed=1) from _call_KittyOutfit_19                        
        elif K_Outfit == "purple bikini" or K_Outfit == "swimsuit3":
                    #If it's already pool clothes, skip this
                    pass   
        elif Mode == "pre":
                #If she was already here
                if K_Loc == "bg pool" and "Kitty" not in Party:
                    if "exhibitionist" in K_Traits:
                        $ K_Outfit = "swimsuit3"
                    else:
                        $ K_Outfit = "purple bikini"
                    call KittyOutfit(Changed=1) from _call_KittyOutfit_20
                    $ K_Water = 2

        elif Mode == "auto":
                #If it's set to do it automatically by the call
                        if K_Loc == "bg pool" and K_Loc == bg_current:
                                show blackscreen onlayer black
                        if "exhibitionist" in K_Traits:
                            $ K_Outfit = "swimsuit3"
                        else:
                            $ K_Outfit = "purple bikini"
                        call KittyOutfit(Changed=1) from _call_KittyOutfit_21
        elif Mode == "goswim":
                #If it's set to do it automatically by the call
                if K_Over or K_Legs or K_Chest or K_Panties: #she's not walking around naked
                    if K_Loc == "bg pool" and K_Loc == bg_current:
                        ch_k "I'l be right there, let me just put on my bikini"
                        show blackscreen onlayer black
                    if "exhibitionist" in K_Traits:
                        $ K_Outfit = "swimsuit3"
                    else:
                        $ K_Outfit = "purple bikini"
                    call KittyOutfit(Changed=1) from _call_KittyOutfit_22
        elif K_Loc == bg_current:
                #If Kitty is in the pool, see if she'll change clothes
                if ApprovalCheck("Kitty", 1300, "LO") or "sub" in K_Traits:
                    pass
                elif ApprovalCheck("Kitty", 800, "LO") and K_Custom[0]:
                    pass
                elif ApprovalCheck("Kitty", 600, "LO") and K_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no":   
                    #If she decides not to ask you   
                    if "arriving" in K_RecentActions:
                        pass
                    else:
                        if GirlsNum:
                            ch_k "I'll be right back too."  
                        else:
                            ch_k "I'll be back soon, gotta change."                       
                        show blackscreen onlayer black
                    if "exhibitionist" in K_Traits:
                        $ K_Outfit = "swimsuit3"
                    else:
                        $ K_Outfit = "purple bikini"
                    call KittyOutfit(Changed=1) from _call_KittyOutfit_23
                #else:
                #    # She asks to change outfits
                #    $ K_DailyActions.append("asked gym")
                #    if GirlsNum:
                #        $ Line = "Should I change too?"  
                #    else:
                #        $ Line = "Would you like me to change into my gym clothes?"   
                #    menu:
                #            ch_k "[Line]"
                #            "Yeah, they look great.":  
                #                call KittyFace("smile")                              
                #                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                #                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 1)
                #                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1)
                #                $ Line = 1                            
                #            "No, stay in that.":
                #                call KittyFace("confused")    
                #                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                #                $ Line = 0
                #            "Whichever you like.": 
                #                call KittyFace("confused")                                      
                #                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                #                $ Line = renpy.random.randint(0, 3)
                #            "I don't care.":        
                #                call KittyFace("angry")      
                #                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                #                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                #                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
                #                $ Line = renpy.random.randint(0, 1)
                    #if Line:
                            #If she decided to change     
                    #        ch_k "Ok, back in a bit"                       
                    #        show blackscreen onlayer black
                    #        if "exhibitionist" in K_Traits:
                    #            $ K_Outfit = "swimsuit3"
                    #        else:
                    #            $ K_Outfit = "purple bikini"
                    #        call KittyOutfit(Changed=1)
                    #end asked
                if K_Outfit == "purple bikini" or K_Outfit == "swimsuit3":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Kitty   

        
    if not Girl or Girl == "Emma":
        if E_Loc != "bg pool" or Mode == "change":  
                #If Emma has left the pool or was told to change back
                if E_Outfit == "bikini" or E_Outfit == "naked pool":
                        if bg_current == "bg pool" and "leaving" in E_RecentActions:
                                #if you're in the pool, and so is Emma
                                show blackscreen onlayer black
                        $ E_Outfit = E_OutfitDay
                        call EmmaOutfit(Changed=1) from _call_EmmaOutfit_22                        
        elif E_Outfit == "bikini" or E_Outfit == "naked pool":
                    #If it's already pool clothes, skip this
                    pass   
        elif Mode == "pre":
                #If she was already here
                if E_Loc == "bg pool" and "Emma" not in Party:
                    if "exhibitionist" in E_Traits:
                        $ E_Outfit = "naked pool"
                    else:
                        $ E_Outfit = "bikini"
                    call EmmaOutfit(Changed=1) from _call_EmmaOutfit_23
                    $ E_Water = 2

        elif Mode == "auto":
                #If it's set to do it automatically by the call
                        if E_Loc == "bg pool" and E_Loc == bg_current:
                                show blackscreen onlayer black
                        if "exhibitionist" in E_Traits:
                            $ E_Outfit = "naked pool"
                        else:
                            $ E_Outfit = "bikini"
                        call EmmaOutfit(Changed=1) from _call_EmmaOutfit_24
        elif Mode == "goswim":
                #If it's set to do it automatically by the call
                if E_Over or E_Legs or E_Chest or E_Panties: #she's not walking around naked
                    if E_Loc == "bg pool" and E_Loc == bg_current:
                        ch_e "I'l be right there, let me just put on my bikini"
                        show blackscreen onlayer black
                    if "exhibitionist" in E_Traits:
                        $ E_Outfit = "naked pool"
                    else:
                        $ E_Outfit = "bikini"
                    call EmmaOutfit(Changed=1) from _call_EmmaOutfit_25
        elif E_Loc == bg_current:
                #If Emma is in the pool, see if she'll change clothes
                if ApprovalCheck("Emma", 1300, "LO") or "sub" in E_Traits:
                    pass
                elif ApprovalCheck("Emma", 800, "LO") and E_Custom[0]:
                    pass
                elif ApprovalCheck("Emma", 600, "LO") and E_Gym[0]:
                    pass
                else:
                    $ Line = "no"
                if Line == "no":   
                    #If she decides not to ask you   
                    if "arriving" in E_RecentActions:
                        pass
                    else:
                        if GirlsNum:
                            ch_e "I'll be right back too."  
                        else:
                            ch_e "I'll be back soon, gotta change."                       
                        show blackscreen onlayer black
                    if "exhibitionist" in E_Traits:
                        $ E_Outfit = "naked pool"
                    else:
                        $ E_Outfit = "bikini"
                    call EmmaOutfit(Changed=1) from _call_EmmaOutfit_26

                    if Line:
                            #If she decided to change     
                            ch_e "Ok, back in a bit"                       
                            show blackscreen onlayer black
                            if "exhibitionist" in E_Traits:
                                $ E_Outfit = "naked pool"
                            else:
                                $ E_Outfit = "bikini"
                            call EmmaOutfit(Changed=1) from _call_EmmaOutfit_27
                    #end asked
                if E_Outfit == "bikini" or E_Outfit == "naked pool":
                    $ GirlsNum += 1 
                $ Line = 0
        hide blackscreen onlayer black
        # End Emma

        return

# End Gym clothes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        

label Check_Outfit_Event:

    if E_Loc == "bg pool":
        #"Emma's here"
        if "exhibitionist" in E_Traits and E_Outfit == "naked pool" and "exhibitionist pool" not in E_History:
            $ E_History.append("exhibitionist pool")
            if Current_Time != "Night":
                "You notice that Emma is completely naked, even though the pool is packed with students."
                "You decide to approach her."
                call Change_Focus("Emma") from _call_Change_Focus_2
                ch_p "Don't get me wrong, I'm enjoying the view, but are you really ok with all the students seeing you like this?"
                call EmmaFace("confused") from _call_EmmaFace_445
                ch_e "What do you mean, [E_Petname]?"
                ch_p "Well, you know, naked."
                call EmmaFace("sexy", 1) from _call_EmmaFace_446
                ch_e "Oh, [E_Petname], I'm not naked, at least not for everyone else."
                ch_p "What do you mean?"
                call EmmaFace("smile", 1) from _call_EmmaFace_447
                ch_e "I'm a telepath [E_Petname], a very powerfull one. They see what I want them to see."
                call EmmaFace("sexy", 1) from _call_EmmaFace_448
                $ E_Wet = 1
                ch_e "But since my powers don't work on you, you're the only one here who can see me like this."
            else:
                "You notice that Emma is completely naked."
                "You approach her."
                call Change_Focus("Emma") from _call_Change_Focus_3
                ch_p "Loved the view."
                call EmmaFace("sexy", 1) from _call_EmmaFace_449
                ch_e "Do you now, [E_Petname]?"
                ch_p "You're not worried someone other than me might see you?"
                ch_e "Oh, [E_Petname], I'm not naked, at least not for everyone else."
                ch_p "What do you mean?"
                call EmmaFace("smile", 1) from _call_EmmaFace_450
                ch_e "I'm a telepath [E_Petname], a very powerfull one. Everyone else would see what I want them to see."
                call EmmaFace("sexy", 1) from _call_EmmaFace_451
                $ E_Wet = 1
                ch_e "But since my powers don't work on you, you're the only one that can see me like this."

    if R_Loc == "bg pool":
        #"Rogue's here"
        if "exhibitionist" in R_Traits and R_Outfit == "swimsuit2" and "exhibitionist pool" not in R_History:
            $ R_History.append("exhibitionist pool")
            if Current_Time != "Night":
                "You notice that Rogue is wearing a very skimpy swimsuit, even though the pool is packed with students."
                if R_Pubes:
                    "You can even see her bush"
                    "You decide to approach her."
                    call Change_Focus("Rogue") from _call_Change_Focus_4
                    ch_p "Hey [R_Pet], you know everyone can see your pubes right?"
                    call RogueFace("sexy", 1) from _call_RogueFace_261
                    ch_r "Maybe I should shave them. . ."
                    call RogueFace("sly", 1) from _call_RogueFace_262
                    ch_r "Let me know what you think later, [R_Petname]."
                    call RogueFace("sexy", 1) from _call_RogueFace_263
                else:
                    "You decide to approach her."
                    call Change_Focus("Rogue") from _call_Change_Focus_5
                    ch_p "Hey [R_Pet], you know everyone can almost see your pussy right?"
                    call RogueFace("sexy", 1) from _call_RogueFace_264
                    ch_r "Maybe I should have gotten a more revealing swimsuit them. . ."
                    #call RogueFace("sly", 1)
                    #call "Let me know what you think later."
            else:
                "You notice that Rogue is wearing a very skimpy swimsuit."
                if R_Pubes:
                    "You can even see her bush"
                    "You decide to approach her."
                    call Change_Focus("Rogue") from _call_Change_Focus_6
                    ch_p "Hey [R_Pet], you know I can see your pubes right?"
                    call RogueFace("sexy", 1) from _call_RogueFace_265
                    ch_r "Maybe I should shave them. . ."
                    call RogueFace("sly", 1) from _call_RogueFace_266
                    ch_r "Let me know what you think later, [R_Petname]."
                    call RogueFace("sexy", 1) from _call_RogueFace_267
                else:
                    "You decide to approach her."
                    call Change_Focus("Rogue") from _call_Change_Focus_7
                    ch_p "Hey [R_Pet], you know I can almost see your pussy right?"
                    call RogueFace("sexy", 1) from _call_RogueFace_268
                    ch_r "Maybe I should have gotten a more revealing swimsuit them. . ."
                    #call RogueFace("sly", 1)
                    #call "Let me know what you think later."

    if K_Loc == "bg pool":
        #"Kitty's here"
        if "exhibitionist" in K_Traits and K_Outfit == "swimsuit3" and "exhibitionist pool" not in K_History:
            $ K_History.append("exhibitionist pool")
            if Current_Time != "Night":
                "You notice that Kitty is wearing a very see-through swimsuit, even though the pool is packed with students."
                "You decide to approach her."
                call Change_Focus("Kitty") from _call_Change_Focus_8
                ch_p "Hey [K_Pet], you know everyone can see your entire body right?"
                call KittyFace("sexy", 1) from _call_KittyFace_253
                $ K_Wet = 1
                ch_k "I know, [K_Petname]. Don't I, [K_Like], look great in these?"
                ch_p "You sure do"
                call KittyFace("smile", 1) from _call_KittyFace_254
                ch_k "Thanks, [K_Petname]."
                call KittyFace("sexy", 1) from _call_KittyFace_255
            else:
                "You notice that Kitty is wearing a very see-through swimsuit."
                "You decide to approach her."
                call Change_Focus("Kitty") from _call_Change_Focus_9
                ch_p "Hey [K_Pet], you know I can see your entire body right?"
                call KittyFace("sexy", 1) from _call_KittyFace_256
                $ K_Wet = 1
                ch_k "I know, [K_Petname], are enjoying the view?"
                ch_p "I sure am"
                call KittyFace("smile", 1) from _call_KittyFace_257
                ch_k "Enjoy the view then, [K_Petname]."
                call KittyFace("sexy", 1) from _call_KittyFace_258

    return




# Start Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girls_Location(GirlsNum = 0,Clear=0):
        #Girlsnum sets the number of girls that have already talked
        #"arriving" is set by the "Schedule" code, and will not be applied unless 
        # the girl in questions was someplace else, and just showed up here on their own.
        if "leaving" in R_RecentActions:
                call Rogue_Leave from _call_Rogue_Leave_4
                if Adjacent == "Rogue" and R_Loc != "bg classroom":
                        $ Adjacent = 0
                $ GirlsNum += 1        
        if "leaving" in K_RecentActions:
                call Kitty_Leave(GirlsNum) from _call_Kitty_Leave_4
                if Adjacent == "Kitty" and K_Loc != "bg classroom":
                        $ Adjacent = 0
                $ GirlsNum += 1  
        if "leaving" in E_RecentActions:
                call Emma_Leave from _call_Emma_Leave_1
                if Adjacent == "Emma" and E_Loc != "bg classroom":
                        $ Adjacent = 0
                $ GirlsNum += 1   
        if "leaving" in newgirl["Mystique"].RecentActions:
                call Mystique_Leave from _call_Mystique_Leave_1
                if Adjacent == "Mystique" and newgirl["Mystique"].Loc != "bg classroom":
                        $ Adjacent = 0
                $ GirlsNum += 1   

        if "leaving" in newgirl["Laura"].RecentActions:
                call Laura_Leave
                if Adjacent == "Laura" and newgirl["Laura"].Loc != "bg classroom":
                        $ Adjacent = 0
                $ GirlsNum += 1   

                        
        if "arriving" in R_RecentActions:
                call Girls_Arrive from _call_Girls_Arrive
        elif "arriving" in K_RecentActions:
                call Girls_Arrive from _call_Girls_Arrive_1
        elif "arriving" in E_RecentActions:
                call Girls_Arrive from _call_Girls_Arrive_2
        elif "arriving" in newgirl["Mystique"].RecentActions:
                call Girls_Arrive from _call_Girls_Arrive_3
        elif "arriving" in newgirl["Laura"].RecentActions:
                call Girls_Arrive
        return
        
# End Girls Location / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label GirlsAngry(Girls = 0):
    # Causes girls to storm off if you've pissed them off. 
    if R_Loc == bg_current and "angry" in R_RecentActions:
            if bg_current == "bg rogue":                
                ch_r "You should get out, I'm fix'in ta throw down."
                "You head back to your room."
                $ renpy.pop_call()
                jump Player_Room_Entry
            else:        
                $ R_Loc = "bg rogue"            
            if "Rogue" in Party:
                $ Party.remove("Rogue")  
            "Rogue storms off."
            $ Girls += 1
            hide Rogue with easeoutleft
    if K_Loc == bg_current and "angry" in K_RecentActions:
            if bg_current == "bg kitty":
                ch_k "You should get out of here, I can't even look at you right now."
                "You head back to your room."
                $ renpy.pop_call()
                jump Player_Room_Entry
            else:        
                $ K_Loc = "bg kitty"
                if Girls:
                    ". . . and so does Kitty."
                else:
                    "Kitty storms off."            
            if "Kitty" in Party:
                $ Party.remove("Kitty")  
            $ Girls += 1
            hide Kitty_Sprite with easeoutleft
    if E_Loc == bg_current and "angry" in E_RecentActions:
            if bg_current == "bg emma":
                ch_e "You should leave, or do you want to test me?"
                "You head back to your room."
                $ renpy.pop_call()
                jump Player_Room_Entry
            else:        
                $ E_Loc = "bg emma"
                if Girls:
                    ". . . and so does [EmmaName]."
                else:
                    "[EmmaName] storms off."            
            if "Emma" in Party:
                $ Party.remove("Emma")  
            $ Girls += 1
            hide Emma_Sprite with easeoutleft
    if newgirl["Mystique"].Loc == bg_current and "angry" in newgirl["Mystique"].RecentActions:
            if bg_current == "bg Mystique":
                if newgirl["Mystique"].LooksLike != "Raven":
                    $ newgirl["Mystique"].LooksLike = "Raven"
                    "Mystique turns back into her original form"
                ch_m "You should leave, or do you want to test me?"
                "You head back to your room."
                $ renpy.pop_call()
                jump Player_Room_Entry
            else:        
                $ newgirl["Mystique"].Loc = "bg Mystique"
                if newgirl["Mystique"].LooksLike != "Raven":
                    $ newgirl["Mystique"].LooksLike = "Raven"
                    "Mystique turns back into her original form"
                if Girls:
                    if newgirl["Mystique"].LooksLike != "Raven":
                        $ newgirl["Mystique"].LooksLike = "Raven"
                        ". . . and so does Mystique while turning back into her original form"
                    else:
                        ". . . and so does Mystique."
                else:
                    if newgirl["Mystique"].LooksLike != "Raven":
                        $ newgirl["Mystique"].LooksLike = "Raven"
                        "Mystique turns back into her original form and storms off."            
                    else:
                        "Mystique storms off."            
            if "Mystique" in Party:
                $ Party.remove("Mystique")  
            $ Girls += 1
            hide Mystique_Sprite with easeoutleft
    if newgirl["Laura"].Loc == bg_current and "angry" in newgirl["Laura"].RecentActions:
            if bg_current == "bg Laura":
                ch_l "You should leave, or do you want to test me?"
                "You head back to your room."
                $ renpy.pop_call()
                jump Player_Room_Entry
            else:        
                $ newgirl["Laura"].Loc = "bg Laura"
                if Girls:
                    ". . . and so does [newgirl[Laura].GirlName]."
                else:
                    "[newgirl[Laura].GirlName] storms off."            
            if "Laura" in Party:
                $ Party.remove("Laura")  
            $ Girls += 1
            hide Laura_Sprite with easeoutleft
    return    
    
# Start Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Girls_Arrive(Primary = 0, Secondary = 0, GirlsNum = 0, NumPresent = 0):
    #"arriving" is set by the "Schedule" code, and will not be applied unless 
    # the girl in questions was someplace else, and just showed up here on their own.
    
    $ Options = []
    if "arriving" in R_RecentActions and "Rogue" not in Party:   
            $ GirlsNum += 1
            $ Options.append("Rogue")
            call DrainWord("Rogue","arriving") from _call_DrainWord_92  
    if "arriving" in K_RecentActions and "Kitty" not in Party: 
            $ GirlsNum += 1
            $ Options.append("Kitty")
            call DrainWord("Kitty","arriving") from _call_DrainWord_93  
    if "arriving" in E_RecentActions and "Emma" not in Party: 
            $ GirlsNum += 1
            $ Options.append("Emma")
            call DrainWord("Emma","arriving") from _call_DrainWord_94 
    if "arriving" in newgirl["Mystique"].RecentActions and "Mystique" not in Party: 
            $ GirlsNum += 1
            $ Options.append("Mystique")
            call DrainWord("Mystique","arriving") from _call_DrainWord_95  
    if "arriving" in newgirl["Laura"].RecentActions and "Laura" not in Party: 
            $ GirlsNum += 1
            $ Options.append("Laura")
            call DrainWord("Laura","arriving")
         
    $ renpy.random.shuffle(Options)
    
    $ Line = len(Options)  
    $ NumPresent = len(Options)+len(Party)      
    
    if Line <= 0 or NumPresent >= 2:
                #If nobody's here, or the space is full, return
                return    
    elif len(Party) <= 1:
                #if the party is one or less and people are in the room
                $ Primary = Options[0] 
                if len(Party) == 0 and Line >= 2:                    
                    #if the party is empty and 2+ people are in the room
                    $ Secondary = Options[1] 
                
    if Line > 2:
            #This triggers if there are more than two girls in the room. Primary and Secondary have been chosen and removed.            
            #If it's her room, she gets to be primary, otherwise she goes to her room            
            $ Options.remove(Primary)
            $ Options.remove(Secondary)
            if "Rogue" in Options:
                        if bg_current == "bg rogue":
                            $ Secondary = Primary
                            $ Primary = "Rogue"
                        else:
                            $ R_Loc = "bg rogue"
                        $ Options.remove("Rogue")
            if "Kitty" in Options:
                        if bg_current == "bg kitty":
                            $ Secondary = Primary
                            $ Primary = "Kitty"
                        else:
                            $ K_Loc = "bg kitty"
                        $ Options.remove("Kitty")   
            if "Emma" in Options:
                        if bg_current == "bg emma":
                            $ Secondary = Primary
                            $ Primary = "Emma"
                        else:
                            $ E_Loc = "bg emma"
                        $ Options.remove("Emma") 
            if "Mystique" in Options:
                        if bg_current == "bg Mystique":
                            $ Secondary = Primary
                            $ Primary = "Mystique"
                        else:
                            $ newgirl["Mystique"].Loc = "bg Mystique"
                        $ Options.remove("Mystique") 
            if "Laura" in Options:
                        if bg_current == "bg Laura":
                            $ Secondary = Primary
                            $ Primary = "Laura"
                        else:
                            $ newgirl["Laura"].Loc = "bg Laura"
                        $ Options.remove("Laura")            
            #end list clearing
            
    if Line > 3:
            #if there is 3 girl in the area, remove the excess.
            if R_Loc == bg_current and "Rogue" not in (Primary,Secondary) and "Rogue" not in Party:
                    call Remove_Girl("Rogue") from _call_Remove_Girl_49
            if K_Loc == bg_current and "Kitty" not in (Primary,Secondary) and "Kitty" not in Party:
                    call Remove_Girl("Kitty") from _call_Remove_Girl_50
            if E_Loc == bg_current and "Emma" not in (Primary,Secondary) and "Emma" not in Party:
                    call Remove_Girl("Emma") from _call_Remove_Girl_51
            if newgirl["Mystique"].Loc == bg_current and "Mystique" not in (Primary,Secondary) and "Mystique" not in Party:
                    call Remove_Girl("Mystique") from _call_Remove_Girl_52
            if newgirl["Laura"].Loc == bg_current and "Laura" not in (Primary,Secondary) and "Laura" not in Party:
                    call Remove_Girl("Laura")
    $ Options = []    
    #This sequence sets the pecking order, more important once there are more girls
    
    if bg_current == "bg dangerroom":   
            call Gym_Clothes("auto") from _call_Gym_Clothes_18
    if bg_current == "bg pool":   
            call Pool_Clothes("auto") from _call_Pool_Clothes_15
    call Set_The_Scene from _call_Set_The_Scene_108 #causes the girls to display
    if bg_current == "bg player":
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered your room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered your room."
                        
                if Primary == "Rogue":
                            if Secondary:                        
                                ch_r "Hey, [R_Petname], can we come in?"
                            else:
                                ch_r "Hey, [R_Petname], can I come in?"
                elif Primary == "Kitty":
                            if Secondary:                        
                                ch_k "Hey[K_like]can we come in?"
                            else:
                                ch_k "Hey[K_like]can I come in?"
                elif Primary == "Emma":
                            if Secondary:                        
                                ch_e "Ah, good, you're here. May we come in?"
                            else:
                                ch_e "Ah, good, you're here. May I come in?"
                elif Primary == "Mystique":
                            if Secondary:                        
                                ch_m "Ah, good, you're here. May we come in?"
                            else:
                                ch_m "Ah, good, you're here. May I come in?"
                elif Primary == "Laura":
                            if Secondary:                        
                                ch_l "Ah, good, you're here. May we come in?"
                            else:
                                ch_l "Ah, good, you're here. May I come in?"
                menu:
                    extend ""
                    "Sure.":
                        $ Line = "sure"                               
                    "Not right now, maybe later.":
                        $ Line = "later"
                    "Nope.":  
                        $ Line = "no"
                               
                                
                if Line == "sure":
                    if Primary == "Rogue" or Secondary == "Rogue":
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
                                if Primary == "Rogue": 
                                        ch_r "Thanks."
                    if Primary == "Kitty" or Secondary == "Kitty":
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                                if Primary == "Kitty":
                                        ch_k "Thanks."
                    if Primary == "Emma" or Secondary == "Emma":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                                if Primary == "Emma":
                                        ch_e "Good."
                    if Primary == "Mystique" or Secondary == "Mystique":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                                if Primary == "Mystique":
                                        ch_m "Good."
                    if Primary == "Laura" or Secondary == "Laura":
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                                if Primary == "Laura":
                                        ch_l "Good."
                    #end "sure"
                if Line == "later":     
                    if Primary == "Rogue" or Secondary == "Rogue":
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -1, 1)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5) 
                                call RogueFace("confused") from _call_RogueFace_269 
                                if Primary == "Rogue" and Secondary: 
                                        ch_r "Um, ok, we'll go then."
                                elif Primary == "Rogue":
                                        ch_r "Um, ok."
                                call Remove_Girl("Rogue") from _call_Remove_Girl_53
                    if Primary == "Kitty" or Secondary == "Kitty":  
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -2, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 7) 
                                call KittyFace("confused") from _call_KittyFace_259 
                                if Primary == "Kitty" and Secondary: 
                                        ch_k "Oh[K_like]we'll get going then."
                                elif Primary == "Kitty":
                                        ch_k "Oh[K_like]I'll get going then."
                                call Remove_Girl("Kitty") from _call_Remove_Girl_54
                    if Primary == "Emma" or Secondary == "Emma":  
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -2)
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 5) 
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -7) 
                                call EmmaFace("confused") from _call_EmmaFace_452 
                                if Primary == "Emma": 
                                        ch_e "If that's how you wish to play it. . ."
                                call Remove_Girl("Emma") from _call_Remove_Girl_55
                    if Primary == "Mystique" or Secondary == "Mystique":  
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -2)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 5) 
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -7) 
                                call MystiqueFace("confused") from _call_MystiqueFace_335 
                                if Primary == "Mystique": 
                                        ch_m "If that's how you wish to play it. . ."
                                call Remove_Girl("Mystique") from _call_Remove_Girl_56
                    if Primary == "Laura" or Secondary == "Laura":  
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -2)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5) 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -7) 
                                call LauraFace("confused")
                                if Primary == "Laura": 
                                        ch_l "If that's how you wish to play it. . ."
                                call Remove_Girl("Laura")
                    #end "later"
                if Line == "no":
                    if Primary == "Rogue" or Secondary == "Rogue":
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)         
                                if ApprovalCheck("Rogue", 1800) or ApprovalCheck("Rogue", 500, "O"):
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    ch_r "I guess that's ok. See you later then."
                                else:    
                                    call RogueFace("angry") from _call_RogueFace_270 
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -5, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -2)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1) 
                                    ch_r "Well fine!"
                                call Remove_Girl("Rogue") from _call_Remove_Girl_57
                    if Primary == "Kitty" or Secondary == "Kitty":  
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 7)         
                                if ApprovalCheck("Kitty", 1800) or ApprovalCheck("Kitty", 500, "O"):
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    ch_k "If you want some alone time. . ."
                                else:    
                                    call KittyFace("angry") from _call_KittyFace_260 
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -6, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1) 
                                    ch_k "Jerk!"
                                call Remove_Girl("Kitty") from _call_Remove_Girl_58
                    if Primary == "Emma" or Secondary == "Emma":  
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)         
                                if ApprovalCheck("Emma", 2000) or ApprovalCheck("Emma", 500, "O"):
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    ch_e "I suppose you can have your personal space. . ."
                                else:    
                                    call EmmaFace("angry") from _call_EmmaFace_453 
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 60, -6, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -4)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1) 
                                    ch_e "We'll see how long that attitude lasts. . ."
                                call Remove_Girl("Emma") from _call_Remove_Girl_59
                    if Primary == "Mystique" or Secondary == "Mystique":  
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)         
                                if ApprovalCheck("Mystique", 2000) or ApprovalCheck("Mystique", 500, "O"):
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    ch_m "I suppose you can have your personal space. . ."
                                else:    
                                    call MystiqueFace("angry") from _call_MystiqueFace_336 
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 60, -6, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -4)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1) 
                                    ch_m "We'll see how long that attitude lasts. . ."
                                call Remove_Girl("Mystique") from _call_Remove_Girl_60
                    if Primary == "Laura" or Secondary == "Laura":  
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)         
                                if ApprovalCheck("Laura", 2000) or ApprovalCheck("Laura", 500, "O"):
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    ch_l "I suppose you can have your personal space. . ."
                                else:    
                                    call LauraFace("angry")
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -6, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -4)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1) 
                                    ch_l "We'll see how long that attitude lasts. . ."
                                call Remove_Girl("Laura")
                    if Secondary:
                                "The girls storm out."
                    #end "nope"
                #end girls showed up to player's room.
    elif bg_current == "bg rogue":       
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."         
                if Primary == "Rogue" or Secondary == "Rogue":
                                if "angry" in R_DailyActions:
                                        call RogueFace("bemused", 1) from _call_RogueFace_271 
                                        ch_r "I'm kinda pissed at you right now, get out of here." 
                                elif Current_Time == "Night" and ApprovalCheck("Rogue", 1000, "LI") and ApprovalCheck("Rogue", 600, "OI"):
                                        ch_r "Oh, hey, [R_Petname], it's pretty late, but I guess you can stick around for a bit."  
                                        $ Line = "stay"                     
                                elif ApprovalCheck("Rogue", 1300) or ApprovalCheck("Rogue", 500, "O"):
                                        ch_r "Oh, hey, [R_Petname], nice to see you here."
                                        $ Line = "stay"
                                elif Current_Time == "Night":
                                        ch_r "Oh, hey, [R_Petname], it's kind late, could you head out of here?" 
                                elif ApprovalCheck("Rogue", 600, "LI") or ApprovalCheck("Rogue", 300, "OI"):
                                        ch_r "Oh, hey, [R_Petname]. You can stick around, I guess."
                                        $ Line = "stay"
                                else: 
                                        ch_r "Hey, [R_Petname], I'm not sure why you're here, but I'd rather you leave."  
                                if Line != "stay":
                                    menu:
                                        extend ""
                                        "Sure, ok.":
                                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                                                    ch_r "Thanks."
                                                    "You head back to your room."
                                        "Sorry, I'll go.":
                                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2)
                                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3) 
                                                    call RogueFace("smile") from _call_RogueFace_272 
                                                    ch_r "Thanks."
                                                    "You head back to your room."
                                        "Are you sure I can't stay?":
                                                    if "angry" in R_DailyActions:
                                                            call RogueFace("angry") from _call_RogueFace_273 
                                                            ch_r "What part of \"no\" don't ya get?"                  
                                                    elif Current_Time == "Night" and ApprovalCheck("Rogue", 800, "LI") and ApprovalCheck("Rogue", 400, "OI"):                                                            
                                                            call RogueFace("sadside") from _call_RogueFace_274 
                                                            ch_r "I suppose I can make an exception this once." 
                                                            $ Line = "stay"
                                                    elif Current_Time == "Night":
                                                            ch_r "No way, [R_Petname]. Try again tomorrow."                                                 
                                                    elif ApprovalCheck("Rogue", 750):
                                                            ch_r "Oh, fine. For a little bit."
                                                            $ Line = "stay"
                                                    else: 
                                                            call RogueFace("angry") from _call_RogueFace_275 
                                                            ch_r "No, seriously, get."    
                                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -1)
                                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                                                    "Rogue kicks you out of the room."                                                    
                                        "I'm sticking around, thanks.":   
                                                    if "angry" in R_DailyActions:
                                                            call RogueFace("angry") from _call_RogueFace_276 
                                                            ch_r "Oh {i}hell{/i} no."
                                                    elif not ApprovalCheck("Rogue", 1800) and not ApprovalCheck("Rogue", 500, "O"):
                                                            call RogueFace("angry") from _call_RogueFace_277 
                                                            ch_r "No way, buster! Out!"
                                                    else:
                                                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                                            call RogueFace("sad") from _call_RogueFace_278 
                                                            ch_r ". . ." 
                                                            ch_r "I guess that's ok."
                                                            $ Line = "stay"
                                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -5, 1)
                                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5) 
                                                    "Rogue kicks you out of the room."
                                if Line != "stay":
                                    $ bg_current = "bg player"  
                                    jump Player_Room
                                #End Rogue tells you to leave. 
                elif Primary == "Kitty":                       
                                ch_k "Hey[K_like]funny meeting you here."
                elif Primary == "Emma":                       
                                ch_e "I didn't expect to run into you here."
                elif Primary == "Mystique":                       
                                ch_m "I didn't expect to run into you here."
                elif Primary == "Laura":                       
                                ch_l "I didn't expect to run into you here."
                #end girls showed up to Rogues's room.    
            
    elif bg_current == "bg kitty":   
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."         
                if Primary == "Kitty" or Secondary == "Kitty":
                                if "angry" in K_DailyActions:
                                        call KittyFace("angry") from _call_KittyFace_261 
                                        ch_k "You shouldn't be here right now." 
                                elif Current_Time == "Night" and ApprovalCheck("Kitty", 1000, "LI") and ApprovalCheck("Kitty", 600, "OI"):
                                        ch_k "Oh, hey, it's kinds late, but you can stay for a bit."  
                                        $ Line = "stay"                     
                                elif ApprovalCheck("Kitty", 1300) or ApprovalCheck("Kitty", 500, "O"):
                                        ch_k "Oh, hey, nice to see you."
                                        $ Line = "stay"
                                elif Current_Time == "Night":
                                        ch_k "Oh, hey, [K_Petname]. It's kind of late, could you come back tomorrow?" 
                                elif ApprovalCheck("Kitty", 600, "LI") or ApprovalCheck("Kitty", 300, "OI"):
                                        ch_k "Oh, hey, [K_Petname], what's up?"
                                        $ Line = "stay"
                                else: 
                                        call KittyFace("confused") from _call_KittyFace_262 
                                        ch_k "Hey, [K_Petname], what are you even doing here?"
                                        ch_k "Could you[K_like]get out?"  
                                if Line != "stay":
                                    menu:
                                        extend ""
                                        "Sure, ok.":
                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
                                                    ch_k "Thanks."
                                                    "You head back to your room."
                                        "Sorry, I'll go.":
                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 2)
                                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3) 
                                                    call KittyFace("smile") from _call_KittyFace_263 
                                                    ch_k "Thanks."
                                                    "You head back to your room."
                                        "Are you sure I can't stay?":
                                                    if "angry" in K_DailyActions:
                                                            call KittyFace("angry") from _call_KittyFace_264 
                                                            ch_k "I think I said {i}NO!{/i}"                  
                                                    elif Current_Time == "Night" and ApprovalCheck("Kitty", 800, "LI") and ApprovalCheck("Kitty", 400, "OI"):
                                                            call KittyFace("sadside") from _call_KittyFace_265 
                                                            ch_k "Maybe just this once. . ." 
                                                            $ Line = "stay"
                                                    elif Current_Time == "Night":
                                                            ch_k "Noooope. Try again tomorrow."                                                 
                                                    elif ApprovalCheck("Kitty", 750):
                                                            ch_k "Oh, fiiiine."
                                                            ch_k "Just for a little bit."
                                                            $ Line = "stay"
                                                    else: 
                                                            ch_k "Noooope."    
                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -1)
                                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                                                    "Kitty kicks you out of the room."                                                    
                                        "I'm sticking around, thanks.":   
                                                    if "angry" in K_DailyActions:
                                                            call KittyFace("angry") from _call_KittyFace_266 
                                                            ch_k "Oh no you do not!"
                                                    elif not ApprovalCheck("Kitty", 1800) and not ApprovalCheck("Kitty", 500, "O"):
                                                            call KittyFace("angry") from _call_KittyFace_267 
                                                            ch_k "Nooope, out!"
                                                    else:
                                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                                            call KittyFace("sad") from _call_KittyFace_268 
                                                            ch_k ". . ." 
                                                            ch_k "Fine."
                                                            $ Line = "stay"
                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -5, 1)
                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 5) 
                                                    "Kitty kicks you out of the room."
                                if Line != "stay":
                                        $ bg_current = "bg player"  
                                        jump Player_Room
                                        #End Kitty tells you to leave. 
                elif Primary == "Rogue":                       
                                ch_r "Sorry, I wasn't expecting to bump into you here."
                elif Primary == "Emma":                       
                                ch_e "I didn't expect to run into you here."
                elif Primary == "Mystique":                       
                                ch_m "I didn't expect to run into you here."
                elif Primary == "Laura":                       
                                ch_l "I didn't expect to run into you here."
                #end girls showed up to Kitty's room.
    elif bg_current == "bg emma": 
                if Secondary:  
                        #if there's a second girl
                        "[Primary] and [Secondary] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary] just entered the room."         
                if Primary == "Emma" or Secondary == "Emma":
                                if "angry" in E_DailyActions:
                                        call EmmaFace("angry") 
                                        ch_e "I don't think you should be here." 
                                elif Current_Time == "Night" and ApprovalCheck("Emma", 1000, "LI") and ApprovalCheck("Emma", 600, "OI"):
                                        ch_e "Oh, it's a bit late, but you're welcome."  
                                        $ Line = "stay"                     
                                elif ApprovalCheck("Emma", 1300) or ApprovalCheck("Emma", 500, "O"):
                                        ch_e "Oh, nice to see you."
                                        $ Line = "stay"
                                elif Current_Time == "Night":
                                        ch_e "Oh, hello, [E_Petname]. It's a bit late, could you come back tomorrow?" 
                                elif ApprovalCheck("Emma", 600, "LI") or ApprovalCheck("Emma", 300, "OI"):
                                        ch_e "Oh, hello, [E_Petname], can I help you with anything?"
                                        $ Line = "stay"
                                else: 
                                        call EmmaFace("confused") 
                                        ch_e "Oh, hello, [E_Petname]?"
                                        ch_e "Did you have a reason to be visiting me?"  
                                if Line != "stay":
                                    menu:
                                        extend ""
                                        "Sure, ok. [[you go]":
                                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)  
                                                    ch_e "Appreciated."
                                                    "You head back to your room."
                                        "Sorry, I'll go.":
                                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)
                                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3) 
                                                    call EmmaFace("smile") 
                                                    ch_e "Thank you."
                                                    "You head back to your room."
                                        "Are you sure I can't stay?":
                                                    if "angry" in E_DailyActions:
                                                            call EmmaFace("angry") 
                                                            ch_e "I believe I said {i}no.{/i}"                  
                                                    elif Current_Time == "Night" and ApprovalCheck("Emma", 800, "LI") and ApprovalCheck("Emma", 400, "OI"):
                                                            call EmmaFace("sadside") 
                                                            ch_e "Perhaps just this once. . ." 
                                                            $ Line = "stay"
                                                    elif Current_Time == "Night":
                                                            ch_e "I'm afraid not. Try again tomorrow."                                                 
                                                    elif ApprovalCheck("Emma", 750):
                                                            ch_e "Oh, very well. . ."
                                                            ch_e "Just for a little bit."
                                                            $ Line = "stay"
                                                    else: 
                                                            ch_e "Definitely not."    
                                                    if Line != "stay":
                                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -1)
                                                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                                                            "Emma kicks you out of the room."                                                    
                                        "I'm sticking around, thanks.":   
                                                    if "angry" in E_DailyActions:
                                                            call EmmaFace("angry") 
                                                            ch_e "You must be joking."
                                                    elif not ApprovalCheck("Emma", 1800) and not ApprovalCheck("Emma", 500, "O"):
                                                            call EmmaFace("angry") 
                                                            ch_e "No, get out."
                                                    else:
                                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                                            call EmmaFace("sad") 
                                                            ch_e ". . ." 
                                                            ch_e "Fine."
                                                            $ Line = "stay"
                                                    if Line != "stay":
                                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 60, -5, 1)
                                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -5)
                                                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                                                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                                                            "Emma kicks you out of the room."
                                if Line != "stay":
                                        $ bg_current = "bg player"  
                                        jump Player_Room
                                        #End Emma tells you to leave. 
                elif Primary == "Rogue":                       
                                ch_r "Sorry, I wasn't expecting to bump into you here."
                elif Primary == "Kitty":                       
                                ch_k "Hey[K_like]funny meeting you here."
                elif Primary == "Mystique":                       
                                ch_m "I didn't expect to run into you here."
                elif Primary == "Laura":                       
                                ch_l "I didn't expect to run into you here."
                #end girls showed up to Emma's room.
    elif bg_current == "bg Mystique": 
            #add room content here
            pass
    elif bg_current == "bg classroom":   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the room."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the room." 
            $ D20 = renpy.random.randint(1, 20) 
            $ Line = 0
            if Primary == "Rogue" or Secondary == "Rogue":
            #Determines who sits next to you
                            ch_r "Hey, [R_Petname]."
                            if not Secondary and not Adjacent and ApprovalCheck("Rogue", 1000):                                
                                        "Rogue sits down next to you."  
                                        $ Adjacent = "Rogue"
                            elif Secondary and not Adjacent and ApprovalCheck("Rogue", 1000): 
                                if D20 >= 10:
                                        "Rogue sits down next to you."
                                        $ Adjacent = "Rogue"
                                else:
                                        $ Line = "and Rogue sits down nearby."
                            else:
                                        "Rogue sits across the room from you."
            elif Primary == "Kitty" or Secondary == "Kitty":
                            ch_k "Oh, hey."
                            if not Secondary and not Adjacent and ApprovalCheckApprovalCheck("Kitty", 1000):    
                                        #if nobody got picked earlier, and nobody else is around, and she likes you,
                                        "Kitty sits down next to you."  
                                        $ Adjacent = "Kitty"                          
                            elif Secondary and not Adjacent and ApprovalCheck("Kitty", 1000): 
                                #if nobody got picked earlier, and she likes you,
                                if Line:
                                        #if another earlier girl got passed up,
                                        $ Line = "Kitty sits down next to you " + Line
                                        "[Line]"
                                        $ Adjacent = "Kitty"                                    
                                elif D20 >= 10:
                                        #if there were no previous girl,
                                        "Kitty sits down next to you."
                                        $ Adjacent = "Kitty"
                                else:
                                        $ Line = "and Kitty sits down nearby."                            
                            else:
                                        #If she doesn't like you, or someone else got picked to sit with you.
                                        "Kitty sits across the room from you."
            if Primary == "Emma" or Secondary == "Emma":
                pass
            if Primary == "Mystique" or Secondary == "Mystique":
                                ch_m "Oh, hello."
            if Primary == "Laura" or Secondary == "Laura":
                                ch_l "Oh, hello."
            if E_Loc == "bg teacher":
                    "Emma takes her position behind the podium."
            #end girls showed up to the Danger Room
    elif bg_current == "bg field":   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the pool area."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the pool area."   
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            elif Primary == "Kitty" or Secondary == "Kitty":
                                ch_k "Oh, hey."
            elif Primary == "Emma" or Secondary == "Emma":
                                ch_e "Oh, hello, [E_Petname]."
            if Primary == "Mystique" or Secondary == "Mystique":
                                ch_m "Oh, hello."
            #end girls showed up to the football field
    elif bg_current == "bg dangerroom":   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the room."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the room."   
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            elif Primary == "Kitty" or Secondary == "Kitty":
                                ch_k "Oh, hey."
            elif Primary == "Emma" or Secondary == "Emma":
                                if "metgym" not in E_History:     
                                    $ E_Gym = [2,0,0,"cape","NewX","corset","white panties",0,0,"white thigh high",0]  
                                    $ E_Over = "cape"
                                    $ E_Legs = 0
                                    $ E_Panties = "white panties"
                                    $ E_Neck = "NewX"      
                                    $ E_Hose = "white thigh high"  
                                    $ E_Outfit = "gym"
                                    call Present_Check from _call_Present_Check_4 #updates who is present                    
                                    jump EmmaMeetGym_Waited
                                ch_e "Oh, hello, [E_Petname]."
            if Primary == "Mystique" or Secondary == "Mystique":
                                if "metgym" not in newgirl["Mystique"].History:     
                                    $ newgirl["Mystique"].Gym = [2,0,"workout pants","workout jacket",0,"workout top","black panties",0,0,0,0]
                                    $ newgirl["Mystique"].Over = "workout jacket"
                                    $ newgirl["Mystique"].Chest = "workout top"
                                    $ newgirl["Mystique"].Legs = "workout pants"
                                    $ newgirl["Mystique"].Panties = "black panties"
                                    $ newgirl["Mystique"].Neck = 0      
                                    $ newgirl["Mystique"].Glasses = 0      
                                    $ newgirl["Mystique"].Outfit = "gym"
                                    call Present_Check from _call_Present_Check_5 #updates who is present                    
                                    jump MystiqueMeetGym_Waited
                                ch_m "Oh, hello."
            #end girls showed up to the Danger Room
    elif bg_current == "bg pool":   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the pool area."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the pool area."   
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            elif Primary == "Kitty" or Secondary == "Kitty":
                                ch_k "Oh, hey."
            elif Primary == "Emma" or Secondary == "Emma":
                                ch_e "Oh, hello, [E_Petname]."
            if Primary == "Mystique" or Secondary == "Mystique":
                                ch_m "Oh, hello."
            #end girls showed up to the Danger Room
    elif bg_current == "bg campus":   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the square."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the square."   
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            elif Primary == "Kitty" or Secondary == "Kitty":
                            ch_k "Oh, hey."
            elif Primary == "Emma" or Secondary == "Emma":
                            ch_e "Oh, hello, [E_Petname]."
            if Primary == "Mystique" or Secondary == "Mystique":
                                ch_m "Oh, hello."
            #end girls showed up to the campus
    else: #if it's anywhere else,   
            if Secondary:  
                    #if there's a second girl
                    "[Primary] and [Secondary] just entered the room."
            else:
                    #if there's no second girl,
                    "[Primary] just entered the room."   
            if Primary == "Rogue" or Secondary == "Rogue":
                            ch_r "Hey, [R_Petname]."
            elif Primary == "Kitty" or Secondary == "Kitty":
                            ch_k "Oh, hey."
            elif Primary == "Emma" or Secondary == "Emma":
                            ch_e "Oh, hello, [E_Petname]."
            if Primary == "Mystique" or Secondary == "Mystique":
                                ch_m "Oh, hello."
            #end girls showed up someplace
                                
                                
    #end "girls showed up"    
    call Present_Check from _call_Present_Check_6 #updates who is present                    
    return
# End Girls Arrive / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    
    
# Start Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label LastNamer(NameTemp = Playername, Wordcount = 0, Splitname = 0, Lastname = 0):
    # Wordcount = number of words
    $ Wordcount = Playername.count(" ")
    # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
    $ Splitname = Playername.split()
    # Lastname picks the last word in that set
    $ Lastname = "Mr. " + Splitname[Wordcount]
#    $ R_Petnames.append(Lastname)
#    $ R_Petname = Lastname
    return Lastname
# End Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


# Start LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label LikeUpdater(Primary = "Rogue", Value = 1, Noticed = 1):
    # call LikeUpdater("Rogue",1)
    # Primary is the primary girl in action, Value is the amount added/subtracted
    # Noticed is whether it matters if she notices or not.
    
    if Primary == "Rogue":
            if K_Loc == bg_current:
                if not Noticed or "noticed Rogue" in K_RecentActions: 
                    #If Kitty was participating in Rogue's activity
                    $ K_LikeRogue += Value
                    $ R_LikeKitty += Value
    
            if E_Loc == bg_current:
                if not Noticed or "noticed Rogue" in E_RecentActions: 
                    #If Emma was participating in Rogue's activity
                    $ E_LikeRogue += Value
                    $ R_LikeEmma += Value
            
            if newgirl["Laura"].Loc == bg_current:
                if not Noticed or "noticed Rogue" in newgirl["Laura"].RecentActions: 
                    #If Laura was participating in Rogue's activity
                    $ newgirl["Laura"].LikeRogue += Value
                    $ R_LikeNewGirl["Laura"] += Value

            if newgirl["Mystique"].Loc == bg_current:
                if not Noticed or "noticed Rogue" in newgirl["Mystique"].RecentActions: 
                    #If Mystique was participating in Rogue's activity
                    $ newgirl["Mystique"].LikeRogue += Value
                    $ R_LikeNewGirl["Mystique"] += Value
                    
    elif Primary == "Kitty":
            if R_Loc == bg_current:
                if not Noticed or "noticed Kitty" in R_RecentActions: 
                    #If Rogue was participating in Kitty's activity
                    $ R_LikeKitty += Value
                    $ K_LikeRogue += Value
            
            if E_Loc == bg_current:
                if not Noticed or "noticed Kitty" in E_RecentActions: 
                    #If Emma was participating in Kitty's activity
                    $ E_LikeRogue += Value
                    $ K_LikeEmma += Value
                    
            if newgirl["Laura"].Loc == bg_current:
                if not Noticed or "noticed Kitty" in newgirl["Laura"].RecentActions: 
                    #If Laura was participating in Kitty's activity
                    $ newgirl["Laura"].LikeKitty += Value
                    $ K_LikeNewGirl["Laura"] += Value  

            if newgirl["Mystique"].Loc == bg_current:
                if not Noticed or "noticed Kitty" in newgirl["Mystique"].RecentActions: 
                    #If Mystique was participating in Kitty's activity
                    $ newgirl["Mystique"].LikeKitty += Value
                    $ K_LikeNewGirl["Mystique"] += Value                    
                    
    elif Primary == "Emma":
            if R_Loc == bg_current:
                if not Noticed or "noticed Emma" in R_RecentActions: 
                    #If Rogue was participating in Emma's activity
                    $ R_LikeEmma += Value
                    $ E_LikeRogue += Value
            
            if K_Loc == bg_current:
                if not Noticed or "noticed Emma" in K_RecentActions: 
                    #If Kitty was participating in Emma's activity
                    $ K_LikeEmma += Value
                    $ E_LikeRogue += Value
                    
            if newgirl["Laura"].Loc == bg_current:
                if not Noticed or "noticed Emma" in newgirl["Laura"].RecentActions: 
                    #If Laura was participating in Emma's activity
                    $ newgirl["Laura"].LikeEmma += Value
                    $ E_LikeNewGirl["Laura"] += Value

            if newgirl["Mystique"].Loc == bg_current:
                if not Noticed or "noticed Emma" in newgirl["Mystique"].RecentActions: 
                    #If Mystique was participating in Emma's activity
                    $ newgirl["Mystique"].LikeEmma += Value
                    $ E_LikeNewGirl["Mystique"] += Value
                    
    elif Primary == "Laura":
            if R_Loc == bg_current:
                if not Noticed or "noticed Laura" in R_RecentActions: 
                    #If Rogue was participating in Laura's activity
                    $ R_LikeNewGirl["Laura"] += Value
                    $ newgirl["Laura"].LikeRogue += Value
            
            if K_Loc == bg_current:
                if not Noticed or "noticed Laura" in K_RecentActions: 
                    #If Kitty was participating in Laura's activity
                    $ K_LikeNewGirl["Laura"] += Value
                    $ newgirl["Laura"].LikeRogue += Value
                    
            if E_Loc == bg_current:
                if not Noticed or "noticed Laura" in E_RecentActions: 
                    #If Emma was participating in Laura's activity
                    $ E_LikeNewGirl["Laura"] += Value
                    $ newgirl["Laura"].LikeEmma += Value

            if newgirl["Mystique"].Loc == bg_current:
                if not Noticed or "noticed Laura" in newgirl["Mystique"].RecentActions: 
                    #If Mystique was participating in Emma's activity
                    $ newgirl["Mystique"].LikeNewGirl["Laura"] += Value
                    $ newgirl["Laura"].LikeNewGirl["Mystique"] += Value

    elif Primary == "Mystique":
            if R_Loc == bg_current:
                if not Noticed or "noticed Mystique" in R_RecentActions: 
                    #If Rogue was participating in Mystique's activity
                    $ R_LikeNewGirl["Mystique"] += Value
                    $ newgirl["Mystique"].LikeRogue += Value
            
            if K_Loc == bg_current:
                if not Noticed or "noticed Mystique" in K_RecentActions: 
                    #If Kitty was participating in Mystique's activity
                    $ K_LikeNewGirl["Mystique"] += Value
                    $ newgirl["Mystique"].LikeRogue += Value
                    
            if E_Loc == bg_current:
                if not Noticed or "noticed Mystique" in E_RecentActions: 
                    #If Emma was participating in Mystique's activity
                    $ E_LikeNewGirl["Mystique"] += Value
                    $ newgirl["Mystique"].LikeEmma += Value

            if newgirl["Mystique"].Loc == bg_current:
                if not Noticed or "noticed Mystique" in newgirl["Laura"].RecentActions: 
                    #If Laura was participating in Emma's activity
                    $ newgirl["Laura"].LikeNewGirl["Mystique"] += Value
                    $ newgirl["Mystique"].LikeNewGirl["Laura"] += Value

    # elif Primary == "Mystique":
    #         if R_Loc == bg_current:
    #             if not Noticed or "noticed emma" in R_RecentActions: 
    #                 #If Rogue was participating in Emma's activity
    #                 $ R_LikeEmma += Value
    #                 $ E_LikeRogue += Value
            
    #         if K_Loc == bg_current:
    #             if not Noticed or "noticed emma" in K_RecentActions: 
    #                 #If Kitty was participating in Emma's activity
    #                 $ K_LikeEmma += Value
    #                 $ E_LikeRogue += Value

    #         if E_Loc == bg_current:
    #             if not Noticed or "noticed kitty" in E_RecentActions: 
    #                 #If Emma was participating in Kitty's activity
    #                 $ E_LikeRogue += Value
    #                 $ K_LikeEmma += Value
    
    return
    
# End LikeUpdater / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Girls_Noticed(Primary="Rogue"):
    #Checks to see if some other girl noticed the primary in action.
    if R_Loc == bg_current and Primary != "Rogue":
                call Rogue_Noticed(Primary)
    if K_Loc == bg_current and Primary != "Kitty":
                call Kitty_Noticed(Primary)
    if newgirl["Laura"].Loc == bg_current and Primary != "Laura":
                call Laura_Noticed(Primary)
    if E_Loc == bg_current and Primary != "Emma":
                call Emma_Noticed(Primary)
    return

label Partner_Threechange(Girl=0):  
        # this routine thorws it to the specific character's threresome activity change
        # Girl is the lead of the encounter, this is called from Threesome actions during sex scenes
        if Partner == Girl:
                "Let Oni know that both roles are set to [Girl]."
                return
        if Partner == "Rogue":
                call Rogue_Three_Change(Girl)        
        elif Partner == "Kitty":
                call Kitty_Three_Change(Girl)
        elif Partner == "Emma":
                call Emma_Three_Change(Girl) 
        elif Partner == "Laura":
                call Laura_Three_Change(Girl) 
        return
    
label Partner_Cleanup:
        # this routine checks if the Partner has jiz on her, and cleans up if yes
        # this is called from Threesome actions during sex scenes
        if not Partner:
                return
        if Partner == "Rogue" and R_Spunk:
                call Rogue_Cleanup("ask")  
        elif Partner == "Kitty" and K_Spunk:
                call Kitty_Cleanup("ask")    
        elif Partner == "Emma" and E_Spunk:
                call Emma_Cleanup("ask")  
        elif Partner == "Laura" and newgirl["Laura"].Spunk:
                call Laura_Cleanup("ask")  
        else:
                "She seems fine."
        return
    
label Partner_Undress:   
        # this routine undresses the partner in a scene
        # this is called from Threesome actions during sex scenes 
        if Partner == "Rogue":
                call R_Undress   
        elif Partner == "Kitty":
                call K_Undress   
        elif Partner == "Emma":
                call E_Undress 
        elif Partner == "Laura":
                call Laura_Undress
        return
    
label Partner_Cumming(Girl=0):
        # this routine is called if the Partner might cum
        #Girl would be the non-Partner
        if R_Lust >= 100 and R_Loc == bg_current and Girl != "Rogue":                                          
            call R_Cumming
        if K_Lust >= 100 and K_Loc == bg_current and Girl != "Kitty":                                          
            call K_Cumming
        if E_Lust >= 100 and E_Loc == bg_current and Girl != "Emma":                                          
            call E_Cumming     
        if newgirl["Laura"].Lust >= 100 and newgirl["Laura"].Loc == bg_current and Girl != "Laura":                                          
            call Laura_Cumming    
        return

label Partner_Like(Girl=0,Value=1,AltValue=1,Measure=800,Backsies=0,Partner=Partner):
        # Thi raises a partner's "like" stat by an amount
        # call Partner_Like("Rogue",2)
        # Girl is the lead, Partner is the second girl
        # Value is the amount it changes if Measure is met, otherwise AltValue
        # Set Backsies to 1, or this will looptwice to cover both girls equally
        
        if not Girl or not Partner:
                return
                
        if Trigger4:
                # if the Partner is doing a secondary action. . .
                if Trigger4 == "watch":
                        pass
                elif Trigger4 in ("hand","blow"):
                        $ Value += 1
                elif Trigger4 in ("lick pussy","lick ass"):
                        $ Value += 3                
                else:
                        $ Value += 2
        #End Trigger4 bonuses
            
        if Girl == "Rogue":
                if Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeRogue += Value if K_LikeRogue >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeRogue += Value if E_LikeRogue >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ newgirl["Laura"].LikeRogue += Value if newgirl["Laura"].LikeRogue >= Measure else AltValue
        elif Girl == "Kitty":
                if Partner == "Rogue": 
                        #If Kitty was participating
                        $ R_LikeKitty += Value if R_LikeKitty >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeKitty += Value if E_LikeKitty >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ newgirl["Laura"].LikeKitty += Value if newgirl["Laura"].LikeKitty >= Measure else AltValue
        elif Girl == "Emma":
                if Partner == "Rogue":  
                        #If Emma was participating
                        $ R_LikeEmma += Value if R_LikeEmma >= Measure else AltValue
                elif Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeEmma += Value if K_LikeEmma >= Measure else AltValue
                elif Partner == "Laura":  
                        #If Laura was participating
                        $ newgirl["Laura"].LikeEmma += Value if newgirl["Laura"].LikeEmma >= Measure else AltValue
        elif Girl == "Laura":
                if Partner == "Rogue":  
                        #If Emma was participating
                        $ R_LikeNewGirl["Laura"] += Value if R_LikeNewGirl["Laura"] >= Measure else AltValue
                elif Partner == "Kitty": 
                        #If Kitty was participating
                        $ K_LikeNewGirl["Laura"] += Value if K_LikeNewGirl["Laura"] >= Measure else AltValue
                elif Partner == "Emma":  
                        #If Emma was participating
                        $ E_LikeNewGirl["Laura"] += Value if E_LikeNewGirl["Laura"] >= Measure else AltValue
        
        if not Backsies:        
                        # this bit causes the function to go through a second cycle, 
                        # skipping this bit and then returning here
                        # the point is to give points going the opposite direction
                        $ Backsies = Partner 
                        $ Partner = Girl 
                        $ Girl = Backsies
                        call Partner_Like(Girl,Value,AltValue,Backsies=Backsies)  
                        $ Partner = Girl
                        
        return
#End Partner_Like


    
# Start Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Sex_Dialog(Primary = Ch_Focus, Secondary = 0, TempFocus = 0, PrimaryLust = 0, SecondaryLust = 0, Line1 = 0, Line2 = 0, Line3 = 0, Line4 = 0, D20S = 0): #call Sex_Dialog("Rogue","Kitty") 
        # Primary is main female, secondary is supporting female, action is what they are doing.
        $ Line = 0
        
        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S #Sets random seed factor for the encounter
        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play. 
           
        # Checks for Taboo, and if it passes through, calls the first sex dialog
        if Primary == "Rogue":
                    if K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Rogue") from _call_Kitty_Noticed
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Rogue")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        call Laura_Noticed(Primary)
                        $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Rogue_Taboo from _call_Rogue_Taboo                    
                    call Rogue_SexDialog from _call_Rogue_SexDialog    
                                    
        elif Primary == "Kitty":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Kitty") from _call_Rogue_Noticed
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Kitty")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Kitty_Taboo from _call_Kitty_Taboo                    
                    call Kitty_SexDialog from _call_Kitty_SexDialog
                    
        elif Primary == "Emma":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Emma") from _call_Rogue_Noticed_1
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Emma") from _call_Kitty_Noticed_1
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        call Laura_Noticed(Primary)
                        $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Emma_Taboo from _call_Emma_Taboo                    
                    call Emma_SexDialog from _call_Emma_SexDialog

        elif Primary == "Mystique":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Mystique") from _call_Rogue_Noticed_2
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Mystique") from _call_Kitty_Noticed_2
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif newgirl["Laura"].Loc == bg_current and not Taboo:
                        call Laura_Noticed(Primary)
                        $ Secondary = "Laura" if newgirl["Laura"].Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Mystique_Taboo from _call_Mystique_Taboo_1                    
                    call Mystique_SexDialog from _call_Mystique_SexDialog

        elif Primary == "Laura":
                    if R_Loc == bg_current and not Taboo:                           #If Rogue is around and it's otherwise private
                        call Rogue_Noticed("Laura")
                        $ Secondary = "Rogue" if R_Loc == bg_current else Secondary
                    elif K_Loc == bg_current and not Taboo:                           #If Kitty is around and it's otherwise private
                        call Kitty_Noticed("Laura")
                        $ Secondary = "Kitty" if K_Loc == bg_current else Secondary
                    elif E_Loc == bg_current and not Taboo:                           #If Emma is around and it's otherwise private
                        call Emma_Noticed("Kitty")
                        $ Secondary = "Emma" if E_Loc == bg_current else Secondary
                    elif Taboo and (D20S + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                        call Laura_Taboo
                    call Laura_SexDialog
        
        
        $ Line1 = Line #Set Line1 to the current state of the Line variable
                
        # If there is a player offhand Trigger set and the random value is 1-15, add an Offhand dialog
        if Trigger2 and D20S <= 15:
                    $ Line = ""
                    if Primary == "Rogue":                        
                        call Rogue_Offhand from _call_Rogue_Offhand
                    elif Primary == "Kitty":
                        call Kitty_Offhand from _call_Kitty_Offhand
                    elif Primary == "Emma":
                        call Emma_Offhand from _call_Emma_Offhand_1
                    elif Primary == "Mystique":
                        call Mystique_Offhand from _call_Mystique_Offhand
                    elif Primary == "Laura":
                        call Laura_Offhand
                    
                    $ Line1 = Line1 + Line
        else:                
                    $ Line1 = Line1 +"."
        
        # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
        if D20S >= 7 and Trigger not in ("masturbation", "lesbian"):
                    $ Line = 0
                    if Primary == "Rogue":
                        call Rogue_Self_Lines("T3",Trigger3) from _call_Rogue_Self_Lines      
                    elif Primary == "Kitty":
                        call Kitty_Self_Lines("T3",Trigger3) from _call_Kitty_Self_Lines_3      
                    elif Primary == "Emma":
                        call Emma_Self_Lines("T3",Trigger3) from _call_Emma_Self_Lines 
                    elif Primary == "Mystique":
                        call NewGirl_Self_Lines("Mystique","T3",Trigger3) from _call_NewGirl_Self_Lines 
                    elif Primary == "Laura":
                        call NewGirl_Self_Lines("Laura","T3",Trigger3)
                    if Line:
                        $ Line3 = Line + "."
           
        # If there is a Secondary character and the random value is 5-15, add a threeway dialog
        if Secondary and (7 <= D20S <= 17 or Trigger4 == "watch"):
                    $ Line = 0
                    if Secondary == "Rogue":
                        call Rogue_SexDialog_Threeway from _call_Rogue_SexDialog_Threeway
                    elif Secondary == "Kitty":
                        call Kitty_SexDialog_Threeway from _call_Kitty_SexDialog_Threeway_1
                    elif Secondary == "Emma":
                        call Emma_SexDialog_Threeway from _call_Emma_SexDialog_Threeway
                    elif Secondary == "Mystique":
                        call Mystique_SexDialog_Threeway from _call_Mystique_SexDialog_Threeway
                    elif Secondary == "Laura":
                        call Laura_SexDialog_Threeway
                    if Line:
                        $ Line4 = Line + "."
        
        #Applying player's satisfaction
        $ P_Focus = Statupdate("Player", "Focus", P_Focus, 200, TempFocus) 
        
        #Applying primary girl's satisfaction
        if Primary == "Rogue":
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, PrimaryLust) 
                call RogueLust from _call_RogueLust_1                         
        elif Primary == "Kitty":
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, PrimaryLust)
                call KittyLust from _call_KittyLust_9                          
        elif Primary == "Emma":
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, PrimaryLust)
                call EmmaLust from _call_EmmaLust_10 
        elif Primary == "Mystique":
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, PrimaryLust)
                call MystiqueLust from _call_MystiqueLust_11    
        elif Primary == "Laura":
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, PrimaryLust)
                call MystiqueLust
        
        #Applying secondary girl's satisfaction
        if Secondary == "Rogue":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and R_LikeKitty >= 70 else 0  
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and R_LikeEmma >= 70 else 0 
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and R_LikeNewGirl[Primary] >= 70 else 0 
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, SecondaryLust) 
                call RogueLust from _call_RogueLust_2
        elif Secondary == "Kitty":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and K_LikeRogue >= 70 else 0  
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and K_LikeEmma >= 70 else 0        
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and K_LikeNewGirl[Primary] >= 70 else 0        
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, SecondaryLust)
                call KittyLust from _call_KittyLust_10 
        elif Secondary == "Emma":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and E_LikeRogue >= 50 else 0   
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and E_LikeKitty >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and E_LikeNewGirl[Primary] >= 50 else 0     
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, SecondaryLust)
                call EmmaLust from _call_EmmaLust_11
        elif Secondary == "Mystique" or Secondary == "Laura":
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Rogue" and newgirl[Secondary].LikeRogue >= 50 else 0   
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Kitty" and newgirl[Secondary].LikeKitty >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if Primary == "Emma" and newgirl[Secondary].LikeEmma >= 50 else 0     
                $ SecondaryLust += (int(PrimaryLust/10)) if (Primary == "Laura" or Primary == "Mystique") and newgirl[Secondary].LikeNewGirl[Primary] >= 50 else 0     
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl[Secondary].Lust, 200, SecondaryLust)
                if Secondary == "Mystique":
                    call MystiqueLust
                elif Secondary == "Laura":
                    call LauraLust

        # Dialog begins to play out. . .  
        
        "[Line1]"
        $ Line = Line1
        if Line3:
                #If there's a secondary line, play it
                "[Line3]"
                $ Line = Line3
        if Line4:   
                #add call to First Les here."
                #If there's a third person line, play it
                "[Line4]"
                $ Line = Line4
        call NewGirl_Dirty_Talk from _call_NewGirl_Dirty_Talk
                        
        return
        
    
# End Primary Sex Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label CloseOut(Chr = "Rogue"):
    # This exits out of the current sex act, whichever it might be, then returns
    if Chr == "Rogue":
            if Trigger == "blow":
                call R_BJAfter from _call_R_BJAfter
            elif Trigger == "hand":  
                call R_HJAfter from _call_R_HJAfter  
            elif Trigger == "titjob":
                call R_TJAfter from _call_R_TJAfter
            elif Trigger == "kissing":
                call R_Kiss_After from _call_R_Kiss_After
            elif Trigger == "fondle breasts":
                call RFB_After from _call_RFB_After
            elif Trigger == "suck breasts":
                call RSB_After from _call_RSB_After
            elif Trigger == "fondle thighs":
                call RFT_After from _call_RFT_After
            elif Trigger == "fondle pussy":
                call RFP_After from _call_RFP_After
            elif Trigger == "lick pussy":
                call RLP_After from _call_RLP_After
            elif Trigger == "fondle ass":
                call RFA_After from _call_RFA_After
            elif Trigger == "insert ass":
                call RIA_After from _call_RIA_After
            elif Trigger == "lick ass":
                call RLA_After from _call_RLA_After
            elif Trigger == "sex":
                call R_SexAfter from _call_R_SexAfter
            elif Trigger == "hotdog":
                call R_HotdogAfter from _call_R_HotdogAfter
            elif Trigger == "anal":
                call R_AnalAfter from _call_R_AnalAfter
            elif Trigger == "dildo pussy":
                call RDP_After from _call_RDP_After
            elif Trigger == "dildo anal":
                call RDA_After from _call_RDA_After
            elif Trigger == "strip":
                call R_Strip_End from _call_R_Strip_End
            else:
                "That's odd, tell Oni how you got here."
    #End Rogue
    elif Chr == "Kitty":
            if Trigger == "blow":
                call K_BJAfter from _call_K_BJAfter
            elif Trigger == "hand":  
                call K_HJAfter from _call_K_HJAfter  
            elif Trigger == "titjob":
                call K_TJAfter from _call_K_TJAfter
            elif Trigger == "kissing":
                call K_Kiss_After from _call_K_Kiss_After
            elif Trigger == "fondle breasts":
                call KFB_After from _call_KFB_After_3
            elif Trigger == "suck breasts":
                call KSB_After from _call_KSB_After_2
            elif Trigger == "fondle thighs":
                call KFT_After from _call_KFT_After_3
            elif Trigger == "fondle pussy":
                call KFP_After from _call_KFP_After_4
            elif Trigger == "lick pussy":
                call KLP_After from _call_KLP_After_2
            elif Trigger == "fondle ass":
                call KFA_After from _call_KFA_After_5
            elif Trigger == "insert ass":
                call KIA_After from _call_KIA_After_4
            elif Trigger == "lick ass":
                call KLA_After from _call_KLA_After_4
            elif Trigger == "sex":
                call K_SexAfter from _call_K_SexAfter
            elif Trigger == "hotdog":
                call K_HotdogAfter from _call_K_HotdogAfter
            elif Trigger == "anal":
                call K_AnalAfter from _call_K_AnalAfter
            elif Trigger == "dildo pussy":
                call KDP_After from _call_KDP_After
            elif Trigger == "dildo anal":
                call KDA_After from _call_KDA_After
            elif Trigger == "strip":
                call K_Strip_End from _call_K_Strip_End
            else:
                "That's odd, tell Oni how you got here."
    elif Chr == "Emma":
            if Trigger == "blow":
                call E_BJAfter from _call_E_BJAfter_3
            elif Trigger == "hand":  
                call E_HJAfter from _call_E_HJAfter_1  
            elif Trigger == "titjob":
                call E_TJAfter from _call_E_TJAfter_2
            elif Trigger == "kissing":
                call E_Kiss_After from _call_E_Kiss_After
            elif Trigger == "fondle breasts":
                call E_FB_After from _call_E_FB_After
            elif Trigger == "suck breasts":
                call E_SB_After from _call_E_SB_After
            elif Trigger == "fondle thighs":
                call E_FT_After from _call_E_FT_After
            elif Trigger == "fondle pussy":
                call E_FP_After from _call_E_FP_After
            elif Trigger == "lick pussy":
                call E_LP_After from _call_E_LP_After
            elif Trigger == "fondle ass":
                call E_FA_After from _call_E_FA_After
            elif Trigger == "insert ass":
                call E_IA_After from _call_E_IA_After
            elif Trigger == "lick ass":
                call E_LA_After from _call_E_LA_After
            elif Trigger == "sex":
                call E_SexAfter from _call_E_SexAfter
            elif Trigger == "hotdog":
                call E_HotdogAfter from _call_E_HotdogAfter
            elif Trigger == "anal":
                call E_AnalAfter from _call_E_AnalAfter
            elif Trigger == "dildo pussy":
                call E_DP_After from _call_E_DP_After
            elif Trigger == "dildo anal":
                call E_DA_After from _call_E_DA_After
            elif Trigger == "strip":
                call E_Strip_End from _call_E_Strip_End
            else:
                "That's odd, tell Oni how you got here."
    elif Chr == "Mystique":
            if Trigger == "blow":
                call M_BJAfter from _call_M_BJAfter
            elif Trigger == "hand":  
                call M_HJAfter from _call_M_HJAfter  
            elif Trigger == "titjob":
                call M_TJAfter from _call_M_TJAfter
            elif Trigger == "kissing":
                call M_Kiss_After from _call_M_Kiss_After
            elif Trigger == "fondle breasts":
                call M_FB_After from _call_M_FB_After
            elif Trigger == "suck breasts":
                call M_SB_After from _call_M_SB_After
            elif Trigger == "fondle thighs":
                call M_FT_After from _call_M_FT_After
            elif Trigger == "fondle pussy":
                call M_FP_After from _call_M_FP_After
            elif Trigger == "lick pussy":
                call M_LP_After from _call_M_LP_After
            elif Trigger == "fondle ass":
                call M_FA_After from _call_M_FA_After
            elif Trigger == "insert ass":
                call M_IA_After from _call_M_IA_After
            elif Trigger == "lick ass":
                call M_LA_After from _call_M_LA_After
            elif Trigger == "sex":
                call M_SexAfter from _call_M_SexAfter
            elif Trigger == "hotdog":
                call M_HotdogAfter from _call_M_HotdogAfter
            elif Trigger == "anal":
                call M_AnalAfter from _call_M_AnalAfter
            elif Trigger == "dildo pussy":
                call M_DP_After from _call_M_DP_After
            elif Trigger == "dildo anal":
                call M_DA_After from _call_M_DA_After
            elif Trigger == "strip":
                call M_Strip_End from _call_M_Strip_End
            else:
                "That's odd, tell Oni how you got here."
    #End Kitty
    return
# End CloseOut  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start Sex_Over  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Sex_Over(Clothes=1,Girls=0):
        #this routine plays out at the end of any sex menu session
        #it cleans them up and puts their clothes on, only returning a line of dialog if they were undressed
        $ Line = 0
        if R_Loc == bg_current:
                # if Rogue is present
                $ R_OCount = 0    
                call Rogue_Cleanup("after")
                if P_Spunk:
                    ch_r "Let me take care of that for you. . ."
                    call R_CleanCock                    
        if K_Loc == bg_current:
                # if Kitty is present
                $ K_OCount = 0    
                call Kitty_Cleanup("after")
                if P_Spunk:
                    ch_k "You've got a little something. . ."
                    ch_k "just let me get that."
                    call K_CleanCock
        if E_Loc == bg_current:
                # if Emma is present
                $ E_OCount = 0    
                call Emma_Cleanup("after") 
                if P_Spunk:
                    ch_e "[E_Petname], let's get you presentable. . ."
                    call E_CleanCock
        if newgirl["Laura"].Loc == bg_current:
                # if Laura is present
                $ newgirl["Laura"].OCount = 0    
                call Laura_Cleanup("after") 
                if P_Spunk:
                    ch_l "[newgirl[Laura].Petname], you've got a little something. . ."
                    call Laura_CleanCock
                    
        call AllReset("all") #resets all sex positions.       
        
        if Clothes:   
                #if asked to put their clothes back on. 
                if R_Loc == bg_current:
                        # if Rogue is present
                        call RogueOutfit(Changed=1)
                        if _return:
                                $ Line = "Rogue"
                                $ Girls += 1
                if K_Loc == bg_current:
                        # if Kitty is present
                        call KittyOutfit(Changed=1)
                        if _return:
                                if Line:
                                    $ Line = Line + " and Kitty"
                                else:
                                    $ Line = "Kitty"
                                $ Girls += 1
                if E_Loc == bg_current:
                        # if Emma is present
                        call EmmaOutfit(Changed=1) 
                        if _return:
                                if Line:
                                    $ Line = Line + " and Emma"
                                else:
                                    $ Line = "Emma"  
                                $ Girls += 1   
                if newgirl["Laura"].Loc == bg_current:
                        # if Laura is present
                        call LauraOutfit(Changed=1) 
                        if _return:
                                if Line:
                                    $ Line = Line + " and Laura"
                                else:
                                    $ Line = "Laura"  
                                $ Girls += 1   
                if Girls > 1:
                    "[Line] throw their clothes back on."
                elif Girls:
                    "[Line] throws her clothes back on."
        call Get_Dressed
        call Checkout(1)
        return



#Character Specific stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
    
    
# Rogue emotion editor ///////////////////////////////////////////////////////////////////////////////////////////////
label RogueEmotionEditor(CountStore = "normal"):
    menu:
        "Normal":
            $ R_Emote = "normal"
            call RogueFace from _call_RogueFace_279
        "Angry":
            $ R_Emote = "angry"
            call RogueFace from _call_RogueFace_280
        "Smiling":
            $ R_Emote = "smile"
            call RogueFace from _call_RogueFace_281
        "Sexy":
            $ R_Emote = "sexy"
            call RogueFace from _call_RogueFace_282
        "Suprised":
            $ R_Emote = "surprised"
            call RogueFace from _call_RogueFace_283
        "Bemused":
            $ R_Emote = "bemused"
            call RogueFace from _call_RogueFace_284
        "Manic":
            $ R_Emote = "manic"
            call RogueFace from _call_RogueFace_285
        "Sad":
            $ R_Emote = "sad"
            call RogueFace from _call_RogueFace_286
        "Sucking":
            $ R_Emote = "sucking"
            call RogueFace from _call_RogueFace_287
        "kiss":
            $ R_Emote = "kiss"
            call RogueFace from _call_RogueFace_288
        "Tongue":
            $ R_Emote = "tongue"
            call RogueFace from _call_RogueFace_289
        "confused":
            $ R_Emote = "confused"
            call RogueFace from _call_RogueFace_290
        "Closed":
            $ R_Emote = "closed"
            call RogueFace from _call_RogueFace_291
        "Down":
            $ R_Emote = "down"
            call RogueFace from _call_RogueFace_292
        "Toggle Squint eyes":
            if R_Eyes == "squint":
                $ R_Eyes = CountStore
            else:
                $ CountStore = R_Eyes
                $ R_Eyes = "squint"
        "Toggle grimace":
            if R_Mouth == "grimace":
                $ R_Mouth = CountStore
            else:
                $ CountStore = R_Mouth
                $ R_Mouth = "grimace"
        "Blush":
            if R_Blush == 2:
                $ R_Blush = 1
            elif R_Blush:
                $ R_Blush = 0
            else:
                $ R_Blush = 2  
        "Exit.":
            return
    jump RogueEmotionEditor
return


                

# Rogue's Wardrobe //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label RogueWardrobe:

    menu:      
        "View":
            while True:
                menu:
                    "Default":
                        call R_Pos_Reset from _call_R_Pos_Reset_2
                    "Face":
                        call R_Kissing_Launch(0) from _call_R_Kissing_Launch_1
                    "Body":
                        call R_Pussy_Launch(0) from _call_R_Pussy_Launch
                    "Doggy":
                        if not renpy.showing("Rogue_Doggy"):
                            call Rogue_Doggy_Launch from _call_Rogue_Doggy_Launch
                        else:
                            call Rogue_Doggy_Reset from _call_Rogue_Doggy_Reset
                    "Back":
                        jump RogueWardrobe 
        # Outfits
        "Green outfit":
            $ R_Outfit = "evo_green"
            call RogueOutfit from _call_RogueOutfit_42
        "Pink outfit":
            $ R_Outfit = "evo_pink"
            call RogueOutfit from _call_RogueOutfit_43
        "Nude":
            $ R_Outfit = "nude"
            call RogueOutfit from _call_RogueOutfit_44
        "Over":              
            while True:
                menu:
                    # Overshirts    
                    "Remove [R_Over]" if R_Over:
                        $ R_Over = 0
                    "Add mesh top":
                        $ R_Over = "mesh top"
                        $ R_Neck = "spiked collar"
                        $ R_Arms = "gloved"
                        if R_Chest == "buttoned tank":
                            $ R_Chest = "tank"     
                    "Add pink top":
                        $ R_Over = "pink top"  
                        $ R_Arms = "gloved"
                    "Add red top":
                        $ R_Over = "red top"  
                        $ R_Arms = "gloved"
                    "Add nighty":
                        $ R_Over = "nighty"   
                        $ R_Arms = 0
                    "Add towel":
                        $ R_Over = "towel"   
                        $ R_Arms = 0
                    "Back":
                        jump RogueWardrobe                
        "Tops":            
            while True:
                menu:
                    # Tops    
                    "Remove [R_Chest]" if R_Chest:
                        $ R_Chest = 0
                    "Add tank top":
                        $ R_Chest = "tank"
                    "Add short tank top":
                        $ R_Chest = "tank short"
                    "Add short slut tank top":
                        $ R_Chest = "slut tank short"
                    "Add sports bra":
                        $ R_Chest = "sports bra"
                    "Add buttoned tank top" if R_Over != "mesh top":
                        $ R_Chest = "buttoned tank"
                    "Add lace bra":
                        $ R_Chest = "lace bra"
                    "Add bra":
                        $ R_Chest = "bra"                            
                    "Toggle Piercings":
                        if R_Pierce == "ring":
                            $ R_Pierce = "barbell"
                        elif R_Pierce == "barbell":
                            $ R_Pierce = 0
                        else:
                            $ R_Pierce = "ring"
                    "Back":
                        jump RogueWardrobe    
    #                "Toggle Top lift" if R_Chest:
    #                    if R_Uptop:
    #                        $ R_Uptop = 0
    #                    else:
    #                        $ R_Uptop = 1           
        
        "Legs":            
            while True:
                menu:
                    # Legs   
                    "Remove legs" if R_Legs:     
                        $ R_Legs = 0
                    "Add Skirt":  
                        $ R_Legs = "skirt"
                        $ R_Upskirt = 0
                    "Add pants":
                        $ R_Legs = "pants"
                        $ R_Hose = 0
                    "Toggle upskirt":
                        if R_Upskirt:
                            $ R_Upskirt = 0
                        else:
                            $ R_Upskirt = 1
                    "Back":
                        jump RogueWardrobe    
        
        "Underwear":            
            while True:
                menu:
                    # Underwear
                    "Hose":
                        menu:
                            "Add hose":     
                                $ R_Hose = "stockings"  
                            "Add garter":     
                                $ R_Hose = "garterbelt"  
                            "Add stockings and garter":     
                                $ R_Hose = "stockings and garterbelt"  
                            "Add pantyhose":     
                                $ R_Hose = "pantyhose"   
                            "Add tights":     
                                $ R_Hose = "tights"   
                            "Add ripped hose":     
                                $ R_Hose = "ripped pantyhose"   
                            "Add ripped tights":     
                                $ R_Hose = "ripped tights"   
                            "Add tights":     
                                $ R_Hose = "tights"  
                            "Add fishnet":
                                $ R_Hose = "fishnet"  
                            "Remove hose" if R_Hose:     
                                $ R_Hose = 0  
                    "Remove panties" if R_Panties:     
                        $ R_Panties = 0     
                    "Add black panties":
                        $ R_Panties = "black panties"
                    "Add shorts":
                        $ R_Legs = "shorts"
                    "Add green panties":
                        $ R_Panties = "green panties"
                    "Add purple bikini panties":
                        $ R_Panties = "purple bikini panties"  
                    "Add lace panties":
                        $ R_Panties = "lace panties"    
                    "pull down-up panties":
                        if R_PantiesDown:
                            $ R_PantiesDown = 0
                        else:
                            $ R_PantiesDown = 1
                    "Back":
                        jump RogueWardrobe    
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call RogueEmotionEditor from _call_RogueEmotionEditor
                    "Toggle Arms":
                        if Rogue_Arms == 1:
                            $ Rogue_Arms = 2
                        else:
                            $ Rogue_Arms = 1
                    "Toggle Wetness":
                        if not R_Wet:
                            $ R_Wet = 1
                        elif R_Wet == 1:
                            $ R_Wet = 2
                        else:
                            $ R_Wet  = 0
                    "Toggle wet look":
                        if not R_Water:
                            $ R_Water = 1
                        elif R_Water == 1:
                            $ R_Water = 3
                        else:
                            $ R_Water  = 0
                    "Toggle pubes":
                        if not R_Pubes:
                            $ R_Pubes = 1
                        else:
                            $ R_Pubes = 0
                    "Toggle held":
                        if not R_Held:
                            $ R_Held  = "phone"
                        elif R_Held == "phone":
                            $ R_Held  = "dildo"
                        elif R_Held == "dildo":
                            $ R_Held  = "vibrator"
                        elif R_Held == "vibrator":
                            $ R_Held  = "panties"
                        else:
                            $ R_Held  = 0    
                    "Add Gloves" if not R_Arms:
                        $ R_Arms = "gloved"
                    "Remove Gloves" if R_Arms:
                        $ R_Arms = 0
                    "Back":
                        jump RogueWardrobe               
        "Set Custom Outfit #1.":
            $ R_Custom[1] = R_Arms  
            $ R_Custom[2] = R_Legs 
            $ R_Custom[3] = R_Over
            $ R_Custom[4] = R_Neck
            $ R_Custom[5] = R_Chest 
            $ R_Custom[13] = R_BodySuit
            $ R_Custom[14] = R_Headband
            $ R_Custom[15] = R_Accessory
            $ R_Custom[6] = R_Panties
            $ R_Custom[7] = R_Boots
            $ R_Custom[8] = R_Hair
            $ R_Custom[9] = R_Hose
            $ R_Custom[0] = 1

        "Wear Custom Outfit #[R_Custom[0]]." if R_Custom[0]:
            $ Line = R_Outfit
            $ R_Outfit = "custom1"
            call RogueOutfit from _call_RogueOutfit_45
            $ R_Outfit = Line
        "Nothing":
            return
    jump RogueWardrobe
return

# Rogue stathacks //////////////////////
label RogueStats:    
    menu:
        "My Love is %(R_Love)d, Inhibition is %(R_Inbt)d, my Obedience is %(R_Obed)d, my Lust is %(R_Lust)d, my Addiction is %(R_Addict)d, my addiction rate is %(R_Addictionrate)d, and I've been kissed %(R_Kissed)d times."
        "Print actions":
            "[R_RecentActions]"
        "Raise Love":
            $ R_Love += 100
        "Lower Love":
            $ R_Love -= 100
        "Raise Obedience":
            $ R_Obed += 100
        "Lower Obedience":
            $ R_Obed -= 100
        "Raise Inhibitions":
            $ R_Inbt += 100
        "Lower Inhibitions":
            $ R_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ R_Love += 10
                    "Lower Love":
                        $ R_Love -= 10
                    "Raise Obedience":
                        $ R_Obed += 10
                    "Lower Obedience":
                        $ R_Obed -= 10
                    "Raise Inhibitions":
                        $ R_Inbt += 10
                    "Lower Inhibitions":
                        $ R_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ R_Lust += 10
                "Lower Lust":
                    $ R_Lust -= 10
                "Raise Addiction":
                    $ R_Addict += 10
                "Lower Addiction":
                    $ R_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call RogueWardrobe from _call_RogueWardrobe
            
        "Return":
            call Checkout from _call_Checkout_47
            return
    jump RogueStats
    

# Kitty emotion editor ///////////////////
label KittyEmotionEditor(CountStore = "normal"):
    menu:
        "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
            menu:
                "Normal":
                    $ K_Emote = "normal"
                    call KittyFace from _call_KittyFace_269
                "Angry":
                    $ K_Emote = "angry"
                    call KittyFace from _call_KittyFace_270
                "Smiling":
                    $ K_Emote = "smile"
                    call KittyFace from _call_KittyFace_271
                "Sexy":
                    $ K_Emote = "sexy"
                    call KittyFace from _call_KittyFace_272
                "Suprised":
                    $ K_Emote = "surprised"
                    call KittyFace from _call_KittyFace_273
                "Bemused":
                    $ K_Emote = "bemused"
                    call KittyFace from _call_KittyFace_274
                "Manic":
                    $ K_Emote = "manic"
                    call KittyFace from _call_KittyFace_275
                    
        "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
            menu:
                "Sad":
                    $ K_Emote = "sad"
                    call KittyFace from _call_KittyFace_276
                "Sucking":
                    $ K_Emote = "sucking"
                    call KittyFace from _call_KittyFace_277
                "kiss":
                    $ K_Emote = "kiss"
                    call KittyFace from _call_KittyFace_278
                "Tongue":
                    $ K_Emote = "tongue"
                    call KittyFace from _call_KittyFace_279
                "confused":
                    $ K_Emote = "confused"
                    call KittyFace from _call_KittyFace_280
                "Closed":
                    $ K_Emote = "closed"
                    call KittyFace from _call_KittyFace_281
                "Down":
                    $ K_Emote = "down"
                    call KittyFace from _call_KittyFace_282
                    
        "Emotions3: Sadside Startled Perplexed Sly":  
            menu:
                "Sadside":
                    $ K_Emote = "sadside"
                    call KittyFace from _call_KittyFace_283
                "Startled":
                    $ K_Emote = "startled"
                    call KittyFace from _call_KittyFace_284
                "Perplexed":
                    $ K_Emote = "perplexed"
                    call KittyFace from _call_KittyFace_285
                "Sly":
                    $ K_Emote = "sly"
                    call KittyFace from _call_KittyFace_286
        "Toggle Mouth Spunk":
            if "mouth" in K_Spunk:
                $ K_Spunk.remove("mouth")
            else:
                $ K_Spunk.append("mouth")
                
        "Toggle Facial Spunk":
            if "facial" in K_Spunk and "hair" not in K_Spunk:
                $ K_Spunk.append("hair")
            elif "facial" in K_Spunk:
                $ K_Spunk.remove("facial")                
                $ K_Spunk.remove("hair")
            else:
                $ K_Spunk.append("facial")
            
        "Blush":
            if K_Blush == 2:
                $ K_Blush = 1
            elif K_Blush:
                $ K_Blush = 0
            else:
                $ K_Blush = 2  
        "Exit.":
            return
    jump KittyEmotionEditor
return

# Kitty's Wardrobe ///////////////////
label KittyWardrobe:

    menu:        
        "Kitty's custom outfit is [K_Custom].[K_Arms]"        
        # Outfits
        "Toggle Kitty":
            if renpy.showing("Kitty_Sprite"):
                hide Kitty_Sprite  
            else:
                call Display_Kitty from _call_Display_Kitty_5
        "Outfits":              
            while True:
                menu:
                    "[K_Outfit]"
                    # Outfits   
                    "Pink outfit" if K_Outfit != "pink outfit":
                        $ K_Outfit = "pink outfit"
                    "Red outfit" if K_Outfit != "red outfit":
                        $ K_Outfit = "red outfit"
                    "Nude" if K_Outfit != "nude":
                        $ K_Outfit = "nude"
                    "Back":
                        jump KittyWardrobe 
                call KittyOutfit from _call_KittyOutfit_24
        "Tops":              
            while True:
                menu:
                    "[K_Over]"
                    # Tops       
                    "Remove pink top" if K_Over == "pink top":
                        $ K_Over = 0
                    "Add pink top" if K_Over != "pink top":
                        $ K_Over = "pink top"  
                    "Remove red shirt" if K_Over == "red shirt": 
                        $ K_Over = 0
                    "Add red shirt" if K_Over != "red shirt":
                        $ K_Over = "red shirt"
                    "Remove violet shirt scarf" if K_Over == "violet shirt scarf": 
                        $ K_Over = 0
                    "Add violet shirt scarf" if K_Over != "violet shirt scarf":
                        $ K_Over = "violet shirt scarf"
                    "Remove violet shirt scarfless" if K_Over == "violet shirt scarfless": 
                        $ K_Over = 0
                    "Add violet shirt scarfless" if K_Over != "violet shirt scarfless":
                        $ K_Over = "violet shirt scarfless"
                    "Remove towel" if K_Over == "towel": 
                        $ K_Over = 0
                    "Add towel" if K_Over != "towel":
                        $ K_Over = "towel"
                    "Back":
                        jump KittyWardrobe   
        "Bras":              
            while True:
                menu:
                    "[K_Chest]"
                    # Bras   
                    "Remove cami" if K_Chest == "cami":
                        $ K_Chest = 0
                    "Add cami" if K_Chest != "cami":
                        $ K_Chest = "cami"
                    "Remove bra" if K_Chest == "bra":
                        $ K_Chest = 0
                    "Add bra" if K_Chest != "bra":
                        $ K_Chest = "bra"
                    "Remove lace bra" if K_Chest == "lace bra":
                        $ K_Chest = 0
                    "Add lace bra" if K_Chest != "lace bra":
                        $ K_Chest = "lace bra"
                    "Remove sports bra" if K_Chest == "sports bra":
                        $ K_Chest = 0
                    "Add sports bra" if K_Chest != "sports bra":
                        $ K_Chest = "sports bra"            
                    "Back":
                        jump KittyWardrobe                     
        "Legs":              
            while True:
                menu:
                    "[K_Legs]"
                    # Legs             
                    "Remove capris pants" if K_Legs == "capris":
                        $ K_Legs = 0
                    "Add capris pants" if K_Legs != "capris":
                        $ K_Legs = "capris"
                    "Remove black jeans" if K_Legs == "black jeans":
                        $ K_Legs = 0
                    "Add black jeans" if K_Legs != "black jeans":
                        $ K_Legs = "black jeans"
                    "Remove black blue pants" if K_Legs == "black blue pants":
                        $ K_Legs = 0
                    "Add black blue pants" if K_Legs != "black blue pants":
                        $ K_Legs = "black blue pants"
                    "Remove Yoga Pants" if K_Legs == "yoga pants":
                        $ K_Legs = 0
                    "Add Yoga Pants" if K_Legs != "yoga pants":
                        $ K_Legs = "yoga pants"
                    "Remove shorts" if K_Legs == "shorts":
                        $ K_Legs = 0
                    "Add shorts" if K_Legs != "shorts":
                        $ K_Legs = "shorts"
                    "Back":
                        jump KittyWardrobe   
        "Underwear":              
            while True:
                menu:
                    "[K_Panties]"
                    # Underwear                            
                    "Remove green panties" if K_Panties == "green panties":
                        $ K_Panties = 0
                    "Add green panties" if K_Panties != "green panties":
                        $ K_Panties = "green panties"        
                    "Remove lace panties" if K_Panties == "lace panties":
                        $ K_Panties = 0
                    "Add lace panties" if K_Panties != "lace panties":
                        $ K_Panties = "lace panties"
                    "Toggle panties down":
                        $ K_PantiesDown = 1 if not K_PantiesDown else 0   
                        "[K_PantiesDown]"
                    "Back":
                        jump KittyWardrobe 
        "Misc":
            while True:
                menu: 
                    "Emotions":
                        call KittyEmotionEditor from _call_KittyEmotionEditor
                    "Toggle Arms":
                        $ K_Arms = 0 if K_Arms == 1 else 1
                    "Toggle pubes":
                        $ K_Pubes = 1 if not K_Pubes else 0 
                    "Toggle Piercings":
                        if K_Pierce == "ring":
                            $ K_Pierce = "barbell"
                        elif K_Pierce == "barbell":
                            $ K_Pierce = 0
                        else:
                            $ K_Pierce = "ring"
                    "Toggle wetness":
                        if not K_Wet:                            
                            $ K_Wet = 1
                        elif K_Wet == 1:
                            $ K_Wet = 2
                        else:
                            $ K_Wet = 0
                    "Toggle wet look":
                        $ K_Water = 1 if not K_Water else 0 
                    "Toggle hair":
                        $ K_Hair = "evo" if K_Hair == "long" else "long"   
                    "Back":
                        jump KittyWardrobe  
                        
        "View":
            menu:
                "Breasts":
                    call K_Breasts_Launch from _call_K_Breasts_Launch_4
                "Pussy":
                    call K_Pussy_Launch from _call_K_Pussy_Launch_12
                "Default":
                    call K_Pos_Reset from _call_K_Pos_Reset_40
                
        "Set Custom Outfit #1.":
            $ K_Custom[0] = 1
            $ K_Custom[1] = K_Gloves
            $ K_Custom[2] = K_Legs
            $ K_Custom[3] = K_Over
            $ K_Custom[4] = K_Under
            $ K_Custom[5] = K_Chest
            $ K_Custom[6] = K_Panties 
            $ K_Custom[7] = K_Pubes 
            $ K_Custom[8] = K_Hair
            $ K_Custom[9] = K_Hose
        "Wear Custom Outfit #[K_Custom[0]]." if K_Custom[0] == 1:
            $ K_Outfit = "custom1"
            call KittyOutfit from _call_KittyOutfit_25
        "Nothing":
            return
    jump KittyWardrobe
return
     
# Kitty stathacks //////////////////////
label KittyStats:    
    menu:
        "My Love is %(K_Love)d, Inhibition is %(K_Inbt)d, my Obedience is %(K_Obed)d, my Lust is %(K_Lust)d, my Addiction is %(K_Addict)d, my addiction rate is %(K_Addictionrate)d, and I've been kissed %(K_Kissed)d times."
        "Print actions":
            "[K_RecentActions]"
        "Raise Love":
            $ K_Love += 100
        "Lower Love":
            $ K_Love -= 100
        "Raise Obedience":
            $ K_Obed += 100
        "Lower Obedience":
            $ K_Obed -= 100
        "Raise Inhibitions":
            $ K_Inbt += 100
        "Lower Inhibitions":
            $ K_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ K_Love += 10
                    "Lower Love":
                        $ K_Love -= 10
                    "Raise Obedience":
                        $ K_Obed += 10
                    "Lower Obedience":
                        $ K_Obed -= 10
                    "Raise Inhibitions":
                        $ K_Inbt += 10
                    "Lower Inhibitions":
                        $ K_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ K_Lust += 10
                "Lower Lust":
                    $ K_Lust -= 10
                "Raise Addiction":
                    $ K_Addict += 10
                "Lower Addiction":
                    $ K_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call KittyWardrobe from _call_KittyWardrobe
            
        "Return":
            call Checkout from _call_Checkout_48
            return
    jump KittyStats
    
# Emma stathacks //////////////////////
label EmmaStats:    
    menu:
        "My Love is %(E_Love)d, Inhibition is %(E_Inbt)d, my Obedience is %(E_Obed)d, my Lust is %(E_Lust)d, my Addiction is %(E_Addict)d, my addiction rate is %(E_Addictionrate)d, and I've been kissed %(E_Kissed)d times."
        "Print actions":
            "[E_RecentActions]"
        "Raise Love":
            $ E_Love += 100
        "Lower Love":
            $ E_Love -= 100
        "Raise Obedience":
            $ E_Obed += 100
        "Lower Obedience":
            $ E_Obed -= 100
        "Raise Inhibitions":
            $ E_Inbt += 100
        "Lower Inhibitions":
            $ E_Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ E_Love += 10
                    "Lower Love":
                        $ E_Love -= 10
                    "Raise Obedience":
                        $ E_Obed += 10
                    "Lower Obedience":
                        $ E_Obed -= 10
                    "Raise Inhibitions":
                        $ E_Inbt += 10
                    "Lower Inhibitions":
                        $ E_Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ E_Lust += 10
                "Lower Lust":
                    $ E_Lust -= 10
                "Raise Addiction":
                    $ E_Addict += 10
                "Lower Addiction":
                    $ E_Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            call EmmaWardrobe from _call_EmmaWardrobe
            
        "Return":
            call Checkout from _call_Checkout_49
            return
    jump EmmaStats

label NewGirlStats(Girl = "Mystique"):    
    $ GirlLove = newgirl[Girl].Love
    $ GirlInbt = newgirl[Girl].Inbt
    $ GirlObed = newgirl[Girl].Obed
    $ GirlLust = newgirl[Girl].Lust
    $ GirlAddict = newgirl[Girl].Addict
    $ GirlAddictionrate = newgirl[Girl].Addictionrate
    $ GirlKissed = newgirl[Girl].Kissed
    $ GirlRecentActions = newgirl[Girl].RecentActions
    menu:
        "My Love is [GirlLove], Inhibition is [GirlInbt], my Obedience is [GirlObed], my Lust is [GirlLust], my Addiction is [GirlAddict], my addiction rate is [GirlAddictionrate], and I've been kissed [GirlKissed] times."
        "Print actions":
            "[GirlRecentActions]"
        "Raise Love":
            $ newgirl[Girl].Love += 100
        "Lower Love":
            $ newgirl[Girl].Love -= 100
        "Raise Obedience":
            $ newgirl[Girl].Obed += 100
        "Lower Obedience":
            $ newgirl[Girl].Obed -= 100
        "Raise Inhibitions":
            $ newgirl[Girl].Inbt += 100
        "Lower Inhibitions":
            $ newgirl[Girl].Inbt -= 100
        "Taboo toggle":
            $ Taboo = 40 if Taboo != 40 else 0
            "[Taboo]"
        "Small":
            $ Count = 1
            while Count:
                menu:
                    "Raise Love":
                        $ newgirl[Girl].Love += 10
                    "Lower Love":
                        $ newgirl[Girl].Love -= 10
                    "Raise Obedience":
                        $ newgirl[Girl].Obed += 10
                    "Lower Obedience":
                        $ newgirl[Girl].Obed -= 10
                    "Raise Inhibitions":
                        $ newgirl[Girl].Inbt += 10
                    "Lower Inhibitions":
                        $ newgirl[Girl].Inbt -= 10
                    "Back":
                        $ Count = 0                    
        "Other":
            menu:        
                "Raise Lust":
                    $ newgirl[Girl].Lust += 10
                "Lower Lust":
                    $ newgirl[Girl].Lust -= 10
                "Raise Addiction":
                    $ newgirl[Girl].Addict += 10
                "Lower Addiction":
                    $ newgirl[Girl].Addict -= 10
                "Back":
                    pass
        "Wardrobe":
            if Girl == "Mystique":
                call MystiqueWardrobe
            elif Girl == "Laura":
                call LauraWardrobe
            else:
                "[Girl] has no wardrobe defined?"
            
        "Return":
            call Checkout
            return
    call NewGirlStats(Girl)
    
label Failsafe: 
    #This routine is meant to set any variables that aren't already set.     
    $ TestVariableBeta = 10 if "TestVariableBeta" not in globals().keys() else TestVariableBeta 
    $ SaveVersion = 976 #keep updated to latest version
    $ Day = 1 if "Day" not in globals().keys() else Day 
    $ Cheat = 0 if "Cheat" not in globals().keys() else Cheat
    $ Time_Options = ["Morning", "Midday", "Evening", "Night"]
    $ Time_Count = 2 if "Time_Count" not in globals().keys() else Time_Count
    $ Current_Time = Time_Options[(Time_Count)]     
    $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    $ Weekday = 6 if "Weekday" not in globals().keys() else Weekday
    $ DayofWeek = Week[Weekday]
    $ bg_current = "bg study" if "bg_current" not in globals().keys() else bg_current
    $ Party = [] if "Party" not in globals().keys() else Party
    $ Taboo = 0 if "Taboo" not in globals().keys() else Taboo
    $ Rules = [] if "Rules" not in globals().keys() else Rules
    $ R_Rules = 1 if "R_Rules" not in globals().keys() else R_Rules
    $ K_Rules = 1 if "K_Rules" not in globals().keys() else K_Rules
    $ E_Rules = 1 if "E_Rules" not in globals().keys() else E_Rules
    $ Line = 0 if "Line" not in globals().keys() else Line 
    $ Situation = 0 if "Situation" not in globals().keys() else Situation                #Whether Auto/Shift
    $ MultiAction = 1 if "MultiAction" not in globals().keys() else MultiAction              #0 if the action cannot continue, 1 if it can
    $ Trigger = 0 if "Trigger" not in globals().keys() else Trigger                 #Mainhand
    $ Trigger2 = 0 if "Trigger2" not in globals().keys() else Trigger2                #Offhand
    $ Trigger3 = 0 if "Trigger3" not in globals().keys() else Trigger3                #Girl's offhand    
    $ Trigger4 = 0 if "Trigger4" not in globals().keys() else Trigger4                #this is the 4th sexual act performed by the second girl 
    $ Trigger5 = 0 if "Trigger5" not in globals().keys() else Trigger5                #this is the 5th sexual act performed by the second girl if masturbating
    $ Present = [] if "Present" not in globals().keys() else Present
    $ Adjacent = 0 if "Adjacent" not in globals().keys() else Adjacent                #this is the girl you're sitting next to in class
    $ Partner = 0 if "Partner" not in globals().keys() else Partner                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
    $ Events = [] if "Events" not in globals().keys() else Events
    $ Tempmod = 0 if "Tempmod" not in globals().keys() else Tempmod
    $ Approval = 0  if "Approval" not in globals().keys() else Approval               #for approval checks
    $ Count = 0 if "Count" not in globals().keys() else Count                   #For within an event
    $ Count2 = 0 if "Count2" not in globals().keys() else Count2                  #For between several events
    $ Round = 100 if "Round" not in globals().keys() else Round   
    $ Stealth = 0 if "Stealth" not in globals().keys() else Stealth                #How careful you're being
    $ Cnt = 0 if "Cnt" not in globals().keys() else Cnt                     #a mini Count variable for discrete operations
    $ Speed = 0 if "Speed" not in globals().keys() else Speed
    $ CountStore = 0 if "CountStore" not in globals().keys() else CountStore              #Stores values for after an event ends
    $ Achievements = [] if "Achievements" not in globals().keys() else Achievements
    $ Options = [] if "Options" not in globals().keys() else Options
    $ Vibration = 0 if "Vibration" not in globals().keys() else Vibration
    $ UI_Tool = 0 if "UI_Tool" not in globals().keys() else UI_Tool
    $ Ch_Focus = "Rogue" if "Ch_Focus" not in globals().keys() else Ch_Focus
    $ TravelMode = 0 if "TravelMode" not in globals().keys() else TravelMode           #used for wandering around, if 0, you use the worldmap
    $ StageRight = 900            #these are values for location points on the screen
    $ StageCenter = 715
    $ StageLeft = 500
    $ StageFarLeft = 150
#Player Stats    
    $ Playername = "Zero" if "Playername" not in globals().keys() else Playername
    $ P_Male = 1 if "P_Male" not in globals().keys() else P_Male
    $ R_Petname = "sugar" if "R_Petname" not in globals().keys() else R_Petname       #What Rogue calls the player
    $ R_Petnames = ["sugar"] if "R_Petnames" not in globals().keys() else R_Petnames
    $ R_Pet = "Rogue" if "R_Pet" not in globals().keys() else R_Pet           #What you call Rogue
    $ R_Pets = ["Rogue"] if "R_Pets" not in globals().keys() else R_Pets
    $ K_Petname = "sweetie" if "K_Petname" not in globals().keys() else K_Petname       #What Rogue calls the player
    $ K_Petnames = ["sweetie"] if "K_Petnames" not in globals().keys() else K_Petnames
    $ K_Pet = "Kitty" if "K_Pet" not in globals().keys() else K_Pet           #What you call Rogue
    $ K_Pets = ["Kitty"] if "K_Pets" not in globals().keys() else K_Pets
    $ P_Semen = 2 if "P_Semen" not in globals().keys() else P_Semen
    $ P_Semen_Max = 3 if "P_Semen_Max" not in globals().keys() else P_Semen_Max
    $ P_Focus = 0 if "P_Focus" not in globals().keys() else P_Focus
    $ P_FocusX = 0 if "P_FocusX" not in globals().keys() else P_FocusX
    $ P_XP = 0 if "P_XP" not in globals().keys() else P_XP
    $ P_StatPoints = 0 if "P_StatPoints" not in globals().keys() else P_StatPoints    
    $ P_XPgoal = 100 if "P_XPgoal" not in globals().keys() else P_XPgoal
    $ P_Lvl = 1 if "P_Lvl" not in globals().keys() else P_Lvl
    $ P_Traits = [] if "P_Traits" not in globals().keys() else P_Traits
    $ P_Rep = 600 if "P_Rep" not in globals().keys() else P_Rep
    $ P_RecentActions = [] if "P_RecentActions" not in globals().keys() else P_RecentActions
    $ P_DailyActions = [] if "P_DailyActions" not in globals().keys() else P_DailyActions
# Player Inventory Variables 
    $ P_Income = 12 if "P_Income" not in globals().keys() else P_Income               #how much you make each day
    $ P_Cash = 20 if "P_Cash" not in globals().keys() else P_Cash
    $ P_Hands = 0 if "P_Hands" not in globals().keys() else P_Hands
    $ P_Inventory = [] if "P_Inventory" not in globals().keys() else P_Inventory
    $ Inventory_Count = 0 if "Inventory_Count" not in globals().keys() else Inventory_Count
    $ Digits = [] if "Digits" not in globals().keys() else Digits
    $ Keys = [] if "Keys" not in globals().keys() else Keys
    $ PunishmentX = 0 if "PunishmentX" not in globals().keys() else PunishmentX
# Player Sprite
    $ P_Sprite = 0 if "P_Sprite" not in globals().keys() else P_Sprite
    $ P_Color = "green" if "P_Color" not in globals().keys() else P_Color
    $ P_Cock = "out" if "P_Cock" not in globals().keys() else P_Cock
    $ P_Spunk = 0 if "P_Spunk" not in globals().keys() else P_Spunk
    $ P_Wet = 0 if "P_Wet" not in globals().keys() else P_Wet
#Rogue Stats   
    $ R_Loc = "bg rogue" if "R_Loc" not in globals().keys() else R_Loc
    $ R_Love = 500 if "R_Love" not in globals().keys() else R_Love
    $ R_Obed = 0 if "R_Obed" not in globals().keys() else R_Obed
    $ R_Inbt = 0 if "R_Inbt" not in globals().keys() else R_Inbt
    $ R_Lust = 10 if "R_Lust" not in globals().keys() else R_Lust
    $ R_LikeKitty = 600 if "R_LikeKitty" not in globals().keys() else R_LikeKitty
    $ R_Addict = 0 if "R_Addict" not in globals().keys() else R_Addict                #how addicted she is
    $ R_Addictionrate = 0 if "R_Addictionrate" not in globals().keys() else R_Addictionrate         #How faster her addiciton rises
    $ R_AddictStore = 0 if "R_AddictStore" not in globals().keys() else R_AddictStore           #stores her base addiction level
    $ R_Resistance = 0 if "R_Resistance" not in globals().keys() else R_Resistance            #how fast her rate falls
    $ R_OCount = 0 if "R_OCount" not in globals().keys() else R_OCount                #Orgasm counter
    $ R_Loose = 0 if "R_Loose" not in globals().keys() else R_Loose
    $ R_Inventory = [] if "R_Inventory" not in globals().keys() else R_Inventory
    $ R_XP = 0 if "R_XP" not in globals().keys() else R_XP
    $ R_ShameLevel = 0 if "R_ShameLevel" not in globals().keys() else R_ShameLevel
    $ R_Cheated = 0 if "R_Cheated" not in globals().keys() else R_Cheated               #number of times you've cheated on her    
    $ R_Break = [0,0] if "R_Break" not in globals().keys() else R_Break                 #minimum time between break-ups/number of total break-ups
    $ R_StatPoints = 0 if "R_StatPoints" not in globals().keys() else R_StatPoints    
    $ R_XPgoal = 100 if "R_XPgoal" not in globals().keys() else R_XPgoal
    $ R_Lvl = 0 if "R_Lvl" not in globals().keys() else R_Lvl
    $ R_Traits = [] if "R_Traits" not in globals().keys() else R_Traits
    $ R_Rep = 800 if "R_Rep" not in globals().keys() else R_Rep
    $ R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0] if "R_OutfitShame" not in globals().keys() else R_OutfitShame
    $ R_Shame = 0 if "R_Shame" not in globals().keys() else R_Shame                 #The amount of shame Rogue generates with her current clothing/action
    $ R_Taboo = 0 if "R_Taboo" not in globals().keys() else R_Taboo                 #The taboo level of the location Rogue is at when not with you
    $ R_Chat = [0,0,0,0,0,0] if "R_Chat" not in globals().keys() else R_Chat
    $ R_Event = [0,0,0,0,0,0,0,0,0,0,0] if "R_Event" not in globals().keys() else R_Event  
    $ R_Todo = [] if "R_Todo" not in globals().keys() else R_Todo
    $ R_PubeC = 0 if "R_PubeC" not in globals().keys() else R_PubeC
  # Sexual Encounters
    $ R_History = [] if "R_History" not in globals().keys() else R_History
    $ R_RecentActions = [] if "R_RecentActions" not in globals().keys() else R_RecentActions
    $ R_DailyActions = [] if "R_DailyActions" not in globals().keys() else R_DailyActions
    $ R_Action = 3 if "R_Action" not in globals().keys() else R_Action
    $ R_MaxAction = 3 if "R_MaxAction" not in globals().keys() else R_MaxAction
    $ R_Caught = 0 if "R_Caught" not in globals().keys() else R_Caught
    $ R_Kissed = 0 if "R_Kissed" not in globals().keys() else R_Kissed              #How many times they've kissed
    $ R_Hand = 0 if "R_Hand" not in globals().keys() else R_Hand
    $ R_Slap = 0 if "R_Slap" not in globals().keys() else R_Slap
    $ R_Spank = 0 if "R_Spank" not in globals().keys() else R_Spank
    $ R_Strip = 0 if "R_Strip" not in globals().keys() else R_Strip
    $ R_Tit = 0 if "R_Tit" not in globals().keys() else R_Tit
    $ R_Sex = 0 if "R_Sex" not in globals().keys() else R_Sex
    $ R_Anal = 0 if "R_Anal" not in globals().keys() else R_Anal
    $ R_Hotdog = 0 if "R_Hotdog" not in globals().keys() else R_Hotdog
    $ R_Mast = 0 if "R_Mast" not in globals().keys() else R_Mast
    $ R_Org = 0 if "R_Org" not in globals().keys() else R_Org
    $ R_FondleB = 0 if "R_FondleB" not in globals().keys() else R_FondleB
    $ R_FondleT = 0 if "R_FondleT" not in globals().keys() else R_FondleT
    $ R_FondleP = 0 if "R_FondleP" not in globals().keys() else R_FondleP
    $ R_FondleA = 0 if "R_FondleA" not in globals().keys() else R_FondleA
    $ R_DildoP = 0 if "R_DildoP" not in globals().keys() else R_DildoP
    $ R_DildoA = 0 if "R_DildoA" not in globals().keys() else R_DildoA
    $ R_Vib = 0 if "R_Vib" not in globals().keys() else R_Vib
    $ R_Vibrator = 0 if "R_Vibrator" not in globals().keys() else R_Vibrator
    $ R_Plug = 0 if "R_Plug" not in globals().keys() else R_Plug
    $ R_Plugged = 0 if "R_Plugged" not in globals().keys() else R_Plugged
    $ R_SuckB = 0 if "R_SuckB" not in globals().keys() else R_SuckB
    $ R_InsertP = 0 if "R_InsertP" not in globals().keys() else R_InsertP
    $ R_InsertA = 0 if "R_InsertA" not in globals().keys() else R_InsertA
    $ R_LickP = 0 if "R_LickP" not in globals().keys() else R_LickP
    $ R_LickA = 0 if "R_LickA" not in globals().keys() else R_LickA
    $ R_Blow = 0 if "R_Blow" not in globals().keys() else R_Blow
    $ R_Swallow = 0 if "R_Swallow" not in globals().keys() else R_Swallow
    $ R_CreamP = 0 if "R_CreamP" not in globals().keys() else R_CreamP
    $ R_CreamA = 0 if "R_CreamA" not in globals().keys() else R_CreamA
    $ R_Les = 0 if "R_Les" not in globals().keys() else R_Les                           #how many times she's done lesbian stuff
    $ R_SexKitty = 0 if "R_SexKitty" not in globals().keys() else R_SexKitty                      #how many times she's had sex involving Kitty
    $ R_SEXP = 0 if "R_SEXP" not in globals().keys() else R_SEXP
    $ R_PlayerFav = 0 if "R_PlayerFav" not in globals().keys() else R_PlayerFav                     #The player's favorite activity with her
    $ R_Favorite = 0 if "R_Favorite" not in globals().keys() else R_Favorite                      #her favorite activity
    $ R_SeenChest = 0 if "R_SeenChest" not in globals().keys() else R_SeenChest
    $ R_SeenPanties = 0 if "R_SeenPanties" not in globals().keys() else R_SeenPanties
    $ R_SeenPussy = 0 if "R_SeenPussy" not in globals().keys() else R_SeenPussy
    $ R_SeenPeen = 0 if "R_SeenPeen" not in globals().keys() else R_SeenPeen                      #How many times she's seen your cock
    $ R_Sleep = 0 if "R_Sleep" not in globals().keys() else R_Sleep 
    $ R_Personality = "normal" if "R_Personality" not in globals().keys() else R_Personality
    $ R_Date = 0 if "R_Date" not in globals().keys() else R_Date 
    $ R_Forced = 0 if "R_Forced" not in globals().keys() else R_Forced                        #This is a toggle for if she's being coerced
    $ R_ForcedCount = 0 if "R_ForcedCount" not in globals().keys() else R_ForcedCount                   #This is a counter for each time she's been coerced lately
#Rogue Sprite Variables
    $ R_Outfit = "evo_green" if "R_Outfit" not in globals().keys() else R_Outfit
    $ R_OutfitDay = "evo_green" if "R_OutfitDay" not in globals().keys() else R_OutfitDay
    $ Rogue_Arms = 1 if "Rogue_Arms" not in globals().keys() else Rogue_Arms
    $ R_Emote = "normal" if "R_Emote" not in globals().keys() else R_Emote
    $ R_Arms = "collargloved" if "R_Arms" not in globals().keys() else R_Arms
    $ R_Legs = "skirt" if "R_Legs" not in globals().keys() else R_Legs
    $ R_Over = "mesh top" if "R_Over" not in globals().keys() else R_Over
    $ R_Under = 0 if "R_Under" not in globals().keys() else R_Under
    $ R_Chest = "tank" if "R_Chest" not in globals().keys() else R_Chest
    $ R_BodySuit = 0 if "R_BodySuit" not in globals().keys() else R_BodySuit
    $ R_Pierce = 0 if "R_Pierce" not in globals().keys() else R_Pierce
    $ R_Panties = "black panties" if "R_Panties" not in globals().keys() else R_Panties
    $ R_Neck = "spiked collar" if "R_Neck" not in globals().keys() else R_Neck
    $ R_Hose = "stockings" if "R_Hose" not in globals().keys() else R_Hose
    $ Temp_R_Hose = 0 if "Temp_R_Hose" not in globals().keys() else Temp_R_Hose
    $ Temp_R_Legs = 0 if "Temp_R_Legs" not in globals().keys() else Temp_R_Legs
    $ R_Mouth = "normal" if "R_Mouth" not in globals().keys() else R_Mouth
    $ R_Brows = "normal" if "R_Brows" not in globals().keys() else R_Brows
    $ R_Eyes = "normal" if "R_Eyes" not in globals().keys() else R_Eyes
    $ R_Hair = "evo" if "R_Hair" not in globals().keys() else R_Hair
    $ R_HairColor = 0 if "R_HairColor" not in globals().keys() else R_HairColor
    $ E_HairColor = 0 if "E_HairColor" not in globals().keys() else E_HairColor
    $ R_Gag = 0 if "R_Gag" not in globals().keys() else R_Gag
    $ R_Gagx = 0 if "R_Gagx" not in globals().keys() else R_Gagx
    $ R_Boots = 0 if "R_Boots" not in globals().keys() else R_Boots
    $ R_Glasses = 0 if "R_Glasses" not in globals().keys() else R_Glasses
    $ R_Headband = 0 if "R_Headband" not in globals().keys() else R_Headband
    $ R_Accessory = 0 if "R_Accessory" not in globals().keys() else R_Accessory
    $ R_Blush = 0 if "R_Blush" not in globals().keys() else R_Blush
    $ R_Spunk = [] if "R_Spunk" not in globals().keys() else R_Spunk
    $ R_Sperm = [] if "R_Sperm" not in globals().keys() else R_Sperm
    $ R_Pubes = 1 if "R_Pubes" not in globals().keys() else R_Pubes
    $ R_Nudes = 1 if "R_Nudes" not in globals().keys() else R_Nudes
    $ R_SelfieOverlay = 0 if "R_SelfieOverlay" not in globals().keys() else R_SelfieOverlay
    $ R_Tan = 0 if "R_Tan" not in globals().keys() else R_Tan
    $ R_LegsUp = 0 if "R_LegsUp" not in globals().keys() else R_LegsUp
    $ R_Wet = 0 if "R_Wet" not in globals().keys() else R_Wet
    $ R_Water = 0 if "R_Water" not in globals().keys() else R_Water
    $ R_Upskirt = 0 if "R_Upskirt" not in globals().keys() else R_Upskirt
    $ R_BodySuitOff = 0 if "R_BodySuitOff" not in globals().keys() else R_BodySuitOff
    $ R_PantiesDown = 0 if "R_PantiesDown" not in globals().keys() else R_PantiesDown
    $ R_Uptop = 0 if "R_Uptop" not in globals().keys() else R_Uptop
    $ R_Held = 0 if "R_Held" not in globals().keys() else R_Held
    $ R_Custom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom" not in globals().keys() else R_Custom
    $ R_Custom2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom2" not in globals().keys() else R_Custom2
    $ R_Custom3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom3" not in globals().keys() else R_Custom3
    $ R_Custom4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom4" not in globals().keys() else R_Custom4
    $ R_Custom5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom5" not in globals().keys() else R_Custom5
    $ R_Custom6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom6" not in globals().keys() else R_Custom6
    $ R_Custom7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] if "R_Custom7" not in globals().keys() else R_Custom7
    $ R_Gym = [0,"gloved","shorts","hoodie",0,"sports bra",0,0,0,0,0,0,0,0,0,0,0] if "R_Gym" not in globals().keys() else R_Gym
    $ R_Sleepwear = [0,0,0,0,"tank","green panties",0,0,0,0,0,0,0] if "R_Sleepwear" not in globals().keys() else R_Sleepwear
    $ R_Schedule = [0,0,0,0,0,0,0,0,4,0] if "R_Schedule" not in globals().keys() else R_Schedule                      #chooses when she wears what
    $ R_SpriteVer = 0 if "R_SpriteVer" not in globals().keys() else R_SpriteVer
    $ RogueLayer = 50 if "RogueLayer" not in globals().keys() else RogueLayer
    $ R_SpriteLoc = StageRight if "R_SpriteLoc" not in globals().keys() else R_SpriteLoc                        #Sets Rogue to $ to the right side  
#Kitty Stats   
    $ K_Loc = "bg kitty" if "K_Loc" not in globals().keys() else K_Loc
    $ K_Love = 400 if "K_Love" not in globals().keys() else K_Love
    $ K_Obed = 100 if "K_Obed" not in globals().keys() else K_Obed
    $ K_Inbt = 0 if "K_Inbt" not in globals().keys() else K_Inbt
    $ K_Lust = 10 if "K_Lust" not in globals().keys() else K_Lust
    $ K_LikeRogue = 700 if "K_LikeRogue" not in globals().keys() else K_LikeRogue
    $ K_Addict = 0 if "K_Addict" not in globals().keys() else K_Addict                #how addicted she is
    $ K_Addictionrate = 0 if "K_Addictionrate" not in globals().keys() else K_Addictionrate         #How faster her addiciton rises
    $ K_AddictStore = 0 if "K_AddictStore" not in globals().keys() else K_AddictStore          #stores her base addiction level
    $ K_Resistance = 0 if "K_Resistance" not in globals().keys() else K_Resistance            #how fast her rate falls
    $ K_OCount = 0 if "K_OCount" not in globals().keys() else K_OCount                #Orgasm counter
    $ K_Loose = 0 if "K_Loose" not in globals().keys() else K_Loose
    $ K_Inventory = [] if "K_Inventory" not in globals().keys() else K_Inventory
    $ K_XP = 0 if "K_XP" not in globals().keys() else K_XP
    $ K_ShameLevel = 0 if "K_ShameLevel" not in globals().keys() else K_ShameLevel
    $ K_Cheated = 0 if "K_Cheated" not in globals().keys() else K_Cheated               #number of times you've cheated on her    
    $ K_Break = [0,0] if "K_Break" not in globals().keys() else K_Break                 #minimum time between break-ups/number of total break-ups
    $ K_StatPoints = 0 if "K_StatPoints" not in globals().keys() else K_StatPoints    
    $ K_XPgoal = 100 if "K_XPgoal" not in globals().keys() else K_XPgoal
    $ K_Lvl = 0 if "K_Lvl" not in globals().keys() else K_Lvl
    $ K_Traits = [] if "K_Traits" not in globals().keys() else K_Traits
    $ K_Rep = 800 if "K_Rep" not in globals().keys() else K_Rep
    $ K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0] if "K_OutfitShame" not in globals().keys() else K_OutfitShame
    $ K_Shame = 0 if "K_Shame" not in globals().keys() else K_Shame                 #The amount of shame Rogue generates with her current clothing/action
    $ K_Taboo = 0 if "K_Taboo" not in globals().keys() else K_Taboo                 #The taboo level of the location Rogue is at when not with you
    $ K_Chat = [0,0,0,0,0,0] if "K_Chat" not in globals().keys() else K_Chat
    $ K_Event = [0,0,0,0,0,0,0,0,0,0,0] if "K_Event" not in globals().keys() else K_Event  
    $ K_Todo = [] if "K_Todo" not in globals().keys() else K_Todo
    $ K_PubeC = 0 if "K_PubeC" not in globals().keys() else K_PubeC
    $ K_Like = "Like, " if "K_Like" not in globals().keys() else K_Like
    $ K_like = ", like, " if "K_like" not in globals().keys() else K_like
  # Sexual Encounters
    $ K_History = [] if "K_History" not in globals().keys() else K_History
    $ K_RecentActions = [] if "K_RecentActions" not in globals().keys() else K_RecentActions
    $ K_DailyActions = [] if "K_DailyActions" not in globals().keys() else K_DailyActions
    $ K_Action = 3 if "K_Action" not in globals().keys() else K_Action
    $ K_MaxAction = 3 if "K_MaxAction" not in globals().keys() else K_MaxAction
    $ K_Caught = 0 if "K_Caught" not in globals().keys() else K_Caught
    $ K_Kissed = 0 if "K_Kissed" not in globals().keys() else K_Kissed              #How many times they've kissed
    $ K_Hand = 0 if "K_Hand" not in globals().keys() else K_Hand
    $ K_Slap = 0 if "K_Slap" not in globals().keys() else K_Slap
    $ K_Spank = 0 if "K_Spank" not in globals().keys() else K_Spank
    $ K_Strip = 0 if "K_Strip" not in globals().keys() else K_Strip
    $ K_Tit = 0 if "K_Tit" not in globals().keys() else K_Tit
    $ K_Sex = 0 if "K_Sex" not in globals().keys() else K_Sex
    $ K_Anal = 0 if "K_Anal" not in globals().keys() else K_Anal
    $ K_Hotdog = 0 if "K_Hotdog" not in globals().keys() else K_Hotdog
    $ K_Mast = 0 if "K_Mast" not in globals().keys() else K_Mast
    $ K_Org = 0 if "K_Org" not in globals().keys() else K_Org
    $ K_FondleB = 0 if "K_FondleB" not in globals().keys() else K_FondleB
    $ K_FondleT = 0 if "K_FondleT" not in globals().keys() else K_FondleT
    $ K_FondleP = 0 if "K_FondleP" not in globals().keys() else K_FondleP
    $ K_FondleA = 0 if "K_FondleA" not in globals().keys() else K_FondleA
    $ K_DildoP = 0 if "K_DildoP" not in globals().keys() else K_DildoP
    $ K_DildoA = 0 if "K_DildoA" not in globals().keys() else K_DildoA
    $ K_Vib = 0 if "K_Vib" not in globals().keys() else K_Vib
    $ K_Vibrator = 0 if "K_Vibrator" not in globals().keys() else K_Vibrator
    $ K_Plug = 0 if "K_Plug" not in globals().keys() else K_Plug
    $ K_Plugged = 0 if "K_Plugged" not in globals().keys() else K_Plugged
    $ K_SuckB = 0 if "K_SuckB" not in globals().keys() else K_SuckB
    $ K_InsertP = 0 if "K_InsertP" not in globals().keys() else K_InsertP
    $ K_InsertA = 0 if "K_InsertA" not in globals().keys() else K_InsertA
    $ K_LickP = 0 if "K_LickP" not in globals().keys() else K_LickP
    $ K_LickA = 0 if "K_LickA" not in globals().keys() else K_LickA
    $ K_Blow = 0 if "K_Blow" not in globals().keys() else K_Blow
    $ K_Swallow = 0 if "K_Swallow" not in globals().keys() else K_Swallow
    $ K_CreamP = 0 if "K_CreamP" not in globals().keys() else K_CreamP
    $ K_CreamA = 0 if "K_CreamA" not in globals().keys() else K_CreamA
    $ K_Les = 0 if "K_Les" not in globals().keys() else K_Les                           #how many times she's done lesbian stuff
    $ K_SexRogue = 0 if "K_SexRogue" not in globals().keys() else K_SexRogue                      #how many times she's had sex involving Rogue
    $ K_SEXP = 0 if "K_SEXP" not in globals().keys() else K_SEXP
    $ K_PlayerFav = 0 if "K_PlayerFav" not in globals().keys() else K_PlayerFav                     #The player's favorite activity with her
    $ K_Favorite = 0 if "K_Favorite" not in globals().keys() else K_Favorite                      #her favorite activity
    $ K_SeenChest = 0 if "K_SeenChest" not in globals().keys() else K_SeenChest
    $ K_SeenPanties = 0 if "K_SeenPanties" not in globals().keys() else K_SeenPanties
    $ K_SeenPussy = 0 if "K_SeenPussy" not in globals().keys() else K_SeenPussy
    $ K_SeenPeen = 0 if "K_SeenPeen" not in globals().keys() else K_SeenPeen                      #How many times she's seen your cock
    $ K_Sleep = 0 if "K_Sleep" not in globals().keys() else K_Sleep 
    $ K_Personality = "normal" if "K_Personality" not in globals().keys() else K_Personality
    $ K_Date = 0 if "K_Date" not in globals().keys() else K_Date 
    $ K_Forced = 0 if "K_Forced" not in globals().keys() else K_Forced                        #This is a toggle for if she's being coerced
    $ K_ForcedCount = 0 if "K_ForcedCount" not in globals().keys() else K_ForcedCount                   #This is a counter for each time she's been coerced lately
#Kitty Sprite Variables
    $ K_Outfit = "pink outfit" if "K_Outfit" not in globals().keys() else K_Outfit
    $ K_OutfitDay = "pink outfit" if "K_OutfitDay" not in globals().keys() else K_OutfitDay
    $ Kitty_Arms = 1 if "Kitty_Arms" not in globals().keys() else Kitty_Arms
    $ K_Emote = "normal" if "K_Emote" not in globals().keys() else K_Emote
    $ K_Arms = 0 if "K_Arms" not in globals().keys() else K_Arms
    $ K_Gloves = 0 if "K_Gloves" not in globals().keys() else K_Gloves
    $ K_Legs = "capris" if "K_Legs" not in globals().keys() else K_Legs
    $ K_Over = "pink top" if "K_Over" not in globals().keys() else K_Over
    $ K_Chest = "cami" if "K_Chest" not in globals().keys() else K_Chest
    $ K_Pierce = 0 if "K_Pierce" not in globals().keys() else K_Pierce
    $ K_Panties = "green panties" if "K_Panties" not in globals().keys() else K_Panties
    $ K_Neck = "gold necklace" if "K_Neck" not in globals().keys() else K_Neck
    $ K_Hose = 0 if "K_Hose" not in globals().keys() else K_Hose
    $ K_Mouth = "normal" if "K_Mouth" not in globals().keys() else K_Mouth
    $ K_Brows = "normal" if "K_Brows" not in globals().keys() else K_Brows
    $ K_Eyes = "normal" if "K_Eyes" not in globals().keys() else K_Eyes
    $ K_Hair = "evo" if "K_Hair" not in globals().keys() else K_Hair
    $ K_HairColor = 0 if "K_HairColor" not in globals().keys() else K_HairColor
    $ K_Blush = 0 if "K_Blush" not in globals().keys() else K_Blush
    $ K_Gag = 0 if "K_Gag" not in globals().keys() else K_Gag
    $ K_Gagx = 0 if "K_Gagx" not in globals().keys() else K_Gagx
    $ K_Blindfold = 0 if "K_Blindfold" not in globals().keys() else K_Blindfold
    $ K_Headband = 0 if "K_Headband" not in globals().keys() else K_Headband
    $ K_Bondage = 0 if "K_Bondage" not in globals().keys() else K_Bondage
    $ K_Spunk = [] if "K_Spunk" not in globals().keys() else K_Spunk
    $ K_Sperm = [] if "K_Sperm" not in globals().keys() else K_Sperm
    $ K_Pubes = 1 if "K_Pubes" not in globals().keys() else K_Pubes
    $ K_Nudes = 1 if "K_Nudes" not in globals().keys() else K_Nudes
    $ K_Tan = 0 if "K_Tan" not in globals().keys() else K_Tan
    $ K_DynamicTan = [0,0,0,0,0,0,0,0] if "K_DynamicTan" not in globals().keys() else K_DynamicTan
    $ K_LegsUp = 0 if "K_LegsUp" not in globals().keys() else K_LegsUp
    $ K_Wet = 0 if "K_Wet" not in globals().keys() else K_Wet
    $ K_Water = 0 if "K_Water" not in globals().keys() else K_Water
    $ K_Upskirt = 0 if "K_Upskirt" not in globals().keys() else K_Upskirt
    $ K_PantiesDown = 0 if "K_PantiesDown" not in globals().keys() else K_PantiesDown
    $ K_Uptop = 0 if "K_Uptop" not in globals().keys() else K_Uptop
    $ K_Held = 0 if "K_Held" not in globals().keys() else K_Held
    $ K_Custom = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom" not in globals().keys() else K_Custom
    $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom2" not in globals().keys() else K_Custom2
    $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom3" not in globals().keys() else K_Custom3
    $ K_Custom4 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom4" not in globals().keys() else K_Custom4
    $ K_Custom5 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom5" not in globals().keys() else K_Custom5
    $ K_Custom6 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom6" not in globals().keys() else K_Custom6
    $ K_Custom7 = [0,0,0,0,0,0,0,0,0,0,0] if "K_Custom7" not in globals().keys() else K_Custom7
    $ K_Gym = [1,0,"shorts",0,0,"sports bra","green panties",0,0,0,0] if "K_Gym" not in globals().keys() else K_Gym
    $ K_Sleepwear = [0,"shorts",0,0,"cami","green panties",0] if "K_Sleepwear" not in globals().keys() else K_Sleepwear
    $ K_Schedule = [0,0,0,0,0,0,0,0,4,0] if "K_Schedule" not in globals().keys() else K_Schedule                      #chooses when she wears what
    $ K_SpriteVer = 0 if "K_SpriteVer" not in globals().keys() else K_SpriteVer
    $ KittyLayer = 100 if "KittyLayer" not in globals().keys() else KittyLayer
    $ K_SpriteLoc = StageCenter if "K_SpriteLoc" not in globals().keys() else K_SpriteLoc                        #Sets Kitty to $ to the center   
#Xavier Sprite Variables    
    $ X_Brows = "happy" if "X_Brows" not in globals().keys() else X_Brows
    $ X_Mouth = "happy" if "X_Mouth" not in globals().keys() else X_Mouth
    $ X_Eyes = "happy" if "X_Eyes" not in globals().keys() else X_Eyes
    $ X_Psychic = 0 if "X_Psychic" not in globals().keys() else X_Psychic
    $ X_Emote = "happy" if "X_Emote" not in globals().keys() else X_Emote
    $ XSpriteLoc = StageCenter if "XSpriteLoc" not in globals().keys() else XSpriteLoc
    
    $ E_Vibrator = 0 if "E_Vibrator" not in globals().keys() else E_Vibrator
    $ E_LegsUp = 0 if "E_LegsUp" not in globals().keys() else E_LegsUp    
    $ E_Gag = 0 if "E_Gag" not in globals().keys() else E_Gag
    $ E_Gagx = 0 if "E_Gagx" not in globals().keys() else E_Gagx
    $ E_Slap = 0 if "E_Slap" not in globals().keys() else E_Slap
    $ E_Spank = 0 if "E_Spank" not in globals().keys() else E_Spank
    $ E_Plugged = 0 if "E_Plugged" not in globals().keys() else E_Plugged
    $ E_Custom = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom" not in globals().keys() else E_Custom
    $ E_Custom2 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom2" not in globals().keys() else E_Custom2
    $ E_Custom3 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom3" not in globals().keys() else E_Custom3
    $ E_Custom4 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom4" not in globals().keys() else E_Custom4
    $ E_Custom5 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom5" not in globals().keys() else E_Custom5
    $ E_Custom6 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom6" not in globals().keys() else E_Custom6
    $ E_Custom7 = [0,0,0,0,0,0,0,0,0,0,0] if "E_Custom7" not in globals().keys() else E_Custom7
    return
