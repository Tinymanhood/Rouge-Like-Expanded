# R_Massage /////////////////////////////////////////////////////////////////////////////
label R_Massage:
    call Shift_Focus("Rogue") from _call_Shift_Focus_218
    $ Tempmod = 0    
    if "angry" in R_RecentActions:
        return    
        
    $ Approval = ApprovalCheck("Rogue", 500, TabM = 1) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call RogueFace("bemused", 1) from _call_RogueFace_861
        if R_Forced:
                call RogueFace("sad") from _call_RogueFace_862
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        ch_r "Ok [R_Petname], sure."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
        jump R_Massage_Prep
        
    else:
        call RogueFace("angry", 1) from _call_RogueFace_863
        if "no massage" in R_RecentActions:  
            ch_r "Heh, I {i}just{/i} told you \"no,\" [R_Petname]."
        elif "no massage" in R_DailyActions:       
            ch_r "I told you \"no,\" earlier [R_Petname]."
        else:
            call RogueFace("bemused") from _call_RogueFace_864
            ch_r "I don't know, not right now."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_865
                ch_r "Ok, no problem, [R_Petname]."              
                return
            "Maybe later?" if "no massage" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_866  
                ch_r "Sure, maybe."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 20, 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)  
                $ R_RecentActions.append("no massage")                      
                $ R_DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_867     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                    ch_r "Well, if you're that desperate. . ."                
                    jump R_Massage_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_868 
                    ch_r "Heh, no thanks, [R_Petname]." 
    
    if "no massage" in R_DailyActions:
        ch_r "You're starting to skeeve me out, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_869
        ch_r "I don't even want you touching me."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_870    
        ch_r "I don't want you touching me in public."                   
    else:
        call RogueFace("sexy") from _call_RogueFace_871 
        $ R_Mouth = "sad"
        ch_r "Seriously, no thanks, [R_Petname]."    
    $ R_RecentActions.append("no massage")                      
    $ R_DailyActions.append("no massage") 
    $ Tempmod = 0    
    return
 
label R_Massage_Prep:
    call Rogue_Top_Off("massage") from _call_Rogue_Top_Off_6
    if "angry" in R_RecentActions:
        return    
        
label R_Massage_Cycle:    
    $ R_RecentActions.append("massage")                      
    $ R_DailyActions.append("massage") 
    
    call Rogue_Doggy_Launch("massage") from _call_Rogue_Doggy_Launch_4
    
    "You massage her back and shoulders."
    if not R_Over:
        $ D20 = renpy.random.randint(10, 20)
        $ Round -= D20 if Round > D20 else (Round-1)
        $ R_Addict -= D20 if R_Addict > D20 else R_Addict
        
    call Rogue_Doggy_Reset from _call_Rogue_Doggy_Reset_8
    
    ch_r "That was very relaxing, [R_Petname]"
    if "massage" not in R_RecentActions:        
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
    return

# end R_Massage /////////////////////////////////////////////////////////////////////////////

# R_Fondle /////////////////////////////////////////////////////////////////////////////
label R_Fondle:
    
    $ R_Mouth = "smile"
    if not R_Action:
        ch_r "I'm a bit worn out right now, [R_Petname], maybe later."
        return
    menu:
        ch_r "Well where exactly were you interested in touching, [R_Petname]?"
        "Your breasts?" if R_Action:
            jump R_Fondle_Breasts
        "Your thighs?" if R_Action:
            jump R_Fondle_Thighs
        "Your pussy?" if R_Action:
            jump R_Fondle_Pussy
        "Your Ass?" if R_Action:
            jump R_Fondle_Ass
        "Never mind.":
            return
    return


# R_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label R_Fondle_Breasts:
    call Shift_Focus("Rogue") from _call_Shift_Focus_219
    
    # Will she let you fondle? Modifiers
    if R_FondleB: #You've done it before
        $ Tempmod += 15
    if R_Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 20
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle breasts" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in R_RecentActions else 0        
        
    $ Approval = ApprovalCheck("Rogue", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call RogueFace("sexy") from _call_RogueFace_872       
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)            
            "As you cup her breast, Rogue gently nods."            
            jump RFB_Prep        
        else:   
            call RogueFace("surprised") from _call_RogueFace_873
            $ R_Brows = "confused"
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            ch_r "Ah, ah, Just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call RogueFace("sexy", 1) from _call_RogueFace_874
        if R_Forced: 
            call RogueFace("sad") from _call_RogueFace_875
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)           
        elif not Taboo and "tabno" in R_DailyActions:        
            ch_r "I guess this is private enough. . ."   
            
    if "fondle breasts" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_876
        ch_r "Mmm, again? Ok."
        jump RFB_Prep
    elif "fondle breasts" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_877
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
            
    if Approval >= 2:             
        call RogueFace("bemused", 1) from _call_RogueFace_878
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_879
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        ch_r "Ok [R_Petname], come and get'em."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
        jump RFB_Prep
        
    else:
        call RogueFace("angry", 1) from _call_RogueFace_880
        if "no fondle breasts" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle breasts" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle breasts" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleB:
            call RogueFace("bemused") from _call_RogueFace_881
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_882
            ch_r "I'd really rather not."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_883
                ch_r "Ok, no problem, [R_Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_884  
                "She re-adjusts her cleavage."
                ch_r "I'll give it some thought, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle breasts")                      
                $ R_DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_885     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."                
                    jump RFB_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_886 
                    ch_r "I'm afraid not this time, sorry [R_Petname]." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_887
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)                 
                    ch_r "Fine, if that's what you want."                         
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)   
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFB_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)  
                    call RogueFace("angry", 1) from _call_RogueFace_888
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
    
    if "no fondle breasts" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_889
        ch_r "I don't want you touching me."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_890    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleB:
        call RogueFace("sad") from _call_RogueFace_891
        ch_r "Sorry, [R_Petname], you aren't touching these again."        
    else:
        call RogueFace("sexy") from _call_RogueFace_892 
        $ R_Mouth = "sad"
        ch_r "Not hap'nin."    
    $ R_RecentActions.append("no fondle breasts")                      
    $ R_DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label RFB_Prep: #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Top_Off from _call_Rogue_Top_Off_7
        if "angry" in R_RecentActions:
            return
        
    $ Tempmod = 0  
    call R_Breasts_Launch("fondle breasts") from _call_R_Breasts_Launch_1
    if not R_FondleB:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 25)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
            
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0   
    $ Cnt = 0    
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_179
    call DrainWord("Rogue","no fondle breasts") from _call_DrainWord_180
    $ R_RecentActions.append("fondle breasts")                      
    $ R_DailyActions.append("fondle breasts") 
    
label RFB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_220
        call R_Breasts_Launch("fondle breasts") from _call_R_Breasts_Launch_2
        call RogueLust from _call_RogueLust_3     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_FondleB):
                    $ R_Brows = "confused"
                    ch_r "You're just going at them, huh?" 
        elif R_Lust >= 85:
                    pass  
        elif Cnt == (15 + R_FondleB) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused" 
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_893   
                                    call R_Pos_Reset from _call_R_Pos_Reset_3
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RFB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass

                        "Slap her ass":                     
                                call R_Slap_Ass from _call_R_Slap_Ass_2
                                jump RFB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress           
                                        
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                            if R_Action and MultiAction:                        
                                                $ Situation = "shift"
                                                call RFB_After from _call_RFB_After_1
                                                call R_Suck_Breasts from _call_R_Suck_Breasts
                                            else:
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"
                                    "Just suck on them without asking.":
                                            if R_Action and MultiAction:                            
                                                $ Situation = "auto"
                                                call RFB_After from _call_RFB_After_2
                                                call R_Suck_Breasts from _call_R_Suck_Breasts_1
                                            else:
                                                "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"
                                            
                                    "Never Mind":
                                            pass
                            else:
                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RFB_After from _call_RFB_After_3
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_1   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_4
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFB_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_5
                                    $ Line = 0
                                    jump RFB_After
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_56
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_6
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFB_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_11
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RFB_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RFB_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_894
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_7
        
    call RogueFace("sexy") from _call_RogueFace_895 
    
    $ R_FondleB += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
     
    if R_FondleB == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was . . . real pleasant, [R_Petname]."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_896
                    ch_r "Did you get your jollies?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_85
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label R_Suck_Breasts:
    call Shift_Focus("Rogue") from _call_Shift_Focus_221
                                                                                        # Will she let you suck? Modifiers
    if R_SuckB: #You've done it before
        $ Tempmod += 15
    if not R_Chest and not R_Over:
        $ Tempmod += 15
    if R_Lust > 75: #She's really horny
        $ Tempmod += 20
    if R_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no suck breasts" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in R_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Rogue", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy") from _call_RogueFace_897       
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)            
            "As you dive in, Rogue seems a bit surprised, but just makes a little \"coo.\""              
            jump RSB_Prep      
        else:               
            call RogueFace("surprised") from _call_RogueFace_898
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            ch_r "Hey, just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_899
        ch_r "Mmm, again? Ok."
        jump RSB_Prep
    elif "suck breasts" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_900
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1) from _call_RogueFace_901
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_902
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        ch_r "Ok [R_Petname], come and get'em."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
        jump RSB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_903
        if "no suck breasts" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no suck breasts" in R_DailyActions:  
            ch_r "I told you we can't do that in public!" 
        elif "no suck breasts" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_SuckB:
            call RogueFace("bemused") from _call_RogueFace_904
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_905
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_906
                ch_r "Yeah, fine, [R_Petname]."              
                return
            "Maybe later?" if "no suck breasts" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_907  
                ch_r "I'll give it some thought, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no suck breasts")                      
                $ R_DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_908     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                    ch_r "You better work your mouth that hard on these."                
                    jump RSB_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_909 
                    ch_r "I'm afraid not this time, sorry [R_Petname]."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Rogue", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_910
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)                 
                    ch_r "Hmmph, well I guess you can go to town. . ."                         
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RSB_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)  
                    call RogueFace("angry", 1) from _call_RogueFace_911
                    "She shoves your head back out."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no suck breasts" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_912
        ch_r "I don't want your lips on me."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:   
        call RogueFace("angry", 1) from _call_RogueFace_913      
        $ R_RecentActions.append("tabno")    
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_SuckB:
        call RogueFace("sad") from _call_RogueFace_914
        ch_r "Sorry, [R_Petname], you aren't getting these in your mouth."            
    else:
        call RogueFace("sexy") from _call_RogueFace_915 
        $ R_Mouth = "sad"
        ch_r "Not hap'nin, [R_Petname]."
    $ R_RecentActions.append("no suck breasts")                      
    $ R_DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
                      
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label RSB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0   
        call Rogue_Top_Off from _call_Rogue_Top_Off_8
        if "angry" in R_RecentActions:
            return
    
    $ Tempmod = 0      
    call R_Breasts_Launch("suck breasts") from _call_R_Breasts_Launch_3
    if not R_SuckB:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -25)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 25)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 17) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
    
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0     
    $ Cnt = 0   
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_181
    call DrainWord("Rogue","no suck breasts") from _call_DrainWord_182
    $ R_RecentActions.append("suck breasts")                      
    $ R_DailyActions.append("suck breasts") 
    
label RSB_Cycle: #Repeating strokes   
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_222
        call R_Breasts_Launch("suck breasts") from _call_R_Breasts_Launch_4
        call RogueLust from _call_RogueLust_4     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_SuckB):
                    $ R_Brows = "confused"
                    ch_r "You're just going at them, huh?"   
        elif R_Lust >= 85:
                    pass
        elif Cnt == (15 + R_SuckB) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RSB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RSB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_916   
                                    call R_Pos_Reset from _call_R_Pos_Reset_8
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RSB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                       
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_3
                                    jump RSB_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_1     
                                
                        "Pull back to fondling.":  
                            if R_Action and MultiAction:
                                $ Situation = "pullback"
                                call RSB_After from _call_RSB_After_1
                                call R_Fondle_Breasts from _call_R_Fondle_Breasts_3
                            else:
                                "As you pull back, Rogue pushes you back in close."
                                ch_r "I'm actually getting a little tired, so maybe we could wrap this up"
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_2
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RSB_After from _call_RSB_After_2
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_3   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_9
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RSB_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_10
                                    $ Line = 0
                                    jump RSB_After
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_57
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_1
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_11
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RSB_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_12
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RSB_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RSB_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_917
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RSB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_12
        
    call RogueFace("sexy") from _call_RogueFace_918 
    
    $ R_SuckB += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
     
    if R_SuckB == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I . . . really liked that, [R_Petname]."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_919
                    ch_r "Did you like the taste?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_86
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label R_Fondle_Thighs:
    call Shift_Focus("Rogue") from _call_Shift_Focus_223
                                                                                        # Will she let you fondle her thighs? Modifiers
    if R_FondleT: #You've done it before
        $ Tempmod += 10
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if R_Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in R_Traits:
        $ Tempmod += Taboo   
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount      
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle thighs" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy") from _call_RogueFace_920       
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)            
            "As you caress her thigh, Rogue glances at you, and smiles."             
            jump RFT_Prep      
        else:               
            call RogueFace("surprised") from _call_RogueFace_921
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            ch_r "Hands off the merchandise, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised") from _call_RogueFace_922    
        $ R_Brows = "sad"
        if R_Lust > 60:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
        "As you pull back, Rogue looks a little sad."              
        jump RFT_Prep  
    elif "fondle thighs" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_923
        ch_r "Mmm, again? Ok."
        jump RFT_Prep
    elif "fondle thighs" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_924
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "You do have a smooth touch. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1) from _call_RogueFace_925
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_926
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        ch_r "Ok [R_Petname], go ahead."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
        jump RFT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_927
        if "no fondle thighs" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle thighs" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleT:
            call RogueFace("bemused") from _call_RogueFace_928
            ch_r "I just don't think I'm ready yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_929
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_930
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle thighs" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_931  
                ch_r "Heh, maybe, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)    
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle thighs")                      
                $ R_DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_932     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."             
                    jump RFT_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_933 
                    ch_r "I'm afraid not this time, sorry [R_Petname]."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_934
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)                 
                    ch_r "Hmmph."                         
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFT_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -8)  
                    call RogueFace("angry", 1) from _call_RogueFace_935
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no fondle thighs" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_936
        ch_r "Not even that much."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 50, 2)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_937    
        $ R_RecentActions.append("tabno")          
        $ R_DailyActions.append("tabno") 
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleT:
        call RogueFace("sad") from _call_RogueFace_938
        ch_r "Fresh!"            
    else:
        call RogueFace("sexy") from _call_RogueFace_939 
        $ R_Mouth = "sad"
        ch_r "No luck, [R_Petname]."
    $ R_RecentActions.append("no fondle thighs")                      
    $ R_DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label RFT_Prep:                                                                 #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_6 
        if "angry" in R_RecentActions:
            return 
            
    $ Tempmod = 0    
    call R_Pussy_Launch("fondle thighs") from _call_R_Pussy_Launch_1
    if not R_FondleT:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 15)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
            
    if Taboo:               
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (int(Taboo/5)))                               
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_183
    call DrainWord("Rogue","no fondle thighs") from _call_DrainWord_184
    $ R_RecentActions.append("fondle thighs")                      
    $ R_DailyActions.append("fondle thighs")  
    
label RFT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_224 
        call R_Pussy_Launch("fondle thighs") from _call_R_Pussy_Launch_2
        call RogueLust from _call_RogueLust_5     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_FondleT):
                    $ R_Brows = "confused"
                    ch_r "You like how those feel, huh?"   
        elif Cnt == (15 + R_FondleT) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFT_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_940   
                                    call R_Pos_Reset from _call_R_Pos_Reset_13
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RFT_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                   
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_4
                                    jump RFT_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_2   
                                
                        "Can I do a little deeper?":
                                if R_Action and MultiAction:
                                    $ Situation = "shift"
                                    call RFT_After from _call_RFT_After_1
                                    call R_Fondle_Pussy from _call_R_Fondle_Pussy_3                
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        "Shift your hands a bit higher without asking":
                                if R_Action and MultiAction:
                                    $ Situation = "auto"
                                    call RFT_After from _call_RFT_After_2
                                    call R_Fondle_Pussy from _call_R_Fondle_Pussy_4    
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_4
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RFT_After from _call_RFT_After_3
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_5   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                                                            
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_14
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFT_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_15
                                    $ Line = 0
                                    jump RFT_After
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_58
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:    
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_2
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_16
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFT_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_13
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RFT_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RFT_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_941
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_17
        
    call RogueFace("sexy") from _call_RogueFace_942 
    
    $ R_FondleT += 1  
    $ R_Action -=1
    if PantsNum("Rogue") != 10 or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 1
     
    if R_FondleT == 1:            
            $ R_SEXP += 3         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was. . . nice."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_943
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_87
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label R_Fondle_Pussy:
    call Shift_Focus("Rogue") from _call_Shift_Focus_225
                                                                                        # Will she let you fondle? Modifiers
    if R_FondleP: #You've done it before
        $ Tempmod += 20
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if R_Lust > 75: #She's really horny
        $ Tempmod += 15
    if R_Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle pussy" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call RogueFace("sexy") from _call_RogueFace_944       
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2)
            "As your hand creeps up her thigh, Rogue seems a bit surprised, but then nods."            
            jump RFP_Prep      
        else:               
            call RogueFace("surprised") from _call_RogueFace_945
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
            ch_r "Hey, just keep doing what you were doing, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised") from _call_RogueFace_946   
        $ R_Brows = "sad"        
        if R_Lust > 80:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -4)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
        "As your hand pulls out, Rogue gasps and looks upset."              
        jump RFP_Prep     
    elif "fondle pussy" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_947
        ch_r "Mmm, again? Ok."
        jump RFP_Prep
    elif "fondle pussy" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_948
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Take it a bit gently, I'm still quivering from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call RogueFace("bemused", 1) from _call_RogueFace_949
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_950
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
        ch_r "Sure, get in there."   
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
        jump RFP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_951
        if "no fondle pussy" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle pussy" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleP:
            call RogueFace("bemused") from _call_RogueFace_952
            ch_r "Um, not down there, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_953
            ch_r "I'd really rather not."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_954
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_955  
                ch_r "I'll give it some thought, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle pussy")                      
                $ R_DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_956     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                    ch_r "Well, if you're gonna beg. . ."                    
                    jump RFP_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_957 
                    ch_r "Tsk, not this time, [R_Petname]." 
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_958
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                    ch_r "Well, at least make it worth it."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFP_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)  
                    call RogueFace("angry", 1) from _call_RogueFace_959
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no fondle pussy" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_960
        ch_r "Stay out of my pants, [R_Petname]."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 70, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_961    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno")
        ch_r "I really don't think this is the right place for that!"                   
    elif R_FondleP:
        call RogueFace("sad") from _call_RogueFace_962
        ch_r "Sorry, keep your hands out of there."           
    else:
        call RogueFace("sexy") from _call_RogueFace_963 
        $ R_Mouth = "sad"
        ch_r "No luck [R_Petname]."
    $ R_RecentActions.append("no fondle pussy")                      
    $ R_DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
    
ch_r "Sorry, I don't even know how I got here. . ."
return
                
label RFP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_7   
        if "angry" in R_RecentActions:
            return 
    $ Tempmod = 0
    
    call R_Pussy_Launch("fondle pussy") from _call_R_Pussy_Launch_3
    if not R_FondleP:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -50)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 35)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 25) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0   
    $ Cnt = 0 
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_185
    call DrainWord("Rogue","no fondle pussy") from _call_DrainWord_186
    $ R_RecentActions.append("fondle pussy")                      
    $ R_DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label RFP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_226 
        call R_Pussy_Launch("fondle pussy") from _call_R_Pussy_Launch_4
        call RogueLust from _call_RogueLust_6     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_FondleP):
                    $ R_Brows = "confused"
                    ch_r "You like how that feels, huh?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_FondleP) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "I know you're having fun, but maybe we could try something else [R_Petname]."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_964   
                                    call R_Pos_Reset from _call_R_Pos_Reset_18
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RFP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                        
                        "I want to stick a finger in. . ." if Speed != 2:
                            if R_InsertP: 
                                $ Speed = 2
                            else:
                                menu:                                
                                    "Ask her first":
                                        $ Situation = "shift"
                                    "Don't ask first [[just stick it in]":                                    
                                        $ Situation = "auto"
                                call R_Insert_Pussy from _call_R_Insert_Pussy  
                       
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_5
                                    jump RFP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_3   
                        
                        "Shift actions":
                                if R_Action and MultiAction:
                                        menu:                                                                                         
                                            "I want to lick your pussy.":
                                                    $ Situation = "shift"
                                                    call RFP_After from _call_RFP_After_1
                                                    call R_Lick_Pussy from _call_R_Lick_Pussy                 
                                            "Just start licking":
                                                    $ Situation = "auto"
                                                    call RFP_After from _call_RFP_After_2
                                                    call R_Lick_Pussy from _call_R_Lick_Pussy_1         
                                            "Pull back to the thighs":
                                                    $ Situation = "pullback"
                                                    call RFP_After from _call_RFP_After_3
                                                    call R_Fondle_Thighs from _call_R_Fondle_Thighs_3
                                            "I want to stick a dildo in.":
                                                    call R_Dildo_Check from _call_R_Dildo_Check
                                                    if _return:
                                                        $ Situation = "shift"
                                                        call RFP_After from _call_RFP_After_4
                                                        call R_Dildo_Pussy from _call_R_Dildo_Pussy  
                                                    else:
                                                        jump RFP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_6
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RFP_After from _call_RFP_After_5
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_7   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_19
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFP_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_20
                                    $ Line = 0
                                    jump RFP_After
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_59
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_3
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_21
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFP_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_14
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RFP_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RFP_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_965
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_22
        
    call RogueFace("sexy") from _call_RogueFace_966 
    
    $ R_FondleP += 1  
    $ R_Action -=1
    if PantsNum("Rogue") != 10 or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
     
    if R_FondleP == 1:            
            $ R_SEXP += 7         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Certainly different with someone else at the wheel."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_967
                    ch_r "Was that enough for you?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_88
    return   

# end R_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label R_Insert_Pussy:
    call Shift_Focus("Rogue") from _call_Shift_Focus_227
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Rogue", 1100, TabM = 2):
            call RogueFace("surprised") from _call_RogueFace_968       
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
            "As you slide a finger in, Rogue seems a bit surprised, but seems into it."              
            jump RIP_Prep
        else:   
            call RogueFace("surprised") from _call_RogueFace_969
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
            ch_r "Keep it outside, [R_Petname]."   
            return            
    
    if ApprovalCheck("Rogue", 1100, TabM = 2):                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_970
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1) from _call_RogueFace_971
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
            ch_r "God yes."                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump RIP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call RogueFace("bemused", 2) from _call_RogueFace_972
        ch_r "Um, no thanks, [R_Petname]."
        $ R_Blush = 1
    return
    
                
label RIP_Prep: #Animation set-up     
    if not R_InsertP:
        $ R_InsertP = 1
        $ R_SEXP += 10          
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -60)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 55)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 35) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 25)
        
    if not R_Forced and Situation != "auto":        
        call R_Undress("bottom") from _call_R_Undress_4
        if "angry" in R_RecentActions:
            return    
            
#    call R_Pussy_Launch("insert pussy")
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
        
    $ Line = 0    
    $ Cnt = 0    
    $ Speed = 2
    return

# end R_Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label R_Lick_Pussy: 
    call Shift_Focus("Rogue") from _call_Shift_Focus_228
                                                                                  # Will she let you fondle? Modifiers     
    if R_LickP: #You've done it before
        $ Tempmod += 15
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if R_Lust > 95:
        $ Tempmod += 20  
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if R_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount     
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick pussy" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised") from _call_RogueFace_973
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Rogue startles, but then sinks into the sensation."  
            call RogueFace("sexy") from _call_RogueFace_974           
            jump RLP_Prep
        else:   
            call RogueFace("surprised") from _call_RogueFace_975
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
            ch_r "Oh! No, no thank you, [R_Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_976
        ch_r "Mmm, again? Ok."
        jump RLP_Prep
    elif "lick pussy" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_977
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "You sure know how to keep a girl satisfied. . .",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_978
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1) from _call_RogueFace_979
            $ R_Eyes = "closed"            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)            
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)
            ch_r "Oooooooh. . ."                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump RLP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_980
        if "no lick pussy" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no lick pussy" in R_DailyActions:  
            ch_r "You already got your answer!" 
        elif "no lick pussy" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_LickP:
            call RogueFace("bemused") from _call_RogueFace_981
            ch_r "That's pretty intimate, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_982
            ch_r "Oh, um, no, I'm not really comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_983
                ch_r "Yeah, ok, [R_Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_984  
                ch_r "I'll be thinking about it, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no lick pussy")                      
                $ R_DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_985           
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
                    jump RLP_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_986 
                    ch_r "Tsk, not this time, [R_Petname], that just seems. . . intimate."     
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Rogue", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_987
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RLP_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)  
                    call RogueFace("angry", 1) from _call_RogueFace_988
                    "She shoves your head back."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no lick pussy" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_989
        ch_r "Not even, [R_Petname]."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)     
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_990    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "This just really isn't the time or place, [R_Petname]!"                   
    elif R_LickP:
        call RogueFace("sad") from _call_RogueFace_991 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        call RogueFace("surprised") from _call_RogueFace_992
        ch_r "Ew!"
        call RogueFace from _call_RogueFace_993
    $ R_RecentActions.append("no lick pussy")                      
    $ R_DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label RLP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        if PantsNum("Rogue") == 10:
            $ Tempmod = 15
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_8
        if "angry" in R_RecentActions:
            return  
            
    $ Tempmod = 0      
    call R_Pussy_Launch("lick pussy") from _call_R_Pussy_Launch_5
    if not R_LickP:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 35)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 75) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 35)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 15)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 35)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if R_Legs == "skirt":
        $ R_Upskirt = 1  
        $ R_SeenPanties = 1
    if not R_Panties:
        call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_22
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_187
    call DrainWord("Rogue","no lick pussy") from _call_DrainWord_188
    $ R_RecentActions.append("lick pussy")                      
    $ R_DailyActions.append("lick pussy") 
    
label RLP_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_229 
        call R_Pussy_Launch("lick pussy") from _call_R_Pussy_Launch_6
        call RogueLust from _call_RogueLust_7     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_LickP):
                    $ R_Brows = "confused"
                    ch_r "You like it down there?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_LickP) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RLP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RLP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_994   
                                    call R_Pos_Reset from _call_R_Pos_Reset_23
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RLP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_6
                                    jump RLP_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_5   
                        
                        "Shift actions":
                                if R_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    if R_Action and MultiAction:
                                                        $ Situation = "pullback"
                                                        call RLP_After from _call_RLP_After_1
                                                        call R_Fondle_Pussy from _call_R_Fondle_Pussy_5
                                                    else:
                                                        ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                                            "I want to stick a dildo in.":
                                                    call R_Dildo_Check from _call_R_Dildo_Check_1
                                                    if _return:
                                                        $ Situation = "shift"
                                                        call RLP_After from _call_RLP_After_2
                                                        call R_Dildo_Pussy from _call_R_Dildo_Pussy_1  
                                                    else:
                                                        jump RLP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_8
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RLP_After from _call_RLP_After_3
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_9   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_24
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RLP_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_25
                                    $ Line = 0
                                    jump RLP_After
        #End menu (if Line)
        
        if R_Panties or PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: #This checks if Rogue wants to strip down.
                call R_Undress("auto") from _call_R_Undress_6
            
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_60
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:  
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_4
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_26
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RLP_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_15
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RLP_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RLP_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_995
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RLP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_27
        
    call RogueFace("sexy") from _call_RogueFace_996 
    
    $ R_LickP += 1  
    $ R_Action -=1     
    if PantsNum("Rogue") != 10 or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 3 if K_LikeRogue >= 800 else 2
     
    if R_LickP == 1:            
            $ R_SEXP += 10         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I. . . how'd I taste?"
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_997
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_89
    return   


# end R_Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label R_Fondle_Ass: 
    call Shift_Focus("Rogue") from _call_Shift_Focus_230
                                                                                     # Will she let you fondle? Modifiers
    if R_FondleA: #You've done it before
        $ Tempmod += 10
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if R_Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in R_Traits:
        $ Tempmod += Taboo  
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount      
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no fondle ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in R_RecentActions else 0   
        
    $ Approval = ApprovalCheck("Rogue", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call RogueFace("surprised", 1) from _call_RogueFace_998  
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
            "As your hand creeps down her backside, Rogue seems a bit surprised, but then nods."              
            call RogueFace("sexy") from _call_RogueFace_999  
            jump RFA_Prep  
        else:          
            call RogueFace("surprised") from _call_RogueFace_1000
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
            ch_r "Hands off, [R_Petname]."   
            call RogueFace("bemused") from _call_RogueFace_1001
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call RogueFace("surprised") from _call_RogueFace_1002   
        $ R_Brows = "sad"        
        if R_Lust > 80:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -4)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
        "As your hand slides out, Rogue gasps and looks upset."              
        jump RFA_Prep     
    elif "fondle ass" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_1003
        ch_r "Mmm, again? Ok."
        jump RFA_Prep
    elif "fondle ass" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_1004
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so rough this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_1005
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
            ch_r "Fine, grab a cheek."   
        else:
            call RogueFace("bemused, 1") from _call_RogueFace_1006 
            ch_r "Sure, grab a cheek."   
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
        jump RFA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_1007
        if "no fondle ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no fondle ass" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no fondle ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_FondleA:
            call RogueFace("bemused") from _call_RogueFace_1008
            ch_r "Not yet, [R_Petname]. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1009
            ch_r "Let's not, ok [R_Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_1010
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_1011  
                ch_r "Heh, maybe, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)  
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no fondle ass")                      
                $ R_DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_1012     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    ch_r "Well, if you're gonna beg. . ."                           
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                    jump RFA_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_1013 
                    ch_r "Tsk, not this time, [R_Petname]."      
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Rogue", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_1014
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -1) 
                    ch_r "Fine, I suppose."                
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3) 
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RFA_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)  
                    call RogueFace("angry", 1) from _call_RogueFace_1015
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                        
    if "no fondle ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1016
        ch_r "Hands off the booty!"
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)    
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_1017    
        $ R_RecentActions.append("tabno")   
        $ R_DailyActions.append("tabno") 
        ch_r "[R_Petname]! Not in public!"                   
    elif R_FondleA:
        call RogueFace("sad") from _call_RogueFace_1018
        ch_r "Sorry, hands off the booty."        
    else:
        call RogueFace("sexy") from _call_RogueFace_1019 
        $ R_Mouth = "sad"
        ch_r "Shoo, [R_Petname]."
    $ R_RecentActions.append("no fondle ass")                      
    $ R_DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_r "Sorry, I don't even know how I got here. . ."
return

label RFA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_9
        if "angry" in R_RecentActions:
            return    
    $ Tempmod = 0      
    call R_Pussy_Launch("fondle ass") from _call_R_Pussy_Launch_7
    if not R_FondleA:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 12)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 20)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_189
    call DrainWord("Rogue","no fondle ass") from _call_DrainWord_190
    $ R_RecentActions.append("fondle ass")                      
    $ R_DailyActions.append("fondle ass") 
    
label RFA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_231 
        call R_Pussy_Launch("fondle ass") from _call_R_Pussy_Launch_8
        call RogueLust from _call_RogueLust_8     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_FondleA):
                    $ R_Brows = "confused"
                    ch_r "Uh, that's nice, but. . ."  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_FondleA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RFA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RFA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1020   
                                    call R_Pos_Reset from _call_R_Pos_Reset_28
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RFA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_7
                                    jump RFA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_7   
                                    
                        "Shift actions":
                                if R_Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call RFA_After from _call_RFA_After_1
                                                    call R_Insert_Ass from _call_R_Insert_Ass    
                                            "Just stick a finger in without asking.":
                                                    $ Situation = "auto"
                                                    call RFA_After from _call_RFA_After_2
                                                    call R_Insert_Ass from _call_R_Insert_Ass_1
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call RFA_After from _call_RFA_After_3
                                                    call R_Lick_Ass from _call_R_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call RFA_After from _call_RFA_After_4
                                                    call R_Lick_Ass from _call_R_Lick_Ass_1    
                                            "I want to stick a dildo in.":
                                                    call R_Dildo_Check from _call_R_Dildo_Check_2
                                                    if Line == "yes":
                                                        $ Situation = "shift"
                                                        call RFA_After from _call_RFA_After_5
                                                        call R_Dildo_Ass from _call_R_Dildo_Ass  
                                                    else:
                                                        jump RFA_Cycle   
                                            "Never Mind":
                                                        pass              
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_10
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RFA_After from _call_RFA_After_6
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_11   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_29
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RFA_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_30
                                    $ Line = 0
                                    jump RFA_After
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_61
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_5
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_31
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RFA_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_16
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RFA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RFA_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1021
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RFA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_32
        
    call RogueFace("sexy") from _call_RogueFace_1022 
    
    $ R_FondleA += 1  
    $ R_Action -=1            
    if PantsNum("Rogue") != 10 or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 1
     
    if R_FondleA == 1:            
            $ R_SEXP += 4         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That was. . . nice. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_1023
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_90    
    return   


# end R_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label R_Insert_Ass:
    call Shift_Focus("Rogue") from _call_Shift_Focus_232
    if R_InsertA: #You've done it before
        $ Tempmod += 25
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if R_Lust > 85 and R_Loose: #She's really horny
        $ Tempmod += 15
    if R_Lust > 95 and R_Loose:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if R_Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no insert ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in R_RecentActions else 0  

    if R_Plugged:
        "You remove the plug from her ass"
        $ R_Plugged = 0 
            
    $ Approval = ApprovalCheck("Rogue", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised") from _call_RogueFace_1024
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
            "As you slide a finger in, Rogue tightens around it in surprise, but seems into it."  
            call RogueFace("sexy") from _call_RogueFace_1025           
            jump RIA_Prep
        else:   
            call RogueFace("surprised") from _call_RogueFace_1026
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
            ch_r "Keep it out of there, [R_Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in R_DailyActions and not R_Loose:
        call RogueFace("bemused", 1) from _call_RogueFace_1027
        ch_r "I'm still a little sore from earlier, [R_Petname]."
    elif "insert ass" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_1028
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "Maybe not so hard this time though.",
            "Mmm. . ."]) 
        ch_r "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_1029
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1) from _call_RogueFace_1030
            $ R_Eyes = "closed"            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)            
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)
            ch_r "Oooooooh. . ."                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
        jump RIA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call RogueFace("angry", 1) from _call_RogueFace_1031
        if "no insert ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no insert ass" in R_DailyActions:  
            ch_r "I told you that wasn't appropriate!" 
        elif "no insert ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_InsertA:
            call RogueFace("perplexed", 1) from _call_RogueFace_1032
            ch_r "I. . . don't think that's. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1033
            ch_r "Oh, um, no, I'm not really comfortable with that. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_1034
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "Maybe later?" if "no insert ass" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_1035  
                ch_r "It's. . . possible, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no insert ass")                      
                $ R_DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_1036           
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
                    jump RIA_Prep
                else:   
                    call RogueFace("bemused") from _call_RogueFace_1037 
                    ch_r "I really don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Rogue", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and R_Forced):                    
                    call RogueFace("surprised", 1) from _call_RogueFace_1038
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                    ch_r "Oh. . . well, ok then. . ."                     
                    call RogueFace("sad") from _call_RogueFace_1039
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RIA_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)  
                    call RogueFace("angry", 1) from _call_RogueFace_1040
                    "She slaps your hand away."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no insert ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1041
        ch_r "Um, no way."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 10) if R_Inbt > 50 else Statupdate("Rogue", "Lust", R_Lust, 50, 3) 
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)      
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_1042    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "[R_Petname]! This just really isn't the time or place!"                   
    elif R_InsertA:
        call RogueFace("sad") from _call_RogueFace_1043 
        ch_r "I think you should keep your fingers to yourself."    
    else:
        call RogueFace("surprised") from _call_RogueFace_1044
        ch_r "I. . . not there!!"
        call RogueFace from _call_RogueFace_1045
    $ R_RecentActions.append("no insert ass")                      
    $ R_DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label RIA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_10
        if "angry" in R_RecentActions:
            return    
            
    $ Tempmod = 0      
    call R_Pussy_Launch("insert ass") from _call_R_Pussy_Launch_9
    if not R_InsertA:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -50)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 60)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 35) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 25)
            
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_191
    call DrainWord("Rogue","no insert ass") from _call_DrainWord_192
    $ R_RecentActions.append("insert ass")                      
    $ R_DailyActions.append("insert ass") 
    
label RIA_Cycle: #Repeating strokes    
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_233 
        call R_Pussy_Launch("insert ass") from _call_R_Pussy_Launch_10
        call RogueLust from _call_RogueLust_9   
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_InsertA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?" 
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_InsertA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RIA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RIA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1046   
                                    call R_Pos_Reset from _call_R_Pos_Reset_33
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RIA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_8
                                    jump RIA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_8   
                        
                        "Shift actions":
                                if R_Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    $ Situation = "pullback"
                                                    call RIA_After from _call_RIA_After_1
                                                    call R_Fondle_Ass from _call_R_Fondle_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call RIA_After from _call_RIA_After_2
                                                    call R_Lick_Ass from _call_R_Lick_Ass_2                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call RIA_After from _call_RIA_After_3
                                                    call R_Lick_Ass from _call_R_Lick_Ass_3    
                                            "I want to stick a dildo in.":
                                                    call R_Dildo_Check from _call_R_Dildo_Check_3
                                                    if Line == "yes":
                                                        $ Situation = "shift"
                                                        call RIA_After from _call_RIA_After_4
                                                        call R_Dildo_Ass from _call_R_Dildo_Ass_1  
                                                    else:
                                                        jump RIA_Cycle  
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_12
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RIA_After from _call_RIA_After_5
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_13   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_34
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RIA_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_35
                                    $ Line = 0
                                    jump RIA_After
        #End menu (if Line)
        
        if R_Panties or PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: #This checks if Rogue wants to strip down.
                call R_Undress("auto") from _call_R_Undress_9
            
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_62
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100: 
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_6
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_36
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RIA_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_17
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RIA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RIA_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1047
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RIA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_37
        
    call RogueFace("sexy") from _call_RogueFace_1048 
    
    $ R_InsertA += 1  
    $ R_Action -=1            
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
     
    if R_InsertA == 1:            
            $ R_SEXP += 12         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "That felt. . . interesting. . ."
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_1049
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_91
    return   


# end R_Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label R_Lick_Ass: 
    call Shift_Focus("Rogue") from _call_Shift_Focus_234
                                                                             # Will she let you lick? Modifiers         
    if R_LickA: #You've done it before
        $ Tempmod += 20
    if PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if R_Lust > 95:
        $ Tempmod += 20  
    elif R_Lust > 85: #She's really horny
        $ Tempmod += 15    
    if R_Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in R_Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 25  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount 
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no lick ass" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in R_RecentActions else 0   
            
    $ Approval = ApprovalCheck("Rogue", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call RogueFace("surprised") from _call_RogueFace_1050   
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Rogue startles briefly, but then begins to melt."  
            call RogueFace("sexy") from _call_RogueFace_1051  
            jump RLA_Prep
        else:   
            call RogueFace("surprised") from _call_RogueFace_1052
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -2)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
            ch_r "Um, no, I'm not really. . . don't."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in R_RecentActions:
        call RogueFace("sexy", 1) from _call_RogueFace_1053
        ch_r "Mmm, again? Ok."
        jump RLA_Prep
    elif "lick ass" in R_DailyActions:
        call RogueFace("sexy", 1) from _call_RogueFace_1054
        $ Line = renpy.random.choice(["Didn't get enough earlier?",
            "I'm still tingling a bit from earlier.",
            "Mmm. . ."]) 
        ch_r "[Line]"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if R_Forced:
            call RogueFace("sad") from _call_RogueFace_1055
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)
            ch_r "Sure, get in there."    
        else:
            call RogueFace("sexy", 1) from _call_RogueFace_1056
            $ R_Eyes = "closed"            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)            
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 3)
            ch_r "Oooooooh. . ."                
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
        jump RLA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call RogueFace("angry", 1) from _call_RogueFace_1057
        if "no lick ass" in R_RecentActions:  
            ch_r "I {i}just{/i} told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions and "no lick ass" in R_DailyActions:  
            ch_r "I told you not to touch me like that in public!" 
        elif "no lick ass" in R_DailyActions:       
            ch_r "I already told you \"no,\" [R_Petname]."
        elif Taboo and "tabno" in R_DailyActions:  
            ch_r "I told you not in public!"  
        elif not R_LickA:                    #First time dialog
            call RogueFace("bemused", 1) from _call_RogueFace_1058
            if R_Love >= R_Obed and R_Love >= R_Inbt:            
                ch_r "I'm not really sure I want you lick'in down there. . ."
            elif R_Obed >= R_Inbt:            
                ch_r "You really don't have to if you don't want to."
            else:
                $ R_Eyes = "sexy"
                ch_r "Hmm. . . it's worth a shot. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1059
            ch_r "Not now, [R_Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in R_DailyActions:
                call RogueFace("bemused") from _call_RogueFace_1060
                ch_r "Yeah, ok, [R_Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in R_DailyActions:
                call RogueFace("sexy") from _call_RogueFace_1061  
                ch_r "Anything's possible, [R_Petname]."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                if Taboo:                    
                    $ R_RecentActions.append("tabno")                      
                    $ R_DailyActions.append("tabno") 
                $ R_RecentActions.append("no lick ass")                      
                $ R_DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call RogueFace("sexy") from _call_RogueFace_1062           
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    ch_r "Ok, you're probably right. . ."      
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2)
                    jump RLA_Prep
                else:   
                    call RogueFace("sexy") from _call_RogueFace_1063 
                    ch_r "Tsk, not this time, [R_Petname], that just seems. . . dirty."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Rogue", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and R_Forced):
                    call RogueFace("sad") from _call_RogueFace_1064
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                    ch_r "Ok, get in there if you're so determined."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ R_Forced = 1
                    jump RLA_Prep
                else:                              
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)  
                    call RogueFace("angry", 1) from _call_RogueFace_1065
                    "She shoves your head back."   
                    $ R_RecentActions.append("angry")
                    $ R_DailyActions.append("angry")   
                    
    if "no lick ass" in R_DailyActions:
        ch_r "Learn to take \"no\" for an answer, [R_Petname]."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1066
        ch_r "Ew, no way."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 10) if R_Inbt > 50 else Statupdate("Rogue", "Lust", R_Lust, 50, 3) 
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:
        call RogueFace("angry", 1) from _call_RogueFace_1067    
        $ R_RecentActions.append("tabno")                   
        $ R_DailyActions.append("tabno") 
        ch_r "This just really isn't the time or place, [R_Petname]!"                   
    elif R_LickP:
        call RogueFace("sad") from _call_RogueFace_1068 
        ch_r "Sorry, keep your tongue in your mouth."    
    else:
        call RogueFace("surprised") from _call_RogueFace_1069
        ch_r "What?! Gross!"
        call RogueFace from _call_RogueFace_1070
    $ R_RecentActions.append("no lick ass")                      
    $ R_DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label RLA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not R_Forced and Situation != "auto":
        $ Tempmod = 0
        if PantsNum("Rogue") == 10:
            $ Tempmod = 15
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_11
        if "angry" in R_RecentActions:
            return    
    $ Tempmod = 0  
    call R_Pussy_Launch("lick ass") from _call_R_Pussy_Launch_11
    if not R_LickA:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -30)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 40)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 80) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 35)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 25)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 55)
    if Taboo:
        $ R_Inbt += int(Taboo/10)  
        $ R_Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ R_Upskirt = 1
    if R_Legs == "skirt":
        $ R_SeenPanties = 1
    if not R_Panties:
        call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_23
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_193
    call DrainWord("Rogue","no lick ass") from _call_DrainWord_194
    
    $ R_RecentActions.append("lick") if "lick" not in R_RecentActions else R_RecentActions
    $ R_RecentActions.append("ass") if "ass" not in R_RecentActions else R_RecentActions
    $ R_RecentActions.append("lick ass")  
    
    $ R_DailyActions.append("lick") if "lick" not in R_DailyActions else R_RecentActions
    $ R_DailyActions.append("ass") if "ass" not in R_DailyActions else R_RecentActions                    
    $ R_DailyActions.append("lick ass")  
label RLA_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_235 
        call R_Pussy_Launch("lick ass") from _call_R_Pussy_Launch_12
        call RogueLust from _call_RogueLust_10     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + R_LickA):
                    $ R_Brows = "confused"
                    ch_r "What are you even doing down there?"  
        elif R_Lust >= 80:
                    pass
        elif Cnt == (15 + R_LickA) and R_SEXP >= 15 and not ApprovalCheck("Rogue", 1500):
                    $ R_Brows = "confused"        
                    menu:
                        ch_r "[R_Petname], this is getting uncomfortable, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump RLA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump RLA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1071   
                                    call R_Pos_Reset from _call_R_Pos_Reset_38
                                    "She scowls at you and pulls back."
                                    ch_r "Well if that's your attitude, I don't need your \"help\"."                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump RLA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_9
                                    jump RLA_Cycle  
                                
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                             
                        "Maybe lose some clothes. . .":
                                    call R_Undress from _call_R_Undress_10   
                                    
                        "Shift actions":
                                if R_Action and MultiAction:
                                        menu:   
                                            "Switch to fondling.":
                                                    $ Situation = "pullback"
                                                    call RLA_After from _call_RLA_After_1
                                                    call R_Fondle_Ass from _call_R_Fondle_Ass_1
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call RLA_After from _call_RLA_After_2
                                                    call R_Insert_Ass from _call_R_Insert_Ass_2                 
                                            "Just stick a finger in [[without asking].":
                                                    $ Situation = "auto"
                                                    call RLA_After from _call_RLA_After_3
                                                    call R_Insert_Ass from _call_R_Insert_Ass_3                        
                                            "I want to stick a dildo in.":
                                                    call R_Dildo_Check from _call_R_Dildo_Check_4
                                                    if Line == "yes":
                                                        $ Situation = "shift"
                                                        call RLA_After from _call_RLA_After_4
                                                        call R_Dildo_Ass from _call_R_Dildo_Ass_2  
                                                    else:
                                                        jump RLA_Cycle   
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_14
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm actually getting a little tired, so maybe we could wrap this up?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call RLA_After from _call_RLA_After_5
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_15   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_39
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump RLA_After
                        "Let's stop for now." if not MultiAction: 
                                    call R_Pos_Reset from _call_R_Pos_Reset_40
                                    $ Line = 0
                                    jump RLA_After
        #End menu (if Line)
        
        if R_Panties or PantsNum("Rogue") == 10 or HoseNum("Rogue") >= 5: #This checks if Rogue wants to strip down.
                call R_Undress("auto") from _call_R_Undress_11
            
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_63
                
        #If either of you could cum 
        
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or R_Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_7
                            if "angry" in R_RecentActions:  
                                call R_Pos_Reset from _call_R_Pos_Reset_41
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump RLA_After 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if R_Lust >= 100:                                               
                        call R_Cumming from _call_R_Cumming_18
                        if Situation == "shift" or "angry" in R_RecentActions:
                            jump RLA_After
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,  
                            "Rogue still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit.":
                                    $ Line = "You get back into it" 
                                "No, I'm done.":
                                    "You pull back."
                                    jump RLA_After
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1072
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    
label RLA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call R_Pos_Reset from _call_R_Pos_Reset_42
        
    call RogueFace("sexy") from _call_RogueFace_1073 
    
    $ R_LickA += 1  
    $ R_Action -=1      
    if PantsNum("Rogue") != 10 or R_Upskirt:        
        $ R_Addictionrate += 1
        if "addictive" in P_Traits:
            $ R_Addictionrate += 1
    
    if K_Loc == bg_current and "noticed rogue" in K_RecentActions: #If Kitty was participating
        $ K_LikeRogue += 2 if K_LikeRogue >= 800 else 1
     
    if R_LickA == 1:            
            $ R_SEXP += 15         
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Was. . . that something you liked?"
                elif R_Obed <= 500 and P_Focus <= 20:
                    call RogueFace("perplexed", 1) from _call_RogueFace_1074
                    ch_r "Did you like that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_92
    return   

# end R_Lick Ass /////////////////////////////////////////////////////////////////////////////

