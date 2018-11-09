## K_Handjob //////////////////////////////////////////////////////////////////////
label K_Handjob:
    call Shift_Focus("Kitty")
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
                    call KittyFace("sexy, 1")                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
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
        call KittyFace("confused", 2)
        ch_k "So you want a handy then?"
        $ K_Blush = 1
            
    if not K_Hand and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1)
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it could be interesting. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1)
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "I kind of {i}need{/i} to. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1)    
            ch_k "I guess. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's it, right?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Well, I guess if it's here. . ."    
        elif "hand" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "You're giving me carpal tunnel. . ."
            jump KHJ_Prep
        elif "hand" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My hand's kinda sore from earlier.",
                "My hand's kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Hand < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic fingers. . ."        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want some of this?",                 
                "So you'd like another handy?",                 
                "A little. . . [fist pumping hand gestures]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine." 
        elif "no hand" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1)
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
        call KittyFace("angry")
        if "no hand" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no hand" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no hand" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Hand:
            call KittyFace("bemused")
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah."              
                return
            "Maybe later?" if "no hand" not in K_DailyActions:
                call KittyFace("sexy")  
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
                    call KittyFace("sexy")     
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
                    call KittyFace("sad")
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
        call KittyFace("angry", 1)
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "Not even if you had a ten foot pole."
        call KittyFace("surprised", 2)
        ch_k "I mean. . ."
        call KittyFace("angry", 1)        
        ch_k "You know what I mean!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)   
    elif K_Hand:
        call KittyFace("sad") 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1)
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
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Kitty_HJ_Launch("L")
    if not K_Hand:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)     
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no hand")
    $ K_RecentActions.append("hand")                      
    $ K_DailyActions.append("hand") 
  
label KHJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Kitty")
        call Kitty_HJ_Launch    
        call KittyLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, hand cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_HJAfter
                                call K_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump KHJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_HJ_Reset
                                $ Situation = "shift"
                                jump K_HJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1)   
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
                            menu:
                                "How about a blowjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_HJAfter                
                                                call K_Blowjob
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
                                    call K_Fondle_Breasts
                                    if Trigger2:
                                         $ K_Action -= 1
                                         
                        "Let's try something else." if MultiAction: 
                                    call Kitty_HJ_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_HJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_HJ_Reset
                                    $ Line = 0
                                    jump K_HJAfter
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_HJ_Reset
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
                            call K_Cumming
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
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label K_HJAfter:
    call KittyFace("sexy") 
    
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
            call KittyFace("smile", 1)
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
        call Kitty_HJ_Reset    
    call Checkout
    return

## end K_Handjob //////////////////////////////////////////////////////////////////////


## K_Titjob //////////////////////////////////////////////////////////////////////              Not finished
label K_Titjob:
    return #fix remove when this works
    
    call Shift_Focus("Kitty")
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
            call Kitty_TJ_Launch("L")            
            "Kitty slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)                     
                    "Kitty starts to slide them up and down."
                "Praise her.":       
                    call KittyFace("sexy, 1")                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Oh, that sounds like a good idea, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":     
                    call KittyFace("confused")  
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty lets it drop out from between her breasts."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    call Kitty_TJ_Reset  
                    return            
            jump KTJ_Cycle
        else:                
            $ Tempmod = 0                               # fix, add kitty auto stuff here
            $ Trigger2 = 0
            return            
    
    if not K_Tit and "no titjob" not in K_RecentActions:        
        call KittyFace("surprised", 1)
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
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "Huh, well that's certainly one way to get off."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "If that's what you want. . ."              
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Hmmmm. . . ."     
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "Heh, might be fun."      
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "This isn't going to become a habit, will it?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."   
        elif "titjob" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Mmm, again? Ok, let me get the girls ready."
            jump KTJ_Prep
        elif "titjob" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My tits are still a bit sore from earlier."]) 
            ch_k "[Line]"
        elif K_Tit < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another titjob?"        
        else:       
            call KittyFace("sexy", 1)
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
            call KittyFace("sad")
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Well, there are worst ways to get you off. . ." 
        elif "no titjob" in K_DailyActions:               
            ch_k "Hmm, I suppose. . ."       
        else:
            call KittyFace("sexy", 1)
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
        call KittyFace("angry")
        if "no titjob" in K_RecentActions:  
            ch_k "I {i}just{/i} told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no titjob" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif "no titjob" in K_DailyActions:       
            ch_k "I already told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "This is just way too exposed!"     
        elif not K_Tit:
            call KittyFace("bemused")
            ch_k "I'm not really up for that, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not, right now [K_Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no titjob" not in K_DailyActions:
                call KittyFace("sexy")  
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
                    call KittyFace("sexy")     
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
                        call KittyFace("confused", 1)
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
                        call KittyFace("confused", 1)
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
                call Kitty_Namecheck
                $ Approval = ApprovalCheck("Kitty", 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
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
        call KittyFace("angry", 1)
        ch_k "Look, I already told you no thanks, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "I'm not that kind of girl."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)      
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "You really expect me to do that here? You realize how. . . exposed that would be?"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_Blow:
        call KittyFace("sad") 
        ch_k "I think I'll let you know when I want you touching these again."       
    else:
        call KittyFace("normal", 1)
        ch_k "How about let's not, [K_Petname]."
    $ K_RecentActions.append("no titjob")                      
    $ K_DailyActions.append("no titjob") 
    $ Tempmod = 0    
    return
    
label KTJ_Prep:
      
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)

        
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Tit:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
        
    call Kitty_TJ_Launch("L")    
    if not K_Tit:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -25)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 30)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30)   
    
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0  
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no titjob")
    $ K_RecentActions.append("titjob")                      
    $ K_DailyActions.append("titjob") 

label KTJ_Cycle: #Repeating strokes  
    call Shift_Focus("Kitty")  
    call Kitty_TJ_Launch
        
    call KittyLust            
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
                call K_TJAfter
                call K_Blowjob 
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
                call Kitty_TJ_Reset
                $ Situation = "shift"
                jump K_TJAfter
            "No, get back down there.":
                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                    "She grumbles but gets back to work."
                else:
                    call KittyFace("angry", 1)   
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
                    call K_TJAfter                
                    call K_Blowjob
                else:
                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
            "How about a handy?":
                if K_Action and MultiAction:
                    $ Situation = "shift"
                    call K_BJAfter
                    call K_Handjob
                else:
                    ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
            "I also want to fondle her breasts." if K_Action and MultiAction:
                $ Trigger2 = "fondle breasts"
                $ Situation = "auto"
                call K_Fondle_Breasts
                if Trigger2:
                     $ K_Action -= 1               
            "Let's try something else." if MultiAction:                
                $ Line = 0
                call Kitty_TJ_Reset
                $ Situation = "shift"
                jump K_TJAfter
            "Let's stop for now." if not MultiAction:                
                $ Line = 0
                call Kitty_TJ_Reset
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
    
    call Kitty_Offhand                                                            #Offhand and reduce addiciton per stroke        
    $ K_Addict -= 2          
    
    if P_Focus >= 100 or K_Lust >= 100:                                     #If either of you could cum    
        if P_Focus >= 100:                                                  #You cum             
            call PK_Cumming
            if "angry" in K_RecentActions:  
                call Kitty_TJ_Reset
                return    
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
            if 100 > K_Lust >= 70 and K_OCount < 2:             
                $ K_RecentActions.append("unsatisfied")                      
                $ K_DailyActions.append("unsatisfied") 
            
            if P_Focus > 80:
                jump K_TJAfter   
        
        if K_Lust >= 100:                                                   #and Kitty cums                    
            call K_Cumming
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
        call KittyFace("bemused", 0)
        $ Line = 0
        ch_k "Ok, [K_Petname], that's enough of that for now."
        
label K_TJAfter:
    $ K_Tit += 1
    
    call KittyFace("sexy")  
        
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
        call Kitty_TJ_Reset    
    call Checkout
    return

## end K_Titjob //////////////////////////////////////////////////////////////////////

# K_Blowjob //////////////////////////////////////////////////////////////////////

label K_Blowjob:
    call Shift_Focus("Kitty")
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
                    call KittyFace("sexy, 1")                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                    ch_p "Hmmm, keep doing that, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":     
                    call KittyFace("surprised")  
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
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
        call KittyFace("surprised", 2)
        $ K_Mouth = "kiss"
        ch_k "You want me to suck your dick?"
        if K_Hand:          
            $ K_Mouth = "smile"
            ch_k "Not satisfied with handies?"        
        $ K_Blush = 1
            
    if not K_Blow and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy")
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I have wondered what you. . . taste like."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal")
            ch_k "If you want me to. . ."               
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "My mouth is watering. . ."   
        else: # Uninhibited 
            call KittyFace("sad")
            $ K_Mouth = "smile"             
            ch_k "[K_Like]sure. . ."       
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "You want me to do that again?"
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Ok, I guess this is private enough. . ."    
        elif "blow" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "Mmm, again? [[stretches her jaw]"
            jump KBJ_Prep                
        elif "blow" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",   
                "You're going to give me lockhee- . . . jaw.", 
                "Let me get some saliva going.",
                "Didn't get enough earlier?",
                "My jaw's still a bit sore from earlier.",
                "My jaw's still a bit sore from earlier."]) 
            ch_k "[Line]"
        elif K_Blow < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "So you'd like another blowjob?"        
        else:       
            call KittyFace("sexy", 1)
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
            call KittyFace("sad")
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Whatever."    
        elif "no blow" in K_DailyActions:               
            ch_k "Ok, fine, I suppose it isn't {i}sooo{/i} bad. . ."  
        else:
            call KittyFace("sexy", 1)
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
        call KittyFace("angry")
        if "no blow" in K_RecentActions:  
            ch_k "What did I[K_like]{i}just{/i} tell you [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no blow" in K_DailyActions:  
            ch_k "I told you, not in public!"  
        elif "no blow" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I told you this is too public!"      
        elif not K_Blow:
            call KittyFace("bemused")
            ch_k "I don't know about the taste, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Later, [K_Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Aw, it's ok, [K_Petname]."              
                return
            "Maybe later?" if "no blow" not in K_DailyActions:
                call KittyFace("sexy")  
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
                    call KittyFace("sexy")     
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
                        call KittyFace("confused", 1)
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
                call Kitty_Namecheck
                $ Approval = ApprovalCheck("Kitty", 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad")
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
        call KittyFace("angry", 1)
        ch_k "You can eat a dick, 'cos I'm not."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
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
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "This is way too exposed!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)    
        return                
    elif K_Blow:
        call KittyFace("sad") 
        ch_k "No, not this time."       
    else:
        call KittyFace("normal", 1)
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
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
    elif K_Hand:
        $ K_Brows = "confused"
        $ K_Eyes = "sexy"
        $ K_Mouth = "smile"
    
    call Kitty_BJ_Launch("L")
    if not K_Blow:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -70)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 45)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 60) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 35)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 40)     
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no blow")
    $ K_RecentActions.append("blow")                      
    $ K_DailyActions.append("blow")     

label KBJ_Cycle: #Repeating strokes  
    while Round >=0:
        call Shift_Focus("Kitty")
        call Kitty_BJ_Launch    
        call KittyLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
         
        if Cnt == (10 + K_Blow):
                $ K_Brows = "angry"        
                menu:
                    ch_k "I'm[K_like]totally worn out here. Can we do something else?"
                    "How about a Handy?" if K_Action and MultiAction:
                            $ Situation = "shift"
                            call K_BJAfter
                            call K_Handjob 
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
                            call Kitty_BJ_Reset
                            $ Situation = "shift"
                            jump K_BJAfter
                    "No, get back down there.":
                            if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                call KittyFace("angry", 1)  
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
                            menu:
                                "How about a handy?":
                                        if K_Action and MultiAction:
                                            $ Situation = "shift"
                                            call K_BJAfter
                                            call K_Handjob
                                        else:
                                            ch_k "I'm kinda tired, could we just wrap this up. . ."
                                "How about a titjob?":
                                        if K_Action and MultiAction:
                                            $ Situation = "shift"
                                            call K_BJAfter
                                            call K_Titjob
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
                                call Kitty_BJ_Reset
                                $ Situation = "shift"
                                jump K_BJAfter
                        "Let's stop for now." if not MultiAction: 
                                $ Line = 0
                                call Kitty_BJ_Reset
                                jump K_BJAfter 
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call Kitty_BJ_Reset
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
                            call K_Cumming
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
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, I gotta rest me jaw for a minute. . ."

label K_BJAfter:    
    call KittyFace("sexy")  
        
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
        call KittyFace("smile", 1)
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
                call KittyFace("smile", 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 10) 
            "[[shake head \"no\"]":        
                if ApprovalCheck("Kitty", 500, "O"):
                    call KittyFace("sad", 2)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                else:
                    call KittyFace("angry", 2)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -25)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                ch_k ". . ."         
                call KittyFace("sad", 1)
    
    $ Tempmod = 0    
    if Situation != "shift":
        call Kitty_BJ_Reset    
    call Checkout
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
    call Shift_Focus("Kitty")
    call K_Dildo_Check    
    if not _return:
        return 

    if K_DildoP: #You've done it before
        $ Tempmod += 15
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
                            call KittyFace("sexy, 1")                    
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                            ch_p "Oh yeah, [K_Pet], let's do this."
                            call Kitty_Namecheck
                            "You grab the dildo and slide it in."
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        "Ask her to stop.":
                            call KittyFace("surprised")       
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [K_Pet]."
                            call Kitty_Namecheck
                            "Kitty sets the dildo down."
                            call KittyOutfit
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
                call KittyFace("surprised", 1)
                
                if (K_DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                    "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    call KittyFace("sexy")
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
                                call KittyFace("sexy", 1)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                                ch_k "Well, now that you mention it. . ."
                                jump KDP_Prep
                            "You pull back before you really get it in."                    
                            call KittyFace("bemused", 1)
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
                                call KittyFace("angry")
                                "Kitty shoves you away and slaps you in the face."
                                ch_k "Jerk!"
                                ch_k "Ask nice if you want to stick something in my ass!"                                               
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Kitty_SexSprite"):
                                    call Kitty_Sex_Reset 
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")                          
                            else:
                                call KittyFace("sad")
                                "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump KDP_Prep
                return             
    #end Auto
   
    if not K_DildoP:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "Hmmm, so you'd like to try out some toys?"    
            if K_Forced:
                call KittyFace("sad")
                ch_k "I suppose there are worst things you could ask for."
            
    if not K_DildoP and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I've had a reasonable amount of experience with these, you know. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun with a partner. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "The toys again?" 
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo pussy" in K_RecentActions:
                call KittyFace("sexy", 1)
                ch_k "Mmm, again? Ok, let's get to it."
                jump KDP_Prep
            elif "dildo pussy" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoP < 3:        
                call KittyFace("sexy", 1)
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my again?"       
            else:       
                call KittyFace("sexy", 1)
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
                call KittyFace("sad")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            else:
                call KittyFace("sexy", 1)
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
            call KittyFace("angry")
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"   
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "Stop swinging that thing around in public!"  
            elif not K_DildoP:
                call KittyFace("bemused")
                ch_k "I'm just not into toys, [K_Petname]. . ."
            else:
                call KittyFace("bemused")
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy")  
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
                        call KittyFace("sexy")     
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
                        call KittyFace("sad")
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
            call KittyFace("angry", 1)
            ch_k "I'm not going to let you use that on me."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)     
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1)         
            $ K_RecentActions.append("tabno")                       
            $ K_DailyActions.append("tabno") 
            ch_k "Not here!"     
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif K_DildoP:
            call KittyFace("sad") 
            ch_k "Sorry, you can keep your toys to yourself."     
    else:
            call KittyFace("normal", 1)
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
        call Kitty_Bottoms_Off
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo pussy")
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
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no dildo")
    $ K_RecentActions.append("dildo pussy")                      
    $ K_DailyActions.append("dildo pussy") 
    
label KDP_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call K_Pussy_Launch("dildo pussy")
        call KittyLust   
        
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
                                    call KittyFace("angry", 1)   
                                    call K_Pos_Reset
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
                                call K_Slap_Ass
                                jump KDP_Cycle  
                                
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
                                            "I want to stick a finger in her ass.":
                                                    $ Situation = "shift"
                                                    call KDP_After
                                                    call K_Insert_Ass    
                                            "Just stick a finger in her ass without asking.":
                                                    $ Situation = "auto"
                                                    call KDP_After
                                                    call K_Insert_Ass                                           
                                            "I want to shift the dilso to her ass.":
                                                    $ Situation = "shift"
                                                    call KDP_After
                                                    call K_Dildo_Ass   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KDP_After
                                    call Kitty_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDP_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump KDP_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto")
            
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset
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
                        call K_Cumming
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
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    
label KDP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset
        
    call KittyFace("sexy") 
    
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
                    call KittyFace("perplexed", 1)
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# end K_Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass    

label K_Dildo_Ass:
    call Shift_Focus("Kitty")
    call K_Dildo_Check
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
                        call KittyFace("sexy, 1")                    
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
                        ch_p "Oh yeah, [K_Pet], let's do this."
                        call Kitty_Namecheck
                        "You grab the dildo and slide it in."
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 85, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    "Ask her to stop.":
                        call KittyFace("surprised")       
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [K_Pet]."
                        call Kitty_Namecheck
                        "Kitty sets the dildo down."
                        call KittyOutfit
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
            call KittyFace("surprised", 1)
            
            if (K_DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Kitty is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call KittyFace("sexy")
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
                            call KittyFace("sexy", 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                            ch_k "Well, now that you mention it. . ."
                            jump KDA_Prep
                        "You pull back before you really get it in."                    
                        call KittyFace("bemused", 1)
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
                            call KittyFace("angry")
                            "Kitty shoves you away and slaps you in the face."
                            ch_k "Jerk!"
                            ch_k "Ask nice if you want to stick something in my ass!"                                                  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -10, 1)                        
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Kitty_SexSprite"):
                                call Kitty_Sex_Reset 
                            $ K_RecentActions.append("angry")
                            $ K_DailyActions.append("angry")                         
                        else:
                            call KittyFace("sad")
                            "Kitty doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump KDA_Prep
            return             
    #end auto
   
    if not K_DildoA:                                                               
            #first time    
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            ch_k "You want to try and fit that. . .?"    
            if K_Forced:
                call KittyFace("sad")
                ch_k "Always about the but, huh?"
    
    if not K_Loose and ("dildo anal" in K_RecentActions or "anal" in K_RecentActions or "dildo anal" in K_DailyActions or "anal" in K_DailyActions):
            call KittyFace("bemused", 1)
            ch_k "I'm still[K_like]sore from earlier. . ."
            
    if not K_DildoA and Approval:                                                 
            #First time dialog        
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            elif K_Love >= (K_Obed + K_Inbt):
                call KittyFace("sexy")
                $ K_Brows = "sad"
                $ K_Mouth = "smile" 
                ch_k "I[K_like]haven't actually used one of these, back there before. . ."            
            elif K_Obed >= K_Inbt:
                call KittyFace("normal")
                ch_k "If that's what you want, [K_Petname]. . ."            
            else: # Uninhibited 
                call KittyFace("sad")
                $ K_Mouth = "smile"             
                ch_k "I guess it could be fun two-player. . ."    
            
    elif Approval:                                                                       
            #Second time+ dialog
            if K_Forced: 
                call KittyFace("sad")
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                ch_k "The toys again?"  
            elif not Taboo and "tabno" in K_DailyActions:        
                ch_k "Well, at least you got us some privacy this time. . ."   
            elif "dildo anal" in K_DailyActions and not K_Loose:
                pass
            elif "dildo anal" in K_DailyActions:
                call KittyFace("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",       
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."]) 
                ch_k "[Line]"
            elif K_DildoA < 3:        
                call KittyFace("sexy", 1)
                $ K_Brows = "confused"
                $ K_Mouth = "kiss"
                ch_k "You want to stick it in my ass again?"       
            else:       
                call KittyFace("sexy", 1)
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
                call KittyFace("sad")
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                ch_k "Ok, fine."    
            else:
                call KittyFace("sexy", 1)
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
            call KittyFace("angry")
            if "no dildo" in K_RecentActions:  
                ch_k "What part of \"no,\" did you not get, [K_Petname]?"
            elif Taboo and "tabno" in K_DailyActions and "no dildo" in K_DailyActions:
                ch_k "Stop swinging that thing around in public!"  
            elif "no dildo" in K_DailyActions:       
                ch_k "I already told you \"no,\" [K_Petname]."
            elif Taboo and "tabno" in K_DailyActions:  
                ch_k "I already told you that I wouldn't do that out here!"  
            elif not K_DildoA:
                call KittyFace("bemused")
                ch_k "I'm just not into toys, [K_Petname]. . ."
            elif not K_Loose and "dildo anal" not in K_DailyActions:
                call KittyFace("perplexed")
                ch_k "You could have been a bit more gentle last time, [K_Petname]. . ."
            else:
                call KittyFace("bemused")
                ch_k "I don't think we need any toys, [K_Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in K_DailyActions:
                    call KittyFace("bemused")
                    ch_k "Yeah, ok, [K_Petname]."              
                    return
                "Maybe later?" if "no dildo" not in K_DailyActions:
                    call KittyFace("sexy")  
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
                        call KittyFace("sexy")     
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
                        call KittyFace("sad")
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
            call KittyFace("angry", 1)
            ch_k "I'm not going to let you use that on me."
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
            $ K_RecentActions.append("angry")
            $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
            call KittyFace("angry", 1)          
            $ K_RecentActions.append("tabno")                       
            $ K_DailyActions.append("tabno") 
            ch_k "Not here!"     
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)  
    elif not K_Loose and "dildo anal" in K_DailyActions:
            call KittyFace("bemused")
            ch_k "Sorry, I just need a little break back there, [K_Petname]."    
    elif K_DildoA:
            call KittyFace("sad") 
            ch_k "Sorry, you can keep your toys out of there."     
    else:
            call KittyFace("normal", 1)
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
        call Kitty_Bottoms_Off
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("dildo anal")
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
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no dildo")
    $ K_RecentActions.append("dildo anal")                      
    $ K_DailyActions.append("dildo anal") 
    
label KDA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Kitty") 
        call K_Pussy_Launch("dildo anal")
        call KittyLust   
        
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
                                    call KittyFace("angry", 1)   
                                    call K_Pos_Reset
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
                                call K_Slap_Ass
                                jump KDA_Cycle  
                                
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
                                            "I want to stick a finger in her pussy.":
                                                    $ Situation = "shift"
                                                    call KDA_After
                                                    call K_Fondle_Pussy    
                                            "Just stick a finger in her pussy without asking.":
                                                    $ Situation = "auto"
                                                    call KDA_After
                                                    call K_Fondle_Pussy                                           
                                            "I want to shift the dilso to her pussy.":
                                                    $ Situation = "shift"
                                                    call KDA_After
                                                    call K_Dildo_Pussy   
                                            "Never Mind":
                                                        pass                  
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KDA_After
                                    call Kitty_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KDA_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset
                                    $ Line = 0
                                    jump KDA_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto")
            
        call Sex_Dialog("Kitty",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset
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
                        call K_Cumming
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
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, [K_Petname], that's enough of that for now."
    
    
label KDA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset
        
    call KittyFace("sexy") 
    
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
                    call KittyFace("perplexed", 1)
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Mmm, so what else did you have in mind?"
    call Checkout
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
    call Shift_Focus("Kitty")
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
                    call KittyFace("sexy, 1")                    
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    ch_p "Oooh, that's good, [K_Pet]."
                    call Kitty_Namecheck
                    "Kitty continues her actions."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                "Ask her to stop.":
                    call KittyFace("surprised")       
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    ch_p "Let's not do that for now, [K_Pet]."
                    call Kitty_Namecheck
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
        call KittyFace("confused", 2)
        ch_k "Huh, so you'd like me to touch your cock with my feet?"
        $ K_Blush = 1
            
    if not K_Foot and Approval:                                                 #First time dialog        
        if K_Forced: 
            call KittyFace("sad",1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
        elif K_Love >= (K_Obed + K_Inbt):
            call KittyFace("sexy",1)
            $ K_Brows = "sad"
            $ K_Mouth = "smile" 
            ch_k "I guess it couldn't hurt. . ."            
        elif K_Obed >= K_Inbt:
            call KittyFace("normal",1)
            ch_k "If you want, [K_Petname]. . ."            
        elif K_Addict >= 50:
            call KittyFace("manic", 1)
            ch_k "Okay. . ."  
        else: # Uninhibited 
            call KittyFace("lipbite",1)    
            ch_k "Sure. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if K_Forced: 
            call KittyFace("sad")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            ch_k "That's all?" 
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "Um, I guess this is secluded enough. . ."    
        elif "foot" in K_RecentActions:
            call KittyFace("sexy", 1)
            ch_k "I'm getting foot cramps. . ."
            jump KFJ_Prep
        elif "foot" in K_DailyActions:
            call KittyFace("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",   
                "You're going to give me calluses.", 
                "Didn't get enough earlier?",
                "My feet are kinda sore from earlier.",
                "My feet are kinda sore from earlier."]) 
            ch_k "[Line]"
        elif K_Foot < 3:        
            call KittyFace("sexy", 1)
            $ K_Brows = "confused"
            $ K_Mouth = "kiss"
            ch_k "Hmm, magic toes. . ."        
        else:       
            call KittyFace("sexy", 1)
            $ Kitty_Arms = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",                 
                "So you'd like another foot sesh?",                 
                "A little. . . [she rubs her foot along your leg]?", 
                "A little TLC?"]) 
            ch_k "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad")
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, fine." 
        elif "no foot" in K_DailyActions:               
            ch_k "OK, geeze!"   
        else:
            call KittyFace("sexy", 1)
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
        call KittyFace("angry")
        if "no foot" in K_RecentActions:  
            ch_k "You don't[K_like]listen do you, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no foot" in K_DailyActions: 
            ch_k "I said not in public!"  
        elif "no foot" in K_DailyActions:       
            ch_k "I told you \"no,\" [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "I said not in public!"     
        elif not K_Foot:
            call KittyFace("bemused")
            ch_k "I don't know, [K_Petname]. . ."
        else:
            call KittyFace("bemused")
            ch_k "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in K_DailyActions:
                call KittyFace("bemused")
                ch_k "Yeah."              
                return
            "Maybe later?" if "no foot" not in K_DailyActions:
                call KittyFace("sexy")  
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
                    call KittyFace("sexy")     
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
                    call KittyFace("sad")
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
        call KittyFace("angry", 1)
        ch_k "I'm not telling you again."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1)
        ch_k "I don't even want to step on it."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)    
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2) if K_Love > 300 else K_Love
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call KittyFace("angry", 1)          
        $ K_DailyActions.append("tabno") 
        ch_k "Not here, not anywhere near here."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5)  
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)   
    elif K_Foot:
        call KittyFace("sad") 
        ch_k "I'm not feeling it today. . ."       
    else:
        call KittyFace("normal", 1)
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
                
    call KittyFace("sexy")
    if K_Forced:
        call KittyFace("sad")
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
    
    call Seen_First_Peen(1)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno")
    call DrainWord("Kitty","no foot")
    $ K_RecentActions.append("foot")                      
    $ K_DailyActions.append("foot") 
  
label KFJ_Cycle:    
    while Round >=0:
        call Shift_Focus("Kitty")
        call Kitty_Sex_Launch("foot")
#        call Kitty_FJ_Launch    #fix, change to sex launch with foot
        call KittyLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == 20:
                    $ K_Brows = "angry"        
                    menu:
                        ch_k "Ouch, foot cramp, can we[K_like]take a break?"
                        "How about a BJ?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_FJAfter
                                call K_Blowjob   
                        "How about a Handy?" if K_Action and MultiAction:
                                $ Situation = "shift"
                                call K_FJAfter
                                call K_Handjob  
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump KFJ_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Kitty_Sex_Reset
                                $ Situation = "shift"
                                jump K_FJAfter
                        "No, get back down there.":
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    call KittyFace("angry", 1)   
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
                   
                        "Maybe lose some clothes. . .":
                                    call K_Undress  
                                    
                        "Shift actions":
                            menu:
                                "How about a blowjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_FJAfter                
                                                call K_Blowjob
                                            else:
                                                ch_k "Actually I'm getting a bit worn out, let's finish up here. . ."
                                "How about a handjob?":
                                            if K_Action and MultiAction:
                                                $ Situation = "shift"
                                                call K_FJAfter                
                                                call K_Handjob
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
                                    call Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                                    
                        "Let's try something else." if MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump K_FJAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Kitty_Sex_Reset
                                    $ Line = 0
                                    jump K_FJAfter
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
                                jump K_FJAfter 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                                                
                            call K_Cumming
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
    call KittyFace("bemused", 0)
    $ Line = 0
    ch_k "Ok, we need to take a break."
    
label K_FJAfter:
    call KittyFace("sexy") 
    
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
            call KittyFace("smile", 1)
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
        call Kitty_Sex_Reset    
    call Checkout
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
                call KittyFace("sexy", 1)
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
                call KittyFace("smile", 1)
                ch_k "Sure, sounds fun!"
                $ Result = 1
            elif Approval:
                call KittyFace("sly", 2)
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
                                call KittyFace("smile")
                                ch_k "Thanks, that's[K_like]really cool of you."
                    "Come on, you might enjoy it. . .":
                            if B >= 50:
                                ch_k "Well, I guess I might." 
                                $ Result = 1
                            else:
                                call KittyFace("sad", 2)
                                ch_k "I don't think so." 
                    "Get in there, now.":
                            if ApprovalCheck("Kitty", 550, "OI", TabM = 2):
                                call KittyFace("sadside", 1)
                                ch_k "Ok, FINE."
                                $ Result = 1
                            else:
                                call KittyFace("angry")
                                ch_k "Like hell I will."  
                                $ K_RecentActions.append("angry")
                                $ K_DailyActions.append("angry")
                    "[Girl], what do you think?":
                            if Girl == "Rogue":
                                call RogueFace("sexy", 1)
                                if R_Les and K_Les:
                                        ch_r "Come on Kitty, don't we have fun?"
                                else:
                                        ch_r "Come on Kitty, couldn't it be fun?"
                                $ K_LikeRogue += (int(B/10))
                                if B >= 50:
                                        $ R_LikeKitty += 5
                            if B >= 50:
                                call KittyFace("smile", 1)
                                ch_k "Heh, I guess you're right, [Girl]."
                                $ Result = 1
                            else:
                                call KittyFace("angry", 1, Eyes="side")
                                ch_k "Yeah, no, I really don't think so."
            if Step == 3:
                    #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                    if Approval:
                            call KittyFace("smile", 1)
                            ch_k "Yeah, I mean I guess we could. . ."
                            $ Result = 1
                    else:
                            call KittyFace("sadside", 1)
                            ch_k "I don't think I could manage that. . ."
            
            if not Result:      
                #no approval
                $ K_RecentActions.append("no lesbian")                      
                $ K_DailyActions.append("no lesbian") 
                call KittyFace("sadside", 1)
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