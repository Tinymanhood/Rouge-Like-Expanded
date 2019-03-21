# start Strip Tease /////////////////////////////////////////////////////////////////////////////

label Laura_Stripping: 
        #This gets called by Group_Stripping, and returns there at the end. 
        if "stopdancing" in newgirl["Laura"].RecentActions: 
            #if she's just standing around, cut back to the other girl        
            if "stopdancing" in K_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End             
            if "stopdancing" in R_RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End                  
            if "stopdancing" in newgirl["Laura"].RecentActions: 
                    $ renpy.pop_call()
                    jump Group_Strip_End    
            return
    
        $ newgirl["Laura"].Girl_Arms = 2
        call LauraLust(1) #sets her lusty face           
        if "keepdancing" not in newgirl["Laura"].RecentActions:  
                # if Count isn't 2, it loops. 
#                if newgirl["Laura"].Arms and not newgirl["Laura"].Over:          
#                        #will she lose the wristbands? Yes, yes she'll lose the gloves. They're gloves. 
#                        $ newgirl["Laura"].Arms = 0
#                        "She pulls her gloves off, and tosses them to the ground."  
                   
                if newgirl["Laura"].Over and newgirl["Laura"].Chest and (newgirl["Laura"].Panties or newgirl["Laura"].Legs or HoseNum("Laura") >= 10):          
                        #will she lose the overshirt when she's dressed under?
                        if ApprovalCheck("Laura", 750, TabM = 3):
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 25, 1)                 
                                $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 3)
                                $ Line = newgirl["Laura"].Over
                                $ newgirl["Laura"].Over = 0
                                "She pulls her [Line] off and throws it behind her."  
                        else:
                                jump Laura_Strip_Ultimatum
                                    
                elif newgirl["Laura"].Legs and (newgirl["Laura"].Panties or HoseNum("Laura") >= 10):                              
                        #will she lose the pants/skirt if she has panties on?
                        if ApprovalCheck("Laura", 1000, TabM = 3) or (newgirl["Laura"].SeenPanties and not Taboo):
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 5)                
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)                
                                $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 5)
                                $ Line = newgirl["Laura"].Legs         
                                $ newgirl["Laura"].Legs = 0      
                                "She unzips and pulls down her [Line], dropping them to the floor."   
                                if not newgirl["Laura"].SeenPanties:
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)                              
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 3)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 2)
                                        $ newgirl["Laura"].SeenPanties = 1                
                        else:
                                jump Laura_Strip_Ultimatum          
                
                elif newgirl["Laura"].Boots: 
                        # Will she lose the boots?
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 2)
                        $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 2)
                        $ newgirl["Laura"].Boots = 0
                        "She unzips her boots and tosses them aside."  
                                    
                elif newgirl["Laura"].Hose: 
                        # Will she lose the hose?
                        if HoseNum("Laura") >= 10:
                                if ApprovalCheck("Laura", 1200, TabM = 3):
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 6)
                                        $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 6)
                                else:    
                                        jump Laura_Strip_Ultimatum
                                
                        elif HoseNum("Laura") >= 6 and ApprovalCheck("Laura", 1200, TabM = 3):
                                if ApprovalCheck("Laura", 1200, TabM = 3):
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 4)
                                        $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 4)
                                else:    
                                        jump Laura_Strip_Ultimatum
                        else:
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 3)
                                $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 3)
                        $ Line = newgirl["Laura"].Hose
                        $ newgirl["Laura"].Hose = 0
                        "She rolls the [Line] down off her legs, leaving them in a small pile."     
                    
                elif newgirl["Laura"].Over and not newgirl["Laura"].Chest and (newgirl["Laura"].Panties or HoseNum("Laura") >= 10):     
                    #will she lose the top when she's topless with panties?        
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (newgirl["Laura"].SeenChest and not Taboo):
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)                
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 10)   
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)     
                            $ Line = newgirl["Laura"].Over
                            $ newgirl["Laura"].Over = 0                       
                            if not newgirl["Laura"].SeenChest:
                                    call LauraFace("bemused", 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 4)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 3)    
                                    "She hesitantly glances down, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Laura_First_Topless       
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground."     
                    else:
                            jump Laura_Strip_Ultimatum
                    
                elif newgirl["Laura"].Chest and not newgirl["Laura"].Over:                                     
                    # Will she lose the bra?
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (newgirl["Laura"].SeenChest and not Taboo):
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)                
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)     
                            $ Line = newgirl["Laura"].Chest
                            $ newgirl["Laura"].Chest = 0   
                            if not newgirl["Laura"].SeenChest:
                                    call LauraFace("bemused", 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 4)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 3)          
                                    "She hesitantly glances down, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Laura_First_Topless
                            else:
                                    call LauraFace("sexy")
                                    "She pulls her [Line] over her head, tossing it to the ground."      
                    else:
                            jump Laura_Strip_Ultimatum
            
                elif newgirl["Laura"].Legs:                                                       
                    #will she lose the pants/skirt if she has no panties on?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (newgirl["Laura"].SeenPussy and not Taboo):
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 75, 10)    
                            $ Line = newgirl["Laura"].Legs
                            $ newgirl["Laura"].Legs = 0                       
                            if not newgirl["Laura"].SeenPussy:
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 4)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 4)  
                                    "She looks up at you, and then slowly unzips and pulls down her [Line], dropping them to the floor."   
                                    call Laura_First_Bottomless 
                            else:                            
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 75, 1)
                                    "She unzips and pulls down her [Line], dropping them to the floor."   
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)           
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 85, 15)
                    else:
                            jump Laura_Strip_Ultimatum
                    
                elif newgirl["Laura"].Over and not newgirl["Laura"].Panties:                                        
                    #will she lose the overshirt when she's bottomless under?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (newgirl["Laura"].SeenPussy and not Taboo):    
                            $ Line = newgirl["Laura"].Over
                            $ newgirl["Laura"].Over = 0               
                            if not newgirl["Laura"].SeenPussy:                
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 4)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 4) 
                                    "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground."
                                    call Laura_First_Bottomless                
                            else:
                                    "She pulls her [Line] over her head, tossing it to the ground." 
                            if not newgirl["Laura"].Chest:
                                    if not newgirl["Laura"].SeenChest:                
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)  
                                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                            call Laura_First_Topless
                                    else:
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 15)                
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                              
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 75, 1)
                                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                            else:
                                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 75, 10)                
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 75, 1)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)                
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 85, 15)    
                    else:
                            jump Laura_Strip_Ultimatum
                
                elif newgirl["Laura"].Chest:                                                               
                    # Will she go topless?
                    if ApprovalCheck("Laura", 1200, TabM = 3) or (newgirl["Laura"].SeenChest and not Taboo):
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                            $ Line = newgirl["Laura"].Chest
                            $ newgirl["Laura"].Chest = 0              
                            if not newgirl["Laura"].SeenChest:
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 4)               
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 3)  
                                    "She glances your way, and then with a shrug pulls her [Line] over her head, tossing it to the ground." 
                                    call Laura_First_Topless
                            else:                
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                    "She pulls her [Line] over her head, tossing it to the ground."  
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 80, 15)   
                    else:
                            jump Laura_Strip_Ultimatum
                    
                elif newgirl["Laura"].Panties:                                                                       
                    # Will she go bottomless?
                    if ApprovalCheck("Laura", 1350, TabM = 3) or (newgirl["Laura"].SeenPussy and not Taboo):
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 75, 10) 
                            $ Line = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Panties = 0               
                            if not newgirl["Laura"].SeenPussy:
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 4)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 4) 
                                    "She looks up at you, and then slowly pulls her [Line] down, kicking them off to the side."   
                                    call Laura_First_Bottomless
                            else:                
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 75, 1)
                                    "She looks up at you, and then gently pulls her [Line] down, kicking them off to the side."                  
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                            $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 85, 15)
                    else:
                            jump Laura_Strip_Ultimatum
                    
                else:    
                    if newgirl["Laura"].Neck or newgirl["Laura"].Arms:                        
                        $ newgirl["Laura"].Neck = 0
                        $ newgirl["Laura"].Arms = 0
                        "She tosses the rest aside."
                    call LauraFace("sexy")
                    ch_l "Well, that's all I've got, [newgirl[Laura].Petname]. . ."
                    menu:
                            extend ""
                            "Ok, you can stop":
                                    $ newgirl["Laura"].RecentActions.append("stopdancing")  
                                    call Laura_Pos_Reset        
                            "Keep on dancing":
                                    $ newgirl["Laura"].RecentActions.append("keepdancing")
        # end "nude" not in newgirl["Laura"].RecentActions loop
                
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 2)               #lust/Focus
        if "exhibitionist" in newgirl["Laura"].Traits:
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 2)
        $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 3)
        if Trigger2 == "jackin":
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 2)
                $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 200, 5)
        
        if not P_Semen and P_Focus >= 50:
                $ P_Focus = 50

        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100:                                     
                #If either of you could cum 
                
                if P_Focus >= 100:                                                  
                    #You cum             
                    call PLaura_Cumming
                    if "angry" in newgirl["Laura"].RecentActions:  
                        return    
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                    if not P_Semen and Trigger2 == "jackin":
                        "You're spitting dust here, maybe just watch quietly for a while."
                        $ Trigger2 = 0
                
                    if P_Focus > 80:
                        jump Group_Strip_End   
                    
                if newgirl["Laura"].Lust >= 100:                                                  
                    #and Laura cums                    
                    call Laura_Cumming
                    if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:                    
                        $ Count = 0
                        jump Group_Strip_End  
                        
                call AllReset("Laura")
                show Laura_Sprite at Laura_Dance1()
                "Laura begins to dance again."
            
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")
        menu:
            "Laura should. . ."
            "Keep Dancing. . ." if "keepdancing" in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].Eyes = "sexy"      
            "Keep Going. . ." if "keepdancing" not in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].Eyes = "sexy"
                    if newgirl["Laura"].Love >= 700 or newgirl["Laura"].Obed >= 500:
                        if not Tempmod:
                            $ Tempmod = 10
                        elif Tempmod <= 20:
                            $ Tempmod += 1
                    if Taboo and newgirl["Laura"].Strip <= 10:
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                    elif Taboo or newgirl["Laura"].Strip <= 10:
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 5)
                    elif newgirl["Laura"].Strip <= 50:
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3) 
                    "She continues to dance."  
                           
            "Stop stripping, keep dancing" if "keepdancing" not in newgirl["Laura"].RecentActions:
                    ch_l "Huh? I guess. . ."
                    $ newgirl["Laura"].RecentActions.append("keepdancing")
                
            "Start stripping again" if "keepdancing" in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].RecentActions.remove("keepdancing")
                    if "stripforced" in newgirl["Laura"].RecentActions: 
                            ch_l ". . ."
                    else:
                            ch_l "Hmm. . ."
                    jump Laura_Stripping
                
            "Just watch silently":
                if "watching" not in newgirl["Laura"].RecentActions:
                    if "keepdancing" not in newgirl["Laura"].RecentActions:
                        if Taboo and newgirl["Laura"].Strip <= 10:
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
                        elif Taboo or newgirl["Laura"].Strip <= 10:
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1) 
                    elif newgirl["Laura"].Strip <= 50:
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 2) 
                    $ newgirl["Laura"].RecentActions.append("watching")  
            
            "Start jack'in it." if Trigger2 != "jackin":
                    call Laura_Jackin                   
            "Stop jack'in it." if Trigger2 == "jackin":
                    $ Trigger2 = 0
            "Ok, that's enough.":
                    ch_l "Alright, [newgirl[Laura].Petname]. . . "
                    $ renpy.pop_call()
                    jump Group_Strip_End
                    
        
        return
    


label Laura_Strip_Ultimatum:  
    if "keepdancing" in newgirl["Laura"].RecentActions: 
        return
               
    call Laura_Pos_Reset
    call LauraFace("bemused", 1)        
    if "stripforced" in newgirl["Laura"].RecentActions: 
        call LauraFace("sad", 1)    
        ch_l "Last call, [newgirl[Laura].Petname]."
    else:
        ch_l "Ok, that's enough, [newgirl[Laura].Petname]. . . for now."
    menu:
        extend ""
        "That's ok, you can stop.":    
                if "ultimatum" not in newgirl["Laura"].DailyActions:                             
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 2)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                        $ newgirl["Laura"].DailyActions.append("ultimatum")
                $ newgirl["Laura"].RecentActions.append("stopdancing")
                return
        "That's ok, but keep dancing for a bit. . .":  
                if "ultimatum" not in newgirl["Laura"].DailyActions:                          
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 2)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                        $ newgirl["Laura"].DailyActions.append("ultimatum")
                $ newgirl["Laura"].RecentActions.append("keepdancing")
                if "stripforced" in newgirl["Laura"].RecentActions: 
                        ch_l ". . ."
                else:
                        ch_l "Eh? Fine."
        "You'd better." if newgirl["Laura"].Forced:
            if not ApprovalCheck("Laura", 500, "O", TabM=5) and not ApprovalCheck("Laura", 800, "L", TabM=5):                    
                    call LauraFace("angry")
                    ch_l "You'd better remember who you're talking to, [newgirl[Laura].Petname]."
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")  
                    call Remove_Girl("Laura")
                    return                                
            $ Tempmod += 20
            $ newgirl["Laura"].Forced += 1
            call LauraFace("sad")
            if "stripforced" in newgirl["Laura"].RecentActions:                    
                    call LauraFace("angry")
                    ch_l ". . ."
            else:
                    ch_l "Grrrr. . ."
                    $ newgirl["Laura"].RecentActions.append("stripforced")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -40)
        "You can do better than that. Keep going." if not newgirl["Laura"].Forced:
            if not ApprovalCheck("Laura", 300, "O", TabM=5) and not ApprovalCheck("Laura", 700, "L", TabM=5):                   
                    call LauraFace("angry")
                    ch_l "I don't like that tone, [newgirl[Laura].Petname]."
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")  
                    call Remove_Girl("Laura")
                    return                
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 75, 5)
            $ Tempmod += 20
            $ newgirl["Laura"].Forced += 1
            call LauraFace("sad")
            ch_l ". . . Right. . ."
            
    if "ultimatum" not in newgirl["Laura"].DailyActions:
            $ newgirl["Laura"].DailyActions.append("ultimatum")
    show Laura_Sprite at Laura_Dance1()
    "Laura begins to dance again."
    return
              
# end Strip Tease ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

transform Laura_Dance1():     
    subpixel True 
    pos (newgirl["Laura"].SpriteLoc, 50)
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
            ease 2.5 xoffset -30
            ease 2.5 xoffset 0
        parallel:     
            ease 1.5 yoffset 150 
            ease 3.5 yoffset 0 
    repeat
    
           

# Start Laura Undressing  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Laura_Undress(Region = "ask", CountStore=0):  
    $ CountStore = Tempmod    
    if Partner == "Laura":
            $ Tempmod = 0  
    call Shift_Focus("Laura")           
                    
    if Region == "auto":
        if newgirl["Laura"].Upskirt and newgirl["Laura"].PantiesDown:
            return
        if newgirl["Laura"].Legs == "pants" and Tempmod < 20:
            $ Tempmod = 20
        if newgirl["Laura"].Lust >= 90:
            $ Tempmod += 10      
        elif newgirl["Laura"].Lust >= 80:
            $ Tempmod += 5  
        $ Situation = "auto"
        call Laura_Bottoms_Off(0)
        $ Situation = 0
    
    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if newgirl["Laura"].Over or newgirl["Laura"].Chest:    
                $ Region = "top"     
            "Her bottoms" if newgirl["Laura"].Legs or newgirl["Laura"].Panties or newgirl["Laura"].Hose:
                $ Region = "bottom"           
            "A little of both. . ." if (newgirl["Laura"].Over or newgirl["Laura"].Chest) and (newgirl["Laura"].Legs or newgirl["Laura"].Panties or newgirl["Laura"].Hose): 
                $ Region = "both"    
            "Never mind":
                pass
    
    if Region == "top":
        if newgirl["Laura"].Over or newgirl["Laura"].Chest:    
                call Laura_Top_Off(0)  
    elif Region == "bottom":
        if newgirl["Laura"].Legs or newgirl["Laura"].Panties or newgirl["Laura"].Hose:
                call Laura_Bottoms_Off(0)  
    elif Region == "both":        
            if newgirl["Laura"].Over or newgirl["Laura"].Chest:    
                    call Laura_Top_Off(0) 
            
            if Partner == "Laura":
                    $ Tempmod = 0
            else:
                    $ Tempmod = CountStore 
            
            if "angry" in newgirl["Laura"].RecentActions: 
                    pass            
            elif not newgirl["Laura"].Legs and not newgirl["Laura"].Panties and not newgirl["Laura"].Hose:
                    pass                
            elif "no topless" in newgirl["Laura"].RecentActions:
                    menu:
                        ch_l "Know when to fold'em, [newgirl[Laura].Petname]."
                        "And now the bottoms?":
                            call Laura_Bottoms_Off(0) 
                        "You're probably right, sorry.":
                            pass
            else:
                    ch_p "And now the bottoms?"
                    call Laura_Bottoms_Off(0) 
                    
    
    $ Tempmod = CountStore
    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Laura_Top_Off(Intro = 1, Line = 0, Cnt = 0):                                                    # Will she take her top off? Modifiers
    call Shift_Focus("Laura")
    
    if not newgirl["Laura"].Over and not newgirl["Laura"].Chest:                              # If she's already topless. Just skip back.
        $ Tempmod = 0
        return
        
    if "angry" in newgirl["Laura"].RecentActions:  
        ch_l "Don't push it, [newgirl[Laura].Petname]."
        return
    
    if newgirl["Laura"].SeenChest and ApprovalCheck("Laura", 600) and not Taboo:                              #You've seen her tits.
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 40 
    if "no topless" in newgirl["Laura"].RecentActions: 
        $ Tempmod -= 10
                     
    if Intro:
        if newgirl["Laura"].Over:
                ch_p "This might be easier without your [newgirl[Laura].Over] on."
        elif newgirl["Laura"].Chest:
                ch_p "This might be easier without your [newgirl[Laura].Chest] on."

    $ Approval = ApprovalCheck("Laura", 1200, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
    
    if Situation == "auto":  
        $Line = 0
        if newgirl["Laura"].Over: # If she's in a top
            if newgirl["Laura"].Chest and ApprovalCheck("Laura", 800, TabM = 1):
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1)
            elif Approval >= 2 or (newgirl["Laura"].SeenChest and ApprovalCheck("Laura", 600) and not Taboo):
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
            else:
                return
            $ Line = newgirl["Laura"].Over
            $ newgirl["Laura"].Over = 0
            "Laura scowls in irritation, and shrugs off her [Line]."
            if not newgirl["Laura"].Chest:
                if Taboo:
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, (int(Taboo/20)))   
                call Laura_First_Topless(1)
                
        if newgirl["Laura"].Chest:
            if Approval >= 2 or (newgirl["Laura"].SeenChest and ApprovalCheck("Laura", 600) and not Taboo):
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                if Taboo:
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, (int(Taboo/20)))  
                if Line:
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0
                    "As it hits the floor, she unfastens her [Line] and allows it to drop as well."  
                else:
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0
                    "Laura scowls in irritation, she unfastens her [Line] and allows it to drop to the floor."                     
                call Laura_First_Topless(1) 
                ch_l "Ah, that's better."  
        return
    
    
    if Approval >= 2:                                                                               # Does she assume top off?            
        if "no topless" in newgirl["Laura"].DailyActions:
            ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
        call LauraFace("sexy", 1)
        if newgirl["Laura"].Forced:
            call LauraFace("sad", 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)  
        $ Cnt = 1
        while (newgirl["Laura"].Chest or newgirl["Laura"].Over) and Cnt:
            menu:                                                                                 #Menu All off?
                ch_l "What did you want to see, [newgirl[Laura].Petname]?"  
                "Lose the wristbands." if newgirl["Laura"].Arms:
                    call LauraFace("bemused", 1)                    
                    $ newgirl["Laura"].Arms = 0               
                    "Laura  pulls off her wristbands and drops them to the floor."                     
                "Lose the [newgirl[Laura].Over]." if newgirl["Laura"].Over:                 
                    call LauraFace("bemused", 1)                    
                    $ Line = newgirl["Laura"].Over
                    $ newgirl["Laura"].Over = 0
                    "Laura shrugs off her [Line] and it drops to the floor."
                "Just lose the [newgirl[Laura].Chest]." if newgirl["Laura"].Over and newgirl["Laura"].Chest:
                    call LauraFace("bemused", 1)                    
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0               
                    "Laura unfastens her [Line] beneath her [newgirl[Laura].Over], and allows it to drop to the floor."   
                "Lose the [newgirl[Laura].Chest]." if not newgirl["Laura"].Over and newgirl["Laura"].Chest:
                    call LauraFace("bemused", 1)
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0              
                    "Laura pulls off her [Line] and allows it to drop to the floor." 
                "Lose both tops." if newgirl["Laura"].Over and newgirl["Laura"].Chest:
                    call LauraFace("bemused", 1)  
                    $ Line = newgirl["Laura"].Over
                    $ newgirl["Laura"].Over = 0
                    "Laura shrugs off her [Line]-"      
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0 
                    "-followed quickly by her [Line]."           
                "That's enough. [[exit]":               
                    call LauraFace("bemused", 1)
                    ch_l "Suit yourself. . ."    
                    $ Cnt = 0
        if not newgirl["Laura"].Chest and not newgirl["Laura"].Over:             
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            call Laura_First_Topless  
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 3)        
        $ newgirl["Laura"].RecentActions.append("ask topless")                      
        $ newgirl["Laura"].DailyActions.append("ask topless") 
        $ Tempmod = 0        
        return
        
    #Else, Approval < 2, Doesn't want to lose the top//////////////////////////////////  
                 
    call LauraFace("bemused", 1)   
    if Intro == "massage" and not Approval:
        ch_l "I could use a massage, but I'm keeping my clothes on."
    elif "no topless" in newgirl["Laura"].RecentActions: 
        call LauraFace("angry")
        ch_l "Don't push it, [newgirl[Laura].Petname]."    
    elif Approval and not newgirl["Laura"].SeenChest:
        ch_l "I don't know, man."    
    elif not newgirl["Laura"].SeenChest:
        ch_l "I really don't think so."   
    elif "no topless" in newgirl["Laura"].DailyActions: 
        ch_l "Dude, relax."           
    elif "ask topless" in newgirl["Laura"].RecentActions: 
        ch_l "Again?"       
    elif Taboo:
        ch_l "[newgirl[Laura].Petname], not around here, alright?"          
    elif Approval:
        ch_l "Are you sure?"
    else:
        ch_l "No."
        
    menu:
        extend ""
        "Sorry, sorry." if "no topless" in newgirl["Laura"].RecentActions:  
            call LauraFace("bemused", 1)   
            ch_l "Right, I get it, stay thirsty."
        "Ok, that's fine." if "no topless" not in newgirl["Laura"].RecentActions: 
            if "ask topless" not in newgirl["Laura"].DailyActions:
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 3)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
            if newgirl["Laura"].Forced:
                $ newgirl["Laura"].Mouth = "grimace"
                ch_l "Ok."
                if "ask topless" not in newgirl["Laura"].DailyActions:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, 2)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
         
        "Lose the gloves." if newgirl["Laura"].Arms:
            call LauraFace("bemused", 1)
            $ newgirl["Laura"].Arms = 0               
            "Laura  pulls off her gloves and drops them to the floor." 
            
        "How about just the [newgirl[Laura].Over]?" if newgirl["Laura"].Over:                                                # asked to go shirtless. 
            if ApprovalCheck("Laura", 1000, TabM = 3) and newgirl["Laura"].Chest: #80, 160 taboo 
                call LauraFace("sexy") 
                ch_l "I mean. . . I guess. . ."                 
                call LauraFace("bemused", 1)                
                $ Line = newgirl["Laura"].Over
                $ newgirl["Laura"].Over = 0
                "Laura shrugs off her [Line]."   
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 1)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
            elif not newgirl["Laura"].Chest:
                $ newgirl["Laura"].Eyes = "surprised"
                $ newgirl["Laura"].Blush = 2
                ch_l "I don't really have anything on under here." 
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ newgirl["Laura"].Mouth = "smile"
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                        ch_l "Right."             
                    "I think I could handle it.":
                        if ApprovalCheck("Laura", 700, "I", TabM=3) or ApprovalCheck("Laura", 1100, TabM=3):
                            call LauraFace("bemused", 1)
                            ch_l "Maybe you could. . ."                               
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 2)                                                         
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
                            call LauraFace("sexy")   
                            $ Line = newgirl["Laura"].Over
                            $ newgirl["Laura"].Over = 0
                            "Laura shrugs off her [Line]."   
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)  
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                            call Laura_First_Topless   
                        else:   
                            call LauraFace("bemused")
                            call Laura_Top_Off_Refused  
                            
                    "I know, take it off.":
                        call Laura_ToplessorNothing
                $ newgirl["Laura"].Blush = 1        
            else:   
                call LauraFace("sexy")
                call Laura_Top_Off_Refused  
                                 
        "Come on, Please? [[take it all off]":                                                                      # asked to go topless. 110, 270 Taboo   
            if Approval and ApprovalCheck("Laura", 600, "L", TabM=1):                 
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)
                call LauraFace("sexy")   
                if "no topless" in newgirl["Laura"].RecentActions:     
                    ch_l "Fine, you thirsty weirdo."
                else:
                    ch_l "I guess I could . . ." 
                if newgirl["Laura"].Over:
                    $ Line = newgirl["Laura"].Over
                    $ newgirl["Laura"].Over = 0
                    "Laura shrugs off her [Line]. . ."   
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0 
                    ". . .and then her [Line] as well."
                else: 
                    $ Line = newgirl["Laura"].Chest
                    $ newgirl["Laura"].Chest = 0 
                    "Laura shrugs off her [Line]." 
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)  
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                call Laura_First_Topless 
            elif "no topless" in newgirl["Laura"].RecentActions:
                call LauraFace("angry")
                ch_l "Still no."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)  
                $ newgirl["Laura"].RecentActions.append("angry")
                $ newgirl["Laura"].DailyActions.append("angry")   
            else:   
                call LauraFace("sexy")
                call Laura_Top_Off_Refused
        
        "No, topless or nothing.":                                                              #demanded topless 60, 260 taboo 
            call Laura_ToplessorNothing
                                
        "Never mind.":
            pass
    
    $ newgirl["Laura"].RecentActions.append("ask topless")                      
    $ newgirl["Laura"].DailyActions.append("ask topless") 
    $ Tempmod = 0
    return


label Laura_Top_Off_Refused:                    #When you insist but she refuses    
    call LauraFace("angry")
    if "no topless" in newgirl["Laura"].RecentActions:  
        ch_l "You're getting real close to the line, [newgirl[Laura].Petname]."
    elif "no topless" in newgirl["Laura"].DailyActions:  
        ch_l "You keep coming back with this, [newgirl[Laura].Petname]."
    call LauraFace("sad")
    menu:
        ch_l "Let it go?"
        "Sure, never mind." if "no topless" not in newgirl["Laura"].RecentActions:
            call LauraFace("sexy")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
            ch_l "Good."  
        "Sorry, I'll drop it." if "no topless" in newgirl["Laura"].RecentActions:   
            ch_l "Good."  
        "No, I'm serious.":
            $ newgirl["Laura"].Brows = "angry"
            ch_l "Your funeral."
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 5)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
            if "no topless" not in newgirl["Laura"].RecentActions:
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)    
            $ newgirl["Laura"].RecentActions.append("angry")
            $ newgirl["Laura"].DailyActions.append("angry")   
    $ newgirl["Laura"].RecentActions.append("no topless")                      
    $ newgirl["Laura"].DailyActions.append("no topless") 
    return
              

label Laura_ToplessorNothing:
    call LauraFace("angry")
    if ApprovalCheck("Laura", 700, "OI", TabM = 4) and ApprovalCheck("Laura", 400, "O", TabM = 3):       
        #She agrees to your ultimatum 
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
        if "no topless" in newgirl["Laura"].RecentActions:             
            ch_l "Hrmph, whatever. . ."                 
        else:
            call LauraFace("sad")
            ch_l "Ugh, whatever."                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
        if newgirl["Laura"].Over:
            if newgirl["Laura"].Chest:        
                $ Line = newgirl["Laura"].Over
                $ newgirl["Laura"].Over = 0 
                "Laura shrugs off her [Line]. . ."    
                $ Line = newgirl["Laura"].Chest
                $ newgirl["Laura"].Chest = 0
                ". . .and then her [Line] as well."
            else:
                $ Line = newgirl["Laura"].Over
                $ newgirl["Laura"].Over = 0
                "Laura shrugs off her [Line]. . ."                    
        elif newgirl["Laura"].Chest:
            $ Line = newgirl["Laura"].Chest
            $ newgirl["Laura"].Chest = 0    
            "Laura unfastens her [Line] and lets it drop to the floor. . ."   
        if newgirl["Laura"].Arms:            
            $ newgirl["Laura"].Arms = 0    
            "She pulls off her gloves and drops them to the floor."
        call Laura_First_Topless                       
    else:                                                                                                
        #she refuses your ultimatum
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, -1, 1)
        if "no topless" in newgirl["Laura"].RecentActions: 
            $newgirl["Laura"].Brows = "angry"
            ch_l "You have got to chill."  
        else: 
            ch_l "Nope."      
        $ newgirl["Laura"].RecentActions.append("no topless")                      
        $ newgirl["Laura"].DailyActions.append("no topless")     
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    return              
    
label Laura_First_Topless(Silent = 0, TempLine = 0):          
    $ newgirl["Laura"].RecentActions.append("topless")                      
    $ newgirl["Laura"].DailyActions.append("topless")
    call DrainWord("Laura","no topless")    
    $ newgirl["Laura"].SeenChest += 1 
    if newgirl["Laura"].SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 15)  
    if not Silent:
        call LauraFace("sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"    
        $ newgirl["Laura"].Blush = 1
        menu:
            extend ""
            "Your tits, they look great.":            
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 20)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 20)           
                call LauraFace("sexy",1,Eyes="down")    
                ch_l "Huh. I mean I guess so. . ."           
                call LauraFace("smile",0)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, 20)
            ". . . [[stunned]":            
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 10)
                ch_l "Cat got your tongue?"
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, 10)  
            "Huh, not what I was expecting. . .":        
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -30)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 25)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, -15)                          
                call LauraFace("confused",2)
                ch_l "Huh?"
                menu:        
                    "They're really perky!":    
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 20)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -20)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 20)                          
                        call LauraFace("perplexed",1)
                        ch_l "Oh. Right. . ."
                    "I, um, no, they're great!":                        
                        call LauraFace("angry",2, Mouth="smile")
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 10)   
                        ch_l "Why wouldn't they be?"    
                    "Kitty's were tighter, that's all." if K_SeenChest:                            
                        $ TempLine = "Kitty"
                    "Emma's were a lot bigger, that's all." if E_SeenChest:                            
                        $ TempLine = "Kitty"
                        
                if TempLine:
                        call LauraFace("angry")
                        $ newgirl["Laura"].Mouth = "surprised"                        
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 30)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, -25)  
                        ". . ."
                        $ newgirl["Laura"].Mouth = "sad"
                        if TempLine == "Emma":
                                if newgirl["Laura"].LikeEmma >= 800:
                                    call LauraFace("sly",2,Eyes="side")
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                    ch_l "They are kinda huge. . ."       
                                    $ newgirl["Laura"].LikeEmma += 20 
                                elif newgirl["Laura"].LikeEmma >= 600:
                                    $ newgirl["Laura"].Eyes = "side" 
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                    ch_l "I guess that's true. . ."    
                                else:                        
                                    $ newgirl["Laura"].LikeEmma -= 50
                                    $ Templine = "bad"
                                
                        elif TempLine == "Kitty":
                                if newgirl["Laura"].LikeKitty >= 800:
                                    call LauraFace("sly",2,Eyes="side")
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                    ch_l "She is very. . . streamlined. . ."       
                                    $ newgirl["Laura"].LikeKitty += 20 
                                elif newgirl["Laura"].LikeKitty >= 700:
                                    $ newgirl["Laura"].Eyes = "side" 
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                    ch_l "they are kinda. . . pointy. . ."    
                                else:                        
                                    $ newgirl["Laura"].LikeKitty -= 50
                                    $ Templine = "bad"
                        
                        
                        if TempLine == "bad":
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -20)
                                ch_l "Still kinda rude though."   
                                call LauraOutfit
                                $ newgirl["Laura"].RecentActions.append("no topless")                      
                                $ newgirl["Laura"].DailyActions.append("no topless")  
                                $ newgirl["Laura"].RecentActions.append("angry")
                                $ newgirl["Laura"].DailyActions.append("angry")  
                        
                    
    else:
        if ApprovalCheck("Laura", 800) and not newgirl["Laura"].Forced:                #if she's not forced and happy about it
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 15) 
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 15)              
            call LauraFace("smile")
        else:                                                           #if she's not happy about it
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -40)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, -20)                          
            call LauraFace("angry")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 40)
    return



# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Laura_Bottoms_Off(Intro = 1, Line = 0, Cnt = 0):
    call Shift_Focus("Laura")
    
    if not newgirl["Laura"].Legs and not newgirl["Laura"].Panties and not newgirl["Laura"].Hose:                                  
        # If she's already bottomless. Just skip back.     
        $ Tempmod = 0
        return
    
    if "angry" in newgirl["Laura"].RecentActions:  
        ch_l "You're barking up the wrong tree."
        return
    
    # Will she take her bottoms off Modifiers
    if newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 800): #You've seen her Pussy.
        $ Tempmod += 20
    elif not newgirl["Laura"].Panties:
        $ Tempmod -= 20
    elif newgirl["Laura"].SeenPanties and ApprovalCheck("Laura", 600): #You've seen her panties.
        $ Tempmod += 5 
    if Intro == "dildo":
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (Taboo * 5)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames and not Taboo:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 40 
    if "no bottomless" in newgirl["Laura"].RecentActions: 
        $ Tempmod -= 20
    
    if Intro:
        if newgirl["Laura"].Legs:
                ch_p "This might be easier without your [newgirl[Laura].Legs] on."
        elif newgirl["Laura"].Panties:
                ch_p "This might be easier without your [newgirl[Laura].Panties] on."
                
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
    
    if Situation == "auto":
            $ Cnt = 0
            
            if not newgirl["Laura"].Upskirt:                      
                if newgirl["Laura"].Legs == "skirt" and not newgirl["Laura"].Upskirt:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 700) and not Taboo):
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                        if Taboo:
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, (int(Taboo/20)))                 
                        $ newgirl["Laura"].Upskirt = 1
                        "She slides her skirt up."
                        $ Cnt = 1 
                        
                if PantsNum("Laura") >= 5 or HoseNum("Laura") >= 6:            
                    if newgirl["Laura"].Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not newgirl["Laura"].SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not newgirl["Laura"].SeenPussy and Taboo):
                        return     
                    elif newgirl["Laura"].Legs == "pants" and newgirl["Laura"].Upskirt:  
                        return
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                    $ newgirl["Laura"].Upskirt = 1
                    "Laura shrugs, and then tugs her [Line] down." 
                    if newgirl["Laura"].Panties:
                        $ newgirl["Laura"].SeenPanties = 1
                    else:
                        call Laura_First_Bottomless(1)  
                        
                    if Taboo:
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if newgirl["Laura"].Panties and not newgirl["Laura"].PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (newgirl["Laura"].SeenPussy and not Taboo):
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)
                    if Taboo:
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, (int(Taboo/10)))  
                    $ newgirl["Laura"].PantiesDown = 1
                    if Cnt:
                        "and pulls her [newgirl[Laura].Panties] down too."
                    else:
                        "Laura tsks in irritation, and tugs her [newgirl[Laura].Panties] down." 
                    call Laura_First_Bottomless(1) 
                        
                    ch_l "I guess all that was in the way."  
            return
            
    
    if Approval >= 2:                 
            #will she volunteer to strip to underwear?///////////////////////////////////////////////////        
            call LauraFace("sexy", 1)
            if newgirl["Laura"].Forced:
                call LauraFace("sad", 1)              
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                $ Line = "Hmm, I guess."            
            elif Approval >= 3:
                $ Line = "What did you want off?"
            else:    
                $ Line = "Hm, what did you want me to lose?"
            
            call Laura_Bottoms_Off_Legs
                
            if not newgirl["Laura"].Panties and Action_Check("Laura", "recent", "bottomless") < 2: 
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 3)
    
  
        
    elif newgirl["Laura"].Legs or newgirl["Laura"].Panties or newgirl["Laura"].Hose:
            # She'd rather not strip but might        
            call LauraFace("bemused", 1) 
            if "no bottomless" in newgirl["Laura"].RecentActions: 
                call LauraFace("angry")
                ch_l "Now you're just embarrassing yourself."   
            elif "no topless" in newgirl["Laura"].RecentActions: 
                call LauraFace("angry")
                ch_l "This is really pushing it."  
            elif Approval and not newgirl["Laura"].SeenPussy:
                ch_l "I don't know if you're earned that yet."  
            elif not newgirl["Laura"].SeenPussy and "ask topless" in newgirl["Laura"].RecentActions:
                ch_l "Kinda pushing it, [newgirl[Laura].Petname]. . ."    
            elif not newgirl["Laura"].SeenPussy:
                ch_l "Maybe, after you've earned it. . ."   
            elif "no bottomless" in newgirl["Laura"].DailyActions: 
                ch_l "So thirsty. . ."             
            elif Taboo:
                ch_l "This is pretty exposed, [newgirl[Laura].Petname]. . ."  
            elif Approval:
                ch_l "Probably not. . ."   
            elif newgirl["Laura"].SeenPussy:
                ch_l "You've probably seen enough . . ."            
            elif PantsNum("Laura") >= 10:
                ch_l "Well, I'm keeping my pants on."           
            elif newgirl["Laura"].Legs == "skirt":
                ch_l "Well, I'm keeping my skirt on."   
            elif PantsNum("Laura") >= 5:
                ch_l "Well, I'm keeping my shorts on."  
            else:
                ch_l "Well, I'm keeping my panties on." 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in newgirl["Laura"].RecentActions:  
                    if "ask bottomless" not in newgirl["Laura"].DailyActions:
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 2)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                    if newgirl["Laura"].Forced:
                        $ newgirl["Laura"].Mouth = "smile"
                        ch_l "Right."
                        if "ask bottomless" not in newgirl["Laura"].DailyActions:
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, 3)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 4)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in newgirl["Laura"].RecentActions:  
                    ch_l "Good."
                 
                "Come on, Please?":       
                    if "no bottomless" in newgirl["Laura"].DailyActions:  
                            call LauraFace("angry")
                            ch_l "You heard me."
                    else:
                            if Approval and ApprovalCheck("Laura", 600, "L", TabM=2):   
                                call LauraFace("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                if D20 == 3:
                                    $ Line = "Well. . ."
                                    $ Approval += 1
                                else:
                                    $ Line = "Maybe. . ."                        
                                call Laura_Bottoms_Off_Legs  
                            else:    
                                call LauraFace("sexy")
                                call Laura_Bottoms_Off_Refused
                                        
                "It doesn't have to be everything. . ." if newgirl["Laura"].Legs or HoseNum("Laura") >= 10 or newgirl["Laura"].Panties == "shorts":    
                    if Approval and "no bottomless" not in newgirl["Laura"].DailyActions:                    
                        call LauraFace("bemused", 1)
                        $Line = "Well like what were you thinking?"
                        call Laura_Bottoms_Off_Legs  
                    else:    # She refuses your request. . .
                        call LauraFace("sexy")
                        call Laura_Bottoms_Off_Refused                                
                "It doesn't have to be everything. . . (locked)" if not newgirl["Laura"].Legs and HoseNum("Laura") < 10 and newgirl["Laura"].Panties != "shorts":   
                    pass
                    
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and newgirl["Laura"].Obed >= 250) or (ApprovalCheck("Laura", 1000, "OI", TabM = 5) and ApprovalCheck("Laura", 500, "O", TabM = 3)):                    
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -1, 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                        $ Line =  "Don't push me. . ."  
                        $ Approval = 1 if Approval < 1 else Approval
                        $ newgirl["Laura"].Forced = 1
                        call Laura_Bottoms_Off_Legs                     
                    else:          
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)
                        if ApprovalCheck("Laura", 400, "O"):
                            ch_l "No way." 
                        else:
                            call LauraFace("angry")
                            ch_l "Fuck off."                          
                            $ newgirl["Laura"].RecentActions.append("angry")
                            $ newgirl["Laura"].DailyActions.append("angry")   
                        $ newgirl["Laura"].RecentActions.append("no bottomless")                      
                        $ newgirl["Laura"].DailyActions.append("no bottomless")  
            #end approval
    
    $ Tempmod = 0
    $ newgirl["Laura"].RecentActions.append("ask bottomless")                      
    $ newgirl["Laura"].DailyActions.append("ask bottomless")     
    return           

label Laura_Bottoms_Off_Legs:    
    
    if newgirl["Laura"].Forced:        
        call LauraFace("sad", 1)
    elif ApprovalCheck("Laura", 1100, "OI", TabM = 3):        
        call LauraFace("sly")
    elif ApprovalCheck("Laura", 1400, TabM = 3):  
        call LauraFace("sexy", 1) 
    else:
        call LauraFace("bemused", 1) 
        
    $ Line = "What did you have in mind?" if not Line else Line
    $ Cnt = 1
    while Cnt and (newgirl["Laura"].Legs or newgirl["Laura"].Panties or newgirl["Laura"].Hose):
        menu:                                       # She's asking what you'd like to see.
            ch_l "[Line]"
            "Everything. . ." if Line != "Well like what were you thinking?": #approval a given
                        
                    if Approval < 2 and not newgirl["Laura"].Panties and HoseNum("Laura") < 10:
                        call Laura_NoPanties
                    
                    if newgirl["Laura"].Legs:
                        $ Line = newgirl["Laura"].Legs      
                        $ newgirl["Laura"].Legs = 0
                        "Laura pulls her [Line] down."
                        $ newgirl["Laura"].SeenPanties = 1 if not newgirl["Laura"].SeenPanties else newgirl["Laura"].SeenPanties
                                           
                    if Approval < 2 and not newgirl["Laura"].Panties and HoseNum("Laura") >= 10:
                        call Laura_NoPanties   
                        
                    if newgirl["Laura"].Boots:
                        $ newgirl["Laura"].Boots = 0
                        "She pulls her boots off."   
                        
                    if newgirl["Laura"].Hose:
                        $ Line = newgirl["Laura"].Hose #HoseName 
                        $ newgirl["Laura"].Hose = 0
                        "She rolls her hose off."                    
                                            
                    if Approval < 2:
                        call Laura_NoPanties   
                    if newgirl["Laura"].Panties:                               
                        $ Line = newgirl["Laura"].Panties   
                        $ newgirl["Laura"].Panties = 0  
                        "She reaches down and pulls her [Line] off." 
                    call Laura_First_Bottomless   
                    
                    
            "Lose the [newgirl[Laura].Legs]." if newgirl["Laura"].Legs: 
                    if newgirl["Laura"].Panties and Approval >= 2:
                        call LauraFace("sexy")
                        ch_l "I guess I could. . ."
                    elif Approval:          
                        call LauraFace("sexy", 1)    
                        if Approval < 2 and not newgirl["Laura"].Panties and HoseNum("Laura") < 10:
                            call Laura_NoPanties
                    else:    
                        call LauraFace("sexy")
                        call Laura_Bottoms_Off_Refused
                        return
                        
                    $ Line = newgirl["Laura"].Legs      
                    $ newgirl["Laura"].Legs = 0
                    if not newgirl["Laura"].Panties and HoseNum("Laura") < 10:
                        call LauraFace("sly", 1)  
                        "She looks at you slyly before pulling her [Line] off." 
                        call Laura_First_Bottomless 
                    else:
                        "Laura pulls down her [Line]."                        
                        $ newgirl["Laura"].SeenPanties = 1 if not newgirl["Laura"].SeenPanties else newgirl["Laura"].SeenPanties
                    call LauraFace("bemused", 1)
            
            
            "Lose the [newgirl[Laura].Panties]." if newgirl["Laura"].Panties:
                    if Approval < 2:
                        ch_l "I'm afraid not."
                        $ newgirl["Laura"].RecentActions.append("no bottomless")                      
                        $ newgirl["Laura"].DailyActions.append("no bottomless")   
                        return                        
                    else:
                        ch_l "Huh, ok. . ."                                    
                    $ Line = newgirl["Laura"].Panties   
                    $ newgirl["Laura"].Panties = 0  
                             
                    if PantsNum("Laura") >= 5:
                        "She pulls down her [newgirl[Laura].Legs], then pulls her [Line] off and puts them back on."    
                    else:
                        "She reaches down and pulls her [Line] off."
                    if not newgirl["Laura"].Legs:
                        call Laura_First_Bottomless 
            
            "Lose the [newgirl[Laura].Boots]." if newgirl["Laura"].Boots:
                    ch_l "Hm, if you want."   
                    $ newgirl["Laura"].Boots = 0                      
                    "She reaches down and pulls her boots off."
                        
            
#            "Lose the [newgirl[Laura].Hose]." if newgirl["Laura"].Hose:                                    #make sure to update this mess if I add hose to her
#                    call LauraFace("bemused", 1) 
#                    if newgirl["Laura"].Legs:
#                        ch_l "All right, fine."                         
#                    elif Approval < 2 and not newgirl["Laura"].Panties and HoseNum("Laura") >= 10:
#                        call Laura_NoPanties                            
#                    elif not Approval and HoseNum("Laura") >= 6:
#                        ch_l "Sorry, no, [newgirl[Laura].Petname]."
#                        return                            
#                    else:
#                        ch_l "Fine, [newgirl[Laura].Petname]."                 
                        
#                    $ Line = newgirl["Laura"].Hose   
#                    $ newgirl["Laura"].Hose = 0  
#                    if newgirl["Laura"].Legs:
#                        "She reaches under her [newgirl[Laura].Legs] and pulls her [Line] down."
#                    elif HoseNum("Laura") < 10:
#                        "Laura pulls her [Line] off." 
#                    elif not newgirl["Laura"].Panties:
#                        call LauraFace("sly", 2)  
#                        "She blushes and looks at you slyly before removing her [Line]." 
#                        $ newgirl["Laura"].Blush = 1
#                        call Laura_First_Bottomless   
#                    elif not newgirl["Laura"].SeenPanties:
#                        "Laura shyly removes her [Line]."
#                        $ newgirl["Laura"].SeenPanties = 1
#                    else:
#                        "Laura pulls her [Line] off." 
                        
            "Keep it all on for now." if Cnt == 1:
                $ newgirl["Laura"].Mouth = "smile"
                $ Cnt = 0
                
            "Ok, that's enough for now." if Cnt == 2:
                $ Cnt = 0
                
        $ Cnt = 2 if Cnt else Cnt  
        $ Line = renpy.random.choice(["Is that it?",       
            "You finished?",
            "Anything else?"]) 
    return


label Laura_NoPanties: 
    #called when asked to remove pants with nothing on under
    if not R_Panties:
        return
    if newgirl["Laura"].Legs or HoseNum("Laura") >= 10:
        ch_l "I don't have anything on under this. . ."  
    else:
        ch_l "These are all I have on. . ."  
    menu:
        extend ""
        "Could you do it anyway?":
            if ApprovalCheck("Laura", 1100, "LI", TabM=1):                                             
                ch_l "I guess. . . "
            else:
                ch_l "Nah, not right now."
                call Laura_Bottoms_Off_Refused
                $ renpy.pop_call()  
        "Don't care, lose'em.":
            if ApprovalCheck("Laura", 800, "OI", TabM=1):
                ch_l "Fine."  
            else:
                call Laura_Bottoms_Off_Refused
                $ renpy.pop_call()  
                                       
        "Ok, you can leave it on.":
            $ renpy.pop_call()   
    return 
        
label Laura_Bottoms_Off_Refused:     
    if "no bottomless" in newgirl["Laura"].RecentActions:  
        ch_l "Reign it in."
    elif "no bottomless" in newgirl["Laura"].DailyActions:  
        ch_l "No, not today."
    else:
        call LauraFace("sad")
        if Cnt == 2:            
            ch_l "No more, is that going to be a problem?"   
        else:
            ch_l "Nope, is that going to be a problem?"        
    menu:
        extend ""
        "No, no, never mind." if "no bottomless" not in newgirl["Laura"].RecentActions:
            $ newgirl["Laura"].Mouth = "smile"
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)    
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)  
            ch_l "Right."    
        "Sorry, I'll drop it." if "no bottomless" in newgirl["Laura"].RecentActions:   
            ch_l "Good. . ."  
        "Yeah, let's do something else.":
            $newgirl["Laura"].Brows = "confused"
            ch_l "Your loss."               
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 5)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2, 1)
            if "no bottomless" not in newgirl["Laura"].RecentActions:  
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 4)      
            $ newgirl["Laura"].RecentActions.append("angry")
            $ newgirl["Laura"].DailyActions.append("angry")   
            
    $ newgirl["Laura"].RecentActions.append("no bottomless")                      
    $ newgirl["Laura"].DailyActions.append("no bottomless")
    $ Tempmod = 0
    return   

label Laura_First_Bottomless(Silent = 0): 
    $ newgirl["Laura"].RecentActions.append("bottomless")                      
    $ newgirl["Laura"].DailyActions.append("bottomless")
    call DrainWord("Laura","no bottomless")
    $ newgirl["Laura"].SeenPussy += 1 
    if newgirl["Laura"].SeenPussy > 1:     
        return                  #ends portion if you've already seen them        
    
    
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 30)  
    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)   
    if not Silent:
        call LauraFace("sly")
        "You find yourself staring at [newgirl[Laura].GirlName]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 20)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 25)            
                call LauraFace("smile")          
                ch_l "You think?"
                ch_l "Yeah, I like it too. . . "
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, 20)
            "I see you keep it natural down there." if newgirl["Laura"].Pubes:          
                call LauraFace("confused",1)  
                ch_l "Well. . . yeah."
                if ApprovalCheck("Laura", 700, "LO"):    
                    call LauraFace("bemused")     
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if ApprovalCheck("Laura", 900, "LO"):
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 30)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 25)        
                                ch_l "I guess I could. . ."
                                $ newgirl["Laura"].Todo.append("pubes")  
                            else:   
                                call LauraFace("normal")     
                                ch_l "Seems like a waste of time."
                                ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 10)
                                ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":  
                                if ApprovalCheck("Laura", 900, "LO"):
                                    call LauraFace("sly")    
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 10)
                                else:
                                    call LauraFace("angry",Mouth="normal")    
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 25) 
                                ch_l "Right."
                                $ newgirl["Laura"].Brows = "normal"
                else:                              
                    call LauraFace("angry",1)  
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -20) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 25)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, -5)         
                    ch_l "I mean, what else would I do?"
            "What a mess.":        
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -30)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 25)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, -30)
                call LauraFace("angry",2)           
                if not newgirl["Laura"].Forced and not ApprovalCheck("Laura", 900, "LO"):                    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 25)
                ch_l "I'll make you a mess. . ."
    else:
        
        if ApprovalCheck("Laura", 800) and not newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 20)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 25)          
            call LauraFace("smile")          
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, 20)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)
        else:        
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -40)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, -20)
            call LauraFace("angry")          
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 30)
    return
    
# End Laura Undressing  ///////////////////////////////////////////////////////////////////

    

label Laura_First_Peen(Silent = 0, Undress = 0, Second = 0, React = 0): 
    #checked each time she sees your cock  ## call Laura_First_Peen(0,1)
    #if Silent it doesn't say anything
    #if Undress then you get nude
    #if Secondary then this is the second girl to see it.
    # React 0 if other girl didn't comment, 
    # 1 = if the other girl commented, 2 = didn't like it
    
    if newgirl["Laura"].Loc != bg_current:
                if Partner == "Laura":
                        $ Partner = 0
                return  
    if "cockout" in P_RecentActions and "peen" in newgirl["Laura"].RecentActions: 
                #If the cock is already out and she's seen it, return
                return
            
    $ newgirl["Laura"].RecentActions.append("peen")                      
    $ newgirl["Laura"].DailyActions.append("peen")
    $ newgirl["Laura"].SeenPeen += 1                      
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1)
    
    if Second:
        #If another girl commented on it first. . .
        if newgirl["Laura"].SeenPeen == 1: 
                call LauraFace("smirk", 2, Eyes = "down")  
                ch_l "Huh, that's a pretty good one you got there. . ."
                call LauraFace("bemused", 1)  
        elif Second == 1:
                # The other girl liked it
                if not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 500, "I"):
                    call LauraFace("sad", 1) 
                    ch_l "I guess . ."
                else:
                    call LauraFace("bemused", 1)  
                    ch_l "Yeah, nice, isn't it. . ."
        elif Second == 2:
                # The other girl didn't like it
                if not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 500, "I"):
                    call LauraFace("sad", 1)  
                    ch_l "I guess. . ."
                else:
                    call LauraFace("confused", 1)  
                    ch_l "Aw, come on, it's not that bad. . ."
                    call LauraFace("sly",0)  
        $ Silent = 1
        
    if Undress:
        $ P_RecentActions.append("naked")    
    if not Silent:        
        if "cockout" in P_RecentActions:
                call LauraFace("down", 2)  
                "Laura glances down at your exposed cock"
        elif React:
                #If called by a sex dialog
                "Laura unzips your pants and draws out your cock."
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        if "cockout" not in P_RecentActions:
                $ P_RecentActions.append("cockout")
        if not ApprovalCheck("Laura", 800) and not ApprovalCheck("Laura", 400, "I"):
                    call LauraFace("surprised", Eyes="down")  
                    ch_l "Mmm?"
                    call LauraFace("angry", 1)  
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")  
                    if newgirl["Laura"].SeenPeen == 1: 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)                
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 35)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 20)
                    else:                    
                        ch_l "Dude, not cool."
                        if Action_Check("Laura", "daily", "peen") >= 2:
                                #if she's seen more than one peen today         
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)     
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                        else:
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)                
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 12)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 10)  
                    $ React = 2                           
        elif Taboo > 20 and (not ApprovalCheck("Laura", 1500) or newgirl["Laura"].SEXP < 10) and bg_current != "bg showerroom":
                call LauraFace("surprised", 2)  
                ch_l "I think there's a time and place for that sort of thing." 
                $ React = 2
                if newgirl["Laura"].SeenPeen == 1: 
                    call LauraFace("bemused", 1, Eyes="down")  
                    ch_l ". . . not that I mind, myself. . ." 
                    $ React = 1
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 30, 15) 
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 15)                
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 25)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 35)  
                call LauraFace("bemused",0)   
        elif newgirl["Laura"].SeenPeen > 10:
                return 0   
        elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                call LauraFace("sly",1) 
                if newgirl["Laura"].SeenPeen == 1: 
                    call LauraFace("surprised",1, Eyes="down")  
                    ch_l "Huh, that's a pretty good one you got there. . ."
                    call LauraFace("bemused",1)  
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 5)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10) 
                elif newgirl["Laura"].SeenPeen == 2:  
                    $ newgirl["Laura"].Eyes = "down"
                    ch_l "Oh, there it is."               
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                elif newgirl["Laura"].SeenPeen == 5: 
                    ch_l "Yeah, I've seen that one." 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7) 
                elif newgirl["Laura"].SeenPeen == 10:  
                    $ newgirl["Laura"].Eyes = "down"
                    ch_l "I don't get tired of that view."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 10)  
                $ newgirl["Laura"].Eyes = "squint" 
                $ React = 1
        else:
                call LauraFace("sad",1) 
                if newgirl["Laura"].SeenPeen == 1: 
                    call LauraFace("perplexed",1 ) 
                    ch_l "Your dick is out."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                elif newgirl["Laura"].SeenPeen < 5: 
                    call LauraFace("sad",0) 
                    ch_l "Hey. . ."
                    ch_l "You might want to put that away, [newgirl[Laura].Petname]."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)  
                elif newgirl["Laura"].SeenPeen == 10: 
                    ch_l "Yeah, yeah, waving your cock around again."               
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)   
                $ React = 2
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if newgirl["Laura"].SeenPeen > 10:
                    return 0
                elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                        if newgirl["Laura"].SeenPeen == 1: 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3) 
                        elif newgirl["Laura"].SeenPeen == 2:      
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                        elif newgirl["Laura"].SeenPeen == 5:          
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7) 
                        elif newgirl["Laura"].SeenPeen == 10: 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)  
                else:
                        if newgirl["Laura"].SeenPeen == 1: 
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                        elif newgirl["Laura"].SeenPeen < 5: 
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)  
                        elif newgirl["Laura"].SeenPeen == 10:              
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3) 
                            
    if newgirl["Laura"].SeenPeen == 1 and "angry" not in newgirl["Laura"].RecentActions:         
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 10)          
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 20)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 20) 
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10)
    
    return React
    # End Laura shown peen
    
    