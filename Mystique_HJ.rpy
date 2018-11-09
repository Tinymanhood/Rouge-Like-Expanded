## Mystique_Handjob //////////////////////////////////////////////////////////////////////
label Mystique_Handjob:
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Hand >= 7: # She loves it
        $ Tempmod += 10
    elif newgirl["Mystique"].Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif newgirl["Mystique"].Hand: #You've done it before
        $ Tempmod += 3
        
    if newgirl["Mystique"].Addict >= 75 and newgirl["Mystique"].Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if newgirl["Mystique"].Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (3*Taboo)    
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40 
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount    
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no hand" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in newgirl["Mystique"].RecentActions else 0    
        
    $ Approval = ApprovalCheck("Mystique", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
        if Approval > 2:                                                      # fix, add Mystique auto stuff here
            if Trigger2 == "jackin":
                "Mystique brushes your hand aside and starts stroking your cock."
            else:
                "Mystique gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)                     
                    "Mystique continues her actions."
                "Praise her.":       
                    call MystiqueFace("sexy, 1")                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique continues her actions."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                "Ask her to stop.":
                    call MystiqueFace("surprised")       
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique puts it down."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump MystiqueHJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
            return            
    
    if not newgirl["Mystique"].Hand and "no hand" not in newgirl["Mystique"].RecentActions:        
        call MystiqueFace("confused", 2)
        ch_m "So you want a handjob?"
        $ newgirl["Mystique"].Blush = 1
            
    if not newgirl["Mystique"].Hand and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad",1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy",1)
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "I guess it could be an interesting experiment. . ."            
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal",1)
            ch_m "If you want, [newgirl[Mystique].Petname]. . ."            
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "I think i {i}need{/i} to. . ."  
        else: # Uninhibited 
            call MystiqueFace("lipbite",1)    
            ch_m "I guess. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's it, right?" 
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Well, I guess if you already got it out. . ."    
        elif "hand" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "You're giving me carpal tunnel. . ."
            jump MystiqueHJ_Prep
        elif "hand" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Hand < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "Hmm, magic fingers. . ."        
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handjob?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine." 
        elif "no hand" in newgirl["Mystique"].DailyActions:               
            ch_m "OK, geeze!"   
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Okay.",                 
                "Fine, let me see your rod.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump MystiqueHJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if "no hand" in newgirl["Mystique"].RecentActions:  
            ch_m "You don't listen do you, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no hand" in newgirl["Mystique"].DailyActions: 
            ch_m "I said not in public!"  
        elif "no hand" in newgirl["Mystique"].DailyActions:       
            ch_m "I told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I said not in public!"     
        elif not newgirl["Mystique"].Hand:
            call MystiqueFace("bemused")
            ch_m "I don't know, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Yeah."              
                return
            "Maybe later?" if "no hand" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m ". . ."
                ch_m "Maybe."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no hand")                      
                $ newgirl["Mystique"].DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                      "Okay.",                 
                      "Fine, let me see your rod.", 
                      "I guess I could. . .",
                      "Ok. . . [She gestures for you to come over].",
                      "Heh, ok, ok."])  
                    ch_m "[Line]"
                    $ Line = 0                   
                    jump MystiqueHJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Ok, fine."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump MystiqueHJ_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)     
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1 
    if "no hand" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("angry", 1)
        ch_m "I'm not telling you again."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Not even if you had a ten foot pole."
        call MystiqueFace("surprised", 2)
        ch_m "I mean. . ."
        call MystiqueFace("angry", 1)        
        ch_m "You know what I mean!"
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)          
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "Not here, not anywhere near here."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)   
    elif newgirl["Mystique"].Hand:
        call MystiqueFace("sad") 
        ch_m "I'm not feeling it today. . ."       
    else:
        call MystiqueFace("normal", 1)
        ch_m "I don't wanna touch that."  
    $ newgirl["Mystique"].RecentActions.append("no hand")                      
    $ newgirl["Mystique"].DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label MystiqueHJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
                
    call MystiqueFace("sexy")
    if newgirl["Mystique"].Forced:
        call MystiqueFace("sad")
    elif newgirl["Mystique"].Hand:
        $ newgirl["Mystique"].Brows = "confused"
        $ newgirl["Mystique"].Eyes = "sexy"
        $ newgirl["Mystique"].Mouth = "smile"
    
    call Mystique_HJ_Launch("L")
    if not newgirl["Mystique"].Hand:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)     
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no hand")
    $ newgirl["Mystique"].RecentActions.append("hand")                      
    $ newgirl["Mystique"].DailyActions.append("hand") 
  
label MystiqueHJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Mystique")
        call Mystique_HJ_Launch    
        call MystiqueLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ newgirl["Mystique"].Brows = "angry"        
                    menu:
                        ch_m "Ouch, hand cramp, can we take a break?"
                        #"How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                        #        $ Situation = "shift"
                        #        call Mystique_HJAfter
                        #        call Mystique_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump MystiqueHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_HJ_Reset
                                $ Situation = "shift"
                                jump Mystique_HJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_m "Hey, I've got better things to do if you're going to be a dick about it."                                               
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)                     
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_HJAfter
        elif Cnt == 10 and newgirl["Mystique"].SEXP <= 100 and not ApprovalCheck("Mystique", 1200, "LO"):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Can we be done with this now? I'm getting sore."         
        #End Count check
        
        if not Speed:
            $ Speed = 1 

        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        
                        "Appearance" if P_Lvl >= 4:
                                call Mystique_Appearance_HJ 
                        
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
                                    call Mystique_Undress  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if newgirl["Mystique"].Action and MultiAction:
                                                $ Situation = "shift"
                                                call Mystique_HJAfter                
                                                call Mystique_Blowjob
                                            else:
                                                ch_m "Actually I'm getting a bit worn out, let's finish up here. . ."
                                       
                        "I also want to fondle her breasts." if newgirl["Mystique"].Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    $ Situation = "auto"
                                    call Mystique_Fondle_Breasts
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                         
                        "Let's try something else." if MultiAction: 
                                    call Mystique_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_HJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_HJ_Reset
                                    $ Line = 0
                                    jump Mystique_HJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_HJ_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_HJAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                                                
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_HJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump Mystique_HJAfter   
        #End orgasm
        
        if Round == 10:
            ch_m "It's kind of time to get moving."   
        elif Round == 5:
            ch_m "For real time's up."      
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, we need to take a break."
    
label Mystique_HJAfter:
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Hand += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)
    
    if newgirl["Mystique"].Loc == bg_current and "noticed rogue" in newgirl["Mystique"].RecentActions: #If Mystique was participating
        $ R_LikeNewGirl["Mystique"] += 1
    
    if "Mystique Handi-Queen" in Achievements:
            pass  
    elif newgirl["Mystique"].Hand >= 10:
            call MystiqueFace("smile", 1)
            ch_m "I've kinda become a \"Handy-Queen\" or something."
            $ Achievements.append("Mystique Handy-Queen")
            $ newgirl["Mystique"].SEXP += 5          
    elif newgirl["Mystique"].Hand == 1:            
            $ newgirl["Mystique"].SEXP += 10
            if newgirl["Mystique"].Love >= 500:
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "It was so warm to the touch. . ."
            elif P_Focus <= 20:
                $ newgirl["Mystique"].Mouth = "sad"
                ch_m "Did that work out for you?"
    elif newgirl["Mystique"].Hand == 5:
                ch_m "Let me know any time when you need me to give you a hand."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Ok, so what were you thinking?"
    else:
        call Mystique_HJ_Reset    
    call Checkout
    return

## end Mystique_Handjob //////////////////////////////////////////////////////////////////////


# Mystique_Blowjob //////////////////////////////////////////////////////////////////////

label Mystique_Blowjob:
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Blow >= 7: # She loves it
        $ Tempmod += 15  
    elif newgirl["Mystique"].Blow >= 3: #You've done it before several times
        $ Tempmod += 10
    elif newgirl["Mystique"].Blow: #You've done it before
        $ Tempmod += 7    
        
    if newgirl["Mystique"].Addict >= 75 and newgirl["Mystique"].Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 25
    elif newgirl["Mystique"].Addict >= 75: #She's really strung out
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount        
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no blow" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no blow" in newgirl["Mystique"].RecentActions else 0    
    
    $ Approval = ApprovalCheck("Mystique", 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
        if Approval > 2:                                                      # fix, add Mystique auto stuff here
            "Mystique slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)                     
                    "Mystique continues licking at it."
                "Praise her.":       
                    call MystiqueFace("sexy, 1")                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                    ch_p "Hmmm, keep doing that, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique continues her actions."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                "Ask her to stop.":     
                    call MystiqueFace("surprised")  
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique puts it down."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                    return            
            jump MystiqueBJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
            return            
    
    if not newgirl["Mystique"].Blow and "no blow" not in newgirl["Mystique"].RecentActions:        
        call MystiqueFace("surprised", 2)
        $ newgirl["Mystique"].Mouth = "kiss"
        ch_m "You want me to suck your dick?"
        if newgirl["Mystique"].Hand:          
            $ newgirl["Mystique"].Mouth = "smile"
            ch_m "Not satisfied with handies anymore?"        
        $ newgirl["Mystique"].Blush = 1
            
    if not newgirl["Mystique"].Blow and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "I have wondered what you. . . taste like."            
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal")
            ch_m "If you want me to. . ."               
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "My mouth is watering. . ."   
        else: # Uninhibited 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Mouth = "smile"             
            ch_m " sure. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "You want me to do that again?"
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Ok, I guess this is private enough. . ."    
        elif "blow" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "Mmm, again? [[stretches her jaw]"
            jump MystiqueBJ_Prep                
        elif "blow" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Blow < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you'd like another blowjob?"        
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",                 
                "So you want another blowjob?",                 
                "A little. . . lick?", 
                "You want me to suck you off?",
                "A little tlc?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Whatever."    
        elif "no blow" in newgirl["Mystique"].DailyActions:               
            ch_m "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."  
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, ahhhhhh.",                 
                "Well. . . ok.",                 
                "Yum.", 
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Yeah, ok, alright."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 1)      
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
        jump MystiqueBJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if "no blow" in newgirl["Mystique"].RecentActions:  
            ch_m "What did I {i}just{/i} tell you [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no blow" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you, not in public!"  
        elif "no blow" in newgirl["Mystique"].DailyActions:       
            ch_m "I told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you this is too public!"      
        elif not newgirl["Mystique"].Blow:
            call MystiqueFace("bemused")
            ch_m "I don't know about the taste, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Later, [newgirl[Mystique].Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Aw, it's ok, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no blow" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "You never know, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no blow")                      
                $ newgirl["Mystique"].DailyActions.append("no blow")            
                return
            "Come on, please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure, I guess.",                 
                        "Well. . . ok.",                 
                        "I could maybe give it a try.", 
                        "I guess I could. . .",
                        "Fine. . . [She licks her lips].",
                        "Ok, fine."]) 
                    ch_m "[Line]"
                    $ Line = 0                   
                    jump MystiqueBJ_Prep
                else:   
                    if ApprovalCheck("Mystique", 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                        call MystiqueFace("confused", 1)
                        #$ newgirl["Mystique"].Arms = 1
                        if newgirl["Mystique"].Hand:
                            ch_m "Maybe I could just use my hand?"
                        else:
                            ch_m "I could maybe. . . [[she makes a jerking motion with her hand]?"
                        menu:
                            ch_m "Would that work?"
                            "Sure, that's fine.":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)  
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)                                
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1) 
                                jump MystiqueHJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                                
                                $ newgirl["Mystique"].Arms = 0                
                                ch_m "Ok, your loss."  
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)  
                    
                    
            "Suck it, [newgirl[Mystique].Pet]":                                               # Pressured into it                
                call Mystique_Namecheck
                $ Approval = ApprovalCheck("Mystique", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Ok, fine. . ."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1
                    jump MystiqueBJ_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)     
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.   
    if "no blow" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("angry", 1)
        ch_m "You can eat a dick, 'cos I'm not."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I just can't do that!"
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)     
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)      
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
        $ newgirl["Mystique"].RecentActions.append("no blow")                      
        $ newgirl["Mystique"].DailyActions.append("no blow") 
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)          
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "This is way too exposed!"
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)    
        return                
    elif newgirl["Mystique"].Blow:
        call MystiqueFace("sad") 
        ch_m "No, not this time."       
    else:
        call MystiqueFace("normal", 1)
        ch_m "Nope."  
    $ newgirl["Mystique"].RecentActions.append("no blow")                      
    $ newgirl["Mystique"].DailyActions.append("no blow") 
    $ Tempmod = 0    
    return
    

label MystiqueBJ_Prep:   
    if renpy.showing("Mystique_HJ_Animation"):
        hide Mystique_HJ_Animation with easeoutbottom
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
                
    call MystiqueFace("sexy")
    if newgirl["Mystique"].Forced:
        call MystiqueFace("sad")
    elif newgirl["Mystique"].Hand:
        $ newgirl["Mystique"].Brows = "confused"
        $ newgirl["Mystique"].Eyes = "sexy"
        $ newgirl["Mystique"].Mouth = "smile"
    
    call Mystique_BJ_Launch("L")
    if not newgirl["Mystique"].Blow:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -70)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 45)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 60) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 35)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 40)     
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no blow")
    $ newgirl["Mystique"].RecentActions.append("blow")                      
    $ newgirl["Mystique"].DailyActions.append("blow")     

label MystiqueBJ_Cycle: #Repeating strokes  
    while Round >=0:
        call Shift_Focus("Mystique")
        call Mystique_BJ_Launch    
        call MystiqueLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
         
        if Cnt == (10 + newgirl["Mystique"].Blow):
                $ newgirl["Mystique"].Brows = "angry"        
                menu:
                    ch_m "I'm totally worn out here. Can we do something else?"
                    "How about a Handy?" if newgirl["Mystique"].Action and MultiAction:
                            $ Situation = "shift"
                            call Mystique_BJAfter
                            call Mystique_Handjob 
                            return
                    "Finish up." if P_FocusX:
                            "You release your concentration. . ."             
                            $ P_FocusX = 0
                            $ P_Focus += 15
                            $ Cnt += 1
                            "[Line]."
                            jump MystiqueBJ_Cycle
                    "Let's try something else." if MultiAction: 
                            $ Line = 0
                            call Mystique_BJ_Reset
                            $ Situation = "shift"
                            jump Mystique_BJAfter
                    "No, get back down there.":
                            if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call MystiqueFace("angry", 1)  
                                "She scowls at you, drops you cock and pulls back."
                                ch_m "Well fuck you then."
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                $ newgirl["Mystique"].RecentActions.append("angry")
                                $ newgirl["Mystique"].DailyActions.append("angry")   
                                jump Mystique_BJAfter        
        elif Cnt == (5 + newgirl["Mystique"].Blow) and newgirl["Mystique"].SEXP <= 100 and not ApprovalCheck("Mystique", 1200, "LO"):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Are you getting close here? I'm cramping up."  
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    
                    menu:
                        "[Line]"
                        
                        "Appearance" if P_Lvl >= 4:
                                call Mystique_Appearance_BJ               
                        
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
                                if "pushed" not in newgirl["Mystique"].RecentActions and newgirl["Mystique"].Blow < 5:
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -(20-(2*newgirl["Mystique"].Blow))) 
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, (30-(3*newgirl["Mystique"].Blow)))
                                    $ newgirl["Mystique"].RecentActions.append("pushed")
                                if Trigger2 == "jackin" and Speed != 3:
                                    "She takes it to the root, and you move your hand out of the way."
                                $ Speed = 4  
                        "Take it deeper. (locked)" if Speed == 4:
                                pass
                            
                        "Set your own pace. . .":                
                                "Mystique hums contentedly."    
                                if "setpace" not in newgirl["Mystique"].RecentActions:
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                                $ D20 = renpy.random.randint(1, 20)     
                                if newgirl["Mystique"].Blow < 5:
                                    $ D20 -= 10
                                elif newgirl["Mystique"].Blow < 10:
                                    $ D20 -= 5
                                    
                                if D20 > 15:
                                    $ Speed = 4              
                                    if "setpace" not in newgirl["Mystique"].RecentActions:      
                                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                                elif D20 > 10:
                                    $ Speed = 3
                                #elif D20 > 5:
                                #    $ Speed = 2
                                else:
                                    $ Speed = 1
                                $ newgirl["Mystique"].RecentActions.append("setpace")
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress  
                                    
                        "Shift actions":
                            menu:
                                "How about a handy?":
                                        if newgirl["Mystique"].Action and MultiAction:
                                            if  newgirl["Mystique"].Over == "armbinder":
                                                call MystiqueFace("sexy", 1)
                                                ch_m "I can't do that with my arms like this [newgirl[Mystique].Petname]"
                                                "You untie her arms and removes her blindfold"
                                                $ newgirl["Mystique"].Over = 0
                                                $ newgirl["Mystique"].Blindfold = 0
                                                if newgirl["Mystique"].Chest or newgirl["Mystique"].Pants or newgirl["Mystique"].Panties:
                                                    "She drops the rest of her clothes"
                                                    $ newgirl["Mystique"].Chest = 0
                                                    $ newgirl["Mystique"].Pants = 0
                                                    $ newgirl["Mystique"].Panties = 0
                                                    $ newgirl["Mystique"].Outfit = "nude"
                                            $ Situation = "shift"
                                            call Mystique_BJAfter
                                            call Mystique_Handjob
                                        else:
                                            ch_m "I'm kinda tired, could we just wrap this up. . ."
                        
                                        
                        "I also want to fondle her breasts.":
                                if newgirl["Mystique"].Action and MultiAction:
                                    $ Trigger2 = "fondle breasts"
                                    "You start to fondle her breasts."
                                    $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm kinda tired, could we just wrap this up?"  
                                         
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_BJ_Reset
                                $ Situation = "shift"
                                jump Mystique_BJAfter
                        "Let's stop for now." if not MultiAction: 
                                $ Line = 0
                                call Mystique_BJ_Reset
                                jump Mystique_BJAfter 
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_BJ_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_BJAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                                                
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_BJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump Mystique_BJAfter   
                
        #End orgasm
        
   
        if Round == 10:
            ch_m "Could we wrap this up?"  
        elif Round == 5:
            ch_m "Seriously, I need a break."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, I gotta rest me jaw for a minute. . ."

label Mystique_BJAfter:    
    call MystiqueFace("sexy")  
        
    $ newgirl["Mystique"].Blow += 1
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1
                
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions:
            $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
            
    if "Mystique Jobber" in Achievements:
        pass
    elif newgirl["Mystique"].Blow >= 10:
        call MystiqueFace("smile", 1)
        ch_m "I can't get your taste out of my mind."      
        $ Achievements.append("Mystique Jobber")
        $ newgirl["Mystique"].SEXP += 5
    elif Situation == "shift":
        pass
    elif newgirl["Mystique"].Blow == 1:
            $ newgirl["Mystique"].SEXP += 15
            if newgirl["Mystique"].Love >= 500:
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "Huh, that wasn't bad."
            elif P_Focus <= 20:
                $ newgirl["Mystique"].Mouth = "sad"
                ch_m "I hope you enjoyed that."     
    elif newgirl["Mystique"].Blow == 5:
        ch_m "I'm getting better at this. . . right?"
        menu:
            "[[nod]":
                call MystiqueFace("smile", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 15)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 5)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Mystique", 500, "O"):
                    call MystiqueFace("sad", 2)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                else:
                    call MystiqueFace("angry", 2)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -25)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 10)
                ch_m ". . ."         
                call MystiqueFace("sad", 1)
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Mystique_BJ_Reset    
    call Checkout
    return
    


# end Mystique_Blowjob                                 //////////////////////////////////////////////////////////////////////////////

## Mystique_Titjob //////////////////////////////////////////////////////////////////////              Not finished
# label Mystique_Titjob:
#     return #fix remove when this works
    
#     call Shift_Focus("Mystique")
#     if newgirl["Mystique"].Tit >= 7: # She loves it
#         $ Tempmod += 10
#     elif newgirl["Mystique"].Tit >= 3: #You've done it before several times
#         $ Tempmod += 7
#     elif newgirl["Mystique"].Tit: #You've done it before
#         $ Tempmod += 5
    
#     if newgirl["Mystique"].Addict >= 75 and newgirl["Mystique"].Swallow >=3: #She's really strung out and has swallowed
#         $ Tempmod += 15
#     elif newgirl["Mystique"].Addict >= 75:
#         $ Tempmod += 5
        
#     if newgirl["Mystique"].SeenChest and ApprovalCheck("Mystique", 500): # You've seen her tits.
#         $ Tempmod += 10    
#     if not newgirl["Mystique"].Chest and not newgirl["Mystique"].Over: #She's already topless
#         $ Tempmod += 10
#     if newgirl["Mystique"].Lust > 75: #She's really horny
#         $ Tempmod += 10
#     if Situation == "shift":
#         $ Tempmod += 15
#     if "exhibitionist" in newgirl["Mystique"].Traits:
#         $ Tempmod += (5*Taboo)
#     if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
#         $ Tempmod += 10
#     elif "ex" in newgirl["Mystique"].Traits:
#         $ Tempmod -= 30 
#     if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
#         $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount    
    
#     if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
#         $ Tempmod -= 10 
        
#     if "no titjob" in newgirl["Mystique"].DailyActions:               
#         $ Tempmod -= 5 
#         $ Tempmod -= 10 if "no titjob" in newgirl["Mystique"].RecentActions else 0    
        
#     $ Approval = ApprovalCheck("Mystique", 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    
#     if Situation == "Mystique":                                                                  #Mystique auto-starts   
#         if Approval > 2:                                                      # fix, add Mystique auto stuff here
#             call Mystique_TJ_Launch("L")            
#             "Mystique slides down and sandwiches your dick between her tits."
#             menu:
#                 "What do you do?"
#                 "Nothing.":                    
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)                     
#                     "Mystique starts to slide them up and down."
#                 "Praise her.":       
#                     call MystiqueFace("sexy, 1")                    
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
#                     ch_p "Oh, that sounds like a good idea, [newgirl[Mystique].Pet]."
#                     call Mystique_Namecheck
#                     "Mystique continues her actions."
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
#                 "Ask her to stop.":     
#                     call MystiqueFace("confused")  
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
#                     ch_p "Let's not do that for now, [newgirl[Mystique].Pet]."
#                     call Mystique_Namecheck
#                     "Mystique lets it drop out from between her breasts."
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
#                     call Mystique_TJ_Reset  
#                     return            
#             jump MystiqueTJ_Cycle
#         else:                
#             $ Tempmod = 0                               # fix, add Mystique auto stuff here
#             $ Trigger2 = 0
#             return            
    
#     if not newgirl["Mystique"].Tit and "no titjob" not in newgirl["Mystique"].RecentActions:        
#         call MystiqueFace("surprised", 1)
#         $ newgirl["Mystique"].Mouth = "kiss"
#         ch_m "You want me to rub your cock with my breasts?"        
#         if newgirl["Mystique"].Blow:          
#             $ newgirl["Mystique"].Mouth = "smile"
#             ch_m "My mouth wasn't enough?"
#         elif newgirl["Mystique"].Hand:          
#             $ newgirl["Mystique"].Mouth = "smile"
#             ch_m "My hand wasn't enough?"
            
#     if not newgirl["Mystique"].Tit and Approval:                                                 #First time dialog    
#         if newgirl["Mystique"].Forced: 
#             call MystiqueFace("sad")
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
#         elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
#             call MystiqueFace("sexy")
#             $ newgirl["Mystique"].Brows = "sad"
#             $ newgirl["Mystique"].Mouth = "smile" 
#             ch_m "Huh, well that's certainly one way to get off."            
#         elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
#             call MystiqueFace("normal")
#             ch_m "If that's what you want. . ."              
#         elif newgirl["Mystique"].Addict >= 50:
#             call MystiqueFace("manic", 1)
#             ch_m "Hmmmm. . . ."     
#         else: # Uninhibited 
#             call MystiqueFace("sad")
#             $ newgirl["Mystique"].Mouth = "smile"             
#             ch_m "Heh, might be fun."      
#     elif Approval:                                                                       #Second time+ dialog
#         if newgirl["Mystique"].Forced: 
#             call MystiqueFace("sad")
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
#             ch_m "This isn't going to become a habit, will it?"
#         elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
#             ch_m "Ok, I guess this is private enough. . ."   
#         elif "titjob" in newgirl["Mystique"].RecentActions:
#             call MystiqueFace("sexy", 1)
#             ch_m "Mmm, again? Ok, let me get the girls ready."
#             jump MystiqueTJ_Prep
#         elif "titjob" in newgirl["Mystique"].DailyActions:
#             call MystiqueFace("sexy", 1)
#             $ Line = renpy.random.choice(["Back again so soon?",   
#                 "You're going to give me calluses.", 
#                 "Didn't get enough earlier?",
#                 "My tits are still a bit sore from earlier."]) 
#             ch_m "[Line]"
#         elif newgirl["Mystique"].Tit < 3:        
#             call MystiqueFace("sexy", 1)
#             $ newgirl["Mystique"].Brows = "confused"
#             $ newgirl["Mystique"].Mouth = "kiss"
#             ch_m "So you'd like another titjob?"        
#         else:       
#             call MystiqueFace("sexy", 1)
#             $ newgirl["Mystique"].Girl_Arms = 2
#             $ Line = renpy.random.choice(["You want some of this action [jiggles her tits]?",                 
#                 "So you'd like another titjob?",                 
#                 "A little. . . bounce?", 
#                 "You want me to pillow your crank?",
#                 "A little soft embrace?"]) 
#             ch_m "[Line]"
#         $ Line = 0
            
#     if Approval >= 2:                                                                   #She's into it. . .               
#         if newgirl["Mystique"].Forced:
#             call MystiqueFace("sad")
#             $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
#             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
#             ch_m "Well, there are worst ways to get you off. . ." 
#         elif "no titjob" in newgirl["Mystique"].DailyActions:               
#             ch_m "Hmm, I suppose. . ."       
#         else:
#             call MystiqueFace("sexy", 1)
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
#             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
#             $ Line = renpy.random.choice(["Well, sure, put it here.",                 
#                 "Well. . . ok.",                 
#                 "Yum.", 
#                 "Sure, whip it out.",
#                 "Fine. . . [She drools a bit into her cleavage].",
#                 "Heh, ok, alright."]) 
#             ch_m "[Line]"
#             $ Line = 0
#         $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1) 
#         $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 1)      
#         $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
#         jump MystiqueTJ_Prep   
    
#     else:                                                                               #She's not into it, but maybe. . .            
#         call MystiqueFace("angry")
#         if "no titjob" in newgirl["Mystique"].RecentActions:  
#             ch_m "I {i}just{/i} told you \"no,\" [newgirl[Mystique].Petname]."
#         elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no titjob" in newgirl["Mystique"].DailyActions:  
#             ch_m "This is just way too exposed!"     
#         elif "no titjob" in newgirl["Mystique"].DailyActions:       
#             ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
#         elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
#             ch_m "This is just way too exposed!"     
#         elif not newgirl["Mystique"].Tit:
#             call MystiqueFace("bemused")
#             ch_m "I'm not really up for that, [newgirl[Mystique].Petname]. . ."
#         else:
#             call MystiqueFace("bemused")
#             ch_m "Not, right now [newgirl[Mystique].Petname]. . ."
#         menu:
#             extend ""
#             "Sorry, never mind." if "no titjob" in newgirl["Mystique"].DailyActions:
#                 call MystiqueFace("bemused")
#                 ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
#                 return
#             "Maybe later?" if "no titjob" not in newgirl["Mystique"].DailyActions:
#                 call MystiqueFace("sexy")  
#                 ch_m "We'll have to see."
#                 $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
#                 $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
#                 if Taboo:                    
#                     $ newgirl["Mystique"].RecentActions.append("tabno")                      
#                     $ newgirl["Mystique"].DailyActions.append("tabno") 
#                 $ newgirl["Mystique"].RecentActions.append("no titjob")                      
#                 $ newgirl["Mystique"].DailyActions.append("no titjob")            
#                 return
#             "I think this could be fun for both of us. . .":             
#                 if Approval:
#                     call MystiqueFace("sexy")     
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
#                     $ Line = renpy.random.choice(["Well, ok, put it here.",                 
#                         "Well. . . ok.",                 
#                         "I guess.", 
#                         "I guess, whip it out.",
#                         "Fine. . . [She drools a bit into her cleavage].",
#                         "Heh, ok, alright."])
#                     ch_m "[Line]"
#                     $ Line = 0                   
#                     jump MystiqueTJ_Prep
#                 else:   
#                     $ Approval = ApprovalCheck("Mystique", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
#                     if Approval >= 2:       
#                         $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
#                         $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
#                         call MystiqueFace("confused", 1)
#                         if newgirl["Mystique"].Blow:
#                             ch_m "I could just. . . blow you instead?"
#                         else:
#                             ch_m "I could maybe. . . you know, [[she pushes her tongue against the side of her cheek]?"
#                         menu:
#                             ch_m "What do you say [[blowjob]?"
#                             "Ok, get down there.":
#                                 $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)  
#                                 $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)                                
#                                 $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1) 
#                                 jump MystiqueBJ_Prep
#                             "Nah, it's all about dem titties.":  
#                                 $ Line = "no BJ"
#                     if Approval:       
#                         $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
#                         $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
#                         call MystiqueFace("confused", 1)
#                         if newgirl["Mystique"].Hand:
#                             ch_m "Maybe you'd settle for a handy?"
#                         else:
#                             ch_m "I could maybe. . . [[she makes a jerking motion with her hand]?"
#                         menu:
#                             ch_m "What do you say?"
#                             "Sure, that's fine.":
#                                 $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)  
#                                 $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)                                
#                                 $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1) 
#                                 jump MystiqueHJ_Prep
#                             "Seriously, titties." if Line == "no BJ":  
#                                 $ Line = 0
#                             "Nah, it's all about dem titties." if Line != "no BJ":  
#                                 pass
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
#                     ch_m "Ok, whatever."  
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2) 
                    
                    
#             "Come on, let me fuck those titties, [newgirl[Mystique].Pet]":                                               # Pressured into it                
#                 call Mystique_Namecheck
#                 $ Approval = ApprovalCheck("Mystique", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
#                 if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
#                     call MystiqueFace("sad")
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
#                     ch_m "Ok, fine, whip it out."  
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
#                     $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
#                     $ newgirl["Mystique"].Forced = 1
#                     jump MystiqueTJ_Prep
#                 else:                              
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)     
#                     $ newgirl["Mystique"].RecentActions.append("angry")
#                     $ newgirl["Mystique"].DailyActions.append("angry")   
    
#     #She refused all offers.   
#     if "no titjob" in newgirl["Mystique"].DailyActions:
#         call MystiqueFace("angry", 1)
#         ch_m "Look, I already told you no thanks, [newgirl[Mystique].Petname]."   
#         $ newgirl["Mystique"].RecentActions.append("angry")
#         $ newgirl["Mystique"].DailyActions.append("angry")   
#     elif newgirl["Mystique"].Forced:
#         call MystiqueFace("angry", 1)
#         ch_m "I'm not that kind of girl."
#         $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)      
#         $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
#         $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)      
#         $ newgirl["Mystique"].RecentActions.append("angry")
#         $ newgirl["Mystique"].DailyActions.append("angry")   
#     elif Taboo:                             # she refuses and this is too public a place for her
#         call MystiqueFace("angry", 1)          
#         $ newgirl["Mystique"].DailyActions.append("tabno") 
#         ch_m "You really expect me to do that here? You realize how. . . exposed that would be?"
#         $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
#         $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)  
#     elif newgirl["Mystique"].Blow:
#         call MystiqueFace("sad") 
#         ch_m "I think I'll let you know when I want you touching these again."       
#     else:
#         call MystiqueFace("normal", 1)
#         ch_m "How about let's not, [newgirl[Mystique].Petname]."
#     $ newgirl["Mystique"].RecentActions.append("no titjob")                      
#     $ newgirl["Mystique"].DailyActions.append("no titjob") 
#     $ Tempmod = 0    
#     return
    
# label MystiqueTJ_Prep:
      
#     if Taboo:
#         $ newgirl["Mystique"].Inbt += int(Taboo/10)  
#         $ newgirl["Mystique"].Lust += int(Taboo/5)

        
#     call MystiqueFace("sexy")
#     if newgirl["Mystique"].Forced:
#         call MystiqueFace("sad")
#     elif newgirl["Mystique"].Tit:
#         $ newgirl["Mystique"].Brows = "confused"
#         $ newgirl["Mystique"].Eyes = "sexy"
#         $ newgirl["Mystique"].Mouth = "smile"
        
#     call Mystique_TJ_Launch("L")    
#     if not newgirl["Mystique"].Tit:        
#         if newgirl["Mystique"].Forced:
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -25)
#             $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 30)
#             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
#         else:
#             $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
#             $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
#             $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30)   
    
    
#     call Seen_First_Peen(1)
    
#     if Situation:     
#         $ renpy.pop_call() 
#         $ Situation = 0  
#     $ Line = 0
#     $ Cnt = 0  
#     if Taboo:
#         call DrainWord("Mystique","tabno")
#     call DrainWord("Mystique","no titjob")
#     $ newgirl["Mystique"].RecentActions.append("titjob")                      
#     $ newgirl["Mystique"].DailyActions.append("titjob") 

# label MystiqueTJ_Cycle: #Repeating strokes  
#     call Shift_Focus("Mystique")  
#     call Mystique_TJ_Launch
        
#     call MystiqueLust            
#     if P_FocusX and P_Focus > 50:
#         $ P_Focus -= 10  
        
#     if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
#             pass
#     elif Cnt == (5 + newgirl["Mystique"].Tit):
#         $ newgirl["Mystique"].Brows = "confused"
#         ch_m "Are you getting close here? I'm getting as little sore."        
#     if Cnt == (10 + newgirl["Mystique"].Tit):
#         $ newgirl["Mystique"].Brows = "angry"        
#         menu:
#             ch_m "I'm getting rug-burn here [newgirl[Mystique].Petname]. Can we do something else?"
#             "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
#                 $ Situation = "shift"
#                 call Mystique_TJAfter
#                 call Mystique_Blowjob 
#                 return
#             "Finish up." if P_FocusX:
#                 "You release your concentration. . ."             
#                 $ P_FocusX = 0
#                 $ P_Focus += 15
#                 $ Cnt += 1
#                 "[Line]."
#                 jump MystiqueTJ_Cycle                
#             "Let's try something else." if MultiAction: 
#                 $ Line = 0
#                 call Mystique_TJ_Reset
#                 $ Situation = "shift"
#                 jump Mystique_TJAfter
#             "No, get back down there.":
#                 if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
#                     "She grumbles but gets back to work."
#                 else:
#                     call MystiqueFace("angry", 1)   
#                     "She scowls at you, drops you cock and pulls back."
#                     ch_m "Well if that's your attitude you can handle your own business."                         
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
#                     $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
#                     $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
#                     $ newgirl["Mystique"].RecentActions.append("angry")
#                     $ newgirl["Mystique"].DailyActions.append("angry")   
#                     jump Mystique_TJAfter
                
        
#     if Line and P_Focus < 100:
#         $ Cnt += 1
#         $ Round -= 1
#         menu:
#             "[Line]."
#             "Get moving. . ." if not Speed:
#                 $ Speed = 1
#             "Keep going. . ." if Speed:
#                 pass
#             "Speed up. . ." if Speed < 2:                    
#                 $ Speed = 2
#                 "You ask her to up the pace a bit."
#             "Speed up. . . (locked)" if Speed >= 2:
#                 pass
#             "Slow Down. . ." if Speed > 1:                    
#                 $ Speed = 1
#                 "You ask her to slow it down a bit."
#             "Slow Down. . . (locked)" if Speed <= 1:
#                 pass

#             "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
#                 call MystiqueFace("sexy", 1) 
#                 "You add a blindfold so she can't see a thing"
#                 $ newgirl["Mystique"].Blindfold = 1

#             "Remove blindfold" if newgirl["Mystique"].Blindfold:
#                 call MystiqueFace("sexy", 1) 
#                 "You remove the blindfold"
#                 $ newgirl["Mystique"].Blindfold = 0

#             "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
#                 pass
#             "Focus to last longer." if "focus" in P_Traits and not P_FocusX:
#                 "You concentrate on not burning out too quickly."                
#                 $ P_FocusX = 1
#             "Release your focus." if P_FocusX:
#                 "You release your concentration. . ."                
#                 $ P_FocusX = 0
#             "How about a blowjob?":
#                 if newgirl["Mystique"].Action and MultiAction:
#                     $ Situation = "shift"
#                     call Mystique_TJAfter                
#                     call Mystique_Blowjob
#                 else:
#                     ch_m "Actually I'm getting a bit worn out, let's finish up here. . ."
#             "How about a handy?":
#                 if newgirl["Mystique"].Action and MultiAction:
#                     $ Situation = "shift"
#                     call Mystique_BJAfter
#                     call Mystique_Handjob
#                 else:
#                     ch_m "Actually I'm getting a bit worn out, let's finish up here. . ."
#             "I also want to fondle her breasts." if newgirl["Mystique"].Action and MultiAction:
#                 $ Trigger2 = "fondle breasts"
#                 $ Situation = "auto"
#                 call Mystique_Fondle_Breasts
#                 if Trigger2:
#                      $ newgirl["Mystique"].Action -= 1               
#             "Let's try something else." if MultiAction:                
#                 $ Line = 0
#                 call Mystique_TJ_Reset
#                 $ Situation = "shift"
#                 jump Mystique_TJAfter
#             "Let's stop for now." if not MultiAction:                
#                 $ Line = 0
#                 call Mystique_TJ_Reset
#                 jump Mystique_TJAfter
    
#     if not Speed:
#         if newgirl["Mystique"].Tit > 2:
#             $ Line = "She just seems to slowly roll it around."
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2) 
#         else:
#             $ Line = "She doesn't seem to know what to do with it."
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 40, 2) 
#         if P_Focus > 60:
#             $ P_Focus -= 5
#         else:
#             $ P_Focus += 3
#         $ newgirl["Mystique"].Addict -= 1
#         jump MystiqueTJ_Cycle
        
    
#     if newgirl["Mystique"].Tit > 4 and newgirl["Mystique"].Blow:                                        #5th+ and blown
#         if Speed <= 1:                                              #slow
#             $ Line = renpy.random.choice(["She rocks her breasts up and down around your cock", 
#                 "She lightly licks the head as it pops up between her tits", 
#                 "She has a smooth motion going now, gentle and precise",
#                 "She pauses to rub her nipples across the shaft",
#                 "In between strokes she gently sucks on the head",
#                 "She drips some spittle down to make sure you're properly lubed",
#                 "She gently caresses the shaft between her tits"])            
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 70, 15)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 5) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4)         
#         else:                                                       #fast
#             $ Line = renpy.random.choice(["She rapidly rocks her breasts up and down around your cock", 
#                 "She licks away at the head every time it pops up between her tits", 
#                 "She has a smooth motion going now, quick by efficient",
#                 "She dancers her nipples across the shaft",
#                 "In as she strokes faster and faster, she bends down to suck on the head",
#                 "She covers her tits with drool to keep them well lubed",
#                 "She rapidly caresses the shaft between her tits"])
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 40, 15, 1)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 5) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 2)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4) 
        
#     elif newgirl["Mystique"].Tit > 1:                                                 #third through 5th time
#         if Speed <= 1:                                              #slow
#             $ Line = renpy.random.choice(["She juggles her breasts up and down around your cock", 
#                 "She lightly strokes the head as it pops up between her tits", 
#                 "She has a smooth motion going now, gentle and precise",
#                 "She pauses to rub her nipples across the shaft",
#                 "She gently caresses the shaft between her tits"])            
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 10)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 5) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)                 
#         else:                                                       #fast
#             $ Line = renpy.random.choice(["She rapidly juggles her breasts up and down around your cock", 
#                 "She lightly brushes the head with her chin as it pops up between her tits", 
#                 "She moves them up and down in a fluid rocking motion",
#                 "She bounces her whole body up and down",
#                 "She rapidly slides the shaft between her tits"])            
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 50, 8, 1)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 7) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 4) 

    
#     else:                                                           #First and second time
#         if Speed <= 1:                                              #slow
#             $ Line = renpy.random.choice(["Mystique sort of squishes her breasts back and forth around your cock", 
#                 "She slides the cock up and down between her cleavage", 
#                 "She kind of bounces her tits around your cock",
#                 "She smooshes her cleavage as tight as she can and rubs up and down"])
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 7)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 5) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 3)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)                 
#         else:                                                       #fast
#             $ Line = renpy.random.choice(["Mystique sort of bounces her breasts off your cock", 
#                 "She tries to quickly slide the cock up and down between her cleavage, but it tends to slide out", 
#                 "She slaps her tits against your dick",
#                 "She smooshes her cleavage as tight as she can and rubs up and down quite quickly"])            
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 60, 7)
#             $ P_Focus = Statupdate("Mystique", "Focus", P_Focus, 200, 4) 
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 2)
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3) 
    
#     call Mystique_Offhand                                                            #Offhand and reduce addiciton per stroke        
#     $ newgirl["Mystique"].Addict -= 2          
    
#     if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                                     #If either of you could cum    
#         if P_Focus >= 100:                                                  #You cum             
#             call Mystique_P_Cumming
#             if "angry" in newgirl["Mystique"].RecentActions:  
#                 call Mystique_TJ_Reset
#                 return    
#             $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
#             if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
#                 $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
#                 $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
            
#             if P_Focus > 80:
#                 jump Mystique_TJAfter   
        
#         if newgirl["Mystique"].Lust >= 100:                                                   #and Mystique cums                    
#             call Mystique_Cumming
#             if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
#                 jump Mystique_TJAfter            
                        
#         if P_Focus <= 20 or not P_Semen:
#             if not P_Semen:
#                 "You're pretty wiped, better stop for now."
#             $ Line = 0
#             jump Mystique_TJAfter     
     

#     if Round:
#         if Round == 10:
#             ch_m "You might want to wrap this up, it's getting late."  
#         elif Round == 5:
#             ch_m "Seriously, it'll be time to stop soon."        
#         jump MystiqueTJ_Cycle  
#     else: # You ran out of tries.
#         call MystiqueFace("bemused", 0)
#         $ Line = 0
#         ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
        
# label Mystique_TJAfter:
#     $ newgirl["Mystique"].Tit += 1
    
#     call MystiqueFace("sexy")  
        
#     $ newgirl["Mystique"].Action -=1
#     $ newgirl["Mystique"].Addictionrate += 1
#     if "addictive" in P_Traits:
#         $ newgirl["Mystique"].Addictionrate += 1
        
#     if newgirl["Mystique"].Tit > 5:
#         pass
#     elif newgirl["Mystique"].Tit == 1 and newgirl["Mystique"].Love >= 500:
#         $ newgirl["Mystique"].Mouth = "smile"
#         ch_m "Well, that was certainly interesting."
#     elif newgirl["Mystique"].Tit == 1 and P_Focus <= 20:
#         $ newgirl["Mystique"].Mouth = "sad"
#         ch_m "Well, I hope that was enough for you."        
#     elif newgirl["Mystique"].Tit == 5:
#         ch_m "I think I've got the goods for this."        
#     if newgirl["Mystique"].Tit == 1:
#         $ newgirl["Mystique"].SEXP += 12
    
#     $ Tempmod = 0    
    
#     if Situation == "shift":
#         ch_m "Mmm, so what else did you have in mind?"
#     else:
#         call Mystique_TJ_Reset    
#     call Checkout
#     return

# ## end Mystique_Titjob //////////////////////////////////////////////////////////////////////

# # ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Mystique_Dildo_Check:
    if "dildo" in P_Inventory:   
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in newgirl["Mystique"].Inventory:
        "You ask Mystique to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1
            
label Mystique_Dildo_Pussy:
    call Shift_Focus("Mystique")
    call Mystique_Dildo_Check    
    if not _return:
        return 

    if newgirl["Mystique"].DildoP: #You've done it before
        $ Tempmod += 15
    if newgirl["Mystique"].Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20
        
    if newgirl["Mystique"].Lust > 95:
        $ Tempmod += 20    
    elif newgirl["Mystique"].Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:        
        $ Tempmod += (5*Taboo) 
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount     
        
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no dildo" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in newgirl["Mystique"].RecentActions else 0       
        
    $ Approval = ApprovalCheck("Mystique", 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
                if Approval > 2:                                                      # fix, add Mystique auto stuff here
                    if newgirl["Mystique"].Legs == "skirt":
                        "Mystique grabs her dildo, hiking up her skirt as she does."
                        $ newgirl["Mystique"].Upskirt = 1
                    elif newgirl["Mystique"].Legs == "pants":
                        "Mystique grabs her dildo, pulling down her pants as she does."              
                        $ newgirl["Mystique"].Legs = 0
                    else:
                        "Mystique grabs her dildo, rubbing is suggestively against her crotch."
                    $ newgirl["Mystique"].SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                            "Mystique slides it in."
                        "Go for it.":       
                            call MystiqueFace("sexy, 1")                    
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                            ch_p "Oh yeah, [newgirl[Mystique].Pet], let's do this."
                            call Mystique_Namecheck
                            "You grab the dildo and slide it in."
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        "Ask her to stop.":
                            call MystiqueFace("surprised")       
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                            call Mystique_Namecheck
                            "Mystique sets the dildo down."
                            call MystiqueOutfit
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                            return            
                    jump MystiqueDP_Prep
                else:                
                    $ Tempmod = 0                               # fix, add Mystique auto stuff here
                    $ Trigger2 = 0
                return            
    
    if Situation == "auto":    
                "You rub the dildo across her body, and along her moist slit."
                call MystiqueFace("surprised", 1)
                
                if (newgirl["Mystique"].DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call MystiqueFace("sexy")
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    ch_m "Ooo, [newgirl[Mystique].Petname], toys!"            
                    jump MystiqueDP_Prep         
                else:                                                                                                            #she's questioning it
                    $ newgirl["Mystique"].Brows = "angry"                
                    menu:
                        ch_m "Hey, what are you planning to do with that?!" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                call MystiqueFace("sexy", 1)
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                                ch_m "Well, now that you mention it. . ."
                                jump MystiqueDP_Prep
                            "You pull back before you really get it in."                    
                            call MystiqueFace("bemused", 1)
                            if newgirl["Mystique"].DildoP:
                                ch_m "Well ok, [newgirl[Mystique].Petname], maybe warn me next time?" 
                            else:
                                ch_m "Well ok, [newgirl[Mystique].Petname], that's a little much. . . for now . . ."                                               
                        "Just playing with my favorite toys.":                    
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                            "You press it inside some more."                              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            if not ApprovalCheck("Mystique", 700, "O", TabM=1): #Checks if Obed is 700+                             
                                call MystiqueFace("angry")
                                "Mystique shoves you away and slaps you in the face."
                                ch_m "Jerk!"
                                ch_m "Ask nice if you want to stick something in my ass!"                                               
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Mystique_SexSprite"):
                                    call Mystique_Sex_Reset 
                                $ newgirl["Mystique"].RecentActions.append("angry")
                                $ newgirl["Mystique"].DailyActions.append("angry")                          
                            else:
                                call MystiqueFace("sad")
                                "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump MystiqueDP_Prep
                return             
    #end Auto
   
    if not newgirl["Mystique"].DildoP:                                                               
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "Hmmm, so you'd like to try out some toys?"    
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "I suppose there are worst things you could ask for."
            
    if not newgirl["Mystique"].DildoP and Approval:                                                 
            #First time dialog        
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "I've had a reasonable amount of experience with these, you know. . ."            
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "If that's what you want, [newgirl[Mystique].Petname]. . ."            
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "The toys again?" 
            elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
                ch_m "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in newgirl["Mystique"].RecentActions:
                call MystiqueFace("sexy", 1)
                ch_m "Mmm, again? Ok, let's get to it."
                jump MystiqueDP_Prep
            elif "dildo pussy" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_m "[Line]"
            elif newgirl["Mystique"].DildoP < 3:        
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Mouth = "kiss"
                ch_m "You want to stick it in my again?"       
            else:       
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Girl_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_m "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Ok, fine."    
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hell yeah.",
                    "Heh, ok, ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump MystiqueDP_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call MystiqueFace("angry")
            if "no dildo" in newgirl["Mystique"].RecentActions:  
                ch_m "What part of \"no,\" did you not get, [newgirl[Mystique].Petname]?"
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no dildo" in newgirl["Mystique"].DailyActions:
                ch_m "Stop swinging that thing around in public!"   
            elif "no dildo" in newgirl["Mystique"].DailyActions:       
                ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "Stop swinging that thing around in public!"  
            elif not newgirl["Mystique"].DildoP:
                call MystiqueFace("bemused")
                ch_m "I'm just not into toys, [newgirl[Mystique].Petname]. . ."
            else:
                call MystiqueFace("bemused")
                ch_m "I don't think we need any toys, [newgirl[Mystique].Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("bemused")
                    ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                    return
                "Maybe later?" if "no dildo" not in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("sexy")  
                    ch_m "Maybe I'll practice on my own time, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                    if Taboo:                    
                        $ newgirl["Mystique"].RecentActions.append("tabno")                      
                        $ newgirl["Mystique"].DailyActions.append("tabno") 
                    $ newgirl["Mystique"].RecentActions.append("no dildo")                      
                    $ newgirl["Mystique"].DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call MystiqueFace("sexy")     
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_m "[Line]"
                        $ Line = 0                   
                        jump MystiqueDP_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Mystique", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                        call MystiqueFace("sad")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                        ch_m "Ok, fine. If we're going to do this, stick it in already."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        $ newgirl["Mystique"].Forced = 1  
                        jump MystiqueDP_Prep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)     
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if "no dildo" in newgirl["Mystique"].DailyActions:
            ch_m "Learn to take \"no\" for an answer, [newgirl[Mystique].Petname]."   
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
            call MystiqueFace("angry", 1)
            ch_m "I'm not going to let you use that on me."
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)   
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)     
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call MystiqueFace("angry", 1)         
            $ newgirl["Mystique"].RecentActions.append("tabno")                       
            $ newgirl["Mystique"].DailyActions.append("tabno") 
            ch_m "Not here!"     
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)  
    elif newgirl["Mystique"].DildoP:
            call MystiqueFace("sad") 
            ch_m "Sorry, you can keep your toys to yourself."     
    else:
            call MystiqueFace("normal", 1)
            ch_m "No way."  
    $ newgirl["Mystique"].RecentActions.append("no dildo")                      
    $ newgirl["Mystique"].DailyActions.append("no dildo")  
    $ Tempmod = 0    
    return
                
label MystiqueDP_Prep: #Animation set-up 
    if Trigger2 == "dildo pussy":
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 15 if newgirl["Mystique"].Legs == "pants" else 0           
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
            
    $ Tempmod = 0      
    call Mystique_Pussy_Launch("dildo pussy")
    if not newgirl["Mystique"].DildoP:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -75)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 60)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 45)
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no dildo")
    $ newgirl["Mystique"].RecentActions.append("dildo pussy")                      
    $ newgirl["Mystique"].DailyActions.append("dildo pussy") 
    
label MystiqueDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("dildo pussy")
        call MystiqueLust   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + newgirl["Mystique"].DildoP):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "What are you even doing down there?" 
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].DildoP) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump MystiqueDP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump MystiqueDP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_m "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump MystiqueDP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        
                        "Appearance" if P_Lvl >= 4:
                                call Mystique_Appearance_BJ               
                        
                        "Keep going. . .":
                                    pass
                                                           
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump MystiqueDP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0

                        
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress  
                                    
                        "Shift actions":
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her ass.":
                                                    $ Situation = "shift"
                                                    call MystiqueDP_After
                                                    call Mystique_Insert_Ass    
                                            "Just stick a finger in her ass without asking.":
                                                    $ Situation = "auto"
                                                    call MystiqueDP_After
                                                    call Mystique_Insert_Ass                                           
                                            "I want to shift the dilso to her ass.":
                                                    $ Situation = "shift"
                                                    call MystiqueDP_After
                                                    call Mystique_Dildo_Ass   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call MystiqueDP_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump MystiqueDP_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump MystiqueDP_After
        #End menu (if Line)
        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: #This checks if Mystique wants to strip down.
                call Mystique_Undress("auto")
            
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Pos_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump MystiqueDP_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump MystiqueDP_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,  
                            "Mystique still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump MystiqueDP_After
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    
label MystiqueDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].DildoP += 1  
    $ newgirl["Mystique"].Action -=1   
        
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].DildoP == 1:            
            $ newgirl["Mystique"].SEXP += 10         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "Thanks for the extra hand. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end newgirl["Mystique"].Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label Mystique_Dildo_Ass:
    call Shift_Focus("Mystique")
    call Mystique_Dildo_Check
    if not _return:
        return 
      
    if newgirl["Mystique"].Loose:
        $ Tempmod += 30   
    elif "anal" in newgirl["Mystique"].RecentActions or "dildo anal" in newgirl["Mystique"].RecentActions:
        $ Tempmod -= 20 
    elif "anal" in newgirl["Mystique"].DailyActions or "dildo anal" in newgirl["Mystique"].DailyActions:
        $ Tempmod -= 10
    elif (newgirl["Mystique"].Anal + newgirl["Mystique"].DildoA + newgirl["Mystique"].Plug) > 0: #You've done it before
        $ Tempmod += 20   
        
    if newgirl["Mystique"].Legs == "pants:": # she's got pants on.
        $ Tempmod -= 20   
        
    if newgirl["Mystique"].Lust > 95:
        $ Tempmod += 20
    elif newgirl["Mystique"].Lust > 85: #She's really horny
        $ Tempmod += 15
        
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:        
        $ Tempmod += (5*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount   
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no dildo" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no dildo" in newgirl["Mystique"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Mystique", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Mystique":                                                                  
            #Mystique auto-starts   
            if Approval > 2:                                                      # fix, add Mystique auto stuff here
                if newgirl["Mystique"].Legs == "skirt":
                    "Mystique grabs her dildo, hiking up her skirt as she does."
                    $ newgirl["Mystique"].Upskirt = 1
                elif newgirl["Mystique"].Legs == "pants":
                    "Mystique grabs her dildo, pulling down her pants as she does."              
                    $ newgirl["Mystique"].Legs = 0
                else:
                    "Mystique grabs her dildo, rubbing is suggestively against her ass."
                $ newgirl["Mystique"].SeenPanties = 1
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                        "Mystique slides it in."
                    "Go for it.":       
                        call MystiqueFace("sexy, 1")                    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                        ch_p "Oh yeah, [newgirl[Mystique].Pet], let's do this."
                        call Mystique_Namecheck
                        "You grab the dildo and slide it in."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    "Ask her to stop.":
                        call MystiqueFace("surprised")       
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                        call Mystique_Namecheck
                        "Mystique sets the dildo down."
                        call MystiqueOutfit
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                        return            
                jump MystiqueDA_Prep
            else:                
                $ Tempmod = 0                               # fix, add Mystique auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            "You rub the dildo across her body, and against her tight anus."
            call MystiqueFace("surprised", 1)
            
            if (newgirl["Mystique"].DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1)
                ch_m "Ooo, [newgirl[Mystique].Petname], toys!"                
                jump MystiqueDA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ newgirl["Mystique"].Brows = "angry"                
                menu:
                    ch_m "Hey, what are you planning to do with that?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call MystiqueFace("sexy", 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_m "Well, now that you mention it. . ."
                            jump MystiqueDA_Prep
                        "You pull back before you really get it in."                    
                        call MystiqueFace("bemused", 1)
                        if newgirl["Mystique"].DildoA:
                            ch_m "Well ok, [newgirl[Mystique].Petname], maybe warn me next time?" 
                        else:
                            ch_m "Well ok, [newgirl[Mystique].Petname], that's a little much. . . for now . . ."                                                   
                    "Just playing with my favorite toys.":                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                        "You press it inside some more."                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        if not ApprovalCheck("Mystique", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call MystiqueFace("angry")
                            "Mystique shoves you away and slaps you in the face."
                            ch_m "Jerk!"
                            ch_m "Ask nice if you want to stick something in my ass!"                                                  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Mystique_SexSprite"):
                                call Mystique_Sex_Reset 
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")                         
                        else:
                            call MystiqueFace("sad")
                            "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump MystiqueDA_Prep
            return             
    #end auto
   
    if not newgirl["Mystique"].DildoA:                                                               
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "You want to try and fit that. . .?"    
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "Always about the but, huh?"
    
    if not newgirl["Mystique"].Loose and ("dildo anal" in newgirl["Mystique"].RecentActions or "anal" in newgirl["Mystique"].RecentActions or "dildo anal" in newgirl["Mystique"].DailyActions or "anal" in newgirl["Mystique"].DailyActions):
            call MystiqueFace("bemused", 1)
            ch_m "I'm still sore from earlier. . ."
            
    if not newgirl["Mystique"].DildoA and Approval:                                                 
            #First time dialog        
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "I haven't actually used one of these, back there before. . ."            
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "If that's what you want, [newgirl[Mystique].Petname]. . ."            
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "The toys again?"  
            elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
                ch_m "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in newgirl["Mystique"].DailyActions and not newgirl["Mystique"].Loose:
                pass
            elif "dildo anal" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_m "[Line]"
            elif newgirl["Mystique"].DildoA < 3:        
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Mouth = "kiss"
                ch_m "You want to stick it in my ass again?"       
            else:       
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Girl_Arms = 2
                $ Line = renpy.random.choice(["You want some of this action?",                 
                    "So you'd like another go?",                 
                    "You want to stick it in my again?",
                    "You want me ta lube up your toy?"]) 
                ch_m "[Line]"
                $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Ok, fine."    
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess I could. . . stick it in.",
                    "Hell yeah.",
                    "Heh, ok, ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump MystiqueDA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call MystiqueFace("angry")
            if "no dildo" in newgirl["Mystique"].RecentActions:  
                ch_m "What part of \"no,\" did you not get, [newgirl[Mystique].Petname]?"
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no dildo" in newgirl["Mystique"].DailyActions:
                ch_m "Stop swinging that thing around in public!"  
            elif "no dildo" in newgirl["Mystique"].DailyActions:       
                ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "I already told you that I wouldn't do that out here!"  
            elif not newgirl["Mystique"].DildoA:
                call MystiqueFace("bemused")
                ch_m "I'm just not into toys, [newgirl[Mystique].Petname]. . ."
            elif not newgirl["Mystique"].Loose and "dildo anal" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("perplexed")
                ch_m "You could have been a bit more gentle last time, [newgirl[Mystique].Petname]. . ."
            else:
                call MystiqueFace("bemused")
                ch_m "I don't think we need any toys, [newgirl[Mystique].Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("bemused")
                    ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                    return
                "Maybe later?" if "no dildo" not in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("sexy")  
                    ch_m "Maybe I'll practice on my own time, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                    if Taboo:                    
                        $ newgirl["Mystique"].RecentActions.append("tabno")                      
                        $ newgirl["Mystique"].DailyActions.append("tabno") 
                    $ newgirl["Mystique"].RecentActions.append("no dildo")                      
                    $ newgirl["Mystique"].DailyActions.append("no dildo") 
                    return
                "I think you'd like it. . .":             
                    if Approval:
                        call MystiqueFace("sexy")     
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                            "I suppose. . .", 
                            "You've got me there."]) 
                        ch_m "[Line]"
                        $ Line = 0                   
                        jump MystiqueDA_Prep
                    else:   
                        pass
                        
                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Mystique", 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                        call MystiqueFace("sad")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                        ch_m "Ok, fine. If we're going to do this, stick it in already."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        $ newgirl["Mystique"].Forced = 1  
                        jump MystiqueDA_Prep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)    
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1   
    if "no dildo" in newgirl["Mystique"].DailyActions:
            ch_m "Learn to take \"no\" for an answer, [newgirl[Mystique].Petname]."   
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
            call MystiqueFace("angry", 1)
            ch_m "I'm not going to let you use that on me."
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)   
            $ newgirl["Mystique"].RecentActions.append("angry")
            $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call MystiqueFace("angry", 1)          
            $ newgirl["Mystique"].RecentActions.append("tabno")                       
            $ newgirl["Mystique"].DailyActions.append("tabno") 
            ch_m "Not here!"     
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)  
    elif not newgirl["Mystique"].Loose and "dildo anal" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("bemused")
            ch_m "Sorry, I just need a little break back there, [newgirl[Mystique].Petname]."    
    elif newgirl["Mystique"].DildoA:
            call MystiqueFace("sad") 
            ch_m "Sorry, you can keep your toys out of there."     
    else:
            call MystiqueFace("normal", 1)
            ch_m "No way." 
    $ newgirl["Mystique"].RecentActions.append("no dildo")                      
    $ newgirl["Mystique"].DailyActions.append("no dildo")   
    $ Tempmod = 0    
    return
                
label MystiqueDA_Prep: #Animation set-up 
    if Trigger2 == "dildo anal":
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 20 if newgirl["Mystique"].Legs == "pants" else 0           
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
            
    $ Tempmod = 0      
    call Mystique_Pussy_Launch("dildo anal")
    if not newgirl["Mystique"].DildoA:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -75)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 60)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 45)
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
    
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no dildo")
    $ newgirl["Mystique"].RecentActions.append("dildo anal")                      
    $ newgirl["Mystique"].DailyActions.append("dildo anal") 
    
label MystiqueDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("dildo anal")
        call MystiqueLust   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + newgirl["Mystique"].DildoA):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "What are you even doing down there?" 
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].DildoA) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump MystiqueDA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump MystiqueDA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_m "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump MystiqueDA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        
                        "Appearance" if P_Lvl >= 4:
                                call Mystique_Appearance_BJ               
                        
                        "Keep going. . .":
                                    pass
                                    
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump MystiqueDA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0
                        
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress  
                                                            
                        "Shift actions":
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in her pussy.":
                                                    $ Situation = "shift"
                                                    call MystiqueDA_After
                                                    call Mystique_Fondle_Pussy    
                                            "Just stick a finger in her pussy without asking.":
                                                    $ Situation = "auto"
                                                    call MystiqueDA_After
                                                    call Mystique_Fondle_Pussy                                           
                                            "I want to shift the dildo to her pussy.":
                                                    $ Situation = "shift"
                                                    call MystiqueDA_After
                                                    call Mystique_Dildo_Pussy   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call MystiqueDA_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump MystiqueDA_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump MystiqueDA_After
        #End menu (if Line)
        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: #This checks if Mystique wants to strip down.
                call Mystique_Undress("auto")
            
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Pos_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump MystiqueDA_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump MystiqueDA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,  
                            "Mystique still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump MystiqueDA_After
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    
label MystiqueDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].DildoA += 1  
    $ newgirl["Mystique"].Action -=1            
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].DildoA == 1:            
            $ newgirl["Mystique"].SEXP += 10         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    if newgirl["Mystique"].Loose:
                        ch_m "That was. . . interesting. . ."
                    else:
                        ch_m "Ouch. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# # end newgirl["Mystique"].Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Mystique_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in P_Inventory:   
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in newgirl["Mystique"].Inventory:
        "You ask Mystique to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1    
    
# ## Mystique_Footjob //////////////////////////////////////////////////////////////////////
label Mystique_Footjob:
    $ newgirl["Mystique"].LegsUp = 0
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Foot >= 7: # She loves it
        $ Tempmod += 10
    elif newgirl["Mystique"].Foot >= 3: #You've done it before several times
        $ Tempmod += 7
    elif newgirl["Mystique"].Foot: #You've done it before
        $ Tempmod += 3
        
    if newgirl["Mystique"].Addict >= 75 and newgirl["Mystique"].Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 10
    if newgirl["Mystique"].Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (3*Taboo)    
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 40 
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount    
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no foot" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no foot" in newgirl["Mystique"].RecentActions else 0    
        
    $ Approval = ApprovalCheck("Mystique", 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
        if Approval > 2:                                                      # fix, add Mystique auto stuff here
            if Trigger2 == "jackin":
                "Mystique leans and starts rubbing your cock between her feet."
            else:
                "Mystique gives you a mischevious smile, and starts to rub her foot along your cock."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)                     
                    "Mystique continues her actions."
                "Praise her.":       
                    call MystiqueFace("sexy, 1")                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique continues her actions."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                "Ask her to stop.":
                    call MystiqueFace("surprised")       
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [newgirl[Mystique].Pet]."
                    call Mystique_Namecheck
                    "Mystique puts it down."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump MystiqueFJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
            return            
    
    if not newgirl["Mystique"].Foot and "no foot" not in newgirl["Mystique"].RecentActions:        
        call MystiqueFace("confused", 2)
        ch_m "Huh, so you'd like me to rub your cock with my feet?"
        $ newgirl["Mystique"].Blush = 1
            
    if not newgirl["Mystique"].Foot and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad",1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy",1)
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "I guess it couldn't hurt. . ."            
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal",1)
            ch_m "If you want, [newgirl[Mystique].Petname]. . ."            
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "Okay. . ."  
        else: # Uninhibited 
            call MystiqueFace("lipbite",1)    
            ch_m "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's all?" 
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Um, I guess this is secluded enough. . ."    
        elif "foot" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "I'm getting foot cramps. . ."
            jump MystiqueFJ_Prep
        elif "foot" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Foot < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "Hmm, magic toes. . ."        
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot session?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine." 
        elif "no foot" in newgirl["Mystique"].DailyActions:               
            ch_m "OK, geeze!"   
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Sure, I guess.",                 
                "Ookay.",                 
                "Cool, let me see it.", 
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump MystiqueFJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if "no foot" in newgirl["Mystique"].RecentActions:  
            ch_m "You don't listen do you, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no foot" in newgirl["Mystique"].DailyActions: 
            ch_m "I said not in public!"  
        elif "no foot" in newgirl["Mystique"].DailyActions:       
            ch_m "I told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I said not in public!"     
        elif not newgirl["Mystique"].Foot:
            call MystiqueFace("bemused")
            ch_m "I don't know, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Yeah."              
                return
            "Maybe later?" if "no foot" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m ". . ."
                ch_m "Maybe."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no foot")                      
                $ newgirl["Mystique"].DailyActions.append("no foot")            
                return
            "I'd really appreciate it. . .":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Sure, I guess.",                 
                            "Okay.",                 
                            "Cool, let me see it.", 
                            "I guess I could. . .",
                            "Ok. . . [She gestures for you to come over].",
                            "Heh, ok, ok."]) 
                    ch_m "[Line]"
                    $ Line = 0                   
                    jump MystiqueFJ_Prep
                else:   
                    pass
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Ok, fine."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump MystiqueFJ_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)     
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1 
    if "no foot" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("angry", 1)
        ch_m "I'm not telling you again."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I don't even want to step on it."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)          
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "Not here, not anywhere near here."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)   
    elif newgirl["Mystique"].Foot:
        call MystiqueFace("sad") 
        ch_m "I'm not feeling it today. . ."       
    else:
        call MystiqueFace("normal", 1)
        ch_m "I don't know about using my feet for. . . that."  
    $ newgirl["Mystique"].RecentActions.append("no foot")                      
    $ newgirl["Mystique"].DailyActions.append("no foot") 
    $ Tempmod = 0    
    return
    

label MystiqueFJ_Prep:
    if Trigger2 == "foot": 
        return
    
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
                
    call MystiqueFace("sexy")
    if newgirl["Mystique"].Forced:
        call MystiqueFace("sad")
    elif newgirl["Mystique"].Foot:
        $ newgirl["Mystique"].Brows = "confused"
        $ newgirl["Mystique"].Eyes = "sexy"
        $ newgirl["Mystique"].Mouth = "smile"
    
    if not newgirl["Mystique"].Foot:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 30) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)     
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no foot")
    $ newgirl["Mystique"].RecentActions.append("foot")                      
    $ newgirl["Mystique"].DailyActions.append("foot") 
  
label MystiqueFJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Mystique")
        call Mystique_Sex_Launch("foot")
        call MystiqueLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ newgirl["Mystique"].Brows = "angry"        
                    menu:
                        ch_m "Ouch, foot cramp, can we take a break?"
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_FJAfter
                                call Mystique_Blowjob   
                        "How about a Handy?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_FJAfter
                                call Mystique_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump MystiqueFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Sex_Reset
                                $ Situation = "shift"
                                jump Mystique_FJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_m "Hey, I've got better things to do if you're going to be a dick about it."                                               
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)                     
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_FJAfter
        elif Cnt == 10 and newgirl["Mystique"].SEXP <= 100 and not ApprovalCheck("Mystique", 1200, "LO"):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Can we be done with this now? I'm getting sore."         
        #End Count check
        
        if not Speed:
            $ Speed = 1 

        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        
                        "Appearance" if P_Lvl >= 4:
                                call Mystique_Appearance               
                        
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

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0
                   
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if newgirl["Mystique"].Action and MultiAction:
                                                $ Situation = "shift"
                                                call Mystique_FJAfter                
                                                call Mystique_Blowjob
                                            else:
                                                ch_m "Actually I'm getting a bit worn out, let's finish up here. . ."
                                "How about a handjob?":
                                            if newgirl["Mystique"].Action and MultiAction:
                                                $ Situation = "shift"
                                                call Mystique_FJAfter                
                                                call Mystique_Handjob
                                            else:
                                                ch_m "Actually I'm getting a bit worn out, let's finish up here. . ."
                                         
                        "I also want to. . . [[Offhand]": #fix set this up
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I kinda need a break, so if we could wrap this up?"  
                                    
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_FJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Line = 0
                                    jump Mystique_FJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Sex_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_FJAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                                                
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_FJAfter            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump Mystique_FJAfter   
        #End orgasm
   
        if Round == 10:
            ch_m "It's kind of time to get moving."   
        elif Round == 5:
            ch_m "For real time's up."      
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, we need to take a break."
    
label Mystique_FJAfter:
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Foot += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 90, 5)
    
    if newgirl["Mystique"].Loc == bg_current and "noticed rogue" in newgirl["Mystique"].RecentActions: #If Mystique was participating
        $ R_LikeNewGirl["Mystique"] += 1
    
    if "Mystiquepedi" in Achievements:
            pass  
    elif newgirl["Mystique"].Foot >= 10:
            call MystiqueFace("smile", 1)
            ch_m "I guess I've gotten pretty smooth at the \"Mystiquepedi.\""
            $ Achievements.append("Mystiquepedi")
            $ newgirl["Mystique"].SEXP += 5          
    elif newgirl["Mystique"].Foot == 1:            
            $ newgirl["Mystique"].SEXP += 10
            if newgirl["Mystique"].Love >= 500:
                $ newgirl["Mystique"].Mouth = "smile"
                ch_m "I could feel you down there. . ."
            elif P_Focus <= 20:
                $ newgirl["Mystique"].Mouth = "sad"
                ch_m "Did that work out for you?"
    elif newgirl["Mystique"].Foot == 5:
                ch_m "Let me know any time you need me to \"foot you up.\""                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Ok, so what were you thinking?"
    else:
        call Mystique_Sex_Reset    
    call Checkout
    return

## end Mystique_Footjob //////////////////////////////////////////////////////////////////////


label Mystique_Les_Response(Girl="Rogue", Step=1, B=0, B2=0, Tempmod=0, Result=0, Approval = 0):
        #Dialog for responses to Lesbian scenes, Girl is the initial girl in the scene. Step is the phase of the conversation
        # call Mystique_Les_Response("Rogue",1)
        if newgirl["Mystique"].Les:
            $ Tempmod += 10
        if newgirl["Mystique"].SEXP >= 50:
            $ Tempmod += 25
        elif newgirl["Mystique"].SEXP >= 30:
            $ Tempmod += 15
        elif newgirl["Mystique"].SEXP >= 15:
            $ Tempmod += 5
                    
        elif newgirl["Mystique"].Inbt >= 750:
            $ Tempmod += 5
            
        if "exhibitionist" in newgirl["Mystique"].Traits:      
            $ Tempmod += (3*Taboo) 
            
        if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
            $ Tempmod += 10        
        elif "ex" in newgirl["Mystique"].Traits:
            $ Tempmod -= 40  
            
        if Girl == "Rogue":
                #if it's Rogue. . .
                if newgirl["Mystique"].LikeRogue >= 900:
                        $ B += 150
                elif newgirl["Mystique"].LikeRogue >= 800 or "poly rogue" in newgirl["Mystique"].Traits:
                        $ B += 100
                elif newgirl["Mystique"].LikeRogue >= 700:
                        $ B += 50
                elif newgirl["Mystique"].LikeRogue <= 200:
                        $ B -= 200
                elif newgirl["Mystique"].LikeRogue <= 500:
                        $ B -= 100
                        
        $ Approval = ApprovalCheck("Mystique", 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800
        
        if Step == 1:
            #this is if the first girl's check failed, but Mystique likes her.
            if Approval >= 2 or (Approval and B >= 150):
                call MystiqueFace("sexy", 1)
                ch_m "Oh, come on [Girl], wouldn't it be fun?"
                if B2 >= 100:
                    $ Result = 1
                    if Girl == "Rogue":
                            $ newgirl["Mystique"].LikeRogue += (int(B/10))
                            $ R_LikeNewGirl["Mystique"] += (int(B2/10))
            else:
                return Result
        
        if Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                call MystiqueFace("smile", 1)
                ch_m "Sure, sounds fun!"
                $ Result = 1
            elif Approval:
                call MystiqueFace("sly", 2)
                if B >= 100:
                        ch_m "I kinda want to, but I don't know. . ."
                if B >= 0:
                        ch_m "I don't know about doing it with her. . ."
                $ newgirl["Mystique"].Blush = 1
                menu:
                    extend ""
                    "Ok, that's fine. . .":
                            if B >= 100:                            
                                ch_m "You know what? I'm in."
                                $ Result = 1
                            else:
                                call MystiqueFace("smile")
                                ch_m "Thanks, that's really cool of you."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_m "Well, I guess I might." 
                                $ Result = 1
                            else:
                                call MystiqueFace("sad", 2)
                                ch_m "I don't think so." 
                    "Get in there, now.":
                            if ApprovalCheck("Mystique", 550, "OI", TabM = 2):
                                call MystiqueFace("sadside", 1)
                                ch_m "Ok, FINE."
                                $ Result = 1
                            else:
                                call MystiqueFace("angry")
                                ch_m "Like hell I will."  
                                $ newgirl["Mystique"].RecentActions.append("angry")
                                $ newgirl["Mystique"].DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1)
                                if R_Les and newgirl["Mystique"].Les:
                                        ch_r "Come on Mystique, don't we have fun?"
                                else:
                                        ch_r "Come on Mystique, couldn't it be fun?"
                                $ newgirl["Mystique"].LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeNewGirl["Mystique"] += 5
                            if B >= 50:
                                call MystiqueFace("smile", 1)
                                ch_m "Heh, I guess you're right, [Girl]."
                                $ Result = 1
                            else:
                                call MystiqueFace("angry", 1, Eyes="side")
                                ch_m "Yeah, no, I really don't think so."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call MystiqueFace("smile", 1)
                            ch_m "Yeah, I mean I guess we could. . ."
                            $ Result = 1
                    else:
                            call MystiqueFace("sadside", 1)
                            ch_m "I don't think I could manage that. . ."
            
            if not Result:      
                #no approval
                $ newgirl["Mystique"].RecentActions.append("no lesbian")                      
                $ newgirl["Mystique"].DailyActions.append("no lesbian") 
                call MystiqueFace("sadside", 1)
                if B <= 0:
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], I just can't do that with her."
                if Taboo:
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], I just can't do that around here."
                if B >= 100:
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], I just can't do that with you around."
                else:
                    ch_m "I'm sorry, [newgirl[Mystique].Petname], I just can't do that."
                
        return Result

label Mystique_Appearance_HJ:
    menu:
        "Why don't you turn into Raven" if newgirl["Mystique"].LooksLike != "Raven":
            ch_m "Sure"
            $ newgirl["Mystique"].LooksLike = "Raven"
            # call NewGirl_RemoveClothes("Mystique")
            call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Raven with your cock still inside her."
            else:
                "She turns into Raven."
            ch_p "Nice"
        "I preffer the real Raven" if newgirl["Mystique"].LooksLike != "Mystique":
            ch_m "Sure"
            $ newgirl["Mystique"].LooksLike = "Mystique"
            call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns back into her original form with your cock still inside her."
            else:
                "She turns back into her original form."
            ch_p "Perfection"
        "Why don't you turn into Emma" if newgirl["Mystique"].LooksLike != "Emma":
            ch_m "So you like blondes huh?"
            $ newgirl["Mystique"].LooksLike = "Emma"
            call NewGirl_RemoveClothes("Mystique")
            call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Emma with your cock still inside her."
            else:
                "She turns into Emma."
            ch_p "Nice"
        "Why don't you turn into Rogue" if newgirl["Mystique"].LooksLike != "Rogue":
            call NewGirl_FaceSpecial("Mystique", "surprised")
            ch_m "You want me to turn into my own daughter?"
            ch_m "That's dirty."
            call NewGirl_FaceSpecial("Mystique", "smile")
            ch_m "I like it."
            $ newgirl["Mystique"].LooksLike = "Rogue"
            call NewGirl_RemoveClothes("Mystique")
            call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Rogue with your cock still inside her."
            else:
                "She turns into Rogue."
            ch_p "Nice"
        "Why don't you turn into Kitty" if newgirl["Mystique"].LooksLike != "Kitty":
            call NewGirl_FaceSpecial("Mystique", "surprised")
            ch_m "So you want me to turn into that brat, huh?"
            call NewGirl_FaceSpecial("Mystique", "smile")
            ch_m "Ok."
            $ newgirl["Mystique"].LooksLike = "Kitty"
            call NewGirl_RemoveClothes("Mystique")
            call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Kitty with your cock still inside her."
            else:
                "She turns into Kitty."
            ch_p "Nice"
        "Nevermind":
            pass 
    return

label Mystique_Appearance_BJ:
    menu:
        "Why don't you turn into Raven" if newgirl["Mystique"].LooksLike != "Raven":
            ch_m "Sure"
            $ newgirl["Mystique"].LooksLike = "Raven"
            # call NewGirl_RemoveClothes("Mystique")
            # call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Raven with your cock still inside her."
            else:
                "She turns into Raven."
            ch_p "Nice"
        "I preffer the real Raven" if newgirl["Mystique"].LooksLike != "Mystique":
            ch_m "Sure"
            $ newgirl["Mystique"].LooksLike = "Mystique"
            # call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns back into her original form with your cock still inside her."
            else:
                "She turns back into her original form."
            ch_p "Perfection"
        "Why don't you turn into Emma" if newgirl["Mystique"].LooksLike != "Emma":
            ch_m "So you like blondes huh?"
            $ newgirl["Mystique"].LooksLike = "Emma"
            call NewGirl_RemoveClothes("Mystique")
            # call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Emma with your cock still inside her."
            else:
                "She turns into Emma."
            ch_p "Nice"
        "Why don't you turn into Rogue" if newgirl["Mystique"].LooksLike != "Rogue":
            call NewGirl_FaceSpecial("Mystique", "surprised")
            ch_m "You want me to turn into my own daughter?"
            ch_m "That's dirty."
            call NewGirl_FaceSpecial("Mystique", "smile")
            ch_m "I like it."
            $ newgirl["Mystique"].LooksLike = "Rogue"
            call NewGirl_RemoveClothes("Mystique")
            # call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Rogue with your cock still inside her."
            else:
                "She turns into Rogue."
            ch_p "Nice"
        "Why don't you turn into Kitty" if newgirl["Mystique"].LooksLike != "Kitty":
            call NewGirl_FaceSpecial("Mystique", "surprised")
            ch_m "So you want me to turn into that brat, huh?"
            call NewGirl_FaceSpecial("Mystique", "smile")
            ch_m "Ok."
            $ newgirl["Mystique"].LooksLike = "Kitty"
            call NewGirl_RemoveClothes("Mystique")
            # call Mystique_HJ_FixPos("L")
            if P_Cock == "anal" or P_Cock == "in":
                "She turns into Kitty with your cock still inside her."
            else:
                "She turns into Kitty."
            ch_p "Nice"
        "Nevermind":
            pass 
    return

#End Mystique_Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >