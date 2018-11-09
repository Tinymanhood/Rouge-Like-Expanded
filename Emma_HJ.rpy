## E_Handjob //////////////////////////////////////////////////////////////////////
label E_Handjob:
    call Shift_Focus("Emma") from _call_Shift_Focus_4
    if E_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif E_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Hand: #You've done it before
        $ Tempmod += 3
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if E_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no hand" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            if Trigger2 == "jackin":
                "Emma brushes your hand aside and starts stroking your cock."
            else:
                "Emma gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)                     
                    "Emma continues her actions."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck
                    "Emma continues her actions."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised") from _call_EmmaFace_1       
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_1
                    "Emma puts it down."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump EHJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Hand and "no hand" not in E_RecentActions:        
        call EmmaFace("confused", 2) from _call_EmmaFace_2
        ch_e "So you want a handy then?"
        $ E_Blush = 1
            
    if not E_Hand and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad",1) from _call_EmmaFace_3
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy",1) from _call_EmmaFace_4
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I guess it could be interesting. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal",1) from _call_EmmaFace_5
            ch_e "If you want, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_6
            ch_e "I kind of {i}need{/i} to. . ."  
        else: # Uninhibited 
            call EmmaFace("lipbite",1) from _call_EmmaFace_7    
            ch_e "I guess. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_8
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's it, right?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Well, I guess if it's here. . ."    
        elif "hand" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_9
            ch_e "You're giving me carpal tunnel. . ."
            jump EHJ_Prep
        elif "hand" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_10
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."]) 
            ch_e "[Line]"
        elif E_Hand < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_11
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "Hmm, magic fingers. . ."        
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_12
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_13
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine." 
        elif "no hand" in E_DailyActions:               
            ch_e "OK, geeze!"   
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_14
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump EHJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_15
        if "no hand" in E_RecentActions:  
            ch_e "You don't listen do you, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no hand" in E_DailyActions: 
            ch_e "I said not in public!"  
        elif "no hand" in E_DailyActions:       
            ch_e "I told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I said not in public!"     
        elif not E_Hand:
            call EmmaFace("bemused") from _call_EmmaFace_16
            ch_e "I don't know, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_17
            ch_e "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_18
                ch_e "Yeah."              
                return
            "Maybe later?" if "no hand" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_19  
                ch_e ". . ."
                ch_e "Maybe."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no hand")                      
                $ E_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_20     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump EHJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_21
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, fine."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1  
                    jump EHJ_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1 
    if "no hand" in E_DailyActions:
        call EmmaFace("angry", 1) from _call_EmmaFace_22
        ch_e "I'm not telling you again."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_23
        ch_e "Not even if you had a ten foot pole."
        call EmmaFace("surprised", 2) from _call_EmmaFace_24
        ch_e "I mean. . ."
        call EmmaFace("angry", 1) from _call_EmmaFace_25        
        ch_e "You know what I mean!"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_26          
        $ E_DailyActions.append("tabno") 
        ch_e "Not here, not anywhere near here."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)   
    elif E_Hand:
        call EmmaFace("sad") from _call_EmmaFace_27 
        ch_e "I'm not feeling it today. . ."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_28
        ch_e "I don't wanna touch that."  
    $ E_RecentActions.append("no hand")                      
    $ E_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label EHJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy") from _call_EmmaFace_29
    if E_Forced:
        call EmmaFace("sad") from _call_EmmaFace_30
    elif E_Hand:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
    
    call Emma_HJ_Launch("L") from _call_Emma_HJ_Launch
    if not E_Hand:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_6
    call DrainWord("Emma","no hand") from _call_DrainWord_7
    $ E_RecentActions.append("hand")                      
    $ E_DailyActions.append("hand") 
  
label EHJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Emma") from _call_Shift_Focus_5
        call Emma_HJ_Launch from _call_Emma_HJ_Launch_1    
        call EmmaLust from _call_EmmaLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "Ouch, hand cramp, can we take a break?"
                        #"How about a BJ?" if E_Action and MultiAction:
                        #        $ Situation = "shift"
                        #        call E_HJAfter
                        #        call E_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump EHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_HJ_Reset from _call_Emma_HJ_Reset
                                $ Situation = "shift"
                                jump E_HJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_31   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "Hey, I've got better things to do if you're going to be a dick about it."                                               
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)                     
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_HJAfter
        elif Cnt == 10 and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Can we be done with this now? I'm getting sore."         
        #End Count check
        
        if not Speed:
            $ Speed = 1 

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
                                    if Trigger2 == "jackin":
                                        "You ask her to up the pace a bit, and move your own hand out of the way."
                                    else:
                                        "You ask her to up the pace a bit."
                                    
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                   
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if E_Action and MultiAction:
                                                $ Situation = "shift"
                                                call E_HJAfter from _call_E_HJAfter                
                                                call E_Blowjob from _call_E_Blowjob
                                            else:
                                                ch_e "Actually I'm getting a bit worn out, let's finish up here. . ."
                                       
                        "I also want to fondle her breasts." if E_Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    $ Situation = "auto"
                                    call E_Fondle_Breasts from _call_E_Fondle_Breasts
                                    if Trigger2:
                                         $ E_Action -= 1
                                         
                        "Let's try something else." if MultiAction: 
                                    call Emma_HJ_Reset from _call_Emma_HJ_Reset_1
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_HJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_HJ_Reset from _call_Emma_HJ_Reset_2
                                    $ Line = 0
                                    jump E_HJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming
                            if "angry" in E_RecentActions:  
                                call Emma_HJ_Reset from _call_Emma_HJ_Reset_3
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_HJAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                                                
                            call E_Cumming from _call_E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_HJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump E_HJAfter   
        #End orgasm
        
        if Round == 10:
            ch_e "It's kind of time to get moving."   
        elif Round == 5:
            ch_e "For real time's up."      
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_32
    $ Line = 0
    ch_e "Ok, we need to take a break."
    
label E_HJAfter:
    call EmmaFace("sexy") from _call_EmmaFace_33 
    
    $ E_Hand += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5)
    
    if E_Loc == bg_current and "noticed rogue" in E_RecentActions: #If Emma was participating
        $ R_LikeEmma += 1
    
    if "Emma Handi-Queen" in Achievements:
            pass  
    elif E_Hand >= 10:
            call EmmaFace("smile", 1) from _call_EmmaFace_34
            ch_e "I've kinda become a \"Handi-Queen\" or something."
            $ Achievements.append("Emma Handi-Queen")
            $E_SEXP += 5          
    elif E_Hand == 1:            
            $E_SEXP += 10
            if E_Love >= 500:
                $ E_Mouth = "smile"
                ch_e "It was so warm to the touch. . ."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "Did that work out for you?"
    elif E_Hand == 5:
                ch_e "Let me know any time you need me to give you a hand."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Ok, so what were you thinking?"
    else:
        call Emma_HJ_Reset from _call_Emma_HJ_Reset_4    
    call Checkout from _call_Checkout_6
    return

## end E_Handjob //////////////////////////////////////////////////////////////////////


# E_Blowjob //////////////////////////////////////////////////////////////////////

label E_Blowjob:
    call Shift_Focus("Emma") from _call_Shift_Focus_6
    if E_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif E_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif E_Blow: #You've done it before
        $ Tempmod += 7    
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif E_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no blow" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in E_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            "Emma slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)                     
                    "Emma continues licking at it."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_35                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    ch_p "Hmmm, keep doing that, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_2
                    "Emma continues her actions."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":     
                    call EmmaFace("surprised") from _call_EmmaFace_36  
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_3
                    "Emma puts it down."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                    return            
            jump EBJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Blow and "no blow" not in E_RecentActions:        
        call EmmaFace("surprised", 2) from _call_EmmaFace_37
        $ E_Mouth = "kiss"
        ch_e "You want me to suck your dick?"
        if E_Hand:          
            $ E_Mouth = "smile"
            ch_e "Not satisfied with handies?"        
        $ E_Blush = 1
            
    if not E_Blow and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_38
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_39
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I have wondered what you. . . taste like."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_40
            ch_e "If you want me to. . ."               
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_41
            ch_e "My mouth is watering. . ."   
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_42
            $ E_Mouth = "smile"             
            ch_e " sure. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_43
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "You want me to do that again?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Ok, I guess this is private enough. . ."    
        elif "blow" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_44
            ch_e "Mmm, again? [[stretches her jaw]"
            jump EBJ_Prep                
        elif "blow" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_45
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_e "[Line]"
        elif E_Blow < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_46
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another blowjob?"        
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_47
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you wanna 'nother blowjob?",                 
                "A little. . . lick?", 
                "You want me to suck you off?",
                "A little tlc?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_48
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Whatever."    
        elif "no blow" in E_DailyActions:               
            ch_e "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."  
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_49
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Lol, ok, alright."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 1)      
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
        jump EBJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_50
        if "no blow" in E_RecentActions:  
            ch_e "What did I {i}just{/i} tell you [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no blow" in E_DailyActions:  
            ch_e "I told you, not in public!"  
        elif "no blow" in E_DailyActions:       
            ch_e "I told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I told you this is too public!"      
        elif not E_Blow:
            call EmmaFace("bemused") from _call_EmmaFace_51
            ch_e "I don't know about the taste, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_52
            ch_e "Later, [E_Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_53
                ch_e "Aw, it's ok, [E_Petname]."              
                return
            "Maybe later?" if "no blow" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_54  
                ch_e "You never know, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no blow")                      
                $ E_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_55     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, I guess.",                 
                        "Well. . . ok.",                 
                        "I could maybe give it a try.", 
                        "I guess I could. . .",
                        "Fiiine. . . [She licks her lips].",
                        "Heh, ok, fine."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump EBJ_Prep
                else:   
                    if ApprovalCheck("Emma", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                        call EmmaFace("confused", 1) from _call_EmmaFace_56
                        #$ E_Arms = 1
                        if E_Hand:
                            ch_e "Maybe I could just use my hand?"
                        else:
                            ch_e "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_e "Would that work?"
                            "Sure, that's fine.":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)  
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)                                
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1) 
                                jump EHJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                                
                                $ E_Arms = 0                
                                ch_e "Ok, your loss."  
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)  
                    
                    
            "Suck it, [E_Pet]":                                               # Pressured into it                
                call Emma_Namecheck from _call_Emma_Namecheck_4
                $ Approval = ApprovalCheck("Emma", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_57
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, fine. . ."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1
                    jump EBJ_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in E_DailyActions:
        call EmmaFace("angry", 1) from _call_EmmaFace_58
        ch_e "You can eat a dick, 'cos I'm not."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_59
        ch_e "I just can't do that!"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)     
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
        $ E_RecentActions.append("no blow")                      
        $ E_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_60          
        $ E_DailyActions.append("tabno") 
        ch_e "This is way too exposed!"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)    
        return                
    elif E_Blow:
        call EmmaFace("sad") from _call_EmmaFace_61 
        ch_e "No, not this time."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_62
        ch_e "Nope."  
    $ E_RecentActions.append("no blow")                      
    $ E_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label EBJ_Prep:   
    if renpy.showing("Emma_HJ_Animation"):
        hide Emma_HJ_Animation with easeoutbottom
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy") from _call_EmmaFace_63
    if E_Forced:
        call EmmaFace("sad") from _call_EmmaFace_64
    elif E_Hand:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
    
    call Emma_BJ_Launch("L") from _call_Emma_BJ_Launch
    if not E_Blow:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -70)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 45)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 60) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 35)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 40)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_1
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_8
    call DrainWord("Emma","no blow") from _call_DrainWord_9
    $ E_RecentActions.append("blow")                      
    $ E_DailyActions.append("blow")     

label EBJ_Cycle: #Repeating strokes  
    while Round >=0:
        call Shift_Focus("Emma") from _call_Shift_Focus_7
        call Emma_BJ_Launch from _call_Emma_BJ_Launch_1    
        call EmmaLust from _call_EmmaLust_1   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
         
        if Cnt == (10 + E_Blow):
                $ E_Brows = "angry"        
                menu:
                    ch_e "I'm totally worn out here. Can we do something else?"
                    "How about a Handy?" if E_Action and MultiAction:
                            $ Situation = "shift"
                            call E_BJAfter from _call_E_BJAfter
                            call E_Handjob from _call_E_Handjob 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump EBJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Emma_BJ_Reset from _call_Emma_BJ_Reset
                            $ Situation = "shift"
                            jump E_BJAfter
                    "No, get back down there.":
                            if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call EmmaFace("angry", 1) from _call_EmmaFace_65  
                                "She scowls at you, drops you cock and pulls back."
                                ch_e "Well fuck you then."
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")   
                                jump E_BJAfter        
        elif Cnt == (5 + E_Blow) and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here? I'm cramping up."  
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                pass
                            
                        "Lick it. . ." if Speed != 1:
                                $ Speed = 1   
                        "Lick it. . . (locked)" if Speed == 1:
                                pass  
                            
                        #"Just the head. . ." if Speed != 2:
                        #    $ Speed = 2
                        #"Just the head. . . (locked)" if Speed == 2:
                        #        pass
                            
                        "Suck on it." if Speed != 3:
                                $ Speed = 3  
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."
                                    
                        "Suck on it. (locked)" if Speed == 3:
                                pass
                            
                        "Take it deeper." if Speed != 4:
                                if "pushed" not in E_RecentActions and E_Blow < 5:
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -(20-(2*E_Blow))) 
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, (30-(3*E_Blow)))
                                    $ E_RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Emma hums contentedly."    
                                if "setpace" not in E_RecentActions:
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if E_Blow < 5:
                                    $ D20 -= 10
                                elif E_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in E_RecentActions:      
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                #elif D20 > 5:
                                #    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ E_RecentActions.append("setpace")

                        "Hold her head" if not P_Hands:
                                $ P_Hands = 1
                                "You hold her head"

                        "No hands" if P_Hands:
                                $ P_Hands = 0
                                "You let go of her head"
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_1  
                                    
                        "Shift actions":
                            menu:
                                "How about a handy?":
                                        if E_Action and MultiAction:
                                            if  E_Over == "armbinder":
                                                call EmmaFace("sexy", 1) from _call_EmmaFace_66
                                                ch_e "I can't do that with my arms like this [E_Petname]"
                                                "You untie her arms and removes her blindfold"
                                                $ E_Over = 0
                                                $ E_Blindfold = 0
                                                if E_Chest or E_Pants or E_Panties:
                                                    "She drops the rest of her clothes"
                                                    $ E_Chest = 0
                                                    $ E_Pants = 0
                                                    $ E_Panties = 0
                                                    $ E_Outfit = "nude"
                                            $ Situation = "shift"
                                            call E_BJAfter from _call_E_BJAfter_1
                                            call E_Handjob from _call_E_Handjob_1
                                        else:
                                            ch_e "I'm kinda tired, could we just wrap this up. . ."
                        
                                        
                        "I also want to fondle her breasts.":
                                if E_Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    "You start to fondle her breasts."
                                    $ E_Action -= 1
                                else:
                                    ch_e "I'm kinda tired, could we just wrap this up?"  
                                         
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_BJ_Reset from _call_Emma_BJ_Reset_1
                                $ Situation = "shift"
                                jump E_BJAfter
                        "Let's stop for now." if not MultiAction: 
                                $ Line = 0
                                call Emma_BJ_Reset from _call_Emma_BJ_Reset_2
                                jump E_BJAfter 
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_1
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_1
                            if "angry" in E_RecentActions:  
                                call Emma_BJ_Reset from _call_Emma_BJ_Reset_3
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_BJAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                                                
                            call E_Cumming from _call_E_Cumming_1
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_BJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump E_BJAfter   
                
        #End orgasm
        
   
        if Round == 10:
            ch_e "Could we wrap this up?"  
        elif Round == 5:
            ch_e "Seriously, I need a break."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_67
    $ Line = 0
    ch_e "Ok, I gotta rest me jaw for a minute. . ."

label E_BJAfter:    
    call EmmaFace("sexy") from _call_EmmaFace_68  
        
    $ E_Blow += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
                
    if R_Loc == bg_current and "noticed Emma" in R_RecentActions:
            $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
            
    if "Emma Jobber" in Achievements:
        pass
    elif E_Blow >= 10:
        call EmmaFace("smile", 1) from _call_EmmaFace_69
        ch_e "I can't get your taste out of my mind."      
        $ Achievements.append("Emma Jobber")
        $E_SEXP += 5
    elif Situation == "shift":
        pass
    elif E_Blow == 1:
            $E_SEXP += 15
            if E_Love >= 500:
                $ E_Mouth = "smile"
                ch_e "Huh, that wasn't bad."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "I hope you enjoyed that."     
    elif E_Blow == 5:
        ch_e "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                call EmmaFace("smile", 1) from _call_EmmaFace_70
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Emma", 500, "O"):
                    call EmmaFace("sad", 2) from _call_EmmaFace_71
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                else:
                    call EmmaFace("angry", 2) from _call_EmmaFace_72
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -25)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                ch_e ". . ."         
                call EmmaFace("sad", 1) from _call_EmmaFace_73
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Emma_BJ_Reset from _call_Emma_BJ_Reset_4    
    call Checkout from _call_Checkout_7
    return
    


# end E_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

## E_Titjob //////////////////////////////////////////////////////////////////////              Not finished
label E_Titjob:
    #return #fix remove when this works
    
    call Shift_Focus("Emma") from _call_Shift_Focus_8
    if E_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif E_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Tit: #You've done it before
        $ Tempmod += 5
    
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif E_Addict >= 75:
        $ Tempmod += 5
        
    if E_SeenChest and ApprovalCheck("Emma", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not E_Chest and not E_Over: #She's already topless
        $ Tempmod += 10
    if E_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 30 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount    
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            call Emma_TJ_Launch("L") from _call_Emma_TJ_Launch            
            "Emma slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)                     
                    "Emma starts to slide them up and down."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_74                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_5
                    "Emma continues her actions."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":     
                    call EmmaFace("confused") from _call_EmmaFace_75  
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_6
                    "Emma lets it drop out from between her breasts."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                    call Emma_TJ_Reset from _call_Emma_TJ_Reset  
                    return            
            jump ETJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Tit and "no titjob" not in E_RecentActions:        
        call EmmaFace("surprised", 1) from _call_EmmaFace_76
        $ E_Mouth = "kiss"
        ch_e "You want me to rub your cock with my breasts?"        
        if E_Blow:          
            $ E_Mouth = "smile"
            ch_e "My mouth wasn't enough?"
        elif E_Hand:          
            $ E_Mouth = "smile"
            ch_e "My hand wasn't enough?"
            
    if not E_Tit and Approval:                                                 #First time dialog    
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_77
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy") from _call_EmmaFace_78
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "Huh, well that's certainly one way to get off."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal") from _call_EmmaFace_79
            ch_e "If that's what you want. . ."              
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_80
            ch_e "Hmmmm. . . ."     
        else: # Uninhibited 
            call EmmaFace("sad") from _call_EmmaFace_81
            $ E_Mouth = "smile"             
            ch_e "Heh, might be fun."      
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_82
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Ok, I guess this is private enough. . ."   
        elif "titjob" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_83
            ch_e "Mmm, again? Ok, let me get the girls ready."
            jump ETJ_Prep
        elif "titjob" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_84
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."]) 
            ch_e "[Line]"
        elif E_Tit < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_85
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "So you'd like another titjob?"        
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_86
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",                 
                "So you'd like another titjob?",                 
                "A little. . . bounce?", 
                "You want me to pillow your crank?",
                "A little soft embrace?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_87
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Well, there are worst ways to get you off. . ." 
        elif "no titjob" in E_DailyActions:               
            ch_e "Hmm, I suppose. . ."       
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_88
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 1)      
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
        jump ETJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_89
        if "no titjob" in E_RecentActions:  
            ch_e "I {i}just{/i} told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no titjob" in E_DailyActions:  
            ch_e "This is just way too exposed!"     
        elif "no titjob" in E_DailyActions:       
            ch_e "I already told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "This is just way too exposed!"     
        elif not E_Tit:
            call EmmaFace("bemused") from _call_EmmaFace_90
            ch_e "I'm not really up for that, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_91
            ch_e "Not, right now [E_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_92
                ch_e "Yeah, ok, [E_Petname]."              
                return
            "Maybe later?" if "no titjob" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_93  
                ch_e "We'll have to see."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no titjob")                      
                $ E_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_94     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok, alright."])
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump ETJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Emma", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                        call EmmaFace("confused", 1) from _call_EmmaFace_95
                        if E_Blow:
                            ch_e "I could just. . . blow you instead?"
                        else:
                            ch_e "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        menu:
                            ch_e "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)  
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)                                
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1) 
                                jump EBJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval:       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                        call EmmaFace("confused", 1) from _call_EmmaFace_96
                        if E_Hand:
                            ch_e "Maybe you'd settle for a handy?"
                        else:
                            ch_e "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_e "What do you say?"
                            "Sure, that's fine.":
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)  
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)                                
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1) 
                                jump EHJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, whatever."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [E_Pet]":                                               # Pressured into it                
                call Emma_Namecheck from _call_Emma_Namecheck_7
                $ Approval = ApprovalCheck("Emma", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_97
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, fine, whip it out."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1
                    jump ETJ_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in E_DailyActions:
        call EmmaFace("angry", 1) from _call_EmmaFace_98
        ch_e "Look, I already told you no thanks, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_99
        ch_e "I'm not that kind of girl."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)      
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_100          
        $ E_DailyActions.append("tabno") 
        ch_e "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif E_Blow:
        call EmmaFace("sad") from _call_EmmaFace_101 
        ch_e "I think I'll let you know when I want you touching these again."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_102
        ch_e "How about let's not, [E_Petname]."
    $ E_RecentActions.append("no titjob")                      
    $ E_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label ETJ_Prep:
      
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)

        
    call EmmaFace("sexy") from _call_EmmaFace_103
    if E_Forced:
        call EmmaFace("sad") from _call_EmmaFace_104
    elif E_Tit:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
        
    call Emma_TJ_Launch("L") from _call_Emma_TJ_Launch_1    
    if not E_Tit:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -25)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 30)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30)   
    
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_2
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_10
    call DrainWord("Emma","no titjob") from _call_DrainWord_11
    $ E_RecentActions.append("titjob")                      
    $ E_DailyActions.append("titjob") 

label ETJ_Cycle: #Repeating strokes  
    call Shift_Focus("Emma") from _call_Shift_Focus_9  
    call Emma_TJ_Launch from _call_Emma_TJ_Launch_2
        
    call EmmaLust from _call_EmmaLust_2            
    if P_FocusX and P_Focus > 50:
        $ P_Focus -= 10  
        
    if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
    elif Cnt == (5 + E_Tit):
        $ E_Brows = "confused"
        ch_e "Are you getting close here? I'm getting as little sore."        
    if Cnt == (10 + E_Tit):
        $ E_Brows = "angry"        
        menu:
            ch_e "I'm getting rug-burn here [E_Petname]. Can we do something else?"
            "How about a BJ?" if E_Action and MultiAction:
                $ Situation = "shift"
                call E_TJAfter from _call_E_TJAfter
                call E_Blowjob from _call_E_Blowjob_1 
                return
            "Finish up." if P_FocusX:
                "You release your concentration. . ."             
                $ P_FocusX = 0
                $ P_Focus += 15
                $ Cnt += 1
                "[Line]."
                jump ETJ_Cycle                
            "Let's try something else." if MultiAction: 
                $ Line = 0
                call Emma_TJ_Reset from _call_Emma_TJ_Reset_1
                $ Situation = "shift"
                jump E_TJAfter
            "No, get back down there.":
                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                    "She grumbles but gets back to work."
                else:
                    call EmmaFace("angry", 1) from _call_EmmaFace_105   
                    "She scowls at you, drops you cock and pulls back."
                    ch_e "Well if that's your attitude you can handle your own business."                         
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    jump E_TJAfter
                
        
    if Line and P_Focus < 100:
        $ Cnt += 1
        $ Round -= 1
        menu:
            "[Line]."
            "Get moving. . ." if not Speed:
                $ Speed = 1
            "Keep going. . ." if Speed:
                pass
            "Speed up. . ." if Speed < 2:                    
                $ Speed = 2
                "You ask her to up the pace a bit."
            "Speed up. . . (locked)" if Speed >= 2:
                pass
            "Slow Down. . ." if Speed > 1:                    
                $ Speed = 1
                "You ask her to slow it down a bit."
            "Slow Down. . . (locked)" if Speed <= 1:
                pass

            # "Blindfold her" if E_Bondage and not E_Blindfold:
            #     call EmmaFace("sexy", 1) 
            #     "You add a blindfold so she can't see a thing"
            #     $ E_Blindfold = 1

            # "Remove blindfold" if E_Blindfold:
            #     call EmmaFace("sexy", 1) 
            #     "You remove the blindfold"
            #     $ E_Blindfold = 0

            "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                pass
            "Focus to last longer." if "focus" in P_Traits and not P_FocusX:
                "You concentrate on not burning out too quickly."                
                $ P_FocusX = 1
            "Release your focus." if P_FocusX:
                "You release your concentration. . ."                
                $ P_FocusX = 0
            "How about a blowjob?":
                if E_Action and MultiAction:
                    $ Situation = "shift"
                    call E_TJAfter from _call_E_TJAfter_1                
                    call E_Blowjob from _call_E_Blowjob_2
                else:
                    ch_e "Actually I'm getting a bit worn out, let's finish up here. . ."
            "How about a handy?":
                if E_Action and MultiAction:
                    $ Situation = "shift"
                    call E_BJAfter from _call_E_BJAfter_2
                    call E_Handjob from _call_E_Handjob_2
                else:
                    ch_e "Actually I'm getting a bit worn out, let's finish up here. . ."
            "I also want to fondle her breasts." if E_Action and MultiAction:
                $ Trigger2 = "fondle breasts"
                $ Situation = "auto"
                call E_Fondle_Breasts from _call_E_Fondle_Breasts_1
                if Trigger2:
                     $ E_Action -= 1               
            "Let's try something else." if MultiAction:                
                $ Line = 0
                call Emma_TJ_Reset from _call_Emma_TJ_Reset_2
                $ Situation = "shift"
                jump E_TJAfter
            "Let's stop for now." if not MultiAction:                
                $ Line = 0
                call Emma_TJ_Reset from _call_Emma_TJ_Reset_3
                jump E_TJAfter
    
    if not Speed:
        if E_Tit > 2:
            $ Line = "She just seems to slowly roll it around."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2) 
        else:
            $ Line = "She doesn't seem to know what to do with it."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 40, 2) 
        if P_Focus > 60:
            $ P_Focus -= 5
        else:
            $ P_Focus += 3
        $ E_Addict -= 1
        jump ETJ_Cycle
        
    
    if E_Tit > 4 and E_Blow:                                        #5th+ and blown
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["She rocks her breasts up and down around your cock", 
                "She lightly licks the head as it pops up between her tits", 
                "She has a smooth motion going now, gentle and precise",
                "She pauses to rub her nipples across the shaft",
                "In between strokes she gently sucks on the head",
                "She drips some spittle down to make sure you're properly lubed",
                "She gently caresses the shaft between her tits"])            
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 70, 15)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 4)         
        else:                                                       #fast
            $ Line = renpy.random.choice(["She rapidly rocks her breasts up and down around your cock", 
                "She licks away at the head every time it pops up between her tits", 
                "She has a smooth motion going now, quick by efficient",
                "She dancers her nipples across the shaft",
                "In as she strokes faster and faster, she bends down to suck on the head",
                "She covers her tits with drool to keep them well lubed",
                "She rapidly caresses the shaft between her tits"])
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 40, 15, 1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 2)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 4) 
        
    elif E_Tit > 1:                                                 #third through 5th time
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["She juggles her breasts up and down around your cock", 
                "She lightly strokes the head as it pops up between her tits", 
                "She has a smooth motion going now, gentle and precise",
                "She pauses to rub her nipples across the shaft",
                "She gently caresses the shaft between her tits"])            
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 10)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)                 
        else:                                                       #fast
            $ Line = renpy.random.choice(["She rapidly juggles her breasts up and down around your cock", 
                "She lightly brushes the head with her chin as it pops up between her tits", 
                "She moves them up and down in a fluid rocking motion",
                "She bounces her whole body up and down",
                "She rapidly slides the shaft between her tits"])            
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 50, 8, 1)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 7) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 4) 

    
    else:                                                           #First and second time
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["Emma sort of squishes her breasts back and forth around your cock", 
                "She slides the cock up and down between her cleavage", 
                "She kind of bounces her tits around your cock",
                "She smooshes her cleavage as tight as she can and rubs up and down"])
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 7)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)                 
        else:                                                       #fast
            $ Line = renpy.random.choice(["Emma sort of bounces her breasts off your cock", 
                "She tries to quickly slide the cock up and down between her cleavage, but it tends to slide out", 
                "She slaps her tits against your dick",
                "She smooshes her cleavage as tight as she can and rubs up and down quite quickly"])            
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 7)
            $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 200, 4) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3) 
    
    call Emma_Offhand from _call_Emma_Offhand                                                            #Offhand and reduce addiciton per stroke        
    $ E_Addict -= 2          
    
    if P_Focus >= 100 or E_Lust >= 100:                                     #If either of you could cum    
        if P_Focus >= 100:                                                  #You cum             
            call PE_Cumming from _call_PE_Cumming_2
            if "angry" in E_RecentActions:  
                call Emma_TJ_Reset from _call_Emma_TJ_Reset_4
                return    
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
            if 100 > E_Lust >= 70 and E_OCount < 2:             
                $ E_RecentActions.append("unsatisfied")                      
                $ E_DailyActions.append("unsatisfied") 
            
            if P_Focus > 80:
                jump E_TJAfter   
        
        if E_Lust >= 100:                                                   #and Emma cums                    
            call E_Cumming from _call_E_Cumming_2
            if Situation == "shift" or "angry" in E_RecentActions:
                jump E_TJAfter            
                        
        if P_Focus <= 20 or not P_Semen:
            if not P_Semen:
                "You're pretty wiped, better stop for now."
            $ Line = 0
            jump E_TJAfter     
     

    if Round:
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
        jump ETJ_Cycle  
    else: # You ran out of tries.
        call EmmaFace("bemused", 0) from _call_EmmaFace_106
        $ Line = 0
        ch_e "Ok, [E_Petname], that's enough of that for now."
        
label E_TJAfter:
    $ E_Tit += 1
    
    call EmmaFace("sexy") from _call_EmmaFace_107  
        
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
        
    if E_Tit > 5:
        pass
    elif E_Tit == 1 and E_Love >= 500:
        $ E_Mouth = "smile"
        ch_e "Well, that was certainly interesting."
    elif E_Tit == 1 and P_Focus <= 20:
        $ E_Mouth = "sad"
        ch_e "Well, I hope that was enough for you."        
    elif E_Tit == 5:
        ch_e "I think I've got the goods for this."        
    if E_Tit == 1:
        $E_SEXP += 12
    
    $ Tempmod = 0    
    
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    else:
        call Emma_TJ_Reset from _call_Emma_TJ_Reset_5    
    call Checkout from _call_Checkout_8
    return

# ## end E_Titjob //////////////////////////////////////////////////////////////////////

# # ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label E_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in E_Inventory:
        "You ask Emma to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label E_Dildo_Pussy:
    call Shift_Focus("Emma") from _call_Shift_Focus_10
    call E_Dildo_Check from _call_E_Dildo_Check    
    if not _return:
        return 

    if E_DildoP: #You've done it before
        $ Tempmod += 15
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
        
    if "no dildo" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in E_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Emma", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
                if Approval > 2:                                                      # fix, add Emma auto stuff here
                    if E_Legs == "skirt":
                        "Emma grabs her dildo, hiking up her skirt as she does."
                        $ E_Upskirt = 1
                    elif E_Legs == "pants":
                        "Emma grabs her dildo, pulling down her pants as she does."              
                        $ E_Legs = 0
                    else:
                        "Emma grabs her dildo, rubbing is suggestively against her crotch."
                    $ E_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                            "Emma slides it in."
                        "Go for it.":       
                            call EmmaFace("sexy, 1") from _call_EmmaFace_108                    
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                            ch_p "Oh yeah, [E_Pet], let's do this."
                            call Emma_Namecheck from _call_Emma_Namecheck_8
                            "You grab the dildo and slide it in."
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        "Ask her to stop.":
                            call EmmaFace("surprised") from _call_EmmaFace_109       
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [E_Pet]."
                            call Emma_Namecheck from _call_Emma_Namecheck_9
                            "Emma sets the dildo down."
                            call EmmaOutfit from _call_EmmaOutfit_4
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                            return            
                    jump EDP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add Emma auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call EmmaFace("surprised", 1) from _call_EmmaFace_110
                
                if (E_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call EmmaFace("sexy") from _call_EmmaFace_111
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_e "Ooo, [E_Petname], toys!"            
                    jump EDP_Prep         
                else:                                                                                                            #she's questioning it
                    $ E_Brows = "angry"                
                    menu:
                        ch_e "Hey, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call EmmaFace("sexy", 1) from _call_EmmaFace_112
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                                ch_e "Well, now that you mention it. . ."
                                jump EDP_Prep
                            "You pull back before you really get it in."                    
                            call EmmaFace("bemused", 1) from _call_EmmaFace_113
                            if E_DildoP:
                                ch_e "Well ok, [E_Petname], maybe warn me next time?" 
                            else:
                                ch_e "Well ok, [E_Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                            "You press it inside some more."                              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            if not ApprovalCheck("Emma", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call EmmaFace("angry") from _call_EmmaFace_114
                                "Emma shoves you away and slaps you in the face."
                                ch_e "Jerk!"
                                ch_e "Ask nice if you want to stick something in my ass!"                                               
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Emma_SexSprite"):
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset 
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")                          
                            else:
                                call EmmaFace("sad") from _call_EmmaFace_115
                                "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump EDP_Prep
                return             
    #end Auto
   
    if not E_DildoP:                                                               
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_116
            $ E_Mouth = "kiss"
            ch_e "Hmmm, so you'd like to try out some toys?"    
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_117
                ch_e "I suppose there are worst things you could ask for."
            
    if not E_DildoP and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_118
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_119
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I've had a reasonable amount of experience with these, you know. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_120
                ch_e "If that's what you want, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_121
                $ E_Mouth = "smile"             
                ch_e "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_122
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "The toys again?" 
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in E_RecentActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_123
                ch_e "Mmm, again? Ok, let's get to it."
                jump EDP_Prep
            elif "dildo pussy" in E_DailyActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_124
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_e "[Line]"
            elif E_DildoP < 3:        
                call EmmaFace("sexy", 1) from _call_EmmaFace_125
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "You want to stick it in my again?"       
            else:       
                call EmmaFace("sexy", 1) from _call_EmmaFace_126
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_e "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_127
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."    
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_128
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
            jump EDP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry") from _call_EmmaFace_129
            if "no dildo" in E_RecentActions:  
                ch_e "What part of \"no,\" did you not get, [E_Petname]?"
            elif Taboo and "tabno" in E_DailyActions and "no dildo" in E_DailyActions:
                ch_e "Stop swinging that thing around in public!"   
            elif "no dildo" in E_DailyActions:       
                ch_e "I already told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "Stop swinging that thing around in public!"  
            elif not E_DildoP:
                call EmmaFace("bemused") from _call_EmmaFace_130
                ch_e "I'm just not into toys, [E_Petname]. . ."
            else:
                call EmmaFace("bemused") from _call_EmmaFace_131
                ch_e "I don't think we need any toys, [E_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in E_DailyActions:
                    call EmmaFace("bemused") from _call_EmmaFace_132
                    ch_e "Yeah, ok, [E_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in E_DailyActions:
                    call EmmaFace("sexy") from _call_EmmaFace_133  
                    ch_e "Maybe I'll practice on my own time, [E_Petname]."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)  
                    if Taboo:                    
                        $ E_RecentActions.append("tabno")                      
                        $ E_DailyActions.append("tabno") 
                    $ E_RecentActions.append("no dildo")                      
                    $ E_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call EmmaFace("sexy") from _call_EmmaFace_134     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump EDP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad") from _call_EmmaFace_135
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                        ch_e "Ok, fine. If we're going to do this, stick it in already."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        $ E_Forced = 1  
                        jump EDP_Prep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)     
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1  
    if "no dildo" in E_DailyActions:
            ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif E_Forced:
            call EmmaFace("angry", 1) from _call_EmmaFace_136
            ch_e "I'm not going to let you use that on me."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)   
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call EmmaFace("angry", 1) from _call_EmmaFace_137         
            $ E_RecentActions.append("tabno")                       
            $ E_DailyActions.append("tabno") 
            ch_e "Not here!"     
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif E_DildoP:
            call EmmaFace("sad") from _call_EmmaFace_138 
            ch_e "Sorry, you can keep your toys to yourself."     
    else:
            call EmmaFace("normal", 1) from _call_EmmaFace_139
            ch_e "No way."  
    $ E_RecentActions.append("no dildo")                      
    $ E_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label EDP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 15 if E_Legs == "pants" else 0           
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("dildo pussy") from _call_E_Pussy_Launch
    if not E_DildoP:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -75)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 60)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 45)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_12
    call DrainWord("Emma","no dildo") from _call_DrainWord_13
    $ E_RecentActions.append("dildo pussy")                      
    $ E_DailyActions.append("dildo pussy") 
    
label EDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_11 
        call E_Pussy_Launch("dildo pussy") from _call_E_Pussy_Launch_1
        call EmmaLust from _call_EmmaLust_3   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + E_DildoP):
                    $ E_Brows = "confused"
                    ch_e "What are you even doing down there?" 
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_DildoP) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump EDP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump EDP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_140   
                                    call E_Pos_Reset from _call_E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump EDP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                                           
                        "Slap her ass":                     
                                call E_Slap_Ass from _call_E_Slap_Ass
                                jump EDP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0

                        
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_2  
                                    
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her ass.":
                                                    $ Situation = "shift"
                                                    call EDP_After from _call_EDP_After
                                                    call E_Insert_Ass from _call_E_Insert_Ass    
                                            "Just stick a finger in her ass without asking.":
                                                    $ Situation = "auto"
                                                    call EDP_After from _call_EDP_After_1
                                                    call E_Insert_Ass from _call_E_Insert_Ass_1                                           
                                            "I want to shift the dilso to her ass.":
                                                    $ Situation = "shift"
                                                    call EDP_After from _call_EDP_After_2
                                                    call E_Dildo_Ass from _call_E_Dildo_Ass   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call EDP_After from _call_EDP_After_3
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_1   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_1
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump EDP_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_2
                                    $ Line = 0
                                    jump EDP_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto") from _call_E_Undress_3
            
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_2
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_3
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_3
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump EDP_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming from _call_E_Cumming_3
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump EDP_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                            "Emma still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump EDP_After
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_141
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    
label EDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_4
        
    call EmmaFace("sexy") from _call_EmmaFace_142 
    
    $ E_DildoP += 1  
    $ E_Action -=1   
        
    if R_Loc == bg_current and "noticed Emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
     
    if E_DildoP == 1:            
            $ E_SEXP += 10         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "Thanks for the extra hand. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_143
                    ch_e "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_9
    return   

# end E_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label E_Dildo_Ass:
    call Shift_Focus("Emma") from _call_Shift_Focus_12
    call E_Dildo_Check from _call_E_Dildo_Check_1
    if not _return:
        return 
      
    if E_Loose:
        $ Tempmod += 30   
    elif "anal" in E_RecentActions or "dildo anal" in E_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in E_DailyActions or "dildo anal" in E_DailyActions:
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
        
    if "no dildo" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in E_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Emma", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Emma":                                                                  
            #Emma auto-starts   
            if Approval > 2:                                                      # fix, add Emma auto stuff here
                if E_Legs == "skirt":
                    "Emma grabs her dildo, hiking up her skirt as she does."
                    $ E_Upskirt = 1
                elif E_Legs == "pants":
                    "Emma grabs her dildo, pulling down her pants as she does."              
                    $ E_Legs = 0
                else:
                    "Emma grabs her dildo, rubbing is suggestively against her ass."
                $ E_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                        "Emma slides it in."
                    "Go for it.":       
                        call EmmaFace("sexy, 1") from _call_EmmaFace_144                    
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
                        ch_p "Oh yeah, [E_Pet], let's do this."
                        call Emma_Namecheck from _call_Emma_Namecheck_10
                        "You grab the dildo and slide it in."
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 85, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    "Ask her to stop.":
                        call EmmaFace("surprised") from _call_EmmaFace_145       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [E_Pet]."
                        call Emma_Namecheck from _call_Emma_Namecheck_11
                        "Emma sets the dildo down."
                        call EmmaOutfit from _call_EmmaOutfit_5
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                        return            
                jump EDA_Prep
            else:                
                $ Tempmod = 0                               # fix, add Emma auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call EmmaFace("surprised", 1) from _call_EmmaFace_146
            
            if (E_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Emma is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call EmmaFace("sexy") from _call_EmmaFace_147
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
                ch_e "Ooo, [E_Petname], toys!"                
                jump EDA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ E_Brows = "angry"                
                menu:
                    ch_e "Hey, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call EmmaFace("sexy", 1) from _call_EmmaFace_148
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                            ch_e "Well, now that you mention it. . ."
                            jump EDA_Prep
                        "You pull back before you really get it in."                    
                        call EmmaFace("bemused", 1) from _call_EmmaFace_149
                        if E_DildoA:
                            ch_e "Well ok, [E_Petname], maybe warn me next time?" 
                        else:
                            ch_e "Well ok, [E_Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)
                        "You press it inside some more."                              
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        if not ApprovalCheck("Emma", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call EmmaFace("angry") from _call_EmmaFace_150
                            "Emma shoves you away and slaps you in the face."
                            ch_e "Jerk!"
                            ch_e "Ask nice if you want to stick something in my ass!"                                                  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10, 1)                        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Emma_SexSprite"):
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_1 
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")                         
                        else:
                            call EmmaFace("sad") from _call_EmmaFace_151
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump EDA_Prep
            return             
    #end auto
   
    if not E_DildoA:                                                               
            #first time    
            call EmmaFace("surprised", 1) from _call_EmmaFace_152
            $ E_Mouth = "kiss"
            ch_e "You want to try and fit that. . .?"    
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_153
                ch_e "Always about the but, huh?"
    
    if not E_Loose and ("dildo anal" in E_RecentActions or "anal" in E_RecentActions or "dildo anal" in E_DailyActions or "anal" in E_DailyActions):
            call EmmaFace("bemused", 1) from _call_EmmaFace_154
            ch_e "I'm still sore from earlier. . ."
            
    if not E_DildoA and Approval:                                                 
            #First time dialog        
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_155
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy") from _call_EmmaFace_156
                $ E_Brows = "sad"
                $ E_Mouth = "smile" 
                ch_e "I haven't actually used one of these, back there before. . ."            
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal") from _call_EmmaFace_157
                ch_e "If that's what you want, [E_Petname]. . ."            
            else: # Uninhibited 
                call EmmaFace("sad") from _call_EmmaFace_158
                $ E_Mouth = "smile"             
                ch_e "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if E_Forced: 
                call EmmaFace("sad") from _call_EmmaFace_159
                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                ch_e "The toys again?"  
            elif not Taboo and "tabno" in E_DailyActions:        
                ch_e "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in E_DailyActions and not E_Loose:
                pass
            elif "dildo anal" in E_DailyActions:
                call EmmaFace("sexy", 1) from _call_EmmaFace_160
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_e "[Line]"
            elif E_DildoA < 3:        
                call EmmaFace("sexy", 1) from _call_EmmaFace_161
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "You want to stick it in my ass again?"       
            else:       
                call EmmaFace("sexy", 1) from _call_EmmaFace_162
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_e "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_163
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                ch_e "Ok, fine."    
            else:
                call EmmaFace("sexy", 1) from _call_EmmaFace_164
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
            jump EDA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call EmmaFace("angry") from _call_EmmaFace_165
            if "no dildo" in E_RecentActions:  
                ch_e "What part of \"no,\" did you not get, [E_Petname]?"
            elif Taboo and "tabno" in E_DailyActions and "no dildo" in E_DailyActions:
                ch_e "Stop swinging that thing around in public!"  
            elif "no dildo" in E_DailyActions:       
                ch_e "I already told you \"no,\" [E_Petname]."
            elif Taboo and "tabno" in E_DailyActions:  
                ch_e "I already told you that I wouldn't do that out here!"  
            elif not E_DildoA:
                call EmmaFace("bemused") from _call_EmmaFace_166
                ch_e "I'm just not into toys, [E_Petname]. . ."
            elif not E_Loose and "dildo anal" not in E_DailyActions:
                call EmmaFace("perplexed") from _call_EmmaFace_167
                ch_e "You could have been a bit more gentle last time, [E_Petname]. . ."
            else:
                call EmmaFace("bemused") from _call_EmmaFace_168
                ch_e "I don't think we need any toys, [E_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in E_DailyActions:
                    call EmmaFace("bemused") from _call_EmmaFace_169
                    ch_e "Yeah, ok, [E_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in E_DailyActions:
                    call EmmaFace("sexy") from _call_EmmaFace_170  
                    ch_e "Maybe I'll practice on my own time, [E_Petname]."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)  
                    if Taboo:                    
                        $ E_RecentActions.append("tabno")                      
                        $ E_DailyActions.append("tabno") 
                    $ E_RecentActions.append("no dildo")                      
                    $ E_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call EmmaFace("sexy") from _call_EmmaFace_171     
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_e "[Line]"
                        $ Line = 0                   
                        jump EDA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad") from _call_EmmaFace_172
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)                 
                        ch_e "Ok, fine. If we're going to do this, stick it in already."  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 4)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        $ E_Forced = 1  
                        jump EDA_Prep
                    else:                              
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -20)    
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1   
    if "no dildo" in E_DailyActions:
            ch_e "Learn to take \"no\" for an answer, [E_Petname]."   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif E_Forced:
            call EmmaFace("angry", 1) from _call_EmmaFace_173
            ch_e "I'm not going to let you use that on me."
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call EmmaFace("angry", 1) from _call_EmmaFace_174          
            $ E_RecentActions.append("tabno")                       
            $ E_DailyActions.append("tabno") 
            ch_e "Not here!"     
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)  
    elif not E_Loose and "dildo anal" in E_DailyActions:
            call EmmaFace("bemused") from _call_EmmaFace_175
            ch_e "Sorry, I just need a little break back there, [E_Petname]."    
    elif E_DildoA:
            call EmmaFace("sad") from _call_EmmaFace_176 
            ch_e "Sorry, you can keep your toys out of there."     
    else:
            call EmmaFace("normal", 1) from _call_EmmaFace_177
            ch_e "No way." 
    $ E_RecentActions.append("no dildo")                      
    $ E_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label EDA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 20 if E_Legs == "pants" else 0           
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_1
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("dildo anal") from _call_E_Pussy_Launch_2
    if not E_DildoA:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -75)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 60)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 45)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_14
    call DrainWord("Emma","no dildo") from _call_DrainWord_15
    $ E_RecentActions.append("dildo anal")                      
    $ E_DailyActions.append("dildo anal") 
    
label EDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_13 
        call E_Pussy_Launch("dildo anal") from _call_E_Pussy_Launch_3
        call EmmaLust from _call_EmmaLust_4   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + E_DildoA):
                    $ E_Brows = "confused"
                    ch_e "What are you even doing down there?" 
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_DildoA) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump EDA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump EDA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_178   
                                    call E_Pos_Reset from _call_E_Pos_Reset_5
                                    "She scowls at you and pulls back."
                                    ch_e "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump EDA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                    
                        "Slap her ass":                     
                                call E_Slap_Ass from _call_E_Slap_Ass_1
                                jump EDA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0
                        
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_4  
                                                            
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her pussy.":
                                                    $ Situation = "shift"
                                                    call EDA_After from _call_EDA_After
                                                    call E_Fondle_Pussy from _call_E_Fondle_Pussy    
                                            "Just stick a finger in her pussy without asking.":
                                                    $ Situation = "auto"
                                                    call EDA_After from _call_EDA_After_1
                                                    call E_Fondle_Pussy from _call_E_Fondle_Pussy_1                                           
                                            "I want to shift the dilso to her pussy.":
                                                    $ Situation = "shift"
                                                    call EDA_After from _call_EDA_After_2
                                                    call E_Dildo_Pussy from _call_E_Dildo_Pussy   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_2
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call EDA_After from _call_EDA_After_3
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_3   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_6
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump EDA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_7
                                    $ Line = 0
                                    jump EDA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto") from _call_E_Undress_5
            
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_3
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_4
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_8
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump EDA_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming from _call_E_Cumming_4
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump EDA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in E_RecentActions:#And Emma is unsatisfied,  
                            "Emma still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump EDA_After
        #End orgasm
        
   
        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_179
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."
    
    
label EDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_9
        
    call EmmaFace("sexy") from _call_EmmaFace_180 
    
    $ E_DildoA += 1  
    $ E_Action -=1            
    
    if R_Loc == bg_current and "noticed Emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
     
    if E_DildoA == 1:            
            $ E_SEXP += 10         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    if E_Loose:
                        ch_e "That was. . . interesting. . ."
                    else:
                        ch_e "Ouch. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_181
                    ch_e "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_10
    return   

# # end E_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label E_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in E_Inventory:
        "You ask Emma to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
# ## E_Footjob //////////////////////////////////////////////////////////////////////
label E_Footjob:
    $ E_LegsUp = 0
    call Shift_Focus("Emma") from _call_Shift_Focus_14
    if E_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif E_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif E_Foot: #You've done it before
        $ Tempmod += 3
        
    if E_Addict >= 75 and E_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if E_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no foot" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in E_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Emma", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Emma":                                                                  #Emma auto-starts   
        if Approval > 2:                                                      # fix, add Emma auto stuff here
            if Trigger2 == "jackin":
                "Emma leans and starts rubbing your cock between her feet."
            else:
                "Emma gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)                     
                    "Emma continues her actions."
                "Praise her.":       
                    call EmmaFace("sexy, 1") from _call_EmmaFace_182                    
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_12
                    "Emma continues her actions."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised") from _call_EmmaFace_183       
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [E_Pet]."
                    call Emma_Namecheck from _call_Emma_Namecheck_13
                    "Emma puts it down."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump EFJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Emma auto stuff here
            $ Trigger2 = 0
            return            
    
    if not E_Foot and "no foot" not in E_RecentActions:        
        call EmmaFace("confused", 2) from _call_EmmaFace_184
        ch_e "Huh, so you'd like me to touch your cock with my feet?"
        $ E_Blush = 1
            
    if not E_Foot and Approval:                                                 #First time dialog        
        if E_Forced: 
            call EmmaFace("sad",1) from _call_EmmaFace_185
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
        elif E_Love >= (E_Obed + E_Inbt):
            call EmmaFace("sexy",1) from _call_EmmaFace_186
            $ E_Brows = "sad"
            $ E_Mouth = "smile" 
            ch_e "I guess it couldn't hurt. . ."            
        elif E_Obed >= E_Inbt:
            call EmmaFace("normal",1) from _call_EmmaFace_187
            ch_e "If you want, [E_Petname]. . ."            
        elif E_Addict >= 50:
            call EmmaFace("manic", 1) from _call_EmmaFace_188
            ch_e "Okay. . ."  
        else: # Uninhibited 
            call EmmaFace("lipbite",1) from _call_EmmaFace_189    
            ch_e "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_190
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            ch_e "That's all?" 
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "Um, I guess this is secluded enough. . ."    
        elif "foot" in E_RecentActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_191
            ch_e "I'm getting foot cramps. . ."
            jump EFJ_Prep
        elif "foot" in E_DailyActions:
            call EmmaFace("sexy", 1) from _call_EmmaFace_192
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_e "[Line]"
        elif E_Foot < 3:        
            call EmmaFace("sexy", 1) from _call_EmmaFace_193
            $ E_Brows = "confused"
            $ E_Mouth = "kiss"
            ch_e "Hmm, magic toes. . ."        
        else:       
            call EmmaFace("sexy", 1) from _call_EmmaFace_194
            $ Emma_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_e "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_195
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "Ok, fine." 
        elif "no foot" in E_DailyActions:               
            ch_e "OK, geeze!"   
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_196
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_e "[Line]"
            $ Line = 0
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump EFJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry") from _call_EmmaFace_197
        if "no foot" in E_RecentActions:  
            ch_e "You don't listen do you, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no foot" in E_DailyActions: 
            ch_e "I said not in public!"  
        elif "no foot" in E_DailyActions:       
            ch_e "I told you \"no,\" [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "I said not in public!"     
        elif not E_Foot:
            call EmmaFace("bemused") from _call_EmmaFace_198
            ch_e "I don't know, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_199
            ch_e "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_200
                ch_e "Yeah."              
                return
            "Maybe later?" if "no foot" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_201  
                ch_e ". . ."
                ch_e "Maybe."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no foot")                      
                $ E_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_202     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_e "[Line]"
                    $ Line = 0                   
                    jump EFJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Emma", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_203
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Ok, fine."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    $ E_Forced = 1  
                    jump EFJ_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)     
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Emma_Arms = 1 
    if "no foot" in E_DailyActions:
        call EmmaFace("angry", 1) from _call_EmmaFace_204
        ch_e "I'm not telling you again."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_205
        ch_e "I don't even want to step on it."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2) if E_Love > 300 else E_Love
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1) from _call_EmmaFace_206          
        $ E_DailyActions.append("tabno") 
        ch_e "Not here, not anywhere near here."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)  
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)   
    elif E_Foot:
        call EmmaFace("sad") from _call_EmmaFace_207 
        ch_e "I'm not feeling it today. . ."       
    else:
        call EmmaFace("normal", 1) from _call_EmmaFace_208
        ch_e "I don't know about using my feet for. . . that."  
    $ E_RecentActions.append("no foot")                      
    $ E_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label EFJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
                
    call EmmaFace("sexy") from _call_EmmaFace_209
    if E_Forced:
        call EmmaFace("sad") from _call_EmmaFace_210
    elif E_Foot:
        $ E_Brows = "confused"
        $ E_Eyes = "sexy"
        $ E_Mouth = "smile"
    
    if not E_Foot:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 30) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_3
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_16
    call DrainWord("Emma","no foot") from _call_DrainWord_17
    $ E_RecentActions.append("foot")                      
    $ E_DailyActions.append("foot") 
  
label EFJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Emma") from _call_Shift_Focus_15
        call Emma_Sex_Launch("foot") from _call_Emma_Sex_Launch
        call EmmaLust from _call_EmmaLust_5   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ E_Brows = "angry"        
                    menu:
                        ch_e "Ouch, foot cramp, can we take a break?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_FJAfter from _call_E_FJAfter
                                call E_Blowjob from _call_E_Blowjob_3   
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_FJAfter from _call_E_FJAfter_1
                                call E_Handjob from _call_E_Handjob_3  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump EFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_2
                                $ Situation = "shift"
                                jump E_FJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call EmmaFace("angry", 1) from _call_EmmaFace_211   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_e "Hey, I've got better things to do if you're going to be a dick about it."                                               
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)                     
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FJAfter
        elif Cnt == 10 and E_SEXP <= 100 and not ApprovalCheck("Emma", 1200, "LO"):
                    $ E_Brows = "confused"
                    ch_e "Can we be done with this now? I'm getting sore."         
        #End Count check
        
        if not Speed:
            $ Speed = 1 

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
                                    if Trigger2 == "jackin":
                                        "You ask her to up the pace a bit, and move your own hand out of the way."
                                    else:
                                        "You ask her to up the pace a bit."
                                    
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        # "Blindfold her" if E_Bondage and not E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ E_Blindfold = 1
            
                        # "Remove blindfold" if E_Blindfold:
                        #     call EmmaFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ E_Blindfold = 0
                   
                        "Maybe lose some clothes. . .":
                                    call E_Undress from _call_E_Undress_6  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if E_Action and MultiAction:
                                                $ Situation = "shift"
                                                call E_FJAfter from _call_E_FJAfter_2                
                                                call E_Blowjob from _call_E_Blowjob_4
                                            else:
                                                ch_e "Actually I'm getting a bit worn out, let's finish up here. . ."
                                "How about a handjob?":
                                            if E_Action and MultiAction:
                                                $ Situation = "shift"
                                                call E_FJAfter from _call_E_FJAfter_3                
                                                call E_Handjob from _call_E_Handjob_4
                                            else:
                                                ch_e "Actually I'm getting a bit worn out, let's finish up here. . ."
                                         
                        "I also want to. . . [[Offhand]": #fix set this up
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_4
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I kinda need a break, so if we could wrap this up?"  
                                    
                        "Let's try something else." if MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_3
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Emma_Sex_Reset from _call_Emma_Sex_Reset_4
                                    $ Line = 0
                                    jump E_FJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_4
                
        #If either of you could cum 
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_5
                            if "angry" in E_RecentActions:  
                                call Emma_Sex_Reset from _call_Emma_Sex_Reset_5
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FJAfter 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                                                
                            call E_Cumming from _call_E_Cumming_5
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_FJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump E_FJAfter   
        #End orgasm
   
        if Round == 10:
            ch_e "It's kind of time to get moving."   
        elif Round == 5:
            ch_e "For real time's up."      
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0) from _call_EmmaFace_212
    $ Line = 0
    ch_e "Ok, we need to take a break."
    
label E_FJAfter:
    call EmmaFace("sexy") from _call_EmmaFace_213 
    
    $ E_Foot += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5)
    
    if E_Loc == bg_current and "noticed rogue" in E_RecentActions: #If Emma was participating
        $ R_LikeEmma += 1
    
    if "Emmapedi" in Achievements:
            pass  
    elif E_Foot >= 10:
            call EmmaFace("smile", 1) from _call_EmmaFace_214
            ch_e "I guess I've gotten pretty smooth at the \"Emmapedi.\""
            $ Achievements.append("Emmapedi")
            $ E_SEXP += 5          
    elif E_Foot == 1:            
            $ E_SEXP += 10
            if E_Love >= 500:
                $ E_Mouth = "smile"
                ch_e "I could feel you down there. . ."
            elif P_Focus <= 20:
                $ E_Mouth = "sad"
                ch_e "Did that work out for you?"
    elif E_Foot == 5:
                ch_e "Let me know any time you need me to \"foot you up.\""                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Ok, so what were you thinking?"
    else:
        call Emma_Sex_Reset from _call_Emma_Sex_Reset_6    
    call Checkout from _call_Checkout_11
    return

## end E_Footjob //////////////////////////////////////////////////////////////////////


label E_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call E_Les_Response("Rogue",1)
        if E_Les:
            $ Tempmod += 10
        if E_SEXP >= 50:
            $ Tempmod += 25
        elif E_SEXP >= 30:
            $ Tempmod += 15
        elif E_SEXP >= 15:
            $ Tempmod += 5
                    
        elif E_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in E_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in E_Traits or "sex friend" in E_Petnames:
            $ Tempmod += 10        
        elif "ex" in E_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if E_LikeRogue >= 900:
                        $ B += 150
                elif E_LikeRogue >= 800 or "poly rogue" in E_Traits:
                        $ B += 100
                elif E_LikeRogue >= 700:
                        $ B += 50
                elif E_LikeRogue <= 200:
                        $ B -= 200
                elif E_LikeRogue <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Emma", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Emma likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call EmmaFace("sexy", 1) from _call_EmmaFace_215
                ch_e "Aw, come on [Girl], wouldn't it be fun?"
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ E_LikeRogue += (int(B/10))
                            $ R_LikeEmma += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call EmmaFace("smile", 1) from _call_EmmaFace_216
                ch_e "Sure, sounds fun!"
                $ Result = 1
            elif Approval:
                call EmmaFace("sly", 2) from _call_EmmaFace_217
                if B >= 100:
                        ch_e "I kinda want to, but I don't know. . ."
                if B >= 0:
                        ch_e "I don't know about doing it with her. . ."
                $ E_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_e "You know what? I'm in."
                                $ Result = 1
                            else:
                                call EmmaFace("smile") from _call_EmmaFace_218
                                ch_e "Thanks, that's really cool of you."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_e "Well, I guess I might." 
                                $ Result = 1
                            else:
                                call EmmaFace("sad", 2) from _call_EmmaFace_219
                                ch_e "I don't think so." 
                    "Get in there, now.":
                            if ApprovalCheck("Emma", 550, "OI", TabM = 2):
                                call EmmaFace("sadside", 1) from _call_EmmaFace_220
                                ch_e "Ok, FINE."
                                $ Result = 1
                            else:
                                call EmmaFace("angry") from _call_EmmaFace_221
                                ch_e "Like hell I will."  
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1) from _call_RogueFace_76
                                if R_Les and E_Les:
                                        ch_r "Come on Emma, don't we have fun?"
                                else:
                                        ch_r "Come on Emma, couldn't it be fun?"
                                $ E_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeEmma += 5
                            if B >= 50:
                                call EmmaFace("smile", 1) from _call_EmmaFace_222
                                ch_e "Heh, I guess you're right, [Girl]."
                                $ Result = 1
                            else:
                                call EmmaFace("angry", 1, Eyes="side") from _call_EmmaFace_223
                                ch_e "Yeah, no, I really don't think so."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call EmmaFace("smile", 1) from _call_EmmaFace_224
                            ch_e "Yeah, I mean I guess we could. . ."
                            $ Result = 1
                    else:
                            call EmmaFace("sadside", 1) from _call_EmmaFace_225
                            ch_e "I don't think I could manage that. . ."
            
            if not Result:      
                #no approval
                $ E_RecentActions.append("no lesbian")                      
                $ E_DailyActions.append("no lesbian") 
                call EmmaFace("sadside", 1) from _call_EmmaFace_226
                if B <= 0:
                    ch_e "I'm sorry, [E_Petname], I just can't do that with her."
                if Taboo:
                    ch_e "I'm sorry, [E_Petname], I just can't do that around here."
                if B >= 100:
                    ch_e "I'm sorry, [E_Petname], I just can't do that with you around."
                else:
                    ch_e "I'm sorry, [E_Petname], I just can't do that."
                
        return Result
#End E_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >