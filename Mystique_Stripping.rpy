# start Strip Tease /////////////////////////////////////////////////////////////////////////////
label Mystique_Strip(Tempmod = Tempmod):    
    call Shift_Focus("Mystique")
    $ newgirl["Mystique"].SpriteLoc = StageCenter 
    call Set_The_Scene
    $ newgirl["Mystique"].Girl_Arms = 2
    call MystiqueFace("sexy")
       
    if "stripping" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You like when I dance for you?",       
            "Didn't get enough earlier?",
            "This is quite a workout."]) 
        ch_m "[Line]" 

    show Mystique_Sprite at Mystique_Dance1()
    "She starts to dance."  
    
    if newgirl["Mystique"].SeenChest or newgirl["Mystique"].SeenPussy:              #You've seen her tits.
        $ Tempmod += 20
    if newgirl["Mystique"].SeenPanties:                           #You've seen her panties.
        $ Tempmod += 5
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo)
    if ("dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames) and not Taboo:
        $ Tempmod += 15
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40 
    elif newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount
    $ Trigger = "strip"
    $ newgirl["Mystique"].RecentActions.append("stripping")                      
    $ newgirl["Mystique"].DailyActions.append("stripping") 
    $ newgirl["Mystique"].Strip += 1
    $ Count = 1
    
label Mystique_Stripping: 
    
    while Round >=0:  
        if Round <= 10:
            ch_m "It's getting late, we should stop for now."
            $ Count = 0
            $ newgirl["Mystique"].Action -= 1    
            $ newgirl["Mystique"].SpriteLoc = StageRight 
            return
        
        $ Round -= 2 if Round > 2 else Round
        
        call MystiqueLust(1) #sets her lusty face    
        if Count != 2:   
            if newgirl["Mystique"].Arms and not newgirl["Mystique"].Over:          
                    #will she lose the gloves? Yes, yes she'll lose the gloves. They're gloves. 
                    $ newgirl["Mystique"].Arms = 0
                    "She pulls her gloves off, and tosses them to the ground."  
               
            elif newgirl["Mystique"].Over and newgirl["Mystique"].Chest and (newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 10):          
                #will she lose the overshirt when she's dressed under?
                if ApprovalCheck("Mystique", 750, TabM = 3):
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 25, 1)                 
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 3)
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0
                    "She pulls her [Line] over her head and throws it behind her."  
                else:
                    jump Mystique_Strip_Ultimatum
                                
            elif newgirl["Mystique"].Legs and (newgirl["Mystique"].Panties or HoseNum("Mystique") >= 10):                              
                #will she lose the pants/skirt if she has panties on?
                if ApprovalCheck("Mystique", 1000, TabM = 3) or (newgirl["Mystique"].SeenPanties and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)                
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 5)
                    $ Line = newgirl["Mystique"].Legs         
                    $ newgirl["Mystique"].Legs = 0      
                    "She unzips and pulls down her [Line], dropping them to the floor."   
                    if not newgirl["Mystique"].SeenPanties:
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 2)
                        $ newgirl["Mystique"].SeenPanties = 1                
                else:
                    jump Mystique_Strip_Ultimatum          
                    
            elif newgirl["Mystique"].Hose: 
                # Will she lose the hose?
                if HoseNum("Mystique") >= 10:
                    if ApprovalCheck("Mystique", 1200, TabM = 3):
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 6)
                        $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 6)
                    else:    
                        jump Mystique_Strip_Ultimatum
                        
                elif HoseNum("Mystique") >= 5 and ApprovalCheck("Mystique", 1200, TabM = 3):
                    if ApprovalCheck("Mystique", 1200, TabM = 3):
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 4)
                        $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 4)
                    else:    
                        jump Mystique_Strip_Ultimatum
                else:
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 3)
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 3)
                $ Line = newgirl["Mystique"].Hose
                $ newgirl["Mystique"].Hose = 0
                "She rolls the [Line] down off her legs, leaving them in a small pile."     
                
            elif newgirl["Mystique"].Over and not newgirl["Mystique"].Chest and (newgirl["Mystique"].Panties or HoseNum("Mystique") >= 10):     
                #will she lose the top when she's topless with panties?        
                if ApprovalCheck("Mystique", 1200, TabM = 3) or (newgirl["Mystique"].SeenChest and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 10)   
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 15)     
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0                       
                    if not newgirl["Mystique"].SeenChest:
                        call MystiqueFace("bemused", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 3)    
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                        call Mystique_First_Topless       
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."     
                else:
                    jump Mystique_Strip_Ultimatum
                
            elif newgirl["Mystique"].Chest and not newgirl["Mystique"].Over:                                     
                # Will she lose the bra?
                if ApprovalCheck("Mystique", 1200, TabM = 3) or (newgirl["Mystique"].SeenChest and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 15)     
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0   
                    call Mystique_Tits_Up
                    if not newgirl["Mystique"].SeenChest:
                        call MystiqueFace("bemused", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 3)          
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        call Mystique_First_Topless
                    else:
                        call MystiqueFace("sexy")
                        "She pulls her [Line] over her head, tossing it to the ground."      
                else:
                    jump Mystique_Strip_Ultimatum
            
            elif newgirl["Mystique"].Legs:                                                       
                #will she lose the pants/skirt if she has no panties on?
                if ApprovalCheck("Mystique", 1350, TabM = 3) or (newgirl["Mystique"].SeenPussy and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 75, 10)    
                    $ Line = newgirl["Mystique"].Legs
                    $ newgirl["Mystique"].Legs = 0                       
                    if not newgirl["Mystique"].SeenPussy:
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 4)  
                        "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."   
                        call Mystique_First_Bottomless 
                    else:                            
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 75, 1)
                        "She unzips and pulls down her [Line], dropping them to the floor."   
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)           
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 85, 15)
                else:
                    jump Mystique_Strip_Ultimatum
                
            elif newgirl["Mystique"].Over and not newgirl["Mystique"].Panties:                                        
                #will she lose the overshirt when she's bottomless under?
                if ApprovalCheck("Mystique", 1350, TabM = 3) or (newgirl["Mystique"].SeenPussy and not Taboo):    
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0               
                    if not newgirl["Mystique"].SeenPussy:                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 4) 
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        call Mystique_First_Bottomless                
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground." 
                    if not newgirl["Mystique"].Chest:
                        if not newgirl["Mystique"].SeenChest:                
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)  
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                            call Mystique_First_Topless
                        else:
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 15)                
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 75, 1)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                    else:
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 75, 10)                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 75, 1)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)                
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 85, 15)    
                else:
                    jump Mystique_Strip_Ultimatum
            
            elif newgirl["Mystique"].Chest:                                                               
                # Will she go topless?
                if ApprovalCheck("Mystique", 1200, TabM = 3) or (newgirl["Mystique"].SeenChest and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5) 
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0   
                    call Mystique_Tits_Up            
                    if not newgirl["Mystique"].SeenChest:
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 4)               
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 3)  
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                        call Mystique_First_Topless
                    else:                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        "She pulls her [Line] over her head, tossing it to the ground."  
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 80, 15)   
                else:
                    jump Mystique_Strip_Ultimatum
                
            elif newgirl["Mystique"].Panties:                                                                       
                # Will she go bottomless?
                if ApprovalCheck("Mystique", 1350, TabM = 3) or (newgirl["Mystique"].SeenPussy and not Taboo):
                    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 75, 10) 
                    $ Line = newgirl["Mystique"].Panties
                    $ newgirl["Mystique"].Panties = 0               
                    if not newgirl["Mystique"].SeenPussy:
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 3)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 200, 5)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, 4) 
                        "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."   
                        call Mystique_First_Bottomless
                    else:                
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 75, 1)
                        "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                    $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 85, 15)
                else:
                    jump Mystique_Strip_Ultimatum
                
            else:    
                call MystiqueFace("sexy")
                ch_m "Well, it appears I've run out of clothes, [newgirl[Mystique].Petname]. . ."
                $ Count = 2        
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 2)               #lust/Focus
        if "exhibitionist" in newgirl["Mystique"].Traits:
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 2)
        $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 3)
        if Trigger2 == "jackin":
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 2)
            $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 5)
        
        if not P_Semen and P_Focus >= 50:
            $ P_Focus = 50

        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                                     #If either of you could cum 
            
            if P_Focus >= 100:                                                  #You cum             
                call Mystique_P_Cumming
                if "angry" in newgirl["Mystique"].RecentActions:  
                    return    
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                if not P_Semen and Trigger2 == "jackin":
                    "You're spitting dust here, maybe just watch quietly for a while."
                    $ Trigger2 = 0
            
                if P_Focus > 80:
                    jump Mystique_Strip_End   
            
            if newgirl["Mystique"].Lust >= 100:                                                   #and Mystique cums                    
                call Mystique_Cumming
                if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:                    
                    $ Count = 0
                    jump Mystique_Strip_End  
            call Mystique_Pos_Reset        
            show Mystique_Sprite at Mystique_Dance1()
            ch_m "I think I've had a bit too much. . . fun."    
            jump Mystique_Strip_End  
        
        menu:
            extend ""
            "Keep Going. . . (locked)" if Count == 2 or "keepdancing" in newgirl["Mystique"].RecentActions:
                pass
            "Keep Going. . ." if Count != 2 and "keepdancing" not in newgirl["Mystique"].RecentActions:
                $ newgirl["Mystique"].Eyes = "sexy"
                if newgirl["Mystique"].Love >= 700 or newgirl["Mystique"].Obed >= 500:
                    if not Tempmod:
                        $ Tempmod = 10
                    elif Count == 1 and Tempmod <= 20:
                        $ Tempmod += 1
                if Taboo and newgirl["Mystique"].Strip <= 10:
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                elif Taboo or newgirl["Mystique"].Strip <= 10:
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 5)
                elif newgirl["Mystique"].Strip <= 50:
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3) 
                "She continues to dance."
            "Keep Dancing. . ." if Count == 2:
                $ newgirl["Mystique"].Eyes = "sexy"        
                "She continues to dance."      
            "Just watch silently" if Count != 2:
                if "watching" not in newgirl["Mystique"].RecentActions:
                    if Count != 2:
                        if Taboo and newgirl["Mystique"].Strip <= 10:
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        elif Taboo or newgirl["Mystique"].Strip <= 10:
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1) 
                    elif newgirl["Mystique"].Strip <= 50:
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 2) 
                    $ newgirl["Mystique"].RecentActions.append("watching")  
                "She continues to dance."
            
            "Start jack'in it." if Trigger2 != "jackin": #add Mystique reaction here.
                call Mystique_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                $ Trigger2 = 0
            "Ok, that's enough.":
                jump Mystique_Strip_End
                
    
    jump Mystique_Stripping
    


label Mystique_Strip_Ultimatum:      
    if newgirl["Mystique"].Arms:          
            #will she lose the gloves? Yes, yes she'll lose the gloves. They're gloves. 
            $ newgirl["Mystique"].Arms = 0
            "She pulls her gloves off, and tosses them to the ground."  
                    
    if "keepdancing" in newgirl["Mystique"].RecentActions: 
        menu:
            "Stop":
                jump Mystique_Strip_End
            "Keep going":
                jump Mystique_Stripping
        
    call Set_The_Scene
    call MystiqueFace("bemused", 1)        
    if "stripforced" in newgirl["Mystique"].RecentActions: 
        call MystiqueFace("sad", 1)    
        ch_m "I think that's plenty, [newgirl[Mystique].Petname]."
    else:
        ch_m "I'm afraid that's as far as I'm ready to go, [newgirl[Mystique].Petname]. . . for now."
    menu:
        extend ""
        "That's ok, you can stop.":                            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
        "That's ok, but keep dancing for a bit. . .":                            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
            $ newgirl["Mystique"].RecentActions.append("keepdancing")
            call Mystique_Pos_Reset        
            show Mystique_Sprite at Mystique_Dance1()
            "Mystique begins to dance again."
            ch_m "Oh, if I must, [newgirl[Mystique].Petname]."
            $ Count = 2
            jump Mystique_Stripping
        "You'd better." if newgirl["Mystique"].Forced:
            if not ApprovalCheck("Mystique", 500, "O", TabM=5) and not ApprovalCheck("Mystique", 800, "L", TabM=5):                    
                call MystiqueFace("angry")
                ch_m "I think you're overstepping your bounds here, [newgirl[Mystique].Petname]."
                ch_m "Remember your place."  
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")  
                $ newgirl["Mystique"].Action -= 1    
                $ newgirl["Mystique"].SpriteLoc = StageRight 
                return                                
            $ Tempmod += 25
            $ newgirl["Mystique"].Forced = 1
            call MystiqueFace("sad")
            if "stripforced" in newgirl["Mystique"].RecentActions:                    
                call MystiqueFace("angry")
                ch_m ". . ."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -40)
            else:
                ch_m "Hmm, forceful. . ."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -40)
                $ newgirl["Mystique"].RecentActions.append("stripforced")
            call Mystique_Pos_Reset        
            show Mystique_Sprite at Mystique_Dance1()
            "Mystique begins to dance again."
            jump Mystique_Stripping
        "You can do better than that. Keep going." if not newgirl["Mystique"].Forced:
            if not ApprovalCheck("Mystique", 300, "O", TabM=5) and not ApprovalCheck("Mystique", 700, "L", TabM=5):                   
                call MystiqueFace("angry")
                ch_m "I think you're overstepping your bounds here, [newgirl[Mystique].Petname]."
                ch_m "Remember your place."  
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")  
                $ newgirl["Mystique"].Action -= 1    
                $ newgirl["Mystique"].SpriteLoc = StageRight 
                return                
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 75, 5)
            $ Tempmod += 25
            $ newgirl["Mystique"].Forced = 1
            call MystiqueFace("sad")
            ch_m "I can't imagine doing better than \"perfection\". . ."
            call Mystique_Pos_Reset        
            show Mystique_Sprite at Mystique_Dance1()
            "Mystique begins to dance again."
            jump Mystique_Stripping
                
label Mystique_Strip_End:   
    ch_m "Ok, [newgirl[Mystique].Petname]. . ."
    $ newgirl["Mystique"].Action -= 1    
    $ Count = 0
    $ newgirl["Mystique"].SpriteLoc = StageCenter    
    call Set_The_Scene
    return

# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

           

# Start Mystique Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Mystique_Undress(Region = "ask", CountStore=0):    
    call Shift_Focus("Mystique")           
    $ CountStore = Tempmod
    
    if Region == "auto":
        if newgirl["Mystique"].Upskirt and newgirl["Mystique"].PantiesDown:
            return
        if newgirl["Mystique"].Legs == "pants":
            $ Tempmod = 20
        if newgirl["Mystique"].Lust >= 90:
            $ Tempmod += 10      
        elif newgirl["Mystique"].Lust >= 80:
            $ Tempmod += 5     
        elif newgirl["Mystique"].Lust >= 70:
            $ Tempmod += 0 
        $ Situation = "auto"
        call Mystique_Bottoms_Off(0)
        $ Situation = 0
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if newgirl["Mystique"].Over or newgirl["Mystique"].Chest:    
                $ Region = "top"     
            "Her bottoms" if newgirl["Mystique"].Legs or newgirl["Mystique"].Panties or newgirl["Mystique"].Hose:
                $ Region = "bottom"           
            "A little of both. . ." if (newgirl["Mystique"].Over or newgirl["Mystique"].Chest) and (newgirl["Mystique"].Legs or newgirl["Mystique"].Panties or newgirl["Mystique"].Hose): 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if newgirl["Mystique"].Over or newgirl["Mystique"].Chest:    
                call Mystique_Top_Off(0)  
    elif Region == "bottom":
        if newgirl["Mystique"].Legs or newgirl["Mystique"].Panties or newgirl["Mystique"].Hose:
                call Mystique_Bottoms_Off(0)  
    elif Region == "both":        
            if newgirl["Mystique"].Over or newgirl["Mystique"].Chest:    
                    call Mystique_Top_Off(0) 
            $ Tempmod = CountStore 
            
            if "angry" in newgirl["Mystique"].RecentActions: 
                    pass            
            elif not newgirl["Mystique"].Legs and not newgirl["Mystique"].Panties and not newgirl["Mystique"].Hose:
                    pass                
            elif "no topless" in newgirl["Mystique"].RecentActions:
                    menu:
                        ch_m "Care to push your luck?"
                        "And now the bottoms?":
                            call Mystique_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Mystique_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Mystique_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Mystique")
    
    if not newgirl["Mystique"].Over and not newgirl["Mystique"].Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in newgirl["Mystique"].RecentActions:  
        ch_m "I'm not in the mood, [newgirl[Mystique].Petname]."
        return
    
    if newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40 
    if "no topless" in newgirl["Mystique"].RecentActions: 
        $ Tempmod -= 10
                     
    if Intro:
        if newgirl["Mystique"].Over:
                ch_p "This might be easier without your [newgirl[Mystique].Over] on."
        elif newgirl["Mystique"].Chest:
                ch_p "This might be easier without your [newgirl[Mystique].Chest] on."

    $ Approval = ApprovalCheck("Mystique", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto":  
        $Line = 0
        if newgirl["Mystique"].Over: # If she's in a top
            if newgirl["Mystique"].Chest and ApprovalCheck("Mystique", 800, TabM = 1):
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 1)
            elif Approval >= 2 or (newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 600) and not Taboo):
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
            else:
                return
            $ Line = newgirl["Mystique"].Over
            $ newgirl["Mystique"].Over = 0
            "Mystique scowls in irritation, and shrugs off her [Line]."
            if not newgirl["Mystique"].Chest:
                if Taboo:
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, (int(Taboo/20)))   
                call Mystique_First_Topless(1)
                
        if newgirl["Mystique"].Chest:
            if Approval >= 2 or (newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 600) and not Taboo):
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                if Taboo:
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, (int(Taboo/20)))  
                if Line:
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0
                    call Mystique_Tits_Up
                    "As it hits the floor, she unfastens her [Line] and allows it to drop as well."  
                else:
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0
                    call Mystique_Tits_Up
                    "Mystique scowls in irritation, she unfastens her [Line] and allows it to drop to the floor."                     
                call Mystique_First_Topless(1) 
                ch_m "Sometimes only direct contact will do."  
        return
    
    
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in newgirl["Mystique"].DailyActions:
            ch_m "{i}Fine,{/i} if that will shut you up."
        call MystiqueFace("sexy", 1)
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)  
        $ Cnt = 1
        while (newgirl["Mystique"].Chest or newgirl["Mystique"].Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_m "What was it you were interested in, [newgirl[Mystique].Petname]?"  
                "Lose the gloves." if newgirl["Mystique"].Arms:
                    call MystiqueFace("bemused", 1)                    
                    $ newgirl["Mystique"].Arms = 0               
                    "Mystique  pulls off her gloves and drops them to the floor."                     
                "Lose the [newgirl[Mystique].Over]." if newgirl["Mystique"].Over:                 
                    call MystiqueFace("bemused", 1)                    
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0
                    "Mystique shrugs off her [Line] and it drops to the floor."
                "Just lose the [newgirl[Mystique].Chest]." if newgirl["Mystique"].Over and newgirl["Mystique"].Chest:
                    call MystiqueFace("bemused", 1)                    
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0   
                    call Mystique_Tits_Up              
                    "Mystique unfastens her [Line] from beneath her [newgirl[Mystique].Over], and allows it to drop to the floor."   
                "Lose the [newgirl[Mystique].Chest]." if not newgirl["Mystique"].Over and newgirl["Mystique"].Chest:
                    call MystiqueFace("bemused", 1)
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0      
                    call Mystique_Tits_Up           
                    "Mystique unfastens her [Line] and allows it to drop to the floor." 
                "Lose both tops." if newgirl["Mystique"].Over and newgirl["Mystique"].Chest:
                    call MystiqueFace("bemused", 1)  
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0
                    call Mystique_Tits_Up
                    "Mystique shrugs off her [Line]-"      
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0 
                    call Mystique_Tits_Up
                    "-followed quickly by her [Line]."           
                "That's enough. [[exit]":               
                    call MystiqueFace("bemused", 1)
                    ch_m "Very well. . ."    
                    $ Cnt = 0
        if not newgirl["Mystique"].Chest and not newgirl["Mystique"].Over:             
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            call Mystique_First_Topless  
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)        
        $ newgirl["Mystique"].RecentActions.append("ask topless")                      
        $ newgirl["Mystique"].DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call MystiqueFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_m "I welcome a massage, but I'm staying fully dressed."
    elif "no topless" in newgirl["Mystique"].RecentActions: 
        call MystiqueFace("angry")
        ch_m "Learn from previous mistakes, [newgirl[Mystique].Petname]."    
    elif Approval and not newgirl["Mystique"].SeenChest:
        ch_m "I don't know if that would be appropriate."    
    elif not newgirl["Mystique"].SeenChest:
        ch_m "I don't think you're ready for that."   
    elif "no topless" in newgirl["Mystique"].DailyActions: 
        ch_m "Are you still that obsessed?"           
    elif "ask topless" in newgirl["Mystique"].RecentActions: 
        ch_m "You want more?"       
    elif Taboo:
        ch_m "[newgirl[Mystique].Petname], not around prying eyes."          
    elif Approval:
        ch_m "Are you sure you're prepared?"
    else:
        ch_m "No."
        
    menu:
        extend ""
        "Sorry, sorry." if "no topless" in newgirl["Mystique"].RecentActions:  
            call MystiqueFace("bemused", 1)   
            ch_m "I can't blame you for your persistance, but learn from your errors."
        "Ok, that's fine." if "no topless" not in newgirl["Mystique"].RecentActions: 
            if "ask topless" not in newgirl["Mystique"].DailyActions:
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
            if newgirl["Mystique"].Forced:
                $ newgirl["Mystique"].Mouth = "grimace"
                ch_m "How. . . generous of you."
                if "ask topless" not in newgirl["Mystique"].DailyActions:
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, 2)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
         
        "Lose the gloves." if newgirl["Mystique"].Arms:
            call MystiqueFace("bemused", 1)
            $ newgirl["Mystique"].Arms = 0               
            "Mystique  pulls off her gloves and drops them to the floor." 
            
        "How about just the [newgirl[Mystique].Over]?" if newgirl["Mystique"].Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Mystique", 1000, TabM = 3) and newgirl["Mystique"].Chest: #80, 160 taboo 
                call MystiqueFace("sexy") 
                ch_m "Well, I suppose that would be fine. . ."                 
                call MystiqueFace("bemused", 1)                
                $ Line = newgirl["Mystique"].Over
                $ newgirl["Mystique"].Over = 0
                "Mystique shrugs off her [Line]."   
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 1)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
            elif not newgirl["Mystique"].Chest:
                $ newgirl["Mystique"].Eyes = "surprised"
                $ newgirl["Mystique"].Blush = 2
                ch_m "I don't think you're prepared for what's under there." 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ newgirl["Mystique"].Mouth = "smile"
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
                        ch_m "Good."             
                    "I think I could handle it.":
                        if ApprovalCheck("Mystique", 700, "I", TabM=3) or ApprovalCheck("Mystique", 1100, TabM=3):
                            call MystiqueFace("bemused", 1)
                            ch_m "Well, I suppose it couldn't hurt to try."                               
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 2)                                                         
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
                            call MystiqueFace("sexy")   
                            $ Line = newgirl["Mystique"].Over
                            $ newgirl["Mystique"].Over = 0
                            "Mystique shrugs off her [Line]."   
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)  
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                            call Mystique_First_Topless   
                        else:   
                            call MystiqueFace("bemused")
                            call Mystique_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Mystique_ToplessorNothing
                $ newgirl["Mystique"].Blush = 1        
            else:   
                call MystiqueFace("sexy")
                call Mystique_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Mystique", 600, "L", TabM=1):                 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)
                call MystiqueFace("sexy")   
                if "no topless" in newgirl["Mystique"].RecentActions:     
                    ch_m "Fine, I can't take your constant begging."
                else:
                    ch_m "Well, I suppose if you ask nicely . . ." 
                if newgirl["Mystique"].Over:
                    $ Line = newgirl["Mystique"].Over
                    $ newgirl["Mystique"].Over = 0
                    call Mystique_Tits_Up
                    "Mystique shrugs off her [Line]. . ."   
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0 
                    call Mystique_Tits_Up
                    ". . .and then her [Line] as well."
                else: 
                    $ Line = newgirl["Mystique"].Chest
                    $ newgirl["Mystique"].Chest = 0 
                    "Mystique shrugs off her [Line]." 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1)  
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                call Mystique_First_Topless 
            elif "no topless" in newgirl["Mystique"].RecentActions:
                call MystiqueFace("angry")
                ch_m "Again, no."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)  
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")   
            else:   
                call MystiqueFace("sexy")
                call Mystique_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Mystique_ToplessorNothing
                                
        "Never mind.":
            pass
    
    $ newgirl["Mystique"].RecentActions.append("ask topless")                      
    $ newgirl["Mystique"].DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Mystique_Top_Off_Refused:                    #When you insist but she refuses    
    call MystiqueFace("angry")
    if "no topless" in newgirl["Mystique"].RecentActions:  
        ch_m "You should probably back off now."
    elif "no topless" in newgirl["Mystique"].DailyActions:  
        ch_m "I'm tired of this, [newgirl[Mystique].Petname]."
    call MystiqueFace("sad")
    menu:
        ch_m "Is this a dealbreaker for you?"
        "No, never mind." if "no topless" not in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)
            ch_m "Good."  
        "Sorry, I'll drop it." if "no topless" in newgirl["Mystique"].RecentActions:   
            ch_m "Good."  
        "Yes, it is.":
            $ newgirl["Mystique"].Brows = "angry"
            ch_m "Very well."
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
            if "no topless" not in newgirl["Mystique"].RecentActions:
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)    
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
    $ newgirl["Mystique"].RecentActions.append("no topless")                      
    $ newgirl["Mystique"].DailyActions.append("no topless") 
    return
              

label Mystique_ToplessorNothing:
    call MystiqueFace("angry")
    if ApprovalCheck("Mystique", 1000, "OI", TabM = 4) and ApprovalCheck("Mystique", 500, "O", TabM = 3):       
        #She agrees to your ultimatum 
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -5, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
        if "no topless" in newgirl["Mystique"].RecentActions:             
            ch_m "Oh, very well. . ."                 
        else:
            call MystiqueFace("sad")
            ch_m "Fine."                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 5)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
        if newgirl["Mystique"].Over:
            if newgirl["Mystique"].Chest:        
                $ Line = newgirl["Mystique"].Over
                $ newgirl["Mystique"].Over = 0 
                call Mystique_Tits_Up
                "Mystique shrugs off her [Line]. . ."    
                $ Line = newgirl["Mystique"].Chest
                $ newgirl["Mystique"].Chest = 0
                call Mystique_Tits_Up
                ". . .and then her [Line] as well."
            else:
                $ Line = newgirl["Mystique"].Over
                $ newgirl["Mystique"].Over = 0
                call Mystique_Tits_Up
                "Mystique shrugs off her [Line]. . ."                    
        elif newgirl["Mystique"].Chest:
            $ Line = newgirl["Mystique"].Chest
            $ newgirl["Mystique"].Chest = 0    
            call Mystique_Tits_Up
            "Mystique unfastens her [Line] and lets it drop to the floor. . ."   
        if newgirl["Mystique"].Arms:            
            $ newgirl["Mystique"].Arms = 0    
            "She pulls off her gloves and drops them to the floor."
        call Mystique_First_Topless                       
    else:                                                                                                
        #she refuses your ultimatum
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, -1, 1)
        if "no topless" in newgirl["Mystique"].RecentActions: 
            $ newgirl["Mystique"].Brows = "angry"
            ch_m "Learn to take \"no\" for an answer."  
        else: 
            ch_m "I'm afraid not."      
        $ newgirl["Mystique"].RecentActions.append("no topless")                      
        $ newgirl["Mystique"].DailyActions.append("no topless")     
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    return              
    
label Mystique_First_Topless(Silent = 0, TempLine = 0):          
    $ newgirl["Mystique"].RecentActions.append("topless")                      
    $ newgirl["Mystique"].DailyActions.append("topless")
    call DrainWord("Mystique","no topless")      
    call Mystique_Tits_Up 
    $ newgirl["Mystique"].SeenChest += 1 
    if newgirl["Mystique"].SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15)  
    if not Silent:
        call MystiqueFace("sly")
        "You get your first look at Mystique's bare chest."
        ch_m "So, [newgirl[Mystique].Petname]? Do you like them?"    
        $ newgirl["Mystique"].Blush = 1
        menu:
            extend ""
            "Definitely, and more.":            
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 20)               
                call MystiqueFace("smile",1)
                ch_m "I do aim to impress."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, 20)  
                $ newgirl["Mystique"].Blush = 0
            ". . . [[stunned]":            
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 30)
                ch_m "Yes, that would be the usual reaction."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, 10)  
            "Huh, not what I was expecting. . .":        
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -30)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 25)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -15)                          
                call MystiqueFace("confused",2)
                ch_m "What?"
                menu:        
                    "They're even better than I imagined!":    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, -20)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 20)                          
                        call MystiqueFace("perplexed",1)
                        ch_m "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":                        
                        call MystiqueFace("angry",2, Mouth="smile")
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 10)   
                        ch_m "Of couse they are!"            
                    "Rogue's were tighter, that's all." if R_SeenChest:                            
                        $ TempLine = "Rogue"
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                        
                if TempLine:
                        call MystiqueFace("angry")
                        $ newgirl["Mystique"].Mouth = "surprised"                        
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 30)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -25)  
                        ". . ."
                        $ newgirl["Mystique"].Mouth = "sad"
                        if TempLine == "Rogue":
                                if newgirl["Mystique"].LikeRogue >= 800:
                                    call MystiqueFace("sly",2,Eyes="side")
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    ch_m "They are rather . . . ripe. . ."       
                                    $ newgirl["Mystique"].LikeRogue += 20 
                                elif newgirl["Mystique"].LikeRogue >= 700:
                                    $ newgirl["Mystique"].Eyes = "side" 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    ch_m "I suppose that's true. . ."    
                                else:                        
                                    $ newgirl["Mystique"].LikeRogue -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if newgirl["Mystique"].LikeKitty >= 800:
                                    call MystiqueFace("sly",2,Eyes="side")
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    ch_m "They are rather . . . pert. . ."       
                                    $ newgirl["Mystique"].LikeKitty += 20 
                                elif newgirl["Mystique"].LikeKitty >= 700:
                                    $ newgirl["Mystique"].Eyes = "side" 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                                    ch_m "Well, for a child. . ."    
                                else:                        
                                    $ newgirl["Mystique"].LikeKitty -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
                                ch_m "I think you've seen enough for now, [newgirl[Mystique].Petname]."   
                                call MystiqueOutfit
                                $ newgirl["Mystique"].RecentActions.append("no topless")                      
                                $ newgirl["Mystique"].DailyActions.append("no topless")  
                                $ newgirl["Mystique"].RecentActions.append("angry")
                                $ newgirl["Mystique"].DailyActions.append("angry")  
                        
                    
    else:
        if ApprovalCheck("Mystique", 800) and not newgirl["Mystique"].Forced:                #if she's not forced and happy about it
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 15) 
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 15)              
            call MystiqueFace("smile")
        else:                                                           #if she's not happy about it
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -40)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -20)                          
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Mystique_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Mystique")
    
    if not newgirl["Mystique"].Legs and not newgirl["Mystique"].Panties and not newgirl["Mystique"].Hose:                                  
        # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in newgirl["Mystique"].RecentActions:  
        ch_m "I would give up on that."
        return
    
    # Will she take her bottoms off Modifiers
    if newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not newgirl["Mystique"].Panties:
        $ Tempmod -= 20
    elif newgirl["Mystique"].SeenPanties and ApprovalCheck("Mystique", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40 
    if "no bottomless" in newgirl["Mystique"].RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if newgirl["Mystique"].Legs:
                ch_p "This might be easier without your [newgirl[Mystique].Legs] on."
        elif newgirl["Mystique"].Panties:
                ch_p "This might be easier without your [newgirl[Mystique].Panties] on."
                
    $ Approval = ApprovalCheck("Mystique", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
            $ Cnt = 0
            
            if not newgirl["Mystique"].Upskirt:                      
                if newgirl["Mystique"].Legs == "skirt" and not newgirl["Mystique"].Upskirt:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (newgirl["Mystique"].SeenPussy and ApprovalCheck("Mystique", 700) and not Taboo):
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                        if Taboo:
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, (int(Taboo/20)))                 
                        $ newgirl["Mystique"].Upskirt = 1
                        "She slides her skirt up."
                        $ Cnt = 1 
                        
                if PantsNum("Mystique") >= 5 or HoseNum("Mystique") >= 5:            
                    if newgirl["Mystique"].Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not newgirl["Mystique"].SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not newgirl["Mystique"].SeenPussy and Taboo):
                        return     
                    elif newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Upskirt:  
                        return
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                    $ newgirl["Mystique"].Upskirt = 1
                    "Mystique shrugs, and then tugs her [Line] down." 
                    if newgirl["Mystique"].Panties:
                        $ newgirl["Mystique"].SeenPanties = 1
                    else:
                        call Mystique_First_Bottomless(1)  
                        
                    if Taboo:
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if newgirl["Mystique"].Panties and not newgirl["Mystique"].PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (newgirl["Mystique"].SeenPussy and not Taboo):
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)
                    if Taboo:
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, (int(Taboo/10)))  
                    $ newgirl["Mystique"].PantiesDown = 1
                    if Cnt:
                        "and pulls her [newgirl[Mystique].Panties] down too."
                    else:
                        "Mystique tsks in irritation, and tugs her [newgirl[Mystique].Panties] down." 
                    call Mystique_First_Bottomless(1) 
                        
                    ch_m "That was just in the way."  
            return
            
    
    if Approval >= 2:                 
            #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
            call MystiqueFace("sexy", 1)
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad", 1)              
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                $ Line = "Oh, very well."            
            elif Approval >= 3:
                $ Line = "Mmmm, what would you like?"
            else:    
                $ Line = "What would you have me take off?" 
            
            call Mystique_Bottoms_Off_Legs
                
            if not newgirl["Mystique"].Panties and Action_Check("Mystique", "recent", "bottomless") < 2: 
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 3)
    
  
        
    elif newgirl["Mystique"].Legs or newgirl["Mystique"].Panties or newgirl["Mystique"].Hose:
            # She'd rather not strip but might        
            call MystiqueFace("bemused", 1) 
            if "no bottomless" in newgirl["Mystique"].RecentActions: 
                call MystiqueFace("angry")
                ch_m "Stop asking, you're embarrassing yourself."   
            elif "no topless" in newgirl["Mystique"].RecentActions: 
                call MystiqueFace("angry")
                ch_m "Do you really think that's likely?"  
            elif Approval and not newgirl["Mystique"].SeenPussy:
                ch_m "I don't know if you're ready for that."  
            elif not newgirl["Mystique"].SeenPussy and "ask topless" in newgirl["Mystique"].RecentActions:
                ch_m "Be careful how far you push it. . ."    
            elif not newgirl["Mystique"].SeenPussy:
                ch_m "Maybe when you've earned it."   
            elif "no bottomless" in newgirl["Mystique"].DailyActions: 
                ch_m "Don't you learn anything, [newgirl[Mystique].Petname]?"             
            elif Taboo:
                ch_m "Not with so many eyes around, [newgirl[Mystique].Petname]. . ."  
            elif Approval:
                ch_m "Probably not. . ."   
            elif newgirl["Mystique"].SeenPussy:
                ch_m "I think you've seen enough . . ."            
            elif PantsNum("Mystique") >= 10:
                ch_m "I'm keeping my pants on."           
            elif newgirl["Mystique"].Legs == "skirt":
                ch_m "I'm keeping my skirt on."   
            elif PantsNum("Mystique") >= 5:
                ch_m "I'm keeping my shorts on."  
            else:
                ch_m "I'm keeping my panties on." 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in newgirl["Mystique"].RecentActions:  
                    if "ask bottomless" not in newgirl["Mystique"].DailyActions:
                        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 2)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                    if newgirl["Mystique"].Forced:
                        $ newgirl["Mystique"].Mouth = "smile"
                        ch_m "Very. . . generous."
                        if "ask bottomless" not in newgirl["Mystique"].DailyActions:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, 3)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 4)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in newgirl["Mystique"].RecentActions:  
                    ch_m "Good."
                 
                "Come on, Please?":       
                    if "no bottomless" in newgirl["Mystique"].DailyActions:  
                            call MystiqueFace("angry")
                            ch_m "I believe you've heard my answer on that."
                    else:
                            if Approval and ApprovalCheck("Mystique", 600, "L", TabM=2):   
                                call MystiqueFace("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                if D20 == 3:
                                    $ Line = "I suppose. . ."
                                    $ Approval += 1
                                else:
                                    $ Line = "Perhaps. . ."                        
                                call Mystique_Bottoms_Off_Legs  
                            else:    
                                call MystiqueFace("sexy")
                                call Mystique_Bottoms_Off_Refused
                                        
                "It doesn't have to be everything. . ." if newgirl["Mystique"].Legs or HoseNum("Mystique") >= 10 or newgirl["Mystique"].Panties == "shorts":    
                    if Approval and "no bottomless" not in newgirl["Mystique"].DailyActions:                    
                        call MystiqueFace("bemused", 1)
                        $Line = "Well what did you have in mind then?"
                        call Mystique_Bottoms_Off_Legs  
                    else:    # She refuses your request. . .
                        call MystiqueFace("sexy")
                        call Mystique_Bottoms_Off_Refused                                
                "It doesn't have to be everything. . . (locked)" if not newgirl["Mystique"].Legs and HoseNum("Mystique") < 10 and newgirl["Mystique"].Panties != "shorts":   
                    pass
                    
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and newgirl["Mystique"].Obed >= 250) or (ApprovalCheck("Mystique", 1000, "OI", TabM = 5) and ApprovalCheck("Mystique", 500, "O", TabM = 3)):                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -1, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                        $ Line =  "Don't test me. . ."  
                        $ Approval = 1 if Approval < 1 else Approval
                        $ newgirl["Mystique"].Forced = 1
                        call Mystique_Bottoms_Off_Legs                     
                    else:          
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                        if ApprovalCheck("Mystique", 400, "O"):
                            ch_m "Definitely not." 
                        else:
                            call MystiqueFace("angry")
                            ch_m "Out of my sight, [newgirl[Mystique].Petname]."                          
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")   
                        $ newgirl["Mystique"].RecentActions.append("no bottomless")                      
                        $ newgirl["Mystique"].DailyActions.append("no bottomless")  
            #end approval
    
    $ Tempmod = 0
    $ newgirl["Mystique"].RecentActions.append("ask bottomless")                      
    $ newgirl["Mystique"].DailyActions.append("ask bottomless")     
    return           

label Mystique_Bottoms_Off_Legs:    
    
    if newgirl["Mystique"].Forced:        
        call MystiqueFace("sad", 1)
    elif ApprovalCheck("Mystique", 1100, "OI", TabM = 3):        
        call MystiqueFace("sly")
    elif ApprovalCheck("Mystique", 1400, TabM = 3):  
        call MystiqueFace("sexy", 1) 
    else:
        call MystiqueFace("bemused", 1) 
        
    $ Line = "Well what did you want off?" if not Line else Line
    $ Cnt = 1
    while Cnt and (newgirl["Mystique"].Legs or newgirl["Mystique"].Panties or newgirl["Mystique"].Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_m "[Line]"
            "Everything. . ." if Line != "Well what did you have in mind then?": #approval a given
                        
                    if Approval < 2 and not newgirl["Mystique"].Panties and HoseNum("Mystique") < 10:
                        call Mystique_NoPanties
                    
                    if newgirl["Mystique"].Legs:
                        $ Line = newgirl["Mystique"].Legs      
                        $ newgirl["Mystique"].Legs = 0
                        "Mystique pulls her [Line] down."
                        $ newgirl["Mystique"].SeenPanties = 1 if not newgirl["Mystique"].SeenPanties else newgirl["Mystique"].SeenPanties
                                           
                    if Approval < 2 and not newgirl["Mystique"].Panties and HoseNum("Mystique") >= 10:
                        call Mystique_NoPanties   
                        
                    if newgirl["Mystique"].Hose:
                        $ Line = newgirl["Mystique"].Hose #HoseName 
                        $ newgirl["Mystique"].Hose = 0
                        "She rolls her hose off."
                    
                                            
                    if Approval < 2:
                        call Mystique_NoPanties   
                    if newgirl["Mystique"].Panties:                               
                        $ Line = newgirl["Mystique"].Panties   
                        $ newgirl["Mystique"].Panties = 0  
                        "She reaches down and pulls her [Line] off." 
                    call Mystique_First_Bottomless   
                    
                    
            "Lose the [newgirl[Mystique].Legs]." if newgirl["Mystique"].Legs: 
                    if newgirl["Mystique"].Panties and Approval >= 2:
                        call MystiqueFace("sexy")
                        ch_m "I can manage that. . ."
                    elif Approval:          
                        call MystiqueFace("sexy", 1)    
                        if Approval < 2 and not newgirl["Mystique"].Panties and HoseNum("Mystique") < 10:
                            call Mystique_NoPanties
                    else:    
                        call MystiqueFace("sexy")
                        call Mystique_Bottoms_Off_Refused
                        return
                        
                    $ Line = newgirl["Mystique"].Legs      
                    $ newgirl["Mystique"].Legs = 0
                    if not newgirl["Mystique"].Panties and HoseNum("Mystique") < 10:
                        call MystiqueFace("sly", 1)  
                        "She looks at you slyly before pulling her [Line] off." 
                        call Mystique_First_Bottomless 
                    else:
                        "Mystique pulls down her [Line]."                        
                        $ newgirl["Mystique"].SeenPanties = 1 if not newgirl["Mystique"].SeenPanties else newgirl["Mystique"].SeenPanties
                    call MystiqueFace("bemused", 1)
            
            
            "Lose the [newgirl[Mystique].Panties]." if newgirl["Mystique"].Panties:
                    if Approval < 2:
                        ch_m "I'm afraid not."
                        $ newgirl["Mystique"].RecentActions.append("no bottomless")                      
                        $ newgirl["Mystique"].DailyActions.append("no bottomless")   
                        return                        
                    elif newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5:
                        ch_m "I suppose that I could. . ."
                    else:
                        ch_m "Of course."                                            
                    $ Line = newgirl["Mystique"].Panties   
                    $ newgirl["Mystique"].Panties = 0  
                             
                    if PantsNum("Mystique") >= 5:
                        "She pulls down her [newgirl[Mystique].Legs], then pulls her [Line] off and puts them back on."    
                    else:
                        "She reaches down and pulls her [Line] off."
                    if not newgirl["Mystique"].Legs:
                        call Mystique_First_Bottomless  
            
#            "Lose the [newgirl[Mystique].Hose]." if newgirl["Mystique"].Hose:                                    #make sure to update this mess if I add hose to her
#                    call MystiqueFace("bemused", 1) 
#                    if newgirl["Mystique"].Legs:
#                        ch_m "All right, fine."                         
#                    elif Approval < 2 and not newgirl["Mystique"].Panties and HoseNum("Mystique") >= 10:
#                        call Mystique_NoPanties                            
#                    elif not Approval and HoseNum("Mystique") >= 5:
#                        ch_m "Sorry, no, [newgirl[Mystique].Petname]."
#                        return                            
#                    else:
#                        ch_m "Fine, [newgirl[Mystique].Petname]."                 
                        
#                    $ Line = newgirl["Mystique"].Hose   
#                    $ newgirl["Mystique"].Hose = 0  
#                    if newgirl["Mystique"].Legs:
#                        "She reaches under her [newgirl[Mystique].Legs] and pulls her [Line] down."
#                    elif HoseNum("Mystique") < 10:
#                        "Mystique pulls her [Line] off." 
#                    elif not newgirl["Mystique"].Panties:
#                        call MystiqueFace("sly", 2)  
#                        "She blushes and looks at you slyly before removing her [Line]." 
#                        $ newgirl["Mystique"].Blush = 1
#                        call Mystique_First_Bottomless   
#                    elif not newgirl["Mystique"].SeenPanties:
#                        "Mystique shyly removes her [Line]."
#                        $ newgirl["Mystique"].SeenPanties = 1
#                    else:
#                        "Mystique pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ newgirl["Mystique"].Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = "Ok, is that all?"
    return


label Mystique_NoPanties: 
    #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if newgirl["Mystique"].Legs or HoseNum("Mystique") >= 10:
        ch_m "I don't have anything on under this. . ."  
    else:
        ch_m "This is all I have on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Mystique", 1100, "LI", TabM=1):                                             
                ch_m "I suppose. . . "
            else:
                ch_m "I'm afraid not."
                call Mystique_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Mystique", 800, "OI", TabM=1):
                ch_m "If you insist."  
            else:
                call Mystique_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Mystique_Bottoms_Off_Refused:     
    if "no bottomless" in newgirl["Mystique"].RecentActions:  
        ch_m "Try to control your impulses."
    elif "no bottomless" in newgirl["Mystique"].DailyActions:  
        ch_m "Not today."
    else:
        call MystiqueFace("sad")
        if Cnt == 2:            
            ch_m "That's all I'm willing to do, is that a deal-breaker?"   
        else:
            ch_m "I'm afraid not, is that a deal-breaker?"        
    menu:
        extend ""
        "No, no, never mind." if "no bottomless" not in newgirl["Mystique"].RecentActions:
            $ newgirl["Mystique"].Mouth = "smile"
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, 2)    
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 2)  
            ch_m "Excellent."    
        "Sorry, I'll drop it." if "no bottomless" in newgirl["Mystique"].RecentActions:   
            ch_m "Good. . ."  
        "Yeah, let's do something else.":
            $ newgirl["Mystique"].Brows = "confused"
            ch_m "Your loss."               
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 5)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2, 1)
            if "no bottomless" not in newgirl["Mystique"].RecentActions:  
                $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 4)      
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
            
    $ newgirl["Mystique"].RecentActions.append("no bottomless")                      
    $ newgirl["Mystique"].DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Mystique_First_Bottomless(Silent = 0): 
    $ newgirl["Mystique"].RecentActions.append("bottomless")                      
    $ newgirl["Mystique"].DailyActions.append("bottomless")
    call DrainWord("Mystique","no bottomless")
    $ newgirl["Mystique"].SeenPussy += 1 
    if newgirl["Mystique"].SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30)  
    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)   
    if not Silent:
        call MystiqueFace("sly")
        "You find yourself staring at Mystique's bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 25)            
                call MystiqueFace("smile")          
                ch_m "I'm aware. . . "
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, 20)
            "I see you keep it smooth down there." if not newgirl["Mystique"].Pubes:          
                call MystiqueFace("confused",1)  
                ch_m "Yes?"
                if ApprovalCheck("Mystique", 700, "LO"):    
                    call MystiqueFace("bemused")     
                    menu:
                        ch_m "Do you prefer more fuzz?"
                        "Yes":
                            if ApprovalCheck("Mystique", 900, "LO"):
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 30)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 25)        
                                ch_m "I suppose I could let it go. . ."
                                $ newgirl["Mystique"].Todo.append("pubes")  
                            else:   
                                call MystiqueFace("normal")     
                                ch_m "Well that's a pity."
                        "Up to you, I guess.":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10)
                                ch_m "I'm glad you agree."
                        "No, leave it that way.":  
                                if ApprovalCheck("Mystique", 900, "LO"):
                                    call MystiqueFace("sly")    
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 10)
                                else:
                                    call MystiqueFace("angry",Mouth="normal")    
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 25) 
                                ch_m "I'm glad I have your. . . permission."
                                $ newgirl["Mystique"].Brows = "normal"
                else:                              
                    call MystiqueFace("angry",1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, -20) 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 25)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, -5)         
                    ch_m "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":        
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -30)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 25)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -30)
                call MystiqueFace("angry",2)           
                if not newgirl["Mystique"].Forced and not ApprovalCheck("Mystique", 900, "LO"):                    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
                ch_m "You will regret that remark. . ."
    else:
        
        if ApprovalCheck("Mystique", 800) and not newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 25)          
            call MystiqueFace("smile")          
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 40, 20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
        else:        
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -40)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, -20)
            call MystiqueFace("angry")          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 30)
    return
    
# End Mystique Undressing  ///////////////////////////////////////////////////////////////////

    

label Mystique_First_Peen(Silent = 0, Undress = 0, GirlsNum = 0): #checked each time she sees your cock  ## call Mystique_First_Peen(0,1)
    if not renpy.showing("Chibi_UI"):
                show Chibi_UI
    if "cockout" in P_RecentActions and "peen" in newgirl["Mystique"].RecentActions: #If the cock is already out and she's seen it, return
            return
            
    $ newgirl["Mystique"].RecentActions.append("peen")                      
    $ newgirl["Mystique"].DailyActions.append("peen")
    $ newgirl["Mystique"].SeenPeen += 1                      
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1)
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call MystiqueFace("down", 2)  
                if GirlsNum:
                    "Mystique also glances down at your cock"
                else:
                    "Mystique glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        if False:
#        if not ApprovalCheck("Mystique", 800) and not ApprovalCheck("Mystique", 400, "I") and "detention" not in newgirl["Mystique"].RecentActions and "classcaught" not in newgirl["Mystique"].RecentActions:
                call MystiqueFace("surprised", Eyes="down")  
                ch_m "Mmm?"
                call MystiqueFace("angry", 1)  
                $ newgirl["Mystique"].RecentActions.append("angry")
                $ newgirl["Mystique"].DailyActions.append("angry")  
                if newgirl["Mystique"].SeenPeen == 1: 
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 35)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 20)
                else:                    
                    ch_m "[newgirl[Mystique].Petname]! We are going to have to work through this. . . problem of yours."
                    if Action_Check("Mystique", "daily", "peen") >= 2:
                            #if she's seen more than one peen today         
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -1)     
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
                    else:
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)                
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 12)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 10)                            
        elif (Taboo and not ApprovalCheck("Mystique", 1500) or newgirl["Mystique"].SEXP < 10) and bg_current != "bg showerroom":
                call MystiqueFace("surprised", 2)  
                ch_m "You really should be careful where you display that thing."
                if newgirl["Mystique"].SeenPeen == 1: 
                    call MystiqueFace("bemused", 1, Eyes="down")  
                    ch_m ". . . impressive though it may be. . ."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 30, 15) 
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 25)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 35)  
                call MystiqueFace("bemused",0)                      
        elif newgirl["Mystique"].SeenPeen > 10:
                return    
        elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                call MystiqueFace("sly",1) 
                if newgirl["Mystique"].SeenPeen == 1: 
                    call MystiqueFace("surprised",1, Eyes="down")  
                    ch_m "Well that's certainly an interesting specimen."
                    call MystiqueFace("bemused",1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 5)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10) 
                elif newgirl["Mystique"].SeenPeen == 2:  
                    $ newgirl["Mystique"].Eyes = "down"
                    ch_m "Oh, hello again."               
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                elif newgirl["Mystique"].SeenPeen == 5: 
                    ch_m "Yes, we've seen that before." 
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7) 
                elif newgirl["Mystique"].SeenPeen == 10:  
                    $ newgirl["Mystique"].Eyes = "down"
                    ch_m "I do appreciate some of your features."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 10)  
                $ newgirl["Mystique"].Eyes = "squint"
        else:
                call MystiqueFace("sad",1) 
                if newgirl["Mystique"].SeenPeen == 1: 
                    call MystiqueFace("perplexed",1 ) 
                    ch_m "Are you aware that your dick is out?"
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                elif newgirl["Mystique"].SeenPeen < 5: 
                    call MystiqueFace("sad",0) 
                    ch_m "You might want to put that away, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                elif newgirl["Mystique"].SeenPeen == 10: 
                    ch_m "Yes, we've all seen that before."               
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if newgirl["Mystique"].SeenPeen > 10:
                    return
                elif ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "L"):
                        if newgirl["Mystique"].SeenPeen == 1: 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 3) 
                        elif newgirl["Mystique"].SeenPeen == 2:      
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 5) 
                        elif newgirl["Mystique"].SeenPeen == 5:          
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7) 
                        elif newgirl["Mystique"].SeenPeen == 10: 
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)  
                else:
                        if newgirl["Mystique"].SeenPeen == 1: 
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        elif newgirl["Mystique"].SeenPeen < 5: 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                        elif newgirl["Mystique"].SeenPeen == 10:              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 7)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                            
    if newgirl["Mystique"].SeenPeen == 1 and "angry" not in newgirl["Mystique"].RecentActions:         
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 10)          
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 20)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 20) 
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 10)
    
    return
    # End Mystique shown peen
    
    
transform Mystique_Dance1():     
    subpixel True 
    pos (StageCenter, 50)
    xoffset 0
    yoffset 0
    choice:
        parallel:              
            ease 2.5 xoffset -40
            ease 2.5 xoffset 0
        parallel:                  
            easeout 1.0 yoffset 30 # 70 and 80
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0 
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50 #1.35
            easein 1.0 yoffset 0  
    choice:
        parallel:              
            ease 2.5 xoffset 40
            ease 2.5 xoffset 0
        parallel:                  
            easeout 1.0 yoffset 30 #1.3
            linear 0.5 yoffset 40
            easein 1.0 yoffset 0 
            easeout 1.0 yoffset 40
            linear 0.5 yoffset 50 #1.35
            easein 1.0 yoffset 0  
    choice(0.3):
        parallel:             
            ease 2 xoffset -30
            ease 2 xoffset 0
        parallel:     
            ease 1 yoffset 200 
            ease 3 yoffset 0 
    repeat