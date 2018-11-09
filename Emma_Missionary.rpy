# Start Emma Sex pose //////////////////////////////////////////////////////////////////////////////////
# E_Sex_P //////////////////////////////////////////////////////////////////////

label E_Sex_P:  
    call Shift_Focus("Emma") from _call_Shift_Focus_78
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
                    call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_2   
                    if E_Legs == "skirt":
                        "Emma slides onto her back and pulls you against her, sliding her skirt up as she does so."
                        $ E_Upskirt = 1
                    elif E_Legs == "capris" or E_Legs == "black jeans":
                        "Emma slides onto her back and pulls you against her, sliding her pants off as she does so." 
                        $ E_Upskirt = 1
                    elif E_Legs == "shorts":
                        "Emma slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                        $ E_Upskirt = 1
                    else:
                        "Emma slides onto her back and pulls you against her."
                    $ E_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                            "Emma slides it in."
                        "Praise her.":       
                            call EmmaFace("sexy, 1") from _call_EmmaFace_327                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            ch_p "Oh yeah, [E_Pet], let's do this."
                            call Emma_Namecheck from _call_Emma_Namecheck_14
                            "Emma slides it in."
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        "Ask her to stop.":
                            call EmmaFace("surprised") from _call_EmmaFace_328       
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [E_Pet]."
                            call Emma_Namecheck from _call_Emma_Namecheck_15
                            "Emma pulls back."
                            call EmmaOutfit from _call_EmmaOutfit_14
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                            return            
                    jump E_Missionary_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add Emma auto stuff here
                    $ Trigger2 = 0
                return   
    #End Emma's lead
    
    if Situation == "auto":   
                call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_3   
                if E_Legs == "skirt":
                    "You press Emma down onto her back, sliding her skirt up as you go."
                    $ E_Upskirt = 1                
                elif E_Legs == "capris" or E_Legs == "black jeans":
                    "You press Emma down onto her back, sliding her pants down as you do."    
                    $ E_Upskirt = 1
                elif E_Legs == "shorts":
                    "You press Emma down onto her back, sliding her shorts down as you do."                
                    $ E_Upskirt = 1
                else:
                    "You press Emma down onto her back."
                $ E_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call EmmaFace("surprised", 1) from _call_EmmaFace_329
                
                if (E_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Emma is briefly startled, but melts into a sly smile."
                    call EmmaFace("sexy") from _call_EmmaFace_330
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_e "Ok, show me what you can do, [E_Petname]."            
                    jump E_Missionary_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ E_Brows = "angry"                
                    menu:
                        ch_e "Um, what do you think you're doing?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call EmmaFace("sexy", 1) from _call_EmmaFace_331
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                                    ch_e "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                                    jump E_Missionary_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call EmmaFace("bemused", 1) from _call_EmmaFace_332
                                    if E_Sex:
                                        ch_e "Maybe you could warn me?" 
                                    else:
                                        ch_e "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                            
                        "Just fucking.":                    
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            "You press inside some more."                              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            if not ApprovalCheck("Emma", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call EmmaFace("angry") from _call_EmmaFace_333
                                "Emma shoves you away and slaps you in the face."
                                ch_e "Jerk!"
                                ch_e "I am not putting up with that shit!"                                                  
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_9
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")                    
                            else:
                                call EmmaFace("sad") from _call_EmmaFace_334
                                "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump E_Missionary_SexPrep
                return   
    #End Auto
    
   
    if not E_Sex and "no sex" not in E_RecentActions:                           
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_335
            $ E_Mouth = "kiss"
            ch_e "I've never done it with a student before. . . "    
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_336
                ch_e "You'd really do this when you have me over a barrel?"
            
            
    if not E_Sex and Approval:                                                  
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_337
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -30, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -20, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_338
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I don't want you to think I'm some kind of slut. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_339
                ch_e "I suppose if it's you, [E_Petname]. . ."            
            elif E_Addict >= 50:
                call EmmaFace("manic", 1) from _call_EmmaFace_340
                ch_e "I have kind of been hoping you might. . ."
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_341
                $ E_Mouth = "smile"             
                ch_e "I can't say i haven't thought about it sometimes. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call EmmaFace("sexy", 1) from _call_EmmaFace_342
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_343
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "Again? Why do you do this to me?" 
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I guess this is more secluded. . ."        
            elif "sex" in E_RecentActions:
                ch_e "Another round? {i}Fine.{/i}"
                jump E_Missionary_SexPrep
            elif "sex" in E_DailyActions:
                $ Line = renpy.random.choice(["Back again so soon? How expectable!",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_e "[Line]"
            elif E_Sex < 3:        
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "So you'd like another round?"       
            else:       
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "Think you can make me scream?",
                    "You wanna slide into me?"]) 
                ch_e "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_344
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fiiiiine."  
            elif "no sex" in E_DailyActions:               
                ch_e "You've made your case. . ."
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_345
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump E_Missionary_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call EmmaFace("angry") from _call_EmmaFace_346       
            if "no sex" in E_RecentActions:  
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no sex" in E_DailyActions:  
                ch_e "I already told you. . .not in public!" 
            elif "no sex" in E_DailyActions:       
                ch_e "I already told you \"no.\""
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you this is too public!"     
            elif not E_Sex:
                call EmmaFace("bemused") from _call_EmmaFace_347
                ch_e "I don't know that I'm. . . ready? . ."
            else:
                call EmmaFace("bemused") from _call_EmmaFace_348
                ch_e "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in E_DailyActions:
                        call EmmaFace("bemused") from _call_EmmaFace_349
                        ch_e "It's cool."
                        return
                "Maybe later?" if "no sex" not in E_DailyActions:
                        call EmmaFace("sexy") from _call_EmmaFace_350  
                        ch_e "Maybe, you never know."
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
                            call EmmaFace("sexy") from _call_EmmaFace_351     
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                            $ Line = renpy.random.choice(["That's. . . true. . .",     
                                "I suppose. . .", 
                                "That's. . . that's a good point. . ."]) 
                            ch_e "[Line]"
                            $ Line = 0                   
                            jump E_Missionary_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Emma", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and E_Forced):
                            call EmmaFace("sad") from _call_EmmaFace_352
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                            ch_e "Well! . .  ok, fine, stick it in."  
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                            $ E_Forced = 1  
                            jump E_Missionary_SexPrep
                        else:                          
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)   
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no sex" in E_DailyActions:
        ch_e "Maybe take \"no\" for an answer?" 
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_353
        ch_e "Not even."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_354
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "I can't believe you'd even consider it around here!"      
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
    elif E_Sex:
        call EmmaFace("sad") from _call_EmmaFace_355 
        ch_e "Maybe just fuck yourself, huh?."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_356
        ch_e "Nuhuh."     
    $ E_RecentActions.append("no sex")                      
    $ E_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label E_Missionary_SexPrep:
    call Emma_Sex_Launch("hotdog") from _call_Emma_Sex_Launch_4
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_2       
        
        
        if E_Panties or E_Legs or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_e "We can't exactly do much like this, huh."
        
        if E_Panties == "zipper panties":
            "She pulls the zippers down"
            $ E_Panties = "zipper panties open"
            if E_Chest == "bustier bra":
                $ E_Chest = "bustier bra open"
        elif E_Panties == "zipper panties open":
            ch_e "I'm ready"    
        elif E_Panties and (E_Legs == "capris" or E_Legs == "black jeans"):
            "She quickly drops her pants and her [E_Panties]."
        elif E_Panties and E_Legs == "shorts":
            "She quickly drops her shorts and her [E_Panties]."
        elif E_Legs == "capris" or E_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif E_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Emma") >= 5 and E_Panties:
            "She shrugs and her [E_Hose] and [E_Panties] fall to the ground."
            $ E_Hose = 0
        elif HoseNum("Emma") >= 5:
            "She shrugs and her [E_Hose] fall to the ground."
            $ E_Hose = 0
        elif E_Panties:
            "She shrugs as her [E_Panties] fall to the ground."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless from _call_Emma_First_Bottomless_2
        
        if Taboo: # Emma gets started. . .
            if not E_Sex:
                "Emma glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Sex:
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Emma leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"  
        if E_Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ E_Panties = "zipper panties open"
            if E_Chest == "bustier bra":
                $ E_Chest = "bustier bra open"
        elif E_Panties == "zipper panties open":
            "You get ready"    
        else:     
            if E_Legs == "pants" and E_Panties:
                "You quickly pull down her pants and her [E_Panties] and press against her slit."
            if E_Panties and E_Legs != "pants":
                "You quickly pull down her [E_Panties] and press against her slit."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_3
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_9
    
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
        call DrainWord("Emma","tabno") from _call_DrainWord_49
    call DrainWord("Emma","no sex") from _call_DrainWord_50
    $ E_RecentActions.append("sex")                      
    $ E_DailyActions.append("sex") 

label E_Missionary_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_79
        call Emma_Sex_Launch("sex") from _call_Emma_Sex_Launch_5 
        call EmmaLust from _call_EmmaLust_7        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ E_Upskirt = 1
        $ E_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Sex):
                    $ E_Brows = "confused"
                    ch_e "So are we getting close here?"   
        elif Cnt == (10 + E_Sex):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_SexAfter from _call_E_Missionary_SexAfter
                                call E_Blowjob from _call_E_Blowjob_5       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Missionary_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_10
                                $ Situation = "shift"
                                jump E_Missionary_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_357   
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_11
                                    "She scowls at you and pulls out."
                                    ch_e "Not with that attitude, boy!"
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Missionary_SexAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    # if ("master" in E_Petnames or "sir" in E_Petnames or E_Pet == "slave") and ApprovalCheck("Emma", 750, "O") and not E_Bondage: # bondage event
                    #     $ E_Bondage = 1
                    #     ch_e "Hey, [E_Petname], I've got some new things here, do you think we could try them?"
                    #     "She grabs what it looks like some bondage gear"
                    #     menu:
                    #         "Yep":
                    #             call EmmaFace("sexy", 1) 
                    #             #if E_Over or E_Chest or E_Panties or E_Legs:
                    #             #    "She glances up at you as her clothes drop to the ground."
                    #             #$ E_Over = 0
                    #             #$ E_Legs = 0
                    #             #$ E_Chest = 0
                    #             #$ E_Panties = 0
                    #             "She starts dressing the new outfit"
                    #             "You help her with the armbinder, making sure she can't move her arms"
                    #             #"And add a blindfold so she can't see a thing"
                    #             #$ E_Blindfold = 1
                    #             $ E_Over = "armbinder"
                    #             #$ E_Chest = "bustier bra"
                    #             #$ E_Panties = "zipper panties"
                    #             #$ E_Outfit = "zipper bondage"
                    #             #$ E_Shame = E_OutfitShame[1]
                    #             #if E_Over == "armbinder":
                    #             #call EmmaFace("sly")
                    #             $ Line = "Emma can't move her arms. She licks her lips in anticipation"
                    #             $ TempLust += 3 if E_Lust < 40 else 1  

                    #             #if E_Blow <= 1 or (E_Obed >= 500 and E_Obed > E_Inbt):
                    #             #        $ TempLust += 2 if E_Lust > 60 else 0                 
                    #             #        $ Line = Line + ", but she seems to be waiting for some instruction"
                    #             #else:
                    #             #        $ Line = Line + ", and then she gets started licking your cock"
                    #             #        $ Speed = 1
                    #             #jump E_HotdogPrep
                    #             #pass
                    #             #call Emma_Bottoms_Off_Legs
                    #             #call Emma_Top_Off
                    #             #call Emma_Bottoms_Off
                    #             #shes gonna wear it
                    #         "Not now, but let's save it for another time":
                    #             pass
                    #             #nope
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed > 0:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass

                        # "How about you put that armbinder" if E_Bondage and E_Over != "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "armbinder"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the armbinder" if E_Over == "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put that bondage outfit" if E_Bondage and E_Over != "bondage":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put those bondage cuffs" if E_Bondage and E_Over != "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage cuffs"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the bondage outfit" if E_Over == "bondage" or E_Over == "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass from _call_E_Slap_Ass_2                                    
                                    jump E_Missionary_Sex_Cycle 

                        "Put her legs up" if not E_LegsUp:
                                    $ E_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if E_LegsUp:
                                    $ E_LegsUp = 0
                                    "You put her legs down."
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_7  
                        
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call E_Missionary_SexAfter from _call_E_Missionary_SexAfter_1
                                            call E_Sex_A from _call_E_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call E_Missionary_SexAfter from _call_E_Missionary_SexAfter_2
                                            call E_Sex_A from _call_E_Sex_A_1
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call E_Missionary_SexAfter from _call_E_Missionary_SexAfter_3
                                            call E_Sex_H from _call_E_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I'm kinda tired here? Could we end it here?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_5
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm kinda tired here? Could we end it here?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_12
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_13
                                    $ Line = 0
                                    jump E_Missionary_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_16
        
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_6
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_14
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Missionary_SexAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if renpy.showing("Emma_SexSprite"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_17
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Missionary_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Sex_Launch(Trigger) from _call_Emma_Sex_Launch_6
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Missionary_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump E_Missionary_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump E_Missionary_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to come to an end now, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_358
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Missionary_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset from _call_Emma_Sex_Reset_15
        
    call EmmaFace("sexy") from _call_EmmaFace_359 
    
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
            call EmmaFace("smile", 1) from _call_EmmaFace_360
            ch_e "I just can't seem to quit you."               
    elif E_Sex == 1:            
            $E_SEXP += 20        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I feel like I've been waiting a million years for that."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "I hope that was worth the wait."
    elif E_Sex == 5:
            ch_e "Why did we not do this sooner?!"  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_361
            $ E_Eyes = "side"
            ch_e "Could you have maybe paid more attention? . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_362
            ch_e "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Did you want to try something else?"
    call Checkout from _call_Checkout_36
    return   

# End Emma sex //////////////////////////////////////////////////////////////////////////////////


# Emma anal //////////////////////////////////////////////////////////////////////

label E_Sex_A:
    call Shift_Focus("Emma") from _call_Shift_Focus_80
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
    
    if Situation == "Emma":                                                                  
            #Emma auto-starts   
            if Approval > 2:                                                      # fix, add Emma auto stuff here
                call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_7   
                if E_Legs == "skirt":
                    "Emma slides onto her back and pulls you against her, sliding her skirt up as she does so."
                    $ E_Upskirt = 1
                elif E_Legs == "capris" or E_Legs == "black jeans":
                    "Emma slides onto her back and pulls you against her, sliding her pants off as she does so." 
                    $ E_Upskirt = 1
                elif E_Legs == "shorts":
                    "Emma slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                    $ E_Upskirt = 1
                else:
                    "Emma slides onto her back and pulls you against her."
                $ E_SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                        "Emma slides it in."
                    "Praise her.":       
                        call EmmaFace("sexy, 1") from _call_EmmaFace_363                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        ch_p "Ooo, dirty girl, [E_Pet], let's do this."
                        call Emma_Namecheck from _call_Emma_Namecheck_16
                        "Emma slides it in."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised") from _call_EmmaFace_364       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck from _call_Emma_Namecheck_17
                        "Emma pulls back."
                        call EmmaOutfit from _call_EmmaOutfit_15
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                        return            
                jump E_Missionary_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add Emma auto stuff here
                $ Trigger2 = 0
            return  
            #end if Emma initiates
    
    if Situation == "auto":   
            call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_8   
            if E_Legs == "skirt":
                "You press Emma down onto her back, sliding her skirt up as you go."
                $ E_Upskirt = 1                
            elif E_Legs == "capris" or E_Legs == "black jeans":
                "You press Emma down onto her back, sliding her pants down as you do."    
                $ E_Upskirt = 1
            elif E_Legs == "shorts":
                "You press Emma down onto her back, sliding her shorts down as you do."                
                $ E_Upskirt = 1
            else:
                "You press Emma down onto her back."
            $ E_SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call EmmaFace("surprised", 1) from _call_EmmaFace_365
            
            if (E_Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                if E_Loose:
                    "Emma is briefly startled, but melts into a sly smile."
                    ch_e "Yes, stick it in, haven't done it for far too long! "            
                else:
                    "Emma is briefly startled, but shrugs."
                    ch_e "You may. . ."                  
                jump E_Missionary_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Um what are you doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1) from _call_EmmaFace_366
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "Well just take it easy, ok? . ."
                            jump E_Missionary_AnalPrep
                        "You pull back before you really get it in."                    
                        call EmmaFace("bemused", 1) from _call_EmmaFace_367
                        
                        if E_Anal:
                            ch_e "Maybe you could warn me?" 
                        else:
                            ch_e "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                           
                    "Just fucking.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                        "You press into her."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 700, "O", TabM=1):                        
                            call EmmaFace("angry") from _call_EmmaFace_368
                            "Emma shoves you away and slaps you in the face."
                            ch_e "Asshole!"
                            ch_e "You need to ask nicer than that!"                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset from _call_Emma_Sex_Reset_16
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                        
                        else:
                            call EmmaFace("sad") from _call_EmmaFace_369
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump E_Missionary_AnalPrep
            return  
            #end "auto" 
    
   
    if not E_Anal and "no anal" not in E_RecentActions:                                                               
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_370
            $ E_Mouth = "kiss"
            ch_e "You want to go in the \"out\" door?!"
      
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_371
                ch_e "Anal? Really?"
        
    if not E_Loose and ("dildo anal" in E_DailyActions or "anal" in E_DailyActions):
            #if she's done anal stuff today
            call EmmaFace("bemused", 1) from _call_EmmaFace_372
            ch_e "I'm not really over the last time."            
    elif "anal" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_373
            ch_e "Again? K."
            jump E_Missionary_AnalPrep
        
    
    if not E_Anal and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_374
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_375
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I guess? . ."           
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_376
                ch_e "Well. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1) from _call_EmmaFace_377
                ch_e "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_378
                $ E_Mouth = "smile"             
                ch_e "Anything's worth a shot. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_379
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "You really ask a lot here. . ."
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I guess this is out of the way. . ."   
            elif "anal" in E_DailyActions and not E_Loose:
                pass      
            elif "anal" in E_RecentActions:
                ch_e "I guess I'm warmed up. . ."
                jump E_Missionary_AnalPrep
            elif "anal" in E_DailyActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_380
                $ Line = renpy.random.choice(["Back again so soon? Just as i expected!",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_e "[Line]"    
            else:       
                call EmmaFace("sexy", 1) from _call_EmmaFace_381
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I do have booty for days. . .", 
                    "Think you can make me scream?",
                    "You wanna slide into me?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_382
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."   
            elif "no anal" in E_DailyActions:               
                ch_e "Well, ok, I've given it some thought, fine. . ." 
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_383
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump E_Missionary_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry") from _call_EmmaFace_384
            if "no anal" in E_RecentActions:  
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no anal" in E_DailyActions:
                ch_e "I already told you. . .not in public!" 
            elif "no anal" in E_DailyActions:       
                ch_e "I already told you \"no.\""
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you this is too public!"      
            elif not E_Anal:
                call EmmaFace("bemused") from _call_EmmaFace_385
                ch_e "I don't know that I'm. . . that kind of girl?"
            elif not E_Loose and "anal" not in E_DailyActions:
                call EmmaFace("perplexed") from _call_EmmaFace_386
                ch_e "That was kind of. . . rough last time?"
            else:
                call EmmaFace("bemused") from _call_EmmaFace_387
                ch_e "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in E_DailyActions:
                    call EmmaFace("bemused") from _call_EmmaFace_388
                    ch_e "It's cool."              
                    return
                "Maybe later?" if "no anal" not in E_DailyActions:
                    call EmmaFace("sexy") from _call_EmmaFace_389  
                    ch_e "Maybe, you never know."
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
                        call EmmaFace("sexy") from _call_EmmaFace_390     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["That's. . . true. . .",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_Missionary_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad") from _call_EmmaFace_391
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                        ch_e "Well! . .  ok, fine, stick it in."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        $ E_Forced = 1  
                        jump E_Missionary_AnalPrep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no anal" in E_DailyActions:
        ch_e "Maybe take \"no\" for an answer?"   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_392
        ch_e "That's a bit much, even for you, darling."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)       
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_393
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "You're being ridiculous. That? Here?!"    
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3) 
    elif not E_Loose and "anal" in E_DailyActions:
        call EmmaFace("bemused") from _call_EmmaFace_394
        ch_e "I'm a little sore here?"    
    elif E_Anal:
        call EmmaFace("sad") from _call_EmmaFace_395 
        ch_e "That's totally off the table."
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_396
        ch_e "No."    
    $ E_RecentActions.append("no anal")                      
    $ E_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label E_Missionary_AnalPrep:    
            
    call Emma_Sex_Launch("hotdog") from _call_Emma_Sex_Launch_9
    
    if Situation != "auto":
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_3        
        if E_Panties or E_Legs or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_e "We can't exactly do much like this, huh."

        if E_Panties == "zipper panties":
            "She pulls the zippers down"
            $ E_Panties = "zipper panties open"
            if E_Chest == "bustier bra":
                $ E_Chest = "bustier bra open"
        elif E_Panties == "zipper panties open":
            ch_e "I'm ready"  
        elif E_Panties and (E_Legs == "capris" or E_Legs == "black jeans"):
            "She quickly drops her pants and her [E_Panties]."
        elif E_Panties and E_Legs == "shorts":
            "She quickly drops her shorts and her [E_Panties]."
        elif E_Legs == "capris" or E_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif E_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Emma") >= 5 and E_Panties:
            "She shrugs and her [E_Hose] and [E_Panties] fall to the ground."
            $ E_Hose = 0
        elif HoseNum("Emma") >= 5:
            "She shrugs and her [E_Hose] fall to the ground."
            $ E_Hose = 0
        elif E_Panties:
            "She shrugs as her [E_Panties] fall to the ground."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless from _call_Emma_First_Bottomless_4
        
        if Taboo: # Emma gets started. . .
            if E_Anal:                
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Emma glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if not E_Anal:
                "Emma leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if E_Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ E_Panties = "zipper panties open"
            if E_Chest == "bustier bra":
                $ E_Chest = "bustier bra open"
        elif E_Panties == "zipper panties open":
            "You get ready"  
        else: 
            if E_Legs == "pants" and E_Panties:
                "You quickly pull down her pants and her [E_Panties] and press against her back door."
            if E_Panties and E_Legs != "pants":
                "You quickly pull down her [E_Panties] and press against her back door."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_5
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_10
    
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
        call DrainWord("Emma","tabno") from _call_DrainWord_51
    call DrainWord("Emma","no anal") from _call_DrainWord_52
    $ E_RecentActions.append("anal")                      
    $ E_DailyActions.append("anal") 

label E_Missionary_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_81
        call Emma_Sex_Launch("anal") from _call_Emma_Sex_Launch_10 
        call EmmaLust from _call_EmmaLust_8        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        $ E_Upskirt = 1
        $ E_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    if E_Loose:
                        ch_e "So are we getting close here?"  
                    else:
                        ch_e "So are we getting close here? This is not super pleasant. . ."   
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                if E_Anal >= 5 and E_Blow >= 10 and E_SEXP >= 50:
                                    $ Situation = "shift"
                                    call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter
                                    call E_Blowjob from _call_E_Blowjob_6      
                                else:
                                    ch_e "No thanks, [E_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter_1
                                    call EHJ_Prep from _call_EHJ_Prep   
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter_2
                                call E_Handjob from _call_E_Handjob_5     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Missionary_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_17
                                $ Situation = "shift"
                                jump E_Missionary_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_397   
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_18
                                    "She scowls at you and pulls out."
                                    ch_e "Not with that attitude, boy!"                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Missionary_AnalAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    # if ("master" in E_Petnames or "sir" in E_Petnames or E_Pet == "slave") and ApprovalCheck("Emma", 750, "O") and not E_Bondage: # bondage event
                    #     $ E_Bondage = 1
                    #     ch_e "Hey, [E_Petname], I've got some new things here, do you think we could try them?"
                    #     "She grabs what it looks like some bondage gear"
                    #     menu:
                    #         "Yep":
                    #             call EmmaFace("sexy", 1) 
                    #             #if E_Over or E_Chest or E_Panties or E_Legs:
                    #             #    "She glances up at you as her clothes drop to the ground."
                    #             #$ E_Over = 0
                    #             #$ E_Legs = 0
                    #             #$ E_Chest = 0
                    #             #$ E_Panties = 0
                    #             "She starts dressing the new outfit"
                    #             "You help her with the armbinder, making sure she can't move her arms"
                    #             #"And add a blindfold so she can't see a thing"
                    #             #$ E_Blindfold = 1
                    #             $ E_Over = "armbinder"
                    #             #$ E_Chest = "bustier bra"
                    #             #$ E_Panties = "zipper panties"
                    #             #$ E_Outfit = "zipper bondage"
                    #             #$ E_Shame = E_OutfitShame[1]
                    #             #if E_Over == "armbinder":
                    #             #call EmmaFace("sly")
                    #             $ Line = "Emma can't move her arms. She licks her lips in anticipation"
                    #             $ TempLust += 3 if E_Lust < 40 else 1  

                    #             #if E_Blow <= 1 or (E_Obed >= 500 and E_Obed > E_Inbt):
                    #             #        $ TempLust += 2 if E_Lust > 60 else 0                 
                    #             #        $ Line = Line + ", but she seems to be waiting for some instruction"
                    #             #else:
                    #             #        $ Line = Line + ", and then she gets started licking your cock"
                    #             #        $ Speed = 1
                    #             #jump E_HotdogPrep
                    #             #pass
                    #             #call Emma_Bottoms_Off_Legs
                    #             #call Emma_Top_Off
                    #             #call Emma_Bottoms_Off
                    #             #shes gonna wear it
                    #         "Not now, but let's save it for another time":
                    #             pass
                    #             #nope
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed > 0:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass

                        # "How about you put that armbinder" if E_Bondage and E_Over != "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "armbinder"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the armbinder" if E_Over == "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put that bondage outfit" if E_Bondage and E_Over != "bondage":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put those bondage cuffs" if E_Bondage and E_Over != "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage cuffs"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the bondage outfit" if E_Over == "bondage" or E_Over == "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass from _call_E_Slap_Ass_3                                    
                                    jump E_Missionary_Anal_Cycle  

                        "Put her legs up" if not E_LegsUp:
                                    $ E_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if E_LegsUp:
                                    $ E_LegsUp = 0
                                    "You put her legs down."
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0       
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_8  
                        
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter_3
                                            call E_Sex_P from _call_E_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter_4
                                            call E_Sex_P from _call_E_Sex_P_1
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call E_Missionary_AnalAfter from _call_E_Missionary_AnalAfter_5
                                            call E_Sex_H from _call_E_Sex_H_1
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I'm kinda tired here? Could we come to an end?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_6
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm kinda tired here? Could we come to an end?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_19
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_20
                                    $ Line = 0
                                    jump E_Missionary_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_17
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_7
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_21
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Missionary_AnalAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if renpy.showing("Emma_SexSprite"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_18
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Missionary_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Sex_Launch(Trigger) from _call_Emma_Sex_Launch_11
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Missionary_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump E_Missionary_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump E_Missionary_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to come to an end, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_398
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Missionary_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset from _call_Emma_Sex_Reset_22
        
    call EmmaFace("sexy") from _call_EmmaFace_399 
    
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
            call EmmaFace("bemused", 1) from _call_EmmaFace_400
            ch_e "I didn't think I'd love this so much!"                  
    elif E_Anal == 1:            
            $E_SEXP += 25        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "Anal. . . huh, who knew?"
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Ouch."
                    ch_e "I guess you got what you needed?"
    elif E_Anal == 5:
            ch_e "I'm really starting to love this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_401
            $ E_Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_402
            ch_e "Ok, that was fun. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_37
    return   


# End Emma Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Emma hotdog //////////////////////////////////////////////////////////////////////

label E_Sex_H: 
    call Shift_Focus("Emma") from _call_Shift_Focus_82
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
    
    if Situation == "Emma":                                                                  
            #Emma auto-starts   
            if Approval > 2:                                                      # fix, add Emma auto stuff here
                call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_12 
                "Emma slides onto her back and pulls you against her, rubbing it against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        "Emma starts to grind against you."
                    "Praise her.":       
                        call EmmaFace("sexy, 1") from _call_EmmaFace_403                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
                        ch_p "Hmmm, that's good, [E_Pet]."
                        call Emma_Namecheck from _call_Emma_Namecheck_18
                        "Emma starts to grind against you."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised") from _call_EmmaFace_404       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck from _call_Emma_Namecheck_19
                        "Emma pulls back."
                        call EmmaOutfit from _call_EmmaOutfit_16
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                        return            
                jump E_Missionary_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add Emma auto stuff here
                $ Trigger2 = 0
            return            
            #end Emma initates
    
    if Situation == "auto":   
            call Emma_Sex_Launch("L") from _call_Emma_Sex_Launch_13   
            "You press Emma down onto her back and press your cock against her."    
            call EmmaFace("surprised", 1) from _call_EmmaFace_405
            
            if (E_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Emma is briefly startled, but melts into a sly smile."
                call EmmaFace("sexy") from _call_EmmaFace_406
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                ch_e "Hmm, I've apparently got someone's attention. . ."            
                jump E_Missionary_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Hey, you got to earn it first, [E_Petname]." 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1) from _call_EmmaFace_407
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "I guess it doesn't feel so bad. . ."
                            jump E_Missionary_HotdogPrep
                        "You pull back from her."                    
                        call EmmaFace("bemused", 1) from _call_EmmaFace_408
                        ch_e "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"                                             
                    "You'll see.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                        "You grind against her crotch."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call EmmaFace("angry") from _call_EmmaFace_409
                            "Emma shoves you away."
                            ch_e "Jerk!"
                            ch_e "I'm not into that!"                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset from _call_Emma_Sex_Reset_23
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                       
                        else:
                            call EmmaFace("sad") from _call_EmmaFace_410
                            "Emma doesn't seem to be into this, but she's knows her place."                        
                            jump E_Missionary_HotdogPrep
            return     
            #end auto
    
   
    if not E_Hotdog and "no hotdog" not in E_RecentActions:                                                               
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_411
            $ E_Mouth = "kiss"
            ch_e "So, just grinding against me?"
      
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_412
                ch_e ". . . That's it?"
        
        
    if not E_Hotdog and Approval:                                                
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_413
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_414
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "It does look a bit swolen. . ."           
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_415
                ch_e "If you want. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1) from _call_EmmaFace_416
                ch_e "Hmmm. . ."
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_417
                $ E_Mouth = "smile"             
                ch_e "Hmm, you look ready to go. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_418
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "That's {i}all{/i} you want?"  
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I guess this is a better location . ."   
            elif "hotdog" in E_RecentActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_419
                ch_e "Again? Ok."
                jump E_Missionary_HotdogPrep
            elif "hotdog" in E_DailyActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_420
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really digging this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_e "[Line]"    
            else:       
                call EmmaFace("sexy", 1) from _call_EmmaFace_421
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really digging this. . .", 
                    "You want another rub?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_422
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."    
            elif "no hotdog" in E_DailyActions:               
                ch_e "Well, I guess it's not so bad. . ."
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_423
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump E_Missionary_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry") from _call_EmmaFace_424
            if "no hotdog" in E_RecentActions:  
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no hotdog" in E_DailyActions: 
                ch_e "I{i}just{/i} told, not in public!" 
            elif "no hotdog" in E_DailyActions:       
                ch_e "I{i}just{/i} told you \"no\" earlier!"
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I{i}just{/i} told you, not in public!"  
            elif not E_Hotdog:
                call EmmaFace("bemused") from _call_EmmaFace_425
                ch_e "That's kinda hot, [E_Petname]. . ."
            else:
                call EmmaFace("bemused") from _call_EmmaFace_426
                ch_e "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in E_DailyActions:
                    call EmmaFace("bemused") from _call_EmmaFace_427
                    ch_e "No problem."              
                    return
                "Maybe later?" if "no hotdog" not in E_DailyActions:
                    call EmmaFace("sexy") from _call_EmmaFace_428  
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
                        call EmmaFace("sexy") from _call_EmmaFace_429     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                        $ Line = renpy.random.choice(["Well, sure, ok.",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_Missionary_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad") from _call_EmmaFace_430
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                        ch_e "Ok, fine. Whatever."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                        $ E_Forced = 1  
                        jump E_Missionary_HotdogPrep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)     
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1      
    
    if "no hotdog" in E_DailyActions:
        ch_e "I'm just not into that."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    if E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_431
        ch_e "Yeah, not happening."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1)  
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_432        
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e " not here though?"  
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif E_Hotdog:
        call EmmaFace("sad") from _call_EmmaFace_433 
        ch_e "Yeah, not again."
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_434
        ch_e "No."    
    $ E_RecentActions.append("no hotdog")                      
    $ E_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label E_Missionary_HotdogPrep:  
    call Emma_Sex_Launch("hotdog") from _call_Emma_Sex_Launch_14
    
    if Situation != "auto":
#        call Emma_Bottoms_Off    
        
        if Taboo: # Emma gets started. . .
            if E_Hotdog:                
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                
            else:         
                "Emma glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:                
            if "cockout" in P_RecentActions:
                "Emma slowly presses against your rigid member."
            else:
                "Emma hesitantly pulls down your pants slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her mound."
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_11
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
        call DrainWord("Emma","tabno") from _call_DrainWord_53
    call DrainWord("Emma","no hotdog") from _call_DrainWord_54
    $ E_RecentActions.append("hotdog")                      
    $ E_DailyActions.append("hotdog") 

label E_Missionary_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_83
        call Emma_Sex_Launch("hotdog") from _call_Emma_Sex_Launch_15 
        call EmmaLust from _call_EmmaLust_9        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Hotdog):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here?"   
        elif Cnt == (10 + E_Hotdog):
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "This is getting a bit dull."
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_HotdogAfter from _call_E_Missionary_HotdogAfter
                                call E_Blowjob from _call_E_Blowjob_7       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump E_Missionary_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_24
                                $ Situation = "shift"
                                jump E_Missionary_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_435   
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_25
                                    "She scowls at you and pulls away."
                                    ch_e "Not with that attitude, mister!"                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_Missionary_HotdogAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    # if ("master" in E_Petnames or "sir" in E_Petnames or E_Pet == "slave") and ApprovalCheck("Emma", 750, "O") and not E_Bondage: # bondage event
                    #     $ E_Bondage = 1
                    #     ch_e "Hey, [E_Petname], I've got some new things here, do you think we could try them?"
                    #     "She grabs what it looks like some bondage gear"
                    #     menu:
                    #         "Yep":
                    #             call EmmaFace("sexy", 1) 
                    #             #if E_Over or E_Chest or E_Panties or E_Legs:
                    #             #    "She glances up at you as her clothes drop to the ground."
                    #             #$ E_Over = 0
                    #             #$ E_Legs = 0
                    #             #$ E_Chest = 0
                    #             #$ E_Panties = 0
                    #             "She starts dressing the new outfit"
                    #             "You help her with the armbinder, making sure she can't move her arms"
                    #             #"And add a blindfold so she can't see a thing"
                    #             #$ E_Blindfold = 1
                    #             $ E_Over = "armbinder"
                    #             #$ E_Chest = "bustier bra"
                    #             #$ E_Panties = "zipper panties"
                    #             #$ E_Outfit = "zipper bondage"
                    #             #$ E_Shame = E_OutfitShame[1]
                    #             #if E_Over == "armbinder":
                    #             #call EmmaFace("sly")
                    #             $ Line = "Emma can't move her arms. She licks her lips in anticipation"
                    #             $ TempLust += 3 if E_Lust < 40 else 1  

                    #             #if E_Blow <= 1 or (E_Obed >= 500 and E_Obed > E_Inbt):
                    #             #        $ TempLust += 2 if E_Lust > 60 else 0                 
                    #             #        $ Line = Line + ", but she seems to be waiting for some instruction"
                    #             #else:
                    #             #        $ Line = Line + ", and then she gets started licking your cock"
                    #             #        $ Speed = 1
                    #             #jump E_HotdogPrep
                    #             #pass
                    #             #call Emma_Bottoms_Off_Legs
                    #             #call Emma_Top_Off
                    #             #call Emma_Bottoms_Off
                    #             #shes gonna wear it
                    #         "Not now, but let's save it for another time":
                    #             pass
                    #             #nope
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

                        # "How about you put that armbinder" if E_Bondage and E_Over != "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "armbinder"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the armbinder" if E_Over == "armbinder":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put that bondage outfit" if E_Bondage and E_Over != "bondage":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "How about you put those bondage cuffs" if E_Bondage and E_Over != "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = "bondage cuffs"
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]

                        # "Remove the bondage outfit" if E_Over == "bondage" or E_Over == "bondage cuffs":
                        #     call EmmaFace("sexy", 1) 
                        #     #if E_Over or E_Chest or E_Panties or E_Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ E_Over = 0
                        #     #$ E_Legs = 0
                        #     #$ E_Chest = 0
                        #     #$ E_Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ E_Blindfold = 1
                        #     $ E_Over = 0
                        #     #$ E_Chest = "bustier bra"
                        #     #$ E_Panties = "zipper panties"
                        #     #$ E_Outfit = "zipper bondage"
                        #     #$ E_Shame = E_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass from _call_E_Slap_Ass_4                                    
                                    jump E_Missionary_Hotdog_Cycle  

                        "Put her legs up" if not E_LegsUp:
                                    $ E_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if E_LegsUp:
                                    $ E_LegsUp = 0
                                    "You put her legs down."
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_9
                                    
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call E_Missionary_HotdogAfter from _call_E_Missionary_HotdogAfter_1
                                        call E_Sex_P from _call_E_Sex_P_2
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call E_Missionary_HotdogAfter from _call_E_Missionary_HotdogAfter_2
                                        call E_Sex_P from _call_E_Sex_P_3
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call E_Missionary_HotdogAfter from _call_E_Missionary_HotdogAfter_3
                                        call E_Sex_A from _call_E_Sex_A_2
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call E_Missionary_HotdogAfter from _call_E_Missionary_HotdogAfter_4
                                        call E_Sex_A from _call_E_Sex_A_3
                                    "Never Mind":
                                        pass
                            else:
                                ch_e "I'm kinda tired here? Could we come to an end?"  
                    
                        "I also want to. . .[[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_7
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm kinda tired here? Could come to an end?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_26
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_27
                                    $ Line = 0
                                    jump E_Missionary_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_18
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_8
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_28
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_Missionary_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Emma can cum
                    if renpy.showing("Emma_SexSprite"):                    #If you're still going at it,
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_19
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump E_Missionary_SexAfter
                        elif "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,                    
                            call Emma_Sex_Launch("hotdog") from _call_Emma_Sex_Launch_16
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump E_Missionary_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump E_Missionary_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump E_Missionary_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to come to an end, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_436
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    

    
label E_Missionary_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset from _call_Emma_Sex_Reset_29
        
    call EmmaFace("sexy") from _call_EmmaFace_437 
    
    $ E_Hotdog += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if E_Loc == bg_current and "noticed Emma" in E_RecentActions: #If Emma was participating
        $ E_LikeEmma += 1
    
    if E_Hotdog == 10:
        $ E_SEXP += 5             
    elif E_Hotdog == 1:            
            $E_SEXP += 10        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I. . . liked that a lot."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Well, did that work for you?"
    elif E_Hotdog == 5:
            ch_e "I'm surprised how much I enjoy this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry") from _call_EmmaFace_438
            $ E_Eyes = "side"
            ch_e "I didn't get much out of that. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_439
            ch_e "I could get into that. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_38
    return   

# End Emma hotdogging //////////////////////////////////////////////////////////////////////////////////
