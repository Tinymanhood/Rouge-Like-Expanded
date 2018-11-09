# E_Massage /////////////////////////////////////////////////////////////////////////////
label E_Massage:
    call Shift_Focus("Emma")
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Emma", 500, TabM = 2) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call EmmaFace("bemused", 1)
        if E_Forced:
                call EmmaFace("sad")
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "I could use it, [E_Petname]."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_Massage_Prep
        
    else:
        call EmmaFace("angry", 1)
        if "no massage" in E_RecentActions:  
            ch_e "I only {i}just{/i} refused you, [E_Petname]."
        elif "no massage" in E_DailyActions:       
            ch_e "I told you \"no\" earlier, [E_Petname]."
        else:
            call EmmaFace("bemused")
            ch_e "I'm not interested at the moment, [E_Petname]."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Don't concern yourself, [E_Petname]."              
                return
            "Maybe later?" if "no massage" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Perhaps."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)  
                $ E_RecentActions.append("no massage")                      
                $ E_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "I do have some tension built up. . ."                
                    jump E_Massage_Prep
                else:   
                    call EmmaFace("sly", Brows="confused") 
                    ch_e "No." 
    
    if "no massage" in E_DailyActions:
        ch_e "I've made myself clear on this, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "You'll have to keep your hands limber for yourself."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        ch_e "I can't been seen doing that with you."                  
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "I really can't."    
    $ E_RecentActions.append("no massage")                      
    $ E_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label E_Massage_Prep:
    call Emma_Top_Off("massage")
    if "angry" in E_RecentActions:
        return    
    
label E_Massage_Cycle: 
    $ E_RecentActions.append("massage")                      
    $ E_DailyActions.append("massage") 
        
    "You massage her back and shoulders."
    if not E_Over:
        $ D20 = renpy.random.randint(10, 20)
        $ Round -= D20 if Round > D20 else (Round-1)
        $ E_Addict -= D20 if E_Addict > D20 else E_Addict
            
    ch_e "That was very. . . pleasant, [E_Petname]"
    if "massage" not in E_RecentActions:        
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
    return

# end E_Massage /////////////////////////////////////////////////////////////////////////////

# E_Fondle /////////////////////////////////////////////////////////////////////////////
label E_Fondle:
    
    $ E_Mouth = "smile"
    if not E_Action:
        ch_e "I'm rather tired right now, [E_Petname], raincheck?"
        return
    menu:
        ch_e "Well? Where did you want to touch, [E_Petname]?"
        "Your breasts?" if E_Action:
                jump E_Fondle_Breasts
        "Your thighs?" if E_Action:
                jump E_Fondle_Thighs
        "Your pussy?" if E_Action:
                jump E_Fondle_Pussy
        "Your Ass?" if E_Action:
                jump E_Fondle_Ass
        "Never mind.":
                return
    return


# E_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label E_Fondle_Breasts:
    call Shift_Focus("Emma")
    
    # Will she let you fondle? Modifiers
    if E_FondleB: #You've done it before
        $ Tempmod += 15
    if E_Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in E_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 20
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no fondle breasts" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in E_RecentActions else 0        
        
    $ Approval = ApprovalCheck("Emma", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call EmmaFace("sexy")       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you cup her breast, Emma gently nods."            
            jump E_FB_Prep        
        else:   
            call EmmaFace("surprised")
            $ E_Brows = "confused"
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call EmmaFace("sexy", 1)
        if E_Forced: 
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)           
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "This does seem less. . . exposed"   
            
    if "fondle breasts" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FB_Prep
    elif "fondle breasts" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
            
    if Approval >= 2:             
        call EmmaFace("bemused", 1)
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "That sounds lovely, ravish me."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FB_Prep
        
    else:
        call EmmaFace("angry", 1)
        if "no fondle breasts" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle breasts" in E_DailyActions:  
            ch_e "You've been warned." 
        elif "no fondle breasts" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleB:
            call EmmaFace("bemused")
            ch_e "I highly doubt you could handle them, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "You wish."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "Don't concern yourself, [E_Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in E_DailyActions:
                call EmmaFace("sexy")  
                "She re-adjusts her cleavage."
                ch_e "Well, I can't rule it out. . ."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)    
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no fondle breasts")                      
                $ E_DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Politeness can be rewarded. . ."                
                    jump E_FB_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "This wasn't a \"tone\" issue." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)                 
                    ch_e "That is not appropriate. . ."
                    ch_e "but neither is it entirely unwelcome. . ."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)   
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_FB_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)  
                    call EmmaFace("angry", 1)
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    if "no fondle breasts" in E_DailyActions:
        ch_e "You need to pay attention when I speak to you."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Don't push your luck."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I can't been seen doing that with you."                   
    elif E_FondleB:
        call EmmaFace("sad")
        ch_e "I'm afraid you haven't earned back my good graces."        
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "No."    
    $ E_RecentActions.append("no fondle breasts")                      
    $ E_DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label E_FB_Prep: #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Top_Off
        if "angry" in E_RecentActions:
            return
        
    $ Tempmod = 0  
    call E_Breasts_Launch("fondle breasts")
    if not E_FondleB:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 5)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
            
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0     
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no fondle breasts")
    $ E_RecentActions.append("fondle breasts")                      
    $ E_DailyActions.append("fondle breasts") 
    
label E_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma")
        call E_Breasts_Launch("fondle breasts")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_FondleB):
                    $ E_Brows = "confused"
                    ch_e "They really are magnificent, aren't they?" 
        elif E_Lust >= 85:
                    pass  
        elif Cnt == (15 + E_FondleB) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused" 
                    menu:
                        ch_e "Perhaps we could try something else, [E_Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump E_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_FB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                     
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_FB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                                    
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                            if E_Action and MultiAction:                        
                                                $ Situation = "shift"
                                                call E_FB_After
                                                call E_Suck_Breasts
                                            else:
                                                ch_e "I could use a break, are you about finished here?"
                                    "Just suck on them without asking.":
                                            if E_Action and MultiAction:                            
                                                $ Situation = "auto"
                                                call E_FB_After
                                                call E_Suck_Breasts
                                            else:
                                                "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                ch_e "I could use a break, are you about finished here?"
                                            
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I could use a break, are you about finished here?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FB_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FB_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_FB_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FB_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_FB_After
                       
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
                                    jump E_FB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_FondleB += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_FondleB == 1:            
            $ E_SEXP += 4         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I'm sure it exceeded your expectations. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Well you certainly hit the jackpot."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label E_Suck_Breasts:
    call Shift_Focus("Emma")
                                                                                        # Will she let you suck? Modifiers
    if E_SuckB: #You've done it before
        $ Tempmod += 15
    if not E_Chest and not E_Over:
        $ Tempmod += 15
    if E_Lust > 75: #She's really horny
        $ Tempmod += 20
    if E_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount     
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no suck breasts" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in E_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Emma", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call EmmaFace("sexy")       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you dive in, Emma seems a bit surprised, but just makes a little \"coo.\""              
            jump E_SB_Prep      
        else:               
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_SB_Prep
    elif "suck breasts" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1)
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Oh very well. . ."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no suck breasts" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no suck breasts" in E_DailyActions:  
            ch_e "I told you I couldn't be seen like that." 
        elif "no suck breasts" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_SuckB:
            call EmmaFace("bemused")
            ch_e "Let's work up to that, perhaps. . ."
        else:
            call EmmaFace("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "No offense taken. I get it."              
                return
            "Maybe later?" if "no suck breasts" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I'll give it some thought, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)    
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no suck breasts")                      
                $ E_DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Oh, if you insist. . ."                
                    jump E_SB_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Emma", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)                 
                    ch_e "You'd better shower them with praise. . ."                         
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_SB_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)  
                    call EmmaFace("angry", 1)
                    "She shoves your head back out."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no suck breasts" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Not worth it."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:   
        call EmmaFace("angry", 1)      
        $ E_RecentActions.append("tabno")    
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_SuckB:
        call EmmaFace("sad")
        ch_e "I am sorry about that, but perhaps later?"            
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "No."
    $ E_RecentActions.append("no suck breasts")                      
    $ E_DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label E_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0   
        call Emma_Top_Off
        if "angry" in E_RecentActions:
            return
    
    $ Tempmod = 0      
    call E_Breasts_Launch("suck breasts")
    if not E_SuckB:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -25)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 17) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
    
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0      
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no suck breasts")
    $ E_RecentActions.append("suck breasts")                      
    $ E_DailyActions.append("suck breasts") 
    
label E_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kissing":
            $ Trigger2 = 0 
    while Round >=0:  
        call Shift_Focus("Emma")
        call E_Breasts_Launch("suck breasts")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_SuckB):
                    $ E_Brows = "sly"
                    ch_e "Lovely, aren't they?"   
        elif E_Lust >= 85:
                    pass
        elif Cnt == (15 + E_SuckB) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_SB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_SB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                   
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_SB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                                    
                        "Pull back to fondling.":  
                            if E_Action and MultiAction:
                                $ Situation = "pullback"
                                call E_SB_After
                                call E_Fondle_Breasts
                            else:
                                "As you pull back, Emma pushes you back in close."
                                ch_e "I could use a break, are you about finished here?"
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_SB_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_SB_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_SB_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_SB_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_SB_After
                       
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
                                    jump E_SB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_SuckB += 1  
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_SuckB == 1:            
            $ E_SEXP += 4         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "Delectable , weren't they."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Did you get enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label E_Fondle_Thighs:
    call Shift_Focus("Emma")
                                                                                        # Will she let you fondle her thighs? Modifiers
    if E_FondleT: #You've done it before
        $ Tempmod += 10
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if E_Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in E_Traits:
        $ Tempmod += Taboo   
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount      
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no fondle thighs" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in E_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Emma", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call EmmaFace("sexy")       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you caress her thigh, Emma glances at you, and smiles."             
            jump E_FT_Prep      
        else:               
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Perhaps we keep it above the waist, [E_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised")    
        $ E_Brows = "sad"
        if E_Lust > 60:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As you pull back, Emma looks a little sad."              
        jump E_FT_Prep  
    elif "fondle thighs" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FT_Prep
    elif "fondle thighs" in E_DailyActions:
        call EmmaFace("sexy", 1)       
        ch_e "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1)
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Ok [E_Petname], go ahead."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no fondle thighs" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle thighs" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleT:
            call EmmaFace("bemused")
            ch_e "Seems a bit forward, [E_Petname]."
        else:
            call EmmaFace("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint."             
                return
            "Maybe later?" if "no fondle thighs" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Perhaps."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)    
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no fondle thighs")                      
                $ E_DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Politeness can be rewarded. . ."             
                    jump E_FT_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)                 
                    ch_e "Hmmph."                         
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_FT_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -8)  
                    call EmmaFace("angry", 1)
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no fondle thighs" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Don't push your luck."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 2)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")          
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_FondleT:
        call EmmaFace("sad")
        ch_e "Hands."            
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "No."
    $ E_RecentActions.append("no fondle thighs")                      
    $ E_DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label E_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Bottoms_Off 
        if "angry" in E_RecentActions:
            return 
            
    $ Tempmod = 0    
    call E_Pussy_Launch("fondle thighs")
    if not E_FondleT:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 15)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
            
    if Taboo:               
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, (int(Taboo/5)))                               
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no fondle thighs")
    $ E_RecentActions.append("fondle thighs")                      
    $ E_DailyActions.append("fondle thighs")  
    
label E_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("fondle thighs")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_FondleT):
                    $ E_Brows = "confused"
                    ch_e "Luxurious, yes?"   
        elif Cnt == (15 + E_FondleT) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_FT_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FT_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                       
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_FT_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                                    
                        "Can I do a little deeper?":
                                if E_Action and MultiAction:
                                    $ Situation = "shift"
                                    call E_FT_After
                                    call E_Fondle_Pussy                
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        "Shift your hands a bit higher without asking":
                                if E_Action and MultiAction:
                                    $ Situation = "auto"
                                    call E_FT_After
                                    call E_Fondle_Pussy    
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_e "I could use a break, are you about finished here?" 
                
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FT_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                                    
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FT_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_FT_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FT_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_FT_After
                       
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
                                    jump E_FT_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_FondleT += 1  
    $ E_Action -=1
    if E_Legs != "pants" or E_Upskirt:        
        $ E_Addictionrate += 1
        if "addictive" in P_Traits:
            $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_FondleT == 1:            
            $ E_SEXP += 3         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was. . . pleasant."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Was that enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label E_Fondle_Pussy:
    call Shift_Focus("Emma")
                                                                                        # Will she let you fondle? Modifiers
    if E_FondleP: #You've done it before
        $ Tempmod += 20
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if E_Lust > 75: #She's really horny
        $ Tempmod += 15
    if E_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount     
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no fondle pussy" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in E_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Emma", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call EmmaFace("sexy")       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
            "As your hand creeps up her thigh, Emma seems a bit surprised, but then nods."            
            jump E_FP_Prep      
        else:               
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised")   
        $ E_Brows = "sad"        
        if E_Lust > 80:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As your hand pulls out, Emma gasps and looks upset."              
        jump E_FP_Prep     
    elif "fondle pussy" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FP_Prep
    elif "fondle pussy" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1)
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Mmmm, I couldn't refuse. . ."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no fondle pussy" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle pussy" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleP:
            call EmmaFace("bemused")
            ch_e "I don't think we're there yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I'll give it some thought, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no fondle pussy")                      
                $ E_DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    ch_e "I do enjoy hearing you beg. . ."                    
                    jump E_FP_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Oh, if you insist. . ."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_FP_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)  
                    call EmmaFace("angry", 1)
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no fondle pussy" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I don't think so, [E_Petname]."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno")
        ch_e "I have a reputation to maintain."                   
    elif E_FondleP:
        call EmmaFace("sad")
        ch_e "Sorry, keep your hands out of there."           
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "No thank you, [E_Petname]."
    $ E_RecentActions.append("no fondle pussy")                      
    $ E_DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label E_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Bottoms_Off   
        if "angry" in E_RecentActions:
            return 
    $ Tempmod = 0
    
    call E_Pussy_Launch("fondle pussy")
    if not E_FondleP:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -50)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 35)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 25) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no fondle pussy")
    $ E_RecentActions.append("fondle pussy")                      
    $ E_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label E_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("fondle pussy")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_FondleP):
                    $ E_Brows = "confused"
                    ch_e "You like how that feels, huh?"  
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_FondleP) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_FP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                        
                        "I want to stick a finger in. . ." if Speed != 2:
                            if E_InsertP: 
                                $ Speed = 2
                            else:
                                menu:                                
                                    "Ask her first":
                                        $ Situation = "shift"
                                    "Don't ask first [[just stick it in]":                                    
                                        $ Situation = "auto"
                                call E_Insert_Pussy  
                       
                        "Pull back to fondling" if Speed == 2:
                                $ Speed = 1   
                                      
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_FP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:                                                                                         
                                            "I want to lick your pussy.":
                                                    $ Situation = "shift"
                                                    call E_FP_After
                                                    call E_Lick_Pussy                 
                                            "Just start licking":
                                                    $ Situation = "auto"
                                                    call E_FP_After
                                                    call E_Lick_Pussy         
                                            "Pull back to the thighs":
                                                    $ Situation = "pullback"
                                                    call E_FP_After
                                                    call E_Fondle_Thighs
#                                            "I want to stick a dildo in.":
#                                                    call E_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call E_FP_After
#                                                        call E_Dildo_Pussy  
#                                                    else:
#                                                        jump E_FP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_e "I could use a break, are you about finished here?"           
                                        
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FP_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FP_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_FP_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FP_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_FP_After
                       
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
                                    jump E_FP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_FondleP += 1  
    $ E_Action -=1
    if E_Legs != "pants" or E_Upskirt:        
        $ E_Addictionrate += 1
        if "addictive" in P_Traits:
            $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_FondleP == 1:            
            $ E_SEXP += 7         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I do appreciate some rather. . . aggressive attention down there."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Did you find what you were looking for?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# end E_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label E_Insert_Pussy:
    call Shift_Focus("Emma")
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Emma", 1100, TabM = 2):
            call EmmaFace("surprised")       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you slide a finger in, Emma seems a bit surprised, but seems into it."              
            jump E_IP_Prep
        else:   
            call EmmaFace("surprised",2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Oooh!"
            "She slaps your hand back."
            call EmmaFace("perplexed",1)
            ch_e "Careful what you put in there, you may not get it back."
            return            
    
    if ApprovalCheck("Emma", 1100, TabM = 2):                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            ch_e "Mmmmmm. . ."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call EmmaFace("bemused", 2)
        ch_e "No. Thank you."
        $ E_Blush = 1
    return
    
                
label E_IP_Prep: #Animation set-up     
    if not E_InsertP:
        $ E_InsertP = 1
        $ E_SEXP += 10          
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -60)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 55)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 25)
                
    if not E_Forced and Situation != "auto":        
        call E_Undress("bottom")
        if "angry" in E_RecentActions:
            return    
            
#    call E_Pussy_Launch("insert pussy")
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
        
    $ Line = 0 
    $ Cnt = 0     
    $ Speed = 2
    return

# end E_Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label E_Lick_Pussy: 
    call Shift_Focus("Emma")
                                                                                  # Will she let you fondle? Modifiers     
    if E_LickP: #You've done it before
        $ Tempmod += 15
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if E_Lust > 95:
        $ Tempmod += 20  
    elif E_Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if E_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount     
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no lick pussy" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in E_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Emma", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Emma jumps, but then softens."  
            call EmmaFace("sexy")           
            jump E_LP_Prep
        else:   
            call EmmaFace("surprised")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "I like where your head is at, so to speak, but perhaps hold off on that." 
            call EmmaFace("perplexed",1)
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_LP_Prep
    elif "lick pussy" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1)
            $ E_Eyes = "closed"            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)            
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)
            ch_e "Mmmmmm. . ."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no lick pussy" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no lick pussy" in E_DailyActions:  
            ch_e "You already got your answer!" 
        elif "no lick pussy" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_LickP:
            call EmmaFace("bemused")
            ch_e "I'm not sure we're at that stage, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "I'm really not comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint, [E_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "I'll be thinking about it, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no lick pussy")                      
                $ E_DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call EmmaFace("sexy")           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "You present a compelling case. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_LP_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "I would, but still no, [E_Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Emma", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "If you insist. . ."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_LP_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)  
                    call EmmaFace("angry", 1)
                    "She shoves your head back."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no lick pussy" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I really can't, [E_Petname]."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_LickP:
        call EmmaFace("sad") 
        ch_e "Keep your head out of there."    
    else:
        call EmmaFace("surprised")
        ch_e "I know, I'm as disappointed as you are."
        call EmmaFace
    $ E_RecentActions.append("no lick pussy")                      
    $ E_DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label E_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        if E_Legs == "pants":
            $ Tempmod = 15
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return  
            
    $ Tempmod = 0      
    call E_Pussy_Launch("lick pussy")
    if not E_LickP:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -30)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 35)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 75) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 35)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 15)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if E_Legs == "skirt":
        $ E_Upskirt = 1  
        $ E_SeenPanties = 1
    if not E_Panties:
        call Emma_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no lick pussy")
    $ E_RecentActions.append("lick pussy")                      
    $ E_DailyActions.append("lick pussy") 
    
label E_LP_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("lick pussy")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_LickP):
                    $ E_Brows = "confused"
                    ch_e "Isn't it just delicious?"  
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_LickP) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_LP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_LP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                  
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_LP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    if E_Action and MultiAction:
                                                        $ Situation = "pullback"
                                                        call E_LP_After
                                                        call E_Fondle_Pussy
                                                    else:
                                                        ch_e "I could use a break, are you about finished here?"  
#                                            "I want to stick a dildo in.":
#                                                    call E_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call E_LP_After
#                                                        call E_Dildo_Pussy  
#                                                    else:
#                                                        jump E_LP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_e "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_LP_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_LP_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_LP_After
        #End menu (if Line)
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto")
        call Sex_Dialog("Emma",Partner)
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_LP_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_LP_After
                       
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
                                    jump E_LP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_LickP += 1  
    $ E_Action -=1     
    if E_Legs != "pants" or E_Upskirt:        
        $ E_Addictionrate += 1
        if "addictive" in P_Traits:
            $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 3 if R_LikeEmma >= 800 else 2
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_LickP == 1:            
            $ E_SEXP += 10         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I could really take advantage of your services more often. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "I suppose that worked out for both of us. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end E_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label E_Fondle_Ass: 
    call Shift_Focus("Emma")
                                                                                     # Will she let you fondle? Modifiers
    if E_FondleA: #You've done it before
        $ Tempmod += 10
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if E_Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in E_Traits:
        $ Tempmod += Taboo  
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount      
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no fondle ass" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in E_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Emma", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call EmmaFace("surprised", 1)  
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
            "As your hand creeps down her backside, Emma jumps a bit, and then relaxes."              
            call EmmaFace("sexy")  
            jump E_FA_Prep  
        else:          
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Hands off, [E_Petname]."   
            call EmmaFace("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised")   
        $ E_Brows = "sad"        
        if E_Lust > 80:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As your finger slides out, Emma gasps and looks upset."              
        jump E_FA_Prep     
    elif "fondle ass" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FA_Prep
    elif "fondle ass" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
            ch_e "If you insist. . ."   
        else:
            call EmmaFace("bemused, 1") 
            ch_e "I can't exactly refuse. . ."   
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
        jump E_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no fondle ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle ass" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleA:
            call EmmaFace("bemused")
            ch_e "Not yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused")
            ch_e "Let's not, ok [E_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Perhaps."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)  
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no fondle ass")                      
                $ E_DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call EmmaFace("sexy")     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "I do enjoy hearing you beg. . ."                           
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    jump E_FA_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -1) 
                    ch_e "Fine, I suppose."                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_FA_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -10)  
                    call EmmaFace("angry", 1)
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                        
    if "no fondle ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Do you want to keep those fingers?"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_FondleA:
        call EmmaFace("sad")
        ch_e "I'm sorry, keep your hands to yourself."        
    else:
        call EmmaFace("sexy") 
        $ E_Mouth = "sad"
        ch_e "No."
    $ E_RecentActions.append("no fondle ass")                      
    $ E_DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_e "Sorry, I don't even know how I got here. . ."
return

label E_FA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
    $ Tempmod = 0      
    call E_Pussy_Launch("fondle ass")
    if not E_FondleA:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -20)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 15) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 12)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 20)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no fondle ass")
    $ E_RecentActions.append("fondle ass")                      
    $ E_DailyActions.append("fondle ass") 
    
label E_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("fondle ass")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_FondleA):
                    $ E_Brows = "confused"
                    ch_e "Mmmm I do enjoy that. . ."  
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_FondleA) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_FA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_FA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_FA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call E_FA_After
                                                    call E_Insert_Ass                 
                                            "Just stick a finger in without asking.":
                                                    $ Situation = "auto"
                                                    call E_FA_After
                                                    call E_Insert_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call E_FA_After
                                                    call E_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call E_FA_After
                                                    call E_Lick_Ass    
#                                            "I want to stick a dildo in.":
#                                                    call E_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call E_FA_After
#                                                        call E_Dildo_Ass  
#                                                    else:
#                                                        jump E_FA_Cycle   
                                            "Never Mind":
                                                        pass              
                                else:
                                    ch_e "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FA_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_FA_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_FA_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_FA_After
                       
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
                                    jump E_FA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_FondleA += 1  
    $ E_Action -=1            
    if E_Legs != "pants" or E_Upskirt:        
        $ E_Addictionrate += 1
        if "addictive" in P_Traits:
            $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_FondleA == 1:            
            $ E_SEXP += 4         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was. . . nice. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Did you enjoy that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end E_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label E_Insert_Ass:
    call Shift_Focus("Emma")
    
    if E_InsertA: #You've done it before
        $ Tempmod += 25
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if E_Lust > 85: #She's really horny
        $ Tempmod += 15
    if E_Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if E_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25 
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no insert ass" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in E_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Emma", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call EmmaFace("surprised")
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you slide a finger in, Emma tightens around it in surprise, but seems into it."  
            call EmmaFace("sexy")           
            jump E_IA_Prep
        else:   
            call EmmaFace("surprised")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Whoa, back off, [E_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in E_DailyActions:
        call EmmaFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1)
            $ E_Eyes = "closed"            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)            
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)
            ch_e "Mmmmm. . ."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1)
        if "no insert ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no insert ass" in E_DailyActions:  
            ch_e "I told you that wasn't appropriate!" 
        elif "no insert ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_InsertA:
            call EmmaFace("perplexed", 1)
            ch_e "That's really not my usual style. . ."
        else:
            call EmmaFace("bemused")
            ch_e "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "It's. . . possible, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no insert ass")                      
                $ E_DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call EmmaFace("sexy")           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "You're probably right. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_IA_Prep
                else:   
                    call EmmaFace("bemused") 
                    ch_e "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Emma", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and E_Forced):                    
                    call EmmaFace("surprised", 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Well hello there. . ."                     
                    call EmmaFace("sad")
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_IA_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)  
                    call EmmaFace("angry", 1)
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no insert ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I'm not going that far today."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10) if E_Inbt > 50 else Statupdate("Emma", "Lust", E_Lust, 50, 3) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_InsertA:
        call EmmaFace("sad") 
        ch_e "I don't feel like it."    
    else:
        call EmmaFace("surprised")
        ch_e "Not today, [E_Petname]."
        call EmmaFace
    $ E_RecentActions.append("no insert ass")                      
    $ E_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label E_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("insert ass")
    if not E_InsertA:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -50)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 60)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 35) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 25)
            
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no insert ass")
    $ E_RecentActions.append("insert ass")                      
    $ E_DailyActions.append("insert ass") 
    
label E_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("insert ass")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_InsertA):
                    $ E_Brows = "confused"
                    ch_e "Ungh, You're getting going there. . ."  
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_InsertA) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting kind sore, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_IA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_IA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_IA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    $ Situation = "pullback"
                                                    call E_IA_After
                                                    call E_Fondle_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call E_IA_After
                                                    call E_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call E_IA_After
                                                    call E_Lick_Ass    
#                                            "I want to stick a dildo in.":
#                                                    call E_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call E_IA_After
#                                                        call E_Dildo_Ass  
#                                                    else:
#                                                        jump E_IA_Cycle  
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_e "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_IA_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_IA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_IA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto")
            
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_IA_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_IA_After
                       
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
                                    jump E_IA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_InsertA += 1  
    $ E_Action -=1            
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_InsertA == 1:            
            $ E_SEXP += 12         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "You certainly surprise me. . ."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Was it everything you dreamed?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   


# end E_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label E_Lick_Ass: 
    call Shift_Focus("Emma")
                                                                             # Will she let you lick? Modifiers         
    if E_LickA: #You've done it before
        $ Tempmod += 20
    if E_Legs == "pants" or HoseNum("Emma") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if E_Lust > 95:
        $ Tempmod += 20  
    elif E_Lust > 85: #She's really horny
        $ Tempmod += 15    
    if E_Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 25  
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount 
    
    if Taboo and "tabno" in E_DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in E_History:                   
        $ Tempmod -= 20 
        
    if "no lick ass" in E_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in E_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Emma", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call EmmaFace("surprised")   
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Emma startles briefly, but then begins to melt."  
            call EmmaFace("sexy")  
            jump E_LA_Prep
        else:   
            call EmmaFace("surprised")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "[E_Petname]! Not now. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in E_RecentActions:
        call EmmaFace("sexy", 1)
        ch_e "Mmmm, again? I suppose. . ."
        jump E_LA_Prep
    elif "lick ass" in E_DailyActions:
        call EmmaFace("sexy", 1)
        ch_e "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad")
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1)
            $ E_Eyes = "closed"            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)            
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)
            ch_e "I'd rather you didn't."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
        jump E_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call EmmaFace("angry", 1)
        if "no lick ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no lick ass" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no lick ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_LickA:                    #First time dialog
            call EmmaFace("bemused", 1)
            if E_Love >= E_Obed and E_Love >= E_Inbt:            
                ch_e "Oh, are we there now?"
            elif E_Obed >= E_Inbt:            
                ch_e "Is that what gets you off?"
            else:
                $ E_Eyes = "sexy"
                ch_e "Hm, I didn't know that's what you were into."
        else:
            call EmmaFace("bemused")
            ch_e "Not now, [E_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in E_DailyActions:
                call EmmaFace("bemused")
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in E_DailyActions:
                call EmmaFace("sexy")  
                ch_e "Anything's possible, [E_Petname]."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)   
                if Taboo:                    
                    $ E_RecentActions.append("tabno")                      
                    $ E_DailyActions.append("tabno") 
                $ E_RecentActions.append("no lick ass")                      
                $ E_DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call EmmaFace("sexy")           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "Ok, you're probably right. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_LA_Prep
                else:   
                    call EmmaFace("sexy") 
                    ch_e "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Emma", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Suit yourself."  
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_LA_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)  
                    call EmmaFace("angry", 1)
                    "She shoves your head back."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no lick ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "I don't think so."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10) if E_Inbt > 50 else Statupdate("Emma", "Lust", E_Lust, 50, 3) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1)    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_LickA:
        call EmmaFace("sad") 
        ch_e "Sorry, no more of that."    
    else:
        call EmmaFace("surprised")
        ch_e "I'm sorry, not now."
        call EmmaFace
    $ E_RecentActions.append("no lick ass")                      
    $ E_DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label E_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        if E_Legs == "pants":
            $ Tempmod = 15
        call Emma_Bottoms_Off
        if "angry" in E_RecentActions:
            return    
    $ Tempmod = 0  
    call E_Pussy_Launch("lick ass")
    if not E_LickA:        
        if E_Forced:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -30)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 40)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 80) 
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 35)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 25)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 55)
    if Taboo:
        $ E_Inbt += int(Taboo/10)  
        $ E_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ E_Upskirt = 1
    if E_Legs == "skirt":
        $ E_SeenPanties = 1
    if not E_Panties:
        call Emma_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no lick ass")
    
    $ E_RecentActions.append("lick") if "lick" not in E_RecentActions else E_RecentActions
    $ E_RecentActions.append("ass") if "ass" not in E_RecentActions else E_RecentActions
    $ E_RecentActions.append("lick ass")  
    
    $ E_DailyActions.append("lick") if "lick" not in E_DailyActions else E_RecentActions
    $ E_DailyActions.append("ass") if "ass" not in E_DailyActions else E_RecentActions                    
    $ E_DailyActions.append("lick ass")  
label E_LA_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Emma") 
        call E_Pussy_Launch("lick ass")
        call EmmaLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_LickA):
                    $ E_Brows = "confused"
                    ch_e "You certainly are enthusiastic. . ."  
        elif E_Lust >= 80:
                    pass
        elif Cnt == (15 + E_LickA) and E_SEXP >= 15 and not ApprovalCheck("Emma", 1500):
                    $ E_Brows = "confused"        
                    menu:
                        ch_e "[E_Petname], this is getting weird, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump E_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump E_LA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):                        
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call EmmaFace("angry", 1)   
                                    call E_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_e "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -3, 1)
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -4, 1)
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, -1, 1)                    
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1, 1)  
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")   
                                    jump E_LA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                           
                        "Slap her ass":                     
                                call E_Slap_Ass
                                jump E_LA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call E_Undress  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:   
                                            "Switch to fondling.":
                                                    $ Situation = "pullback"
                                                    call E_LA_After
                                                    call E_Fondle_Ass
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call E_LA_After
                                                    call E_Insert_Ass                 
                                            "Just stick a finger in [[without asking].":
                                                    $ Situation = "auto"
                                                    call E_LA_After
                                                    call E_Insert_Ass                        
#                                            "I want to stick a dildo in.":
#                                                    call E_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call E_LA_After
#                                                        call E_Dildo_Ass  
#                                                    else:
#                                                        jump E_LA_Cycle   
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_e "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_LA_After
                                    call Emma_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_LA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset
                                    $ Line = 0
                                    jump E_LA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto")
            
        call Sex_Dialog("Emma",Partner)
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset
                                return    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5) 
                            if 100 > E_Lust >= 70 and E_OCount < 2:             
                                $ E_RecentActions.append("unsatisfied")                      
                                $ E_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump E_LA_After 
                            $ Line = "came"
     
                    #If Emma can cum
                    if E_Lust >= 100:                                               
                        call E_Cumming
                        if Situation == "shift" or "angry" in E_RecentActions:
                            jump E_LA_After
                       
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
                                    jump E_LA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_e "It's getting late. . ."  
        elif Round == 5:
            ch_e "We should take a break soon."       
    
    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset
        
    call EmmaFace("sexy") 
    
    $ E_LickA += 1  
    $ E_Action -=1      
    if E_Legs != "pants" or E_Upskirt:        
        $ E_Addictionrate += 1
        if "addictive" in P_Traits:
            $ E_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed emma" in R_RecentActions: #If Rogue was participating
        $ R_LikeEmma += 2 if R_LikeEmma >= 800 else 1
    if K_Loc == bg_current and "noticed emma" in K_RecentActions: #If Kitty was participating
        $ K_LikeEmma += 2 if K_LikeEmma >= 800 else 1
     
    if E_LickA == 1:            
            $ E_SEXP += 15         
            if not Situation: 
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "That was. . . invigorating."
                elif E_Obed <= 500 and P_Focus <= 20:
                    call EmmaFace("perplexed", 1)
                    ch_e "Was it all you dreamed of?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout
    return   

# end E_Lick Ass /////////////////////////////////////////////////////////////////////////////

