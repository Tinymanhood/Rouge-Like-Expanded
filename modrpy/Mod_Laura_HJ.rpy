## L_Handjob //////////////////////////////////////////////////////////////////////
label L_Handjob:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if newgirl["Laura"].Hand >= 7: # She loves it
        $ Tempmod += 10
    elif newgirl["Laura"].Hand >= 3: #You've done it before several times
        $ Tempmod += 7
    elif newgirl["Laura"].Hand: #You've done it before
        $ Tempmod += 3
        
    if newgirl["Laura"].Addict >= 75 and newgirl["Laura"].Swallow >=3: #She's really strung out and has swallowed
        $ Tempmod += 15
    if newgirl["Laura"].Addict >= 75:
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (3*Taboo)    
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 40 
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount    
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
        
    if "no hand" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hand" in newgirl["Laura"].RecentActions else 0    
        
    $ Approval = ApprovalCheck("Laura", 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
        if Approval > 2:                                                      # fix, add Laura auto stuff here
            if Trigger2 == "jackin":
                "Laura brushes your hand aside and starts stroking your cock."
            else:
                "Laura draws her fingers across your cock, and begins to stroke it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)                     
                    "Laura continues her actions."
                "Praise her.":       
                    call LauraFace("sexy", 1)                    
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
                    ch_p "Oooh, that's good, [newgirl[Laura].Pet]."
                    call Laura_Namecheck
                    "Laura continues her actions."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                "Ask her to stop.":
                    call LauraFace("surprised")       
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [newgirl[Laura].Pet]."
                    call Laura_Namecheck
                    "Laura puts it down."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                    return            
            if Trigger:
                $ Trigger3 = "hand"
                return
            jump L_HJ_Prep
        else:                
            $ Tempmod = 0                               # fix, add Laura auto stuff here
            $ Trigger2 = 0
            return            
    
    if not newgirl["Laura"].Hand and "no hand" not in newgirl["Laura"].RecentActions:        
        call LauraFace("sly", 2)
        ch_l "You'd like me to take care of that for you?"
            
    if not newgirl["Laura"].Hand and Approval:                                                 #First time dialog        
        if newgirl["Laura"].Forced: 
            call LauraFace("sad",1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
        elif newgirl["Laura"].Love >= (newgirl["Laura"].Obed + newgirl["Laura"].Inbt):
            call LauraFace("sexy",1)
            $ newgirl["Laura"].Brows = "sad"
            $ newgirl["Laura"].Mouth = "smile" 
            ch_l "I suppose you've earned something. . ."            
        elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
            call LauraFace("normal",1)
            ch_l "If that's what you'd like, [newgirl[Laura].Petname]. . ."            
        elif newgirl["Laura"].Addict >= 50:
            call LauraFace("manic", 1)
            ch_l "Mmmmmmmm. . ."  
        else: # Uninhibited 
            call LauraFace("lipbite",1,Eyes="side")    
            ch_l "I suppose. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Laura"].Forced: 
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            ch_l "No more than that?" 
        elif not Taboo and "tabno" in newgirl["Laura"].DailyActions:        
            ch_l "Here, hmm?. . ."    
        elif "hand" in newgirl["Laura"].RecentActions:
            call LauraFace("sexy", 1)
            ch_l "I will need to grade papers later, you know. . ."
            jump L_HJ_Prep
        elif "hand" in newgirl["Laura"].DailyActions:
            call LauraFace("sexy", 1)
            $ Line = renpy.random.choice(["Another?",   
                "You're going to wear out my arm.", 
                "Didn't get enough earlier?",
                "My hand's a bit sore from earlier.",
                "My hand's rather sore from before."]) 
            ch_l "[Line]"
        elif newgirl["Laura"].Hand < 3:        
            call LauraFace("sly", 1)
            ch_l "Enjoyed last time?. . ."        
        else:       
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want more?",                 
                "So you'd like another?",                 
                "More of this? [fist pumping hand gestures]", 
                "Oh, did you want some attention?"]) 
            ch_l "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
            ch_l "Very well." 
        elif "no hand" in newgirl["Laura"].DailyActions:               
            ch_l "Oh, fine!"   
        else:
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Oh, I suppose.",                 
                "I'll do it.",                 
                "Well, give it here.", 
                "I suppose I could. . .",
                "Fine. . . [She gestures for you to come over].",
                "Ok, ok."]) 
            ch_l "[Line]"
            $ Line = 0
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
        jump L_HJ_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry")
        if "no hand" in newgirl["Laura"].RecentActions:  
            ch_l "You need to learn to take\"no\" for an answer, [newgirl[Laura].Petname]."
        elif "no hand" in newgirl["Laura"].DailyActions:       
            ch_l "I told you \"no,\" [newgirl[Laura].Petname]."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, this is too public!"     
        elif not newgirl["Laura"].Hand:
            call LauraFace("bemused")
            ch_l "Are you sure though, [newgirl[Laura].Petname]?. . ."
        else:
            call LauraFace("bemused")
            ch_l "I'd rather not right now though."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "Quite alright."              
                return
            "Maybe later?" if "no hand" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l ". . ."
                ch_l "I couldn't rule it out. . ."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no hand")                      
                $ newgirl["Laura"].DailyActions.append("no hand")            
                return
            "I'd really appreciate it. . .":             
                #if Approval:    #she's doing it
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Oh, I suppose.",                 
                        "I'll do it.",                 
                        "Well, give it here.", 
                        "I suppose I could. . .",
                        "Fine. . . [She gestures for you to come over].",
                        "Ok, ok."]) 
                    ch_l "[Line]"
                    $ Line = 0                   
                    jump L_HJ_Prep
                    
            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                call LauraFace("angry")
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("angry")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)                 
                    ch_l "Hm. Alright, but don't push your luck, [newgirl[Laura].Petname]."  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    $ newgirl["Laura"].Forced = 1  
                    jump L_HJ_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -15)     
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Laura"].Girl_Arms = 1 
    if "no hand" in newgirl["Laura"].DailyActions:
        call LauraFace("angry", 1)
        ch_l "Don't make me repeat myself."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "Even that is asking too much."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5)    
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2) if newgirl["Laura"].Love > 300 else newgirl["Laura"].Love
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)    
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    # elif Taboo:                             # she refuses and this is too public a place for her
    #     call LauraFace("angry", 1)          
    #     $ newgirl["Laura"].DailyActions.append("tabno") 
    #     ch_l "I couldn't possibly do that. . . here!"
    #     $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5)  
    #     $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)   
    elif newgirl["Laura"].Hand:
        call LauraFace("sad") 
        ch_l "I'd really rather not. . ."       
    else:
        call LauraFace("normal", 1)
        ch_l "No, I don't think so, [newgirl[Laura].Petname]."  
    $ newgirl["Laura"].RecentActions.append("no hand")                      
    $ newgirl["Laura"].DailyActions.append("no hand") 
    $ Tempmod = 0    
    return
    

label L_HJ_Prep:
    if Trigger2 == "hand": 
        return
    
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
                
    call LauraFace("sexy")
    if newgirl["Laura"].Forced:
        call LauraFace("sad")
    elif newgirl["Laura"].Hand:
        $ newgirl["Laura"].Brows = "confused"
        $ newgirl["Laura"].Eyes = "sexy"
        $ newgirl["Laura"].Mouth = "smile"
        
    # call Seen_First_Peen("Laura",Partner) #shit removed
    call Laura_HJ_Launch("L")
    if not newgirl["Laura"].Hand:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -20)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 25)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 30) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 20)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 20)     
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no hand")
    $ newgirl["Laura"].RecentActions.append("hand")                      
    $ newgirl["Laura"].DailyActions.append("hand") 
  
label L_HJ_Cycle:    
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_HJ_Launch    
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
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
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        # "Other options":
                        #         menu:   
                        #             "I also want to fondle her breasts." if Trigger2 != "fondle breasts":
                        #                     if newgirl["Laura"].Action and MultiAction:
                        #                         $ Trigger2 = "fondle breasts"
                        #                         "You start to fondle her breasts."
                        #                         $ newgirl["Laura"].Action -= 1
                        #                     else:
                        #                         ch_l "Hmm, I think we've probably done enough for now. . ."  
                                         
                        #             "Shift primary action":
                        #                     if newgirl["Laura"].Action and MultiAction:
                        #                             menu:
                        #                                 "How about a blowjob?":
                        #                                             if newgirl["Laura"].Action and MultiAction:
                        #                                                 $ Situation = "shift"
                        #                                                 call L_HJ_After                
                        #                                                 call E_Blowjob
                        #                                             else:
                        #                                                 ch_l "Hmm, I think we've probably done enough for now. . ."
                                                                        
                        #                                 "Never Mind":
                        #                                         jump L_HJ_Cycle
                        #                     else: 
                        #                         ch_l "Hmm, I think we've probably done enough for now. . ."           
                    
                        #             "Threesome actions (locked)" if not Partner: 
                        #                 pass
                        #             "Threesome actions" if Partner:   
                        #                 menu:
                        #                     "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                        #                                 call Laura_Les_Change
                        #                     "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                        #                                 pass
                        #                     "Ask [Partner] to do something else":
                        #                                 if Partner == "Rogue":
                        #                                     call Rogue_Three_Change("Laura")
                        #                                 elif Partner == "Kitty":
                        #                                     call Kitty_Three_Change("Laura")                                                  
                        #                     "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                        #                                 $ ThreeCount = 0                                                            
                        #                     "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                        #                                 $ ThreeCount = 0          
                        #                     "Swap to [Partner]":
                        #                                 call Trigger_Swap("Laura")
                        #                     "Undress [Partner]":
                        #                                 if Partner == "Rogue":
                        #                                         call R_Undress   
                        #                                 elif Partner == "Kitty":
                        #                                         call K_Undress 
                        #                     "Clean up Partner":
                        #                                 if Partner == "Rogue" and R_Spunk:
                        #                                         call Rogue_Cleanup("ask")    
                        #                                 elif Partner == "Kitty" and K_Spunk:
                        #                                         call Kitty_Cleanup("ask")  
                        #                                 else:
                        #                                         "She seems fine."
                        #                                         jump L_HJ_Cycle 
                        #                     "Never mind":
                        #                                 jump L_HJ_Cycle 
                        #             "Undress Laura":
                        #                     call E_Undress   
                        #             "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                        #                     pass  
                        #             "Clean up Laura" if newgirl["Laura"].Spunk:
                        #                     call Laura_Cleanup("ask")                                         
                        #             "Never mind":
                        #                     jump L_HJ_Cycle 
                                                   
                        # "Back to Sex Menu" if MultiAction: 
                        #             ch_p "Let's try something else."
                        #             call Laura_HJ_Reset
                        #             $ Situation = "shift"
                        #             $ Line = 0
                        #             jump L_HJ_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_HJ_Reset
                                    $ Line = 0
                                    jump L_HJ_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")    
        #call Sex_Dialog("Laura",Partner)
        #Applying player's satisfaction
        $ P_Focus = Statupdate("Player", "Focus", P_Focus, 200, Speed*10) #instead of sex_dialog
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            #call PE_Cumming
                            call Laura_No_Cum
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_HJ_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump L_HJ_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call E_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump L_HJ_After
                       
                    if Line == "came": #ex P_Focus <= 20: 
                            #If you've just cum,  
                            $ Line = 0
                            if not P_Semen:
                                "You're emptied out, you should probably take a break."
                            
                            
                            if "unsatisfied" in newgirl["Laura"].RecentActions:#And Laura is unsatisfied,  
                                    "Laura still seems a bit unsatisfied with the experience."
                                    menu:
                                        "Finish her?"
                                        "Yes, keep going for a bit.":
                                            $ Line = "You get back into it" 
                                        "No, I'm done.":
                                            "You pull back."
                                            jump L_HJ_After    
        if Partner:
                #Checks if partner could orgasm
                if Partner == "Rogue" and R_Lust >= 100:                                          
                    call R_Cumming
                elif Partner == "Kitty" and K_Lust >= 100:                                          
                    call K_Cumming
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        # if Cnt == 20:
        #             $ newgirl["Laura"].Brows = "angry"    
        #             ch_l "Hmm, I'm getting a bit of a cramp here."    
        #             menu:
        #                 ch_l "Mind if we take a break?"
        #                 "How about a BJ?" if newgirl["Laura"].Action and MultiAction:
        #                         $ Situation = "shift"
        #                         call L_HJ_After
        #                         call E_Blowjob       
        #                 "Finish up." if P_FocusX:
        #                         "You release your concentration. . ."             
        #                         $ P_FocusX = 0
        #                         $ P_Focus += 15
        #                         $ Cnt += 1
        #                         "[Line]"
        #                         jump L_HJ_Cycle
        #                 "Let's try something else." if MultiAction: 
        #                         $ Line = 0
        #                         call Laura_HJ_Reset
        #                         $ Situation = "shift"
        #                         jump L_HJ_After
        #                 "No, get back down there.":
        #                         if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):
        #                             $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
        #                             $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
        #                             $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
        #                             "She scowls but gets back to work."
        #                         else:
        #                             call LauraFace("angry", 1)   
        #                             "She scowls at you, drops you cock and pulls back."
        #                             ch_l "You know, I do have better things to do with my time than this."                                               
        #                             $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
        #                             $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
        #                             $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
        #                             $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)                     
        #                             $ newgirl["Laura"].RecentActions.append("angry")
        #                             $ newgirl["Laura"].DailyActions.append("angry")   
        #                             jump L_HJ_After
        # elif Cnt == 10 and newgirl["Laura"].SEXP <= 100 and not ApprovalCheck("Laura", 1200, "LO"):
        #             $ newgirl["Laura"].Brows = "confused"
        #             ch_l "Are you certain you didn't have anything else in mind?"         
        #End Count check
                   
        if Round == 10:
            ch_l "It's about time for a break."     
        elif Round == 5:
            ch_l "Ok, that's enough, for now. . ."    
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, seriously, I'm putting it down for a minute."
    
label L_HJ_After:
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].Hand += 1  
    $ newgirl["Laura"].Action -=1
    $ newgirl["Laura"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Laura"].Addictionrate += 1        
    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)
    
    if R_Loc == bg_current and "noticed Laura" in R_RecentActions: #If Rogue was participating
        $ R_LikeLaura += 1
    if K_Loc == bg_current and "noticed Laura" in K_RecentActions: #If Kitty was participating
        $ K_LikeLaura += 1
                    
    if "Laura Handi-Queen" in Achievements:
            pass  
    elif newgirl["Laura"].Hand >= 10:
            call LauraFace("smile", 1)
            ch_l "I've apparently become the \"queen\" of handjobs as well."
            $ Achievements.append("Laura Handi-Queen")
            $newgirl["Laura"].SEXP += 5          
    elif newgirl["Laura"].Hand == 1:            
            $newgirl["Laura"].SEXP += 10
            if not newgirl["Laura"].Forced:
                $ newgirl["Laura"].Mouth = "smile"
                ch_l "What a lovely experience. . ."
            elif P_Focus <= 20:
                $ newgirl["Laura"].Mouth = "sad"
                ch_l "Was that sufficient?"
    elif newgirl["Laura"].Hand == 5:
                ch_l "Please do call again. . ."                  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_l "Very well, what did you want to do?"
    else:
        call Laura_HJ_Reset    
    call Checkout
    return

## end L_Handjob //////////////////////////////////////////////////////////////////////


# Laura Lusty face check ////////////////////////////////////////////////////////////////////////////////
label LauraLust(Extreme = 0, Kissing = 0):
                
    if newgirl["Laura"].Lust >= 90:        
            $ newgirl["Laura"].Blush = 2
    elif newgirl["Laura"].Lust >= 40:        
            $ newgirl["Laura"].Blush = 1 
        
    if newgirl["Laura"].Lust >= 80:
            $ newgirl["Laura"].Wet = 2 
    elif newgirl["Laura"].Lust >= 50:
            $ newgirl["Laura"].Wet = 1
            
    if newgirl["Laura"].Loc == "bg teacher" and not Extreme:
            #this prevents her face from changing if she's just being a teacher.
            return
       
    if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1
    elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
            #if the girls are kissing or all three are
            $ Kissing = 1   
    elif Partner != "Laura":
            #If Laura is kissing and is primary
            if Trigger == "kiss you" or Trigger2 == "kiss you":  
                $ Kissing = 1
    elif Trigger4 == "kiss you":   
            #If Laura is kissing you in a threesome action
            $ Kissing = 1
            
    if Kissing:
            $ newgirl["Laura"].Eyes = "closed"
            if newgirl["Laura"].Kissed >= 10 and newgirl["Laura"].Inbt >= 300:
                $ newgirl["Laura"].Mouth = "sucking"
            elif newgirl["Laura"].Kissed > 1 and newgirl["Laura"].Addict >= 50:            
                $ newgirl["Laura"].Mouth = "sucking"
            else:
                $ newgirl["Laura"].Mouth = "kiss"
                
    else:    
            #If Laura is not kissing someone
            if newgirl["Laura"].Lust >= 90:
                    $ newgirl["Laura"].Eyes = "closed"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "surprised"
            elif newgirl["Laura"].Lust >= 70:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "lipbite"
            elif newgirl["Laura"].Lust >= 50 and not Extreme:
                    $ newgirl["Laura"].Eyes = "squint"
                    $ newgirl["Laura"].Brows = "sad"
                    $ newgirl["Laura"].Mouth = "lipbite"
            elif newgirl["Laura"].Lust >= 30 and not Extreme:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "normal"
                    $ newgirl["Laura"].Mouth = "smirk"
            elif not Extreme:
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "normal"
                    $ newgirl["Laura"].Mouth = "smirk"    
    
    if Partner == "Laura" and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                    $ newgirl["Laura"].Mouth = "tongue"  
    elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                    $ newgirl["Laura"].Mouth = "tongue"  
                    
    if newgirl["Laura"].OCount >= 10:   
            #If you've fucked her senseless
            $ newgirl["Laura"].Eyes = "stunned"
            $ newgirl["Laura"].Mouth = "tongue"   
                
    return

# End faces

label Laura_No_Cum:
    #this is a temporary thing until this system is complete
    call LauraFace("confused", B=1)
    if Situation == "warn":
        ch_p "I'm about to. . . blow. . ."
        ch_l "Oh? How thoughtful."
    elif Situation == "asked":        
        ch_p "I'm about to. . . blow. . ."
        ch_p "Could I. . . come in your mouth?"
        ch_l "Hmmm, I don't think so."
    else:
        ch_l "Oh, I know that look, I've seen it too many times. You're about to make a mess on me aren't you."         
    $ newgirl["Laura"].Girl_Arms = 2
    call LauraFace("sly", B=2)
    ch_l "I don't have time to go get cleaned up. . ."
    ch_l "For now why don't you just come in my hand here. . ."
    $ newgirl["Laura"].Spunk.append("hand") 
    call LauraFace("sexy", B=2)
    "She grabs the head of your cock and you gush into it."
    #ch_l "See? That wasn't so hard."
    call Laura_HJ_Reset   
    ch_l "Now I should get going, see you soon"      
    return
