# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# E_Doggy_P //////////////////////////////////////////////////////////////////////

label E_Doggy_P:  
    call Shift_Focus("Emma") from _call_Shift_Focus_194
    if E_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif E_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif E_Sex: #You've done it before
        $ Tempmod += 10    
        
    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif E_Addict >= 75:
        $ Tempmod += 15
        
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in E_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
    
    
        
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in E_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Emma", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_2   
            if (E_Legs == "skirt" or E_Legs == "cheerleader skirt"):
                "Emma turns and backs up against your cock, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "pants":
                "Emma turns and backs up against your cock, sliding her pants off as she does so."                
                $ E_Legs = 0
            else:
                "Emma turns and backs up against your cock."
            $ E_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                    "Emma slides it in."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_1343                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    ch_p "Oh yeah, [E_Pet], let's do this."
                    call Emma_Namecheck from _call_Emma_Namecheck_21
                    "Emma slides it in."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised") from _call_EmmaFace_1344       
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_22
                    "Emma pulls back."
                    call EmmaOutfit from _call_EmmaOutfit_61
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    return            
            jump E_Doggy_SexPrep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_3   
        if (E_Legs == "skirt" or E_Legs == "cheerleader skirt"):
            "You press up against Emma's backside, sliding her skirt up as you go."
            $ E_Upskirt = 1
        elif E_Legs == "pants":
            "You press up against Emma's backside, sliding her pants down as you do."                
            $ E_Legs = 0
        else:
            "You press up against Emma's backside."
        $ E_SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call EmmaFace("surprised", 1) from _call_EmmaFace_1345
        
        if (E_Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy") from _call_EmmaFace_1346
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
            ch_e "Ok, [E_Petname], let's do this."            
            jump E_Doggy_SexPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1) from _call_EmmaFace_1347
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_e "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump E_Doggy_SexPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1) from _call_EmmaFace_1348
                    if E_Sex:
                        ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_e "Well ok, [E_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                    "You press inside some more."                              
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    if not ApprovalCheck("Emma", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call EmmaFace("angry") from _call_EmmaFace_1349
                        "Emma shoves you away and slaps you in the face."
                        ch_e "Jackass!"
                        ch_e "If that's how you want to treat me, we're done here!"                                                  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_2
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                    
                    else:
                        call EmmaFace("sad") from _call_EmmaFace_1350
                        "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump E_Doggy_SexPrep
        return             
    
   
    if not E_Sex and "no sex" not in E_RecentActions:                           #first time    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1351
        $ E_Mouth = "kiss"
        ch_e "So, you'd like to take this to the next level? Actual sex? . . ."    
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1352
            ch_e "You'd really take it that far?"
            
            
    if not E_Sex and Approval:                                                  #First time dialog        
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1353
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -30, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -20, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_1354
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "Well, I've never been able to do this before now, so this might be fun."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_1355
            ch_e "If that's what you want, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_1356
            ch_e "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_1357
            $ E_Mouth = "smile"             
            ch_e "Hmm, I've always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call EmmaFace("sexy", 1) from _call_EmmaFace_1358
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1359
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's really what you want?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."        
        elif "sex" in E_RecentActions:
            ch_e "You want to go again? Ok."
            jump E_Doggy_SexPrep
        elif "sex" in E_DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_e "[Line]"
        elif E_Sex < 3:        
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1360
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine."  
        elif "no sex" in E_DailyActions:               
            ch_e "Ok, you've won me over on this one. . ."
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1361
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_Doggy_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call EmmaFace("angry") from _call_EmmaFace_1362       
        if "no sex" in E_RecentActions:  
            ch_e "I {i}just{/i} told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no sex" in E_DailyActions:  
            ch_e "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in E_DailyActions:       
            ch_e "I already told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I already told you this is too public!"     
        elif not E_Sex:
            call EmmaFace("bemused") from _call_EmmaFace_1363
            ch_e "I just don't think I'm ready yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1364
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1365
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no sex" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1366  
                ch_e "I'll give it some thought, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no sex")                      
                $ E_DailyActions.append("no sex")            
                return
            "I think you'd enjoy it as much as I would. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_1367     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_Doggy_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1368
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                    ch_e "Ok, fine. If we're going to do this, stick it in already."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1  
                    jump E_Doggy_SexPrep
                else:                          
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no sex" in E_DailyActions:
        ch_e "Learn to take \"no\" for an answer, [E_Petname]." 
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1369
        ch_e "I'm not doing that just because you have me over a barrel."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_1370
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "Even if I wanted to, it certainly wouldn't be here!"      
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
    elif E_Sex:
        call EmmaFace("sad") from _call_EmmaFace_1371 
        ch_e "Maybe you could go fuck yourself instead."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_1372
        ch_e "No way."     
    $ E_RecentActions.append("no sex")                      
    $ E_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label E_Doggy_SexPrep:
    call Emma_Doggy_Launch("hotdog") from _call_Emma_Doggy_Launch_4
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_14       
        
        
        if E_Panties or E_Legs or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_e "Well, I guess some things are necessary, [E_Petname]."
            
        if E_Legs == "pants" and E_Panties:
            "She quickly pulls down her pants and drops her [E_Panties]."
        elif E_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Emma") >= 5 and E_Panties:
            "She quickly pulls down her [E_Hose] and drops her [E_Panties]."
            $ E_Hose = 0
        elif HoseNum("Emma") >= 5:
            "She quickly pulls down her [E_Hose], exposing her bare ass."
            $ E_Hose = 0
        elif E_Panties:
            "She quickly pulls down her [E_Panties]."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless from _call_Emma_First_Bottomless_22
        
        if Taboo: # Emma gets started. . .
            if not E_Sex:
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Sex:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Emma bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
        if E_Legs == "pants" and E_Panties:
            "You quickly pull down her pants and her [E_Panties] and press against her slit."
        if E_Panties and E_Legs != "pants":
            "You quickly pull down her [E_Panties] and press against her slit."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_23
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_18
    
    if not E_Sex:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -150)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 60)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 50) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 30)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_156
    call DrainWord("Emma","no sex") from _call_DrainWord_157
    $ E_RecentActions.append("sex")                      
    $ E_DailyActions.append("sex") 

label E_Doggy_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_195
        call Emma_Doggy_Launch("sex") from _call_Emma_Doggy_Launch_5 
        call EmmaLust from _call_EmmaLust_21        
        $ P_Cock = "in"
        $ Trigger = "sex"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == (5 + E_Sex):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + E_Sex):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . .worn out. . . here, . . [E_Petname]."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_SexAfter from _call_E_Doggy_SexAfter
                                call E_Blowjob from _call_E_Blowjob_8       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Doggy_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_3
                                $ Situation = "shift"
                                jump E_Doggy_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1373   
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_4
                                    "She scowls at you and pulls out."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_SexAfter
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
                            if not E_Gag:
                                #"You put a gag on Emma"
                            #            $ E_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call E_Gagging("ballgag") from _call_E_Gagging
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call E_Gagging("ballgag") from _call_E_Gagging_1
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call E_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call E_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Emma's gag"
                                $ E_Gag = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call E_Slap_Ass from _call_E_Slap_Ass_15 
                                    hide Slap_Ass2                                    
                                    jump E_Doggy_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_22           
                        
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call E_Doggy_SexAfter from _call_E_Doggy_SexAfter_1
                                            call E_Doggy_A from _call_E_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call E_Doggy_SexAfter from _call_E_Doggy_SexAfter_2
                                            call E_Doggy_A from _call_E_Doggy_A_1
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call E_Doggy_SexAfter from _call_E_Doggy_SexAfter_3
                                            call E_Doggy_H from _call_E_Doggy_H
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call E_Doggy_SexAfter from _call_E_Doggy_SexAfter_4
                                            call E_Plug_Ass from _call_E_Plug_Ass
                                    "Just stick the plug in her ass [[without asking]." if not E_Plugged:
                                            $ Situation = "auto"
                                            call E_Doggy_SexAfter from _call_E_Doggy_SexAfter_5
                                            call E_Plug_Ass from _call_E_Plug_Ass_1
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_24
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_5
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_6
                                    $ Line = 0
                                    jump E_Doggy_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_47
        
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_18
                            if "angry" in E_RecentActions:  
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_7
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_SexAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if renpy.showing("Emma_Doggy"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_29
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Doggy_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Doggy_Launch(Trigger) from _call_Emma_Doggy_Launch_6
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Doggy_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump E_Doggy_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump E_Doggy_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_1374
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Doggy_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_8
        
    call EmmaFace("sexy") from _call_EmmaFace_1375 
    
    $ E_Sex += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if E_Loc == bg_current and "noticed Emma" in E_RecentActions: #If Emma was participating
        $ E_LikeEmma += 2 if E_LikeEmma >= 800 else 1
    
    if "Emma Sex Addict" in Achievements:
            pass 
            
    elif E_Sex >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not Situation:
            call EmmaFace("smile", 1) from _call_EmmaFace_1376
            ch_e "I think I'm getting addicted to this."               
    elif E_Sex == 1:            
            $E_SEXP += 20        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was really great, [E_Petname], we'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Did you get what you needed here?"
    elif E_Sex == 5:
            ch_e "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_1377
            $ E_Eyes = "side"
            ch_e "I didn't exactly get off there. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1378
            ch_e "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_76
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////

# Gag Emma //////////////////////////////////////////////////////////////////////////////////////

label E_Gagging(Gagtype = 0):
    if E_Gagx >= 7: # She loves it
        $ Tempmod += 20   
    elif E_Gagx >= 3: #You've done it before several times
        $ Tempmod += 17
    elif E_Gagx: #You've done it before
        $ Tempmod += 15 
        
    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif E_Addict >= 75: 
        $ Tempmod += 15
    
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
 
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10      
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
        
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
            
    $ Approval = ApprovalCheck("Emma", 1450, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    
    if Situation == "auto":   

        "You grab a ballgag and tries to put it on her mouth."
    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1379
        
        if (E_Gagx and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and nods in agreement."
            call EmmaFace("sexy") from _call_EmmaFace_1380
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
            ch_e "Naughty. . ."            
            jump E_GagPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hey, what do you think you're doing?!" 
                "Sorry, sorry! I thought you'd like it.":
                    if Approval:     
                        call EmmaFace("sexy", 1) from _call_EmmaFace_1381
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_e "I guess if you really want to try it. . ."
                        jump E_GagPrep
                    "You take the ballgag back before you really put it on her."                    
                    call EmmaFace("bemused", 1) from _call_EmmaFace_1382
                    if E_Gagx:
                        ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_e "Well ok, [E_Petname], I'm not really into that, but maybe if you ask nicely next time . . ."
                    #$ E_Gagx -= 1                                               
                "Just shut up.":                    
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                    "You put the ballgag on her mouth."  
                    $ E_Gag = Gagtype                           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 15)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    if not ApprovalCheck("Emma", 700, "O", TabM=1):                        
                        call EmmaFace("angry") from _call_EmmaFace_1383
                        "Emma shoves you away, take the ballgag off and throw it on your face."
                        $ E_Gag = 0
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_9
                        ch_e "You shut up!"
                        ch_e "If that's how you want to treat me, we're done here!"                                                  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                        
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")  
                        #$ E_Gagx -= 1                      
                    else:
                        $ E_Gag = Gagtype
                        call EmmaFace("sad") from _call_EmmaFace_1384
                        "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
        return             
    
   
    if not E_Gagx:                                                               #first time    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1385
        $ E_Mouth = "kiss"
        ch_e "Wait, you want to put a gag in my mouth?!"
  
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1386
            ch_e "Seriously?"
        
    
    if not E_Gagx and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1387
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_1388
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I guess if you really want to try it. . ."           
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_1389
            ch_e "Ok, [E_Petname]."
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_1390
            ch_e "Well. . . I bet it would feel really good."
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_1391
            $ E_Mouth = "smile"             
            ch_e "Hmm, it has been on my list. . ."  
        jump E_GagPrep
    
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1392
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's really what you want?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."   
        elif E_Gagx < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_1393
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you wanna try that again?"       
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_1394
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some bondage?",                 
                "So you wanna try that again?",                 
                "I like that."]) 
            ch_e "[Line]"
        $ Line = 0
        jump E_GagPrep
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1395
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine."   
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1396
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, shut me up.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . .",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_GagPrep 
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_1397
        if Taboo:
            ch_e "I already told you that I wouldn't do that out here!"  
        elif not E_Gagx:
            call EmmaFace("bemused") from _call_EmmaFace_1398
            ch_e "I'm just not into that, [E_Petname]. . ."
        elif E_Gagx:
            call EmmaFace("perplexed") from _call_EmmaFace_1399
            ch_e "You could have been a bit more gentle last time, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1400
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Maybe later?":
                call EmmaFace("sexy") from _call_EmmaFace_1401  
                ch_e "I'll give it some thought, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)  
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_1402     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    #jump E_Doggy_AnalPrep
                else:   
                    pass
                    
            "Shut it.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1403
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                    ch_e "Ok, fine. If we're going to do this, stick it in already."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1  
                    jump E_GagPrep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    call EmmaFace("angry") from _call_EmmaFace_1404
                    "Emma shoves you away."
                    $ renpy.pop_call()
                    if Situation:
                        $ renpy.pop_call()
                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_10
                    ch_e "You shut it"
                    ch_e "If that's how you want to treat me, we're done here!"                                                  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                    

    
    #She refused all offers.
    $ Emma_Arms = 1  
    if E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1405
        ch_e "That's a bit much, even for you."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)       
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_1406
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "That you would even suggest such a thing in a place like this. . ."    
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3) 
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_1407
        ch_e "Not happening."    
    $ Tempmod = 0    
    return

# End Gag Emma //////////////////////////////////////////////////////////////////////////////////

# E_Gag_Prep ////////////////////////////////////////////////////////////////////////////////

label E_GagPrep:    
            
    #call Emma_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        
        if Taboo: # Emma gets started. . .
            if E_Gagx:                
                "Emma glances around to see if anyone notices what she's doing, then you put the ballgag on her."
                
            else:         
                "Emma glances around for voyeurs. . ."
                $ E_Mouth = "sucking"
                "Emma hesitantly opens her mouth."
                "You put the ballgag in her mouth."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Gagx:
                $ E_Mouth = "sucking"
                "Emma opens her mouth wide."

                "You carefuly put the gag on her."
            else:
                $ E_Mouth = "sucking"

                "Emma opens her mouth wide."
                "You put the gag on her."
                     
    else: #if Situation == "auto"       

        "You quickly put the ballgag on her mouth."
    $ E_Gag = Gagtype
    
    if not E_Gagx:                                                      #First time stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -150)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 70)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 40) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 70) 
    elif E_Gagx < 6:                                                   #first few times stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
        else:
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 7)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
                
    if Situation:    
        #$ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    #$ Cnt = 0
    #$ P_Cock = "anal"
    #$ Trigger = "anal"
    #$ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_158
    #call DrainWord("Emma","no anal")
    #$ E_RecentActions.append("anal")                      
    #$ E_DailyActions.append("anal") 
    return
# End Gag Prep

# E_Doggy_A anal //////////////////////////////////////////////////////////////////////

label E_Doggy_A:
    call Shift_Focus("Emma") from _call_Shift_Focus_196
    if E_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif E_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif E_Anal: #You've done it before
        $ Tempmod += 15 
        
    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif E_Addict >= 75: 
        $ Tempmod += 15
    
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if E_Loose:
        $ Tempmod += 10  
    elif "anal" in E_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in E_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10      
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
        
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in E_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in E_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Emma", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_7   
            if (E_Legs == "skirt" or E_Legs == "cheerleader skirt"):
                "Emma turns and backs up against your cock, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "pants":
                "Emma turns and backs up against your cock, sliding her pants off as she does so."                
                $ E_Legs = 0
            else:
                "Emma turns and backs up against your cock."
            $ E_SeenPanties = 1
            if E_Plugged:
                "You remove the plug from her asshole"
                $ E_Plugged = 0
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                    "Emma slides it in."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_1408                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    ch_p "Ooo, dirty girl, [E_Pet], let's do this."
                    call Emma_Namecheck from _call_Emma_Namecheck_23
                    "Emma slides it in."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised") from _call_EmmaFace_1409       
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_24
                    "Emma pulls back."
                    call EmmaOutfit from _call_EmmaOutfit_62
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                    return            
            jump E_Doggy_AnalPrep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_8   
        if (E_Legs == "skirt" or E_Legs == "cheerleader skirt"):
            "You press up against Emma's backside, sliding her skirt up as you go."
            $ E_Upskirt = 1
        elif E_Legs == "pants":
            "You press up against Emma's backside, sliding her pants down as you do."                
            $ E_Legs = 0
        else:
            "You press up against Emma's backside."
        $ E_SeenPanties = 1
        if E_Plugged:
            "You remove the plug from her asshole"
            $ E_Plugged = 0
        "You press the tip of your cock against her tight rim."        
        call EmmaFace("surprised", 1) from _call_EmmaFace_1410
        
        if (E_Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy") from _call_EmmaFace_1411
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
            if E_Plugged:
                "She removes the plug from her asshole"
                $ E_Plugged = 0
            ch_e "Hmm, stick it in. . ."            
            jump E_Doggy_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1) from _call_EmmaFace_1412
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_e "I guess if you really want to try it. . ."
                        if E_Plugged:
                            ch_e "Let me just remove this first. . ."
                            "She removes the plug from her asshole"
                            $ E_Plugged = 0
                        jump E_Doggy_AnalPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1) from _call_EmmaFace_1413
                    if E_Anal:
                        ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_e "Well ok, [E_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                    if E_Plugged:
                        "You remove the plug from her asshole and press your dick into her"
                        $ E_Plugged = 0
                    else:
                        "You press into her."                              
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    if not ApprovalCheck("Emma", 700, "O", TabM=1):                        
                        call EmmaFace("angry") from _call_EmmaFace_1414
                        "Emma shoves you away and slaps you in the face."
                        ch_e "Jackass!"
                        ch_e "If that's how you want to treat me, we're done here!"                                                  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_11
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                        
                    else:
                        call EmmaFace("sad") from _call_EmmaFace_1415
                        "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump E_Doggy_AnalPrep
        return             
    
   
    if not E_Anal and "no anal" not in E_RecentActions:                                                               #first time    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1416
        $ E_Mouth = "kiss"
        ch_e "Wait, so you want to stick it in my butt?!"
  
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1417
            ch_e "Seriously?"
        
    if not E_Loose and ("dildo anal" in E_DailyActions or "anal" in E_DailyActions):
        call EmmaFace("bemused", 1) from _call_EmmaFace_1418
        ch_e "I'm still a little sore from earlier."
            
    elif "anal" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1419
        ch_e "You want to go again? Ok."
        if E_Plugged:
            "She removes the plug from her asshole"
            $ E_Plugged = 0
        jump E_Doggy_AnalPrep
        
    
    if not E_Anal and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1420
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_1421
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I guess if you really want to try it. . ."           
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_1422
            ch_e "Ok, [E_Petname], I'm ready."
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_1423
            ch_e "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_1424
            $ E_Mouth = "smile"             
            ch_e "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1425
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's really what you want?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."   
        elif "anal" in E_DailyActions and not E_Loose:
            pass      
        elif "anal" in E_RecentActions:
            ch_e "I think I'm warmed up. . ."
            if E_Plugged:
                "She removes the plug from her asshole"
                $ E_Plugged = 0
            jump E_Doggy_AnalPrep
        elif "anal" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1426
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_e "[Line]"
        elif E_Anal < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_1427
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_1428
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1429
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine."   
        elif "no anal" in E_DailyActions:               
            ch_e "Ok, ok, I have been itching for this. . ." 
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1430
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        if E_Plugged:
            "She removes the plug from her asshole"
            $ E_Plugged = 0
        jump E_Doggy_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_1431
        if "no anal" in E_RecentActions:  
            ch_e "What part of \"no,\" did you not get, [E_Petname]?"
        elif Taboo and "tabno" in E_DailyActions and "no anal" in E_DailyActions:
            ch_e "I already told you that I wouldn't do that out here!"  
        elif "no anal" in E_DailyActions:       
            ch_e "I already told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I already told you that I wouldn't do that out here!"  
        elif not E_Anal:
            call EmmaFace("bemused") from _call_EmmaFace_1432
            ch_e "I'm just not into that, [E_Petname]. . ."
        elif not E_Loose and "anal" not in E_DailyActions:
            call EmmaFace("perplexed") from _call_EmmaFace_1433
            ch_e "You could have been a bit more gentle last time, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1434
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1435
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no anal" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1436  
                ch_e "I'll give it some thought, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)  
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no anal")                      
                $ E_DailyActions.append("no anal") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_1437     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0        
                    if E_Plugged:
                        "She removes the plug from her asshole"  
                        $ E_Plugged = 0         
                    jump E_Doggy_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1438
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                    ch_e "Ok, fine. If we're going to do this, stick it in already."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1  
                    jump E_Doggy_AnalPrep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no anal" in E_DailyActions:
        ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1439
        ch_e "That's a bit much, even for you."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)       
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_1440
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "That you would even suggest such a thing in a place like this. . ."    
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3) 
    elif not E_Loose and "anal" in E_DailyActions:
        call EmmaFace("bemused") from _call_EmmaFace_1441
        ch_e "Sorry, I just need a little break back there, [E_Petname]."    
    elif E_Anal:
        call EmmaFace("sad") from _call_EmmaFace_1442 
        ch_e "The only thing you can do with my ass is kiss it, [E_Petname]."
        ch_e ". . .Don't get any ideas."   
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_1443
        ch_e "Not happening."    
    $ E_RecentActions.append("no anal")                      
    $ E_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label E_Plug_Ass:
    call Shift_Focus("Emma") from _call_Shift_Focus_197
      
    if E_Loose:
        $ Tempmod += 30   
    elif "anal" in E_RecentActions or "plug anal" in E_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in E_DailyActions or "plug anal" in E_DailyActions:
        $ Tempmod -= 10
    elif (E_Anal + E_DildoA + E_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if E_Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if E_Lust > 95:
        $ Tempmod += 20
    elif E_Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:        
        $ Tempmod += (5*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount   
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no plug" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no plug" in E_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Emma", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Emma":                                                                  
            #Emma auto-starts   
            call Emma_Doggy_Launch("plug") from _call_Emma_Doggy_Launch_9 
        
            if Approval > 2:                                                      # fix, add Emma auto stuff here
                if E_Legs == "skirt":
                    "Emma grabs her plug, hiking up her skirt as she does."
                    $ E_Upskirt = 1
                elif E_Legs == "pants":
                    "Emma grabs her plug, pulling down her pants as she does."              
                    $ E_Legs = 0
                else:
                    "Emma grabs her plug, rubbing it suggestively against her ass."
                $ E_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                        "Emma slides it in."
                    "Go for it.":       
                        call EmmaFace("sexy, 1") from _call_EmmaFace_1444                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        ch_p "Oh yeah, [E_Pet], let's do this."
                        call Emma_Namecheck from _call_Emma_Namecheck_25
                        "You grab the plug and slide it in."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised") from _call_EmmaFace_1445       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck from _call_Emma_Namecheck_26
                        "Emma sets the plug down."
                        call EmmaOutfit from _call_EmmaOutfit_63
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                        return            
                jump EPA_Prep
            else:                
                $ Tempmod = 0                               # fix, add Emma auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            call Emma_Doggy_Launch("massage") from _call_Emma_Doggy_Launch_10  

            "You rub the plug across her body, and against her tight anus."
            call EmmaFace("surprised", 1) from _call_EmmaFace_1446
            
            if (E_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call EmmaFace("sexy") from _call_EmmaFace_1447
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                ch_e "Ok, [E_Petname], let's do this."            
                jump EPA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Hey, what do you think you're doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1) from _call_EmmaFace_1448
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                            jump EPA_Prep
                        "You pull back before you really get it in."                    
                        call EmmaFace("bemused", 1) from _call_EmmaFace_1449
                        if E_DildoA:
                            ch_e "Well ok, [E_Petname], no harm done. Just give me a little warning next time." 
                        else:
                            ch_e "Well ok, [E_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                    "Just playing with my favorite toys.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                        "You press it inside some more."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call EmmaFace("angry") from _call_EmmaFace_1450
                            "Emma shoves you away and slaps you in the face."
                            ch_e "Jackass!"
                            ch_e "If that's how you want to treat me, we're done here!"                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            if E_Plugged:
                                "She removes the plug from her asshole"
                                $ E_Plugged = 0
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Emma_Doggy"):
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_12  
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                         
                        else:
                            call EmmaFace("sad") from _call_EmmaFace_1451
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump EPA_Prep
            return             
    #end auto
   
    if not E_DildoA:                                                               
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_1452
            $ E_Mouth = "kiss"
            ch_e "Hmmm, so you'd like to try out some toys?"    
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_1453
                ch_e "You had to go for the butt, uh?"
    
    if not E_Loose and ("dildo anal" in E_RecentActions or "plug anal" in E_RecentActions or "anal" in E_RecentActions or "dildo anal" in E_DailyActions or "plug anal" in E_DailyActions or "anal" in E_DailyActions):
            call EmmaFace("bemused", 1) from _call_EmmaFace_1454
            ch_e "I'm still a bit sore from earlier. . ."
            
    if not E_DildoA and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_1455
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_1456
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I haven't actually used one of these, back there before. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_1457
                ch_e "If that's what you want, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_1458
                $ E_Mouth = "smile"             
                ch_e "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_1459
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "The toys again?"  
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "Well, at least you got us some privacy this time. . ."   
            elif "plug anal" in E_DailyActions and not E_Loose:
                pass
            elif "plug anal" in E_DailyActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_1460
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_e "[Line]"
            elif E_DildoA < 3:        
                call EmmaFace("sexy", 1) from _call_EmmaFace_1461
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "You want to stick it in my ass again?"       
            else:       
                call EmmaFace("sexy", 1) from _call_EmmaFace_1462
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"]) 
                ch_e "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_1463
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."    
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_1464
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump EPA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry") from _call_EmmaFace_1465
            if "no plug" in E_RecentActions:  
                ch_e "What part of \"no,\" did you not get, [E_Petname]?"
            elif Taboo and "tabno" in E_DailyActions and "no plug" in E_DailyActions:
                ch_e "Stop swinging that thing around in public!"  
            elif "no plug" in E_DailyActions:       
                ch_e "I already told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you that I wouldn't do that out here!"  
            elif not E_DildoA:
                call EmmaFace("bemused") from _call_EmmaFace_1466
                ch_e "I'm just not into toys, [E_Petname]. . ."
            elif not E_Loose and "plug anal" not in E_DailyActions:
                call EmmaFace("perplexed") from _call_EmmaFace_1467
                ch_e "You could have been a bit more gentle last time, [E_Petname]. . ."
            else:
                call EmmaFace("bemused") from _call_EmmaFace_1468
                ch_e "I don't think we need any toys, [E_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no plug" in E_DailyActions:
                    call EmmaFace("bemused") from _call_EmmaFace_1469
                    ch_e "Yeah, ok, [E_Petname]."              
                    return
                "Maybe later?" if "no plug" not in E_DailyActions:
                    call EmmaFace("sexy") from _call_EmmaFace_1470  
                    ch_e "Maybe I'll practice on my own time, [E_Petname]."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)  
                    if Taboo:                    
                        $ E_RecentActions.append("tabno")                      
                        $ E_DailyActions.append("tabno") 
                    $ E_RecentActions.append("no plug")                      
                    $ E_DailyActions.append("no plug") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call EmmaFace("sexy") from _call_EmmaFace_1471     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump EPA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad") from _call_EmmaFace_1472
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                        ch_e "Ok, fine. If we're going to do this, stick it in already."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        $ E_Forced = 1  
                        jump EPA_Prep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1   
    if "no plug" in E_DailyActions:
            ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif E_Forced:
            call EmmaFace("angry", 1) from _call_EmmaFace_1473
            ch_e "I'm not going to let you use that on me."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call EmmaFace("angry", 1) from _call_EmmaFace_1474          
            $ E_RecentActions.append("tabno")                       
            $ E_DailyActions.append("tabno") 
            ch_e "Not here!"     
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif not E_Loose and "plug anal" in E_DailyActions:
            call EmmaFace("bemused") from _call_EmmaFace_1475
            ch_e "Sorry, I just need a little break back there, [E_Petname]."    
    elif E_DildoA:
            call EmmaFace("sad") from _call_EmmaFace_1476 
            ch_e "Sorry, you can keep your toys out of there."     
    else:
            call EmmaFace("normal", 1) from _call_EmmaFace_1477
            ch_e "No way." 
    $ E_RecentActions.append("no plug")                      
    $ E_DailyActions.append("no plug")   
    $ Tempmod = 0    
    return

label EPA_Prep:  
            
    call Emma_Doggy_Launch("massage") from _call_Emma_Doggy_Launch_11
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_15        
        if E_Panties or E_Legs or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_e "Well, I guess some things are necessary, [E_Petname]."
            
        if E_Legs == "pants" and E_Panties:
            "She quickly pulls down her pants and drops her [E_Panties]."
        elif E_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Emma") >= 5 and E_Panties:
            "She quickly pulls down her [E_Hose] and drops her [E_Panties]."
            $ E_Hose = 0
        elif HoseNum("Emma") >= 5:
            "She quickly pulls down her [E_Hose], exposing her bare ass."
            $ E_Hose = 0
        elif E_Panties:
            "She quickly pulls down her [E_Panties]."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless from _call_Emma_First_Bottomless_24
        
        if Taboo: # Emma gets started. . .
            if E_Anal:                
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against the plug."
                #"You guide your cock into place and ram it home."   
                
            else:         
                "Emma glances around for voyeurs. . ."
                "Emma slowly backs up against the plug."
                #"You guide it into place and slide it in."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Anal:
                "Emma bends over and presses her backside against the plug suggestively."
                #"You take careful aim and then push your cock in."
            else:
                "Emma slowly backs up against the plug."
                #"You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if E_Legs == "pants" and E_Panties:
            "You quickly pull down her pants and her [E_Panties] and press the plug against her ass."
        if E_Panties and E_Legs != "pants":
            "You quickly pull down her [E_Panties] and press the plug against her ass."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_25
        
    #call Seen_First_Peen(1)
    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_13
    call Emma_Doggy_Launch("plug") from _call_Emma_Doggy_Launch_12
    
    if not E_Anal:                                                      #First time stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -150)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 70)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 40) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 70) 
    elif not E_Loose:                                                   #first few times stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
        else:
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 7)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "plug"
    $ Trigger = "plug"
    $ Speed = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_159
    call DrainWord("Emma","no anal") from _call_DrainWord_160
    $ E_RecentActions.append("plug anal")                      
    $ E_DailyActions.append("plug anal")


label E_Anal_Plug_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_198
        call Emma_Doggy_Launch("plug") from _call_Emma_Doggy_Launch_13 
        call EmmaLust from _call_EmmaLust_22        
        $ P_Cock = "plug"
        $ Trigger = "plug"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    ch_e "Can you finish there? I'm getting a little sore."   
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . .worn out. . . here, . . [E_Petname]."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "Let's try something else." if MultiAction: 
                                if Speed != 0:
                                    "But keep the plug inside you."
                                    $ E_Plugged = 1
                                    $ Speed = 0
                                $ Line = 0
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_14
                                $ Situation = "shift"
                                jump E_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1478   
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_15
                                    "She scowls at you and pulls out."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    if E_Plugged:
                                        "She removes the plug from her asshole"
                                        $ E_Plugged = 0
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_AnalAfter
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
                            if not E_Gag:
                                #"You put a gag on Emma"
                            #            $ E_Gag = "ballgag"
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call E_Gagging("ballgag") from _call_E_Gagging_2
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call E_Gagging("ballgag") from _call_E_Gagging_3
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call E_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call E_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Emma's gag"
                                $ E_Gag = 0
                           
                        #"Leave it in" if Speed:                    
                        #            $ Speed = 2
                        #            $ E_Plugged = 1
                        #            "You leave the plug inside her ass."

                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call E_Slap_Ass from _call_E_Slap_Ass_16 
                                    hide Slap_Ass2                                    
                                    jump E_Anal_Plug_Cycle  
                                    
                           
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_23             
                        
                        "Shift actions":
                            if E_Action and MultiAction:
                                if Speed != 0:
                                    "You leave the plug inside her asshole"
                                    $ E_Plugged = 1
                                    $ Speed = 0
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter
                                            call E_Doggy_P from _call_E_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_1
                                            call E_Doggy_P from _call_E_Doggy_P_1
                                    "Start hotdogging her.":
                                            $ Situation = "pullback"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_2
                                            call E_Doggy_H from _call_E_Doggy_H_1
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter
                                            call E_Doggy_A from _call_E_Doggy_A_2
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_1
                                            call E_Doggy_A from _call_E_Doggy_A_3
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_25
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    menu:
                                        "And keep the plug inside":
                                            $ E_Plugged = 1
        
                                        "And you can remove the plug":
                                            $ E_Plugged = 0
        
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_16
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction:
                                    menu:
                                        "But keep the plug inside":
                                            $ E_Plugged = 1
        
                                        "And you can remove the plug":
                                            $ E_Plugged = 0
         
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_17
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_48
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_19
                            if "angry" in E_RecentActions:  
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_18
                                if E_Plugged:
                                    "She removes the plug from her asshole"
                                    $ E_Plugged = 0
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if renpy.showing("Emma_Doggy"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_30
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Doggy_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Doggy_Launch(Trigger) from _call_Emma_Doggy_Launch_14
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Anal_Plug_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump E_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump E_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_1479
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."

    return


label E_Doggy_AnalPrep:  
            
    call Emma_Doggy_Launch("hotdog") from _call_Emma_Doggy_Launch_15
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_16        
        if E_Panties or E_Legs or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_e "Well, I guess some things are necessary, [E_Petname]."
            
        if E_Legs == "pants" and E_Panties:
            "She quickly pulls down her pants and drops her [E_Panties]."
        elif E_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Emma") >= 5 and E_Panties:
            "She quickly pulls down her [E_Hose] and drops her [E_Panties]."
            $ E_Hose = 0
        elif HoseNum("Emma") >= 5:
            "She quickly pulls down her [E_Hose], exposing her bare ass."
            $ E_Hose = 0
        elif E_Panties:
            "She quickly pulls down her [E_Panties]."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless from _call_Emma_First_Bottomless_26
        
        if E_Plugged:
            "She removes the plug from her asshole."
            $ E_Plugged = 0


        if Taboo: # Emma gets started. . .
            if E_Anal:                
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Anal:
                "Emma bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if E_Legs == "pants" and E_Panties:
            "You quickly pull down her pants and her [E_Panties] and press against her ass."
        if E_Panties and E_Legs != "pants":
            "You quickly pull down her [E_Panties] and press against her ass."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_27
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_19
    
    if not E_Anal:                                                      #First time stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -150)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 70)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 40) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 70) 
    elif not E_Loose:                                                   #first few times stat buffs       
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
        else:
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 7)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_161
    call DrainWord("Emma","no anal") from _call_DrainWord_162
    $ E_RecentActions.append("anal")                      
    $ E_DailyActions.append("anal") 

label E_Doggy_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_199
        call Emma_Doggy_Launch("anal") from _call_Emma_Doggy_Launch_16 
        call EmmaLust from _call_EmmaLust_23        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . .worn out. . . here, . . [E_Petname]."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                if E_Anal >= 5 and E_Blow >= 10 and E_SEXP >= 50:
                                    $ Situation = "shift"
                                    call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_3
                                    call E_Blowjob from _call_E_Blowjob_9      
                                else:
                                    ch_e "No thanks, [E_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_4
                                    call EHJ_Prep from _call_EHJ_Prep_1   
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_5
                                call E_Handjob from _call_E_Handjob_6     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Doggy_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_19
                                $ Situation = "shift"
                                jump E_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1480   
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_20
                                    "She scowls at you and pulls out."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_AnalAfter
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
                            if not E_Gag:
                                #"You put a gag on Emma"
                            #            $ E_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call E_Gagging("ballgag") from _call_E_Gagging_4
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call E_Gagging("ballgag") from _call_E_Gagging_5
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call E_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call E_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Emma's gag"
                                $ E_Gag = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call E_Slap_Ass from _call_E_Slap_Ass_17 
                                    hide Slap_Ass2                                   
                                    jump E_Doggy_Anal_Cycle  

                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                           
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_24             
                        
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_6
                                            call E_Doggy_P from _call_E_Doggy_P_2
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_7
                                            call E_Doggy_P from _call_E_Doggy_P_3
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_8
                                            call E_Doggy_H from _call_E_Doggy_H_2
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_9
                                            call E_Plug_Ass from _call_E_Plug_Ass_2
                                    "Just stick the plug in her ass [[without asking]." if not E_Plugged:
                                            $ Situation = "auto"
                                            call E_Doggy_AnalAfter from _call_E_Doggy_AnalAfter_10
                                            call E_Plug_Ass from _call_E_Plug_Ass_3
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_26
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_21
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_22
                                    $ Line = 0
                                    jump E_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_49
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_20
                            if "angry" in E_RecentActions:  
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_23
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if renpy.showing("Emma_Doggy"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_31
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Doggy_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Doggy_Launch(Trigger) from _call_Emma_Doggy_Launch_17
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Doggy_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump E_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump E_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_1481
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Doggy_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_24
        
    call EmmaFace("sexy") from _call_EmmaFace_1482 
    
    $ E_Anal += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 3) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if E_Loc == bg_current and "noticed Emma" in E_RecentActions: #If Emma was participating
        $ E_LikeEmma += 2 if E_LikeEmma >= 800 else 1
    
    if "Emma Anal Addict" in Achievements:
            pass 
            
    elif E_Anal >= 10:
        $ E_SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not Situation:
            call EmmaFace("bemused", 1) from _call_EmmaFace_1483
            ch_e "I. . . really think I enjoy this. . ."                  
    elif E_Anal == 1:            
            $E_SEXP += 25        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was . . . interesting [E_Petname]. We'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Ouch."
                    ch_e "Did you get what you needed here?"
    elif E_Anal == 5:
            ch_e "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_1484
            $ E_Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1485
            ch_e "That felt . . . good. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_77
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# E_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label E_Doggy_H: 
    call Shift_Focus("Emma") from _call_Shift_Focus_200
    if E_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif E_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in E_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount 
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in E_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Emma", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_18 
            "Emma turns and backs up against your cock, rubbing it against her ass."
            menu:
                "What do you do?"
                "Nothing.":                     
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                    "Emma starts to grind against you."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_1486                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
                    ch_p "Hmmm, that's good, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_27
                    "Emma starts to grind against you."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised") from _call_EmmaFace_1487       
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_28
                    "Emma pulls back."
                    call EmmaOutfit from _call_EmmaOutfit_64
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                    return            
            jump E_Doggy_HotdogPrep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Emma_Doggy_Launch("L") from _call_Emma_Doggy_Launch_19   
        "You press up against Emma's backside."    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1488
        
        if (E_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call EmmaFace("sexy") from _call_EmmaFace_1489
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
            ch_e "Hmm, I've apparently got someone's attention. . ."            
            jump E_Doggy_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ E_Brows = "angry"                
            menu:
                ch_e "Hmm, kinda rude, [E_Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call EmmaFace("sexy", 1) from _call_EmmaFace_1490
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_e "I guess it doesn't feel so bad. . ."
                        jump E_Doggy_HotdogPrep
                    "You pull back before you really get it in."                    
                    call EmmaFace("bemused", 1) from _call_EmmaFace_1491
                    if E_Hotdog:
                        ch_e "Well ok, [E_Petname], it has been kinda fun." 
                    else:
                        ch_e "Well ok, [E_Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                    "You grind against her asscrack."                              
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    if not ApprovalCheck("Emma", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call EmmaFace("angry") from _call_EmmaFace_1492
                        "Emma shoves you away."
                        ch_e "Dick!"
                        ch_e "If that's how you want want to act, I'm out of here!"                                                  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_25
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")                       
                    else:
                        call EmmaFace("sad") from _call_EmmaFace_1493
                        "Emma doesn't seem to be into this, but she's knows her place."                        
                        jump E_Doggy_HotdogPrep
        return             
    
   
    if not E_Hotdog and "no hotdog" not in E_RecentActions:                                                               #first time    
        call EmmaFace("surprised", 1) from _call_EmmaFace_1494
        $ E_Mouth = "kiss"
        ch_e "Wait, so you want to grind against my butt?!"
  
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1495
            ch_e ". . . That's all?"
        
        
    if not E_Hotdog and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1496
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_1497
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "It looks like you need some relief. . ."           
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_1498
            ch_e "If that's what you need, [E_Petname]."
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_1499
            ch_e "Hmmm. . ."
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_1500
            $ E_Mouth = "smile"             
            ch_e "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1501
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's all you want?"  
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1502
            ch_e "You want to go again? Ok."
            jump E_Doggy_HotdogPrep
        elif "hotdog" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1503
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_e "[Line]"
        elif E_Hotdog < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_1504
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another go?"       
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_1505
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1506
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine."    
        elif "no hotdog" in E_DailyActions:               
            ch_e "Well, I guess it's not so bad. . ."
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1507
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_Doggy_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_1508
        if "no hotdog" in E_RecentActions:  
            ch_e "I {i}just{/i} told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no hotdog" in E_DailyActions: 
            ch_e "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in E_DailyActions:       
            ch_e "I told you \"no\" earlier, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you that I didn't want you rubb'in up on me in public!"     
        elif not E_Hotdog:
            call EmmaFace("bemused") from _call_EmmaFace_1509
            ch_e "That's kinda naughty, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1510
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1511
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no hotdog" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1512  
                ch_e "Yeah, maybe, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no hotdog")                      
                $ E_DailyActions.append("no hotdog")                          
                return
            "You might like it. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_1513     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump E_Doggy_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1514
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, fine. Whatever."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                    $ E_Forced = 1  
                    jump E_Doggy_HotdogPrep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1      
    
    if "no hotdog" in E_DailyActions:
        ch_e "I just don't want to, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    if E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1515
        ch_e "Even that's not worth it."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1)  
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_1516        
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "I'd be a bit embarassed doing that here."  
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif E_Hotdog:
        call EmmaFace("sad") from _call_EmmaFace_1517 
        ch_e "Eh-eh, not anymore, [E_Petname]."
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_1518
        ch_e "Not interested."    
    $ E_RecentActions.append("no hotdog")                      
    $ E_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label E_Doggy_HotdogPrep:  
    call Emma_Doggy_Launch("hotdog") from _call_Emma_Doggy_Launch_20
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_17    
        
        if Taboo: # Emma gets started. . .
            if E_Hotdog:                
                "Emma glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                
            else:         
                "Emma glances around for voyeurs. . ."
                "Emma hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Hotdog:
                "Emma bends over and presses her backside against you suggestively."
            else:
                "Emma hesitantly pulls down your pants slowly backs up against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her ass."
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_20

    if not E_Hotdog:                                                      #First time stat buffs      
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_163
    call DrainWord("Emma","no hotdog") from _call_DrainWord_164
    $ E_RecentActions.append("hotdog")                      
    $ E_DailyActions.append("hotdog") 

label E_Doggy_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_201
        call Emma_Doggy_Launch("hotdog") from _call_Emma_Doggy_Launch_21 
        call EmmaLust from _call_EmmaLust_24        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + E_Hotdog):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here?"   
        elif Cnt == (10 + E_Hotdog):
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "I'm kinda done with this, [E_Petname]."
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_2
                                call E_Blowjob from _call_E_Blowjob_10       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Doggy_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_26
                                $ Situation = "shift"
                                jump E_Doggy_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1519   
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_27
                                    "She scowls at you and pulls away."
                                    ch_e "Well if that's your attitude you can handle your own business."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Doggy_HotdogAfter
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
                            if not E_Gag:
                                #"You put a gag on Emma"
                            #            $ E_Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call E_Gagging("ballgag") from _call_E_Gagging_6
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call E_Gagging("ballgag") from _call_E_Gagging_7
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call E_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call E_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Emma's gag"
                                $ E_Gag = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call E_Slap_Ass from _call_E_Slap_Ass_18 
                                    hide Slap_Ass2                                   
                                    jump E_Doggy_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                          
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_25    
                                    
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_3
                                        call E_Doggy_P from _call_E_Doggy_P_4
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_4
                                        call E_Doggy_P from _call_E_Doggy_P_5
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_5
                                        call E_Doggy_A from _call_E_Doggy_A_4
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_6
                                        call E_Doggy_A from _call_E_Doggy_A_5
                                    "How about the plug?":
                                        $ Situation = "shift"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_7
                                        call E_Plug_Ass from _call_E_Plug_Ass_4
                                    "Just stick the plug in her ass [[without asking]." if not E_Plugged:
                                        $ Situation = "auto"
                                        call E_Doggy_HotdogAfter from _call_E_Doggy_HotdogAfter_8
                                        call E_Plug_Ass from _call_E_Plug_Ass_5
                                    "Never Mind":
                                        pass
                            else:
                                ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_27
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_28
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Doggy_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_29
                                    $ Line = 0
                                    jump E_Doggy_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_50
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_21
                            if "angry" in E_RecentActions:  
                                call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_30
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Doggy_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Emma can cum
                    if renpy.showing("Emma_Doggy"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_32
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Doggy_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Doggy_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Doggy_Launch("hotdog") from _call_Emma_Doggy_Launch_22
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Doggy_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump E_Doggy_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump E_Doggy_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_1520
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Doggy_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_31
        
    call EmmaFace("sexy") from _call_EmmaFace_1521 
    
    $ E_Hotdog += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if E_Loc == bg_current and "noticed Emma" in E_RecentActions: #If Emma was participating
        $ E_LikeEmma += 1
    
    if "Emma Full Buns" in Achievements:
            pass 
            
    elif E_Hotdog >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Full Buns")
        if not Situation:
            call EmmaFace("smile", 1) from _call_EmmaFace_1522
            ch_e "I think I'm getting addicted to this."               
    elif E_Hotdog == 1:            
            $E_SEXP += 10        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was pretty hot, [E_Petname], we'll have to do that again sometime."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Did you get what you needed here?"
    elif E_Hotdog == 5:
            ch_e "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_1523
            $ E_Eyes = "side"
            ch_e "That didn't really do it for me. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1524
            ch_e "That was an interesting diversion. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_78
    return   

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////

    
    