# start Strip Tease /////////////////////////////////////////////////////////////////////////////
label E_Strip(Tempmod = Tempmod):    
    call Shift_Focus("Emma")
    $ E_SpriteLoc = StageCenter 
    call Set_The_Scene
    $ Emma_Arms = 2
    call EmmaFace("sexy")
       
    if "stripping" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You like when I dance for you?",       
            "Didn't get enough earlier?",
            "This is quite a workout."]) 
        ch_e "[Line]" 

    show Emma_Sprite at Emma_Dance1()
    "She starts to dance."  
    
    if E_SeenChest or E_SeenPussy:              #You've seen her tits.
        $ Tempmod += 20
    if E_SeenPanties:                           #You've seen her panties.
        $ Tempmod += 5
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if ("dating" in E_Traits or "sex friend" in E_Petnames) and not Taboo:
        $ Tempmod += 15
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    elif E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
    $ Trigger = "strip"
    $ E_RecentActions.append("stripping")                      
    $ E_DailyActions.append("stripping") 
    $ E_Strip += 1
    $ Count = 1
    
label E_Stripping: 
    
    while Round >=0:  
        if Round <= 10:
            ch_e "It's getting late, we should stop for now."
            $ Count = 0
            $ E_Action -= 1    
            $ E_SpriteLoc = StageRight 
            return
        
        $ Round -= 2 if Round > 2 else Round
        
        call EmmaLust(1) #sets her lusty face    
        if Count != 2:   
            if E_Arms and not E_Over:          
                    #will she lose the gloves? Yes, yes she'll lose the gloves. They're gloves. 
                    $ E_Arms = 0
                    "She pulls her gloves off, and tosses them to the ground."  
               
            elif E_Over and E_Chest and (E_Panties or E_Legs or HoseNum("Emma") >= 10):          
                #will she lose the overshirt when she's dressed under?
                if ApprovalCheck("Emma", 750, TabM = 3):
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 25, 1)                 
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 3)
                    $ Line = E_Over
                    $ E_Over = 0
                    "She pulls her [Line] over her head and throws it behind her."  
                else:
                    jump E_Strip_Ultimatum
                                
            elif E_Legs and (E_Panties or HoseNum("Emma") >= 10):                              
                #will she lose the pants/skirt if she has panties on?
                if ApprovalCheck("Emma", 1000, TabM = 3) or (E_SeenPanties and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)                
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 5)
                    $ Line = E_Legs         
                    $ E_Legs = 0      
                    "She unzips and pulls down her [Line], dropping them to the floor."   
                    if not E_SeenPanties:
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 2)
                        $ E_SeenPanties = 1                
                else:
                    jump E_Strip_Ultimatum          
                    
            elif E_Hose: 
                # Will she lose the hose?
                if HoseNum("Emma") >= 10:
                    if ApprovalCheck("Emma", 1200, TabM = 3):
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 6)
                        $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 6)
                    else:    
                        jump E_Strip_Ultimatum
                        
                elif HoseNum("Emma") >= 5 and ApprovalCheck("Emma", 1200, TabM = 3):
                    if ApprovalCheck("Emma", 1200, TabM = 3):
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 4)
                        $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 4)
                    else:    
                        jump E_Strip_Ultimatum
                else:
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 3)
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 3)
                $ Line = E_Hose
                $ E_Hose = 0
                "She rolls the [Line] down off her legs, leaving them in a small pile."     
                
            elif E_Over and not E_Chest and (E_Panties or HoseNum("Emma") >= 10):     
                #will she lose the top when she's topless with panties?        
                if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10)   
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)     
                    $ Line = E_Over
                    $ E_Over = 0                       
                    if not E_SeenChest:
                        call EmmaFace("bemused", 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 3)    
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                        call Emma_First_Topless       
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."     
                else:
                    jump E_Strip_Ultimatum
                
            elif E_Chest and not E_Over:                                     
                # Will she lose the bra?
                if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)     
                    $ Line = E_Chest
                    $ E_Chest = 0   
                    call Emma_Tits_Up
                    if not E_SeenChest:
                        call EmmaFace("bemused", 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 3)          
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        call Emma_First_Topless
                    else:
                        call EmmaFace("sexy")
                        "She pulls her [Line] over her head, tossing it to the ground."      
                else:
                    jump E_Strip_Ultimatum
            
            elif E_Legs:                                                       
                #will she lose the pants/skirt if she has no panties on?
                if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 75, 10)    
                    $ Line = E_Legs
                    $ E_Legs = 0                       
                    if not E_SeenPussy:
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 4)  
                        "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."   
                        call Emma_First_Bottomless 
                    else:                            
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 75, 1)
                        "She unzips and pulls down her [Line], dropping them to the floor."   
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)           
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 85, 15)
                else:
                    jump E_Strip_Ultimatum
                
            elif E_Over and not E_Panties:                                        
                #will she lose the overshirt when she's bottomless under?
                if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):    
                    $ Line = E_Over
                    $ E_Over = 0               
                    if not E_SeenPussy:                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 4) 
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        call Emma_First_Bottomless                
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground." 
                    if not E_Chest:
                        if not E_SeenChest:                
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)  
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                            call Emma_First_Topless
                        else:
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 15)                
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 75, 1)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                    else:
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 75, 10)                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 75, 1)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)                
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 85, 15)    
                else:
                    jump E_Strip_Ultimatum
            
            elif E_Chest:                                                               
                # Will she go topless?
                if ApprovalCheck("Emma", 1200, TabM = 3) or (E_SeenChest and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
                    $ Line = E_Chest
                    $ E_Chest = 0   
                    call Emma_Tits_Up            
                    if not E_SeenChest:
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 4)               
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 3)  
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                        call Emma_First_Topless
                    else:                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        "She pulls her [Line] over her head, tossing it to the ground."  
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 80, 15)   
                else:
                    jump E_Strip_Ultimatum
                
            elif E_Panties:                                                                       
                # Will she go bottomless?
                if ApprovalCheck("Emma", 1350, TabM = 3) or (E_SeenPussy and not Taboo):
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 75, 10) 
                    $ Line = E_Panties
                    $ E_Panties = 0               
                    if not E_SeenPussy:
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 5)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 4) 
                        "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."   
                        call Emma_First_Bottomless
                    else:                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 75, 1)
                        "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                    $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 85, 15)
                else:
                    jump E_Strip_Ultimatum
                
            else:    
                call EmmaFace("sexy")
                ch_e "Well, it appears I've run out of clothes, [E_Petname]. . ."
                $ Count = 2        
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 2)               #lust/Focus
        if "exhibitionist" in E_Traits:
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 2)
        $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 3)
        if Trigger2 == "jackin":
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 2)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 5)
        
        if not P_Semen and P_Focus >= 50:
            $ P_Focus = 50

        if P_Focus >= 100 or E_Lust >= 100:                                     #If either of you could cum 
            
            if P_Focus >= 100:                                                  #You cum             
                call PE_Cumming
                if "angry" in E_RecentActions:  
                    return    
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                if not P_Semen and Trigger2 == "jackin":
                    "You're spitting dust here, maybe just watch quietly for a while."
                    $ Trigger2 = 0
            
                if P_Focus > 80:
                    jump E_Strip_End   
            
            if E_Lust >= 100:                                                   #and Emma cums                    
                call E_Cumming
                if Situation == "shift" or "angry" in E_RecentActions:                    
                    $ Count = 0
                    jump E_Strip_End  
            call E_Pos_Reset        
            show Emma_Sprite at Emma_Dance1()
            ch_e "I think I've had a bit too much. . . fun."    
            jump E_Strip_End  
        
        menu:
            extend ""
            "Keep Going. . . (locked)" if Count == 2 or "keepdancing" in E_RecentActions:
                pass
            "Keep Going. . ." if Count != 2 and "keepdancing" not in E_RecentActions:
                $ E_Eyes = "sexy"
                if E_Love >= 700 or E_Obed >= 500:
                    if not Tempmod:
                        $ Tempmod = 10
                    elif Count == 1 and Tempmod <= 20:
                        $ Tempmod += 1
                if Taboo and E_Strip <= 10:
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                elif Taboo or E_Strip <= 10:
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                elif E_Strip <= 50:
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3) 
                "She continues to dance."
            "Keep Dancing. . ." if Count == 2:
                $ E_Eyes = "sexy"        
                "She continues to dance."      
            "Just watch silently" if Count != 2:
                if "watching" not in E_RecentActions:
                    if Count != 2:
                        if Taboo and E_Strip <= 10:
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        elif Taboo or E_Strip <= 10:
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1) 
                    elif E_Strip <= 50:
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 2) 
                    $ E_RecentActions.append("watching")  
                "She continues to dance."
            
            "Start jack'in it." if Trigger2 != "jackin": #add Emma reaction here.
                call E_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                $ Trigger2 = 0
            "Ok, that's enough.":
                jump E_Strip_End
                
    
    jump E_Stripping
    


label E_Strip_Ultimatum:      
    if E_Arms:          
            #will she lose the gloves? Yes, yes she'll lose the gloves. They're gloves. 
            $ E_Arms = 0
            "She pulls her gloves off, and tosses them to the ground."  
                    
    if "keepdancing" in E_RecentActions: 
        menu:
            "Stop":
                jump E_Strip_End
            "Keep going":
                jump E_Stripping
        
    call Set_The_Scene
    call EmmaFace("bemused", 1)        
    if "stripforced" in E_RecentActions: 
        call EmmaFace("sad", 1)    
        ch_e "I think that's plenty, [E_Petname]."
    else:
        ch_e "I'm afraid that's as far as I'm ready to go, [E_Petname]. . . for now."
    menu:
        extend ""
        "That's ok, you can stop.":                            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
        "That's ok, but keep dancing for a bit. . .":                            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
            $ E_RecentActions.append("keepdancing")
            call E_Pos_Reset        
            show Emma_Sprite at Emma_Dance1()
            "Emma begins to dance again."
            ch_e "Oh, if I must, [E_Petname]."
            $ Count = 2
            jump E_Stripping
        "You'd better." if E_Forced:
            if not ApprovalCheck("Emma", 500, "O", TabM=5) and not ApprovalCheck("Emma", 800, "L", TabM=5):                    
                call EmmaFace("angry")
                ch_e "I think you're overstepping your bounds here, [E_Petname]."
                ch_e "Remember your place."  
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")  
                $ E_Action -= 1    
                $ E_SpriteLoc = StageRight 
                return                                
            $ Tempmod += 25
            $ E_Forced = 1
            call EmmaFace("sad")
            if "stripforced" in E_RecentActions:                    
                call EmmaFace("angry")
                ch_e ". . ."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -40)
            else:
                ch_e "Hmm, forceful. . ."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -40)
                $ E_RecentActions.append("stripforced")
            call E_Pos_Reset        
            show Emma_Sprite at Emma_Dance1()
            "Emma begins to dance again."
            jump E_Stripping
        "You can do better than that. Keep going." if not E_Forced:
            if not ApprovalCheck("Emma", 300, "O", TabM=5) and not ApprovalCheck("Emma", 700, "L", TabM=5):                   
                call EmmaFace("angry")
                ch_e "I think you're overstepping your bounds here, [E_Petname]."
                ch_e "Remember your place."  
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")  
                $ E_Action -= 1    
                $ E_SpriteLoc = StageRight 
                return                
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 75, 5)
            $ Tempmod += 25
            $ E_Forced = 1
            call EmmaFace("sad")
            ch_e "I can't imagine doing better than \"perfection\". . ."
            call E_Pos_Reset        
            show Emma_Sprite at Emma_Dance1()
            "Emma begins to dance again."
            jump E_Stripping
                
label E_Strip_End:   
    ch_e "Ok, [E_Petname]. . ."
    $ E_Action -= 1    
    $ Count = 0
    $ E_SpriteLoc = StageCenter    
    call Set_The_Scene
    return

# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

           

# Start Emma Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label E_Undress(Region = "ask", CountStore=0):    
    call Shift_Focus("Emma")           
    $ CountStore = Tempmod
    
    if Region == "auto":
        if E_Upskirt and E_PantiesDown:
            return
        if E_Legs == "pants":
            $ Tempmod = 20
        if E_Lust >= 90:
            $ Tempmod += 10      
        elif E_Lust >= 80:
            $ Tempmod += 5     
        elif E_Lust >= 70:
            $ Tempmod += 0 
        $ Situation = "auto"
        call Emma_Bottoms_Off(0)
        $ Situation = 0
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if E_Over or E_Chest:    
                $ Region = "top"     
            "Her bottoms" if E_Legs or E_Panties or E_Hose:
                $ Region = "bottom"           
            "A little of both. . ." if (E_Over or E_Chest) and (E_Legs or E_Panties or E_Hose): 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if E_Over or E_Chest:    
                call Emma_Top_Off(0)  
    elif Region == "bottom":
        if E_Legs or E_Panties or E_Hose:
                call Emma_Bottoms_Off(0)  
    elif Region == "both":        
            if E_Over or E_Chest:    
                    call Emma_Top_Off(0) 
            $ Tempmod = CountStore 
            
            if "angry" in E_RecentActions: 
                    pass            
            elif not E_Legs and not E_Panties and not E_Hose:
                    pass                
            elif "no topless" in E_RecentActions:
                    menu:
                        ch_e "Care to push your luck?"
                        "And now the bottoms?":
                            call Emma_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Emma_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Emma_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Emma")
    
    if not E_Over and not E_Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in E_RecentActions:  
        ch_e "I'm in no mood, [E_Petname]."
        return
    
    if E_SeenChest and ApprovalCheck("Emma", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if "no topless" in E_RecentActions: 
        $ Tempmod -= 10
                     
    if Intro:
        if E_Over:
                ch_p "This might be easier without your [E_Over] on."
        elif E_Chest:
                ch_p "This might be easier without your [E_Chest] on."

    $ Approval = ApprovalCheck("Emma", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto":  
        $Line = 0
        if E_Over: # If she's in a top
            if E_Chest and ApprovalCheck("Emma", 800, TabM = 1):
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 1)
            elif Approval >= 2 or (E_SeenChest and ApprovalCheck("Emma", 600) and not Taboo):
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
            else:
                return
            $ Line = E_Over
            $ E_Over = 0
            "Emma scowls in irritation, and shrugs off her [Line]."
            if not E_Chest:
                if Taboo:
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, (int(Taboo/20)))   
                call Emma_First_Topless(1)
                
        if E_Chest:
            if Approval >= 2 or (E_SeenChest and ApprovalCheck("Emma", 600) and not Taboo):
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
                if Taboo:
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, (int(Taboo/20)))  
                if Line:
                    $ Line = E_Chest
                    $ E_Chest = 0
                    call Emma_Tits_Up
                    "As it hits the floor, she unfastens her [Line] and allows it to drop as well."  
                else:
                    $ Line = E_Chest
                    $ E_Chest = 0
                    call Emma_Tits_Up
                    "Emma scowls in irritation, she unfastens her [Line] and allows it to drop to the floor."                     
                call Emma_First_Topless(1) 
                ch_e "Sometimes only direct contact will do."  
        return
    
    
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in E_DailyActions:
            ch_e "{i}Fine,{/i} if that will shut you up."
        call EmmaFace("sexy", 1)
        if E_Forced:
            call EmmaFace("sad", 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)  
        $ Cnt = 1
        while (E_Chest or E_Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_e "What was it you were interested in, [E_Petname]?"  
                "Lose the gloves." if E_Arms:
                    call EmmaFace("bemused", 1)                    
                    $ E_Arms = 0               
                    "Emma  pulls off her gloves and drops them to the floor."                     
                "Lose the [E_Over]." if E_Over:                 
                    call EmmaFace("bemused", 1)                    
                    $ Line = E_Over
                    $ E_Over = 0
                    "Emma shrugs off her [Line] and it drops to the floor."
                "Just lose the [E_Chest]." if E_Over and E_Chest:
                    call EmmaFace("bemused", 1)                    
                    $ Line = E_Chest
                    $ E_Chest = 0   
                    call Emma_Tits_Up              
                    "Emma unfastens her [Line] from beneath her [E_Over], and allows it to drop to the floor."   
                "Lose the [E_Chest]." if not E_Over and E_Chest:
                    call EmmaFace("bemused", 1)
                    $ Line = E_Chest
                    $ E_Chest = 0      
                    call Emma_Tits_Up           
                    "Emma unfastens her [Line] and allows it to drop to the floor." 
                "Lose both tops." if E_Over and E_Chest:
                    call EmmaFace("bemused", 1)  
                    $ Line = E_Over
                    $ E_Over = 0
                    call Emma_Tits_Up
                    "Emma shrugs off her [Line]-"      
                    $ Line = E_Chest
                    $ E_Chest = 0 
                    call Emma_Tits_Up
                    "-followed quickly by her [Line]."           
                "That's enough. [[exit]":               
                    call EmmaFace("bemused", 1)
                    ch_e "Very well. . ."    
                    $ Cnt = 0
        if not E_Chest and not E_Over:             
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            call Emma_First_Topless  
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)        
        $ E_RecentActions.append("ask topless")                      
        $ E_DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call EmmaFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_e "I welcome a massage, but I'm staying fully dressed."
    elif "no topless" in E_RecentActions: 
        call EmmaFace("angry")
        ch_e "Learn from previous mistakes, [E_Petname]."    
    elif Approval and not E_SeenChest:
        ch_e "I don't know if that would be appropriate."    
    elif not E_SeenChest:
        ch_e "I don't think you're ready for that."   
    elif "no topless" in E_DailyActions: 
        ch_e "Are you still that obsessed?"           
    elif "ask topless" in E_RecentActions: 
        ch_e "You want more?"       
    elif Taboo:
        ch_e "[E_Petname], not around prying eyes."          
    elif Approval:
        ch_e "Are you sure you're prepared?"
    else:
        ch_e "No."
        
    menu:
        extend ""
        "Sorry, sorry." if "no topless" in E_RecentActions:  
            call EmmaFace("bemused", 1)   
            ch_e "I can't blame you for your persistance, but learn from your errors."
        "Ok, that's fine." if "no topless" not in E_RecentActions: 
            if "ask topless" not in E_DailyActions:
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
            if E_Forced:
                $ E_Mouth = "grimace"
                ch_e "How. . . generous of you."
                if "ask topless" not in E_DailyActions:
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 20, 2)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2)
         
        "Lose the gloves." if E_Arms:
            call EmmaFace("bemused", 1)
            $ E_Arms = 0               
            "Emma  pulls off her gloves and drops them to the floor." 
            
        "How about just the [E_Over]?" if E_Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Emma", 1000, TabM = 3) and E_Chest: #80, 160 taboo 
                call EmmaFace("sexy") 
                ch_e "Well, I suppose that would be fine. . ."                 
                call EmmaFace("bemused", 1)                
                $ Line = E_Over
                $ E_Over = 0
                "Emma shrugs off her [Line]."   
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
            elif not E_Chest:
                $ E_Eyes = "surprised"
                $ E_Blush = 2
                ch_e "I don't think you're prepared for what's under there." 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ E_Mouth = "smile"
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2)
                        ch_e "Good."             
                    "I think I could handle it.":
                        if ApprovalCheck("Emma", 700, "I", TabM=3) or ApprovalCheck("Emma", 1100, TabM=3):
                            call EmmaFace("bemused", 1)
                            ch_e "Well, I suppose it couldn't hurt to try."                               
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 2)                                                         
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
                            call EmmaFace("sexy")   
                            $ Line = E_Over
                            $ E_Over = 0
                            "Emma shrugs off her [Line]."   
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)  
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                            call Emma_First_Topless   
                        else:   
                            call EmmaFace("bemused")
                            call Emma_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Emma_ToplessorNothing
                $ E_Blush = 1        
            else:   
                call EmmaFace("sexy")
                call Emma_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Emma", 600, "L", TabM=1):                 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
                call EmmaFace("sexy")   
                if "no topless" in E_RecentActions:     
                    ch_e "Fine, I can't take your constant begging."
                else:
                    ch_e "Well, I suppose if you ask nicely . . ." 
                if E_Over:
                    $ Line = E_Over
                    $ E_Over = 0
                    call Emma_Tits_Up
                    "Emma shrugs off her [Line]. . ."   
                    $ Line = E_Chest
                    $ E_Chest = 0 
                    call Emma_Tits_Up
                    ". . .and then her [Line] as well."
                else: 
                    $ Line = E_Chest
                    $ E_Chest = 0 
                    "Emma shrugs off her [Line]." 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)  
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                call Emma_First_Topless 
            elif "no topless" in E_RecentActions:
                call EmmaFace("angry")
                ch_e "Again, no."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)  
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
            else:   
                call EmmaFace("sexy")
                call Emma_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Emma_ToplessorNothing
                                
        "Never mind.":
            pass
    
    $ E_RecentActions.append("ask topless")                      
    $ E_DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Emma_Top_Off_Refused:                    #When you insist but she refuses    
    call EmmaFace("angry")
    if "no topless" in E_RecentActions:  
        ch_e "You should probably back off now."
    elif "no topless" in E_DailyActions:  
        ch_e "I'm tired of this, [E_Petname]."
    call EmmaFace("sad")
    menu:
        ch_e "Is this a dealbreaker for you?"
        "No, never mind." if "no topless" not in E_RecentActions:
            call EmmaFace("sexy")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2)
            ch_e "Good."  
        "Sorry, I'll drop it." if "no topless" in E_RecentActions:   
            ch_e "Good."  
        "Yes, it is.":
            $ E_Brows = "angry"
            ch_e "Very well."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
            if "no topless" not in E_RecentActions:
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)    
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    $ E_RecentActions.append("no topless")                      
    $ E_DailyActions.append("no topless") 
    return
              

label Emma_ToplessorNothing:
    call EmmaFace("angry")
    if ApprovalCheck("Emma", 1000, "OI", TabM = 4) and ApprovalCheck("Emma", 500, "O", TabM = 3):       
        #She agrees to your ultimatum 
        $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -5, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
        if "no topless" in E_RecentActions:             
            ch_e "Oh, very well. . ."                 
        else:
            call EmmaFace("sad")
            ch_e "Fine."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
        if E_Over:
            if E_Chest:        
                $ Line = E_Over
                $ E_Over = 0 
                call Emma_Tits_Up
                "Emma shrugs off her [Line]. . ."    
                $ Line = E_Chest
                $ E_Chest = 0
                call Emma_Tits_Up
                ". . .and then her [Line] as well."
            else:
                $ Line = E_Over
                $ E_Over = 0
                call Emma_Tits_Up
                "Emma shrugs off her [Line]. . ."                    
        elif E_Chest:
            $ Line = E_Chest
            $ E_Chest = 0    
            call Emma_Tits_Up
            "Emma unfastens her [Line] and lets it drop to the floor. . ."   
        if E_Arms:            
            $ E_Arms = 0    
            "She pulls off her gloves and drops them to the floor."
        call Emma_First_Topless                       
    else:                                                                                                
        #she refuses your ultimatum
        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, -1, 1)
        if "no topless" in E_RecentActions: 
            $E_Brows = "angry"
            ch_e "Learn to take \"no\" for an answer."  
        else: 
            ch_e "I'm afraid not."      
        $ E_RecentActions.append("no topless")                      
        $ E_DailyActions.append("no topless")     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    return              
    
label Emma_First_Topless(Silent = 0, TempLine = 0):          
    $ E_RecentActions.append("topless")                      
    $ E_DailyActions.append("topless")
    call DrainWord("Emma","no topless")      
    call Emma_Tits_Up 
    $ E_SeenChest += 1 
    if E_SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15)  
    if not Silent:
        call EmmaFace("sly")
        "You get your first look at Emma's bare chest."
        ch_e "Well, [E_Petname]? Is it everything you dreamed?"    
        $ E_Blush = 1
        menu:
            extend ""
            "Definitely, and more.":            
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 20)               
                call EmmaFace("smile",1)
                ch_e "I do aim to impress."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 40, 20)  
                $ E_Blush = 0
            ". . . [[stunned]":            
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 30)
                ch_e "Yes, that would be the usual reaction."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 40, 10)  
            "Huh, not what I was expecting. . .":        
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -30)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 25)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -15)                          
                call EmmaFace("confused",2)
                ch_e "What?"
                menu:        
                    "They're even better than I imagined!":    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -20)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 20)                          
                        call EmmaFace("perplexed",1)
                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":                        
                        call EmmaFace("angry",2, Mouth="smile")
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 10)   
                        ch_e "Of couse they are!"            
                    "Rogue's were tighter, that's all." if R_SeenChest:                            
                        $ TempLine = "Rogue"
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                        
                if TempLine:
                        call EmmaFace("angry")
                        $ E_Mouth = "surprised"                        
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 30)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -25)  
                        ". . ."
                        $ E_Mouth = "sad"
                        if TempLine == "Rogue":
                                if E_LikeRogue >= 800:
                                    call EmmaFace("sly",2,Eyes="side")
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    ch_e "They are rather . . . ripe. . ."       
                                    $ E_LikeRogue += 20 
                                elif E_LikeRogue >= 700:
                                    $ E_Eyes = "side" 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    ch_e "I suppose that's true. . ."    
                                else:                        
                                    $ E_LikeRogue -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if E_LikeKitty >= 800:
                                    call EmmaFace("sly",2,Eyes="side")
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    ch_e "They are rather . . . pert. . ."       
                                    $ E_LikeKitty += 20 
                                elif E_LikeKitty >= 700:
                                    $ E_Eyes = "side" 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                    ch_e "Well, for a child. . ."    
                                else:                        
                                    $ E_LikeKitty -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
                                ch_e "I think you've seen enough for now, [E_Petname]."   
                                call EmmaOutfit
                                $ E_RecentActions.append("no topless")                      
                                $ E_DailyActions.append("no topless")  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")  
                        
                    
    else:
        if ApprovalCheck("Emma", 800) and not E_Forced:                #if she's not forced and happy about it
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 15) 
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 15)              
            call EmmaFace("smile")
        else:                                                           #if she's not happy about it
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -40)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -20)                          
            call EmmaFace("angry")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Emma_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Emma")
    
    if not E_Legs and not E_Panties and not E_Hose:                                  
        # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in E_RecentActions:  
        ch_e "I would give up on that."
        return
    
    # Will she take her bottoms off Modifiers
    if E_SeenPussy and ApprovalCheck("Emma", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not E_Panties:
        $ Tempmod -= 20
    elif E_SeenPanties and ApprovalCheck("Emma", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in E_Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if "no bottomless" in E_RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if E_Legs:
                ch_p "This might be easier without your [E_Legs] on."
        elif E_Panties:
                ch_p "This might be easier without your [E_Panties] on."
                
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
            $ Cnt = 0
            
            if not E_Upskirt:                      
                if E_Legs == "skirt" and not E_Upskirt:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (E_SeenPussy and ApprovalCheck("Emma", 700) and not Taboo):
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                        if Taboo:
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, (int(Taboo/20)))                 
                        $ E_Upskirt = 1
                        "She slides her skirt up."
                        $ Cnt = 1 
                        
                if PantsNum("Emma") >= 5 or HoseNum("Emma") >= 5:            
                    if E_Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not E_SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not E_SeenPussy and Taboo):
                        return     
                    elif E_Legs == "pants" and E_Upskirt:  
                        return
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                    $ E_Upskirt = 1
                    "Emma shrugs, and then tugs her [Line] down." 
                    if E_Panties:
                        $ E_SeenPanties = 1
                    else:
                        call Emma_First_Bottomless(1)  
                        
                    if Taboo:
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if E_Panties and not E_PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (E_SeenPussy and not Taboo):
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
                    if Taboo:
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, (int(Taboo/10)))  
                    $ E_PantiesDown = 1
                    if Cnt:
                        "and pulls her [E_Panties] down too."
                    else:
                        "Emma tsks in irritation, and tugs her [E_Panties] down." 
                    call Emma_First_Bottomless(1) 
                        
                    ch_e "That was just in the way."  
            return
            
    
    if Approval >= 2:                 
            #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
            call EmmaFace("sexy", 1)
            if E_Forced:
                call EmmaFace("sad", 1)              
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                $ Line = "Oh, very well."            
            elif Approval >= 3:
                $ Line = "Mmmm, what would you like?"
            else:    
                $ Line = "What would you have me take off?" 
            
            call Emma_Bottoms_Off_Legs
                
            if not E_Panties and Action_Check("Emma", "recent", "bottomless") < 2: 
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 3)
    
  
        
    elif E_Legs or E_Panties or E_Hose:
            # She'd rather not strip but might        
            call EmmaFace("bemused", 1) 
            if "no bottomless" in E_RecentActions: 
                call EmmaFace("angry")
                ch_e "Stop asking, you're embarrassing yourself."   
            elif "no topless" in E_RecentActions: 
                call EmmaFace("angry")
                ch_e "Do you really think that's likely?"  
            elif Approval and not E_SeenPussy:
                ch_e "I don't know if you're ready for that."  
            elif not E_SeenPussy and "ask topless" in E_RecentActions:
                ch_e "Be careful how far you push it. . ."    
            elif not E_SeenPussy:
                ch_e "Maybe when you've earned it."   
            elif "no bottomless" in E_DailyActions: 
                ch_e "Don't you learn anything, [E_Petname]?"             
            elif Taboo:
                ch_e "Not with so many eyes around, [E_Petname]. . ."  
            elif Approval:
                ch_e "Probably not. . ."   
            elif E_SeenPussy:
                ch_e "I think you've seen enough . . ."            
            elif PantsNum("Emma") >= 10:
                ch_e "I'm keeping my pants on."           
            elif E_Legs == "skirt":
                ch_e "I'm keeping my skirt on."   
            elif PantsNum("Emma") >= 5:
                ch_e "I'm keeping my shorts on."  
            else:
                ch_e "I'm keeping my panties on." 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in E_RecentActions:  
                    if "ask bottomless" not in E_DailyActions:
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 2)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                    if E_Forced:
                        $ E_Mouth = "smile"
                        ch_e "Very. . . generous."
                        if "ask bottomless" not in E_DailyActions:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, 3)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 4)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in E_RecentActions:  
                    ch_e "Good."
                 
                "Come on, Please?":       
                    if "no bottomless" in E_DailyActions:  
                            call EmmaFace("angry")
                            ch_e "I believe you've heard my answer on that."
                    else:
                            if Approval and ApprovalCheck("Emma", 600, "L", TabM=2):   
                                call EmmaFace("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                if D20 == 3:
                                    $ Line = "I suppose. . ."
                                    $ Approval += 1
                                else:
                                    $ Line = "Perhaps. . ."                        
                                call Emma_Bottoms_Off_Legs  
                            else:    
                                call EmmaFace("sexy")
                                call Emma_Bottoms_Off_Refused
                                        
                "It doesn't have to be everything. . ." if E_Legs or HoseNum("Emma") >= 10 or E_Panties == "shorts":    
                    if Approval and "no bottomless" not in E_DailyActions:                    
                        call EmmaFace("bemused", 1)
                        $Line = "Well what did you have in mind then?"
                        call Emma_Bottoms_Off_Legs  
                    else:    # She refuses your request. . .
                        call EmmaFace("sexy")
                        call Emma_Bottoms_Off_Refused                                
                "It doesn't have to be everything. . . (locked)" if not E_Legs and HoseNum("Emma") < 10 and E_Panties != "shorts":   
                    pass
                    
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and E_Obed >= 250) or (ApprovalCheck("Emma", 1000, "OI", TabM = 5) and ApprovalCheck("Emma", 500, "O", TabM = 3)):                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -1, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                        $ Line =  "Don't test me. . ."  
                        $ Approval = 1 if Approval < 1 else Approval
                        $ E_Forced = 1
                        call Emma_Bottoms_Off_Legs                     
                    else:          
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                        if ApprovalCheck("Emma", 400, "O"):
                            ch_e "Definitely not." 
                        else:
                            call EmmaFace("angry")
                            ch_e "Out of my sight, [E_Petname]."                          
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")   
                        $ E_RecentActions.append("no bottomless")                      
                        $ E_DailyActions.append("no bottomless")  
            #end approval
    
    $ Tempmod = 0
    $ E_RecentActions.append("ask bottomless")                      
    $ E_DailyActions.append("ask bottomless")     
    return           

label Emma_Bottoms_Off_Legs:    
    
    if E_Forced:        
        call EmmaFace("sad", 1)
    elif ApprovalCheck("Emma", 1100, "OI", TabM = 3):        
        call EmmaFace("sly")
    elif ApprovalCheck("Emma", 1400, TabM = 3):  
        call EmmaFace("sexy", 1) 
    else:
        call EmmaFace("bemused", 1) 
        
    $ Line = "Well what did you want off?" if not Line else Line
    $ Cnt = 1
    while Cnt and (E_Legs or E_Panties or E_Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_e "[Line]"
            "Everything. . ." if Line != "Well what did you have in mind then?": #approval a given
                        
                    if Approval < 2 and not E_Panties and HoseNum("Emma") < 10:
                        call Emma_NoPanties
                    
                    if E_Legs:
                        $ Line = E_Legs      
                        $ E_Legs = 0
                        "Emma pulls her [Line] down."
                        $ E_SeenPanties = 1 if not E_SeenPanties else E_SeenPanties
                                           
                    if Approval < 2 and not E_Panties and HoseNum("Emma") >= 10:
                        call Emma_NoPanties   
                        
                    if E_Hose:
                        $ Line = E_Hose #HoseName 
                        $ E_Hose = 0
                        "She rolls her hose off."
                    
                                            
                    if Approval < 2:
                        call Emma_NoPanties   
                    if E_Panties:                               
                        $ Line = E_Panties   
                        $ E_Panties = 0  
                        "She reaches down and pulls her [Line] off." 
                    call Emma_First_Bottomless   
                    
                    
            "Lose the [E_Legs]." if E_Legs: 
                    if E_Panties and Approval >= 2:
                        call EmmaFace("sexy")
                        ch_e "I can manage that. . ."
                    elif Approval:          
                        call EmmaFace("sexy", 1)    
                        if Approval < 2 and not E_Panties and HoseNum("Emma") < 10:
                            call Emma_NoPanties
                    else:    
                        call EmmaFace("sexy")
                        call Emma_Bottoms_Off_Refused
                        return
                        
                    $ Line = E_Legs      
                    $ E_Legs = 0
                    if not E_Panties and HoseNum("Emma") < 10:
                        call EmmaFace("sly", 1)  
                        "She looks at you slyly before pulling her [Line] off." 
                        call Emma_First_Bottomless 
                    else:
                        "Emma pulls down her [Line]."                        
                        $ E_SeenPanties = 1 if not E_SeenPanties else E_SeenPanties
                    call EmmaFace("bemused", 1)
            
            
            "Lose the [E_Panties]." if E_Panties:
                    if Approval < 2:
                        ch_e "I'm afraid not."
                        $ E_RecentActions.append("no bottomless")                      
                        $ E_DailyActions.append("no bottomless")   
                        return                        
                    elif E_Legs == "pants" or HoseNum("Emma") >= 5:
                        ch_e "I suppose that I could. . ."
                    else:
                        ch_e "Of course."                                            
                    $ Line = E_Panties   
                    $ E_Panties = 0  
                             
                    if PantsNum("Emma") >= 5:
                        "She pulls down her [E_Legs], then pulls her [Line] off and puts them back on."    
                    else:
                        "She reaches down and pulls her [Line] off."
                    if not E_Legs:
                        call Emma_First_Bottomless  
            
#            "Lose the [E_Hose]." if E_Hose:                                    #make sure to update this mess if I add hose to her
#                    call EmmaFace("bemused", 1) 
#                    if E_Legs:
#                        ch_e "All right, fine."                         
#                    elif Approval < 2 and not E_Panties and HoseNum("Emma") >= 10:
#                        call Emma_NoPanties                            
#                    elif not Approval and HoseNum("Emma") >= 5:
#                        ch_e "Sorry, no, [E_Petname]."
#                        return                            
#                    else:
#                        ch_e "Fine, [E_Petname]."                 
                        
#                    $ Line = E_Hose   
#                    $ E_Hose = 0  
#                    if E_Legs:
#                        "She reaches under her [E_Legs] and pulls her [Line] down."
#                    elif HoseNum("Emma") < 10:
#                        "Emma pulls her [Line] off." 
#                    elif not E_Panties:
#                        call EmmaFace("sly", 2)  
#                        "She blushes and looks at you slyly before removing her [Line]." 
#                        $ E_Blush = 1
#                        call Emma_First_Bottomless   
#                    elif not E_SeenPanties:
#                        "Emma shyly removes her [Line]."
#                        $ E_SeenPanties = 1
#                    else:
#                        "Emma pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ E_Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = "Ok, is that all?"
    return


label Emma_NoPanties: 
    #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if E_Legs or HoseNum("Emma") >= 10:
        ch_e "I don't have anything on under this. . ."  
    else:
        ch_e "This is all I have on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Emma", 1100, "LI", TabM=1):                                             
                ch_e "I suppose. . . "
            else:
                ch_e "I'm afraid not."
                call Emma_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Emma", 800, "OI", TabM=1):
                ch_e "If you insist."  
            else:
                call Emma_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Emma_Bottoms_Off_Refused:     
    if "no bottomless" in E_RecentActions:  
        ch_e "Try to control your impulses."
    elif "no bottomless" in E_DailyActions:  
        ch_e "Not today."
    else:
        call EmmaFace("sad")
        if Cnt == 2:            
            ch_e "That's all I'm willing to do, is that a deal-breaker?"   
        else:
            ch_e "I'm afraid not, is that a deal-breaker?"        
    menu:
        extend ""
        "No, no, never mind." if "no bottomless" not in E_RecentActions:
            $ E_Mouth = "smile"
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2)    
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)  
            ch_e "Excellent."    
        "Sorry, I'll drop it." if "no bottomless" in E_RecentActions:   
            ch_e "Good. . ."  
        "Yeah, let's do something else.":
            $E_Brows = "confused"
            ch_e "Your loss."               
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 5)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
            if "no bottomless" not in E_RecentActions:  
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)      
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
            
    $ E_RecentActions.append("no bottomless")                      
    $ E_DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Emma_First_Bottomless(Silent = 0): 
    $ E_RecentActions.append("bottomless")                      
    $ E_DailyActions.append("bottomless")
    call DrainWord("Emma","no bottomless")
    $ E_SeenPussy += 1 
    if E_SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30)  
    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)   
    if not Silent:
        call EmmaFace("sly")
        "You find yourself staring at [EmmaName]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 25)            
                call EmmaFace("smile")          
                ch_e "I'm aware. . . "
                $ E_Love = Statupdate("Emma", "Love", E_Love, 40, 20)
            "I see you keep it smooth down there." if not E_Pubes:          
                call EmmaFace("confused",1)  
                ch_e "Yes?"
                if ApprovalCheck("Emma", 700, "LO"):    
                    call EmmaFace("bemused")     
                    menu:
                        ch_e "Do you prefer more fuzz?"
                        "Yes":
                            if ApprovalCheck("Emma", 900, "LO"):
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 30)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 25)        
                                ch_e "I suppose I could let it go. . ."
                                $ E_Todo.append("pubes")  
                            else:   
                                call EmmaFace("normal")     
                                ch_e "Well that's a pity."
                        "Up to you, I guess.":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10)
                                ch_e "I'm glad you agree."
                        "No, leave it that way.":  
                                if ApprovalCheck("Emma", 900, "LO"):
                                    call EmmaFace("sly")    
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 10)
                                else:
                                    call EmmaFace("angry",Mouth="normal")    
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 25) 
                                ch_e "I'm glad I have your. . . permission."
                                $ E_Brows = "normal"
                else:                              
                    call EmmaFace("angry",1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 40, -20) 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 25)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, -5)         
                    ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":        
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -30)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 25)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -30)
                call EmmaFace("angry",2)           
                if not E_Forced and not ApprovalCheck("Emma", 900, "LO"):                    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
                ch_e "You will regret that remark. . ."
    else:
        
        if ApprovalCheck("Emma", 800) and not E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 25)          
            call EmmaFace("smile")          
            $ E_Love = Statupdate("Emma", "Love", E_Love, 40, 20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
        else:        
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -40)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, -20)
            call EmmaFace("angry")          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
    return
    
# End Emma Undressing  ///////////////////////////////////////////////////////////////////

    

label Emma_First_Peen(Silent = 0, Undress = 0, GirlsNum = 0): #checked each time she sees your cock  ## call Emma_First_Peen(0,1)
    if not renpy.showing("Chibi_UI"):
                show Chibi_UI
    if "cockout" in P_RecentActions and "peen" in E_RecentActions: #If the cock is already out and she's seen it, return
            return
            
    $ E_RecentActions.append("peen")                      
    $ E_DailyActions.append("peen")
    $ E_SeenPeen += 1                      
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1)
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call EmmaFace("down", 2)  
                if GirlsNum:
                    "Emma also glances down at your cock"
                else:
                    "Emma glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        if False:
#        if not ApprovalCheck("Emma", 800) and not ApprovalCheck("Emma", 400, "I") and "detention" not in E_RecentActions and "classcaught" not in E_RecentActions:
                call EmmaFace("surprised", Eyes="down")  
                ch_e "Mmm?"
                call EmmaFace("angry", 1)  
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")  
                if E_SeenPeen == 1: 
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 35)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 20)
                else:                    
                    ch_e "[E_Petname]! We are going to have to work through this. . . problem of yours."
                    if Action_Check("Emma", "daily", "peen") >= 2:
                            #if she's seen more than one peen today         
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1)     
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
                    else:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)                
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 12)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 10)                            
        elif (Taboo and not ApprovalCheck("Emma", 1500) or E_SEXP < 10) and bg_current != "bg showerroom":
                call EmmaFace("surprised", 2)  
                ch_e "You really should be careful where you display that thing."
                if E_SeenPeen == 1: 
                    call EmmaFace("bemused", 1, Eyes="down")  
                    ch_e ". . . impressive though it may be. . ."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 30, 15) 
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 25)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 35)  
                call EmmaFace("bemused",0)                      
        elif E_SeenPeen > 10:
                return    
        elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                call EmmaFace("sly",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("surprised",1, Eyes="down")  
                    ch_e "Well that's certainly an interesting specimen."
                    call EmmaFace("bemused",1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 5)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10) 
                elif E_SeenPeen == 2:  
                    $ E_Eyes = "down"
                    ch_e "Oh, hello again."               
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                elif E_SeenPeen == 5: 
                    ch_e "Yes, we've seen that before." 
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7) 
                elif E_SeenPeen == 10:  
                    $ E_Eyes = "down"
                    ch_e "I do appreciate some of your features."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 10)  
                $ E_Eyes = "squint"
        else:
                call EmmaFace("sad",1) 
                if E_SeenPeen == 1: 
                    call EmmaFace("perplexed",1 ) 
                    ch_e "Are you aware that your dick is out?"
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                elif E_SeenPeen < 5: 
                    call EmmaFace("sad",0) 
                    ch_e "You might want to put that away, [E_Petname]."
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                elif E_SeenPeen == 10: 
                    ch_e "Yes, we've all seen that before."               
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if E_SeenPeen > 10:
                    return
                elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                        if E_SeenPeen == 1: 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3) 
                        elif E_SeenPeen == 2:      
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                        elif E_SeenPeen == 5:          
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7) 
                        elif E_SeenPeen == 10: 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)  
                else:
                        if E_SeenPeen == 1: 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        elif E_SeenPeen < 5: 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                        elif E_SeenPeen == 10:              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                            
    if E_SeenPeen == 1 and "angry" not in E_RecentActions:         
        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 10)          
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 20)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 20) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10)
    
    return
    # End Emma shown peen
    
    
transform Emma_Dance1():     
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