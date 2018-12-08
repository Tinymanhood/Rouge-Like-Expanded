# K_Massage /////////////////////////////////////////////////////////////////////////////
label K_Massage:
    call Shift_Focus("Kitty") from _call_Shift_Focus_84
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Kitty", 500, TabM = 1) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call KittyFace("bemused", 1) from _call_KittyFace_28
        if K_Forced:
                call KittyFace("sad") from _call_KittyFace_29
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
        ch_k "Sure, why not."   
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
        jump K_Massage_Prep
        
    else:
        call KittyFace("angry", 1) from _call_KittyFace_30
        if "no massage" in K_RecentActions:  
            ch_k "Come on, I {i}just{/i} told you \"no,\" [K_Petname]."
        elif "no massage" in K_DailyActions:       
            ch_k "I already told you \"no.\""
        else:
            call KittyFace("bemused") from _call_KittyFace_31
            ch_k "I don't know, not right now."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_32
                ch_k "It's cool, [K_Petname]."              
                return
            "Maybe later?" if "no massage" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_33  
                ch_k "Yeah, maybe."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 20, 1)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)  
                $ K_RecentActions.append("no massage")                      
                $ K_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_34     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
                    ch_k "I guess I could use some relaxation. . ."                
                    jump K_Massage_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_35 
                    ch_k "Heh, sorry, [K_Petname]." 
    
    if "no massage" in K_DailyActions:
        ch_k "Um, get a clue, [K_Petname]."   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_36
        ch_k "Even that's too much."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_37    
        ch_k "Not[K_like]in public."                   
    else:
        call KittyFace("sexy") from _call_KittyFace_38 
        $ K_Mouth = "sad"
        ch_k "Seriously, no thank you!"    
    $ K_RecentActions.append("no massage")                      
    $ K_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label K_Massage_Prep:
    call Kitty_Top_Off("massage") from _call_Kitty_Top_Off
    if "angry" in K_RecentActions:
        return    
    
label K_Massage_Cycle: 
    $ K_RecentActions.append("massage")                      
    $ K_DailyActions.append("massage") 
        
    "You massage her back and shoulders."
    if not K_Over:
        $ D20 = renpy.random.randint(10, 20)
        $ Round -= D20 if Round > D20 else (Round-1)
        $ K_Addict -= D20 if K_Addict > D20 else K_Addict
            
    ch_k "That was very relaxing, [K_Petname]"
    if "massage" not in K_RecentActions:        
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
    return

# end K_Massage /////////////////////////////////////////////////////////////////////////////

# K_Fondle /////////////////////////////////////////////////////////////////////////////
label K_Fondle:
    
    $ K_Mouth = "smile"
    if not K_Action:
        ch_k "I'm kinda tired right now, [K_Petname], later?"
        return
    menu:
        ch_k "Um, what did you want to touch, [K_Petname]?"
        "Your breasts?" if K_Action:
                jump K_Fondle_Breasts
        "Your thighs?" if K_Action:
                jump K_Fondle_Thighs
        "Your pussy?" if K_Action:
                jump K_Fondle_Pussy
        "Your Ass?" if K_Action:
                jump K_Fondle_Ass
        "Never mind.":
                return
    return


# K_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label K_Fondle_Breasts:
    call Shift_Focus("Kitty") from _call_Shift_Focus_85
    
    # Will she let you fondle? Modifiers
    if K_FondleB: #You've done it before
        $ Tempmod += 15
    if K_Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in K_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 20
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle breasts" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in K_RecentActions else 0        
        
    $ Approval = ApprovalCheck("Kitty", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call KittyFace("sexy") from _call_KittyFace_39       
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)            
            "As you cup her breast, Kitty gently nods."            
            jump KFB_Prep        
        else:   
            call KittyFace("surprised") from _call_KittyFace_40
            $ K_Brows = "confused"
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            ch_k "Nuh-uh, [K_Petname], get back to what you were doing."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call KittyFace("sexy", 1) from _call_KittyFace_41
        if K_Forced: 
            call KittyFace("sad") from _call_KittyFace_42
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)           
        elif not Taboo and "tabno" in K_DailyActions:        
            ch_k "I guess here is fine. . ."   
            
    if "fondle breasts" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_43
        ch_k "Mmm, again? Ok."
        jump KFB_Prep
    elif "fondle breasts" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_44
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."]) 
        ch_k "[Line]"
            
    if Approval >= 2:             
        call KittyFace("bemused", 1) from _call_KittyFace_45
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_46
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
        ch_k "Ok [K_Petname], come and get'em."   
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
        jump KFB_Prep
        
    else:
        call KittyFace("angry", 1) from _call_KittyFace_47
        if "no fondle breasts" in K_RecentActions:  
            ch_k "[K_Like]no way, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions and "no fondle breasts" in K_DailyActions:  
            ch_k "I told you not here!" 
        elif "no fondle breasts" in K_DailyActions:       
            ch_k "I[K_like]already told you \"no.\""
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_FondleB:
            call KittyFace("bemused") from _call_KittyFace_48
            ch_k "I'm[K_like]not ready for that, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_49
            ch_k "Um, no."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_50
                ch_k "It's cool, [K_Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_51  
                "She re-adjusts her cleavage."
                ch_k "Um, yeah, maybe later."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)    
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no fondle breasts")                      
                $ K_DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_52     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
                    ch_k "Well[K_like]if you ask nicely. . ."                
                    jump KFB_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_53 
                    ch_k "Um, still no." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_54
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)                 
                    ch_k "Rude! But. . . whatever."                         
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)   
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KFB_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)  
                    call KittyFace("angry", 1) from _call_KittyFace_55
                    "She slaps your hand away."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
    
    if "no fondle breasts" in K_DailyActions:
        ch_k "{i}Listen{/i}!"   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_56
        ch_k "Not even."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_57    
        $ K_RecentActions.append("tabno")                   
        $ K_DailyActions.append("tabno") 
        ch_k "I don't like being so. . . exposed."                   
    elif K_FondleB:
        call KittyFace("sad") from _call_KittyFace_58
        ch_k "You had your shot."        
    else:
        call KittyFace("sexy") from _call_KittyFace_59 
        $ K_Mouth = "sad"
        ch_k "No way."    
    $ K_RecentActions.append("no fondle breasts")                      
    $ K_DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label KFB_Prep: #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        call Kitty_Top_Off from _call_Kitty_Top_Off_1
        if "angry" in K_RecentActions:
            return
        
    $ Tempmod = 0  
    call K_Breasts_Launch("fondle breasts") from _call_K_Breasts_Launch
    if not K_FondleB:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
            
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0     
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_55
    call DrainWord("Kitty","no fondle breasts") from _call_DrainWord_56
    $ K_RecentActions.append("fondle breasts")                      
    $ K_DailyActions.append("fondle breasts") 
    
label KFB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_86
        call K_Breasts_Launch("fondle breasts") from _call_K_Breasts_Launch_1
        call KittyLust from _call_KittyLust_1     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_FondleB):
                    $ K_Brows = "confused"
                    ch_k "You're just going at them, huh?" 
        elif K_Lust >= 85:
                    pass  
        elif Cnt == (15 + K_FondleB) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused" 
                    menu:
                        ch_k "Maybe we could try something else here [K_Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump KFB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KFB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_60   
                                    call K_Pos_Reset from _call_K_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KFB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                     
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass
                                jump KFB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress  
                                    
                        "Shift actions":
                            if K_Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                            if K_Action and MultiAction:                        
                                                $ Situation = "shift"
                                                call KFB_After from _call_KFB_After
                                                call K_Suck_Breasts from _call_K_Suck_Breasts
                                            else:
                                                ch_k "I kinda need a break, so if we could wrap this up?"
                                    "Just suck on them without asking.":
                                            if K_Action and MultiAction:                            
                                                $ Situation = "auto"
                                                call KFB_After from _call_KFB_After_1
                                                call K_Suck_Breasts from _call_K_Suck_Breasts_1
                                            else:
                                                "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                ch_k "I kinda need a break, so if we could wrap this up?"
                                            
                                    "Never Mind":
                                            pass
                            else:
                                ch_k "I kinda need a break, so if we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KFB_After from _call_KFB_After_2
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_1   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_1
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KFB_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_2
                                    $ Line = 0
                                    jump KFB_After
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_19
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_3
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KFB_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_1
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KFB_After
                       
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
                                    jump KFB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_61
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KFB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_4
        
    call KittyFace("sexy") from _call_KittyFace_62 
    
    $ K_FondleB += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_FondleB == 1:            
            $ K_SEXP += 4         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "I hope there was[K_like]enough to work with."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_63
                    ch_k "Not a disappointment, right?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_39
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label K_Suck_Breasts:
    call Shift_Focus("Kitty") from _call_Shift_Focus_87
                                                                                        # Will she let you suck? Modifiers
    if K_SuckB: #You've done it before
        $ Tempmod += 15
    if not K_Chest and not K_Over:
        $ Tempmod += 15
    if K_Lust > 75: #She's really horny
        $ Tempmod += 20
    if K_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount     
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no suck breasts" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in K_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Kitty", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call KittyFace("sexy") from _call_KittyFace_64       
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)            
            "As you dive in, Kitty seems a bit surprised, but just makes a little \"purr.\""              
            jump KSB_Prep      
        else:               
            call KittyFace("surprised") from _call_KittyFace_65
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            ch_k "Nuh-uh, [K_Petname], get back to what you were doing."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_66
        ch_k "Mmm, again? Ok."
        jump KSB_Prep
    elif "suck breasts" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_67
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."]) 
        ch_k "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call KittyFace("bemused", 1) from _call_KittyFace_68
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_69
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
        ch_k "Ok, fiiiine."   
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
        jump KSB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_70
        if "no suck breasts" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no suck breasts" in K_DailyActions:  
            ch_k "I told you this was[K_like]too public!" 
        elif "no suck breasts" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_SuckB:
            call KittyFace("bemused") from _call_KittyFace_71
            ch_k "Not. . . yet. . . maybe later."
        else:
            call KittyFace("bemused") from _call_KittyFace_72
            ch_k "Um, no."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_73
                ch_k "No problem."              
                return
            "Maybe later?" if "no suck breasts" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_74  
                ch_k "I'll give it some thought, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)    
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no suck breasts")                      
                $ K_DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_75     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
                    ch_k "Only if you make it worth it."                
                    jump KSB_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_76 
                    ch_k "Um, still no."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Kitty", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_77
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)                 
                    ch_k "Ugh, I guess if you're so enthusiastic. . ."                         
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KSB_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)  
                    call KittyFace("angry", 1) from _call_KittyFace_78
                    "She shoves your head back out."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no suck breasts" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_79
        ch_k "[K_Like]get your mouth away from me."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:   
        call KittyFace("angry", 1) from _call_KittyFace_80      
        $ K_RecentActions.append("tabno")    
        $ K_DailyActions.append("tabno") 
        ch_k "Time and place, [K_Petname]!"                   
    elif K_SuckB:
        call KittyFace("sad") from _call_KittyFace_81
        ch_k "Sorry, [K_Petname], maybe later?"            
    else:
        call KittyFace("sexy") from _call_KittyFace_82 
        $ K_Mouth = "sad"
        ch_k "Nooope."
    $ K_RecentActions.append("no suck breasts")                      
    $ K_DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label KSB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0   
        call Kitty_Top_Off from _call_Kitty_Top_Off_2
        if "angry" in K_RecentActions:
            return
    
    $ Tempmod = 0      
    call K_Breasts_Launch("suck breasts") from _call_K_Breasts_Launch_2
    if not K_SuckB:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -25)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 17) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
    
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0      
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_57
    call DrainWord("Kitty","no suck breasts") from _call_DrainWord_58
    $ K_RecentActions.append("suck breasts")                      
    $ K_DailyActions.append("suck breasts") 
    
label KSB_Cycle: #Repeating strokes  
    if Trigger2 == "kissing":
            $ Trigger2 = 0 
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_88
        call K_Breasts_Launch("suck breasts") from _call_K_Breasts_Launch_3
        call KittyLust from _call_KittyLust_2     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_SuckB):
                    $ K_Brows = "confused"
                    ch_k "Are they keeping you satisfied?"   
        elif K_Lust >= 85:
                    pass
        elif Cnt == (15 + K_SuckB) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "You look like you're having fun there, but maybe we could[K_like]try something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KSB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KSB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_83   
                                    call K_Pos_Reset from _call_K_Pos_Reset_5
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KSB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                   
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_1
                                jump KSB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_1  
                                    
                        "Pull back to fondling.":  
                            if K_Action and MultiAction:
                                $ Situation = "pullback"
                                call KSB_After from _call_KSB_After
                                call K_Fondle_Breasts from _call_K_Fondle_Breasts
                            else:
                                "As you pull back, Kitty pushes you back in close."
                                ch_k "I kinda need a break, so if we could wrap this up?"
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_2
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KSB_After from _call_KSB_After_1
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_3   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_6
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KSB_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_7
                                    $ Line = 0
                                    jump KSB_After
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_20
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_1
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_8
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KSB_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_2
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KSB_After
                       
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
                                    jump KSB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_84
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KSB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_9
        
    call KittyFace("sexy") from _call_KittyFace_85 
    
    $ K_SuckB += 1  
    $ K_Action -=1
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_SuckB == 1:            
            $ K_SEXP += 4         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "I hope they were enough for you. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_86
                    ch_k "Did that satisfy you?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_40
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label K_Fondle_Thighs:
    call Shift_Focus("Kitty") from _call_Shift_Focus_89
                                                                                        # Will she let you fondle her thighs? Modifiers
    if K_FondleT: #You've done it before
        $ Tempmod += 10
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if K_Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in K_Traits:
        $ Tempmod += Taboo   
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount      
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle thighs" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in K_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Kitty", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call KittyFace("sexy") from _call_KittyFace_87       
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)            
            "As you caress her thigh, Kitty glances at you, and smiles."             
            jump KFT_Prep      
        else:               
            call KittyFace("surprised") from _call_KittyFace_88
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            ch_k "Heh, keep it above the belt, [K_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call KittyFace("surprised") from _call_KittyFace_89    
        $ K_Brows = "sad"
        if K_Lust > 60:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
        "As you pull back, Kitty looks a little sad."              
        jump KFT_Prep  
    elif "fondle thighs" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_90
        ch_k "Mmm, again? Ok."
        jump KFT_Prep
    elif "fondle thighs" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_91       
        ch_k "Didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call KittyFace("bemused", 1) from _call_KittyFace_92
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_93
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
        ch_k "Ok [K_Petname], go ahead."   
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
        jump KFT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_94
        if "no fondle thighs" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no fondle thighs" in K_DailyActions:  
            ch_k "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_FondleT:
            call KittyFace("bemused") from _call_KittyFace_95
            ch_k "Not. . . yet. . . maybe later."
        else:
            call KittyFace("bemused") from _call_KittyFace_96
            ch_k "Um, no."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_97
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no fondle thighs" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_98  
                ch_k "Heh, maybe, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)    
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no fondle thighs")                      
                $ K_DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_99     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
                    ch_k "Well[K_like]if you ask nicely. . ."             
                    jump KFT_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_100 
                    ch_k "Um, still no."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Kitty", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_101
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)                 
                    ch_k "Hmmph."                         
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KFT_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -8)  
                    call KittyFace("angry", 1) from _call_KittyFace_102
                    "She slaps your hand away."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no fondle thighs" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_103
        ch_k "Not even."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 50, 2)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1)   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_104    
        $ K_RecentActions.append("tabno")          
        $ K_DailyActions.append("tabno") 
        ch_k "Time and place, [K_Petname]!"                   
    elif K_FondleT:
        call KittyFace("sad") from _call_KittyFace_105
        ch_k "Fresh!"            
    else:
        call KittyFace("sexy") from _call_KittyFace_106 
        $ K_Mouth = "sad"
        ch_k "Nooope."
    $ K_RecentActions.append("no fondle thighs")                      
    $ K_DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label KFT_Prep:                                                                 #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off 
        if "angry" in K_RecentActions:
            return 
            
    $ Tempmod = 0    
    call K_Pussy_Launch("fondle thighs") from _call_K_Pussy_Launch
    if not K_FondleT:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 15)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
            
    if Taboo:               
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (int(Taboo/5)))                               
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_59
    call DrainWord("Kitty","no fondle thighs") from _call_DrainWord_60
    $ K_RecentActions.append("fondle thighs")                      
    $ K_DailyActions.append("fondle thighs")  
    
label KFT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_90 
        call K_Pussy_Launch("fondle thighs") from _call_K_Pussy_Launch_1
        call KittyLust from _call_KittyLust_3     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_FondleT):
                    $ K_Brows = "confused"
                    ch_k "You like how those feel, huh?"   
        elif Cnt == (15 + K_FondleT) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "You look like you're having fun there, but maybe we could[K_like]try something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KFT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KFT_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_107   
                                    call K_Pos_Reset from _call_K_Pos_Reset_10
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KFT_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                       
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_2
                                jump KFT_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_2  
                                    
                        "Can I do a little deeper?":
                                if K_Action and MultiAction:
                                    $ Situation = "shift"
                                    call KFT_After from _call_KFT_After
                                    call K_Fondle_Pussy from _call_K_Fondle_Pussy                
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        "Shift your hands a bit higher without asking":
                                if K_Action and MultiAction:
                                    $ Situation = "auto"
                                    call KFT_After from _call_KFT_After_1
                                    call K_Fondle_Pussy from _call_K_Fondle_Pussy_1    
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_k "I kinda need a break, so if we could wrap this up?" 
                
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_4
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KFT_After from _call_KFT_After_2
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_5   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                                    
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_11
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KFT_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_12
                                    $ Line = 0
                                    jump KFT_After
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_21
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_2
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_13
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KFT_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_3
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KFT_After
                       
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
                                    jump KFT_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_108
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KFT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_14
        
    call KittyFace("sexy") from _call_KittyFace_109 
    
    $ K_FondleT += 1  
    $ K_Action -=1
    if K_Legs != "pants" or K_Upskirt:        
        $ K_Addictionrate += 1
        if "addictive" in P_Traits:
            $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 1
     
    if K_FondleT == 1:            
            $ K_SEXP += 3         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "I liked that."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_110
                    ch_k "Was that enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_41
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label K_Fondle_Pussy:
    call Shift_Focus("Kitty") from _call_Shift_Focus_91
                                                                                        # Will she let you fondle? Modifiers
    if K_FondleP: #You've done it before
        $ Tempmod += 20
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if K_Lust > 75: #She's really horny
        $ Tempmod += 15
    if K_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount     
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle pussy" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in K_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Kitty", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call KittyFace("sexy") from _call_KittyFace_111       
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2)
            "As your hand creeps up her thigh, Kitty seems a bit surprised, but then nods."            
            jump KFP_Prep      
        else:               
            call KittyFace("surprised") from _call_KittyFace_112
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
            ch_k "Nuh-uh, [K_Petname], get back to what you were doing."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call KittyFace("surprised") from _call_KittyFace_113   
        $ K_Brows = "sad"        
        if K_Lust > 80:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -4)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
        "As your hand pulls out, Kitty gasps and looks upset."              
        jump KFP_Prep     
    elif "fondle pussy" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_114
        ch_k "Mmm, again? Ok."
        jump KFP_Prep
    elif "fondle pussy" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_115
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_k "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call KittyFace("bemused", 1) from _call_KittyFace_116
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_117
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
        ch_k "Ok, whatever."   
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
        jump KFP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_118
        if "no fondle pussy" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no fondle pussy" in K_DailyActions:  
            ch_k "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_FondleP:
            call KittyFace("bemused") from _call_KittyFace_119
            ch_k "Um, not down there, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_120
            ch_k "Um, no."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_121
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_122  
                ch_k "I'll give it some thought, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no fondle pussy")                      
                $ K_DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_123     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    ch_k "I like it when you beg. . ."                    
                    jump KFP_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_124 
                    ch_k "Nuh uh."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Kitty", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_125
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Well. . . I guess. . ."
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KFP_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)  
                    call KittyFace("angry", 1) from _call_KittyFace_126
                    "She slaps your hand away."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no fondle pussy" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_127
        ch_k "Keep away from my kitty, [K_Petname]."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 70, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)    
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_128    
        $ K_RecentActions.append("tabno")                   
        $ K_DailyActions.append("tabno")
        ch_k "Time and place, [K_Petname]!"                   
    elif K_FondleP:
        call KittyFace("sad") from _call_KittyFace_129
        ch_k "Sorry, keep your hands out of there."           
    else:
        call KittyFace("sexy") from _call_KittyFace_130 
        $ K_Mouth = "sad"
        ch_k "No luck [K_Petname]."
    $ K_RecentActions.append("no fondle pussy")                      
    $ K_DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label KFP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_1   
        if "angry" in K_RecentActions:
            return 
    $ Tempmod = 0
    
    call K_Pussy_Launch("fondle pussy") from _call_K_Pussy_Launch_2
    if not K_FondleP:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -50)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 35)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 25) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_61
    call DrainWord("Kitty","no fondle pussy") from _call_DrainWord_62
    $ K_RecentActions.append("fondle pussy")                      
    $ K_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label KFP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_92 
        call K_Pussy_Launch("fondle pussy") from _call_K_Pussy_Launch_3
        call KittyLust from _call_KittyLust_4     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_FondleP):
                    $ K_Brows = "confused"
                    ch_k "You like how that feels, huh?"  
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_FondleP) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "You look like you're having fun there, but maybe we could[K_like]try something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KFP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KFP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_131   
                                    call K_Pos_Reset from _call_K_Pos_Reset_15
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KFP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                        
                        "I want to stick a finger in. . ." if Speed != 2:
                            if K_InsertP: 
                                $ Speed = 2
                            else:
                                menu:                                
                                    "Ask her first":
                                        $ Situation = "shift"
                                    "Don't ask first [[just stick it in]":                                    
                                        $ Situation = "auto"
                                call K_Insert_Pussy from _call_K_Insert_Pussy  
                       
                        "Pull back to fondling" if Speed == 2:
                                $ Speed = 1   
                                      
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_3
                                jump KFP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_3  
                        
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:                                                                                         
                                            "I want to lick your pussy.":
                                                    $ Situation = "shift"
                                                    call KFP_After from _call_KFP_After
                                                    call K_Lick_Pussy from _call_K_Lick_Pussy                 
                                            "Just start licking":
                                                    $ Situation = "auto"
                                                    call KFP_After from _call_KFP_After_1
                                                    call K_Lick_Pussy from _call_K_Lick_Pussy_1         
                                            "Pull back to the thighs":
                                                    $ Situation = "pullback"
                                                    call KFP_After from _call_KFP_After_2
                                                    call K_Fondle_Thighs from _call_K_Fondle_Thighs
#                                            "I want to stick a dildo in.":
#                                                    call K_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call KFP_After
#                                                        call K_Dildo_Pussy  
#                                                    else:
#                                                        jump KFP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"           
                                        
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_6
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KFP_After from _call_KFP_After_3
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_7   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_16
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KFP_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_17
                                    $ Line = 0
                                    jump KFP_After
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_22
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_3
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_18
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KFP_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_4
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KFP_After
                       
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
                                    jump KFP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_132
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KFP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_19
        
    call KittyFace("sexy") from _call_KittyFace_133 
    
    $ K_FondleP += 1  
    $ K_Action -=1
    if K_Legs != "pants" or K_Upskirt:        
        $ K_Addictionrate += 1
        if "addictive" in P_Traits:
            $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_FondleP == 1:            
            $ K_SEXP += 7         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Your hand is. . . bigger than mine."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_134
                    ch_k "Did you get what you needed?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_42
    return   

# end K_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label K_Insert_Pussy:
    call Shift_Focus("Kitty") from _call_Shift_Focus_93
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Kitty", 1100, TabM = 2):
            call KittyFace("surprised") from _call_KittyFace_135       
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
            "As you slide a finger in, Kitty seems a bit surprised, but seems into it."              
            jump KIP_Prep
        else:   
            call KittyFace("surprised",2) from _call_KittyFace_136
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
            ch_k "Oooh!"
            "She slaps your hand back."
            call KittyFace("perplexed",1) from _call_KittyFace_137
            ch_k "Um, no take that out."
            return            
    
    if ApprovalCheck("Kitty", 1100, TabM = 2):                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_138
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, whatever."    
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_139
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3) 
            ch_k "Mmmmmm."                
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump KIP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call KittyFace("bemused", 2) from _call_KittyFace_140
        ch_k "Um, no thanks, [K_Petname]."
        $ K_Blush = 1
    return
    
                
label KIP_Prep: #Animation set-up     
    if not K_InsertP:
        $ K_InsertP = 1
        $ K_SEXP += 10          
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -60)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 55)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 25)
                
    if not K_Forced and Situation != "auto":        
        call K_Undress("bottom") from _call_K_Undress_4
        if "angry" in K_RecentActions:
            return    
            
#    call K_Pussy_Launch("insert pussy")
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
        
    $ Line = 0 
    $ Cnt = 0     
    $ Speed = 2
    return

# end K_Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label K_Lick_Pussy: 
    call Shift_Focus("Kitty") from _call_Shift_Focus_94
                                                                                  # Will she let you fondle? Modifiers     
    if K_LickP: #You've done it before
        $ Tempmod += 15
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if K_Lust > 95:
        $ Tempmod += 20  
    elif K_Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if K_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount     
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick pussy" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in K_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Kitty", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call KittyFace("surprised") from _call_KittyFace_141
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Kitty jumps, but then softens."  
            call KittyFace("sexy") from _call_KittyFace_142           
            jump KLP_Prep
        else:   
            call KittyFace("surprised") from _call_KittyFace_143
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
            ch_k "Oooo! Um, no, no thanks. No. . ." 
            call KittyFace("perplexed",1) from _call_KittyFace_144
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_145
        ch_k "Mmm, again? Ok."
        jump KLP_Prep
    elif "lick pussy" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_146
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a girl wants. . .",
            "Mmm. . ."]) 
        ch_k "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_147
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, whatever."    
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_148
            $ K_Eyes = "closed"            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)            
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)
            ch_k "Oooooooh. . ."                
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump KLP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_149
        if "no lick pussy" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no lick pussy" in K_DailyActions:  
            ch_k "You already got your answer!" 
        elif "no lick pussy" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_LickP:
            call KittyFace("bemused") from _call_KittyFace_150
            ch_k "That's pretty intimate, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_151
            ch_k "Oh, um, no, I'm not really comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_152
                ch_k "Yeah, ok, [K_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_153  
                ch_k "I'll be thinking about it, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no lick pussy")                      
                $ K_DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_154           
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    ch_k "Oh. . . you're probably right. . ."      
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                    jump KLP_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_155 
                    ch_k "Um, not this time, [K_Petname], that's too. . ."     
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Kitty", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_156
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, get in there if you're so determined."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KLP_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)  
                    call KittyFace("angry", 1) from _call_KittyFace_157
                    "She shoves your head back."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no lick pussy" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_158
        ch_k "Not even, [K_Petname]."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)     
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_159    
        $ K_RecentActions.append("tabno")                   
        $ K_DailyActions.append("tabno") 
        ch_k "This just really isn't the time or place, [K_Petname]!"                   
    elif K_LickP:
        call KittyFace("sad") from _call_KittyFace_160 
        ch_k "Keep your head out of there."    
    else:
        call KittyFace("surprised") from _call_KittyFace_161
        ch_k "Ugh!"
        call KittyFace from _call_KittyFace_162
    $ K_RecentActions.append("no lick pussy")                      
    $ K_DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label KLP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        if K_Legs == "pants":
            $ Tempmod = 15
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_2
        if "angry" in K_RecentActions:
            return  
            
    $ Tempmod = 0      
    call K_Pussy_Launch("lick pussy") from _call_K_Pussy_Launch_4
    if not K_LickP:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -30)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 35)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 75) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 35)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 15)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if K_Legs == "skirt":
        $ K_Upskirt = 1  
        $ K_SeenPanties = 1
    if not K_Panties:
        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_4
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_63
    call DrainWord("Kitty","no lick pussy") from _call_DrainWord_64
    $ K_RecentActions.append("lick pussy")                      
    $ K_DailyActions.append("lick pussy") 
    
label KLP_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_95 
        call K_Pussy_Launch("lick pussy") from _call_K_Pussy_Launch_5
        call KittyLust from _call_KittyLust_5     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_LickP):
                    $ K_Brows = "confused"
                    ch_k "You like it down there?"  
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_LickP) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KLP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KLP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_163   
                                    call K_Pos_Reset from _call_K_Pos_Reset_20
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KLP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                  
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_4
                                jump KLP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_5  
                        
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    if K_Action and MultiAction:
                                                        $ Situation = "pullback"
                                                        call KLP_After from _call_KLP_After
                                                        call K_Fondle_Pussy from _call_K_Fondle_Pussy_2
                                                    else:
                                                        ch_k "I kinda need a break, so if we could wrap this up?"  
#                                            "I want to stick a dildo in.":
#                                                    call K_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call KLP_After
#                                                        call K_Dildo_Pussy  
#                                                    else:
#                                                        jump KLP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_8
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KLP_After from _call_KLP_After_1
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_9   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_21
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KLP_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_22
                                    $ Line = 0
                                    jump KLP_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto") from _call_K_Undress_6
            
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_23
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_4
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_23
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KLP_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_5
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KLP_After
                       
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
                                    jump KLP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_164
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KLP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_24
        
    call KittyFace("sexy") from _call_KittyFace_165 
    
    $ K_LickP += 1  
    $ K_Action -=1     
    if K_Legs != "pants" or K_Upskirt:        
        $ K_Addictionrate += 1
        if "addictive" in P_Traits:
            $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 3 if R_LikeKitty >= 800 else 2
     
    if K_LickP == 1:            
            $ K_SEXP += 10         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Was it. . . good?"
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_166
                    ch_k "Well, did you like the taste?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_43
    return   


# end K_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label K_Fondle_Ass: 
    call Shift_Focus("Kitty") from _call_Shift_Focus_96
                                                                                     # Will she let you fondle? Modifiers
    if K_FondleA: #You've done it before
        $ Tempmod += 10
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if K_Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in K_Traits:
        $ Tempmod += Taboo  
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount      
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle ass" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in K_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Kitty", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call KittyFace("surprised", 1) from _call_KittyFace_167  
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
            "As your hand creeps down her backside, Kitty jumps a bit, and then relaxes."              
            call KittyFace("sexy") from _call_KittyFace_168  
            jump KFA_Prep  
        else:          
            call KittyFace("surprised") from _call_KittyFace_169
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
            ch_k "Hands off, [K_Petname]."   
            call KittyFace("bemused") from _call_KittyFace_170
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call KittyFace("surprised") from _call_KittyFace_171   
        $ K_Brows = "sad"        
        if K_Lust > 80:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -4)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
        "As your finger slides out, Kitty gasps and looks upset."              
        jump KFA_Prep     
    elif "fondle ass" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_172
        ch_k "Mmm, again? Ok."
        jump KFA_Prep
    elif "fondle ass" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_173
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."]) 
        ch_k "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_174
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
            ch_k "Ok, geeze."   
        else:
            call KittyFace("bemused, 1") from _call_KittyFace_175 
            ch_k "Ok, go for it."   
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
        jump KFA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_176
        if "no fondle ass" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no fondle ass" in K_DailyActions:  
            ch_k "I told you not to touch me like that in public!" 
        elif "no fondle ass" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_FondleA:
            call KittyFace("bemused") from _call_KittyFace_177
            ch_k "Not yet, [K_Petname]. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_178
            ch_k "Let's not, ok [K_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_179
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_180  
                ch_k "Heh, maybe, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 2)  
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no fondle ass")                      
                $ K_DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_181     
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    ch_k "I like it when you beg. . ."                           
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
                    jump KFA_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_182 
                    ch_k "Nuh uh."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Kitty", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_183
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -1) 
                    ch_k "Fine, I suppose."                
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3) 
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KFA_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)  
                    call KittyFace("angry", 1) from _call_KittyFace_184
                    "She slaps your hand away."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                        
    if "no fondle ass" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_185
        ch_k "Back off!"
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)    
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_186    
        $ K_RecentActions.append("tabno")   
        $ K_DailyActions.append("tabno") 
        ch_k "[K_Petname]! Not here!"                   
    elif K_FondleA:
        call KittyFace("sad") from _call_KittyFace_187
        ch_k "Sorry, hands to yourself."        
    else:
        call KittyFace("sexy") from _call_KittyFace_188 
        $ K_Mouth = "sad"
        ch_k "Scram, [K_Petname]."
    $ K_RecentActions.append("no fondle ass")                      
    $ K_DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_k "Sorry, I don't even know how I got here. . ."
return

label KFA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_3
        if "angry" in K_RecentActions:
            return    
    $ Tempmod = 0      
    call K_Pussy_Launch("fondle ass") from _call_K_Pussy_Launch_6
    if not K_FondleA:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 15) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 12)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_65
    call DrainWord("Kitty","no fondle ass") from _call_DrainWord_66
    $ K_RecentActions.append("fondle ass")                      
    $ K_DailyActions.append("fondle ass") 
    
label KFA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_97 
        call K_Pussy_Launch("fondle ass") from _call_K_Pussy_Launch_7
        call KittyLust from _call_KittyLust_6     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_FondleA):
                    $ K_Brows = "confused"
                    ch_k "Uh, that's nice, but. . ."  
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_FondleA) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KFA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KFA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_189   
                                    call K_Pos_Reset from _call_K_Pos_Reset_25
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KFA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_5
                                jump KFA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_7  
                        
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call KFA_After from _call_KFA_After
                                                    call K_Insert_Ass from _call_K_Insert_Ass                 
                                            "Just stick a finger in without asking.":
                                                    $ Situation = "auto"
                                                    call KFA_After from _call_KFA_After_1
                                                    call K_Insert_Ass from _call_K_Insert_Ass_1
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call KFA_After from _call_KFA_After_2
                                                    call K_Lick_Ass from _call_K_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call KFA_After from _call_KFA_After_3
                                                    call K_Lick_Ass from _call_K_Lick_Ass_1    
#                                            "I want to stick a dildo in.":
#                                                    call K_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call KFA_After
#                                                        call K_Dildo_Ass  
#                                                    else:
#                                                        jump KFA_Cycle   
                                            "Never Mind":
                                                        pass              
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_10
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KFA_After from _call_KFA_After_4
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_11   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_26
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KFA_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_27
                                    $ Line = 0
                                    jump KFA_After
        #End menu (if Line)
        
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_24
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_5
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_28
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KFA_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_6
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KFA_After
                       
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
                                    jump KFA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_190
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KFA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_29
        
    call KittyFace("sexy") from _call_KittyFace_191 
    
    $ K_FondleA += 1  
    $ K_Action -=1            
    if K_Legs != "pants" or K_Upskirt:        
        $ K_Addictionrate += 1
        if "addictive" in P_Traits:
            $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 1
     
    if K_FondleA == 1:            
            $ K_SEXP += 4         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "Huh. . . um. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_192
                    ch_k "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_44
    return   


# end K_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label K_Insert_Ass:
    call Shift_Focus("Kitty") from _call_Shift_Focus_98
    
    if K_InsertA: #You've done it before
        $ Tempmod += 25
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if K_Lust > 85 and K_Loose: #She's really horny
        $ Tempmod += 15
    if K_Lust > 95 and K_Loose:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if K_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25 
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no insert ass" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in K_RecentActions else 0   

    if K_Plugged:
        "You remove the plug from her ass"
        $ K_Plugged = 0
            
    $ Approval = ApprovalCheck("Kitty", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call KittyFace("surprised") from _call_KittyFace_193
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 2) 
            "As you slide a finger in, Kitty tightens around it in surprise, but seems into it."  
            call KittyFace("sexy") from _call_KittyFace_194           
            jump KIA_Prep
        else:   
            call KittyFace("surprised") from _call_KittyFace_195
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
            ch_k "Whoa, back off, [K_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in K_DailyActions and not K_Loose:
        call KittyFace("bemused", 1) from _call_KittyFace_196
        ch_k "I'm still a little sore from earlier, [K_Petname]."
    elif "insert ass" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_197
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Take it easy though.",
            "Mmm. . ."]) 
        ch_k "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_198
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
            ch_k "Ok, whatever."    
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_199
            $ K_Eyes = "closed"            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)            
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)
            ch_k "Mmmmm. . ."                
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2) 
        jump KIA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call KittyFace("angry", 1) from _call_KittyFace_200
        if "no insert ass" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no insert ass" in K_DailyActions:  
            ch_k "I told you that wasn't appropriate!" 
        elif "no insert ass" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_InsertA:
            call KittyFace("perplexed", 1) from _call_KittyFace_201
            ch_k "I. . . don't think that's. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_202
            ch_k "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_203
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_204  
                ch_k "It's. . . possible, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no insert ass")                      
                $ K_DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_205           
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    ch_k "Ok, you're probably right. . ."      
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                    jump KIA_Prep
                else:   
                    call KittyFace("bemused") from _call_KittyFace_206 
                    ch_k "I really don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Kitty", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and K_Forced):                    
                    call KittyFace("surprised", 1) from _call_KittyFace_207
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Oh. . . well, ok then. . ."                     
                    call KittyFace("sad") from _call_KittyFace_208
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KIA_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)  
                    call KittyFace("angry", 1) from _call_KittyFace_209
                    "She slaps your hand away."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no insert ass" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_210
        ch_k "Um, no way."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 10) if K_Inbt > 50 else Statupdate("Kitty", "Lust", K_Lust, 50, 3) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)      
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_211    
        $ K_RecentActions.append("tabno")                   
        $ K_DailyActions.append("tabno") 
        ch_k "[K_Petname]! Time and place!"                   
    elif K_InsertA:
        call KittyFace("sad") from _call_KittyFace_212 
        ch_k "I don't feel like it."    
    else:
        call KittyFace("surprised") from _call_KittyFace_213
        ch_k "That's. . . not cool."
        call KittyFace from _call_KittyFace_214
    $ K_RecentActions.append("no insert ass")                      
    $ K_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label KIA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_4
        if "angry" in K_RecentActions:
            return    
            
    $ Tempmod = 0      
    call K_Pussy_Launch("insert ass") from _call_K_Pussy_Launch_8
    if not K_InsertA:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -50)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 60)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 35) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 25)
            
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_67
    call DrainWord("Kitty","no insert ass") from _call_DrainWord_68
    $ K_RecentActions.append("insert ass")                      
    $ K_DailyActions.append("insert ass") 
    
label KIA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_99 
        call K_Pussy_Launch("insert ass") from _call_K_Pussy_Launch_9
        call KittyLust from _call_KittyLust_7     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_InsertA):
                    $ K_Brows = "confused"
                    ch_k "What are you even?"  
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_InsertA) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting kind sore, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KIA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KIA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_215   
                                    call K_Pos_Reset from _call_K_Pos_Reset_30
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KIA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_6
                                jump KIA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_8  
                        
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    $ Situation = "pullback"
                                                    call KIA_After from _call_KIA_After
                                                    call K_Fondle_Ass from _call_K_Fondle_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call KIA_After from _call_KIA_After_1
                                                    call K_Lick_Ass from _call_K_Lick_Ass_2                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call KIA_After from _call_KIA_After_2
                                                    call K_Lick_Ass from _call_K_Lick_Ass_3    
#                                            "I want to stick a dildo in.":
#                                                    call K_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call KIA_After
#                                                        call K_Dildo_Ass  
#                                                    else:
#                                                        jump KIA_Cycle  
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_12
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KIA_After from _call_KIA_After_3
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_13   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_31
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KIA_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_32
                                    $ Line = 0
                                    jump KIA_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto") from _call_K_Undress_9
            
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_25
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_6
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_33
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KIA_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_7
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KIA_After
                       
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
                                    jump KIA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_216
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KIA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_34
        
    call KittyFace("sexy") from _call_KittyFace_217 
    
    $ K_InsertA += 1  
    $ K_Action -=1            
    $ K_Addictionrate += 1
    if "addictive" in P_Traits:
        $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_InsertA == 1:            
            $ K_SEXP += 12         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was odd. . ."
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_218
                    ch_k "Well? Satisfied?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_45
    return   


# end K_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label K_Lick_Ass: 
    call Shift_Focus("Kitty") from _call_Shift_Focus_100
                                                                             # Will she let you lick? Modifiers         
    if K_LickA: #You've done it before
        $ Tempmod += 20
    if K_Legs == "pants" or HoseNum("Kitty") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if K_Lust > 95:
        $ Tempmod += 20  
    elif K_Lust > 85: #She's really horny
        $ Tempmod += 15    
    if K_Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in K_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in K_Traits or "sex friend" in K_Petnames:
        $ Tempmod += 10
    elif "ex" in K_Traits:
        $ Tempmod -= 25  
    if K_ForcedCount and not K_Forced:
        $ Tempmod -= 5 * K_ForcedCount 
    
    if Taboo and "tabno" in K_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick ass" in K_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in K_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Kitty", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call KittyFace("surprised") from _call_KittyFace_219   
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 3) 
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Kitty startles briefly, but then begins to melt."  
            call KittyFace("sexy") from _call_KittyFace_220  
            jump KLA_Prep
        else:   
            call KittyFace("surprised") from _call_KittyFace_221
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -2)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -3)
            ch_k "Um, don't do that. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in K_RecentActions:
        call KittyFace("sexy", 1) from _call_KittyFace_222
        ch_k "Mmm, again? Ok."
        jump KLA_Prep
    elif "lick ass" in K_DailyActions:
        call KittyFace("sexy", 1) from _call_KittyFace_223
        ch_k "Didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if K_Forced:
            call KittyFace("sad") from _call_KittyFace_224
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -3, 1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 20, -2, 1)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
            ch_k "Ok, whatever."    
        else:
            call KittyFace("sexy", 1) from _call_KittyFace_225
            $ K_Eyes = "closed"            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)            
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 3)
            ch_k "Wha. . ."                
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 20, 1)
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 1)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 2) 
        jump KLA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call KittyFace("angry", 1) from _call_KittyFace_226
        if "no lick ass" in K_RecentActions:  
            ch_k "I[K_like]{i}just{/i} told you \"no!\""
        elif Taboo and "tabno" in K_DailyActions and "no lick ass" in K_DailyActions:  
            ch_k "I told you not to touch me like that in public!" 
        elif "no lick ass" in K_DailyActions:       
            ch_k "[K_Like]take a lesson, [K_Petname]."
        elif Taboo and "tabno" in K_DailyActions:  
            ch_k "Not here!"  
        elif not K_LickA:                    #First time dialog
            call KittyFace("bemused", 1) from _call_KittyFace_227
            if K_Love >= K_Obed and K_Love >= K_Inbt:            
                ch_k "That's, I don't know. . ."
            elif K_Obed >= K_Inbt:            
                ch_k "You don't have to do that."
            else:
                $ K_Eyes = "sexy"
                ch_k "That's kinda gross. . ."
        else:
            call KittyFace("bemused") from _call_KittyFace_228
            ch_k "Not now, [K_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in K_DailyActions:
                call KittyFace("bemused") from _call_KittyFace_229
                ch_k "Yeah, ok, [K_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in K_DailyActions:
                call KittyFace("sexy") from _call_KittyFace_230  
                ch_k "Anything's possible, [K_Petname]."
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 2)   
                if Taboo:                    
                    $ K_RecentActions.append("tabno")                      
                    $ K_DailyActions.append("tabno") 
                $ K_RecentActions.append("no lick ass")                      
                $ K_DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call KittyFace("sexy") from _call_KittyFace_231           
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 2)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                    ch_k "Ok, you're probably right. . ."      
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 2)
                    jump KLA_Prep
                else:   
                    call KittyFace("sexy") from _call_KittyFace_232 
                    ch_k "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Kitty", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and K_Forced):
                    call KittyFace("sad") from _call_KittyFace_233
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, -5, 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -2)                 
                    ch_k "Ok, {i}fine{/i}."  
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 1) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ K_Forced = 1
                    jump KLA_Prep
                else:                              
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)  
                    call KittyFace("angry", 1) from _call_KittyFace_234
                    "She shoves your head back."   
                    $ K_RecentActions.append("angry")
                    $ K_DailyActions.append("angry")   
                    
    if "no lick ass" in K_DailyActions:
        ch_k "How many times do I have to say \"no?\""   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif K_Forced:
        call KittyFace("angry", 1) from _call_KittyFace_235
        ch_k "Ew, no way."
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 10) if K_Inbt > 50 else Statupdate("Kitty", "Lust", K_Lust, 50, 3) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)   
        $ K_RecentActions.append("angry")
        $ K_DailyActions.append("angry")   
    elif Taboo:
        call KittyFace("angry", 1) from _call_KittyFace_236    
        $ K_RecentActions.append("tabno")                   
        $ K_DailyActions.append("tabno") 
        ch_k "This just really isn't the time or place, [K_Petname]!"                   
    elif K_LickA:
        call KittyFace("sad") from _call_KittyFace_237 
        ch_k "Sorry, no more of that."    
    else:
        call KittyFace("surprised") from _call_KittyFace_238
        ch_k "Ew."
        call KittyFace from _call_KittyFace_239
    $ K_RecentActions.append("no lick ass")                      
    $ K_DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label KLA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not K_Forced and Situation != "auto":
        $ Tempmod = 0
        if K_Legs == "pants":
            $ Tempmod = 15
        call Kitty_Bottoms_Off from _call_Kitty_Bottoms_Off_5
        if "angry" in K_RecentActions:
            return    
    $ Tempmod = 0  
    call K_Pussy_Launch("lick ass") from _call_K_Pussy_Launch_10
    if not K_LickA:        
        if K_Forced:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -30)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 40)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 80) 
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 35)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 25)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 55)
    if Taboo:
        $ K_Inbt += int(Taboo/10)  
        $ K_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ K_Upskirt = 1
    if K_Legs == "skirt":
        $ K_SeenPanties = 1
    if not K_Panties:
        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_5
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Kitty","tabno") from _call_DrainWord_69
    call DrainWord("Kitty","no lick ass") from _call_DrainWord_70
    
    $ K_RecentActions.append("lick") if "lick" not in K_RecentActions else K_RecentActions
    $ K_RecentActions.append("ass") if "ass" not in K_RecentActions else K_RecentActions
    $ K_RecentActions.append("lick ass")  
    
    $ K_DailyActions.append("lick") if "lick" not in K_DailyActions else K_RecentActions
    $ K_DailyActions.append("ass") if "ass" not in K_DailyActions else K_RecentActions                    
    $ K_DailyActions.append("lick ass")  
label KLA_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Kitty") from _call_Shift_Focus_101 
        call K_Pussy_Launch("lick ass") from _call_K_Pussy_Launch_11
        call KittyLust from _call_KittyLust_8     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if K_SEXP >= 100 or ApprovalCheck("Kitty", 1200, "LO"):
            pass
        elif Cnt == (5 + K_LickA):
                    $ K_Brows = "confused"
                    ch_k "What are you even?"  
        elif K_Lust >= 80:
                    pass
        elif Cnt == (15 + K_LickA) and K_SEXP >= 15 and not ApprovalCheck("Kitty", 1500):
                    $ K_Brows = "confused"        
                    menu:
                        ch_k "[K_Petname], this is getting weird, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump KLA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump KLA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Kitty", 1200) or ApprovalCheck("Kitty", 500, "O"):                        
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call KittyFace("angry", 1) from _call_KittyFace_240   
                                    call K_Pos_Reset from _call_K_Pos_Reset_35
                                    "She scowls at you and pulls back."
                                    ch_k "Fun for you maybe, I'm tired of it."                         
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -3, 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -4, 1)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, -1, 1)                    
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -1, 1)  
                                    $ K_RecentActions.append("angry")
                                    $ K_DailyActions.append("angry")   
                                    jump KLA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                           
                        "Slap her ass":                     
                                call K_Slap_Ass from _call_K_Slap_Ass_7
                                jump KLA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                            
                        "Maybe lose some clothes. . .":
                                    call K_Undress from _call_K_Undress_10  
                        
                        "Shift actions":
                                if K_Action and MultiAction:
                                        menu:   
                                            "Switch to fondling.":
                                                    $ Situation = "pullback"
                                                    call KLA_After from _call_KLA_After
                                                    call K_Fondle_Ass from _call_K_Fondle_Ass_1
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call KLA_After from _call_KLA_After_1
                                                    call K_Insert_Ass from _call_K_Insert_Ass_2                 
                                            "Just stick a finger in [[without asking].":
                                                    $ Situation = "auto"
                                                    call KLA_After from _call_KLA_After_2
                                                    call K_Insert_Ass from _call_K_Insert_Ass_3                        
#                                            "I want to stick a dildo in.":
#                                                    call K_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call KLA_After
#                                                        call K_Dildo_Ass  
#                                                    else:
#                                                        jump KLA_Cycle   
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if K_Action and MultiAction:
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_14
                                    if Trigger2:
                                         $ K_Action -= 1
                                else:
                                    ch_k "I kinda need a break, so if we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call KLA_After from _call_KLA_After_3
                                    call Kitty_Offhand_Set from _call_Kitty_Offhand_Set_15   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_36
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump KLA_After
                        "Let's stop for now." if not MultiAction: 
                                    call K_Pos_Reset from _call_K_Pos_Reset_37
                                    $ Line = 0
                                    jump KLA_After
        #End menu (if Line)
        
        if K_Panties or K_Legs == "pants" or HoseNum("Kitty") >= 5: #This checks if Kitty wants to strip down.
                call K_Undress("auto") from _call_K_Undress_11
            
        call Sex_Dialog("Kitty",Partner) from _call_Sex_Dialog_26
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or K_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PK_Cumming from _call_PK_Cumming_7
                            if "angry" in K_RecentActions:  
                                call K_Pos_Reset from _call_K_Pos_Reset_38
                                return    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                            if 100 > K_Lust >= 70 and K_OCount < 2:             
                                $ K_RecentActions.append("unsatisfied")                      
                                $ K_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump KLA_After 
                            $ Line = "came"
     
                    #If Kitty can cum
                    if K_Lust >= 100:                                               
                        call K_Cumming from _call_K_Cumming_8
                        if Situation == "shift" or "angry" in K_RecentActions:
                            jump KLA_After
                       
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
                                    jump KLA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_k "It's[K_like]getting kinda late."  
        elif Round == 5:
            ch_k "We should wrap this up."       
    
    #Round = 0 loop breaks
    call KittyFace("bemused", 0) from _call_KittyFace_241
    $ Line = 0
    ch_k "Time to take a little break, for now."
    
    
label KLA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call K_Pos_Reset from _call_K_Pos_Reset_39
        
    call KittyFace("sexy") from _call_KittyFace_242 
    
    $ K_LickA += 1  
    $ K_Action -=1      
    if K_Legs != "pants" or K_Upskirt:        
        $ K_Addictionrate += 1
        if "addictive" in P_Traits:
            $ K_Addictionrate += 1
    
    if R_Loc == bg_current and "noticed kitty" in R_RecentActions: #If Rogue was participating
        $ R_LikeKitty += 2 if R_LikeKitty >= 800 else 1
     
    if K_LickA == 1:            
            $ K_SEXP += 15         
            if not Situation: 
                if K_Love >= 500 and "unsatisfied" not in K_RecentActions:
                    ch_k "That was. . . good for you?"
                elif K_Obed <= 500 and P_Focus <= 20:
                    call KittyFace("perplexed", 1) from _call_KittyFace_243
                    ch_k "Did that work for you?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_k "Ok, what else did you want to do?"
    call Checkout from _call_Checkout_46
    return   

# end K_Lick Ass /////////////////////////////////////////////////////////////////////////////

