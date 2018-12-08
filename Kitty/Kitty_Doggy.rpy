# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# K_Doggy_P //////////////////////////////////////////////////////////////////////

label K_Doggy_P:  
    call Shift_Focus("Kitty") from _call_Shift_Focus_309
    if K_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif K_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif K_Sex: #You've done it before
        $ Tempmod += 10    
        
    if K_Addict >= 75 and (K_CreamP + K_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif K_Addict >= 75:
        $ Tempmod += 15
        
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in K_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
    
    
        
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in K_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Kitty", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add Kitty auto stuff here
            call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_2   
            if (K_Legs == "skirt" or K_Legs == "cheerleader skirt"):
                "Kitty turns and backs up against your cock, sliding her skirt up as she does so."
                $ K_Upskirt = 1
            elif K_Legs == "pants":
                "Kitty turns and backs up against your cock, sliding her pants off as she does so."                
                $ K_Legs = 0
            else:
                "Kitty turns and backs up against your cock."
            $ K_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                    "Kitty slides it in."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_1533                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Oh yeah, [K_Pet], let's do this."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_23
                    "Kitty slides it in."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised") from _call_KittyFace_1534       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_24
                    "Kitty pulls back."
                    call KittyOutfit from _call_KittyOutfit_69
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                    return            
            jump K_Doggy_SexPrep
        else:                
            $ Tempmod = 0                               # fix, add Kitty auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_3   
        if (K_Legs == "skirt" or K_Legs == "cheerleader skirt"):
            "You press up against Kitty's backside, sliding her skirt up as you go."
            $ K_Upskirt = 1
        elif K_Legs == "pants":
            "You press up against Kitty's backside, sliding her pants down as you do."                
            $ K_Legs = 0
        else:
            "You press up against Kitty's backside."
        $ K_SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call KittyFace("surprised", 1) from _call_KittyFace_1535
        
        if (K_Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy") from _call_KittyFace_1536
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
            ch_k "Ok, [K_Petname], let's do this."            
            jump K_Doggy_SexPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1) from _call_KittyFace_1537
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_k "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump K_Doggy_SexPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1) from _call_KittyFace_1538
                    if K_Sex:
                        ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_k "Well ok, [K_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                    "You press inside some more."                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    if not ApprovalCheck("Kitty", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call KittyFace("angry") from _call_KittyFace_1539
                        "Kitty shoves you away and slaps you in the face."
                        ch_k "Jackass!"
                        ch_k "If that's how you want to treat me, we're done here!"                                                  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_2
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                    
                    else:
                        call KittyFace("sad") from _call_KittyFace_1540
                        "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump K_Doggy_SexPrep
        return             
    
   
    if not K_Sex and "no sex" not in K_RecentActions:                           #first time    
        call KittyFace("surprised", 1) from _call_KittyFace_1541
        $ K_Mouth = "kiss"
        ch_k "So, you'd like to take this to the next level? Actual sex? . . ."    
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1542
            ch_k "You'd really take it that far?"
            
            
    if not K_Sex and Approval:                                                  #First time dialog        
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1543
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -30, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -20, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_1544
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "Well, I've never been able to do this before now, so this might be fun."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_1545
            ch_k "If that's what you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_1546
            ch_k "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_1547
            $ K_Mouth = "smile"             
            ch_k "Hmm, I've always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call KittyFace("sexy", 1) from _call_KittyFace_1548
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1549
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's really what you want?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."        
        elif "sex" in K_RecentActions:
            ch_k "You want to go again? Ok."
            jump K_Doggy_SexPrep
        elif "sex" in K_DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_k "[Line]"
        elif K_Sex < 3:        
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1550
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine."  
        elif "no sex" in K_DailyActions:               
            ch_k "Ok, you've won me over on this one. . ."
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_1551
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump K_Doggy_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call KittyFace("angry") from _call_KittyFace_1552       
        if "no sex" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no sex" in K_DailyActions:  
            ch_k "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I already told you this is too public!"     
        elif not K_Sex:
            call KittyFace("bemused") from _call_KittyFace_1553
            ch_k "I just don't think I'm ready yet, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1554
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_1555
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no sex" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_1556  
                ch_k "I'll give it some thought, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no sex")                      
                $ K_DailyActions.append("no sex")            
                return
            "I think you'd enjoy it as much as I would. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_1557     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump K_Doggy_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_1558
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                    ch_k "Ok, fine. If we're going to do this, stick it in already."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1  
                    jump K_Doggy_SexPrep
                else:                          
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no sex" in K_DailyActions:
        ch_k "Learn to take \"no\" for an answer, [K_Petname]." 
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_1559
        ch_k "I'm not doing that just because you have me over a barrel."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)     
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_1560
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "Even if I wanted to, it certainly wouldn't be here!"      
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
    elif K_Sex:
        call KittyFace("sad") from _call_KittyFace_1561 
        ch_k "Maybe you could go fuck yourself instead."       
    else:
        call KittyFace("normal", 1) from _call_KittyFace_1562
        ch_k "No way."     
    $ K_RecentActions.append("no sex")                      
    $ K_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label K_Doggy_SexPrep:
    call Kitty_Doggy_Launch("hotdog") from _call_Kitty_Doggy_Launch_4
    
    if Situation != "auto":
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_14       
        
        
        if K_Panties or K_Legs or HoseNum("Kitty") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_k "Well, I guess some things are necessary, [K_Petname]."
            
        if K_Legs == "pants" and K_Panties:
            "She quickly pulls down her pants and drops her [K_Panties]."
        elif K_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Kitty") >= 5 and K_Panties:
            "She quickly pulls down her [K_Hose] and drops her [K_Panties]."
            $ K_Hose = 0
        elif HoseNum("Kitty") >= 5:
            "She quickly pulls down her [K_Hose], exposing her bare ass."
            $ K_Hose = 0
        elif K_Panties:
            "She quickly pulls down her [K_Panties]."  
            
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless from _call_Kitty_First_Bottomless_41
        
        if Taboo: # Kitty gets started. . .
            if not K_Sex:
                "Kitty glances around for voyeurs. . ."
                "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Sex:
                "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Kitty bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
        if K_Legs == "pants" and K_Panties:
            "You quickly pull down her pants and her [K_Panties] and press against her slit."
        if K_Panties and K_Legs != "pants":
            "You quickly pull down her [K_Panties] and press against her slit."  
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_42
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_34
    
    if not K_Sex:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -150)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 60)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 50) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 30)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_239
    call DrainWord("Kitty","no sex") from _call_DrainWord_240
    $ K_RecentActions.append("sex")                      
    $ K_DailyActions.append("sex") 

label K_Doggy_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_310
        call Kitty_Doggy_Launch("sex") from _call_Kitty_Doggy_Launch_5 
        call KittyLust from _call_KittyLust_23        
        $ P_Cock = "in"
        $ Trigger = "sex"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == (5 + K_Sex):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + K_Sex):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . .worn out. . . here, . . [K_Petname]."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_SexAfter from _call_K_Doggy_SexAfter
                                call K_Blowjob from _call_K_Blowjob_10       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Doggy_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_3
                                $ Situation = "shift"
                                jump K_Doggy_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_1563   
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_4
                                    "She scowls at you and pulls out."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_SexAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . ." if Speed == 2:
                                    $ Speed = 3
                                    "You start pounding her pussy as fast as you can" #pussy

                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Gag":
                            if not K_Gag:
                                #"You put a gag on Kitty"
                            #            $ K_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call K_Gagging("ballgag") from _call_K_Gagging
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call K_Gagging("ballgag") from _call_K_Gagging_1
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call K_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call K_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Kitty's gag"
                                $ K_Gag = 0

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1564 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1565 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call K_Slap_Ass from _call_K_Slap_Ass_16 
                                    hide Slap_Ass2                                    
                                    jump K_Doggy_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_25           
                        
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call K_Doggy_SexAfter from _call_K_Doggy_SexAfter_1
                                            call K_Doggy_A from _call_K_Doggy_A_1
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call K_Doggy_SexAfter from _call_K_Doggy_SexAfter_2
                                            call K_Doggy_A from _call_K_Doggy_A_2
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call K_Doggy_SexAfter from _call_K_Doggy_SexAfter_3
                                            call K_Doggy_H from _call_K_Doggy_H_1
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call K_Doggy_SexAfter from _call_K_Doggy_SexAfter_4
                                            call K_Plug_Ass from _call_K_Plug_Ass
                                    "Just stick the plug in her ass [[without asking]." if not K_Plugged:
                                            $ Situation = "auto"
                                            call K_Doggy_SexAfter from _call_K_Doggy_SexAfter_5
                                            call K_Plug_Ass from _call_K_Plug_Ass_1
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_24
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_5
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_6
                                    $ Line = 0
                                    jump K_Doggy_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_79
        
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_20
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_7
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_SexAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_Doggy"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming from _call_K_Cumming_29
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_Doggy_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Doggy_Launch(Trigger) from _call_Kitty_Doggy_Launch_6
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Doggy_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump K_Doggy_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump K_Doggy_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_1566
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_Doggy_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_8
        
    call KittyFace("sexy") from _call_KittyFace_1567 
    
    $ K_Sex += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Kitty" in K_RecentActions: #If Kitty was participating
        $ K_LikeKitty += 2 if K_LikeKitty >= 800 else 1
    
    if "Kitty Sex Addict" in Achievements:
            pass 
            
    elif K_Sex >= 10:
        $ K_SEXP += 5
        $ Achievements.append("Kitty Sex Addict")
        if not Situation:
            call KittyFace("smile", 1) from _call_KittyFace_1568
            ch_k "I think I'm getting addicted to this."               
    elif K_Sex == 1:            
            $K_SEXP += 20        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was really great, [K_Petname], we'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Did you get what you needed here?"
    elif K_Sex == 5:
            ch_k "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry") from _call_KittyFace_1569
            $ K_Eyes = "side"
            ch_k "I didn't exactly get off there. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1570
            ch_k "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_112
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////

# Gag Kitty //////////////////////////////////////////////////////////////////////////////////////

label K_Gagging(Gagtype = 0):
    if K_Gagx >= 7: # She loves it
        $ Tempmod += 20   
    elif K_Gagx >= 3: #You've done it before several times
        $ Tempmod += 17
    elif K_Gagx: #You've done it before
        $ Tempmod += 15 
        
    if K_Addict >= 75 and (K_CreamP + K_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif K_Addict >= 75: 
        $ Tempmod += 15
    
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
 
    if "exhibitionist" in K_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10      
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
        
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
            
    $ Approval = ApprovalCheck("Kitty", 1450, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    
    if Situation == "auto":   

        "You grab a ballgag and tries to put it on her mouth."
    
        call KittyFace("surprised", 1) from _call_KittyFace_1571
        
        if (K_Gagx and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and nods in agreement."
            call KittyFace("sexy") from _call_KittyFace_1572
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
            ch_k "Naughty. . ."            
            jump K_GagPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hey, what do you think you're doing?!" 
                "Sorry, sorry! I thought you'd like it.":
                    if Approval:     
                        call KittyFace("sexy", 1) from _call_KittyFace_1573
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_k "I guess if you really want to try it. . ."
                        jump K_GagPrep
                    "You take the ballgag back before you really put it on her."                    
                    call KittyFace("bemused", 1) from _call_KittyFace_1574
                    if K_Gagx:
                        ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_k "Well ok, [K_Petname], I'm not really into that, but maybe if you ask nicely next time . . ."
                    #$ K_Gagx -= 1                                               
                "Just shut up.":                    
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)
                    "You put the ballgag on her mouth."  
                    $ K_Gag = Gagtype                           
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 15)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    if not ApprovalCheck("Kitty", 700, "O", TabM=1):                        
                        call KittyFace("angry") from _call_KittyFace_1575
                        "Kitty shoves you away, take the ballgag off and throw it on your face."
                        $ K_Gag = 0
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_9
                        ch_k "You shut up!"
                        ch_k "If that's how you want to treat me, we're done here!"                                                  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                        
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")  
                        #$ K_Gagx -= 1                      
                    else:
                        $ K_Gag = Gagtype
                        call KittyFace("sad") from _call_KittyFace_1576
                        "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
        return             
    
   
    if not K_Gagx:                                                               #first time    
        call KittyFace("surprised", 1) from _call_KittyFace_1577
        $ K_Mouth = "kiss"
        ch_k "Wait, you want to put a gag in my mouth?!"
  
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1578
            ch_k "Seriously?"
        
    
    if not K_Gagx and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1579
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_1580
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess if you really want to try it. . ."           
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_1581
            ch_k "Ok, [K_Petname]."
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_1582
            ch_k "Well. . . I bet it would feel really good."
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_1583
            $ K_Mouth = "smile"             
            ch_k "Hmm, it has been on my list. . ."  
        jump K_GagPrep
    
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1584
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's really what you want?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."   
        elif K_Gagx < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_1585
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you wanna try that again?"       
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_1586
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some bondage?",                 
                "So you wanna try that again?",                 
                "I like that."]) 
            ch_k "[Line]"
        $ Line = 0
        jump K_GagPrep
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1587
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine."   
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_1588
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, shut me up.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . .",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump K_GagPrep 
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_1589
        if Taboo:
            ch_k "I already told you that I wouldn't do that out here!"  
        elif not K_Gagx:
            call KittyFace("bemused") from _call_KittyFace_1590
            ch_k "I'm just not into that, [K_Petname]. . ."
        elif K_Gagx:
            call KittyFace("perplexed") from _call_KittyFace_1591
            ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1592
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Maybe later?":
                call KittyFace("sexy") from _call_KittyFace_1593  
                ch_k "I'll give it some thought, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)  
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_1594     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    #jump K_Doggy_AnalPrep
                else:   
                    pass
                    
            "Shut it.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_1595
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                    ch_k "Ok, fine. If we're going to do this, stick it in already."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1  
                    jump K_GagPrep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)    
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    call KittyFace("angry") from _call_KittyFace_1596
                    "Kitty shoves you away."
                    $ renpy.pop_call()
                    if Situation:
                        $ renpy.pop_call()
                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_10
                    ch_k "You shut it"
                    ch_k "If that's how you want to treat me, we're done here!"                                                  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    

    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_1597
        ch_k "That's a bit much, even for you."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)       
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_1598
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "That you would even suggest such a thing in a place like this. . ."    
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3) 
    else:
        call KittyFace("normal", 1) from _call_KittyFace_1599
        ch_k "Not happening."    
    $ Tempmod = 0    
    return

# End Gag Kitty //////////////////////////////////////////////////////////////////////////////////

# K_Gag_Prep ////////////////////////////////////////////////////////////////////////////////

label K_GagPrep:    
            
    #call Kitty_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        
        if Taboo: # Kitty gets started. . .
            if K_Gagx:                
                "Kitty glances around to see if anyone notices what she's doing, then you put the ballgag on her."
                
            else:         
                "Kitty glances around for voyeurs. . ."
                $ K_Mouth = "sucking"
                "Kitty hesitantly opens her mouth."
                "You put the ballgag in her mouth."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Gagx:
                $ K_Mouth = "sucking"
                "Kitty opens her mouth wide."

                "You carefuly put the gag on her."
            else:
                $ K_Mouth = "sucking"

                "Kitty opens her mouth wide."
                "You put the gag on her."
                     
    else: #if Situation == "auto"       

        "You quickly put the ballgag on her mouth."
    $ K_Gag = Gagtype
    
    if not K_Gagx:                                                      #First time stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -150)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 70)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 40) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 70) 
    elif K_Gagx < 6:                                                   #first few times stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
        else:
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 7)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
                
    if Situation:    
        #$ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    #$ Cnt = 0
    #$ P_Cock = "anal"
    #$ Trigger = "anal"
    #$ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_241
    #call DrainWord("Kitty","no anal")
    #$ K_RecentActions.append("anal")                      
    #$ K_DailyActions.append("anal") 
    return
# End Gag Prep

# K_Doggy_A anal //////////////////////////////////////////////////////////////////////

label K_Doggy_A:
    call Shift_Focus("Kitty") from _call_Shift_Focus_311
    if K_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif K_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif K_Anal: #You've done it before
        $ Tempmod += 15 
        
    if K_Addict >= 75 and (K_CreamP + K_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif K_Addict >= 75: 
        $ Tempmod += 15
    
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if K_Loose:
        $ Tempmod += 10  
    elif "anal" in K_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in K_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in K_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10      
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
        
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in K_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in K_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Kitty", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add Kitty auto stuff here
            call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_7   
            if (K_Legs == "skirt" or K_Legs == "cheerleader skirt"):
                "Kitty turns and backs up against your cock, sliding her skirt up as she does so."
                $ K_Upskirt = 1
            elif K_Legs == "pants":
                "Kitty turns and backs up against your cock, sliding her pants off as she does so."                
                $ K_Legs = 0
            else:
                "Kitty turns and backs up against your cock."
            $ K_SeenPanties = 1
            if K_Plugged:
                "You remove the plug from her asshole"
                $ K_Plugged = 0
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                    "Kitty slides it in."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_1600                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Ooo, dirty girl, [K_Pet], let's do this."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_25
                    "Kitty slides it in."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised") from _call_KittyFace_1601       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_26
                    "Kitty pulls back."
                    call KittyOutfit from _call_KittyOutfit_70
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)                    
                    return            
            jump K_Doggy_AnalPrep
        else:                
            $ Tempmod = 0                               # fix, add Kitty auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_8   
        if (K_Legs == "skirt" or K_Legs == "cheerleader skirt"):
            "You press up against Kitty's backside, sliding her skirt up as you go."
            $ K_Upskirt = 1
        elif K_Legs == "pants":
            "You press up against Kitty's backside, sliding her pants down as you do."                
            $ K_Legs = 0
        else:
            "You press up against Kitty's backside."
        $ K_SeenPanties = 1
        if K_Plugged:
            "You remove the plug from her asshole"
            $ K_Plugged = 0
        "You press the tip of your cock against her tight rim."        
        call KittyFace("surprised", 1) from _call_KittyFace_1602
        
        if (K_Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy") from _call_KittyFace_1603
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
            if K_Plugged:
                "She removes the plug from her asshole"
                $ K_Plugged = 0
            ch_k "Hmm, stick it in. . ."            
            jump K_Doggy_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1) from _call_KittyFace_1604
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_k "I guess if you really want to try it. . ."
                        if K_Plugged:
                            ch_k "Let me just remove this first. . ."
                            "She removes the plug from her asshole"
                            $ K_Plugged = 0
                        jump K_Doggy_AnalPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1) from _call_KittyFace_1605
                    if K_Anal:
                        ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_k "Well ok, [K_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)
                    if K_Plugged:
                        "You remove the plug from her asshole and press your dick into her"
                        $ K_Plugged = 0
                    else:
                        "You press into her."                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    if not ApprovalCheck("Kitty", 700, "O", TabM=1):                        
                        call KittyFace("angry") from _call_KittyFace_1606
                        "Kitty shoves you away and slaps you in the face."
                        ch_k "Jackass!"
                        ch_k "If that's how you want to treat me, we're done here!"                                                  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_11
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                        
                    else:
                        call KittyFace("sad") from _call_KittyFace_1607
                        "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump K_Doggy_AnalPrep
        return             
    
   
    if not K_Anal and "no anal" not in K_RecentActions:                                                               #first time    
        call KittyFace("surprised", 1) from _call_KittyFace_1608
        $ K_Mouth = "kiss"
        ch_k "Wait, so you want to stick it in my butt?!"
  
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1609
            ch_k "Seriously?"
        
    if not K_Loose and ("dildo anal" in K_DailyActions or "anal" in K_DailyActions):
        call KittyFace("bemused", 1) from _call_KittyFace_1610
        ch_k "I'm still a little sore from earlier."
            
    elif "anal" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_1611
        ch_k "You want to go again? Ok."
        if K_Plugged:
            "She removes the plug from her asshole"
            $ K_Plugged = 0
        jump K_Doggy_AnalPrep
        
    
    if not K_Anal and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1612
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_1613
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess if you really want to try it. . ."           
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_1614
            ch_k "Ok, [K_Petname], I'm ready."
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_1615
            ch_k "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_1616
            $ K_Mouth = "smile"             
            ch_k "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1617
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's really what you want?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."   
        elif "anal" in K_DailyActions and not K_Loose:
            pass      
        elif "anal" in K_RecentActions:
            ch_k "I think I'm warmed up. . ."
            if K_Plugged:
                "She removes the plug from her asshole"
                $ K_Plugged = 0
            jump K_Doggy_AnalPrep
        elif "anal" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_1618
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_k "[Line]"
        elif K_Anal < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_1619
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_1620
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1621
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine."   
        elif "no anal" in K_DailyActions:               
            ch_k "Ok, ok, I have been itching for this. . ." 
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_1622
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        if K_Plugged:
            "She removes the plug from her asshole"
            $ K_Plugged = 0
        jump K_Doggy_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_1623
        if "no anal" in K_RecentActions:  
            ch_k "What part of \"no,\" did you not get, [K_Petname]?"
        elif Taboo and "tabno" in K_DailyActions and "no anal" in K_DailyActions:
            ch_k "I already told you that I wouldn't do that out here!"  
        elif "no anal" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I already told you that I wouldn't do that out here!"  
        elif not K_Anal:
            call KittyFace("bemused") from _call_KittyFace_1624
            ch_k "I'm just not into that, [K_Petname]. . ."
        elif not K_Loose and "anal" not in K_DailyActions:
            call KittyFace("perplexed") from _call_KittyFace_1625
            ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1626
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_1627
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no anal" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_1628  
                ch_k "I'll give it some thought, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)  
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no anal")                      
                $ K_DailyActions.append("no anal") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_1629     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0        
                    if K_Plugged:
                        "She removes the plug from her asshole"  
                        $ K_Plugged = 0         
                    jump K_Doggy_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_1630
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                    ch_k "Ok, fine. If we're going to do this, stick it in already."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1  
                    jump K_Doggy_AnalPrep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)    
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no anal" in K_DailyActions:
        ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_1631
        ch_k "That's a bit much, even for you."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)       
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_1632
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "That you would even suggest such a thing in a place like this. . ."    
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3) 
    elif not K_Loose and "anal" in K_DailyActions:
        call KittyFace("bemused") from _call_KittyFace_1633
        ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_Anal:
        call KittyFace("sad") from _call_KittyFace_1634 
        ch_k "The only thing you can do with my ass is kiss it, [K_Petname]."
        ch_k ". . .Don't get any ideas."   
    else:
        call KittyFace("normal", 1) from _call_KittyFace_1635
        ch_k "Not happening."    
    $ K_RecentActions.append("no anal")                      
    $ K_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label K_Plug_Ass:
    call Shift_Focus("Kitty") from _call_Shift_Focus_312
      
    if K_Loose:
        $ Tempmod += 30   
    elif "anal" in K_RecentActions or "plug anal" in K_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in K_DailyActions or "plug anal" in K_DailyActions:
        $ Tempmod -= 10
    elif (K_Anal + K_DildoA + K_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if K_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if K_Lust > 95:
        $ Tempmod += 20
    elif K_Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:        
        $ Tempmod += (5*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount   
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no plug" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no plug" in K_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Kitty", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            call Kitty_Doggy_Launch("plug") from _call_Kitty_Doggy_Launch_9 
        
            if Approval > 2:                                                      # fix, add Kitty auto stuff here
                if K_Legs == "skirt":
                    "Kitty grabs her plug, hiking up her skirt as she does."
                    $ K_Upskirt = 1
                elif K_Legs == "pants":
                    "Kitty grabs her plug, pulling down her pants as she does."              
                    $ K_Legs = 0
                else:
                    "Kitty grabs her plug, rubbing it suggestively against her ass."
                $ K_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                        "Kitty slides it in."
                    "Go for it.":       
                        call KittyFace("sexy, 1") from _call_KittyFace_1636                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        ch_p "Oh yeah, [K_Pet], let's do this."
                        call Kitty_Namecheck from _call_Kitty_Namecheck_27
                        "You grab the plug and slide it in."
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised") from _call_KittyFace_1637       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck from _call_Kitty_Namecheck_28
                        "Kitty sets the plug down."
                        call KittyOutfit from _call_KittyOutfit_71
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                        return            
                jump KPA_Prep
            else:                
                $ Tempmod = 0                               # fix, add Kitty auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            call Kitty_Doggy_Launch("massage") from _call_Kitty_Doggy_Launch_10  

            "You rub the plug across her body, and against her tight anus."
            call KittyFace("surprised", 1) from _call_KittyFace_1638
            
            if (K_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call KittyFace("sexy") from _call_KittyFace_1639
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                ch_k "Ok, [K_Petname], let's do this."            
                jump KPA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ K_Brows = "angry"                
                menu:
                    ch_k "Hey, what do you think you're doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call KittyFace("sexy", 1) from _call_KittyFace_1640
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_k "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                            jump KPA_Prep
                        "You pull back before you really get it in."                    
                        call KittyFace("bemused", 1) from _call_KittyFace_1641
                        if K_DildoA:
                            ch_k "Well ok, [K_Petname], no harm done. Just give me a little warning next time." 
                        else:
                            ch_k "Well ok, [K_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                    "Just playing with my favorite toys.":                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                        "You press it inside some more."                              
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        if not ApprovalCheck("Kitty", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call KittyFace("angry") from _call_KittyFace_1642
                            "Kitty shoves you away and slaps you in the face."
                            ch_k "Jackass!"
                            ch_k "If that's how you want to treat me, we're done here!"                                                  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            if K_Plugged:
                                "She removes the plug from her asshole"
                                $ K_Plugged = 0
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Kitty_Doggy"):
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_12  
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                         
                        else:
                            call KittyFace("sad") from _call_KittyFace_1643
                            "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump KPA_Prep
            return             
    #end auto
   
    if not K_DildoA:                                                               
            #first time    
            call KittyFace("surprised", 1) from _call_KittyFace_1644
            $ K_Mouth = "kiss"
            ch_k "Hmmm, so you'd like to try out some toys?"    
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_1645
                ch_k "You had to go for the butt, uh?"
    
    if not K_Loose and ("dildo anal" in K_RecentActions or "plug anal" in K_RecentActions or "anal" in K_RecentActions or "dildo anal" in K_DailyActions or "plug anal" in K_DailyActions or "anal" in K_DailyActions):
            call KittyFace("bemused", 1) from _call_KittyFace_1646
            ch_k "I'm still a bit sore from earlier. . ."
            
    if not K_DildoA and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_1647
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy") from _call_KittyFace_1648
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I haven't actually used one of these, back there before. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal") from _call_KittyFace_1649
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad") from _call_KittyFace_1650
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_1651
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "The toys again?"  
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "plug anal" in K_DailyActions and not K_Loose:
                pass
            elif "plug anal" in K_DailyActions:
                call KittyFace("sexy", 1) from _call_KittyFace_1652
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoA < 3:        
                call KittyFace("sexy", 1) from _call_KittyFace_1653
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my ass again?"       
            else:       
                call KittyFace("sexy", 1) from _call_KittyFace_1654
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"]) 
                ch_k "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_1655
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            else:
                call KittyFace("sexy", 1) from _call_KittyFace_1656
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_k "[Line]"
                $ Line = 0
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
            jump KPA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry") from _call_KittyFace_1657
            if "no plug" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no plug" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"  
            elif "no plug" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you that I wouldn't do that out here!"  
            elif not K_DildoA:
                call KittyFace("bemused") from _call_KittyFace_1658
                ch_k "I'm just not into toys, [K_Petname]. . ."
            elif not K_Loose and "plug anal" not in K_DailyActions:
                call KittyFace("perplexed") from _call_KittyFace_1659
                ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
            else:
                call KittyFace("bemused") from _call_KittyFace_1660
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no plug" in K_DailyActions:
                    call KittyFace("bemused") from _call_KittyFace_1661
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no plug" not in K_DailyActions:
                    call KittyFace("sexy") from _call_KittyFace_1662  
                    ch_k "Maybe I'll practice on my own time, [K_Petname]."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)  
                    if Taboo:                    
                        $ K_RecentActions.append("tabno")                      
                        $ K_DailyActions.append("tabno") 
                    $ K_RecentActions.append("no plug")                      
                    $ K_DailyActions.append("no plug") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call KittyFace("sexy") from _call_KittyFace_1663     
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump KPA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad") from _call_KittyFace_1664
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                        ch_k "Ok, fine. If we're going to do this, stick it in already."  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                        $ K_Forced = 1  
                        jump KPA_Prep
                    else:                              
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1   
    if "no plug" in K_DailyActions:
            ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif K_Forced:
            call KittyFace("angry", 1) from _call_KittyFace_1665
            ch_k "I'm not going to let you use that on me."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1) from _call_KittyFace_1666          
            $ K_RecentActions.append("tabno")                       
            $ K_DailyActions.append("tabno") 
            ch_k "Not here!"     
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif not K_Loose and "plug anal" in K_DailyActions:
            call KittyFace("bemused") from _call_KittyFace_1667
            ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_DildoA:
            call KittyFace("sad") from _call_KittyFace_1668 
            ch_k "Sorry, you can keep your toys out of there."     
    else:
            call KittyFace("normal", 1) from _call_KittyFace_1669
            ch_k "No way." 
    $ K_RecentActions.append("no plug")                      
    $ K_DailyActions.append("no plug")   
    $ Tempmod = 0    
    return

label KPA_Prep:  
            
    call Kitty_Doggy_Launch("massage") from _call_Kitty_Doggy_Launch_11
    
    if Situation != "auto":
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_15        
        if K_Panties or K_Legs or HoseNum("Kitty") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_k "Well, I guess some things are necessary, [K_Petname]."
            
        if K_Legs == "pants" and K_Panties:
            "She quickly pulls down her pants and drops her [K_Panties]."
        elif K_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Kitty") >= 5 and K_Panties:
            "She quickly pulls down her [K_Hose] and drops her [K_Panties]."
            $ K_Hose = 0
        elif HoseNum("Kitty") >= 5:
            "She quickly pulls down her [K_Hose], exposing her bare ass."
            $ K_Hose = 0
        elif K_Panties:
            "She quickly pulls down her [K_Panties]."  
            
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless from _call_Kitty_First_Bottomless_43
        
        if Taboo: # Kitty gets started. . .
            if K_Anal:                
                "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against the plug."
                #"You guide your cock into place and ram it home."   
                
            else:         
                "Kitty glances around for voyeurs. . ."
                "Kitty slowly backs up against the plug."
                #"You guide it into place and slide it in."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Anal:
                "Kitty bends over and presses her backside against the plug suggestively."
                #"You take careful aim and then push your cock in."
            else:
                "Kitty slowly backs up against the plug."
                #"You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if K_Legs == "pants" and K_Panties:
            "You quickly pull down her pants and her [K_Panties] and press the plug against her ass."
        if K_Panties and K_Legs != "pants":
            "You quickly pull down her [K_Panties] and press the plug against her ass."  
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_44
        
    #call Seen_First_Peen(1)
    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_13
    call Kitty_Doggy_Launch("plug") from _call_Kitty_Doggy_Launch_12
    
    if not K_Anal:                                                      #First time stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -150)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 70)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 40) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 70) 
    elif not K_Loose:                                                   #first few times stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
        else:
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 7)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "plug"
    $ Trigger = "plug"
    $ Speed = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_242
    call DrainWord("Kitty","no anal") from _call_DrainWord_243
    $ K_RecentActions.append("plug anal")                      
    $ K_DailyActions.append("plug anal")


label K_Anal_Plug_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_313
        call Kitty_Doggy_Launch("plug") from _call_Kitty_Doggy_Launch_13 
        call KittyLust from _call_KittyLust_24        
        $ P_Cock = "plug"
        $ Trigger = "plug"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + K_Anal):
                    $ K_Brows = "confused"
                    ch_k "Can you finish there? I'm getting a little sore."   
        elif Cnt == (10 + K_Anal):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . .worn out. . . here, . . [K_Petname]."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "Let's try something else." if MultiAction: 
                                if Speed != 0:
                                    "But keep the plug inside you."
                                    $ K_Plugged = 1
                                    $ Speed = 0
                                $ Line = 0
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_14
                                $ Situation = "shift"
                                jump K_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_1670   
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_15
                                    "She scowls at you and pulls out."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    if K_Plugged:
                                        "She removes the plug from her asshole"
                                        $ K_Plugged = 0
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_AnalAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Gag":
                            if not K_Gag:
                                #"You put a gag on Kitty"
                            #            $ K_Gag = "ballgag"
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call K_Gagging("ballgag") from _call_K_Gagging_2
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call K_Gagging("ballgag") from _call_K_Gagging_3
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call K_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call K_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Kitty's gag"
                                $ K_Gag = 0
                           
                        #"Leave it in" if Speed:                    
                        #            $ Speed = 2
                        #            $ K_Plugged = 1
                        #            "You leave the plug inside her ass."

                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call K_Slap_Ass from _call_K_Slap_Ass_17 
                                    hide Slap_Ass2                                    
                                    jump K_Anal_Plug_Cycle  
                                    
                           
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_26             
                        
                        "Shift actions":
                            if K_Action and MultiAction:
                                if Speed != 0:
                                    "You leave the plug inside her asshole"
                                    $ K_Plugged = 1
                                    $ Speed = 0
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter
                                            call K_Doggy_P from _call_K_Doggy_P_1
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_1
                                            call K_Doggy_P from _call_K_Doggy_P_2
                                    "Start hotdogging her.":
                                            $ Situation = "pullback"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_2
                                            call K_Doggy_H from _call_K_Doggy_H_2
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter
                                            call K_Doggy_A from _call_K_Doggy_A_3
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_1
                                            call K_Doggy_A from _call_K_Doggy_A_4
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_25
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    menu:
                                        "And keep the plug inside":
                                            $ K_Plugged = 1
        
                                        "And you can remove the plug":
                                            $ K_Plugged = 0
        
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_16
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction:
                                    menu:
                                        "But keep the plug inside":
                                            $ K_Plugged = 1
        
                                        "And you can remove the plug":
                                            $ K_Plugged = 0
         
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_17
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_80
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_21
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_18
                                if K_Plugged:
                                    "She removes the plug from her asshole"
                                    $ K_Plugged = 0
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_Doggy"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming from _call_K_Cumming_30
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_Doggy_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Doggy_Launch(Trigger) from _call_Kitty_Doggy_Launch_14
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Anal_Plug_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump K_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump K_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_1671
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."

    return


label K_Doggy_AnalPrep:  
            
    call Kitty_Doggy_Launch("hotdog") from _call_Kitty_Doggy_Launch_15
    
    if Situation != "auto":
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_16        
        if K_Panties or K_Legs or HoseNum("Kitty") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_k "Well, I guess some things are necessary, [K_Petname]."
            
        if K_Legs == "pants" and K_Panties:
            "She quickly pulls down her pants and drops her [K_Panties]."
        elif K_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Kitty") >= 5 and K_Panties:
            "She quickly pulls down her [K_Hose] and drops her [K_Panties]."
            $ K_Hose = 0
        elif HoseNum("Kitty") >= 5:
            "She quickly pulls down her [K_Hose], exposing her bare ass."
            $ K_Hose = 0
        elif K_Panties:
            "She quickly pulls down her [K_Panties]."  
            
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless from _call_Kitty_First_Bottomless_45
        
        if K_Plugged:
            "She removes the plug from her asshole."
            $ K_Plugged = 0


        if Taboo: # Kitty gets started. . .
            if K_Anal:                
                "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Kitty glances around for voyeurs. . ."
                "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Anal:
                "Kitty bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if K_Legs == "pants" and K_Panties:
            "You quickly pull down her pants and her [K_Panties] and press against her ass."
        if K_Panties and K_Legs != "pants":
            "You quickly pull down her [K_Panties] and press against her ass."  
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_46
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_35
    
    if not K_Anal:                                                      #First time stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -150)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 70)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 40) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 70) 
    elif not K_Loose:                                                   #first few times stat buffs       
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
        else:
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 7)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_244
    call DrainWord("Kitty","no anal") from _call_DrainWord_245
    $ K_RecentActions.append("anal")                      
    $ K_DailyActions.append("anal") 

label K_Doggy_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_314
        call Kitty_Doggy_Launch("anal") from _call_Kitty_Doggy_Launch_16 
        call KittyLust from _call_KittyLust_25        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + K_Anal):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + K_Anal):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . .worn out. . . here, . . [K_Petname]."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                if K_Anal >= 5 and K_Blow >= 10 and K_SEXP >= 50:
                                    $ Situation = "shift"
                                    call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_3
                                    call K_Blowjob from _call_K_Blowjob_11      
                                else:
                                    ch_k "No thanks, [K_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_4
                                    call KHJ_Prep from _call_KHJ_Prep_2   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_5
                                call K_Handjob from _call_K_Handjob_7     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Doggy_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_19
                                $ Situation = "shift"
                                jump K_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_1672   
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_20
                                    "She scowls at you and pulls out."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_AnalAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . ." if Speed == 2:
                                    $ Speed = 3  #anal
                                    "You start pounding her ass as fast as you can"

                        "Balls deep." if Speed == 3 :                    
                                    $ Speed = 4
                                    "You go balls deep."
                        
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Gag":
                            if not K_Gag:
                                #"You put a gag on Kitty"
                            #            $ K_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call K_Gagging("ballgag") from _call_K_Gagging_4
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call K_Gagging("ballgag") from _call_K_Gagging_5
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call K_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call K_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Kitty's gag"
                                $ K_Gag = 0

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1673 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1674 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call K_Slap_Ass from _call_K_Slap_Ass_18 
                                    hide Slap_Ass2                                   
                                    jump K_Doggy_Anal_Cycle  

                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                           
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_27             
                        
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_6
                                            call K_Doggy_P from _call_K_Doggy_P_3
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_7
                                            call K_Doggy_P from _call_K_Doggy_P_4
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_8
                                            call K_Doggy_H from _call_K_Doggy_H_3
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_9
                                            call K_Plug_Ass from _call_K_Plug_Ass_2
                                    "Just stick the plug in her ass [[without asking]." if not K_Plugged:
                                            $ Situation = "auto"
                                            call K_Doggy_AnalAfter from _call_K_Doggy_AnalAfter_10
                                            call K_Plug_Ass from _call_K_Plug_Ass_3
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_26
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_21
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_22
                                    $ Line = 0
                                    jump K_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_81
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_22
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_23
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_Doggy"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming from _call_K_Cumming_31
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_Doggy_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Doggy_Launch(Trigger) from _call_Kitty_Doggy_Launch_17
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Doggy_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump K_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump K_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_1675
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_Doggy_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_24
        
    call KittyFace("sexy") from _call_KittyFace_1676 
    
    $ K_Anal += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 3) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Kitty" in K_RecentActions: #If Kitty was participating
        $ K_LikeKitty += 2 if K_LikeKitty >= 800 else 1
    
    if "Kitty Anal Addict" in Achievements:
            pass 
            
    elif K_Anal >= 10:
        $ K_SEXP += 7
        $ Achievements.append("Kitty Anal Addict")
        if not Situation:
            call KittyFace("bemused", 1) from _call_KittyFace_1677
            ch_k "I. . . really think I enjoy this. . ."                  
    elif K_Anal == 1:            
            $K_SEXP += 25        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was . . . interesting [K_Petname]. We'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Ouch."
                    ch_k "Did you get what you needed here?"
    elif K_Anal == 5:
            ch_k "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry") from _call_KittyFace_1678
            $ K_Eyes = "side"
            ch_k  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1679
            ch_k "That felt . . . good. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_113
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# K_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label K_Doggy_H: 
    call Shift_Focus("Kitty") from _call_Shift_Focus_315
    if K_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif K_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if K_Lust > 85:
        $ Tempmod += 10
    elif K_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in K_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 40 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount 
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in K_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Kitty", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add Kitty auto stuff here
            call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_18 
            "Kitty turns and backs up against your cock, rubbing it against her ass."
            menu:
                "What do you do?"
                "Nothing.":                     
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                    "Kitty starts to grind against you."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_1680                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
                    ch_p "Hmmm, that's good, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_29
                    "Kitty starts to grind against you."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)
                "Ask her to stop.":
                    call KittyFace("surprised") from _call_KittyFace_1681       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_30
                    "Kitty pulls back."
                    call KittyOutfit from _call_KittyOutfit_72
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)                    
                    return            
            jump K_Doggy_HotdogPrep
        else:                
            $ Tempmod = 0                               # fix, add Kitty auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Kitty_Doggy_Launch("L") from _call_Kitty_Doggy_Launch_19   
        "You press up against Kitty's backside."    
        call KittyFace("surprised", 1) from _call_KittyFace_1682
        
        if (K_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call KittyFace("sexy") from _call_KittyFace_1683
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
            ch_k "Hmm, I've apparently got someone's attention. . ."            
            jump K_Doggy_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ K_Brows = "angry"                
            menu:
                ch_k "Hmm, kinda rude, [K_Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call KittyFace("sexy", 1) from _call_KittyFace_1684
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_k "I guess it doesn't feel so bad. . ."
                        jump K_Doggy_HotdogPrep
                    "You pull back before you really get it in."                    
                    call KittyFace("bemused", 1) from _call_KittyFace_1685
                    if K_Hotdog:
                        ch_k "Well ok, [K_Petname], it has been kinda fun." 
                    else:
                        ch_k "Well ok, [K_Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)
                    "You grind against her asscrack."                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    if not ApprovalCheck("Kitty", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call KittyFace("angry") from _call_KittyFace_1686
                        "Kitty shoves you away."
                        ch_k "Dick!"
                        ch_k "If that's how you want want to act, I'm out of here!"                                                  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_25
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")                       
                    else:
                        call KittyFace("sad") from _call_KittyFace_1687
                        "Kitty doesn't seem to be into this, but she's knows her place."                        
                        jump K_Doggy_HotdogPrep
        return             
    
   
    if not K_Hotdog and "no hotdog" not in K_RecentActions:                                                               #first time    
        call KittyFace("surprised", 1) from _call_KittyFace_1688
        $ K_Mouth = "kiss"
        ch_k "Wait, so you want to grind against my butt?!"
  
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1689
            ch_k ". . . That's all?"
        
        
    if not K_Hotdog and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1690
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_1691
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "It looks like you need some relief. . ."           
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_1692
            ch_k "If that's what you need, [K_Petname]."
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_1693
            ch_k "Hmmm. . ."
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_1694
            $ K_Mouth = "smile"             
            ch_k "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_1695
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's all you want?"  
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in K_RecentActions:
            call KittyFace("sexy", 1) from _call_KittyFace_1696
            ch_k "You want to go again? Ok."
            jump K_Doggy_HotdogPrep
        elif "hotdog" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_1697
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_k "[Line]"
        elif K_Hotdog < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_1698
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another go?"       
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_1699
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_1700
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine."    
        elif "no hotdog" in K_DailyActions:               
            ch_k "Well, I guess it's not so bad. . ."
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_1701
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump K_Doggy_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_1702
        if "no hotdog" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no hotdog" in K_DailyActions: 
            ch_k "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in K_DailyActions:       
            ch_k "I told you \"no\" earlier, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I told you that I didn't want you rubb'in up on me in public!"     
        elif not K_Hotdog:
            call KittyFace("bemused") from _call_KittyFace_1703
            ch_k "That's kinda naughty, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1704
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_1705
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no hotdog" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_1706  
                ch_k "Yeah, maybe, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no hotdog")                      
                $ K_DailyActions.append("no hotdog")                          
                return
            "You might like it. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_1707     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump K_Doggy_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_1708
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, fine. Whatever."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                    $ K_Forced = 1  
                    jump K_Doggy_HotdogPrep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1      
    
    if "no hotdog" in K_DailyActions:
        ch_k "I just don't want to, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    if K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_1709
        ch_k "Even that's not worth it."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -1) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1)  
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_1710        
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "I'd be a bit embarassed doing that here."  
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_Hotdog:
        call KittyFace("sad") from _call_KittyFace_1711 
        ch_k "Eh-eh, not anymore, [K_Petname]."
    else:
        call KittyFace("normal", 1) from _call_KittyFace_1712
        ch_k "Not interested."    
    $ K_RecentActions.append("no hotdog")                      
    $ K_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label K_Doggy_HotdogPrep:  
    call Kitty_Doggy_Launch("hotdog") from _call_Kitty_Doggy_Launch_20
    
    if Situation != "auto":
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_17    
        
        if Taboo: # Kitty gets started. . .
            if K_Hotdog:                
                "Kitty glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                
            else:         
                "Kitty glances around for voyeurs. . ."
                "Kitty hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Hotdog:
                "Kitty bends over and presses her backside against you suggestively."
            else:
                "Kitty hesitantly pulls down your pants slowly backs up against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her ass."
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_36

    if not K_Hotdog:                                                      #First time stat buffs      
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_246
    call DrainWord("Kitty","no hotdog") from _call_DrainWord_247
    $ K_RecentActions.append("hotdog")                      
    $ K_DailyActions.append("hotdog") 

label K_Doggy_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_316
        call Kitty_Doggy_Launch("hotdog") from _call_Kitty_Doggy_Launch_21 
        call KittyLust from _call_KittyLust_26        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + K_Hotdog):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here?"   
        elif Cnt == (10 + K_Hotdog):
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "I'm kinda done with this, [K_Petname]."
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_2
                                call K_Blowjob from _call_K_Blowjob_12       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Doggy_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_26
                                $ Situation = "shift"
                                jump K_Doggy_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_1713   
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_27
                                    "She scowls at you and pulls away."
                                    ch_k "Well if that's your attitude you can handle your own business."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_Doggy_HotdogAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Gag":
                            if not K_Gag:
                                #"You put a gag on Kitty"
                            #            $ K_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call K_Gagging("ballgag") from _call_K_Gagging_6
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call K_Gagging("ballgag") from _call_K_Gagging_7
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call K_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call K_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Kitty's gag"
                                $ K_Gag = 0

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1714 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_1715 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call K_Slap_Ass from _call_K_Slap_Ass_19 
                                    hide Slap_Ass2                                   
                                    jump K_Doggy_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                          
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_28    
                                    
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_3
                                        call K_Doggy_P from _call_K_Doggy_P_5
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_4
                                        call K_Doggy_P from _call_K_Doggy_P_6
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_5
                                        call K_Doggy_A from _call_K_Doggy_A_5
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_6
                                        call K_Doggy_A from _call_K_Doggy_A_6
                                    "How about the plug?":
                                        $ Situation = "shift"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_7
                                        call K_Plug_Ass from _call_K_Plug_Ass_4
                                    "Just stick the plug in her ass [[without asking]." if not K_Plugged:
                                        $ Situation = "auto"
                                        call K_Doggy_HotdogAfter from _call_K_Doggy_HotdogAfter_8
                                        call K_Plug_Ass from _call_K_Plug_Ass_5
                                    "Never Mind":
                                        pass
                            else:
                                ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_27
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_28
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_Doggy_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_29
                                    $ Line = 0
                                    jump K_Doggy_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_82
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_23
                            if "angry" in K_RecentActions:  
                                call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_30
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_Doggy_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_Doggy"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming from _call_K_Cumming_32
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_Doggy_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_Doggy_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Doggy_Launch("hotdog") from _call_Kitty_Doggy_Launch_22
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Doggy_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump K_Doggy_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump K_Doggy_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_1716
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_Doggy_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Doggy_Reset from _call_Kitty_Doggy_Reset_31
        
    call KittyFace("sexy") from _call_KittyFace_1717 
    
    $ K_Hotdog += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Kitty" in K_RecentActions: #If Kitty was participating
        $ K_LikeKitty += 1
    
    if "Kitty Full Buns" in Achievements:
            pass 
            
    elif K_Hotdog >= 10:
        $ K_SEXP += 5
        $ Achievements.append("Kitty Full Buns")
        if not Situation:
            call KittyFace("smile", 1) from _call_KittyFace_1718
            ch_k "I think I'm getting addicted to this."               
    elif K_Hotdog == 1:            
            $K_SEXP += 10        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was pretty hot, [K_Petname], we'll have to do that again sometime."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Did you get what you needed here?"
    elif K_Hotdog == 5:
            ch_k "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry") from _call_KittyFace_1719
            $ K_Eyes = "side"
            ch_k "That didn't really do it for me. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_1720
            ch_k "That was an interesting diversion. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_114
    return   

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////

    
    