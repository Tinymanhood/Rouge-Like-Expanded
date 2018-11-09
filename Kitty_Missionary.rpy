# Start Kitty Sex pose //////////////////////////////////////////////////////////////////////////////////
# K_Sex_P //////////////////////////////////////////////////////////////////////

label K_Sex_P:  
    call Shift_Focus("Kitty")
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
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                    call Kitty_Sex_Launch("L")   
                    if K_Legs == "skirt":
                        "Kitty slides onto her back and pulls you against her, sliding her skirt up as she does so."
                        $ K_Upskirt = 1
                    elif K_Legs == "capris" or K_Legs == "black jeans":
                        "Kitty slides onto her back and pulls you against her, sliding her pants off as she does so." 
                        $ K_Upskirt = 1
                    elif K_Legs == "shorts":
                        "Kitty slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                        $ K_Upskirt = 1
                    else:
                        "Kitty slides onto her back and pulls you against her."
                    $ K_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                            "Kitty slides it in."
                        "Praise her.":       
                            call KittyFace("sexy, 1")                    
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                            ch_p "Oh yeah, [K_Pet], let's do this."
                            call Kitty_Namecheck
                            "Kitty slides it in."
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        "Ask her to stop.":
                            call KittyFace("surprised")       
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [K_Pet]."
                            call Kitty_Namecheck
                            "Kitty pulls back."
                            call KittyOutfit
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                            return            
                    jump K_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add kitty auto stuff here
                    $ Trigger2 = 0
                return   
    #End Kitty's lead
    
    if Situation == "auto":   
                call Kitty_Sex_Launch("L")   
                if K_Legs == "skirt":
                    "You press Kitty down onto her back, sliding her skirt up as you go."
                    $ K_Upskirt = 1                
                elif K_Legs == "capris" or K_Legs == "black jeans":
                    "You press Kitty down onto her back, sliding her pants down as you do."    
                    $ K_Upskirt = 1
                elif K_Legs == "shorts":
                    "You press Kitty down onto her back, sliding her shorts down as you do."                
                    $ K_Upskirt = 1
                else:
                    "You press Kitty down onto her back."
                $ K_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call KittyFace("surprised", 1)
                
                if (K_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Kitty is briefly startled, but melts into a sly smile."
                    call KittyFace("sexy")
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_k "Oh. . . game on, [K_Petname]."            
                    jump K_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ K_Brows = "angry"                
                    menu:
                        ch_k "Um, what do you think you're doing?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call KittyFace("sexy", 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                                    ch_k "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                                    jump K_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call KittyFace("bemused", 1)
                                    if K_Sex:
                                        ch_k "Maybe you could[K_like]warn me?" 
                                    else:
                                        ch_k "Maybe you could[K_like]warn me? I don't know that I'm[K_like]ready for that sort of thing. . ."                                            
                        "Just fucking.":                    
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                            "You press inside some more."                              
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            if not ApprovalCheck("Kitty", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call KittyFace("angry")
                                "Kitty shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "I am not putting up with that shit!"                                                  
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Kitty_Sex_Reset
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")                    
                            else:
                                call KittyFace("sad")
                                "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump K_SexPrep
                return   
    #End Auto
    
   
    if not K_Sex and "no sex" not in K_RecentActions:                           
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "I haven't really had much experience with this. . . "    
            if K_Forced:
                call KittyFace("sad")
                ch_k "You'd really do this when you have me over a barrel?"
            
            
    if not K_Sex and Approval:                                                  
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -30, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -20, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I don't want you to think I'm some kind of slut. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "I suppose if it's you, [K_Petname]. . ."            
            elif K_Addict >= 50:
                call KittyFace("manic", 1)
                ch_k "I have kind of been hoping you might. . ."
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I can't say it hasn't crossed my mind. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call KittyFace("sexy", 1)
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "Again? Why do you do this to me?" 
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "I guess this is more secluded. . ."        
            elif "sex" in K_RecentActions:
                ch_k "Another round? {i}Fine.{/i}"
                jump K_SexPrep
            elif "sex" in K_DailyActions:
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_k "[Line]"
            elif K_Sex < 3:        
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "So you'd like another round?"       
            else:       
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "You gonna make me purr?",
                    "You wanna slide into me?"]) 
                ch_k "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fiiiiine."  
            elif "no sex" in K_DailyActions:               
                ch_k "You've made your case. . ."
            else:
                call KittyFace("sexy", 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_k "[Line]"
                $ Line = 0
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
            jump K_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call KittyFace("angry")       
            if "no sex" in K_RecentActions:  
                ch_k "I{i}just{/i}[K_like]told you \"no!\""
            elif Taboo and "tabno" in K_DailyActions and "no sex" in K_DailyActions:  
                ch_k "I already told you. . .not in public!" 
            elif "no sex" in K_DailyActions:       
                ch_k "I already[K_like]told you \"no.\""
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you this is too public!"     
            elif not K_Sex:
                call KittyFace("bemused")
                ch_k "I don't know that I'm. . .[K_like]ready? . ."
            else:
                call KittyFace("bemused")
                ch_k "Maybe[K_like]not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in K_DailyActions:
                        call KittyFace("bemused")
                        ch_k "It's cool."
                        return
                "Maybe later?" if "no sex" not in K_DailyActions:
                        call KittyFace("sexy")  
                        ch_k "Maybe, you never know."
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
                            call KittyFace("sexy")     
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                            $ Line = renpy.random.choice(["That's. . . true. . .",     
                                "I suppose. . .", 
                                "That's. . . that's a good point. . ."]) 
                            ch_k "[Line]"
                            $ Line = 0                   
                            jump K_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Kitty", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and K_Forced):
                            call KittyFace("sad")
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                            ch_k "Well! . .  ok, fine, stick it in."  
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                            $ K_Forced = 1  
                            jump K_SexPrep
                        else:                          
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)   
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no sex" in K_DailyActions:
        ch_k "Maybe[K_like]take \"no\" for an answer?" 
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "Not even."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)     
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "I can't believe you'd even consider it around here!"      
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
    elif K_Sex:
        call KittyFace("sad") 
        ch_k "Maybe just[K_like]fuck yourself, huh?."       
    else:
        call KittyFace("normal", 1)
        ch_k "Nuhuh."     
    $ K_RecentActions.append("no sex")                      
    $ K_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label K_SexPrep:
    call Kitty_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Kitty_Bottoms_Off       
        
        
        if K_Panties or K_Legs or HoseNum("Kitty") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_k "We can't exactly do much like this, huh."
            
        if K_Panties and (K_Legs == "capris" or K_Legs == "black jeans"):
            "She quickly drops her pants and her [K_Panties]."
        elif K_Panties and K_Legs == "shorts":
            "She quickly drops her shorts and her [K_Panties]."
        elif K_Legs == "capris" or K_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif K_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Kitty") >= 5 and K_Panties:
            "She shrugs and her [K_Hose] and [K_Panties] fall to the ground."
            $ K_Hose = 0
        elif HoseNum("Kitty") >= 5:
            "She shrugs and her [K_Hose] fall to the ground."
            $ K_Hose = 0
        elif K_Panties:
            "She shrugs as her [K_Panties] fall to the ground."  
            
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless
        
        if Taboo: # Kitty gets started. . .
            if not K_Sex:
                "Kitty glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Kitty slowly presses against your rigid member."
                else:
                    "Kitty hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Kitty glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Sex:
                if "cockout" in P_RecentActions:
                    "Kitty slowly presses against your rigid member."
                else:
                    "Kitty hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Kitty leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
        if K_Legs == "pants" and K_Panties:
            "You quickly pull down her pants and her [K_Panties] and press against her slit."
        if K_Panties and K_Legs != "pants":
            "You quickly pull down her [K_Panties] and press against her slit."  
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
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
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no sex")
    $ K_RecentActions.append("sex")                      
    $ K_DailyActions.append("sex") 

label K_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Sex_Launch("sex") 
        call KittyLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ K_Upskirt = 1
        $ K_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Sex):
                    $ K_Brows = "confused"
                    ch_k "So are we[K_like]getting close here?"   
        elif Cnt == (10 + K_Sex):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_SexAfter
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump K_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Not with that attitude, mister!"
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_SexAfter
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
                            
                        "Slap her ass":                     
                                    call K_Slap_Ass                                    
                                    jump K_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress  
                        
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call K_SexAfter
                                            call K_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call K_SexAfter
                                            call K_Sex_A
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call K_SexAfter
                                            call K_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I'm[K_like]kinda tired here? Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm[K_like]kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump K_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner)
        
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Sex_Reset
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_SexAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_SexSprite"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Sex_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump K_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump K_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Sex_Reset
        
    call KittyFace("sexy") 
    
    $ K_Sex += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
    
    if "Kitty Sex Addict" in Achievements:
            pass 
            
    elif K_Sex >= 10:
        $ K_SEXP += 5
        $ Achievements.append("Kitty Sex Addict")
        if not Situation:
            call KittyFace("smile", 1)
            ch_k "I just can't seem to quit you."               
    elif K_Sex == 1:            
            $K_SEXP += 20        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "I feel like I've been waiting[K_like]a million years for that."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "I hope that was worth the wait."
    elif K_Sex == 5:
            ch_k "Why did we not do this sooner?!"  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k "Could you have maybe paid more attention? . ."
        else:
            call KittyFace("bemused")
            ch_k "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Did you[K_like]want to try something else?"
    call Checkout
    return   

# End kitty sex //////////////////////////////////////////////////////////////////////////////////


# Kitty anal //////////////////////////////////////////////////////////////////////

label K_Sex_A:
    call Shift_Focus("Kitty")
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
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            if Approval > 2:                                                      # fix, add kitty auto stuff here
                call Kitty_Sex_Launch("L")   
                if K_Legs == "skirt":
                    "Kitty slides onto her back and pulls you against her, sliding her skirt up as she does so."
                    $ K_Upskirt = 1
                elif K_Legs == "capris" or K_Legs == "black jeans":
                    "Kitty slides onto her back and pulls you against her, sliding her pants off as she does so." 
                    $ K_Upskirt = 1
                elif K_Legs == "shorts":
                    "Kitty slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                    $ K_Upskirt = 1
                else:
                    "Kitty slides onto her back and pulls you against her."
                $ K_SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                        "Kitty slides it in."
                    "Praise her.":       
                        call KittyFace("sexy, 1")                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        ch_p "Ooo, dirty girl, [K_Pet], let's do this."
                        call Kitty_Namecheck
                        "Kitty slides it in."
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised")       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck
                        "Kitty pulls back."
                        call KittyOutfit
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)                    
                        return            
                jump K_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add kitty auto stuff here
                $ Trigger2 = 0
            return  
            #end if Kitty initiates
    
    if Situation == "auto":   
            call Kitty_Sex_Launch("L")   
            if K_Legs == "skirt":
                "You press Kitty down onto her back, sliding her skirt up as you go."
                $ K_Upskirt = 1                
            elif K_Legs == "capris" or K_Legs == "black jeans":
                "You press Kitty down onto her back, sliding her pants down as you do."    
                $ K_Upskirt = 1
            elif K_Legs == "shorts":
                "You press Kitty down onto her back, sliding her shorts down as you do."                
                $ K_Upskirt = 1
            else:
                "You press Kitty down onto her back."
            $ K_SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call KittyFace("surprised", 1)
            
            if (K_Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                if K_Loose:
                    "Kitty is briefly startled, but melts into a sly smile."
                    ch_k "Hmm, stick it in. . ."            
                else:
                    "Kitty is briefly startled, but shrugs."
                    ch_k "Oookay. . ."                  
                jump K_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ K_Brows = "angry"                
                menu:
                    ch_k "Um[K_like]what are you doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call KittyFace("sexy", 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_k "Well[K_like]just take it easy, ok? . ."
                            jump K_AnalPrep
                        "You pull back before you really get it in."                    
                        call KittyFace("bemused", 1)
                        
                        if K_Anal:
                            ch_k "Maybe you could[K_like]warn me?" 
                        else:
                            ch_k "Maybe you could[K_like]warn me? I don't know that I'm[K_like]ready for that sort of thing. . ."                                           
                    "Just fucking.":                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)
                        "You press into her."                              
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        if not ApprovalCheck("Kitty", 700, "O", TabM=1):                        
                            call KittyFace("angry")
                            "Kitty shoves you away and slaps you in the face."
                            ch_k "Asshole!"
                            ch_k "You need to ask nicer than that!"                                                  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Kitty_Sex_Reset
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                        
                        else:
                            call KittyFace("sad")
                            "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump K_AnalPrep
            return  
            #end "auto" 
    
   
    if not K_Anal and "no anal" not in K_RecentActions:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "You want to go in the \"out\" door?!"
      
            if K_Forced:
                call KittyFace("sad")
                ch_k "Anal? Really?"
        
    if not K_Loose and ("dildo anal" in K_DailyActions or "anal" in K_DailyActions):
            #if she's done anal stuff today
            call KittyFace("bemused", 1)
            ch_k "I'm not really over the last time."            
    elif "anal" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Again? K."
            jump K_AnalPrep
        
    
    if not K_Anal and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I guess? . ."           
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "Well. . ."
            elif K_Addict >= 50:
                call KittyFace("manic", 1)
                ch_k "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "Anything's worth a shot. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "You really ask a lot here. . ."
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "I guess this is out of the way. . ."   
            elif "anal" in K_DailyActions and not K_Loose:
                pass      
            elif "anal" in K_RecentActions:
                ch_k "I guess I'm warmed up. . ."
                jump K_AnalPrep
            elif "anal" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_k "[Line]"    
            else:       
                call KittyFace("sexy", 1)
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I do have booty for days. . .", 
                    "You gonna make me purr?",
                    "You wanna slide into me?"]) 
                ch_k "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."   
            elif "no anal" in K_DailyActions:               
                ch_k "Well, ok, I've given it some thought, fine. . ." 
            else:
                call KittyFace("sexy", 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_k "[Line]"
                $ Line = 0
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
            jump K_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry")
            if "no anal" in K_RecentActions:  
                ch_k "I{i}just{/i}[K_like]told you \"no!\""
            elif Taboo and "tabno" in K_DailyActions and "no anal" in K_DailyActions:
                ch_k "I already told you. . .not in public!" 
            elif "no anal" in K_DailyActions:       
                ch_k "I already[K_like]told you \"no.\""
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you this is too public!"      
            elif not K_Anal:
                call KittyFace("bemused")
                ch_k "I don't know that I'm. . .[K_like]that kind of girl?"
            elif not K_Loose and "anal" not in K_DailyActions:
                call KittyFace("perplexed")
                ch_k "That was kind of. . . rough last time?"
            else:
                call KittyFace("bemused")
                ch_k "Maybe[K_like]not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "It's cool."              
                    return
                "Maybe later?" if "no anal" not in K_DailyActions:
                    call KittyFace("sexy")  
                    ch_k "Maybe, you never know."
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
                        call KittyFace("sexy")     
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["That's. . . true. . .",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump K_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad")
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                        ch_k "Well! . .  ok, fine, stick it in."  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                        $ K_Forced = 1  
                        jump K_AnalPrep
                    else:                              
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no anal" in K_DailyActions:
        ch_k "Maybe[K_like]take \"no\" for an answer?"   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "That's a bit much, even for you."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)       
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call KittyFace("angry", 1)
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "You're being ridiculous. That? Here?!"    
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3) 
    elif not K_Loose and "anal" in K_DailyActions:
        call KittyFace("bemused")
        ch_k "I'm[K_like]a little sore here?"    
    elif K_Anal:
        call KittyFace("sad") 
        ch_k "That's[K_like]totally off the table."
    else:
        call KittyFace("normal", 1)
        ch_k "Noooop."    
    $ K_RecentActions.append("no anal")                      
    $ K_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label K_AnalPrep:    
            
    call Kitty_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Kitty_Bottoms_Off        
        if K_Panties or K_Legs or HoseNum("Kitty") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_k "We can't exactly do much like this, huh."
            
        if K_Panties and (K_Legs == "capris" or K_Legs == "black jeans"):
            "She quickly drops her pants and her [K_Panties]."
        elif K_Panties and K_Legs == "shorts":
            "She quickly drops her shorts and her [K_Panties]."
        elif K_Legs == "capris" or K_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif K_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Kitty") >= 5 and K_Panties:
            "She shrugs and her [K_Hose] and [K_Panties] fall to the ground."
            $ K_Hose = 0
        elif HoseNum("Kitty") >= 5:
            "She shrugs and her [K_Hose] fall to the ground."
            $ K_Hose = 0
        elif K_Panties:
            "She shrugs as her [K_Panties] fall to the ground."  
            
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless
        
        if Taboo: # Kitty gets started. . .
            if K_Anal:                
                "Kitty glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Kitty glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Kitty slowly presses against your rigid member."
                else:
                    "Kitty hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:    
            if not K_Anal:
                "Kitty leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in P_RecentActions:
                    "Kitty slowly presses against your rigid member."
                else:
                    "Kitty hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if K_Legs == "pants" and K_Panties:
            "You quickly pull down her pants and her [K_Panties] and press against her back door."
        if K_Panties and K_Legs != "pants":
            "You quickly pull down her [K_Panties] and press against her back door."  
        $ K_Upskirt = 1
        $ K_PantiesDown = 1       
        $ K_SeenPanties = 1
        call Kitty_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
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
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no anal")
    $ K_RecentActions.append("anal")                      
    $ K_DailyActions.append("anal") 

label K_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Sex_Launch("anal") 
        call KittyLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        $ K_Upskirt = 1
        $ K_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Anal):
                    $ K_Brows = "confused"
                    if K_Loose:
                        ch_k "So are we[K_like]getting close here?"  
                    else:
                        ch_k "So are we[K_like]getting close here? This is not super pleasant. . ."   
        elif Cnt == (10 + K_Anal):
                    $ K_Brows = "angry"        
                    ch_k "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_k "Can we. . . do something. . . else?"
                        "How about a BJ?" if K_Action and MultiAction:
                                if K_Anal >= 5 and K_Blow >= 10 and K_SEXP >= 50:
                                    $ Situation = "shift"
                                    call K_AnalAfter
                                    call K_Blowjob      
                                else:
                                    ch_k "No thanks, [K_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call K_AnalAfter
                                    call RHJ_Prep   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_AnalAfter
                                call K_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump K_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_k "Not with that attitude, mister!"                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_AnalAfter
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
                            
                        "Slap her ass":                     
                                    call K_Slap_Ass                                    
                                    jump K_Anal_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0       
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress  
                        
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call K_AnalAfter
                                            call K_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call K_AnalAfter
                                            call K_Sex_P
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call K_AnalAfter
                                            call K_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I'm[K_like]kinda tired here? Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm[K_like]kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump K_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Sex_Reset
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_AnalAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_SexSprite"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Sex_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump K_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump K_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Sex_Reset
        
    call KittyFace("sexy") 
    
    $ K_Anal += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 3) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
    
    if "Kitty Anal Addict" in Achievements:
            pass 
            
    elif K_Anal >= 10:
        $ K_SEXP += 7
        $ Achievements.append("Kitty Anal Addict")
        if not Situation:
            call KittyFace("bemused", 1)
            ch_k "I didn't think I'd love this so much!"                  
    elif K_Anal == 1:            
            $K_SEXP += 25        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Anal. . . huh, who knew?"
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Ouch."
                    ch_k "I guess you got what you needed?"
    elif K_Anal == 5:
            ch_k "I'm really starting to love this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call KittyFace("bemused")
            ch_k "Ok, that was fun. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End Kitty Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Kitty hotdog //////////////////////////////////////////////////////////////////////

label K_Sex_H: 
    call Shift_Focus("Kitty")
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
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            if Approval > 2:                                                      # fix, add kitty auto stuff here
                call Kitty_Sex_Launch("L") 
                "Kitty slides onto her back and pulls you against her, rubbing it against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                        "Kitty starts to grind against you."
                    "Praise her.":       
                        call KittyFace("sexy, 1")                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
                        ch_p "Hmmm, that's good, [K_Pet]."
                        call Kitty_Namecheck
                        "Kitty starts to grind against you."
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised")       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck
                        "Kitty pulls back."
                        call KittyOutfit
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)                    
                        return            
                jump K_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add kitty auto stuff here
                $ Trigger2 = 0
            return            
            #end Kitty initates
    
    if Situation == "auto":   
            call Kitty_Sex_Launch("L")   
            "You press Kitty down onto her back and press your cock against her."    
            call KittyFace("surprised", 1)
            
            if (K_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Kitty is briefly startled, but melts into a sly smile."
                call KittyFace("sexy")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                ch_k "Hmm, I've apparently got someone's attention. . ."            
                jump K_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ K_Brows = "angry"                
                menu:
                    ch_k "Hmm, kinda rude, [K_Petname]." 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call KittyFace("sexy", 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_k "I guess it doesn't feel so bad. . ."
                            jump K_HotdogPrep
                        "You pull back from her."                    
                        call KittyFace("bemused", 1)
                        ch_k "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"                                             
                    "You'll see.":                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)
                        "You grind against her crotch."                              
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        if not ApprovalCheck("Kitty", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call KittyFace("angry")
                            "Kitty shoves you away."
                            ch_k "Jerk!"
                            ch_k "I'm not into that!"                                                  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Kitty_Sex_Reset
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                       
                        else:
                            call KittyFace("sad")
                            "Kitty doesn't seem to be into this, but she's knows her place."                        
                            jump K_HotdogPrep
            return     
            #end auto
    
   
    if not K_Hotdog and "no hotdog" not in K_RecentActions:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "So, just grinding against me?"
      
            if K_Forced:
                call KittyFace("sad")
                ch_k ". . . That's it?"
        
        
    if not K_Hotdog and Approval:                                                
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "It does look a bit swolen. . ."           
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If you want. . ."
            elif K_Addict >= 50:
                call KittyFace("manic", 1)
                ch_k "Hmmm. . ."
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "Hmm, you look ready to go. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "That's {i}all{/i} you want?"  
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "I guess this is a better location . ."   
            elif "hotdog" in K_RecentActions:
                call KittyFace("sexy", 1)
                ch_k "Again? Ok."
                jump K_HotdogPrep
            elif "hotdog" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really digging this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_k "[Line]"    
            else:       
                call KittyFace("sexy", 1)
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really digging this. . .", 
                    "You want another rub?"]) 
                ch_k "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            elif "no hotdog" in K_DailyActions:               
                ch_k "Well, I guess it's not so bad. . ."
            else:
                call KittyFace("sexy", 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_k "[Line]"
                $ Line = 0
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
            jump K_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry")
            if "no hotdog" in K_RecentActions:  
                ch_k "I{i}just{/i}[K_like]told you \"no!\""
            elif Taboo and "tabno" in K_DailyActions and "no hotdog" in K_DailyActions: 
                ch_k "I{i}just{/i}[K_like]told, not in public!" 
            elif "no hotdog" in K_DailyActions:       
                ch_k "I{i}just{/i}[K_like]told you \"no\" earlier!"
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I{i}just{/i}[K_like]told you, not in public!"  
            elif not K_Hotdog:
                call KittyFace("bemused")
                ch_k "That's kinda hot, [K_Petname]. . ."
            else:
                call KittyFace("bemused")
                ch_k "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "No problem."              
                    return
                "Maybe later?" if "no hotdog" not in K_DailyActions:
                    call KittyFace("sexy")  
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
                        call KittyFace("sexy")     
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2) 
                        $ Line = renpy.random.choice(["Well, sure, ok.",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump K_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad")
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                        ch_k "Ok, fine. Whatever."  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                        $ K_Forced = 1  
                        jump K_HotdogPrep
                    else:                              
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)     
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1      
    
    if "no hotdog" in K_DailyActions:
        ch_k "I'm just not into that."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    if K_Forced:
        call KittyFace("angry", 1)
        ch_k "Yeah, not happening."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -1) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1)  
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)        
        $ K_RecentActions.append("tabno")                      
        $ K_DailyActions.append("tabno") 
        ch_k "[K_Like]not here though?"  
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_Hotdog:
        call KittyFace("sad") 
        ch_k "Yeah, not again."
    else:
        call KittyFace("normal", 1)
        ch_k "Noooop."    
    $ K_RecentActions.append("no hotdog")                      
    $ K_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label K_HotdogPrep:  
    call Kitty_Sex_Launch("hotdog")
    
    if Situation != "auto":
#        call Kitty_Bottoms_Off    
        
        if Taboo: # Kitty gets started. . .
            if K_Hotdog:                
                "Kitty glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                
            else:         
                "Kitty glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Kitty slowly presses against your rigid member."
                else:
                    "Kitty hesitantly pulls down your pants and slowly presses against your rigid member."
            $ K_Inbt += int(Taboo/10)  
            $ K_Lust += int(Taboo/5)
        else:                
            if "cockout" in P_RecentActions:
                "Kitty slowly presses against your rigid member."
            else:
                "Kitty hesitantly pulls down your pants slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her mound."
    
    call Seen_First_Peen(1)
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
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no hotdog")
    $ K_RecentActions.append("hotdog")                      
    $ K_DailyActions.append("hotdog") 

label K_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Kitty")
        call Kitty_Sex_Launch("hotdog") 
        call KittyLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_Hotdog):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here?"   
        elif Cnt == (10 + K_Hotdog):
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "This is getting a bit dull."
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_HotdogAfter
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump K_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump K_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call KittyFace("angry", 1)   
                                    call Kitty_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_k "Not with that attitude, mister!"                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_HotdogAfter
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
                                    call K_Slap_Ass                                    
                                    jump K_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress
                                    
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call K_HotdogAfter
                                        call K_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call K_HotdogAfter
                                        call K_Sex_P
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call K_HotdogAfter
                                        call K_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call K_HotdogAfter
                                        call K_Sex_A
                                    "Never Mind":
                                        pass
                            else:
                                ch_k "I'm[K_like]kinda tired here? Could we wrap it up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm[K_like]kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump K_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_Sex_Reset
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Kitty can cum
                    if renpy.showing("Kitty_SexSprite"):                    #If you're still going at it,
                        if K_Lust >= 100:                                               
                            call K_Cumming
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump K_SexAfter
                        elif "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,                    
                            call Kitty_Sex_Launch("hotdog")
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump K_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump K_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump K_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    

    
label K_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Kitty_Sex_Reset
        
    call KittyFace("sexy") 
    
    $ K_Hotdog += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 1) 
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 1
    
    if K_Hotdog == 10:
        $ K_SEXP += 5             
    elif K_Hotdog == 1:            
            $K_SEXP += 10        
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "I. . . liked that a lot."
                elif K_Obed <= 500 and P_Focus <= 20:
                    $ K_Mouth = "sad"
                    ch_k "Well, did that work for you?"
    elif K_Hotdog == 5:
            ch_k "I'm surprised how much I enjoy this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in K_RecentActions:
            call KittyFace("angry")
            $ K_Eyes = "side"
            ch_k "I didn't get much out of that. . ."
        else:
            call KittyFace("bemused")
            ch_k "I could get into that. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Kitty hotdogging //////////////////////////////////////////////////////////////////////////////////
