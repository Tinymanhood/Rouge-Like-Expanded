# start Strip Tease /////////////////////////////////////////////////////////////////////////////
label R_Strip(Tempmod = Tempmod):  
    call Shift_Focus("Rogue")  
    $ R_SpriteLoc = StageCenter 
    call Set_The_Scene
    $ Rogue_Arms = 2
    call RogueFace("sexy")
       
    if "stripping" in R_DailyActions:
        call RogueFace("sexy", 1)
        $ Line = renpy.random.choice(["You liked the show earlier?",       
            "Didn't get enough earlier?",
            "You're going to wear me out."]) 
        ch_r "[Line]" 

    show Rogue at Rogue_Dance1()
    "She starts to dance."  
    
    if (R_SeenChest or R_SeenPussy) and ApprovalCheck("Rogue", 500):              #You've seen her tits.
        $ Tempmod += 20
    if R_SeenPanties and ApprovalCheck("Rogue", 500):                           #You've seen her panties.
        $ Tempmod += 5
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if ("dating" in R_Traits or "sex friend" in R_Petnames) and not Taboo:
        $ Tempmod += 15
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    $ Trigger = "strip"
    $ R_RecentActions.append("stripping")                      
    $ R_DailyActions.append("stripping") 
    $ R_Strip += 1
    $ Count = 1
    
label R_Stripping: 
    
    while Round >=0:  
        if Round <= 10:
            ch_r "It's getting late, we should stop for now."
            $ Count = 0
            $ R_Action -= 1    
            $ R_SpriteLoc = StageRight 
            return
        
        $ Round -= 2 if Round > 2 else Round
        
        call RogueLust(1) #sets her lusty face    
        if Count != 2:             
            if R_Over and R_Chest and (R_Panties or R_Legs or HoseNum("Rogue") >= 10):          #will she lose the overshirt when she's dressed under?
                if ApprovalCheck("Rogue", 750, TabM = 3):
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 1)                 
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 3)
                    $ Line = R_Over                
                    $ R_Over = 0                     
                    "She pulls her [Line] over her head and throws it behind her."  
                else:
                    jump R_Strip_Ultimatum
            
            elif R_Legs and (R_Panties or HoseNum("Rogue") >= 10):                              #will she lose the pants/skirt if she has panties on?
                if ApprovalCheck("Rogue", 1200, TabM = 3) or (R_SeenPanties and ApprovalCheck("Rogue", 900, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)                
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 5)
                    $ Line = R_Legs         
                    $ R_Legs = 0      
                    "She unzips and pulls down her [Line], dropping them to the floor."   
                    if not R_SeenPanties:
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 2)
                        $ R_SeenPanties = 1                
                else:
                    jump R_Strip_Ultimatum          
                    
            elif R_Hose:  # Will she lose the hose?
                if HoseNum("Rogue") >= 10:
                    if ApprovalCheck("Rogue", 1200, TabM = 3):
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 6)
                        $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 6)
                    else:    
                        jump R_Strip_Ultimatum
                        
                elif HoseNum("Rogue") >= 5 and ApprovalCheck("Rogue", 1200, TabM = 3):
                    if ApprovalCheck("Rogue", 1200, TabM = 3):
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 4)
                        $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 4)
                    else:    
                        jump R_Strip_Ultimatum
                else:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 3)
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 3)
                $ Line = R_Hose
                $ R_Hose = 0
                "She rolls the [Line] down off her legs, leaving them in a small pile."     
                
            elif R_Over and not R_Chest and (R_Panties or HoseNum("Rogue") >= 10):      #will she lose the top when she's topless with panties?        
                if ApprovalCheck("Rogue", 1250, TabM = 3) or (R_SeenChest and ApprovalCheck("Rogue", 1000, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)   
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)                     
                    $ Line = R_Over                
                    $ R_Over = 0                     
                    if not R_SeenChest:
                        call RogueFace("bemused", 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3) 
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."   
                        call Rogue_First_Topless(1)        
                    else:               
                        "She pulls her [Line] over her head, tossing it to the ground."   
                else:
                    jump R_Strip_Ultimatum
                
            elif R_Chest and not R_Over:                                     # Will she lose the bra?
                if ApprovalCheck("Rogue", 1250, TabM = 3) or (R_SeenChest and ApprovalCheck("Rogue", 1000, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15) 
                    $ Line = R_Chest                
                    $ R_Chest = 0                     
                    if not R_SeenChest:
                        call RogueFace("bemused", 1)
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)    
                        call Rogue_First_Topless(1)
                    else:
                        call RogueFace("sexy")
                        "She pulls her [Line] over her head, tossing it to the ground."  
                else:
                    jump R_Strip_Ultimatum
            
            elif R_Legs:                                                        #will she lose the pants/skirt if she has no panties on?
                if ApprovalCheck("Rogue", 1350, TabM = 3) or (R_SeenPussy and ApprovalCheck("Rogue", 1100, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 75, 10)  
                    $ Line = R_Legs                
                    $ R_Legs = 0       
                    if not R_SeenPussy:
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 3)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 4)  
                        "She shyly looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."    
                        call Rogue_First_Bottomless(1)  
                    else:                            
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 75, 1)
                        "She unzips and pulls down her [Line], dropping them to the floor."   
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)       
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 85, 15)
                else:
                    jump R_Strip_Ultimatum
                
            elif R_Over and not R_Panties:                                         #will she lose the overshirt when she's bottomless under?
                if ApprovalCheck("Rogue", 1350, TabM = 3) or (R_SeenPussy and ApprovalCheck("Rogue", 1100, TabM = 3) and not Taboo):                  
                    $ Line = R_Over                
                    $ R_Over = 0                                 
                    if not R_SeenPussy:                
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 3)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 4) 
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                        call Rogue_First_Bottomless(1)                
                    else:
                        "She pulls her [Line] over her head, tossing it to the ground."     
                    if not R_Chest:
                        if not R_SeenChest:                
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)  
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                            call Rogue_First_Topless(1)
                        else:
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 15)                
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 75, 1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                    else:
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 75, 10)                
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 75, 1)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)                
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 85, 15)    
                else:
                    jump R_Strip_Ultimatum
            
            elif R_Chest:                                                               # Will she go topless?
                if ApprovalCheck("Rogue", 1250, TabM = 3) or (R_SeenChest and ApprovalCheck("Rogue", 1100, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5) 
                    $ Line = R_Chest                
                    $ R_Chest = 0                     
                    if not R_SeenChest:
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 4)               
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)  
                        "She hesitantly glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."                                      
                        call Rogue_First_Topless(1)
                    else:                
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                        "She pulls her [Line] over her head, tossing it to the ground."  
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)   
                else:
                    jump R_Strip_Ultimatum
                
            elif R_Panties:                                                                        # Will she go bottomless?
                if ApprovalCheck("Rogue", 1350, TabM = 3) or (R_SeenPussy and ApprovalCheck("Rogue", 1100, TabM = 3) and not Taboo):
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 75, 10) 
                    $ Line = R_Panties                
                    $ R_Panties = 0                     
                    if not R_SeenPussy:
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 3)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 4) 
                        "She shyly looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."  
                        call Rogue_First_Bottomless(1) 
                    else:                
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 75, 1)
                        "She  looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 85, 15)
                else:
                    jump R_Strip_Ultimatum
                
            else:    
                call RogueFace("sexy")
                ch_r "I'm afraid that's all I have on, [R_Petname]. . ."
                $ Count = 2
        
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 2)               #lust/Focus
        if "exhibitionist" in R_Traits:
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 2)
        $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 60, 3)
        if Trigger2 == "jackin":
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 2)
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 200, 5)
        
        if not P_Semen and P_Focus >= 50:
            $ P_Focus = 50
    
        if P_Focus >= 100 or R_Lust >= 100:                                     #If either of you could cum 
            
            if P_Focus >= 100:                                                  #You cum             
                call PR_Cumming
                if "angry" in R_RecentActions:  
                    return    
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                if not P_Semen and Trigger2 == "jackin":
                    "You're spitting dust here, maybe just watch quietly for a while."
                    $ Trigger2 = 0
            
                if P_Focus > 80:
                    jump R_Strip_End   
            
            if R_Lust >= 100:                                                   #and Rogue cums                    
                call R_Cumming
                if Situation == "shift" or "angry" in R_RecentActions:                    
                    $ Count = 0
                    jump R_Strip_End  
            call R_Pos_Reset        
            show Rogue at Rogue_Dance1()
            "Rogue begins to dance again."
        
        menu:
            extend ""
            "Keep Going. . . (locked)" if Count == 2 or "keepdancing" in R_RecentActions:
                pass
            "Keep Going. . ." if Count != 2 and "keepdancing" not in R_RecentActions:
                $ R_Eyes = "sexy"
                if R_Love >= 700 or R_Obed >= 500:
                    if not Tempmod:
                        $ Tempmod = 10
                    elif Count == 1 and Tempmod <= 20:
                        $ Tempmod += 1
                if Taboo and R_Strip <= 10:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 7)
                elif Taboo or R_Strip <= 10:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                elif R_Strip <= 50:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3) 
            "Keep Dancing. . ." if Count == 2:
                $ R_Eyes = "sexy"              
            "Just watch silently" if Count != 2:
                if "watching" not in R_RecentActions:
                    if Count != 2:
                        if Taboo and R_Strip <= 10:
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        elif Taboo or R_Strip <= 10:
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1) 
                    elif R_Strip <= 50:
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 2) 
                    $ R_RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin": #add Rogue reaction here.
                call R_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                $ Trigger2 = 0
            "Lose the gloves. . ." if R_Arms:
                call RogueFace("surprised")
                $ R_Mouth = "kiss"
                ch_r "All right, [R_Petname]."
                call RogueFace("sexy")
                $ R_Arms = 0          
            "Lose the gloves. . .(locked)" if not R_Arms:
                pass
            "Ok, that's enough.":
                jump R_Strip_End
                
    
    jump R_Stripping
    


label R_Strip_Ultimatum:  
    if "keepdancing" in R_RecentActions: 
        jump R_Stripping
        
#    call Set_The_Scene
    
#    show blackscreen onlayer black
#    hide Rogue
#    show Rogue at SpriteLoc(StageCenter) zorder RogueLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.6, 0.0)
    call R_Pos_Reset
#    hide blackscreen onlayer black
    call RogueFace("bemused", 1)        
    if "stripforced" in R_RecentActions: 
        call RogueFace("sad", 1)    
        ch_r "That's as far as I care to go, [R_Petname]."
    else:
        ch_r "I'm sorry, [R_Petname], I'm not ready to show you more. . . Yet."
    menu:
        extend ""
        "That's ok, you can stop.":                            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
        "That's ok, but keep dancing for a bit. . .":                            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
            $ R_RecentActions.append("keepdancing")
            call R_Pos_Reset        
            show Rogue at Rogue_Dance1()
            "Rogue begins to dance again."
            ch_r "Heh, ok [R_Petname]."
            jump R_Stripping
        "You'd better." if R_Forced:
            if not ApprovalCheck("Rogue", 500, "O", TabM=5) and not ApprovalCheck("Rogue", 800, "L", TabM=5):                    
                call RogueFace("angry")
                ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                ch_r "I think we're done here for now."  
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")  
                $ R_Action -= 1    
                $ R_SpriteLoc = StageRight 
                return                                
            $ Tempmod += 25
            $ R_Forced = 1
            call RogueFace("sad")
            if "stripforced" in R_RecentActions:                    
                call RogueFace("angry")
                ch_r ". . ."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40)
            else:
                ch_r "I. . . guess I could. . ."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40)
                $ R_RecentActions.append("stripforced")
            call R_Pos_Reset        
            show Rogue at Rogue_Dance1()
            "Rogue begins to dance again."
            jump R_Stripping
        "You can do better than that. Keep going." if not R_Forced:
            if not ApprovalCheck("Rogue", 300, "O", TabM=5) and not ApprovalCheck("Rogue", 700, "L", TabM=5):                   
                call RogueFace("angry")
                ch_r "I don't know who you think I am, but I ain't gonna just jump when you say \"toad\"."
                ch_r "I think we're done here for now."  
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")  
                $ R_Action -= 1    
                $ R_SpriteLoc = StageRight 
                return                
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 75, 5)
            $ Tempmod += 25
            $ R_Forced = 1
            call RogueFace("sad")
            ch_r "Well, if you insist. . ."
            call R_Pos_Reset        
            show Rogue at Rogue_Dance1()
            "Rogue begins to dance again."
            jump R_Stripping
                
label R_Strip_End:   
    ch_r "Ok, [R_Petname]. . . "
    $ R_Action -= 1    
    $ Count = 0
    $ R_SpriteLoc = StageRight 
    call R_Pos_Reset        
    return

# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

           

# Start Rogue Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label R_Undress(Region = "ask",CountStore=0):  
    call Shift_Focus("Rogue")           
    $ CountStore = Tempmod
    
    if Region == "auto":
        if R_Upskirt and R_PantiesDown:
            return
        if R_Legs == "pants":
            $ Tempmod = 20
        if R_Lust >= 90:
            $ Tempmod += 10      
        elif R_Lust >= 80:
            $ Tempmod += 5     
        elif R_Lust >= 70:
            $ Tempmod += 0 
        $ Situation = "auto"
        call Rogue_Bottoms_Off(0)
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if R_Over or R_Chest:    
                $ Region = "top"     
            "Her bottoms" if R_Legs or R_Panties or R_Hose:
                $ Region = "bottom"           
            "A little of both. . ." if R_Over or R_Chest or R_Legs or R_Panties or R_Hose: 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if R_Over or R_Chest:    
                call Rogue_Top_Off(0)  
    elif Region == "bottom":
        if R_Legs or R_Panties or R_Hose:
                call Rogue_Bottoms_Off(0)    
    elif Region == "both":        
            if R_Over or R_Chest:    
                    call Rogue_Top_Off(0) 
            $ Tempmod = CountStore 
            
            if "angry" in R_RecentActions: 
                    pass            
            elif not R_Legs and not R_Panties and not R_Hose:
                    pass                
            elif "no topless" in R_RecentActions:
                    menu:
                        ch_r "You might want to rethink your next question."
                        "And now the bottoms?":
                            call Rogue_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Rogue_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Rogue_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Rogue")
    
    if not R_Over and not R_Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in R_RecentActions:  
        ch_r "I'm just too annoyed to deal with this right now."
        return
    
    if R_SeenChest and ApprovalCheck("Rogue", 500) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if "no topless" in R_RecentActions: 
        $ Tempmod -= 10
            
   
    if Intro:
        if R_Over:
                ch_p "This might be easier without your [R_Over] on."
        elif R_Chest:
                ch_p "This might be easier without your [R_Chest] on."                   
    

    $ Approval = ApprovalCheck("Rogue", 1100, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto":     
        $ Line = 0
        if R_Over: # If she's in a top
            if R_Chest and ApprovalCheck("Rogue", 800, TabM = 1):
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 1)
            elif Approval >= 2 or (R_SeenChest and ApprovalCheck("Rogue", 500) and not Taboo):
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
            else:
                return
            $ Line = R_Over
            $ R_Over = 0
            "Rogue sighs in frustration, and pulls her [Line] over her head, throwing it aside."
            if not R_Chest:
                if Taboo:
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, (int(Taboo/20)))   
                call Rogue_First_Topless(1)
                
        if R_Chest:
            if Approval >= 2 or (R_SeenChest and ApprovalCheck("Rogue", 500) and not Taboo):
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
                if Taboo:
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, (int(Taboo/20))) 
                if Line:
                    $ Line = R_Chest
                    $ R_Chest = 0
                    "After that, she also tears off her [Line]."  
                else:
                    $ Line = R_Chest
                    $ R_Chest = 0
                    "Rogue sighs in frustration, and pulls off her [Line]."  

                call Rogue_First_Topless(1) 
                ch_r "I just wasn't getting much out of it that way."  
        return
    
    
    if Approval >= 2: #(R_Love + R_Obed + R_Inbt + (2*Tempmod) - (4*Taboo)) >= 1250:                              # Does she assume top off?            
        if "no topless" in R_DailyActions:
            ch_r "Ok, fine, top off."
        call RogueFace("sexy", 1)
        if R_Forced:
            call RogueFace("sad", 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)  
        $ Cnt = 1
        while (R_Chest or R_Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_r "So, [R_Petname]. Did you want me to take my top off?"  
                "Lose the [R_Over]." if R_Over:                 
                    call RogueFace("bemused", 1)                    
                    $ Line = R_Over
                    $ R_Over = 0
                    "Rogue pulls her [Line] off and tosses it aside."
                "Why don't you lose the [R_Neck]?" if R_Neck:
                    $ Line = R_Neck
                    $ R_Neck = 0
                    "Rogue pulls her [Line] off."                    
                "Just lose the [R_Chest]." if R_Over and R_Chest:
                    call RogueFace("bemused", 1)                    
                    $ Line = R_Chest
                    $ R_Chest = 0                 
                    "Rogue slowly removes her [Line] from under the [R_Over]."   
                "Lose the [R_Chest]." if not R_Over and R_Chest:
                    call RogueFace("bemused", 1)
                    $ Line = R_Chest
                    $ R_Chest = 0                 
                    "Rogue throws off her [Line]."   
                "Lose both tops." if R_Over and R_Chest:
                    call RogueFace("bemused", 1)
                    $ Line = R_Over
                    $ R_Over = 0
                    "Rogue tosses the [Line] over her head. . ."   
                    $ Line = R_Chest
                    $ R_Chest = 0 
                    ". . .and then the [Line] as well."                
                "That's enough. [[exit]":               
                    call RogueFace("bemused", 1)
                    ch_r "All right, [R_Petname]."    
                    $ Cnt = 0
        if not R_Chest and not R_Over:             
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            call Rogue_First_Topless  
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)        
        $ R_RecentActions.append("ask topless")                      
        $ R_DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Doesn't want to lose the top//////////////////////////////////  
                 
    call RogueFace("bemused", 1)       
    if Intro == "massage" and not Approval:
        ch_r "I'm ok with a massage, but my top stays on."
    elif "no topless" in R_RecentActions: 
        call RogueFace("angry")
        ch_r "I just told you no, [R_Petname]."    
    elif Approval and not R_SeenChest:
        ch_r "I'd like to leave something to the imagination. . ."    
    elif not R_SeenChest:
        ch_r "I'm not ready to show you those yet. . ."   
    elif "no topless" in R_DailyActions: 
        ch_r "I wasn't into it earlier, [R_Petname], what's changed?"           
    elif "ask topless" in R_RecentActions: 
        ch_r "Changed your mind, [R_Petname]?"       
    elif Taboo:
        ch_r "It's a bit exposed here. . ."          
    elif Approval:
        ch_r "Well, you've seen them before, but. . ."
    else:
        ch_r "Not right now."
        
    menu:
        ch_r "I'm keep'in my top on for now, [R_Petname]."
        "Sorry, sorry." if "no topless" in R_RecentActions:  
            call RogueFace("bemused", 1)   
            ch_r "Ok, just. . . give it a rest, huh?"
        "Ok, that's fine." if "no topless" not in R_RecentActions: 
            if "ask topless" not in R_DailyActions:
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
            if R_Forced:
                $ R_Mouth = "grimace"
                ch_r "I really appreciate that."
                if "ask topless" not in R_DailyActions:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, 2)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                                                                                                         
        "How about just the [R_Over]?" if R_Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Rogue", 800, TabM = 2) and R_Chest: #80, 160 taboo 
                call RogueFace("sexy") 
                ch_r "Well, that's no big deal I guess. . ."                 
                call RogueFace("bemused", 1)                
                $ Line = R_Over
                $ R_Over = 0
                "Rogue tosses the [Line] over her head."   
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
            elif not R_Chest:
                $ R_Eyes = "surprised"
                $ R_Blush = 2
                ch_r "I'm not exactly decent under this, you know." 
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ R_Mouth = "smile"
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                        ch_r "Great!"             
                    "That doesn't bother me any.":                                              #fix this
                        if ApprovalCheck("Rogue", 500, "I", TabM=3) or ApprovalCheck("Rogue", 1000, "LI", TabM=3):
                            call RogueFace("bemused", 1)
                            ch_r "Ooh, at least you know what you like"                               
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 2)                                                         
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
                            call RogueFace("sexy")   
                            $ Line = R_Over
                            $ R_Over = 0
                            "Rogue tosses the [Line] over her head."                            
                            $ R_Over = 0
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)  
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                            call Rogue_First_Topless   
                        else:   
                            call RogueFace("bemused")
                            call Rogue_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Rogue_ToplessorNothing
                $ R_Blush = 1        
            else:   
                call RogueFace("sexy")
                call Rogue_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo           
            if Approval and ApprovalCheck("Rogue", 600, "L", TabM=1):                 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 2)
                call RogueFace("sexy")    
                if "no topless" in R_RecentActions:  
                    ch_r "You're pretty persistent, [R_Petname]. I guess this time it'll be rewarded. . ."
                else:
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ." 
                if R_Over:
                    $ Line = R_Over
                    $ R_Over = 0
                    "Rogue tosses the [Line] over her head. . ."   
                    $ Line = R_Chest
                    $ R_Chest = 0 
                    ". . .and then the [Line] as well."
                else:                    
                    $ Line = R_Chest
                    $ R_Chest = 0 
                    "Rogue tosses her [Line] over her head."                      
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)  
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                call Rogue_First_Topless     
            elif "no topless" in R_RecentActions:
                call RogueFace("angry")
                ch_r "Nuh uh, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)   
                $ R_RecentActions.append("angry")   
                $ R_DailyActions.append("angry")
            else:   
                call RogueFace("sexy")
                call Rogue_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Rogue_ToplessorNothing
            
        "Never mind.":
            pass
    
    $ R_RecentActions.append("ask topless")                      
    $ R_DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Rogue_Top_Off_Refused:                    #When you insist but she refuses    
    call RogueFace("angry")
    if "no topless" in R_RecentActions:  
        ch_r "Get a clue, [R_Petname]."
    elif "no topless" in R_DailyActions:  
        ch_r "Give it a rest, [R_Petname]."
    else:
        call RogueFace("sad")
        ch_r "I'm afraid not this time, [R_Petname]. Sure we can't have some fun anyway?"
    menu:
        extend ""
        "Sure, never mind." if "no topless" not in R_RecentActions:
            call RogueFace("sexy")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
            ch_r "Great!"  
        "Sorry, I'll drop it." if "no topless" in R_RecentActions:   
            ch_r "Fine. . ."  
        "No, let's do something else.":
            $R_Brows = "confused"
            ch_r "Ok [R_Petname], your loss."
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2, 1)
            if "no topless" not in R_RecentActions:
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 4)    
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
    $ R_RecentActions.append("no topless")                      
    $ R_DailyActions.append("no topless") 
    return
              

label Rogue_ToplessorNothing:
    call RogueFace("angry")
    if ApprovalCheck("Rogue", 800, "OI", TabM = 4) and ApprovalCheck("Rogue", 400, "O", TabM = 3):        
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)
        if "no topless" in R_RecentActions:             
            ch_r "Ok, ok, whatever."                 
        else:
            call RogueFace("sad")
            ch_r "Fine, if that's what you want."                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 4)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
        if R_Over:
            $ Line = R_Over
            $ R_Over = 0
            "Rogue haltingly pulls the [Line] over her head. . ."
            if R_Chest:
                $ Line = R_Chest
                $ R_Chest = 0 
                ". . .and then the [Line] as well."
        elif R_Chest:
            $ Line = R_Chest
            $ R_Chest = 0 
            "Rogue haltingly pulls the [Line] over her head. . ."
        call Rogue_First_Topless                       
    else:  
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, -1, 1)
        if "no topless" in R_RecentActions: 
            ch_r "Seriously, cut this shit out."      
        else:
            $R_Brows = "confused"
            ch_r "\"Nothing\" it is then."   
        $ R_RecentActions.append("no topless")                      
        $ R_DailyActions.append("no topless")     
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    return              
    
label Rogue_First_Topless(Silent = 0, TempLine=0):          
    $ R_RecentActions.append("topless")                      
    $ R_DailyActions.append("topless")
    call DrainWord("Rogue","no topless")    
    $ R_SeenChest += 1 
    if R_SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20)  
    if not Silent:
        call RogueFace("bemused", 1)
        "Rogue looks a bit shy, and slowly lowers her hands from her chest."
        ch_r "Well, [R_Petname]? Like what you see?"    
        menu:
            extend ""
            "Nod":            
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20)               
                call RogueFace("smile")
                ch_r ". . ."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 40, 20)
            "Whatever.":        
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -10)                          
                call RogueFace("angry")
                ch_r "Hmph!"
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            "Well, that aren't that bad. . .":        
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 25)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -15)                          
                call RogueFace("confused",2)
                ch_r "Say what now?"
                menu:      
                    "I, um, no, they're great!":                        
                        call RogueFace("angry",2, Mouth="smile")
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 10)   
                        ch_r "Of couse they are!"            
                    "[EmmaName]'s were bigger, that's all." if E_SeenChest:                            
                        $ TempLine = "Emma"
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                        
                if TempLine:
                        call RogueFace("angry")
                        $ R_Mouth = "surprised"                        
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -10)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 30)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -25) 
                        ". . ."
                        $ R_Mouth = "sad"
                        if TempLine == "Emma":
                                if R_LikeEmma >= 800:
                                    call RogueFace("sly",2,Eyes="side")
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                    ch_r "Well, I mean they would be quite the handful. . ."       
                                    $ R_LikeEmma += 20 
                                elif R_LikeEmma >= 700:
                                    $ R_Eyes = "side" 
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                    ch_r "I mean, I guess, if you like that kind of thing. . ."
                                else:                        
                                    $ R_LikeEmma -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if R_LikeKitty >= 800:
                                    call RogueFace("sly",2,Eyes="side")
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                    ch_r "They are kind of adorable. . ."       
                                    $ R_LikeKitty += 20 
                                elif R_LikeKitty >= 700:
                                    $ R_Eyes = "side" 
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                    ch_r "I mean, yeah, I guess. . ."    
                                else:                        
                                    $ R_LikeKitty -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
                                ch_r "Yeah, that's enough outta you, [R_Petname]."   
                                call RogueOutfit
                                $ R_RecentActions.append("no topless")                      
                                $ R_DailyActions.append("no topless")  
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")  
    else:
        if ApprovalCheck("Rogue", 500) and not R_Forced:
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20) 
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)              
            call RogueFace("smile")
        else:        
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -10)                          
            call RogueFace("angry")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Rogue_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Rogue")
    
    if not R_Legs and not R_Panties and not R_Hose:                                  # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in R_RecentActions:  
        ch_r "I'm just too annoyed to deal with this right now."
        return
    
    # Will she take her bottoms off Modifiers
    if R_SeenPussy and ApprovalCheck("Rogue", 700): #You've seen her Pussy.
        $ Tempmod += 20
    elif not R_Panties:
        $ Tempmod -= 20
    elif R_SeenPanties and ApprovalCheck("Rogue", 500): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in R_Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in R_Traits or "sex friend" in R_Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if "no bottomless" in R_RecentActions: 
        $ Tempmod -= 20
        
    if Intro:
        if R_Legs:
                ch_p "This might be easier without your [R_Legs] on."
        elif R_Panties:
                ch_p "This might be easier without your [R_Panties] on."
        
    $ Approval = ApprovalCheck("Rogue", 1200, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
        $ Cnt = 0
        
        if not R_Upskirt:                     
            if R_Legs == "skirt":                                          #If she's in a skirt with panties, hike it up?
                if Approval >= 2 or (R_SeenPussy and not Taboo):
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                    if Taboo:
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, (int(Taboo/20)))                 
                    $ R_Upskirt = 1
                    "She slides her skirt up."
                    $ Cnt = 1 
                    
            if R_Legs == "pants" or HoseNum("Rogue") >= 5:            
                if R_Panties:                                               #she has pants and panties on
                    if not Approval or (not R_SeenPanties and Taboo):
                        return   
                elif Approval < 2 or (not R_SeenPussy and Taboo):
                    return     
                elif R_Legs == "pants" and R_Upskirt:  
                    return
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                $ R_Upskirt = 1
                $ Line = R_Hose
                if R_Panties:
                    if R_Legs == "pants": 
                        "Rogue grumbles to herself, and then unzips her jeans, sliding them down her legs." 
                    else: #HoseNum("Rogue") >= 5
                        "Rogue grumbles to herself, and then pulls her [R_Hose] down her legs." 
                    $ R_SeenPanties = 1
                else:
                    if R_Legs == "pants":
                        "Rogue grumbles to herself, and then unzips her jeans, sliding them off her bare ass." 
                    else: #HoseNum("Rogue") >= 5 
                        "Rogue grumbles to herself, and then pulls her [R_Hose] down her bare ass." 
                    call Rogue_First_Bottomless(1)  
                    
                if Taboo:
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, (int(Taboo/10)))  
                $ Cnt = 1 
            
        if R_Panties and not R_PantiesDown:                                              # Just wearing panties, lose them?
            if Approval >= 2 or (R_SeenPussy and not Taboo):
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
                if Taboo:
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, (int(Taboo/10)))  
                $ R_PantiesDown = 1
                if Cnt:
                    "Rogue tsks in irritation, and pulls down her [R_Panties] too."
                else:
                    "Rogue tsks in irritation, and pulls down her [R_Panties]." 
                call Rogue_First_Bottomless(1) 
                    
                ch_r "I wasn't getting anything out of it with those on. Give it another go."  
        return
            
    
    if Approval >= 2:                 #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
        call RogueFace("sexy", 1)
        if R_Forced:
            call RogueFace("sad", 1)              
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        if Approval >= 3:
            $ Line = "Hmmm, what do you want to see? . ."
        else:    
            $ Line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ." 
        
        call Rogue_Bottoms_Off_Legs
            
        if not R_Panties and Action_Check("Rogue", "recent", "bottomless") < 2: 
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
    
  
        
    elif R_Legs or R_Panties or R_Hose:                                                      # She'd rather not strip but might        
        call RogueFace("bemused", 1) 
        if "no bottomless" in R_RecentActions: 
            call RogueFace("angry")
            ch_r "What did I just tell you, [R_Petname]?"   
        elif "no topless" in R_RecentActions: 
            call RogueFace("angry")
            ch_r "I doubt your odds will be better here, [R_Petname]. . ."  
        elif Approval and not R_SeenPussy:
            ch_r "Not everything, right?"  
        elif not R_SeenPussy and "ask topless" in R_RecentActions:
            ch_r "I'm not ready to show you that either."    
        elif not R_SeenPussy:
            ch_r "I'm not ready to show you all that yet."   
        elif "no bottomless" in R_DailyActions: 
            ch_r "Have you forgot what I said earlier, [R_Petname]?"   
        elif Taboo:
            ch_r "I don't know about doing it here. . ."  
        elif Approval:
            ch_r "I don't know if I want to take my bottoms off. . ."   
        elif R_SeenPussy:
            ch_r "Well, you've seen it before, but. . ."            
        else:
            ch_r "I'm not taking my bottoms off."
        menu:            
            extend ""
            "Ok, never mind." if "no bottomless" not in R_RecentActions:  
                if "ask bottomless" not in R_DailyActions:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 2)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                if R_Forced:
                    $ R_Mouth = "smile"
                    ch_r "I really appreciate that."
                    if "ask bottomless" not in R_DailyActions:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, 3)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
                    
            "Sorry, sorry." if "no bottomless" in R_RecentActions:  
                ch_r "Ok, fine, just chill out about it."
             
            "Come on, Please?":   
                    if "no bottomless" in R_DailyActions:    
                            call RogueFace("angry", 1)
                            ch_r "Listen up when I tell you \"no.\""
                    else:                      
                        if Approval and ApprovalCheck("Rogue", 600, "L", TabM=1):   
                            call RogueFace("sexy", 1)
                            $ D20 = renpy.random.randint(1, 3)
                            $ Approval += 1 if D20 == 3 else 0
                            $ Line = "Well, what were you thinking then. . ."
                            call Rogue_Bottoms_Off_Legs  
                        else:    
                            call RogueFace("sexy")
                            call Rogue_Bottoms_Off_Refused
                                    
            "It doesn't have to be everything. . ." if R_Legs or HoseNum("Rogue") >= 10 or R_Panties == "shorts":    
                if Approval and "no bottomless" not in R_DailyActions:                   
                    call RogueFace("bemused", 1)
                    $Line = "Well, Maybe. . . What were you thinking?"
                    call Rogue_Bottoms_Off_Legs  
                else:    # She refuses your request. . .
                    call RogueFace("sexy")
                    call Rogue_Bottoms_Off_Refused                       
            "It doesn't have to be everything. . . (locked)" if not R_Legs and HoseNum("Rogue") < 10 and R_Panties != "shorts":   
                    pass
                            
            "No, lose 'em.":            #85 and -200 taboo             
                if (Approval and R_Obed >= 250) or (ApprovalCheck("Rogue", 850, "OI", TabM = 5) and ApprovalCheck("Rogue", 400, "O")):                    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -1, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)
                    $ Line =  "Fine, if that's what you want. What do you want to see?"  
                    $ Approval = 1 if Approval < 1 else Approval
                    $ R_Forced = 1
                    call Rogue_Bottoms_Off_Legs                     
                else:          
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    if ApprovalCheck("Rogue", 400, "O"):
                        ch_r "I. . . I really can't." 
                    else:
                        call RogueFace("angry")
                        ch_r "Well fuck off then!"                          
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
                    $ R_RecentActions.append("no bottomless")                      
                    $ R_DailyActions.append("no bottomless")   
    
    $ Tempmod = 0
    $ R_RecentActions.append("ask bottomless")                      
    $ R_DailyActions.append("ask bottomless")     
    return           

label Rogue_Bottoms_Off_Legs:    
    
    if R_Forced:        
        call RogueFace("sad", 1)
    elif ApprovalCheck("Rogue", 1100, "OI", TabM = 3):        
        call RogueFace("sly")
    elif ApprovalCheck("Rogue", 1400, TabM = 3):  
        call RogueFace("sexy", 1) 
    else:
        call RogueFace("bemused", 1) 
        
    $ Line = "Well what did you want off?" if not Line else Line
    $ Cnt = 1
    while Cnt and (R_Legs or R_Panties or R_Hose):
        menu:                                       
            # She's asking what you'd like to see.
            ch_r "[Line]"
            "Everything. . ." if Line != "Well, Maybe. . . What were you thinking?": #approval a given
                        
                    if Approval < 2 and not R_Panties and HoseNum("Rogue") < 10:
                        call Rogue_NoPanties
                    
                    if R_Legs:
                        $ Line = R_Legs      
                        $ R_Legs = 0
                        if not R_SeenPanties:
                            "Rogue shyly removes her [Line]."
                            $ R_SeenPanties = 1
                        else:
                            "Rogue pulls her [Line] off." 
                    
                    if Approval < 2 and not R_Panties and HoseNum("Rogue") >= 10:
                        call Rogue_NoPanties   
                        
                    if R_Hose:
                        $ Line = R_Hose #HoseName 
                        $ R_Hose = 0
                        "She pulls her hose down."
                           
                    if Approval < 2:
                        call Rogue_NoPanties   
                        
                    if R_Panties:                               
                        $ Line = R_Panties   
                        $ R_Panties = 0  
                        "She glances up at you as she removes her [Line]." 
                    call Rogue_First_Bottomless   
                    
                    
            "Lose the [R_Legs]." if R_Legs: 
                    if R_Panties and Approval >= 2:
                        call RogueFace("sexy")
                        ch_r "I guess I could do that. . ."
                    elif Approval:          
                        call RogueFace("sexy", 1)    
                        if Approval < 2 and not R_Panties and HoseNum("Rogue") < 10:
                            call Rogue_NoPanties
                    else:    
                        call RogueFace("sexy")
                        call Rogue_Bottoms_Off_Refused
                        return
                        
                    $ Line = R_Legs      
                    $ R_Legs = 0
                    if not R_Panties and HoseNum("Rogue") < 10:
                        call RogueFace("sly", 2)  
                        "She blushes and looks at you slyly before removing her [Line]." 
                        call Rogue_First_Bottomless   
                    elif not R_SeenPanties:
                        "Rogue shyly removes her [Line]."
                        $ R_SeenPanties = 1
                    else:
                        "Rogue pulls her [Line] off." 
                    call RogueFace("bemused", 1)
            
            
            "Lose the [R_Panties]." if R_Panties:
                    if Approval < 2:
                        ch_r "No thanks, [R_Petname]."                        
                        $ R_RecentActions.append("no bottomless")                      
                        $ R_DailyActions.append("no bottomless")   
                        return                        
                    elif R_Legs == "pants" or HoseNum("Rogue") >= 5:
                        ch_r "A little backwards, but sure. . ."
                    else:
                        ch_r "Ok, sure, [R_Petname]."                                            
                    $ Line = R_Panties   
                    $ R_Panties = 0  
                    if R_Legs == "pants":
                        "She pulls her pants off, then removes her [Line], before putting them back on."                        
                    elif HoseNum("Rogue") >= 5:
                        "She pulls her [R_Hose] off, then removes her [Line], before putting them back on."   
                    elif R_Legs:                            
                        "She reaches under her [R_Legs] and pulls her [Line] down."
                    else:
                        "She glances up at you as she removes her [Line]."
                    if not R_Legs:
                        call Rogue_First_Bottomless  
            
            "Lose the [R_Hose]." if R_Hose:
                    call RogueFace("bemused", 1) 
                    if R_Legs:
                        ch_r "Ok, no problem."                         
                    elif Approval < 2 and not R_Panties and HoseNum("Rogue") >= 10:
                        call Rogue_NoPanties                            
                    elif not Approval and HoseNum("Rogue") >= 5:
                        ch_r "No thanks, [R_Petname]."
                        return                            
                    else:
                        ch_r "Ok, sure, [R_Petname]."                 
                        
                    $ Line = R_Hose   
                    $ R_Hose = 0  
                    if R_Legs:
                        "She reaches under her [R_Legs] and pulls her [Line] down."
                    elif HoseNum("Rogue") < 10:
                        "Rogue pulls her [Line] off." 
                    elif not R_Panties:
                        call RogueFace("sly", 2)  
                        "She blushes and looks at you slyly before removing her [Line]." 
                        $ R_Blush = 1
                        call Rogue_First_Bottomless   
                    elif not R_SeenPanties:
                        "Rogue shyly removes her [Line]."
                        $ R_SeenPanties = 1
                    else:
                        "Rogue pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = "Anything else?"
    return


label Rogue_NoPanties: #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if R_Legs or HoseNum("Rogue") >= 10:
        ch_r "Well, I'm not exactly decent under here, you know. . ."  
    else:
        ch_r "This is the last bit. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Rogue", 1000, "LI", TabM=1):                                             
                ch_r "Well, if you're gonna ask so nicely. . . "
            else:
                ch_r "Sorry, I don't think so."
                call Rogue_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Rogue", 800, "OI", TabM=1):
                ch_r "Fine, whatever."  
            else:
                call Rogue_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Rogue_Bottoms_Off_Refused:     
    if "no bottomless" in R_RecentActions:  
        ch_r "What part of \"no\" escapes you, [R_Petname]?"
    elif "no bottomless" in R_DailyActions:  
        ch_r "If you keep this up, not ever, [R_Petname]."
    else:
        call RogueFace("sad")
        if Cnt == 2:            
            ch_r "That's enough, [R_Petname]. Sure we can't have some fun anyway?" 
        else:
            ch_r "I'm afraid not this time, [R_Petname]. Sure we can't have some fun anyway?"        
    menu:
        extend ""
        "Sure, never mind." if "no bottomless" not in R_RecentActions:
            $ R_Mouth = "smile"
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)    
            ch_r "Great!"    
        "Sorry, I'll drop it." if "no bottomless" in R_RecentActions:   
            ch_r "Fine. . ."  
        "No, let's do something else.":
            $R_Brows = "confused"
            ch_r "Ok [R_Petname], your loss."               
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 5)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2, 1)
            if "no bottomless" not in R_RecentActions:  
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 4)      
            $ R_RecentActions.append("angry")
            $ R_DailyActions.append("angry")   
            
    $ R_RecentActions.append("no bottomless")                      
    $ R_DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   
    
label Rogue_First_Bottomless(Silent = 0): 
    $ R_RecentActions.append("bottomless")                      
    $ R_DailyActions.append("bottomless")
    call DrainWord("Rogue","no bottomless")
    $ R_SeenPussy += 1 
    if R_SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 40)     
    if not Silent:
        call RogueFace("bemused", 1)
        "Rogue shyly moves her hands aside, revealing her pussy."        
        menu:        
            ch_r "Well, [R_Petname]? Was it worth the wait?"
            "Lovely. . .":            
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 30)            
                call RogueFace("smile")          
                ch_r ". . ."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 40, 20)
            "I suppose.":        
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -20)
                call RogueFace("angry")           
                ch_r ". . ."
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
    else:
        if ApprovalCheck("Rogue", 500):
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 30)          
            call RogueFace("smile")          
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 40, 20)
        else:        
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, -10)
            call RogueFace("angry")          
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
    return
    
# End Rogue Undressing  ///////////////////////////////////////////////////////////////////


label Rogue_First_Peen(Silent = 0, Undress = 0): #checked each time she sees your cock  ## call Rogue_First_Peen(0,1)
    if not renpy.showing("Chibi_UI"):
                show Chibi_UI
    if "cockout" in P_RecentActions and "peen" in R_RecentActions: #If the cock is already out and she's seen it, return
            return
            
    $ R_RecentActions.append("peen")                      
    $ R_DailyActions.append("peen")
    $ R_SeenPeen += 1                      
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1)
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:
        if "cockout" in P_RecentActions:
                call RogueFace("down", 2)  
                "Rogue glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        if not ApprovalCheck("Rogue", 800) and not ApprovalCheck("Rogue", 500, "I"):
                call RogueFace("surprised", 2)  
                ch_r "What the hell?"
                call RogueFace("angry", 1)  
                $ R_RecentActions.append("angry")
                $ R_DailyActions.append("angry")  
                if R_SeenPeen == 1: 
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 30)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 20)
                else:                    
                    ch_r "What is {i}wrong{/i} with you?"
                    if Action_Check("Rogue", "daily", "peen") >= 2:
                            #if she's seen more than one peen today         
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -1)     
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
                    else:
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)                
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 10)  
        elif (Taboo and not ApprovalCheck("Rogue", 1500) or R_SEXP < 10) and bg_current != "bg showerroom":
                call RogueFace("surprised", 2)  
                ch_r "What are you- you should really put that thing away!"
                call RogueFace("bemused", 1)  
                if R_SeenPeen == 1: 
                    ch_r "I mean. . . no, definitely put that away!"
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 30)  
                    
        elif R_SeenPeen > 10:
                return    
        elif ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "L"):
                call RogueFace("sly",1) 
                if R_SeenPeen == 1: 
                    call RogueFace("surprised",2)  
                    ch_r "Whoa, I didn't know they looked so big up close."
                    call RogueFace("bemused",1)  
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5) 
                elif R_SeenPeen == 2:  
                    ch_r "That thing sure is impressive."               
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5) 
                elif R_SeenPeen == 5: 
                    ch_r "I certainly appreciate that guy."
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)  
                elif R_SeenPeen == 10: 
                    ch_r "I never get tired of seeing that."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)  
        else:
                call RogueFace("sad",1) 
                if R_SeenPeen == 1: 
                    call RogueFace("perplexed",1 ) 
                    ch_r "Well, I guess that's impressive. What do you plan to do with it?"
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)  
                elif R_SeenPeen < 5: 
                    call RogueFace("sad",0) 
                    ch_r "Yeah, I've seen it."
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                elif R_SeenPeen == 10: 
                    ch_r "I'm getting tired of seeing that."               
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if R_SeenPeen > 10:
                    return
                elif ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "L"):
                        if R_SeenPeen == 1: 
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5) 
                        elif R_SeenPeen == 2:              
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5) 
                        elif R_SeenPeen == 5: 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)  
                        elif R_SeenPeen == 10: 
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)  
                else:
                        if R_SeenPeen == 1: 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)  
                        elif R_SeenPeen < 5: 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                        elif R_SeenPeen == 10:              
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5) 
                            
    if R_SeenPeen == 1:            
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15)                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 20)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 20) 
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)
    
    return
    # End Rogue shown peen
        
    

transform Rogue_Dance1():     
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