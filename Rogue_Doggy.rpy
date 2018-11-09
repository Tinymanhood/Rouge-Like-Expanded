# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# R_Doggy_P //////////////////////////////////////////////////////////////////////

label R_Doggy_P:  
    call Shift_Focus("Rogue")
    if R_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif R_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif R_Sex: #You've done it before
        $ Tempmod += 10    
        
    if R_Addict >= 75 and (R_CreamP + R_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif R_Addict >= 75:
        $ Tempmod += 15
        
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in R_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    
        
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in R_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Rogue", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Rogue_Doggy_Launch("L")   
            if R_Legs == "skirt":
                "Rogue turns and backs up against your cock, sliding her skirt up as she does so."
                $ R_Upskirt = 1
            elif R_Legs == "pants":
                "Rogue turns and backs up against your cock, sliding her pants off as she does so."                
                $ R_Legs = 0
            else:
                "Rogue turns and backs up against your cock."
            $ R_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                    "Rogue slides it in."
                "Praise her.":       
                    call RogueFace("sexy, 1")                    
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                    ch_p "Oh yeah, [R_Pet], let's do this."
                    call Rogue_Namecheck
                    "Rogue slides it in."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                "Ask her to stop.":
                    call RogueFace("surprised")       
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call RogueOutfit
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
                    return            
            jump R_SexPrep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Rogue_Doggy_Launch("L")   
        if R_Legs == "skirt":
            "You press up against Rogue's backside, sliding her skirt up as you go."
            $ R_Upskirt = 1
        elif R_Legs == "pants":
            "You press up against Rogue's backside, sliding her pants down as you do."                
            $ R_Legs = 0
        else:
            "You press up against Rogue's backside."
        $ R_SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call RogueFace("surprised", 1)
        
        if (R_Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Rogue is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call RogueFace("sexy")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
            ch_r "Ok, [R_Petname], let's do this."            
            jump R_SexPrep         
        else:                                                                                                            #she's questioning it
            $ R_Brows = "angry"                
            menu:
                ch_r "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call RogueFace("sexy", 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                        ch_r "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                        jump R_SexPrep
                    "You pull back before you really get it in."                    
                    call RogueFace("bemused", 1)
                    if R_Sex:
                        ch_r "Well ok, [R_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_r "Well ok, [R_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    "You press inside some more."                              
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                    if not ApprovalCheck("Rogue", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call RogueFace("angry")
                        "Rogue shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"                                                  
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Doggy_Reset
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")                    
                    else:
                        call RogueFace("sad")
                        "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump R_SexPrep
        return             
    
   
    if not R_Sex and "no sex" not in R_RecentActions:                           #first time    
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "So, you'd like to take this to the next level? Actual sex? . . ."    
        if R_Forced:
            call RogueFace("sad")
            ch_r "You'd really take it that far?"
            
            
    if not R_Sex and Approval:                                                  #First time dialog        
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -30, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -20, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "Well, I've never been able to do this before now, so this might be fun."            
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "If that's what you want, [R_Petname]. . ."            
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "Hmm, I've always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call RogueFace("sexy", 1)
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            ch_r "That's really what you want?" 
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Well, at least you got us some privacy this time. . ."        
        elif "sex" in R_RecentActions:
            ch_r "You want to go again? Ok."
            jump R_SexPrep
        elif "sex" in R_DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_r "[Line]"
        elif R_Sex < 3:        
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Ok, fine."  
        elif "no sex" in R_DailyActions:               
            ch_r "Ok, you've won me over on this one. . ."
        else:
            call RogueFace("sexy", 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_r "[Line]"
            $ Line = 0
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump R_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call RogueFace("angry")       
        if "no sex" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no sex" in R_DailyActions:  
            ch_r "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I already told you this is too public!"     
        elif not R_Sex:
            call RogueFace("bemused")
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no sex" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll give it some thought, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no sex")                      
                $ R_DailyActions.append("no sex")            
                return
            "I think you'd enjoy it as much as I would. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump R_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Rogue", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                 
                    ch_r "Ok, fine. If we're going to do this, stick it in already."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    $ R_Forced = 1  
                    jump R_SexPrep
                else:                          
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20)   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1  
    if "no sex" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]." 
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "I'm not doing that just because you have me over a barrel."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)    
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)     
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r "Even if I wanted to, it certainly wouldn't be here!"      
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
    elif R_Sex:
        call RogueFace("sad") 
        ch_r "Maybe you could go fuck yourself instead."       
    else:
        call RogueFace("normal", 1)
        ch_r "No way."     
    $ R_RecentActions.append("no sex")                      
    $ R_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label R_SexPrep:
    call Rogue_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Rogue_Bottoms_Off       
        
        
        if R_Panties or R_Legs or HoseNum("Rogue") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_r "Well, I guess some things are necessary, [R_Petname]."
            
        if R_Legs == "pants" and R_Panties:
            "She quickly pulls down her pants and drops her [R_Panties]."
        elif R_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Rogue") >= 5 and R_Panties:
            "She quickly pulls down her [R_Hose] and drops her [R_Panties]."
            $ R_Hose = 0
        elif HoseNum("Rogue") >= 5:
            "She quickly pulls down her [R_Hose], exposing her bare ass."
            $ R_Hose = 0
        elif R_Panties:
            "She quickly pulls down her [R_Panties]."  
            
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless
        
        if Taboo: # Rogue gets started. . .
            if not R_Sex:
                "Rogue glances around for voyeurs. . ."
                "Rogue hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Rogue glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:    
            if not R_Sex:
                "Rogue hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Rogue bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
        if R_Legs == "pants" and R_Panties:
            "You quickly pull down her pants and her [R_Panties] and press against her slit."
        if R_Panties and R_Legs != "pants":
            "You quickly pull down her [R_Panties] and press against her slit."  
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
    if not R_Sex:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -150)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 60)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 50) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 30)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no sex")
    $ R_RecentActions.append("sex")                      
    $ R_DailyActions.append("sex") 

label R_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue")
        call Rogue_Doggy_Launch("sex") 
        call RogueLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == (5 + R_Sex):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + R_Sex):
                    $ R_Brows = "angry"        
                    ch_r "I'm . . .getting . . .worn out. . . here, . . [R_Petname]."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_SexAfter
                                call R_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Doggy_Reset
                                $ Situation = "shift"
                                jump R_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1)   
                                    call Rogue_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_r "Well if that's your attitude you can handle your own business."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_SexAfter
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
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass                                    
                                    jump R_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call R_Undress           
                        
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call R_SexAfter
                                            call R_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call R_SexAfter
                                            call R_Doggy_A
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call R_SexAfter
                                            call R_Doggy_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Line = 0
                                    jump R_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner)
        
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_Doggy_Reset
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_SexAfter 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_Doggy"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Doggy_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump R_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump R_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Doggy_Reset
        
    call RogueFace("sexy") 
    
    $ R_Sex += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
    
    if "Rogue Sex Addict" in Achievements:
            pass 
            
    elif R_Sex >= 10:
        $ R_SEXP += 5
        $ Achievements.append("Rogue Sex Addict")
        if not Situation:
            call RogueFace("smile", 1)
            ch_r "I think I'm getting addicted to this."               
    elif R_Sex == 1:            
            $R_SEXP += 20        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was really great, [R_Petname], we'll have to do that again sometime."
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "Did you get what you needed here?"
    elif R_Sex == 5:
            ch_r "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry")
            $ R_Eyes = "side"
            ch_r "I didn't exactly get off there. . ."
        else:
            call RogueFace("bemused")
            ch_r "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////


# R_Doggy_A anal //////////////////////////////////////////////////////////////////////

label R_Doggy_A:
    call Shift_Focus("Rogue")
    if R_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif R_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif R_Anal: #You've done it before
        $ Tempmod += 15 
        
    if R_Addict >= 75 and (R_CreamP + R_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif R_Addict >= 75: 
        $ Tempmod += 15
    
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if R_Loose:
        $ Tempmod += 10  
    elif "anal" in R_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in R_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in R_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10      
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
        
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in R_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in R_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Rogue", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Rogue_Doggy_Launch("L")   
            if R_Legs == "skirt":
                "Rogue turns and backs up against your cock, sliding her skirt up as she does so."
                $ R_Upskirt = 1
            elif R_Legs == "pants":
                "Rogue turns and backs up against your cock, sliding her pants off as she does so."                
                $ R_Legs = 0
            else:
                "Rogue turns and backs up against your cock."
            $ R_SeenPanties = 1
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                    "Rogue slides it in."
                "Praise her.":       
                    call RogueFace("sexy, 1")                    
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                    ch_p "Ooo, dirty girl, [R_Pet], let's do this."
                    call Rogue_Namecheck
                    "Rogue slides it in."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                "Ask her to stop.":
                    call RogueFace("surprised")       
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call RogueOutfit
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                    
                    return            
            jump R_AnalPrep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Rogue_Doggy_Launch("L")   
        if R_Legs == "skirt":
            "You press up against Rogue's backside, sliding her skirt up as you go."
            $ R_Upskirt = 1
        elif R_Legs == "pants":
            "You press up against Rogue's backside, sliding her pants down as you do."                
            $ R_Legs = 0
        else:
            "You press up against Rogue's backside."
        $ R_SeenPanties = 1
        "You press the tip of your cock against her tight rim."        
        call RogueFace("surprised", 1)
        
        if (R_Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Rogue is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call RogueFace("sexy")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
            ch_r "Hmm, stick it in. . ."            
            jump R_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ R_Brows = "angry"                
            menu:
                ch_r "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call RogueFace("sexy", 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                        ch_r "I guess if you really want to try it. . ."
                        jump R_AnalPrep
                    "You pull back before you really get it in."                    
                    call RogueFace("bemused", 1)
                    if R_Anal:
                        ch_r "Well ok, [R_Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_r "Well ok, [R_Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -8)
                    "You press into her."                              
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                    if not ApprovalCheck("Rogue", 700, "O", TabM=1):                        
                        call RogueFace("angry")
                        "Rogue shoves you away and slaps you in the face."
                        ch_r "Jackass!"
                        ch_r "If that's how you want to treat me, we're done here!"                                                  
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Doggy_Reset
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")                        
                    else:
                        call RogueFace("sad")
                        "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump R_AnalPrep
        return             
    
   
    if not R_Anal and "no anal" not in R_RecentActions:                                                               #first time    
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "Wait, so you want to stick it in my butt?!"
  
        if R_Forced:
            call RogueFace("sad")
            ch_r "Seriously?"
        
    if not R_Loose and ("dildo anal" in R_DailyActions or "anal" in R_DailyActions):
        call RogueFace("bemused", 1)
        ch_r "I'm still a little sore from earlier."
            
    elif "anal" in R_RecentActions:
        call RogueFace("sexy", 1)
        ch_r "You want to go again? Ok."
        jump R_AnalPrep
        
    
    if not R_Anal and Approval:                                                 #First time dialog        
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "I guess if you really want to try it. . ."           
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "Ok, [R_Petname], I'm ready."
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            ch_r "That's really what you want?"
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Well, at least you got us some privacy this time. . ."   
        elif "anal" in R_DailyActions and not R_Loose:
            pass      
        elif "anal" in R_RecentActions:
            ch_r "I think I'm warmed up. . ."
            jump R_AnalPrep
        elif "anal" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_r "[Line]"
        elif R_Anal < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another go?"       
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Ok, fine."   
        elif "no anal" in R_DailyActions:               
            ch_r "Ok, ok, I have been itching for this. . ." 
        else:
            call RogueFace("sexy", 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_r "[Line]"
            $ Line = 0
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump R_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no anal" in R_RecentActions:  
            ch_r "What part of \"no,\" did you not get, [R_Petname]?"
        elif Taboo and "tabno" in R_DailyActions and "no anal" in R_DailyActions:
            ch_r "I already told you that I wouldn't do that out here!"  
        elif "no anal" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I already told you that I wouldn't do that out here!"  
        elif not R_Anal:
            call RogueFace("bemused")
            ch_r "I'm just not into that, [R_Petname]. . ."
        elif not R_Loose and "anal" not in R_DailyActions:
            call RogueFace("perplexed")
            ch_r "You could have been a bit more gentle last time, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no anal" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "I'll give it some thought, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)  
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no anal")                      
                $ R_DailyActions.append("no anal") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump R_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Rogue", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                 
                    ch_r "Ok, fine. If we're going to do this, stick it in already."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    $ R_Forced = 1  
                    jump R_AnalPrep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20)    
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1  
    if "no anal" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1)
        ch_r "That's a bit much, even for you."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)       
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r "That you would even suggest such a thing in a place like this. . ."    
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3) 
    elif not R_Loose and "anal" in R_DailyActions:
        call RogueFace("bemused")
        ch_r "Sorry, I just need a little break back there, [R_Petname]."    
    elif R_Anal:
        call RogueFace("sad") 
        ch_r "The only thing you can do with my ass is kiss it, [R_Petname]."
        ch_r ". . .Don't get any ideas."   
    else:
        call RogueFace("normal", 1)
        ch_r "Not happening."    
    $ R_RecentActions.append("no anal")                      
    $ R_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label R_AnalPrep:    
            
    call Rogue_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Rogue_Bottoms_Off        
        if R_Panties or R_Legs or HoseNum("Rogue") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_r "Well, I guess some things are necessary, [R_Petname]."
            
        if R_Legs == "pants" and R_Panties:
            "She quickly pulls down her pants and drops her [R_Panties]."
        elif R_Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Rogue") >= 5 and R_Panties:
            "She quickly pulls down her [R_Hose] and drops her [R_Panties]."
            $ R_Hose = 0
        elif HoseNum("Rogue") >= 5:
            "She quickly pulls down her [R_Hose], exposing her bare ass."
            $ R_Hose = 0
        elif R_Panties:
            "She quickly pulls down her [R_Panties]."  
            
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless
        
        if Taboo: # Rogue gets started. . .
            if R_Anal:                
                "Rogue glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Rogue glances around for voyeurs. . ."
                "Rogue hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:    
            if not R_Anal:
                "Rogue bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "Rogue hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if R_Legs == "pants" and R_Panties:
            "You quickly pull down her pants and her [R_Panties] and press against her ass."
        if R_Panties and R_Legs != "pants":
            "You quickly pull down her [R_Panties] and press against her ass."  
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
    if not R_Anal:                                                      #First time stat buffs       
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -150)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 70)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 40) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 70) 
    elif not R_Loose:                                                   #first few times stat buffs       
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5) 
        else:
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 7)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no anal")
    $ R_RecentActions.append("anal")                      
    $ R_DailyActions.append("anal") 

label R_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue")
        call Rogue_Doggy_Launch("anal") 
        call RogueLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_Anal):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here? I'm getting as little sore."   
        elif Cnt == (10 + R_Anal):
                    $ R_Brows = "angry"        
                    ch_r "I'm . . .getting . . .worn out. . . here, . . [R_Petname]."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                if R_Anal >= 5 and R_Blow >= 10 and R_SEXP >= 50:
                                    $ Situation = "shift"
                                    call R_AnalAfter
                                    call R_Blowjob      
                                else:
                                    ch_r "No thanks, [R_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call R_AnalAfter
                                    call RHJ_Prep   
                        "How about a Handy?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_AnalAfter
                                call R_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Doggy_Reset
                                $ Situation = "shift"
                                jump R_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1)   
                                    call Rogue_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_r "Well if that's your attitude you can handle your own business."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_AnalAfter
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
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass                                    
                                    jump R_Anal_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                           
                        "Maybe lose some clothes. . .":
                                    call R_Undress             
                        
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call R_AnalAfter
                                            call R_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call R_AnalAfter
                                            call R_Doggy_P
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call R_AnalAfter
                                            call R_Doggy_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Line = 0
                                    jump R_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_Doggy_Reset
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_AnalAfter 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_Doggy"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Doggy_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump R_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump R_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Doggy_Reset
        
    call RogueFace("sexy") 
    
    $ R_Anal += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 3) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
    
    if "Rogue Anal Addict" in Achievements:
            pass 
            
    elif R_Anal >= 10:
        $ R_SEXP += 7
        $ Achievements.append("Rogue Anal Addict")
        if not Situation:
            call RogueFace("bemused", 1)
            ch_r "I. . . really think I enjoy this. . ."                  
    elif R_Anal == 1:            
            $R_SEXP += 25        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was . . . interesting [R_Petname]. We'll have to do that again sometime."
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "Ouch."
                    ch_r "Did you get what you needed here?"
    elif R_Anal == 5:
            ch_r "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry")
            $ R_Eyes = "side"
            ch_r  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call RogueFace("bemused")
            ch_r "That felt . . . good. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# R_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label R_Doggy_H: 
    call Shift_Focus("Rogue")
    if R_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif R_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount 
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in R_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Rogue", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
        if Approval > 2:                                                      # fix, add rogue auto stuff here
            call Rogue_Doggy_Launch("L") 
            "Rogue turns and backs up against your cock, rubbing it against her ass."
            menu:
                "What do you do?"
                "Nothing.":                     
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                    "Rogue starts to grind against you."
                "Praise her.":       
                    call RogueFace("sexy, 1")                    
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
                    ch_p "Hmmm, that's good, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue starts to grind against you."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 2)
                "Ask her to stop.":
                    call RogueFace("surprised")       
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                    ch_p "Let's not do that right now, [R_Pet]."
                    call Rogue_Namecheck
                    "Rogue pulls back."
                    call RogueOutfit
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                    
                    return            
            jump R_HotdogPrep
        else:                
            $ Tempmod = 0                               # fix, add rogue auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Rogue_Doggy_Launch("L")   
        "You press up against Rogue's backside."    
        call RogueFace("surprised", 1)
        
        if (R_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Rogue is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call RogueFace("sexy")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
            ch_r "Hmm, I've apparently got someone's attention. . ."            
            jump R_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ R_Brows = "angry"                
            menu:
                ch_r "Hmm, kinda rude, [R_Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call RogueFace("sexy", 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                        ch_r "I guess it doesn't feel so bad. . ."
                        jump R_HotdogPrep
                    "You pull back before you really get it in."                    
                    call RogueFace("bemused", 1)
                    if R_Hotdog:
                        ch_r "Well ok, [R_Petname], it has been kinda fun." 
                    else:
                        ch_r "Well ok, [R_Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -8)
                    "You grind against her asscrack."                              
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                    if not ApprovalCheck("Rogue", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call RogueFace("angry")
                        "Rogue shoves you away."
                        ch_r "Dick!"
                        ch_r "If that's how you want want to act, I'm out of here!"                                                  
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Rogue_Doggy_Reset
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")                       
                    else:
                        call RogueFace("sad")
                        "Rogue doesn't seem to be into this, but she's knows her place."                        
                        jump R_HotdogPrep
        return             
    
   
    if not R_Hotdog and "no hotdog" not in R_RecentActions:                                                               #first time    
        call RogueFace("surprised", 1)
        $ R_Mouth = "kiss"
        ch_r "Wait, so you want to grind against my butt?!"
  
        if R_Forced:
            call RogueFace("sad")
            ch_r ". . . That's all?"
        
        
    if not R_Hotdog and Approval:                                                 #First time dialog        
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
        elif R_Love >= (R_Obed + R_Inbt):
            call RogueFace("sexy")
            $ R_Brows = "sad"
            $ R_Mouth = "smile" 
            ch_r "It looks like you need some relief. . ."           
        elif R_Obed >= R_Inbt:
            call RogueFace("normal")
            ch_r "If that's what you need, [R_Petname]."
        elif R_Addict >= 50:
            call RogueFace("manic", 1)
            ch_r "Hmmm. . ."
        else: # Uninhibited 
            call RogueFace("sad")
            $ R_Mouth = "smile"             
            ch_r "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if R_Forced: 
            call RogueFace("sad")
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            ch_r "That's all you want?"  
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in R_RecentActions:
            call RogueFace("sexy", 1)
            ch_r "You want to go again? Ok."
            jump R_HotdogPrep
        elif "hotdog" in R_DailyActions:
            call RogueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_r "[Line]"
        elif R_Hotdog < 3:        
            call RogueFace("sexy", 1)
            $ R_Brows = "confused"
            $ R_Mouth = "kiss"
            ch_r "So you'd like another go?"       
        else:       
            call RogueFace("sexy", 1)
            $ Rogue_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_r "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad")
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Ok, fine."    
        elif "no hotdog" in R_DailyActions:               
            ch_r "Well, I guess it's not so bad. . ."
        else:
            call RogueFace("sexy", 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
            $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess we could do that.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_r "[Line]"
            $ Line = 0
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump R_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry")
        if "no hotdog" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no hotdog" in R_DailyActions: 
            ch_r "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in R_DailyActions:       
            ch_r "I told you \"no\" earlier, [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you that I didn't want you rubb'in up on me in public!"     
        elif not R_Hotdog:
            call RogueFace("bemused")
            ch_r "That's kinda naughty, [R_Petname]. . ."
        else:
            call RogueFace("bemused")
            ch_r "Not, right now [R_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in R_DailyActions:
                call RogueFace("bemused")
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no hotdog" not in R_DailyActions:
                call RogueFace("sexy")  
                ch_r "Yeah, maybe, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no hotdog")                      
                $ R_DailyActions.append("no hotdog")                          
                return
            "You might like it. . .":             
                if Approval:
                    call RogueFace("sexy")     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_r "[Line]"
                    $ Line = 0                   
                    jump R_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad")
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                    ch_r "Ok, fine. Whatever."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                    $ R_Forced = 1  
                    jump R_HotdogPrep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)     
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1      
    
    if "no hotdog" in R_DailyActions:
        ch_r "I just don't want to, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    if R_Forced:
        call RogueFace("angry", 1)
        ch_r "Even that's not worth it."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -1) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1)  
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1)        
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r "I'd be a bit embarassed doing that here."  
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)  
    elif R_Hotdog:
        call RogueFace("sad") 
        ch_r "Eh-eh, not anymore, [R_Petname]."
    else:
        call RogueFace("normal", 1)
        ch_r "Not interested."    
    $ R_RecentActions.append("no hotdog")                      
    $ R_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label R_HotdogPrep:  
    call Rogue_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Rogue_Bottoms_Off    
        
        if Taboo: # Rogue gets started. . .
            if R_Hotdog:                
                "Rogue glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                
            else:         
                "Rogue glances around for voyeurs. . ."
                "Rogue hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:    
            if not R_Hotdog:
                "Rogue bends over and presses her backside against you suggestively."
            else:
                "Rogue hesitantly pulls down your pants slowly backs up against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her ass."
    
    call Seen_First_Peen(1)

    if not R_Hotdog:                                                      #First time stat buffs      
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno")
    call DrainWord("Rogue","no hotdog")
    $ R_RecentActions.append("hotdog")                      
    $ R_DailyActions.append("hotdog") 

label R_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Rogue")
        call Rogue_Doggy_Launch("hotdog") 
        call RogueLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_Hotdog):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here?"   
        elif Cnt == (10 + R_Hotdog):
                    $ R_Brows = "angry"        
                    menu:
                        ch_r "I'm kinda done with this, [R_Petname]."
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_HotdogAfter
                                call R_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Doggy_Reset
                                $ Situation = "shift"
                                jump R_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1)   
                                    call Rogue_Doggy_Reset
                                    "She scowls at you and pulls away."
                                    ch_r "Well if that's your attitude you can handle your own business."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_HotdogAfter
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
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass                                    
                                    jump R_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                          
                        "Maybe lose some clothes. . .":
                                    call R_Undress    
                                    
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call R_HotdogAfter
                                        call R_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call R_HotdogAfter
                                        call R_Doggy_P
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call R_HotdogAfter
                                        call R_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call R_HotdogAfter
                                        call R_Doggy_A
                                    "Never Mind":
                                        pass
                            else:
                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Doggy_Reset
                                    $ Line = 0
                                    jump R_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming
                            if "angry" in R_RecentActions:  
                                call Rogue_Doggy_Reset
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_Doggy"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Doggy_Launch("hotdog")
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump R_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump R_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0)
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Doggy_Reset
        
    call RogueFace("sexy") 
    
    $ R_Hotdog += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 1
    
    if "Rogue Full Buns" in Achievements:
            pass 
            
    elif R_Hotdog >= 10:
        $ R_SEXP += 5
        $ Achievements.append("Rogue Full Buns")
        if not Situation:
            call RogueFace("smile", 1)
            ch_r "I think I'm getting addicted to this."               
    elif R_Hotdog == 1:            
            $R_SEXP += 10        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was pretty hot, [R_Petname], we'll have to do that again sometime."
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "Did you get what you needed here?"
    elif R_Hotdog == 5:
            ch_r "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry")
            $ R_Eyes = "side"
            ch_r "That didn't really do it for me. . ."
        else:
            call RogueFace("bemused")
            ch_r "That was an interesting diversion. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////


            
image AssBase:                  #This is the base image, used in masks
    "images/RogueDoggy/Rogue_Doggy_Ass.png"

image Dildo_Animation:
    contains:
        "UI_Dildo"
        block: 
            ease 1 pos (100,300) #pos (0,50)
            ease 1 pos (100,400) #pos (0,0)
            repeat
    
image AssTest:
#    "Dildo_Animation"
    AlphaMask("Dildo_Animation", "AssBase")
    
    