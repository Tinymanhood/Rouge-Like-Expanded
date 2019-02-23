## K_Handjob //////////////////////////////////////////////////////////////////////
label K_Handjob:
    call Shift_Focus("Kitty") from _call_Shift_Focus_206
    if K_Hand >= 7: # She loves it
        $ Tempmod += 10
    elif K_Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Hand: #You've done it before
        $ Tempmod += 3
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if K_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no hand" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            if Trigger2 == "jackin":
                "Kitty brushes your hand aside and starts stroking your cock."
            else:
                "Kitty gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)                     
                    "Kitty continues her actions."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_724                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_8
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised") from _call_KittyFace_725       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_9
                    "Kitty puts it down."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump KHJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Hand and "no hand" not in K_RecentActions:        
        call KittyFace("confused", 2) from _call_KittyFace_726
        ch_k "So you want a handy then?"
        $ K_Blush = 1
            
    if not K_Hand and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1) from _call_KittyFace_727
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1) from _call_KittyFace_728
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it could be interesting. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1) from _call_KittyFace_729
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_730
            ch_k "I kind of {i}need{/i} to. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1) from _call_KittyFace_731    
            ch_k "I guess. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_732
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's it, right?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, I guess if it's here. . ."    
        elif "hand" in K_RecentActions:
            call KittyFace("sexy", 1) from _call_KittyFace_733
            ch_k "You're giving me carpal tunnel. . ."
            jump KHJ_Prep
        elif "hand" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_734
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Hand < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_735
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic fingers. . ."        
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_736
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_737
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine." 
        elif "no hand" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_738
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump KHJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_739
        if "no hand" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no hand" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no hand" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Hand:
            call KittyFace("bemused") from _call_KittyFace_740
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_741
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_742
                ch_k "Yeah."              
                return
            "Maybe later?" if "no hand" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_743  
                ch_k ". . ."
                ch_k "Maybe."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no hand")                      
                $ K_DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_744     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KHJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_745
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, fine."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1  
                    jump KHJ_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1 
    if "no hand" in K_DailyActions:
        call KittyFace("angry", 1) from _call_KittyFace_746
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_747
        ch_k "Not even if you had a ten foot pole."
        call KittyFace("surprised", 2) from _call_KittyFace_748
        ch_k "I mean. . ."
        call KittyFace("angry", 1) from _call_KittyFace_749        
        ch_k "You know what I mean!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_750          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)   
    elif K_Hand:
        call KittyFace("sad") from _call_KittyFace_751 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1) from _call_KittyFace_752
        ch_k "I don't wanna touch that."  
    $ K_RecentActions.append("no hand")                      
    $ K_DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label KHJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy") from _call_KittyFace_753
    if K_Forced:
        call KittyFace("sad") from _call_KittyFace_754
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Kitty_HJ_Launch("L") from _call_Kitty_HJ_Launch_10
    if not K_Hand:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_21
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_167
    call DrainWord("Kitty","no hand") from _call_DrainWord_168
    $ K_RecentActions.append("hand")                      
    $ K_DailyActions.append("hand") 
  
label KHJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Kitty") from _call_Shift_Focus_207
        call Kitty_HJ_Launch from _call_Kitty_HJ_Launch_11    
        call KittyLust from _call_KittyLust_17   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, hand cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_HJAfter from _call_K_HJAfter_1
                                call K_Blowjob from _call_K_Blowjob_4       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump KHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_4
                                $ Situation = "shift"
                                jump K_HJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_755   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[K_like]going to be a dick about it."                                               
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)                     
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_HJAfter
        elif Cnt == 10 and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Can we[K_Like]be done with this now? I'm getting sore."         
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

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_756 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1

                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_757 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                            
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                   
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_18  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_HJAfter from _call_K_HJAfter_2                
                                                call K_Blowjob from _call_K_Blowjob_5
                                            else:
                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                
#                                "How about a titjob?":
#                                            if K_Action and MultiAction:
#                                                $ Situation = "shift"
#                                                call K_HJAfter
#                                                call K_Titjob
#                                            else:
#                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                        
                        "I also want to fondle her breasts." if K_Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    $ Situation = "auto"
                                    call K_Fondle_Breasts from _call_K_Fondle_Breasts_5
                                    if Trigger2:
                                         $ K_Action -= 1
                                         
                        "Let's try something else." if MultiAction: 
                                    call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_5
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_HJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_6
                                    $ Line = 0
                                    jump K_HJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_51
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_14
                            if "angry" in K_RecentActions:  
                                call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_7
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_HJAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                                                
                            call K_Cumming from _call_K_Cumming_23
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_HJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump K_HJAfter   
                
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_758
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label K_HJAfter:
    call KittyFace("sexy") from _call_KittyFace_759 
    
    $ K_Hand += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5)
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ R_LikeKitty += 1
    
    if "Kitty Handi-Queen" in Achievements:
            pass  
    elif K_Hand >= 10:
            call KittyFace("smile", 1) from _call_KittyFace_760
            ch_k "I've kinda become[K_like]a \"Handi-Queen\" or something."
            $ Achievements.append("Kitty Handi-Queen")
            $K_SEXP += 5          
    elif K_Hand == 1:            
            $K_SEXP += 10
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "It was so warm to the touch. . ."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "Did that work out for you?"
    elif K_Hand == 5:
                ch_k "Let me know any time you need me to give you a hand."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_HJ_Reset from _call_Kitty_HJ_Reset_8    
    call Checkout from _call_Checkout_79
    return

## end K_Handjob //////////////////////////////////////////////////////////////////////


## K_Titjob //////////////////////////////////////////////////////////////////////              Not finished
label K_Titjob:
    return #fix remove when this works
    
    call Shift_Focus("Kitty") from _call_Shift_Focus_208
    if K_Tit >= 7: # She loves it
        $ Tempmod += 10
    elif K_Tit >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Tit: #You've done it before
        $ Tempmod += 5
    
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    elif K_Addict >= 75:
        $ Tempmod += 5
        
    if K_SeenChest and ApprovalCheck("Kitty", 500): # You've seen her tits.
        $ Tempmod += 10    
    if not K_Chest and not K_Over: #She's already topless
        $ Tempmod += 10
    if K_Lust > 75: #She's really horny
        $ Tempmod += 10
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in K_Traits:
        $ Tempmod += (5*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 30 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount    
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no titjob" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no titjob" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            call Kitty_TJ_Launch("L") from _call_Kitty_TJ_Launch            
            "Kitty slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)                     
                    "Kitty starts to slide them up and down."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_761                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_10
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":     
                    call KittyFace("confused") from _call_KittyFace_762  
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_11
                    "Kitty lets it drop out from between her breasts."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_1  
                    return            
            jump KTJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Tit and "no titjob" not in K_RecentActions:        
        call KittyFace("surprised", 1) from _call_KittyFace_763
        $ K_Mouth = "kiss"
        ch_k "You want me to rub your cock with my breasts?"        
        if K_Blow:          
            $ K_Mouth = "smile"
            ch_k "My mouth wasn't enough?"
        elif K_Hand:          
            $ K_Mouth = "smile"
            ch_k "My hand wasn't enough?"
            
    if not K_Tit and Approval:                                                 #First time dialog    
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_764
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_765
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "Huh, well that's certainly one way to get off."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_766
            ch_k "If that's what you want. . ."              
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_767
            ch_k "Hmmmm. . . ."     
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_768
            $ K_Mouth = "smile"             
            ch_k "Heh, might be fun."      
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_769
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."   
        elif "titjob" in K_RecentActions:
            call KittyFace("sexy", 1) from _call_KittyFace_770
            ch_k "Mmm, again? Ok, let me get the girls ready."
            jump KTJ_Prep
        elif "titjob" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_771
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."]) 
            ch_k "[Line]"
        elif K_Tit < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_772
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another titjob?"        
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_773
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",                 
                "So you'd like another titjob?",                 
                "A little. . . bounce?", 
                "You want me to pillow your crank?",
                "A little soft embrace?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_774
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Well, there are worst ways to get you off. . ." 
        elif "no titjob" in K_DailyActions:               
            ch_k "Hmm, I suppose. . ."       
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_775
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, put it here.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok, alright."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 1)      
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
        jump KTJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_776
        if "no titjob" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no titjob" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif "no titjob" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif not K_Tit:
            call KittyFace("bemused") from _call_KittyFace_777
            ch_k "I'm not really up for that, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_778
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_779
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no titjob" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_780  
                ch_k "We'll have to see."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no titjob")                      
                $ K_DailyActions.append("no titjob")            
                return
            "I think this could be fun for both of us. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_781     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, ok, put it here.",                 
                        "Well. . . ok.",                 
                        "I guess.", 
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok, alright."])
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KTJ_Prep
                else:   
                    $ Approval = ApprovalCheck("Kitty", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2:       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                        call KittyFace("confused", 1) from _call_KittyFace_782
                        if K_Blow:
                            ch_k "I could just. . . blow you instead?"
                        else:
                            ch_k "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
                        menu:
                            ch_k "What do you say [[blowjob]?"
                            "Ok, get down there.":
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)  
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)                                
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1) 
                                jump KBJ_Prep
                            "Nah, it's all about dem titties.":  
                                $ Line = "no BJ"
                    if Approval:       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                        call KittyFace("confused", 1) from _call_KittyFace_783
                        if K_Hand:
                            ch_k "Maybe you'd settle for a handy?"
                        else:
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_k "What do you say?"
                            "Sure, that's fine.":
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)  
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)                                
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1) 
                                jump KHJ_Prep
                            "Seriously, titties." if Line == "no BJ":  
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":  
                                pass
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, whatever."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2) 
                    
                    
            "Come on, let me fuck those titties, [K_Pet]":                                               # Pressured into it                
                call Kitty_Namecheck from _call_Kitty_Namecheck_12
                $ Approval = ApprovalCheck("Kitty", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_784
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, fine, whip it out."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1
                    jump KTJ_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no titjob" in K_DailyActions:
        call KittyFace("angry", 1) from _call_KittyFace_785
        ch_k "Look, I already told you no thanks, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_786
        ch_k "I'm not that kind of girl."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)      
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_787          
        $ K_DailyActions.append("tabno") 
        ch_k "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_Blow:
        call KittyFace("sad") from _call_KittyFace_788 
        ch_k "I think I'll let you know when I want you touching these again."       
    else:
        call KittyFace("normal", 1) from _call_KittyFace_789
        ch_k "How about let's not, [K_Petname]."
    $ K_RecentActions.append("no titjob")                      
    $ K_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label KTJ_Prep:
      
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)

        
    call KittyFace("sexy") from _call_KittyFace_790
    if K_Forced:
        call KittyFace("sad") from _call_KittyFace_791
    elif K_Tit:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
        
    call Kitty_TJ_Launch("L") from _call_Kitty_TJ_Launch_1    
    if not K_Tit:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -25)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30)   
    
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_22
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_169
    call DrainWord("Kitty","no titjob") from _call_DrainWord_170
    $ K_RecentActions.append("titjob")                      
    $ K_DailyActions.append("titjob") 

label KTJ_Cycle: #Repeating strokes  
    call Shift_Focus("Kitty") from _call_Shift_Focus_209  
    call Kitty_TJ_Launch from _call_Kitty_TJ_Launch_2
        
    call KittyLust from _call_KittyLust_18            
    if P_FocusX and P_Focus > 50:
        $ P_Focus -= 10  
        
    if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
    elif Cnt == (5 + K_Tit):
        $ K_Brows = "confused"
        ch_k "Are you getting close here? I'm getting as little sore."        
    if Cnt == (10 + K_Tit):
        $ K_Brows = "angry"        
        menu:
            ch_k "I'm getting rug-burn here [K_Petname]. Can we do something else?"
            "How about a BJ?" if K_Action and MultiAction:
                $ Situation = "shift"
                call K_TJAfter from _call_K_TJAfter_1
                call K_Blowjob from _call_K_Blowjob_6 
                return
            "Finish up." if P_FocusX:
                "You release your concentration. . ."             
                $ P_FocusX = 0
                $ P_Focus += 15
                $ Cnt += 1
                "[Line]."
                jump KTJ_Cycle                
            "Let's try something else." if MultiAction: 
                $ Line = 0
                call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_2
                $ Situation = "shift"
                jump K_TJAfter
            "No, get back down there.":
                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                    "She grumbles but gets back to work."
                else:
                    call KittyFace("angry", 1) from _call_KittyFace_792   
                    "She scowls at you, drops you cock and pulls back."
                    ch_k "Well if that's your attitude you can handle your own business."                         
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    jump K_TJAfter
                
        
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

            "Blindfold her" if K_Bondage and not K_Blindfold:
                call KittyFace("sexy", 1) from _call_KittyFace_793 
                "You add a blindfold so she can't see a thing"
                $ K_Blindfold = 1

            "Remove blindfold" if K_Blindfold:
                call KittyFace("sexy", 1) from _call_KittyFace_794 
                "You remove the blindfold"
                $ K_Blindfold = 0

            "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                pass
            "Focus to last longer." if "focus" in P_Traits and not P_FocusX:
                "You concentrate on not burning out too quickly."                
                $ P_FocusX = 1
            "Release your focus." if P_FocusX:
                "You release your concentration. . ."                
                $ P_FocusX = 0
            "How about a blowjob?":
                if K_Action and MultiAction:
                    $ Situation = "shift"
                    call K_TJAfter from _call_K_TJAfter_2                
                    call K_Blowjob from _call_K_Blowjob_7
                else:
                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
            "How about a handy?":
                if K_Action and MultiAction:
                    $ Situation = "shift"
                    call K_BJAfter from _call_K_BJAfter_1
                    call K_Handjob from _call_K_Handjob_2
                else:
                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
            "I also want to fondle her breasts." if K_Action and MultiAction:
                $ Trigger2 = "fondle breasts"
                $ Situation = "auto"
                call K_Fondle_Breasts from _call_K_Fondle_Breasts_6
                if Trigger2:
                     $ K_Action -= 1               
            "Let's try something else." if MultiAction:                
                $ Line = 0
                call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_3
                $ Situation = "shift"
                jump K_TJAfter
            "Let's stop for now." if not MultiAction:                
                $ Line = 0
                call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_4
                jump K_TJAfter
    
    if not Speed:
        if K_Tit > 2:
            $ Line = "She just seems to slowly roll it around."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2) 
        else:
            $ Line = "She doesn't seem to know what to do with it."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 40, 2) 
        if P_Focus > 60:
            $ P_Focus -= 5
        else:
            $ P_Focus += 3
        $ K_Addict -= 1
        jump KTJ_Cycle
        
    
    if K_Tit > 4 and K_Blow:                                        #5th+ and blown
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["She rocks her breasts up and down around your cock", 
                "She lightly licks the head as it pops up between her tits", 
                "She has a smooth motion going now, gentle and precise",
                "She pauses to rub her nipples across the shaft",
                "In between strokes she gently sucks on the head",
                "She drips some spittle down to make sure you're properly lubed",
                "She gently caresses the shaft between her tits"])            
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 70, 15)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 4)         
        else:                                                       #fast
            $ Line = renpy.random.choice(["She rapidly rocks her breasts up and down around your cock", 
                "She licks away at the head every time it pops up between her tits", 
                "She has a smooth motion going now, quick by efficient",
                "She dancers her nipples across the shaft",
                "In as she strokes faster and faster, she bends down to suck on the head",
                "She covers her tits with drool to keep them well lubed",
                "She rapidly caresses the shaft between her tits"])
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 40, 15, 1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 2)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 4) 
        
    elif K_Tit > 1:                                                 #third through 5th time
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["She juggles her breasts up and down around your cock", 
                "She lightly strokes the head as it pops up between her tits", 
                "She has a smooth motion going now, gentle and precise",
                "She pauses to rub her nipples across the shaft",
                "She gently caresses the shaft between her tits"])            
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 60, 10)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)                 
        else:                                                       #fast
            $ Line = renpy.random.choice(["She rapidly juggles her breasts up and down around your cock", 
                "She lightly brushes the head with her chin as it pops up between her tits", 
                "She moves them up and down in a fluid rocking motion",
                "She bounces her whole body up and down",
                "She rapidly slides the shaft between her tits"])            
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 50, 8, 1)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 7) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 4) 

    
    else:                                                           #First and second time
        if Speed <= 1:                                              #slow
            $ Line = renpy.random.choice(["Kitty sort of squishes her breasts back and forth around your cock", 
                "She slides the cock up and down between her cleavage", 
                "She kind of bounces her tits around your cock",
                "She smooshes her cleavage as tight as she can and rubs up and down"])
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 60, 7)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 5) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 3)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)                 
        else:                                                       #fast
            $ Line = renpy.random.choice(["Kitty sort of bounces her breasts off your cock", 
                "She tries to quickly slide the cock up and down between her cleavage, but it tends to slide out", 
                "She slaps her tits against your dick",
                "She smooshes her cleavage as tight as she can and rubs up and down quite quickly"])            
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 60, 7)
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 200, 4) 
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 2)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3) 
    
    call Kitty_Offhand from _call_Kitty_Offhand_1                                                            #Offhand and reduce addiciton per stroke        
    $ K_Addict -= 2          
    
    if P_Focus >= 100 or K_Lust >= 100:                                     #If either of you could cum    
        if P_Focus >= 100:                                                  #You cum             
            call PK_Cumming from _call_PK_Cumming_15
            if "angry" in K_RecentActions:  
                call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_5
                return    
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
            if 100 > K_Lust >= 70 and K_OCount < 2:             
                $ K_RecentActions.append("unsatisfied")                      
                $ K_DailyActions.append("unsatisfied") 
            
            if P_Focus > 80:
                jump K_TJAfter   
        
        if K_Lust >= 100:                                                   #and Kitty cums                    
            call K_Cumming from _call_K_Cumming_24
            if Situation == "shift" or "angry" in K_RecentActions:
                jump K_TJAfter            
                        
        if P_Focus <= 20 or not P_Semen:
            if not P_Semen:
                "You're pretty wiped, better stop for now."
            $ Line = 0
            jump K_TJAfter     
     

    if Round:
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
        jump KTJ_Cycle  
    else: # You ran out of tries.
        call KittyFace("bemused", 0) from _call_KittyFace_795
        $ Line = 0
        ch_k "Ok, [K_Petname], that's enough of that for now."
        
label K_TJAfter:
    $ K_Tit += 1
    
    call KittyFace("sexy") from _call_KittyFace_796  
        
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1
        
    if K_Tit > 5:
        pass
    elif K_Tit == 1 and K_Love >= 500:
        $ K_Mouth = "smile"
        ch_k "Well, that was certainly interesting."
    elif K_Tit == 1 and P_Focus <= 20:
        $ K_Mouth = "sad"
        ch_k "Well, I hope that was enough for you."        
    elif K_Tit == 5:
        ch_k "I think I've got the goods for this."        
    if K_Tit == 1:
        $K_SEXP += 12
    
    $ Tempmod = 0    
    
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    else:
        call Kitty_TJ_Reset from _call_Kitty_TJ_Reset_6    
    call Checkout from _call_Checkout_80
    return

## end K_Titjob //////////////////////////////////////////////////////////////////////

# K_Blowjob //////////////////////////////////////////////////////////////////////

label K_Blowjob:
    call Shift_Focus("Kitty") from _call_Shift_Focus_210
    if K_Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif K_Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif K_Blow: #You've done it before
        $ Tempmod += 7    
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif K_Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no blow" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in K_RecentActions else 0    
    
    $ Approval = ApprovalCheck("Kitty", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            "Kitty slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)                     
                    "Kitty continues licking at it."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_797                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Hmmm, keep doing that, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_13
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":     
                    call KittyFace("surprised") from _call_KittyFace_798  
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_14
                    "Kitty puts it down."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    return            
            jump KBJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Blow and "no blow" not in K_RecentActions:        
        call KittyFace("surprised", 2) from _call_KittyFace_799
        $ K_Mouth = "kiss"
        ch_k "You want me to suck your dick?"
        if K_Hand:          
            $ K_Mouth = "smile"
            ch_k "Not satisfied with handies?"        
        $ K_Blush = 1
            
    if not K_Blow and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_800
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy") from _call_KittyFace_801
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I have wondered what you. . . taste like."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal") from _call_KittyFace_802
            ch_k "If you want me to. . ."               
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_803
            ch_k "My mouth is watering. . ."   
        else: # Uninhibited 
            call KittyFace("sad") from _call_KittyFace_804
            $ K_Mouth = "smile"             
            ch_k "[K_Like]sure. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_805
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "You want me to do that again?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."    
        elif "blow" in K_RecentActions:
            call KittyFace("sexy", 1) from _call_KittyFace_806
            ch_k "Mmm, again? [[stretches her jaw]"
            jump KBJ_Prep                
        elif "blow" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_807
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_k "[Line]"
        elif K_Blow < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_808
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another blowjob?"        
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_809
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you wanna 'nother blowjob?",                 
                "A little. . . lick?", 
                "You want me to suck you off?",
                "A little tlc?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_810
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Whatever."    
        elif "no blow" in K_DailyActions:               
            ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."  
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_811
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Lol, ok, alright."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 1)      
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
        jump KBJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_812
        if "no blow" in K_RecentActions:  
            ch_k "What did I[K_like]{i}just{/i} tell you [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no blow" in K_DailyActions:  
            ch_k "I told you, not in public!"  
        elif "no blow" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I told you this is too public!"      
        elif not K_Blow:
            call KittyFace("bemused") from _call_KittyFace_813
            ch_k "I don't know about the taste, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_814
            ch_k "Later, [K_Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_815
                ch_k "Aw, it's ok, [K_Petname]."              
                return
            "Maybe later?" if "no blow" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_816  
                ch_k "You[K_like]never know, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no blow")                      
                $ K_DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_817     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, I guess.",                 
                        "Well. . . ok.",                 
                        "I could maybe give it a try.", 
                        "I guess I could. . .",
                        "Fiiine. . . [She licks her lips].",
                        "Heh, ok, fine."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KBJ_Prep
                else:   
                    if ApprovalCheck("Kitty", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                        call KittyFace("confused", 1) from _call_KittyFace_818
                        $ K_Arms = 1
                        if K_Hand:
                            ch_k "Maybe I could just use my hand?"
                        else:
                            ch_k "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_k "Would that work?"
                            "Sure, that's fine.":
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)  
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)                                
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1) 
                                jump KHJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                                
                                $ K_Arms = 0                
                                ch_k "Ok, your loss."  
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)  
                    
                    
            "Suck it, [K_Pet]":                                               # Pressured into it                
                call Kitty_Namecheck from _call_Kitty_Namecheck_15
                $ Approval = ApprovalCheck("Kitty", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_819
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, fine. . ."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1
                    jump KBJ_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in K_DailyActions:
        call KittyFace("angry", 1) from _call_KittyFace_820
        ch_k "You can eat a dick, 'cos I'm not."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_821
        ch_k "I just can't do that!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)     
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
        $ K_RecentActions.append("no blow")                      
        $ K_DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_822          
        $ K_DailyActions.append("tabno") 
        ch_k "This is way too exposed!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)    
        return                
    elif K_Blow:
        call KittyFace("sad") from _call_KittyFace_823 
        ch_k "No, not this time."       
    else:
        call KittyFace("normal", 1) from _call_KittyFace_824
        ch_k "Nope."  
    $ K_RecentActions.append("no blow")                      
    $ K_DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label KBJ_Prep:   
    if renpy.showing("Kitty_HJ_Animation"):
        hide Kitty_HJ_Animation with easeoutbottom
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy") from _call_KittyFace_825
    if K_Forced:
        call KittyFace("sad") from _call_KittyFace_826
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Kitty_BJ_Launch("L") from _call_Kitty_BJ_Launch_12
    if not K_Blow:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -70)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 45)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 60) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 35)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 40)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_23
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_171
    call DrainWord("Kitty","no blow") from _call_DrainWord_172
    $ K_RecentActions.append("blow")                      
    $ K_DailyActions.append("blow")     

label KBJ_Cycle: #Repeating strokes  
    while Round >=0:
        call Shift_Focus("Kitty") from _call_Shift_Focus_211
        call Kitty_BJ_Launch from _call_Kitty_BJ_Launch_13    
        call KittyLust from _call_KittyLust_19   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
         
        if Cnt == (10 + K_Blow):
                $ K_Brows = "angry"        
                menu:
                    ch_k "I'm[K_like]totally worn out here. Can we do something else?"
                    "How about a Handy?" if K_Action and MultiAction:
                            $ Situation = "shift"
                            call K_BJAfter from _call_K_BJAfter_2
                            call K_Handjob from _call_K_Handjob_3 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump KBJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_3
                            $ Situation = "shift"
                            jump K_BJAfter
                    "No, get back down there.":
                            if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call KittyFace("angry", 1) from _call_KittyFace_827  
                                "She scowls at you, drops you cock and pulls back."
                                ch_k "Well fuck you then."
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")   
                                jump K_BJAfter        
        elif Cnt == (5 + K_Blow) and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Are you getting close here? I'm cramping up."  
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    if ("master" in K_Petnames or "sir" in K_Petnames or K_Pet == "slave") and ApprovalCheck("Kitty", 750, "O") and not K_Bondage: # bondage event
                        $ K_Bondage = 1
                        ch_k "Hey, [K_Petname], I've got some new things here, do you think we could try them?"
                        "She grabs what it looks like some bondage gear"
                        menu:
                            "Yep":
                                call KittyFace("sexy", 1) from _call_KittyFace_828 
                                if K_Over or K_Chest or K_Panties or K_Legs:
                                    "She glances up at you as her clothes drop to the ground."
                                $ K_Over = 0
                                $ K_Legs = 0
                                $ K_Chest = 0
                                $ K_Panties = 0
                                "She starts dressing the new outfit"
                                "You help her with the armbinder, making sure she can't move her arms"
                                "And add a blindfold so she can't see a thing"
                                $ K_Blindfold = 1
                                $ K_Over = "armbinder"
                                $ K_Chest = "bustier bra"
                                $ K_Panties = "zipper panties"
                                $ K_Outfit = "zipper bondage"
                                $ K_Shame = K_OutfitShame[1]
                                #if K_Over == "armbinder":
                                #call KittyFace("sly")
                                $ Line = "Kitty can't see a thing. She licks her lips in anticipation"
                                $ TempLust += 3 if K_Lust < 40 else 1  

                                if K_Blow <= 1 or (K_Obed >= 500 and K_Obed > K_Inbt):
                                        $ TempLust += 2 if K_Lust > 60 else 0                 
                                        $ Line = Line + ", but she seems to be waiting for some instruction"
                                else:
                                        $ Line = Line + ", and then she gets started licking your cock"
                                #        $ Speed = 1
                                #jump K_HotdogPrep
                                #pass
                                #call Kitty_Bottoms_Off_Legs
                                #call Kitty_Top_Off
                                #call Kitty_Bottoms_Off
                                #shes gonna wear it
                            "Not now, but let's save it for another time":
                                pass
                                #nope
                    menu:
                        "[Line]"
                        "Keep going. . ." if Speed:
                                pass
                            
                        "Lick it. . ." if Speed != 1:
                                $ Speed = 1   
                        "Lick it. . . (locked)" if Speed == 1:
                                pass  
                            
                        "Just the head. . ." if Speed != 2:
                            $ Speed = 2
                        "Just the head. . . (locked)" if Speed == 2:
                                pass
                            
                        "Suck on it." if Speed != 3:
                                $ Speed = 3  
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."
                                    
                        "Suck on it. (locked)" if Speed == 3:
                                pass
                            
                        "Take it deeper." if Speed != 4:
                                if "pushed" not in K_RecentActions and K_Blow < 5:
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -(20-(2*K_Blow))) 
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, (30-(3*K_Blow)))
                                    $ K_RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Kitty hums contentedly."    
                                if "setpace" not in K_RecentActions:
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if K_Blow < 5:
                                    $ D20 -= 10
                                elif K_Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in K_RecentActions:      
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                elif D20 > 5:
                                    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ K_RecentActions.append("setpace")
                        "Hold her head" if not P_Hands:
                                $ P_Hands = 1
                                "You hold her head"

                        "No hands" if P_Hands:
                                $ P_Hands = 0
                                "You let go of her head"

                        "How about you put that bondage outfit" if K_Bondage and K_Outfit != "zipper bondage" and K_Outfit != "zipper bondage open":
                            call KittyFace("sexy", 1) from _call_KittyFace_829 
                            if K_Over or K_Chest or K_Panties or K_Legs:
                                "She glances up at you as her clothes drop to the ground."
                            $ K_Over = 0
                            $ K_Legs = 0
                            $ K_Chest = 0
                            $ K_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the armbinder, making sure she can't move her arms"
                            "And add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
                            $ K_Over = "armbinder"
                            $ K_Chest = "bustier bra"
                            $ K_Panties = "zipper panties"
                            $ K_Outfit = "zipper bondage"
                            $ K_Shame = K_OutfitShame[1]

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_830 
                            #if K_Over or K_Chest or K_Panties or K_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ K_Neck = 0
                            #$ K_Over = 0
                            #$ K_Legs = 0
                            #$ K_Chest = 0
                            #$ K_Panties = 0
                            #"She starts dressing the new outfit"
                            #"You help her with the armbinder, making sure she can't move her arms"
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
                            #$ K_Over = "armbinder"
                            #$ K_Chest = "bustier bra"
                            #$ K_Panties = "zipper panties"
                            #$ K_Outfit = "zipper bondage"
                            #$ K_Shame = K_OutfitShame[1]

                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_831 
                            #if K_Over or K_Chest or K_Panties or K_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ K_Neck = 0
                            #$ K_Over = 0
                            #$ K_Legs = 0
                            #$ K_Chest = 0
                            #$ K_Panties = 0
                            #"She starts dressing the new outfit"
                            #"You help her with the armbinder, making sure she can't move her arms"
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                            #$ K_Over = "armbinder"
                            #$ K_Chest = "bustier bra"
                            #$ K_Panties = "zipper panties"
                            #$ K_Outfit = "zipper bondage"
                            #$ K_Shame = K_OutfitShame[1]
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_19  
                                    
                        "Shift actions":
                            menu:
                                "How about a handy?":
                                        if K_Action and MultiAction:
                                            if  K_Over == "armbinder":
                                                call KittyFace("sexy", 1) from _call_KittyFace_832
                                                ch_k "I can't do that with my arms like this [K_Petname]"
                                                "You untie her arms and removes her blindfold"
                                                $ K_Over = 0
                                                $ K_Blindfold = 0
                                                if K_Chest or K_Pants or K_Panties:
                                                    "She drops the rest of her clothes"
                                                    $ K_Chest = 0
                                                    $ K_Pants = 0
                                                    $ K_Panties = 0
                                                    $ K_Outfit = "nude"
                                            $ Situation = "shift"
                                            call K_BJAfter from _call_K_BJAfter_3
                                            call K_Handjob from _call_K_Handjob_4
                                        else:
                                            ch_k "I'm kinda tired, could we just wrap this up. . ."
                                "How about a titjob?":
                                        if K_Action and MultiAction:
                                            $ Situation = "shift"
                                            call K_BJAfter from _call_K_BJAfter_4
                                            call K_Titjob from _call_K_Titjob
                                        else:
                                            ch_k "I'm kinda tired, could we just wrap this up. . ."
                        
                                        
                        "I also want to fondle her breasts.":
                                if K_Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    "You start to fondle her breasts."
                                    $ K_Action -= 1
                                else:
                                    ch_k "I'm kinda tired, could we just wrap this up?"  
                                         
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_4
                                $ Situation = "shift"
                                jump K_BJAfter
                        "Let's stop for now." if not MultiAction: 
                                $ Line = 0
                                call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_5
                                jump K_BJAfter 
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_52
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_16
                            if "angry" in K_RecentActions:  
                                call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_6
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_BJAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                                                
                            call K_Cumming from _call_K_Cumming_25
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_BJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump K_BJAfter   
                
        #End orgasm
        
   
        if Round == 10:
            ch_k "Could we[K_like]wrap this up?"  
        elif Round == 5:
            ch_k "Seriously, I need a break."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_833
    $ Line = 0
    ch_k "Ok, I gotta rest me jaw for a minute. . ."

label K_BJAfter:    
    call KittyFace("sexy") from _call_KittyFace_834  
        
    $ K_Blow += 1
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1
                
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions:
            $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
            
    if "Kitty Jobber" in Achievements:
        pass
    elif K_Blow >= 10:
        call KittyFace("smile", 1) from _call_KittyFace_835
        ch_k "I can't[K_like]get your taste out of my mind."      
        $ Achievements.append("Kitty Jobber")
        $K_SEXP += 5
    elif Situation == "shift":
        pass
    elif K_Blow == 1:
            $K_SEXP += 15
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "Huh, that wasn't bad."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "I hope you enjoyed that."     
    elif K_Blow == 5:
        ch_k "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                call KittyFace("smile", 1) from _call_KittyFace_836
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Kitty", 500, "O"):
                    call KittyFace("sad", 2) from _call_KittyFace_837
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                else:
                    call KittyFace("angry", 2) from _call_KittyFace_838
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -25)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                ch_k ". . ."         
                call KittyFace("sad", 1) from _call_KittyFace_839
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Kitty_BJ_Reset from _call_Kitty_BJ_Reset_7    
    call Checkout from _call_Checkout_81
    return
    


# end K_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label K_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in K_Inventory:
        "You ask Kitty to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label K_Dildo_Pussy:
    call Shift_Focus("Kitty") from _call_Shift_Focus_212
    call K_Dildo_Check from _call_K_Dildo_Check    
    if not _return:
        return 

    if K_DildoP: #You've done it before
        $ Tempmod += 15
    if K_Legs == "pants": # she's got pants on.
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
        
    if "no dildo" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in K_RecentActions else 0       
        
    $ Approval = ApprovalCheck("Kitty", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
                if Approval > 2:                                                      # fix, add kitty auto stuff here
                    if K_Legs == "skirt":
                        "Kitty grabs her dildo, hiking up her skirt as she does."
                        $ K_Upskirt = 1
                    elif K_Legs == "pants":
                        "Kitty grabs her dildo, pulling down her pants as she does."              
                        $ K_Legs = 0
                    else:
                        "Kitty grabs her dildo, rubbing is suggestively against her crotch."
                    $ K_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                            "Kitty slides it in."
                        "Go for it.":       
                            call KittyFace("sexy, 1") from _call_KittyFace_840                    
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                            ch_p "Oh yeah, [K_Pet], let's do this."
                            call Kitty_Namecheck from _call_Kitty_Namecheck_16
                            "You grab the dildo and slide it in."
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        "Ask her to stop.":
                            call KittyFace("surprised") from _call_KittyFace_841       
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [K_Pet]."
                            call Kitty_Namecheck from _call_Kitty_Namecheck_17
                            "Kitty sets the dildo down."
                            call KittyOutfit from _call_KittyOutfit_37
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                            return            
                    jump KDP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add kitty auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call KittyFace("surprised", 1) from _call_KittyFace_842
                
                if (K_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call KittyFace("sexy") from _call_KittyFace_843
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_k "Ooo, [K_Petname], toys!"            
                    jump KDP_Prep         
                else:                                                                                                            #she's questioning it
                    $ K_Brows = "angry"                
                    menu:
                        ch_k "Hey, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call KittyFace("sexy", 1) from _call_KittyFace_844
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                                ch_k "Well, now that you mention it. . ."
                                jump KDP_Prep
                            "You pull back before you really get it in."                    
                            call KittyFace("bemused", 1) from _call_KittyFace_845
                            if K_DildoP:
                                ch_k "Well ok, [K_Petname], maybe warn me next time?" 
                            else:
                                ch_k "Well ok, [K_Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                            "You press it inside some more."                              
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            if not ApprovalCheck("Kitty", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call KittyFace("angry") from _call_KittyFace_846
                                "Kitty shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "Ask nice if you want to stick something in my ass!"                                               
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Kitty_SexSprite"):
                                    call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_24 
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")                          
                            else:
                                call KittyFace("sad") from _call_KittyFace_847
                                "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump KDP_Prep
                return             
    #end Auto
   
    if not K_DildoP:                                                               
            #first time    
            call KittyFace("surprised", 1) from _call_KittyFace_848
            $ K_Mouth = "kiss"
            ch_k "Hmmm, so you'd like to try out some toys?"    
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_849
                ch_k "I suppose there are worst things you could ask for."
            
    if not K_DildoP and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_850
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy") from _call_KittyFace_851
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I've had a reasonable amount of experience with these, you know. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal") from _call_KittyFace_852
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad") from _call_KittyFace_853
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_854
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "The toys again?" 
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in K_RecentActions:
                call KittyFace("sexy", 1) from _call_KittyFace_855
                ch_k "Mmm, again? Ok, let's get to it."
                jump KDP_Prep
            elif "dildo pussy" in K_DailyActions:
                call KittyFace("sexy", 1) from _call_KittyFace_856
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoP < 3:        
                call KittyFace("sexy", 1) from _call_KittyFace_857
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my again?"       
            else:       
                call KittyFace("sexy", 1) from _call_KittyFace_858
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_k "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_859
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            else:
                call KittyFace("sexy", 1) from _call_KittyFace_860
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
            jump KDP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry") from _call_KittyFace_861
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"   
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "Stop swinging that thing around in public!"  
            elif not K_DildoP:
                call KittyFace("bemused") from _call_KittyFace_862
                ch_k "I'm just not into toys, [K_Petname]. . ."
            else:
                call KittyFace("bemused") from _call_KittyFace_863
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused") from _call_KittyFace_864
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy") from _call_KittyFace_865  
                    ch_k "Maybe I'll practice on my own time, [K_Petname]."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)  
                    if Taboo:                    
                        $ K_RecentActions.append("tabno")                      
                        $ K_DailyActions.append("tabno") 
                    $ K_RecentActions.append("no dildo")                      
                    $ K_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call KittyFace("sexy") from _call_KittyFace_866     
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump KDP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad") from _call_KittyFace_867
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                        ch_k "Ok, fine. If we're going to do this, stick it in already."  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                        $ K_Forced = 1  
                        jump KDP_Prep
                    else:                              
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)     
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1  
    if "no dildo" in K_DailyActions:
            ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif K_Forced:
            call KittyFace("angry", 1) from _call_KittyFace_868
            ch_k "I'm not going to let you use that on me."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)     
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1) from _call_KittyFace_869         
            $ K_RecentActions.append("tabno")                       
            $ K_DailyActions.append("tabno") 
            ch_k "Not here!"     
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_DildoP:
            call KittyFace("sad") from _call_KittyFace_870 
            ch_k "Sorry, you can keep your toys to yourself."     
    else:
            call KittyFace("normal", 1) from _call_KittyFace_871
            ch_k "No way."  
    $ K_RecentActions.append("no dildo")                      
    $ K_DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label KDP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 15 if K_Legs == "pants" else 0           
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_12
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo pussy") from _call_K_Pussy_Launch_13
    if not K_DildoP:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -75)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 60)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 45)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_173
    call DrainWord("Kitty","no dildo") from _call_DrainWord_174
    $ K_RecentActions.append("dildo pussy")                      
    $ K_DailyActions.append("dildo pussy") 
    
label KDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_213 
        call K_Pussy_Launch("dildo pussy") from _call_K_Pussy_Launch_14
        call KittyLust from _call_KittyLust_20   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + K_DildoP):
                    $ K_Brows = "confused"
                    ch_k "What are you even doing down there?" 
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_DildoP) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KDP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KDP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_872   
                                    call K_Pos_Reset from _call_K_Pos_Reset_50
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KDP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                                           
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_12
                                jump KDP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_873 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_874 
                            "You remove the blindfold"
                            $ K_Blindfold = 0

                        
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_20  
                                    
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her ass.":
                                                    $ Situation = "shift"
                                                    call KDP_After from _call_KDP_After_1
                                                    call K_Insert_Ass from _call_K_Insert_Ass_5    
                                            "Just stick a finger in her ass without asking.":
                                                    $ Situation = "auto"
                                                    call KDP_After from _call_KDP_After_2
                                                    call K_Insert_Ass from _call_K_Insert_Ass_6                                           
                                            "I want to shift the dilso to her ass.":
                                                    $ Situation = "shift"
                                                    call KDP_After from _call_KDP_After_3
                                                    call K_Dildo_Ass from _call_K_Dildo_Ass_1   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_19
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KDP_After from _call_KDP_After_4
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_20   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_51
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDP_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_52
                                    $ Line = 0
                                    jump KDP_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto") from _call_K_Undress_21
            
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_53
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_17
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_53
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KDP_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_26
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KDP_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                            "Kitty still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump KDP_After
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_875
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    
label KDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_54
        
    call KittyFace("sexy") from _call_KittyFace_876 
    
    $ K_DildoP += 1  
    $ K_Action -=1   
        
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_DildoP == 1:            
            $ K_SEXP += 10         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Thanks for the extra hand. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_877
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_82
    return   

# end K_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label K_Dildo_Ass:
    call Shift_Focus("Kitty") from _call_Shift_Focus_214
    call K_Dildo_Check from _call_K_Dildo_Check_1
    if not _return:
        return 
      
    if K_Loose:
        $ Tempmod += 30   
    elif "anal" in K_RecentActions or "dildo anal" in K_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in K_DailyActions or "dildo anal" in K_DailyActions:
        $ Tempmod -= 10
    elif (K_Anal + K_DildoA + K_Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if K_Legs == "pants": # she's got pants on.
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
        
    if "no dildo" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in K_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Kitty", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Kitty":                                                                  
            #Kitty auto-starts   
            if Approval > 2:                                                      # fix, add kitty auto stuff here
                if K_Legs == "skirt":
                    "Kitty grabs her dildo, hiking up her skirt as she does."
                    $ K_Upskirt = 1
                elif K_Legs == "pants":
                    "Kitty grabs her dildo, pulling down her pants as she does."              
                    $ K_Legs = 0
                else:
                    "Kitty grabs her dildo, rubbing is suggestively against her ass."
                $ K_SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)
                        "Kitty slides it in."
                    "Go for it.":       
                        call KittyFace("sexy, 1") from _call_KittyFace_878                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        ch_p "Oh yeah, [K_Pet], let's do this."
                        call Kitty_Namecheck from _call_Kitty_Namecheck_18
                        "You grab the dildo and slide it in."
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised") from _call_KittyFace_879       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck from _call_Kitty_Namecheck_19
                        "Kitty sets the dildo down."
                        call KittyOutfit from _call_KittyOutfit_38
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                        return            
                jump KDA_Prep
            else:                
                $ Tempmod = 0                               # fix, add kitty auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call KittyFace("surprised", 1) from _call_KittyFace_880
            
            if (K_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call KittyFace("sexy") from _call_KittyFace_881
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1)
                ch_k "Ooo, [K_Petname], toys!"                
                jump KDA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ K_Brows = "angry"                
                menu:
                    ch_k "Hey, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call KittyFace("sexy", 1) from _call_KittyFace_882
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_k "Well, now that you mention it. . ."
                            jump KDA_Prep
                        "You pull back before you really get it in."                    
                        call KittyFace("bemused", 1) from _call_KittyFace_883
                        if K_DildoA:
                            ch_k "Well ok, [K_Petname], maybe warn me next time?" 
                        else:
                            ch_k "Well ok, [K_Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -10, 1)  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                        "You press it inside some more."                              
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                        if not ApprovalCheck("Kitty", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call KittyFace("angry") from _call_KittyFace_884
                            "Kitty shoves you away and slaps you in the face."
                            ch_k "Jerk!"
                            ch_k "Ask nice if you want to stick something in my ass!"                                                  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Kitty_SexSprite"):
                                call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_25 
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                         
                        else:
                            call KittyFace("sad") from _call_KittyFace_885
                            "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump KDA_Prep
            return             
    #end auto
   
    if not K_DildoA:                                                               
            #first time    
            call KittyFace("surprised", 1) from _call_KittyFace_886
            $ K_Mouth = "kiss"
            ch_k "You want to try and fit that. . .?"    
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_887
                ch_k "Always about the but, huh?"
    
    if not K_Loose and ("dildo anal" in K_RecentActions or "anal" in K_RecentActions or "dildo anal" in K_DailyActions or "anal" in K_DailyActions):
            call KittyFace("bemused", 1) from _call_KittyFace_888
            ch_k "I'm still[K_like]sore from earlier. . ."
            
    if not K_DildoA and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_889
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy") from _call_KittyFace_890
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I[K_like]haven't actually used one of these, back there before. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal") from _call_KittyFace_891
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad") from _call_KittyFace_892
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad") from _call_KittyFace_893
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "The toys again?"  
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in K_DailyActions and not K_Loose:
                pass
            elif "dildo anal" in K_DailyActions:
                call KittyFace("sexy", 1) from _call_KittyFace_894
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoA < 3:        
                call KittyFace("sexy", 1) from _call_KittyFace_895
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my ass again?"       
            else:       
                call KittyFace("sexy", 1) from _call_KittyFace_896
                $ Kitty_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_k "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if K_Forced:
                call KittyFace("sad") from _call_KittyFace_897
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            else:
                call KittyFace("sexy", 1) from _call_KittyFace_898
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
            jump KDA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call KittyFace("angry") from _call_KittyFace_899
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"  
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you that I wouldn't do that out here!"  
            elif not K_DildoA:
                call KittyFace("bemused") from _call_KittyFace_900
                ch_k "I'm just not into toys, [K_Petname]. . ."
            elif not K_Loose and "dildo anal" not in K_DailyActions:
                call KittyFace("perplexed") from _call_KittyFace_901
                ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
            else:
                call KittyFace("bemused") from _call_KittyFace_902
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused") from _call_KittyFace_903
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy") from _call_KittyFace_904  
                    ch_k "Maybe I'll practice on my own time, [K_Petname]."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)  
                    if Taboo:                    
                        $ K_RecentActions.append("tabno")                      
                        $ K_DailyActions.append("tabno") 
                    $ K_RecentActions.append("no dildo")                      
                    $ K_DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call KittyFace("sexy") from _call_KittyFace_905     
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_k "[Line]"
                        $ Line = 0                   
                        jump KDA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Kitty", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and K_Forced):
                        call KittyFace("sad") from _call_KittyFace_906
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)                 
                        ch_k "Ok, fine. If we're going to do this, stick it in already."  
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 4)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                        $ K_Forced = 1  
                        jump KDA_Prep
                    else:                              
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)    
                        $ K_RecentActions.append("angry")
                        $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1   
    if "no dildo" in K_DailyActions:
            ch_k "Learn to take \"no\" for an answer, [K_Petname]."   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif K_Forced:
            call KittyFace("angry", 1) from _call_KittyFace_907
            ch_k "I'm not going to let you use that on me."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1) from _call_KittyFace_908          
            $ K_RecentActions.append("tabno")                       
            $ K_DailyActions.append("tabno") 
            ch_k "Not here!"     
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif not K_Loose and "dildo anal" in K_DailyActions:
            call KittyFace("bemused") from _call_KittyFace_909
            ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_DildoA:
            call KittyFace("sad") from _call_KittyFace_910 
            ch_k "Sorry, you can keep your toys out of there."     
    else:
            call KittyFace("normal", 1) from _call_KittyFace_911
            ch_k "No way." 
    $ K_RecentActions.append("no dildo")                      
    $ K_DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label KDA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 20 if K_Legs == "pants" else 0           
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_13
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo anal") from _call_K_Pussy_Launch_15
    if not K_DildoA:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -75)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 60)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 45)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_175
    call DrainWord("Kitty","no dildo") from _call_DrainWord_176
    $ K_RecentActions.append("dildo anal")                      
    $ K_DailyActions.append("dildo anal") 
    
label KDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_215 
        call K_Pussy_Launch("dildo anal") from _call_K_Pussy_Launch_16
        call KittyLust from _call_KittyLust_21   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + K_DildoA):
                    $ K_Brows = "confused"
                    ch_k "What are you even doing down there?" 
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_DildoA) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KDA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KDA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_912   
                                    call K_Pos_Reset from _call_K_Pos_Reset_55
                                    "She scowls at you and pulls back."
                                    ch_k "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KDA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                    
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_13
                                jump KDA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_913 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_914 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                        
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_22  
                                                            
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her pussy.":
                                                    $ Situation = "shift"
                                                    call KDA_After from _call_KDA_After_1
                                                    call K_Fondle_Pussy from _call_K_Fondle_Pussy_5    
                                            "Just stick a finger in her pussy without asking.":
                                                    $ Situation = "auto"
                                                    call KDA_After from _call_KDA_After_2
                                                    call K_Fondle_Pussy from _call_K_Fondle_Pussy_6                                           
                                            "I want to shift the dilso to her pussy.":
                                                    $ Situation = "shift"
                                                    call KDA_After from _call_KDA_After_3
                                                    call K_Dildo_Pussy from _call_K_Dildo_Pussy_1   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_21
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KDA_After from _call_KDA_After_4
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_22   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_56
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDA_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_57
                                    $ Line = 0
                                    jump KDA_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto") from _call_K_Undress_23
            
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_54
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_18
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_58
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KDA_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_27
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KDA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in K_RecentActions:#And Kitty is unsatisfied,  
                            "Kitty still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump KDA_After
        #End orgasm
        
   
        if Round == 10:
            ch_k "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_k "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_915
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    
label KDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_59
        
    call KittyFace("sexy") from _call_KittyFace_916 
    
    $ K_DildoA += 1  
    $ K_Action -=1            
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_DildoA == 1:            
            $ K_SEXP += 10         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    if K_Loose:
                        ch_k "That was. . . interesting. . ."
                    else:
                        ch_k "Ouch. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_917
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_83
    return   

# end K_Dildo Ass /////////////////////////////////////////////////////////////////////////////

label K_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in K_Inventory:
        "You ask Kitty to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
## K_Footjob //////////////////////////////////////////////////////////////////////
label K_Footjob:
    $ K_LegsUp = 0
    call Shift_Focus("Kitty") from _call_Shift_Focus_216
    if K_Foot >= 7: # She loves it
        $ Tempmod += 10
    elif K_Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif K_Foot: #You've done it before
        $ Tempmod += 3
        
    if K_Addict >= 75 and K_Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if K_Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
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
        
    if "no foot" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in K_RecentActions else 0    
        
    $ Approval = ApprovalCheck("Kitty", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Kitty":                                                                  #Kitty auto-starts   
        if Approval > 2:                                                      # fix, add kitty auto stuff here
            if Trigger2 == "jackin":
                "Kitty leans and starts rubbing your cock between her feet."
            else:
                "Kitty gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)                     
                    "Kitty continues her actions."
                "Praise her.":       
                    call KittyFace("sexy, 1") from _call_KittyFace_918                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_20
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised") from _call_KittyFace_919       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck from _call_Kitty_Namecheck_21
                    "Kitty puts it down."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump KFJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Foot and "no foot" not in K_RecentActions:        
        call KittyFace("confused", 2) from _call_KittyFace_920
        ch_k "Huh, so you'd like me to touch your cock with my feet?"
        $ K_Blush = 1
            
    if not K_Foot and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1) from _call_KittyFace_921
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1) from _call_KittyFace_922
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it couldn't hurt. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1) from _call_KittyFace_923
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1) from _call_KittyFace_924
            ch_k "Okay. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1) from _call_KittyFace_925    
            ch_k "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_926
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's all?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Um, I guess this is secluded enough. . ."    
        elif "foot" in K_RecentActions:
            call KittyFace("sexy", 1) from _call_KittyFace_927
            ch_k "I'm getting foot cramps. . ."
            jump KFJ_Prep
        elif "foot" in K_DailyActions:
            call KittyFace("sexy", 1) from _call_KittyFace_928
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Foot < 3:        
            call KittyFace("sexy", 1) from _call_KittyFace_929
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic toes. . ."        
        else:       
            call KittyFace("sexy", 1) from _call_KittyFace_930
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_931
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine." 
        elif "no foot" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_932
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ooooookay.",                 
                "Cool, lemme see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_k "[Line]"
            $ Line = 0
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump KFJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry") from _call_KittyFace_933
        if "no foot" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no foot" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no foot" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Foot:
            call KittyFace("bemused") from _call_KittyFace_934
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_935
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_936
                ch_k "Yeah."              
                return
            "Maybe later?" if "no foot" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_937  
                ch_k ". . ."
                ch_k "Maybe."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no foot")                      
                $ K_DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_938     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Ooooookay.",                 
                            "Cool, lemme see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_k "[Line]"
                    $ Line = 0                   
                    jump KFJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Kitty", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_939
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, fine."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    $ K_Forced = 1  
                    jump KFJ_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)     
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Kitty_Arms = 1 
    if "no foot" in K_DailyActions:
        call KittyFace("angry", 1) from _call_KittyFace_940
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_941
        ch_k "I don't even want to step on it."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1) from _call_KittyFace_942          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)   
    elif K_Foot:
        call KittyFace("sad") from _call_KittyFace_943 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1) from _call_KittyFace_944
        ch_k "I don't know about using my feet for. . . that."  
    $ K_RecentActions.append("no foot")                      
    $ K_DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label KFJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
                
    call KittyFace("sexy") from _call_KittyFace_945
    if K_Forced:
        call KittyFace("sad") from _call_KittyFace_946
    elif K_Foot:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    if not K_Foot:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)     
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_24
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_177
    call DrainWord("Kitty","no foot") from _call_DrainWord_178
    $ K_RecentActions.append("foot")                      
    $ K_DailyActions.append("foot") 
  
label KFJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Kitty") from _call_Shift_Focus_217
        call Kitty_Sex_Launch("foot") from _call_Kitty_Sex_Launch_16
#        call Kitty_FJ_Launch    #fix, change to sex launch with foot
        call KittyLust from _call_KittyLust_22   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, foot cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_FJAfter from _call_K_FJAfter
                                call K_Blowjob from _call_K_Blowjob_8   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_FJAfter from _call_K_FJAfter_1
                                call K_Handjob from _call_K_Handjob_5  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump KFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_26
                                $ Situation = "shift"
                                jump K_FJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_947   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_k "Hey, I've got better things to do if you're[K_like]going to be a dick about it."                                               
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)                     
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump K_FJAfter
        elif Cnt == 10 and K_SEXP <= 100 and not ApprovalCheck("Kitty", 1200, "LO"):
                    $ K_Brows = "confused"
                    ch_k "Can we[K_Like]be done with this now? I'm getting sore."         
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

                        "Blindfold her" if K_Bondage and not K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_948 
                            "You add a blindfold so she can't see a thing"
                            $ K_Blindfold = 1
            
                        "Remove blindfold" if K_Blindfold:
                            call KittyFace("sexy", 1) from _call_KittyFace_949 
                            "You remove the blindfold"
                            $ K_Blindfold = 0
                   
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_24  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_FJAfter from _call_K_FJAfter_2                
                                                call K_Blowjob from _call_K_Blowjob_9
                                            else:
                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                "How about a handjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_FJAfter from _call_K_FJAfter_3                
                                                call K_Handjob from _call_K_Handjob_6
                                            else:
                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                                
#                                "How about a titjob?":
#                                            if K_Action and MultiAction:
#                                                $ Situation = "shift"
#                                                call K_FJAfter
#                                                call K_Titjob
#                                            else:
#                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                        
#                        "I also want to fondle her breasts." if K_Action and MultiAction:
#                                    $ Trigger2 = "fondle breasts"
#                                    $ Situation = "auto"
#                                    call K_Fondle_Breasts
#                                    if Trigger2:
#                                         $ K_Action -= 1
                                         
                        "I also want to. . . [[Offhand]": #fix set this up
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_23
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                                    
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_27
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_FJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_28
                                    $ Line = 0
                                    jump K_FJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_55
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_19
                            if "angry" in K_RecentActions:  
                                call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_29
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump K_FJAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                                                
                            call K_Cumming from _call_K_Cumming_28
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump K_FJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump K_FJAfter   
                
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's kind of time to get moving."   
        elif Round == 5:
            ch_k "For real[K_like]time's up."      
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_950
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label K_FJAfter:
    call KittyFace("sexy") from _call_KittyFace_951 
    
    $ K_Foot += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5)
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ R_LikeKitty += 1
    
    if "Kittypedi" in Achievements:
            pass  
    elif K_Foot >= 10:
            call KittyFace("smile", 1) from _call_KittyFace_952
            ch_k "I guess I've gotten pretty smooth at the \"Kittypedi.\""
            $ Achievements.append("Kittypedi")
            $ K_SEXP += 5          
    elif K_Foot == 1:            
            $ K_SEXP += 10
            if K_Love >= 500:
                $ K_Mouth = "smile"
                ch_k "I could feel you down there. . ."
            elif P_Focus <= 20:
                $ K_Mouth = "sad"
                ch_k "Did that work out for you?"
    elif K_Foot == 5:
                ch_k "Let me know any time you need me to \"foot you up.\""                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, so what were you thinking?"
    else:
        call Kitty_Sex_Reset from _call_Kitty_Sex_Reset_30    
    call Checkout from _call_Checkout_84
    return

## end K_Footjob //////////////////////////////////////////////////////////////////////


label K_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call K_Les_Response("Rogue",1)
        if K_Les:
            $ Tempmod += 10
        if K_SEXP >= 50:
            $ Tempmod += 25
        elif K_SEXP >= 30:
            $ Tempmod += 15
        elif K_SEXP >= 15:
            $ Tempmod += 5
                    
        elif K_Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in K_Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in K_Traits or "sex friend" in K_Petnames:
            $ Tempmod += 10        
        elif "ex" in K_Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if K_LikeRogue >= 900:
                        $ B += 150
                elif K_LikeRogue >= 800 or "poly rogue" in K_Traits:
                        $ B += 100
                elif K_LikeRogue >= 700:
                        $ B += 50
                elif K_LikeRogue <= 200:
                        $ B -= 200
                elif K_LikeRogue <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Kitty", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Kitty likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call KittyFace("sexy", 1) from _call_KittyFace_953
                ch_k "Aw, come on [Girl], wouldn't it be fun?"
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ K_LikeRogue += (int(B/10))
                            $ R_LikeKitty += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call KittyFace("smile", 1) from _call_KittyFace_954
                ch_k "Sure, sounds fun!"
                $ Result = 1
            elif Approval:
                call KittyFace("sly", 2) from _call_KittyFace_955
                if B >= 100:
                        ch_k "I kinda want to, but I don't know. . ."
                if B >= 0:
                        ch_k "I don't know about doing it with her. . ."
                $ K_Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_k "You know what? I'm in."
                                $ Result = 1
                            else:
                                call KittyFace("smile") from _call_KittyFace_956
                                ch_k "Thanks, that's[K_like]really cool of you."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_k "Well, I guess I might." 
                                $ Result = 1
                            else:
                                call KittyFace("sad", 2) from _call_KittyFace_957
                                ch_k "I don't think so." 
                    "Get in there, now.":
                            if ApprovalCheck("Kitty", 550, "OI", TabM = 2):
                                call KittyFace("sadside", 1) from _call_KittyFace_958
                                ch_k "Ok, FINE."
                                $ Result = 1
                            else:
                                call KittyFace("angry") from _call_KittyFace_959
                                ch_k "Like hell I will."  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1) from _call_RogueFace_860
                                if R_Les and K_Les:
                                        ch_r "Come on Kitty, don't we have fun?"
                                else:
                                        ch_r "Come on Kitty, couldn't it be fun?"
                                $ K_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeKitty += 5
                            if B >= 50:
                                call KittyFace("smile", 1) from _call_KittyFace_960
                                ch_k "Heh, I guess you're right, [Girl]."
                                $ Result = 1
                            else:
                                call KittyFace("angry", 1, Eyes="side") from _call_KittyFace_961
                                ch_k "Yeah, no, I really don't think so."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call KittyFace("smile", 1) from _call_KittyFace_962
                            ch_k "Yeah, I mean I guess we could. . ."
                            $ Result = 1
                    else:
                            call KittyFace("sadside", 1) from _call_KittyFace_963
                            ch_k "I don't think I could manage that. . ."
            
            if not Result:      
                #no approval
                $ K_RecentActions.append("no lesbian")                      
                $ K_DailyActions.append("no lesbian") 
                call KittyFace("sadside", 1) from _call_KittyFace_964
                if B <= 0:
                    ch_k "I'm sorry, [K_Petname], I just can't do that with her."
                if Taboo:
                    ch_k "I'm sorry, [K_Petname], I just can't do that around here."
                if B >= 100:
                    ch_k "I'm sorry, [K_Petname], I just can't do that with you around."
                else:
                    ch_k "I'm sorry, [K_Petname], I just can't do that."
                
        return Result
#End K_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >