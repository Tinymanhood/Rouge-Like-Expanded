# E_Massage /////////////////////////////////////////////////////////////////////////////
label E_Massage:
    call Shift_Focus("Emma") from _call_Shift_Focus_176
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Emma", 500, TabM = 2) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call EmmaFace("bemused", 1) from _call_EmmaFace_1128
        if E_Forced:
                call EmmaFace("sad") from _call_EmmaFace_1129
                $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "I could use it, [E_Petname]."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_Massage_Prep
        
    else:
        call EmmaFace("angry", 1) from _call_EmmaFace_1130
        if "no massage" in E_RecentActions:  
            ch_e "I only {i}just{/i} refused you, [E_Petname]."
        elif "no massage" in E_DailyActions:       
            ch_e "I told you \"no\" earlier, [E_Petname]."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1131
            ch_e "I'm not interested at the moment, [E_Petname]."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1132
                ch_e "Don't concern yourself, [E_Petname]."              
                return
            "Maybe later?" if "no massage" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1133  
                ch_e "Perhaps."
                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 1)
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)  
                $ E_RecentActions.append("no massage")                      
                $ E_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call EmmaFace("sexy") from _call_EmmaFace_1134     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "I do have some tension built up. . ."                
                    jump E_Massage_Prep
                else:   
                    call EmmaFace("sly", Brows="confused") from _call_EmmaFace_1135 
                    ch_e "No." 
    
    if "no massage" in E_DailyActions:
        ch_e "I've made myself clear on this, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1136
        ch_e "You'll have to keep your hands limber for yourself."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1137    
        ch_e "I can't been seen doing that with you."                  
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1138 
        $ E_Mouth = "sad"
        ch_e "I really can't."    
    $ E_RecentActions.append("no massage")                      
    $ E_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label E_Massage_Prep:
    call Emma_Top_Off("massage") from _call_Emma_Top_Off_2
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
    call Shift_Focus("Emma") from _call_Shift_Focus_177
    
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
            call EmmaFace("sexy") from _call_EmmaFace_1139       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you cup her breast, Emma gently nods."            
            jump E_FB_Prep        
        else:   
            call EmmaFace("surprised") from _call_EmmaFace_1140
            $ E_Brows = "confused"
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call EmmaFace("sexy", 1) from _call_EmmaFace_1141
        if E_Forced: 
            call EmmaFace("sad") from _call_EmmaFace_1142
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)           
        elif not Taboo and "tabno" in E_DailyActions:        
            ch_e "This does seem less. . . exposed"   
            
    if "fondle breasts" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1143
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FB_Prep
    elif "fondle breasts" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1144
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
            
    if Approval >= 2:             
        call EmmaFace("bemused", 1) from _call_EmmaFace_1145
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1146
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "That sounds lovely, ravish me."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FB_Prep
        
    else:
        call EmmaFace("angry", 1) from _call_EmmaFace_1147
        if "no fondle breasts" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle breasts" in E_DailyActions:  
            ch_e "You've been warned." 
        elif "no fondle breasts" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleB:
            call EmmaFace("bemused") from _call_EmmaFace_1148
            ch_e "I highly doubt you could handle them, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1149
            ch_e "You wish."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1150
                ch_e "Don't concern yourself, [E_Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1151  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1152     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Politeness can be rewarded. . ."                
                    jump E_FB_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1153 
                    ch_e "This wasn't a \"tone\" issue." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1154
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1155
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
    
    if "no fondle breasts" in E_DailyActions:
        ch_e "You need to pay attention when I speak to you."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1156
        ch_e "Don't push your luck."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1157    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I can't been seen doing that with you."                   
    elif E_FondleB:
        call EmmaFace("sad") from _call_EmmaFace_1158
        ch_e "I'm afraid you haven't earned back my good graces."        
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1159 
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
        call Emma_Top_Off from _call_Emma_Top_Off_3
        if "angry" in E_RecentActions:
            return
        
    $ Tempmod = 0  
    call E_Breasts_Launch("fondle breasts") from _call_E_Breasts_Launch
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
        call DrainWord("Emma","tabno") from _call_DrainWord_140
    call DrainWord("Emma","no fondle breasts") from _call_DrainWord_141
    $ E_RecentActions.append("fondle breasts")                      
    $ E_DailyActions.append("fondle breasts") 
    
label E_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_178
        call E_Breasts_Launch("fondle breasts") from _call_E_Breasts_Launch_1
        call EmmaLust from _call_EmmaLust_13     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1160   
                                    call E_Pos_Reset from _call_E_Pos_Reset_16
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
                                call E_Slap_Ass from _call_E_Slap_Ass_7
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
                                    call E_Undress from _call_E_Undress_10  
                                    
                        "Shift actions":
                            if E_Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                            if E_Action and MultiAction:                        
                                                $ Situation = "shift"
                                                call E_FB_After from _call_E_FB_After_1
                                                call E_Suck_Breasts from _call_E_Suck_Breasts
                                            else:
                                                ch_e "I could use a break, are you about finished here?"
                                    "Just suck on them without asking.":
                                            if E_Action and MultiAction:                            
                                                $ Situation = "auto"
                                                call E_FB_After from _call_E_FB_After_2
                                                call E_Suck_Breasts from _call_E_Suck_Breasts_1
                                            else:
                                                "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                ch_e "I could use a break, are you about finished here?"
                                            
                                    "Never Mind":
                                            pass
                            else:
                                ch_e "I could use a break, are you about finished here?" 
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_8
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FB_After from _call_E_FB_After_3
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_9   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_17
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FB_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_18
                                    $ Line = 0
                                    jump E_FB_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_39
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_10
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_19
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
                        call E_Cumming from _call_E_Cumming_21
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1161
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_20
        
    call EmmaFace("sexy") from _call_EmmaFace_1162 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1163
                    ch_e "Well you certainly hit the jackpot."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_68
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label E_Suck_Breasts:
    call Shift_Focus("Emma") from _call_Shift_Focus_179
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
            call EmmaFace("sexy") from _call_EmmaFace_1164       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you dive in, Emma seems a bit surprised, but just makes a little \"coo.\""              
            jump E_SB_Prep      
        else:               
            call EmmaFace("surprised") from _call_EmmaFace_1165
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1166
        ch_e "Mmmm, again? I suppose. . ."
        jump E_SB_Prep
    elif "suck breasts" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1167
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1) from _call_EmmaFace_1168
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1169
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Oh very well. . ."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1) from _call_EmmaFace_1170
        if "no suck breasts" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no suck breasts" in E_DailyActions:  
            ch_e "I told you I couldn't be seen like that." 
        elif "no suck breasts" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_SuckB:
            call EmmaFace("bemused") from _call_EmmaFace_1171
            ch_e "Let's work up to that, perhaps. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1172
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1173
                ch_e "No offense taken. I get it."              
                return
            "Maybe later?" if "no suck breasts" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1174  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1175     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Oh, if you insist. . ."                
                    jump E_SB_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1176 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Emma", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1177
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1178
                    "She shoves your head back out."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no suck breasts" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1179
        ch_e "Not worth it."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:   
        call EmmaFace("angry", 1) from _call_EmmaFace_1180      
        $ E_RecentActions.append("tabno")    
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_SuckB:
        call EmmaFace("sad") from _call_EmmaFace_1181
        ch_e "I am sorry about that, but perhaps later?"            
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1182 
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
        call Emma_Top_Off from _call_Emma_Top_Off_4
        if "angry" in E_RecentActions:
            return
    
    $ Tempmod = 0      
    call E_Breasts_Launch("suck breasts") from _call_E_Breasts_Launch_2
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
        call DrainWord("Emma","tabno") from _call_DrainWord_142
    call DrainWord("Emma","no suck breasts") from _call_DrainWord_143
    $ E_RecentActions.append("suck breasts")                      
    $ E_DailyActions.append("suck breasts") 
    
label E_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kissing":
            $ Trigger2 = 0 
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_180
        call E_Breasts_Launch("suck breasts") from _call_E_Breasts_Launch_3
        call EmmaLust from _call_EmmaLust_14     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1183   
                                    call E_Pos_Reset from _call_E_Pos_Reset_21
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
                                call E_Slap_Ass from _call_E_Slap_Ass_8
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
                                    call E_Undress from _call_E_Undress_11  
                                    
                        "Pull back to fondling.":  
                            if E_Action and MultiAction:
                                $ Situation = "pullback"
                                call E_SB_After from _call_E_SB_After_1
                                call E_Fondle_Breasts from _call_E_Fondle_Breasts_2
                            else:
                                "As you pull back, Emma pushes you back in close."
                                ch_e "I could use a break, are you about finished here?"
                    
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_10
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_SB_After from _call_E_SB_After_2
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_11   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_22
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_SB_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_23
                                    $ Line = 0
                                    jump E_SB_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_40
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_11
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_24
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
                        call E_Cumming from _call_E_Cumming_22
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1184
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_25
        
    call EmmaFace("sexy") from _call_EmmaFace_1185 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1186
                    ch_e "Did you get enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_69
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label E_Fondle_Thighs:
    call Shift_Focus("Emma") from _call_Shift_Focus_181
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
            call EmmaFace("sexy") from _call_EmmaFace_1187       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)            
            "As you caress her thigh, Emma glances at you, and smiles."             
            jump E_FT_Prep      
        else:               
            call EmmaFace("surprised") from _call_EmmaFace_1188
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Perhaps we keep it above the waist, [E_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised") from _call_EmmaFace_1189    
        $ E_Brows = "sad"
        if E_Lust > 60:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As you pull back, Emma looks a little sad."              
        jump E_FT_Prep  
    elif "fondle thighs" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1190
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FT_Prep
    elif "fondle thighs" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1191       
        ch_e "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1) from _call_EmmaFace_1192
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1193
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Ok [E_Petname], go ahead."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1) from _call_EmmaFace_1194
        if "no fondle thighs" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle thighs" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleT:
            call EmmaFace("bemused") from _call_EmmaFace_1195
            ch_e "Seems a bit forward, [E_Petname]."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1196
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1197
                ch_e "I appreciate your restraint."             
                return
            "Maybe later?" if "no fondle thighs" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1198  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1199     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
                    ch_e "Politeness can be rewarded. . ."             
                    jump E_FT_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1200 
                    ch_e "This wasn't a \"tone\" issue."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1201
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1202
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no fondle thighs" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1203
        ch_e "Don't push your luck."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 2)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -1)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1204    
        $ E_RecentActions.append("tabno")          
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_FondleT:
        call EmmaFace("sad") from _call_EmmaFace_1205
        ch_e "Hands."            
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1206 
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
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_8 
        if "angry" in E_RecentActions:
            return 
            
    $ Tempmod = 0    
    call E_Pussy_Launch("fondle thighs") from _call_E_Pussy_Launch_5
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
        call DrainWord("Emma","tabno") from _call_DrainWord_144
    call DrainWord("Emma","no fondle thighs") from _call_DrainWord_145
    $ E_RecentActions.append("fondle thighs")                      
    $ E_DailyActions.append("fondle thighs")  
    
label E_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_182 
        call E_Pussy_Launch("fondle thighs") from _call_E_Pussy_Launch_6
        call EmmaLust from _call_EmmaLust_15     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1207   
                                    call E_Pos_Reset from _call_E_Pos_Reset_26
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
                                call E_Slap_Ass from _call_E_Slap_Ass_9
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
                                    call E_Undress from _call_E_Undress_12  
                                    
                        "Can I do a little deeper?":
                                if E_Action and MultiAction:
                                    $ Situation = "shift"
                                    call E_FT_After from _call_E_FT_After_1
                                    call E_Fondle_Pussy from _call_E_Fondle_Pussy_2                
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        "Shift your hands a bit higher without asking":
                                if E_Action and MultiAction:
                                    $ Situation = "auto"
                                    call E_FT_After from _call_E_FT_After_2
                                    call E_Fondle_Pussy from _call_E_Fondle_Pussy_3    
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_e "I could use a break, are you about finished here?" 
                
                        "I also want to. . . [[Offhand]":
                                if E_Action and MultiAction:
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_12
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FT_After from _call_E_FT_After_3
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_13   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                                    
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_27
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FT_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_28
                                    $ Line = 0
                                    jump E_FT_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_41
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_12
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_29
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
                        call E_Cumming from _call_E_Cumming_23
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1208
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_30
        
    call EmmaFace("sexy") from _call_EmmaFace_1209 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1210
                    ch_e "Was that enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_70
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label E_Fondle_Pussy:
    call Shift_Focus("Emma") from _call_Shift_Focus_183
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
            call EmmaFace("sexy") from _call_EmmaFace_1211       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
            "As your hand creeps up her thigh, Emma seems a bit surprised, but then nods."            
            jump E_FP_Prep      
        else:               
            call EmmaFace("surprised") from _call_EmmaFace_1212
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
            ch_e "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised") from _call_EmmaFace_1213   
        $ E_Brows = "sad"        
        if E_Lust > 80:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As your hand pulls out, Emma gasps and looks upset."              
        jump E_FP_Prep     
    elif "fondle pussy" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1214
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FP_Prep
    elif "fondle pussy" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1215
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call EmmaFace("bemused", 1) from _call_EmmaFace_1216
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1217
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
        ch_e "Mmmm, I couldn't refuse. . ."   
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
        jump E_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1) from _call_EmmaFace_1218
        if "no fondle pussy" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle pussy" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleP:
            call EmmaFace("bemused") from _call_EmmaFace_1219
            ch_e "I don't think we're there yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1220
            ch_e "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1221
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1222  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1223     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    ch_e "I do enjoy hearing you beg. . ."                    
                    jump E_FP_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1224 
                    ch_e "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1225
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1226
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no fondle pussy" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1227
        ch_e "I don't think so, [E_Petname]."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)    
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1228    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno")
        ch_e "I have a reputation to maintain."                   
    elif E_FondleP:
        call EmmaFace("sad") from _call_EmmaFace_1229
        ch_e "Sorry, keep your hands out of there."           
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1230 
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
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_9   
        if "angry" in E_RecentActions:
            return 
    $ Tempmod = 0
    
    call E_Pussy_Launch("fondle pussy") from _call_E_Pussy_Launch_7
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
        call DrainWord("Emma","tabno") from _call_DrainWord_146
    call DrainWord("Emma","no fondle pussy") from _call_DrainWord_147
    $ E_RecentActions.append("fondle pussy")                      
    $ E_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label E_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_184 
        call E_Pussy_Launch("fondle pussy") from _call_E_Pussy_Launch_8
        call EmmaLust from _call_EmmaLust_16     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1231   
                                    call E_Pos_Reset from _call_E_Pos_Reset_31
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
                                call E_Insert_Pussy from _call_E_Insert_Pussy  
                       
                        "Pull back to fondling" if Speed == 2:
                                $ Speed = 1   
                                      
                        "Slap her ass":                     
                                call E_Slap_Ass from _call_E_Slap_Ass_10
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
                                    call E_Undress from _call_E_Undress_13  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:                                                                                         
                                            "I want to lick your pussy.":
                                                    $ Situation = "shift"
                                                    call E_FP_After from _call_E_FP_After_1
                                                    call E_Lick_Pussy from _call_E_Lick_Pussy                 
                                            "Just start licking":
                                                    $ Situation = "auto"
                                                    call E_FP_After from _call_E_FP_After_2
                                                    call E_Lick_Pussy from _call_E_Lick_Pussy_1         
                                            "Pull back to the thighs":
                                                    $ Situation = "pullback"
                                                    call E_FP_After from _call_E_FP_After_3
                                                    call E_Fondle_Thighs from _call_E_Fondle_Thighs
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
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_14
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FP_After from _call_E_FP_After_4
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_15   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_32
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FP_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_33
                                    $ Line = 0
                                    jump E_FP_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_42
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_13
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_34
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
                        call E_Cumming from _call_E_Cumming_24
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1232
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_35
        
    call EmmaFace("sexy") from _call_EmmaFace_1233 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1234
                    ch_e "Did you find what you were looking for?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_71
    return   

# end E_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label E_Insert_Pussy:
    call Shift_Focus("Emma") from _call_Shift_Focus_185
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Emma", 1100, TabM = 2):
            call EmmaFace("surprised") from _call_EmmaFace_1235       
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you slide a finger in, Emma seems a bit surprised, but seems into it."              
            jump E_IP_Prep
        else:   
            call EmmaFace("surprised",2) from _call_EmmaFace_1236
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Oooh!"
            "She slaps your hand back."
            call EmmaFace("perplexed",1) from _call_EmmaFace_1237
            ch_e "Careful what you put in there, you may not get it back."
            return            
    
    if ApprovalCheck("Emma", 1100, TabM = 2):                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1238
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1239
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
            ch_e "Mmmmmm. . ."                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2) 
        jump E_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call EmmaFace("bemused", 2) from _call_EmmaFace_1240
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
        call E_Undress("bottom") from _call_E_Undress_14
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
    call Shift_Focus("Emma") from _call_Shift_Focus_186
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
            call EmmaFace("surprised") from _call_EmmaFace_1241
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Emma jumps, but then softens."  
            call EmmaFace("sexy") from _call_EmmaFace_1242           
            jump E_LP_Prep
        else:   
            call EmmaFace("surprised") from _call_EmmaFace_1243
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "I like where your head is at, so to speak, but perhaps hold off on that." 
            call EmmaFace("perplexed",1) from _call_EmmaFace_1244
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1245
        ch_e "Mmmm, again? I suppose. . ."
        jump E_LP_Prep
    elif "lick pussy" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1246
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "What a queen deserves. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1247
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1248
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
        call EmmaFace("angry", 1) from _call_EmmaFace_1249
        if "no lick pussy" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no lick pussy" in E_DailyActions:  
            ch_e "You already got your answer!" 
        elif "no lick pussy" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_LickP:
            call EmmaFace("bemused") from _call_EmmaFace_1250
            ch_e "I'm not sure we're at that stage, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1251
            ch_e "I'm really not comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1252
                ch_e "I appreciate your restraint, [E_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1253  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1254           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "You present a compelling case. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_LP_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1255 
                    ch_e "I would, but still no, [E_Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Emma", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1256
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1257
                    "She shoves your head back."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no lick pussy" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1258
        ch_e "I really can't, [E_Petname]."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)     
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1259    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_LickP:
        call EmmaFace("sad") from _call_EmmaFace_1260 
        ch_e "Keep your head out of there."    
    else:
        call EmmaFace("surprised") from _call_EmmaFace_1261
        ch_e "I know, I'm as disappointed as you are."
        call EmmaFace from _call_EmmaFace_1262
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
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_10
        if "angry" in E_RecentActions:
            return  
            
    $ Tempmod = 0      
    call E_Pussy_Launch("lick pussy") from _call_E_Pussy_Launch_9
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
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_20
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_148
    call DrainWord("Emma","no lick pussy") from _call_DrainWord_149
    $ E_RecentActions.append("lick pussy")                      
    $ E_DailyActions.append("lick pussy") 
    
label E_LP_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_187 
        call E_Pussy_Launch("lick pussy") from _call_E_Pussy_Launch_10
        call EmmaLust from _call_EmmaLust_17     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1263   
                                    call E_Pos_Reset from _call_E_Pos_Reset_36
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
                                call E_Slap_Ass from _call_E_Slap_Ass_11
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
                                    call E_Undress from _call_E_Undress_15  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    if E_Action and MultiAction:
                                                        $ Situation = "pullback"
                                                        call E_LP_After from _call_E_LP_After_1
                                                        call E_Fondle_Pussy from _call_E_Fondle_Pussy_4
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
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_16
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_LP_After from _call_E_LP_After_2
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_17   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_37
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_LP_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_38
                                    $ Line = 0
                                    jump E_LP_After
        #End menu (if Line)
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto") from _call_E_Undress_16
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_43
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_14
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_39
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
                        call E_Cumming from _call_E_Cumming_25
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1264
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_40
        
    call EmmaFace("sexy") from _call_EmmaFace_1265 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1266
                    ch_e "I suppose that worked out for both of us. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_72
    return   


# end E_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label E_Fondle_Ass: 
    call Shift_Focus("Emma") from _call_Shift_Focus_188
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
            call EmmaFace("surprised", 1) from _call_EmmaFace_1267  
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
            "As your hand creeps down her backside, Emma jumps a bit, and then relaxes."              
            call EmmaFace("sexy") from _call_EmmaFace_1268  
            jump E_FA_Prep  
        else:          
            call EmmaFace("surprised") from _call_EmmaFace_1269
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Hands off, [E_Petname]."   
            call EmmaFace("bemused") from _call_EmmaFace_1270
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call EmmaFace("surprised") from _call_EmmaFace_1271   
        $ E_Brows = "sad"        
        if E_Lust > 80:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
        "As your finger slides out, Emma gasps and looks upset."              
        jump E_FA_Prep     
    elif "fondle ass" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1272
        ch_e "Mmmm, again? I suppose. . ."
        jump E_FA_Prep
    elif "fondle ass" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1273
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1274
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
            ch_e "If you insist. . ."   
        else:
            call EmmaFace("bemused, 1") from _call_EmmaFace_1275 
            ch_e "I can't exactly refuse. . ."   
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 3)
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
        jump E_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call EmmaFace("angry", 1) from _call_EmmaFace_1276
        if "no fondle ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no fondle ass" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no fondle ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_FondleA:
            call EmmaFace("bemused") from _call_EmmaFace_1277
            ch_e "Not yet, [E_Petname]. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1278
            ch_e "Let's not, ok [E_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1279
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1280  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1281     
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "I do enjoy hearing you beg. . ."                           
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                    jump E_FA_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1282 
                    ch_e "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Emma", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1283
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1284
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                        
    if "no fondle ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1285
        ch_e "Do you want to keep those fingers?"
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1286    
        $ E_RecentActions.append("tabno")   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_FondleA:
        call EmmaFace("sad") from _call_EmmaFace_1287
        ch_e "I'm sorry, keep your hands to yourself."        
    else:
        call EmmaFace("sexy") from _call_EmmaFace_1288 
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
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_11
        if "angry" in E_RecentActions:
            return    
    $ Tempmod = 0      
    call E_Pussy_Launch("fondle ass") from _call_E_Pussy_Launch_11
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
        call DrainWord("Emma","tabno") from _call_DrainWord_150
    call DrainWord("Emma","no fondle ass") from _call_DrainWord_151
    $ E_RecentActions.append("fondle ass")                      
    $ E_DailyActions.append("fondle ass") 
    
label E_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_189 
        call E_Pussy_Launch("fondle ass") from _call_E_Pussy_Launch_12
        call EmmaLust from _call_EmmaLust_18     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1289   
                                    call E_Pos_Reset from _call_E_Pos_Reset_41
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
                                call E_Slap_Ass from _call_E_Slap_Ass_12
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
                                    call E_Undress from _call_E_Undress_17  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call E_FA_After from _call_E_FA_After_1
                                                    call E_Insert_Ass from _call_E_Insert_Ass_2                 
                                            "Just stick a finger in without asking.":
                                                    $ Situation = "auto"
                                                    call E_FA_After from _call_E_FA_After_2
                                                    call E_Insert_Ass from _call_E_Insert_Ass_3
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call E_FA_After from _call_E_FA_After_3
                                                    call E_Lick_Ass from _call_E_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call E_FA_After from _call_E_FA_After_4
                                                    call E_Lick_Ass from _call_E_Lick_Ass_1    
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
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_18
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_FA_After from _call_E_FA_After_5
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_19   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_42
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_FA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_43
                                    $ Line = 0
                                    jump E_FA_After
        #End menu (if Line)
        
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_44
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_15
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_44
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
                        call E_Cumming from _call_E_Cumming_26
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1290
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_45
        
    call EmmaFace("sexy") from _call_EmmaFace_1291 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1292
                    ch_e "Did you enjoy that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_73
    return   


# end E_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label E_Insert_Ass:
    call Shift_Focus("Emma") from _call_Shift_Focus_190
    
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
            call EmmaFace("surprised") from _call_EmmaFace_1293
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
            "As you slide a finger in, Emma tightens around it in surprise, but seems into it."  
            call EmmaFace("sexy") from _call_EmmaFace_1294           
            jump E_IA_Prep
        else:   
            call EmmaFace("surprised") from _call_EmmaFace_1295
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "Whoa, back off, [E_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1296
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_e "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1297
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1298
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
        call EmmaFace("angry", 1) from _call_EmmaFace_1299
        if "no insert ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no insert ass" in E_DailyActions:  
            ch_e "I told you that wasn't appropriate!" 
        elif "no insert ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_InsertA:
            call EmmaFace("perplexed", 1) from _call_EmmaFace_1300
            ch_e "That's really not my usual style. . ."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1301
            ch_e "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1302
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1303  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1304           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "You're probably right. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_IA_Prep
                else:   
                    call EmmaFace("bemused") from _call_EmmaFace_1305 
                    ch_e "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Emma", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and E_Forced):                    
                    call EmmaFace("surprised", 1) from _call_EmmaFace_1306
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)                 
                    ch_e "Well hello there. . ."                     
                    call EmmaFace("sad") from _call_EmmaFace_1307
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ E_Forced = 1
                    jump E_IA_Prep
                else:                              
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -15)  
                    call EmmaFace("angry", 1) from _call_EmmaFace_1308
                    "She slaps your hand away."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no insert ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1309
        ch_e "I'm not going that far today."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10) if E_Inbt > 50 else Statupdate("Emma", "Lust", E_Lust, 50, 3) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)      
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1310    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_InsertA:
        call EmmaFace("sad") from _call_EmmaFace_1311 
        ch_e "I don't feel like it."    
    else:
        call EmmaFace("surprised") from _call_EmmaFace_1312
        ch_e "Not today, [E_Petname]."
        call EmmaFace from _call_EmmaFace_1313
    $ E_RecentActions.append("no insert ass")                      
    $ E_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label E_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not E_Forced and Situation != "auto":
        $ Tempmod = 0
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_12
        if "angry" in E_RecentActions:
            return    
            
    $ Tempmod = 0      
    call E_Pussy_Launch("insert ass") from _call_E_Pussy_Launch_13
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
        call DrainWord("Emma","tabno") from _call_DrainWord_152
    call DrainWord("Emma","no insert ass") from _call_DrainWord_153
    $ E_RecentActions.append("insert ass")                      
    $ E_DailyActions.append("insert ass") 
    
label E_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Emma") from _call_Shift_Focus_191 
        call E_Pussy_Launch("insert ass") from _call_E_Pussy_Launch_14
        call EmmaLust from _call_EmmaLust_19     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1314   
                                    call E_Pos_Reset from _call_E_Pos_Reset_46
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
                                call E_Slap_Ass from _call_E_Slap_Ass_13
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
                                    call E_Undress from _call_E_Undress_18  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    $ Situation = "pullback"
                                                    call E_IA_After from _call_E_IA_After_1
                                                    call E_Fondle_Ass from _call_E_Fondle_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call E_IA_After from _call_E_IA_After_2
                                                    call E_Lick_Ass from _call_E_Lick_Ass_2                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call E_IA_After from _call_E_IA_After_3
                                                    call E_Lick_Ass from _call_E_Lick_Ass_3    
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
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_20
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_IA_After from _call_E_IA_After_4
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_21   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_47
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_IA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_48
                                    $ Line = 0
                                    jump E_IA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto") from _call_E_Undress_19
            
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_45
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_16
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_49
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
                        call E_Cumming from _call_E_Cumming_27
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1315
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_50
        
    call EmmaFace("sexy") from _call_EmmaFace_1316 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1317
                    ch_e "Was it everything you dreamed?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_74
    return   


# end E_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label E_Lick_Ass: 
    call Shift_Focus("Emma") from _call_Shift_Focus_192
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
            call EmmaFace("surprised") from _call_EmmaFace_1318   
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3) 
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Emma startles briefly, but then begins to melt."  
            call EmmaFace("sexy") from _call_EmmaFace_1319  
            jump E_LA_Prep
        else:   
            call EmmaFace("surprised") from _call_EmmaFace_1320
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
            ch_e "[E_Petname]! Not now. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in E_RecentActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1321
        ch_e "Mmmm, again? I suppose. . ."
        jump E_LA_Prep
    elif "lick ass" in E_DailyActions:
        call EmmaFace("sexy", 1) from _call_EmmaFace_1322
        ch_e "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if E_Forced:
            call EmmaFace("sad") from _call_EmmaFace_1323
            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -3, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 20, -2, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
            ch_e "If you must. . ."    
        else:
            call EmmaFace("sexy", 1) from _call_EmmaFace_1324
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
        call EmmaFace("angry", 1) from _call_EmmaFace_1325
        if "no lick ass" in E_RecentActions:  
            ch_e "Your persistance is doing you no favors, [E_Petname]."
        elif Taboo and "tabno" in E_DailyActions and "no lick ass" in E_DailyActions:  
            ch_e "I told you not to touch me like that in public!" 
        elif "no lick ass" in E_DailyActions:       
            ch_e "I believe you know my answer on this matter."
        elif Taboo and "tabno" in E_DailyActions:  
            ch_e "As I said, not here, [E_Petname]."  
        elif not E_LickA:                    #First time dialog
            call EmmaFace("bemused", 1) from _call_EmmaFace_1326
            if E_Love >= E_Obed and E_Love >= E_Inbt:            
                ch_e "Oh, are we there now?"
            elif E_Obed >= E_Inbt:            
                ch_e "Is that what gets you off?"
            else:
                $ E_Eyes = "sexy"
                ch_e "Hm, I didn't know that's what you were into."
        else:
            call EmmaFace("bemused") from _call_EmmaFace_1327
            ch_e "Not now, [E_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in E_DailyActions:
                call EmmaFace("bemused") from _call_EmmaFace_1328
                ch_e "I appreciate your restraint, [E_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in E_DailyActions:
                call EmmaFace("sexy") from _call_EmmaFace_1329  
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
                    call EmmaFace("sexy") from _call_EmmaFace_1330           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                    ch_e "Ok, you're probably right. . ."      
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                    jump E_LA_Prep
                else:   
                    call EmmaFace("sexy") from _call_EmmaFace_1331 
                    ch_e "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Emma", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and E_Forced):
                    call EmmaFace("sad") from _call_EmmaFace_1332
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
                    call EmmaFace("angry", 1) from _call_EmmaFace_1333
                    "She shoves your head back."   
                    $ E_RecentActions.append("angry")
                    $ E_DailyActions.append("angry")   
                    
    if "no lick ass" in E_DailyActions:
        ch_e "I don't appreciate having to repeat myself, [E_Petname]."   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif E_Forced:
        call EmmaFace("angry", 1) from _call_EmmaFace_1334
        ch_e "I don't think so."
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10) if E_Inbt > 50 else Statupdate("Emma", "Lust", E_Lust, 50, 3) 
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)   
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")   
    elif Taboo:
        call EmmaFace("angry", 1) from _call_EmmaFace_1335    
        $ E_RecentActions.append("tabno")                   
        $ E_DailyActions.append("tabno") 
        ch_e "I have a reputation to maintain."                   
    elif E_LickA:
        call EmmaFace("sad") from _call_EmmaFace_1336 
        ch_e "Sorry, no more of that."    
    else:
        call EmmaFace("surprised") from _call_EmmaFace_1337
        ch_e "I'm sorry, not now."
        call EmmaFace from _call_EmmaFace_1338
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
        call Emma_Bottoms_Off from _call_Emma_Bottoms_Off_13
        if "angry" in E_RecentActions:
            return    
    $ Tempmod = 0  
    call E_Pussy_Launch("lick ass") from _call_E_Pussy_Launch_15
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
        call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_21
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Emma","tabno") from _call_DrainWord_154
    call DrainWord("Emma","no lick ass") from _call_DrainWord_155
    
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
        call Shift_Focus("Emma") from _call_Shift_Focus_193 
        call E_Pussy_Launch("lick ass") from _call_E_Pussy_Launch_16
        call EmmaLust from _call_EmmaLust_20     
        
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
                                    call EmmaFace("angry", 1) from _call_EmmaFace_1339   
                                    call E_Pos_Reset from _call_E_Pos_Reset_51
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
                                call E_Slap_Ass from _call_E_Slap_Ass_14
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
                                    call E_Undress from _call_E_Undress_20  
                        
                        "Shift actions":
                                if E_Action and MultiAction:
                                        menu:   
                                            "Switch to fondling.":
                                                    $ Situation = "pullback"
                                                    call E_LA_After from _call_E_LA_After_1
                                                    call E_Fondle_Ass from _call_E_Fondle_Ass_1
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call E_LA_After from _call_E_LA_After_2
                                                    call E_Insert_Ass from _call_E_Insert_Ass_4                 
                                            "Just stick a finger in [[without asking].":
                                                    $ Situation = "auto"
                                                    call E_LA_After from _call_E_LA_After_3
                                                    call E_Insert_Ass from _call_E_Insert_Ass_5                        
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
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_22
                                    if Trigger2:
                                         $ E_Action -= 1
                                else:
                                    ch_e "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call E_LA_After from _call_E_LA_After_4
                                    call Emma_Offhand_Set from _call_Emma_Offhand_Set_23   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_52
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_LA_After
                        "Let's stop for now." if not MultiAction: 
                                    call E_Pos_Reset from _call_E_Pos_Reset_53
                                    $ Line = 0
                                    jump E_LA_After
        #End menu (if Line)
        
        if E_Panties or E_Legs == "pants" or HoseNum("Emma") >= 5: #This checks if Emma wants to strip down.
                call E_Undress("auto") from _call_E_Undress_21
            
        call Sex_Dialog("Emma",Partner) from _call_Sex_Dialog_46
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or E_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PE_Cumming from _call_PE_Cumming_17
                            if "angry" in E_RecentActions:  
                                call E_Pos_Reset from _call_E_Pos_Reset_54
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
                        call E_Cumming from _call_E_Cumming_28
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
    call EmmaFace("bemused", 0) from _call_EmmaFace_1340
    $ Line = 0
    ch_e "We need to stop for a moment, let me catch my breath."
    
    
label E_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call E_Pos_Reset from _call_E_Pos_Reset_55
        
    call EmmaFace("sexy") from _call_EmmaFace_1341 
    
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
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_1342
                    ch_e "Was it all you dreamed of?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_e "Oh? What did you have in mind?"
    call Checkout from _call_Checkout_75
    return   

# end E_Lick Ass /////////////////////////////////////////////////////////////////////////////

