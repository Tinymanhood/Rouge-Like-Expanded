# Start Emma Sex pose //////////////////////////////////////////////////////////////////////////////////
# E_Cowgirl //////////////////////////////////////////////////////////////////////

label E_Cowgirl_P:  
    call Shift_Focus("Emma")
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
                if Approval > 2:                                                      # fix, add emma auto stuff here
                    call Emma_Cowgirl_Launch("L")   
                    if E_Legs == "skirt":
                        "Emma pushes you down and climbs on top of you, sliding her skirt up as she does so."
                        $ E_Upskirt = 1
                    elif PantsNum("Emma") >= 5:
                        "Emma pushes you down and climbs on top of you, sliding her [E_Legs] off as she does so." 
                        $ E_Legs = 0
                    else:
                        "Emma pushes you down and climbs on top of you."
                    $ E_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                            "Emma slides it in."
                        "Praise her.":       
                            call EmmaFace("sexy, 1")                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            ch_p "Oh yeah, [E_Pet], let's do this."
                            call Emma_Namecheck
                            "Emma slides it in."
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        "Ask her to stop.":
                            call EmmaFace("surprised")       
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [E_Pet]."
                            call Emma_Namecheck
                            "Emma pulls back."
                            call EmmaOutfit
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                            return            
                    jump E_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add emma auto stuff here
                    $ Trigger2 = 0
                return   
    #End Emma's lead
    
    if Situation == "auto":   
                call Emma_Cowgirl_Launch("L")   
                if E_Legs == "skirt":
                    "You roll back, pulling Emma on top of you, sliding her skirt up as you go."
                    $ E_Upskirt = 1                
                elif PantsNum("Emma") >= 5:
                    "You roll back, pulling Emma on top of you, sliding her pants down as you do."    
                    $ E_Legs = 0    
                else:
                    "You roll back, pulling Emma on top of you."
                $ E_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call EmmaFace("surprised", 1)
                
                if (E_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Emma is briefly startled, but melts into a sly smile."
                    call EmmaFace("sly")
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_e "Mmm, if you insist, [E_Petname]."            
                    jump E_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ E_Brows = "angry"                
                    menu:
                        ch_e "Do you really think you can handle that?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call EmmaFace("sexy", 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                                    ch_e "I am willing to give it a try if you are. . ."
                                    jump E_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call EmmaFace("bemused", 1)
                                    if E_Sex:
                                        ch_e "Perhaps ask first, [E_Petname]." 
                                    else:
                                        ch_e "Perhaps some other time, when you ask nicely."
                        "Just fucking.":                    
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            "You press inside some more."                              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            if not ApprovalCheck("Emma", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call EmmaFace("angry")
                                "Emma shoves you away and backhands you in the face."
                                ch_e "Impertinent!"
                                ch_e "do not test my patience with you."                                                  
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Emma_Cowgirl_Launch
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")                    
                            else:
                                call EmmaFace("sad")
                                "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump E_SexPrep
                return   
    #End Auto
    
   
    if not E_Sex and "no sex" not in E_RecentActions:                           
            #first time    
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "Hmm, are you sure you're really prepared for this? . . "    
            if E_Forced:
                call EmmaFace("sad")
                ch_e "Are you sure this is how you'd like to use your. . . influence?"
            
            
    if not E_Sex and Approval:                                                  
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -30, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -20, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I wouldn't want you to get hurt. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If you insist, [E_Petname]. . ."            
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "I was wondering how it would feel with you. . ."
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I was hoping you'd ask. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call EmmaFace("sexy", 1)
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "Again? You're really wearing out your welcome." 
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I suppose this is more private."        
            elif "sex" in E_RecentActions:
                ch_e "Again? [E_Petname], you're insatiable!" 
                jump E_SexPrep
            elif "sex" in E_DailyActions:
                $ Line = renpy.random.choice(["Back again?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + E_Petname + "."]) 
                ch_e "[Line]"
            elif E_Sex < 3:        
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "Oh? Another round?"      
            else:       
                $ Line = renpy.random.choice(["Oh, you want some of this?",                 
                    "You'd like another round?",                 
                    "I suppose I am irresistible. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"]) 
                ch_e "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad")
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Oh, fine, if it will shut you up."  
            elif "no sex" in E_DailyActions:               
                ch_e "Very well, you've convinced me. . ."
            else:
                call EmmaFace("sexy", 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . fine, I accept.",                 
                    "Sure!", 
                    "We could, I suppose.",
                    "Hmmm, yes.",
                    "How could I refuse?"]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump E_SexPrep
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call EmmaFace("angry")       
            if "no sex" in E_RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions and "no sex" in E_DailyActions:  
                ch_e "I already told you. . .not in such an exposed location." 
            elif "no sex" in E_DailyActions:       
                ch_e "I believe I just told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you this is too public!"     
            elif not E_Sex:
                call EmmaFace("bemused")
                ch_e "I really doubt you understand what you're in for. . ."
            else:
                call EmmaFace("bemused")
                ch_e "Perhaps another time would be better? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in E_DailyActions:
                        call EmmaFace("bemused")
                        ch_e "I can appreciate your. . . drive."
                        return
                "Maybe later?" if "no sex" not in E_DailyActions:
                        call EmmaFace("sexy")  
                        ch_e "Oh, most certainly. . ."
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
                            call EmmaFace("sexy")     
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                            $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                            ch_e "[Line]"
                            $ Line = 0                   
                            jump E_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Emma", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and E_Forced):
                            call EmmaFace("sad")
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                            ch_e "Fine, if it'll shut you up."  
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                            $ E_Forced = 1  
                            jump E_SexPrep
                        else:                          
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)   
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no sex" in E_DailyActions:
        ch_e "Don't question me again." 
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Don't overestimate your leverage here."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "How can you imagine this would be an appropriate location?"      
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
    elif E_Sex:
        call EmmaFace("sad") 
        ch_e "I'm sure you can figure out how to take care fo that yourself."       
    else:
        call EmmaFace("normal", 1)
        ch_e "I'm afraid not."     
    $ E_RecentActions.append("no sex")                      
    $ E_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label E_SexPrep:
    call Seen_First_Peen("Emma",Partner)
    call Emma_Cowgirl_Launch("hotdog")
    
    if Situation != "auto":
        call Emma_Bottoms_Off       
        
        
        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_e "I suppose we can't do much with all this on."
            
            if (E_Panties and not E_PantiesDown) and (PantsNum("Emma") > 5 and not E_Upskirt):
                "She quickly drops her pants and her [E_Panties]."
            elif (E_Panties and not E_PantiesDown) and (E_Legs == "shorts" and not E_Upskirt):
                "She quickly drops her shorts and her [E_Panties]."
            elif PantsNum("Emma") > 5 and not E_Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif E_Legs == "shorts" and not E_Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif HoseNum("Emma") >= 5 and (E_Panties and not E_PantiesDown):
                "She tugs her [E_Hose] and [E_Panties] off."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 5:
                "She tugs her [E_Hose] off and drops them to the ground."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She tugs her [E_Panties] off and drops them to the ground."  
            
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # Emma gets started. . .
            "Emma glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Emma pushes you back and slowly presses against your rigid member."
            else:
                "Emma pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock slides in."
                            
    else:  #if Situation == "auto"         
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her slit."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her slit."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)
            
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
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no sex")
    $ E_RecentActions.append("sex")                      
    $ E_DailyActions.append("sex") 

label E_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Cowgirl_Launch("sex") 
        $ Speed = 2 if Speed >= 4 else Speed
        call EmmaLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ E_Upskirt = 1
        $ E_PantiesDown = 1  
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Sex_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call E_SexAfter
                                                                call E_Cowgirl_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_SexAfter
                                                                call E_Cowgirl_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_SexAfter
                                                                call E_Cowgirl_H
                                                        "Never Mind":
                                                                jump E_Sex_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        if Partner == "Rogue":
                                                            call Rogue_Three_Change("Emma")
                                                        elif Partner == "Kitty":
                                                            call Kitty_Three_Change("Emma")                                                  
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0          
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        if Partner == "Rogue":
                                                                call R_Undress   
                                                        elif Partner == "Kitty":
                                                                call K_Undress 
                                            "Clean up Partner":
                                                        if Partner == "Rogue" and R_Spunk:
                                                                call Rogue_Cleanup("ask")    
                                                        elif Partner == "Kitty" and K_Spunk:
                                                                call Kitty_Cleanup("ask")  
                                                        else:
                                                                "She seems fine."
                                                                jump E_Sex_Cycle 
                                            "Never mind":
                                                        jump E_Sex_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Sex_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Cowgirl_Launch
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_SexAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Cowgirl_Launch
                                    $ Line = 0
                                    jump E_SexAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Cowgirl_Launch
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_SexAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_SexAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Sex_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_SexAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_SexAfter        
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Rogue" and R_Lust >= 100:                                          
                    call R_Cumming
                elif Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Sex):
                    $ E_Brows = "confused"
                    ch_e "So are we getting close?"   
        elif Cnt == (10 + E_Sex):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . a bit. . . tired. . . here. . ."
                    menu:
                        ch_e "Could we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_SexAfter
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Cowgirl_Launch
                                $ Situation = "shift"
                                jump E_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Cowgirl_Launch
                                    "She scowls at you and pulls out."
                                    ch_e "No, I think not."
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_SexAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Cowgirl_Launch
        
    call EmmaFace("sexy") 
    
    $ E_Sex += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
        
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
            $ R_LikeEmma += 3 if R_LikeEmma >= 700 else 2    
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
            $ K_LikeEmma += 3 if K_LikeEmma >= 700 else 2
    
    if "Emma Sex Addict" in Achievements:
            pass 
            
    elif E_Sex >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not Situation:
            call EmmaFace("smile", 1)
            ch_e "I seem to fit you like a glove. . ."               
    elif E_Sex == 1:            
            $E_SEXP += 20        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I assume I rocked your entire world."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "I hope you enjoyed that."
    elif E_Sex == 5:
            ch_e "We really should have done this sooner."
            ch_e "I can't imagine why I waited so long."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "Could you have perhaps been more attentive? . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Did you[E_like]want to try something else?"
    call Checkout
    return   

# End emma sex //////////////////////////////////////////////////////////////////////////////////


# Emma anal //////////////////////////////////////////////////////////////////////

label E_Cowgirl_A:
    call Shift_Focus("Emma")
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
        
    $ Tempmod += 10  # she starts out loose    
        
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
            if Approval > 2:                                                      
                # fix, add emma auto stuff here
                call Emma_Cowgirl_Launch("L")   
                if E_Legs == "skirt":
                    "Emma pushes you down and climbs on top of you, sliding her skirt up as she does so."
                    $ E_Upskirt = 1
                elif PantsNum("Emma") >= 5:
                    "Emma pushes you down and climbs on top of you, sliding her [E_Legs] off as she does so." 
                    $ E_Legs = 0
                else:
                    "Emma pushes you down and climbs on top of you."
                $ E_SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                        "Emma slides it in."
                    "Praise her.":       
                        call EmmaFace("sexy, 1")                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        ch_p "Ooo, dirty girl, [E_Pet], let's do this."
                        call Emma_Namecheck
                        "Emma slides it in."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised")       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck
                        "Emma pulls back."
                        call EmmaOutfit
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                        return            
                jump E_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add emma auto stuff here
                $ Trigger2 = 0
            return  
            #end if Emma initiates
    
    if Situation == "auto":   
            call Emma_Cowgirl_Launch("L")   
            if E_Legs == "skirt":
                "You roll back, pulling Emma on top of you, sliding her skirt up as you go."
                $ E_Upskirt = 1                
            elif PantsNum("Emma") >= 5:
                "You roll back, pulling Emma on top of you, sliding her pants down as you do."    
                $ E_Legs = 0    
            else:
                "You roll back, pulling Emma on top of you."
            $ E_SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call EmmaFace("surprised", 1)
            
            if (E_Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                "Emma is briefly startled, but melts into a sly smile."
                ch_e "Oooh, naughty boy. . ."          
                jump E_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Oh? What exactly are you doing back there?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "Well, so long as you know what you're doing . ."
                            ch_e "I didn't say I was opposed. . ."
                            jump E_AnalPrep
                        "You pull back before you really get it in."                    
                        call EmmaFace("bemused", 1)
                        
                        if E_Anal:
                            ch_e "I do appreciate a little warning. . ." 
                        else:
                            ch_e "Perhaps we could work up to that. . ."
                    "Just fucking.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                        "You press into her."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 700, "O", TabM=1):                        
                            call EmmaFace("angry")
                            "Emma shoves you away and backhands you in the face."
                            ch_e "Impertinent!"
                            ch_e "You need to ask a lady first."                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Cowgirl_Launch
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                        
                        else:
                            call EmmaFace("sad")
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump E_AnalPrep
            return  
            #end "auto" 
    
   
    if not E_Anal and "no anal" not in E_RecentActions:                                                               
            #first time    
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "Oooh, naughty boy. Anal?"
      
            if E_Forced:
                call EmmaFace("sad")
                ch_e "Anal? That's your goto?"
        
    if "anal" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "Alright."
            jump E_AnalPrep
        
    
    if not E_Anal and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I was wondering when you'd ask. . ."           
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "I expected we'd get here at some point. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "Hmm, that would be an interesting experience. . ."
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "I was getting tired of waiting. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "You don't hold back. . ."
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I suppose this is secluded enough. . ."   
            elif "anal" in E_DailyActions and not E_Loose:
                pass      
            elif "anal" in E_RecentActions:
                ch_e "I am warmed up. . ."
                jump E_AnalPrep
            elif "anal" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out, " + E_Petname + "."]) 
                ch_e "[Line]"    
            else:       
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I knew you enjoyed it. . .", 
                    "Do you intend to make me melt?",
                    "You want me to ride you?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad")
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Oh very well."   
            elif "no anal" in E_DailyActions:               
                ch_e "After some consideration. . ."
                ch_e "It might be entertaining."
            else:
                call EmmaFace("sexy", 1)
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
            jump E_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry")
            if "no anal" in E_RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions and "no anal" in E_DailyActions:
                ch_e "I already told you. . .not in such an exposed location." 
            elif "no anal" in E_DailyActions:       
                ch_e "I believe I just told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you this is too public!"      
            elif not E_Anal:
                call EmmaFace("bemused")
                ch_e "I don't know that you're ready for that yet."
            else:
                call EmmaFace("bemused")
                ch_e "Perhaps we can work up to that."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "I don't blame you for your. . . enthusiasm."              
                    return
                "Maybe later?" if "no anal" not in E_DailyActions:
                    call EmmaFace("sexy")  
                    ch_e "I imagine we will. . ."
                    ch_e ". . . often."
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
                        call EmmaFace("sexy")     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                        ch_e "Oh, very well, get it over with."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        $ E_Forced = 1  
                        jump E_AnalPrep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no anal" in E_DailyActions:
        ch_e "Don't question me again."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "You're really shooting for the fences on that one."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)       
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "How can you imagine this would be an appropriate location?" 
        ch_e "This place, I mean, not anal."
        if ApprovalCheck("Emma", 500, "I"):
                ch_e "Anal can be nice, sometimes."
        if not Approval:
                ch_e "Maybe not with you."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3) 
    elif "anal" in E_DailyActions:
        call EmmaFace("bemused")
        ch_e "Don't wear me out here."    
    elif E_Anal:
        call EmmaFace("sad") 
        ch_e "You'll have to show me you're worth it again."
    else:
        call EmmaFace("normal", 1)
        ch_e "I don't think you've earned that yet."    
    $ E_RecentActions.append("no anal")                      
    $ E_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label E_AnalPrep:    
    call Seen_First_Peen("Emma",Partner)
    call Emma_Cowgirl_Launch("hotdog")
    
    if Situation != "auto":
        call Emma_Bottoms_Off    
        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_e "I suppose we can't do much with all this on."
            
            if (E_Panties and not E_PantiesDown) and (PantsNum("Emma") > 5 and not E_Upskirt):
                "She quickly drops her pants and her [E_Panties]."
            elif (E_Panties and not E_PantiesDown) and (E_Legs == "shorts" and not E_Upskirt):
                "She quickly drops her shorts and her [E_Panties]."
            elif PantsNum("Emma") > 5 and not E_Upskirt:
                "She tugs her pants down, exposing her bare pussy."
            elif E_Legs == "shorts" and not E_Upskirt:
                "She tugs her shorts down, exposing her bare pussy."
            elif HoseNum("Emma") >= 5 and (E_Panties and not E_PantiesDown):
                "She tugs her [E_Hose] and [E_Panties] off."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 5:
                "She tugs her [E_Hose] off and drops them to the ground."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She tugs her [E_Panties] off and drops them to the ground."  
                
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless
        
        if Taboo: # Emma gets started. . .
            "Emma glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Emma pushes you back and slowly presses against your rigid member."
            else:
                "Emma pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
        "She leans back a bit and your cock pops in."
                     
    else: #if Situation == "auto"       
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her back door."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her back door."  
        $ E_Upskirt = 1
        $ E_PantiesDown = 1       
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)
            
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
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no anal")
    $ E_RecentActions.append("anal")                      
    $ E_DailyActions.append("anal") 

label E_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Cowgirl_Launch("anal") 
        $ Speed = 2 if Speed >= 4 else Speed
        call EmmaLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        if P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Anal_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call E_AnalAfter
                                                                call E_Cowgirl_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_AnalAfter
                                                                call E_Cowgirl_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_AnalAfter
                                                                call E_Cowgirl_H
                                                        "Never Mind":
                                                                jump E_Anal_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        if Partner == "Rogue":
                                                            call Rogue_Three_Change("Emma")
                                                        elif Partner == "Kitty":
                                                            call Kitty_Three_Change("Emma")                                                  
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0          
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        if Partner == "Rogue":
                                                                call R_Undress   
                                                        elif Partner == "Kitty":
                                                                call K_Undress 
                                            "Clean up Partner":
                                                        if Partner == "Rogue" and R_Spunk:
                                                                call Rogue_Cleanup("ask")    
                                                        elif Partner == "Kitty" and K_Spunk:
                                                                call Kitty_Cleanup("ask")  
                                                        else:
                                                                "She seems fine."
                                                                jump E_Anal_Cycle 
                                            "Never mind":
                                                        jump E_Anal_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Anal_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Cowgirl_Launch
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_AnalAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Cowgirl_Launch
                                    $ Line = 0
                                    jump E_AnalAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Cowgirl_Launch
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_AnalAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_AnalAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Anal_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_AnalAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_AnalAfter        
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Rogue" and R_Lust >= 100:                                          
                    call R_Cumming
                elif Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    ch_e "So are we getting close here?"   
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"        
                    ch_e "I'm . . .getting . . a bit. . . tired. . . of this. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_AnalAfter
                                call E_Blowjob  
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_AnalAfter
                                call E_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Cowgirl_Launch
                                $ Situation = "shift"
                                jump E_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Cowgirl_Launch
                                    "She scowls at you and pulls out."
                                    ch_e "No, I think not."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_AnalAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Cowgirl_Launch
        
    call EmmaFace("sexy") 
    
    $ E_Anal += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 3) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
            $ R_LikeEmma += 3   
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
            $ K_LikeEmma += 4 if K_LikeEmma >= 800 else 3
    
    if "Emma Anal Addict" in Achievements:
            pass 
            
    elif E_Anal >= 10:
        $ E_SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not Situation:
            call EmmaFace("bemused", 1)
            ch_e "You're one of the better partners I've had at that."                  
    elif E_Anal == 1:            
            $E_SEXP += 25        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "You really took to that well."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Oooh."
                    ch_e "It's been a while."
    elif E_Anal == 5:
            ch_e "You're pretty good at that."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that than I did. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End Emma Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Emma hotdog //////////////////////////////////////////////////////////////////////

label E_Cowgirl_H: 
    call Shift_Focus("Emma")
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
            if Approval > 2:                                                      # fix, add emma auto stuff here
                call Emma_Cowgirl_Launch("L") 
                "Emma pushes you down and climbs on top of you, rubbing it against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                        "Emma starts to grind against you."
                    "Praise her.":       
                        call EmmaFace("sexy, 1")                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
                        ch_p "Hmmm, that's good, [E_Pet]."
                        call Emma_Namecheck
                        "Emma starts to grind against you."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised")       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck
                        "Emma pulls back."
                        call EmmaOutfit
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)                    
                        return            
                jump E_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add emma auto stuff here
                $ Trigger2 = 0
            return            
            #end Emma initates
    
    if Situation == "auto":   
            call Emma_Cowgirl_Launch("L")   
            "You roll back, pulling Emma on top of you, and press your cock against her."    
            call EmmaFace("surprised", 1)
            
            if (E_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Emma is briefly startled, but melts into a sly smile."
                call EmmaFace("sly")
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                ch_e "Now what shall we do with that . ."            
                jump E_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "You might want to take a step back, [E_Petname]?" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "Or not. . ."
                            jump E_HotdogPrep
                        "You pull back from her."                    
                        call EmmaFace("bemused", 1)
                        ch_e "You might get better results if you asked first?"                                             
                    "You'll see.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)
                        "You grind against her crotch."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call EmmaFace("angry")
                            "Emma shoves you away."
                            ch_e "Don't push your luck, [E_Petname]."                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Cowgirl_Launch
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                       
                        else:
                            call EmmaFace("sad")
                            "Emma doesn't seem to be into this, but she knows her place."                        
                            jump E_HotdogPrep
            return     
            #end auto
    
   
    if not E_Hotdog and "no hotdog" not in E_RecentActions:                                                               
            #first time    
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "You just want me to grind against you then?"
      
            if E_Forced:
                call EmmaFace("sad")
                ch_e ". . . nothing more than that?"
        
        
    if not E_Hotdog and Approval:                                                
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I wouldn't want to leave you. . . unattended. . ."           
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If that's what works for you. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "Hrmm. . ."
            else: # Uninhibited 
                call EmmaFace("sad")
                $ E_Mouth = "smile"             
                ch_e "Well if that's what gets you off. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "Maybe that's going a bit too far. . ."  
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "I suppose this is a better location . ."   
            elif "hotdog" in E_RecentActions:
                call EmmaFace("sexy", 1)
                ch_e "Again? Oh, very well."
                jump E_HotdogPrep
            elif "hotdog" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really into this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_e "[Line]"    
            else:       
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really into this. . .", 
                    "You want another rub?"]) 
                ch_e "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad")
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."    
            elif "no hotdog" in E_DailyActions:               
                ch_e "It was rather entertaining. . ."
            else:
                call EmmaFace("sexy", 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, let me give it a rub.",                 
                    "Very well.",                 
                    "Nice!", 
                    "I suppose we could do that.",
                    "Allow me. . .",
                    "Heh, ok, ok."]) 
                ch_e "[Line]"
                $ Line = 0
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
            jump E_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry")
            if "no hotdog" in E_RecentActions:  
                ch_e "I'm afraid that \"no\" is my final answer, [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions and "no hotdog" in E_DailyActions: 
                ch_e "I just told you. . .not in such an exposed location." 
            elif "no hotdog" in E_DailyActions:       
                ch_e "I'm believe I just told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you. . .not in such an exposed location." 
            elif not E_Hotdog:
                call EmmaFace("bemused")
                ch_e "Hmm, that could be amusing, [E_Petname]. . ."
            else:
                call EmmaFace("bemused")
                ch_e "I don't think that would be appropriate. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "No harm in asking. Once."              
                    return
                "Maybe later?" if "no hotdog" not in E_DailyActions:
                    call EmmaFace("sexy")  
                    ch_e "I imagine it will happen at some point, [E_Petname]."
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
                        call EmmaFace("sexy")     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                        $ Line = renpy.random.choice(["I can't exactly argue with that. . .",     
                                "I suppose. . .", 
                                "You raise a good point. . ."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump E_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                        ch_e "Alright, fine. Lay back."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                        $ E_Forced = 1  
                        jump E_HotdogPrep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)     
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1      
    
    if "no hotdog" in E_DailyActions:
        ch_e "I've made myself clear."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    if E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I just don't see the benefit."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -1) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1)  
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)        
        $ E_RecentActions.append("tabno")                      
        $ E_DailyActions.append("tabno") 
        ch_e "This area is a bit too exposed for that sort of thing. . ."  
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif E_Hotdog:
        call EmmaFace("sad") 
        ch_e "Not under the circumstances."
    else:
        call EmmaFace("normal", 1)
        ch_e "No, thank you."    
    $ E_RecentActions.append("no hotdog")                      
    $ E_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label E_HotdogPrep:  
    call Seen_First_Peen("Emma",Partner)
    call Emma_Cowgirl_Launch("hotdog")
    
    if Situation != "auto":
#        call Emma_Bottoms_Off    
        
        if Taboo: # Emma gets started. . .
            "Emma glances around to see if anyone notices what she's doing."
            if "cockout" in P_RecentActions:
                "Then she pushes you back and slowly presses against your rigid member."
            else:
                "Then she pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
            $ E_Inbt += int(Taboo/10)  
            $ E_Lust += int(Taboo/5)
        else:    
            if "cockout" in P_RecentActions:
                "Emma pushes you back and slowly presses against your rigid member."
            else:
                "Emma pulls down your pants and climbs on top of you."
                "She slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You roll back, pulling her on top of you and your rigid member."
    
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
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no hotdog")
    $ E_RecentActions.append("hotdog")                      
    $ E_DailyActions.append("hotdog") 

label E_Hotdog_Cycle: #Repeating strokes 
    while Round >=0:  
        call Shift_Focus("Emma")
        call Emma_Cowgirl_Launch("hotdog") 
        $ Speed = 2 if Speed >= 4 else Speed
        call EmmaLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass
                                    
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1                            
                        "Speed up. . ." if 0 < Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    call E_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump E_Hotdog_Cycle  
                                    
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                                
                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call E_HotdogAfter
                                                            call E_Cowgirl_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_HotdogAfter
                                                            call E_Cowgirl_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call E_HotdogAfter
                                                            call E_Cowgirl_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_HotdogAfter
                                                            call E_Cowgirl_A
                                                        "Never Mind":
                                                                jump E_Hotdog_Cycle
                                            else:
                                                ch_e "I'm getting a bit tired here, could we take a break?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        if Partner == "Rogue":
                                                            call Rogue_Three_Change("Emma")
                                                        elif Partner == "Kitty":
                                                            call Kitty_Three_Change("Emma")                                                  
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0          
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        if Partner == "Rogue":
                                                                call R_Undress   
                                                        elif Partner == "Kitty":
                                                                call K_Undress 
                                            "Clean up Partner":
                                                        if Partner == "Rogue" and R_Spunk:
                                                                call Rogue_Cleanup("ask")    
                                                        elif Partner == "Kitty" and K_Spunk:
                                                                call Kitty_Cleanup("ask")  
                                                        else:
                                                                "She seems fine."
                                                                jump E_Hotdog_Cycle 
                                            "Never mind":
                                                        jump E_Hotdog_Cycle 
                                    "Undress Emma":
                                            call E_Undress   
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass  
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")                                         
                                    "Never mind":
                                            jump E_Hotdog_Cycle                                    
                                                        
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Emma_Cowgirl_Launch
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_HotdogAfter
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Emma_Cowgirl_Launch
                                    $ Line = 0
                                    jump E_HotdogAfter
        #End menu (if Line)              
        
        call Shift_Focus("Emma")    
        call Sex_Dialog("Emma",Partner)
        
        $ Cnt += 1
        $ Round -= 1     
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If either of you could cum    
                    if P_Focus >= 100:
                            #If you can cum:                                                
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_Cowgirl_Launch
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                    $ E_RecentActions.append("unsatisfied")                      
                                    $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_HotdogAfter 
                            $ Line = "came"

                    if E_Lust >= 100:         
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_HotdogAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,  
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                    "She is breathing heavily as your cock rubs inside her.", 
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it" 
                                        jump E_Hotdog_Cycle  
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_HotdogAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_HotdogAfter        
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Rogue" and R_Lust >= 100:                                          
                    call R_Cumming
                elif Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
        #End orgasm
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Hotdog):
                    $ E_Brows = "confused"
                    ch_e "Are we getting close here?"   
        elif Cnt == (10 + E_Hotdog):
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "I'm a bit bored by this."
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_HotdogAfter
                                call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Cowgirl_Launch
                                $ Situation = "shift"
                                jump E_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call Emma_Cowgirl_Launch
                                    "She scowls at you and pulls away."
                                    ch_e "No, I think not."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_HotdogAfter
        #End Count check
   
        if Round == 10:
            ch_e "You might want to think about your endgame here. . ."  
        elif Round == 5:
            ch_e "We'll need a break soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
label E_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Cowgirl_Launch
        
    call EmmaFace("sexy") 
    
    $ E_Hotdog += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
            $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1    
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
            $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
    
    if E_Hotdog == 10:
        $ E_SEXP += 5             
    elif E_Hotdog == 1:            
            $E_SEXP += 10        
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was. . . pleasant."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Was that enough for you?" 
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "I'm afraid that didn't do much for me. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Emma hotdogging //////////////////////////////////////////////////////////////////////////////////
