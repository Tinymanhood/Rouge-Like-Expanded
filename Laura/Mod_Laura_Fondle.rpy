# newgirl["Laura"].Massage /////////////////////////////////////////////////////////////////////////////
label Laura_Massage:
    call Shift_Focus("Laura")
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Laura", 500, TabM = 2) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call LauraFace("bemused", 1)
        if newgirl["Laura"].Forced:
                call LauraFace("sad")
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
        ch_l "I guess I could use a rubdown."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
        jump Laura_Massage_Prep
        
    else:
        call LauraFace("angry", 1)
        if "no massage" in newgirl["Laura"].RecentActions:  
            ch_l "I only {i}just{/i} refused you, [newgirl[Laura].Petname]."
        elif "no massage" in newgirl["Laura"].DailyActions:       
            ch_l "I told you \"no\" earlier, [newgirl[Laura].Petname]."
        else:
            call LauraFace("bemused")
            ch_l "I'm not interested at the moment, [newgirl[Laura].Petname]."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "No worries."              
                return
            "Maybe later?" if "no massage" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 1)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)  
                $ newgirl["Laura"].RecentActions.append("no massage")                      
                $ newgirl["Laura"].DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                    ch_l "I do have some tension built up. . ."                
                    jump Laura_Massage_Prep
                else:   
                    call LauraFace("sly", Brows="confused") 
                    ch_l "No." 
    
    if "no massage" in newgirl["Laura"].DailyActions:
        ch_l "I've made myself clear on this, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "You'll have to keep your hands limber for yourself."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        ch_l "I try to stay off the radar."                  
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "I really can't."    
    $ newgirl["Laura"].RecentActions.append("no massage")                      
    $ newgirl["Laura"].DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label Laura_Massage_Prep:
    call Laura_Top_Off("massage")
    if "angry" in newgirl["Laura"].RecentActions:
        return    
    
label Laura_Massage_Cycle: 
    $ newgirl["Laura"].RecentActions.append("massage")                      
    $ newgirl["Laura"].DailyActions.append("massage") 
        
    "You massage her back and shoulders."
    if not newgirl["Laura"].Over:
        $ newgirl["Laura"].Addict -= D20 if newgirl["Laura"].Addict > D20 else newgirl["Laura"].Addict
    
    $ D20 = renpy.random.randint(10, 20)
    $ Round -= D20 if Round > D20 else (Round-1)
            
    ch_l "That was very. . . pleasant, [newgirl[Laura].Petname]"
    if "massage" not in newgirl["Laura"].RecentActions:        
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 2)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
    return

# end newgirl["Laura"].Massage /////////////////////////////////////////////////////////////////////////////

# newgirl["Laura"].Fondle /////////////////////////////////////////////////////////////////////////////
label Laura_Fondle:
    
    $ newgirl["Laura"].Mouth = "smile"
    if not newgirl["Laura"].Action:
        ch_l "I'm rather tired right now, [newgirl[Laura].Petname], raincheck?"
        return
    menu:
        ch_l "Well? Where did you want to touch, [newgirl[Laura].Petname]?"
        "Your breasts?" if newgirl["Laura"].Action:
                jump Laura_Fondle_Breasts
        "Your thighs?" if newgirl["Laura"].Action:
                jump Laura_Fondle_Thighs
        "Your pussy?" if newgirl["Laura"].Action:
                jump Laura_Fondle_Pussy
        "Your Ass?" if newgirl["Laura"].Action:
                jump Laura_Fondle_Ass
        "Never mind.":
                return
    return


# newgirl["Laura"].Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label Laura_Fondle_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    
    # Will she let you fondle? Modifiers
    if newgirl["Laura"].FondleB: #You've done it before
        $ Tempmod += 15
    if newgirl["Laura"].Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 20
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle breasts" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in newgirl["Laura"].RecentActions else 0        
        
    $ Approval = ApprovalCheck("Laura", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call LauraFace("sexy")       
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)            
            "As you cup her breast, Laura gently nods."            
            jump Laura_FB_Prep        
        else:   
            call LauraFace("surprised")
            $ newgirl["Laura"].Brows = "confused"
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)
            ch_l "Roll it back, [newgirl[Laura].Petname]. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call LauraFace("sexy", 1)
        if newgirl["Laura"].Forced: 
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)           
        elif not Taboo and "tabno" in newgirl["Laura"].DailyActions:        
            ch_l "This does seem less. . . exposed."   
            
    if "fondle breasts" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FB_Prep
    elif "fondle breasts" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
            
    if Approval >= 2:             
        call LauraFace("bemused", 1)
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
        ch_l "Sure, sounds fun."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
        jump Laura_FB_Prep
        
    else:
        call LauraFace("angry", 1)
        if "no fondle breasts" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no fondle breasts" in newgirl["Laura"].DailyActions:  
            ch_l "I've had enough of this today." 
        elif "no fondle breasts" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].FondleB:
            call LauraFace("bemused")
            ch_l "Look, I don't know if we're ready for that, [newgirl[Laura].Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Keep dreaming."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "No worries."              
                return
            "Maybe later?" if "no fondle breasts" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Eh. Maybe."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no fondle breasts")                      
                $ newgirl["Laura"].DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."                
                    jump Laura_FB_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)                 
                    ch_l "Hey. . ."
                    ch_l "Eh, whatever. . ."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)   
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_FB_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
    
    if "no fondle breasts" in newgirl["Laura"].DailyActions:
        ch_l "Listen to the words that are coming out of my mouth."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "No."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")                   
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].FondleB:
        call LauraFace("sad")
        ch_l "You'll have to earn that back."        
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No."    
    $ newgirl["Laura"].RecentActions.append("no fondle breasts")                      
    $ newgirl["Laura"].DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label Laura_FB_Prep: #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Top_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return
        
    $ Tempmod = 0  
    call Laura_Breasts_Launch("fondle breasts")
    if not newgirl["Laura"].FondleB:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -20)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 25)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
            
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)        
    
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0     
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no fondle breasts")
    $ newgirl["Laura"].RecentActions.append("fondle breasts")                      
    $ newgirl["Laura"].DailyActions.append("fondle breasts") 
    
label Laura_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Breasts_Launch("fondle breasts")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_FB_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:
                                                        "Ask to suck on them.":
                                                                if newgirl["Laura"].Action and MultiAction:                        
                                                                    $ Situation = "shift"
                                                                    call Laura_FB_After
                                                                    call Laura_Suck_Breasts
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"
                                                        "Just suck on them without asking.":
                                                                if newgirl["Laura"].Action and MultiAction:                            
                                                                    $ Situation = "auto"
                                                                    call Laura_FB_After
                                                                    call Laura_Suck_Breasts
                                                                else:
                                                                    "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                                    ch_l "Maybe we could finish this up for now?"
                                                        "Never Mind":
                                                                jump Laura_FB_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_FB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_FB_Cycle 
                                            "Never mind":
                                                        jump Laura_FB_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_FB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FB_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_FB_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_FB_After
                       
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
                                        jump Laura_FB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].FondleB):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Enjoying yourself?" 
        elif newgirl["Laura"].Lust >= 85:
                    pass  
        elif Cnt == (15 + newgirl["Laura"].FondleB) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused" 
                    menu:
                        ch_l "Maybe it's time for something else, [newgirl[Laura].Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "Well, I've got better things to be doing."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_FB_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
label Laura_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].FondleB += 1  
    $ newgirl["Laura"].Action -=1
    $ newgirl["Laura"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Laura"].Addictionrate += 1        
    
    call Partner_Like("Laura",2)
     
    if newgirl["Laura"].FondleB == 1:            
            $ newgirl["Laura"].SEXP += 4         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "Did you enjoy that?"
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "That worked out for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label Laura_Suck_Breasts:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you suck? Modifiers
    if newgirl["Laura"].SuckB: #You've done it before
        $ Tempmod += 15
    if not newgirl["Laura"].Chest and not newgirl["Laura"].Over:
        $ Tempmod += 15
    if newgirl["Laura"].Lust > 75: #She's really horny
        $ Tempmod += 20
    if newgirl["Laura"].Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25  
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no suck breasts" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in newgirl["Laura"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Laura", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)            
            "As you dive in, Laura seems a bit surprised, but just makes a little \"grunt.\""              
            jump Laura_SB_Prep      
        else:               
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)
            ch_l "Roll it back, [newgirl[Laura].Petname]. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_SB_Prep
    elif "suck breasts" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
        ch_l "Sure."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
        jump Laura_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no suck breasts" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no suck breasts" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, I couldn't be caught like that." 
        elif "no suck breasts" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].SuckB:
            call LauraFace("bemused")
            ch_l "Let's work up to that maybe. ."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool."              
                return
            "Maybe later?" if "no suck breasts" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no suck breasts")                      
                $ newgirl["Laura"].DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                    ch_l "Ok, fine. . ."                
                    jump Laura_SB_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."    
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Laura", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)                 
                    ch_l "Hmm. . . ok. . ."                         
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_SB_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)  
                    call LauraFace("angry", 1)
                    "She shoves your head back out."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no suck breasts" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "Not worth it."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)    
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:   
        call LauraFace("angry", 1)      
        $ newgirl["Laura"].RecentActions.append("tabno")    
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].SuckB:
        call LauraFace("sad")
        ch_l "You'll have to earn that back."            
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No."
    $ newgirl["Laura"].RecentActions.append("no suck breasts")                      
    $ newgirl["Laura"].DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label Laura_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0   
        call Laura_Top_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return
    
    $ Tempmod = 0      
    call Laura_Breasts_Launch("suck breasts")
    if not newgirl["Laura"].SuckB:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -25)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 25)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 17) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
    
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0  
    $ Cnt = 0      
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no suck breasts")
    $ newgirl["Laura"].RecentActions.append("suck breasts")                      
    $ newgirl["Laura"].DailyActions.append("suck breasts") 
    
label Laura_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Breasts_Launch("suck breasts")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_SB_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:
                                                        "Pull back to fondling.":  
                                                            if newgirl["Laura"].Action and MultiAction:
                                                                $ Situation = "pullback"
                                                                call Laura_SB_After
                                                                call Laura_Fondle_Breasts
                                                            else:
                                                                "As you pull back, Laura pushes you back in close."
                                                                ch_l "Maybe we could finish this up for now?"
                                                        "Never Mind":
                                                                jump Laura_SB_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_SB_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_SB_Cycle 
                                            "Never mind":
                                                        jump Laura_SB_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_SB_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_SB_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_SB_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_SB_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_SB_After
                       
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
                                            jump Laura_SB_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].SuckB):
                    $ newgirl["Laura"].Brows = "sly"
                    ch_l "This is kinda nice. . ."   
        elif newgirl["Laura"].Lust >= 85:
                    pass
        elif Cnt == (15 + newgirl["Laura"].SuckB) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_SB_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_SB_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
label Laura_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].SuckB += 1  
    $ newgirl["Laura"].Action -=1
    $ newgirl["Laura"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Laura"].Addictionrate += 1        
    
    if Partner == "Kitty":
        call Partner_Like("Laura",2,2)
    else:
        call Partner_Like("Laura",2)
     
    if newgirl["Laura"].SuckB == 1:            
            $ newgirl["Laura"].SEXP += 4         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was kinda nice."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you get enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label Laura_Fondle_Thighs:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you fondle her thighs? Modifiers
    if newgirl["Laura"].FondleT: #You've done it before
        $ Tempmod += 10
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if newgirl["Laura"].Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += Taboo   
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25 
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount      
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle thighs" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in newgirl["Laura"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)            
            "As you caress her thigh, Laura glances at you, and smiles."             
            jump Laura_FT_Prep      
        else:               
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)
            ch_l "Maybe we keep it above the waist, [newgirl[Laura].Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")    
        $ newgirl["Laura"].Brows = "sad"
        if newgirl["Laura"].Lust > 60:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
        "As you pull back, Laura looks a little annoyed."              
        jump Laura_FT_Prep  
    elif "fondle thighs" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FT_Prep
    elif "fondle thighs" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)       
        ch_l "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
        ch_l "Ok [newgirl[Laura].Petname], go ahead."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
        jump Laura_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle thighs" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no fondle thighs" in newgirl["Laura"].DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].FondleT:
            call LauraFace("bemused")
            ch_l "Seems a bit aggressive, [newgirl[Laura].Petname]."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool."             
                return
            "Maybe later?" if "no fondle thighs" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no fondle thighs")                      
                $ newgirl["Laura"].DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                    ch_l "Well if you're going to be a little bitch about it. . ."             
                    jump Laura_FT_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "Well if you're going to be a little bitch about it. . ."    
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)                 
                    ch_l "Hmmph."                         
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_FT_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -8)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no fondle thighs" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "No."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 2)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1)   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")          
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].FondleT:
        call LauraFace("sad")
        ch_l "Keep your hands to yourself."            
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No."
    $ newgirl["Laura"].RecentActions.append("no fondle thighs")                      
    $ newgirl["Laura"].DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label Laura_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kiss you": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off 
        if "angry" in newgirl["Laura"].RecentActions:
            return 
            
    $ Tempmod = 0    
    call Laura_Pussy_Launch("fondle thighs")
    if not newgirl["Laura"].FondleT:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 15)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 10) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
            
    if Taboo:               
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, (int(Taboo/5)))                               
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no fondle thighs")
    $ newgirl["Laura"].RecentActions.append("fondle thighs")                      
    $ newgirl["Laura"].DailyActions.append("fondle thighs")  
    
label Laura_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("fondle thighs")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                         
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_FT_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "Can I do a little deeper?":
                                                                if newgirl["Laura"].Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Laura_FT_After
                                                                    call Laura_Fondle_Pussy                
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"  
                                                        "Shift your hands a bit higher without asking":
                                                                if newgirl["Laura"].Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Laura_FT_After
                                                                    call Laura_Fondle_Pussy    
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_l "Maybe we could finish this up for now?" 
                                                        "Never Mind":
                                                                jump Laura_FT_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_FT_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_FT_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_FT_Cycle 
                                            "Never mind":
                                                        jump Laura_FT_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_FT_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FT_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FT_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_FT_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_FT_After
                       
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
                                            jump Laura_FT_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].FondleT):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Kinda nice, but. . ."   
        elif Cnt == (15 + newgirl["Laura"].FondleT) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FT_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_FT_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
    
label Laura_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].FondleT += 1  
    $ newgirl["Laura"].Action -=1
    if newgirl["Laura"].Legs != "pants" or newgirl["Laura"].Upskirt:        
        $ newgirl["Laura"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 1
    
    if Partner == "Kitty":
        call Partner_Like("Laura",2)
    else:
        call Partner_Like("Laura",1)
     
    if newgirl["Laura"].FondleT == 1:            
            $ newgirl["Laura"].SEXP += 3         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was. . . interesting."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Was that enough?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label Laura_Fondle_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                        # Will she let you fondle? Modifiers
    if newgirl["Laura"].FondleP: #You've done it before
        $ Tempmod += 20
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if newgirl["Laura"].Lust > 75: #She's really horny
        $ Tempmod += 15
    if newgirl["Laura"].Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25  
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle pussy" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in newgirl["Laura"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call LauraFace("sexy")       
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
            "As your hand creeps up her thigh, Laura seems a bit surprised, but then nods."            
            jump Laura_FP_Prep      
        else:               
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)
            ch_l "Roll it back, [newgirl[Laura].Petname]. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")   
        $ newgirl["Laura"].Brows = "sad"        
        if newgirl["Laura"].Lust > 80:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -4)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
        "As your hand pulls out, Laura gasps and looks upset."              
        jump Laura_FP_Prep     
    elif "fondle pussy" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FP_Prep
    elif "fondle pussy" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Take it slow, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call LauraFace("bemused", 1)
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
        ch_l "Mmmm, I couldn't refuse. . ."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
        jump Laura_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle pussy" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no fondle pussy" in newgirl["Laura"].DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].FondleP:
            call LauraFace("bemused")
            ch_l "I don't think we're there yet, [newgirl[Laura].Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [newgirl[Laura].Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no fondle pussy")                      
                $ newgirl["Laura"].DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                    ch_l "Oooh, beg for me. . ."                    
                    jump Laura_FP_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)                 
                    ch_l "Ok, fine. . ."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_FP_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -15)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no fondle pussy" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "I don't think so, [newgirl[Laura].Petname]."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)    
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")                   
        $ newgirl["Laura"].DailyActions.append("tabno")
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].FondleP:
        call LauraFace("sad")
        ch_l "Sorry, fingers outside."           
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No thank you, [newgirl[Laura].Petname]."
    $ newgirl["Laura"].RecentActions.append("no fondle pussy")                      
    $ newgirl["Laura"].DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label Laura_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off   
        if "angry" in newgirl["Laura"].RecentActions:
            return 
    $ Tempmod = 0
    
    call Laura_Pussy_Launch("fondle pussy")
    if not newgirl["Laura"].FondleP:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -50)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 35)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 25) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
    
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no fondle pussy")
    $ newgirl["Laura"].RecentActions.append("fondle pussy")                      
    $ newgirl["Laura"].DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label Laura_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("fondle pussy")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                          
                        "I want to stick a finger in. . ." if Speed != 2:
                                if newgirl["Laura"].InsertP: 
                                    $ Speed = 2
                                else:
                                    menu:                                
                                        "Ask her first":
                                            $ Situation = "shift"
                                        "Don't ask first [[just stick it in]":                                    
                                            $ Situation = "auto"
                                    call Laura_Insert_Pussy 
                        
                        "Pull back a bit. . ." if Speed == 2:
                                    $ Speed = 0
                                    
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_FP_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to lick your pussy.":
                                                                $ Situation = "shift"
                                                                call Laura_FP_After
                                                                call Laura_Lick_Pussy                 
                                                        "Just start licking":
                                                                $ Situation = "auto"
                                                                call Laura_FP_After
                                                                call Laura_Lick_Pussy         
                                                        "Pull back to the thighs":
                                                                $ Situation = "pullback"
                                                                call Laura_FP_After
                                                                call Laura_Fondle_Thighs
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_FP_After
                                                                call Laura_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Laura_FP_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_FP_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_FP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_FP_Cycle 
                                            "Never mind":
                                                        jump Laura_FP_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_FP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FP_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_FP_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_FP_After
                       
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
                                            jump Laura_FP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].FondleP):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Mmmm, you're enjoying that, huh?"  
        elif newgirl["Laura"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Laura"].FondleP) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_FP_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
    
label Laura_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].FondleP += 1  
    $ newgirl["Laura"].Action -=1
    if newgirl["Laura"].Legs != "pants" or newgirl["Laura"].Upskirt:        
        $ newgirl["Laura"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if newgirl["Laura"].FondleP == 1:            
            $ newgirl["Laura"].SEXP += 7         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "You're really getting into the good stuff."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you find what you were looking for?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# end newgirl["Laura"].Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Laura_Insert_Pussy:
    call Shift_Focus("Laura")
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Laura", 1100, TabM = 2):
            call LauraFace("surprised")       
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
            "As you slide a finger in, Laura seems a bit surprised, but seems into it."              
            jump Laura_IP_Prep
        else:   
            call LauraFace("surprised",2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
            ch_l "Oooh!"
            "She slaps your hand back."
            call LauraFace("perplexed",1)
            ch_l "Watch your hands, or lose them."
            return            
    
    if ApprovalCheck("Laura", 1100, TabM = 2):                                                                   #She's into it. . .               
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
            ch_l "Going there, huh. . ."    
        else:
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
            ch_l "Mmmmmm. . ."                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
        jump Laura_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call LauraFace("bemused", 1)
        ch_l "Nope."
        $ newgirl["Laura"].Blush = 0
    return
    
                
label Laura_IP_Prep: #Animation set-up     
    if not newgirl["Laura"].InsertP:
        $ newgirl["Laura"].InsertP = 1
        $ newgirl["Laura"].SEXP += 10          
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -60)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 55)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 35) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 20)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 25)
                
    if not newgirl["Laura"].Forced and Situation != "auto":        
        call Laura_Undress("bottom")
        if "angry" in newgirl["Laura"].RecentActions:
            return    
            
#    call Laura_Pussy_Launch("insert pussy")
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
        
    $ Line = 0  
    $ Speed = 2
    return

# end newgirl["Laura"].Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Laura_Lick_Pussy: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                  # Will she let you fondle? Modifiers     
    if newgirl["Laura"].LickP: #You've done it before
        $ Tempmod += 15
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if newgirl["Laura"].Lust > 95:
        $ Tempmod += 20  
    elif newgirl["Laura"].Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if newgirl["Laura"].Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25  
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no lick pussy" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in newgirl["Laura"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Laura starts, but then softens."  
            call LauraFace("sexy")           
            jump Laura_LP_Prep
        else:   
            call LauraFace("surprised")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
            ch_l "Hey, good instincts, but maybe hold off?" 
            call LauraFace("perplexed",1)
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LP_Prep
    elif "lick pussy" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this treatment. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
            ch_l "If you must. . ."    
        else:
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Eyes = "closed"            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)            
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 3)
            ch_l "Mmmmmm. . ."                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
        jump Laura_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no lick pussy" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no lick pussy" in newgirl["Laura"].DailyActions:  
            ch_l "You already got your answer!" 
        elif "no lick pussy" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].LickP:
            call LauraFace("bemused")
            ch_l "I'm not sure we're there yet, [newgirl[Laura].Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "I'm really not cool with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [newgirl[Laura].Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "I'll be thinking about it, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no lick pussy")                      
                $ newgirl["Laura"].DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    ch_l "You make a good point. . ."      
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    jump Laura_LP_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "I would, but still no, [newgirl[Laura].Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Laura", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)                 
                    ch_l "If you insist. . ."  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_LP_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -15)  
                    call LauraFace("angry", 1)
                    "She shoves your head back."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no lick pussy" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "I really can't, [newgirl[Laura].Petname]."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)     
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")                   
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].LickP:
        call LauraFace("sad") 
        ch_l "Keep your head out of there."    
    else:
        call LauraFace("surprised")
        ch_l "Yeah, sorry."
        call LauraFace
    $ newgirl["Laura"].RecentActions.append("no lick pussy")                      
    $ newgirl["Laura"].DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label Laura_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        if newgirl["Laura"].Legs == "pants":
            $ Tempmod = 15
        call Laura_Bottoms_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return  
            
    $ Tempmod = 0      
    call Laura_Pussy_Launch("lick pussy")
    if not newgirl["Laura"].LickP:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -30)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 35)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 75) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 35)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 15)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 35)
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if newgirl["Laura"].Legs == "skirt":
        $ newgirl["Laura"].Upskirt = 1  
        $ newgirl["Laura"].SeenPanties = 1
    if not newgirl["Laura"].Panties:
        call Laura_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no lick pussy")
    $ newgirl["Laura"].RecentActions.append("lick pussy")                      
    $ newgirl["Laura"].DailyActions.append("lick pussy") 
    
label Laura_LP_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0   
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("lick pussy")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_LP_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                if newgirl["Laura"].Action and MultiAction:
                                                                    $ Situation = "pullback"
                                                                    call Laura_LP_After
                                                                    call Laura_Fondle_Pussy
                                                                else:
                                                                    ch_l "Maybe we could finish this up for now?"  
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_LP_After
                                                                call Laura_Dildo_Pussy  
                                                        "Never Mind":
                                                                jump Laura_LP_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_LP_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_LP_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_LP_Cycle 
                                            "Never mind":
                                                        jump Laura_LP_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_LP_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_LP_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_LP_After
        #End menu (if Line)
        
        if newgirl["Laura"].Panties or newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call Laura_Undress("auto")
                
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_LP_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_LP_After
                       
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
                                            jump Laura_LP_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].LickP):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Isn't it just delicious?"  
        elif newgirl["Laura"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Laura"].LickP) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                       
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_LP_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_LP_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
    
label Laura_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].LickP += 1  
    $ newgirl["Laura"].Action -=1     
    if newgirl["Laura"].Legs != "pants" or newgirl["Laura"].Upskirt:        
        $ newgirl["Laura"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 1
    
    if Partner == "Rogue":
        call Partner_Like("Laura",3,2)
    else:
        call Partner_Like("Laura",2)
     
    if newgirl["Laura"].LickP == 1:            
            $ newgirl["Laura"].SEXP += 10         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was a really good use of that tongue of yours."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "I suppose we both got something out of that. . ."
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end newgirl["Laura"].Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label Laura_Fondle_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                                     # Will she let you fondle? Modifiers
    if newgirl["Laura"].FondleA: #You've done it before
        $ Tempmod += 10
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if newgirl["Laura"].Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += Taboo  
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25 
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount      
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle ass" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in newgirl["Laura"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Laura", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call LauraFace("surprised", 1)  
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
            "As your hand creeps down her backside, Laura shivers a bit, and then relaxes."              
            call LauraFace("sexy")  
            jump Laura_FA_Prep  
        else:          
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
            ch_l "Hands off, [newgirl[Laura].Petname]."   
            call LauraFace("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call LauraFace("surprised")   
        $ newgirl["Laura"].Brows = "sad"        
        if newgirl["Laura"].Lust > 80:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -4)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
        "As your finger slides out, Laura gasps and looks upset."              
        jump Laura_FA_Prep     
    elif "fondle ass" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_FA_Prep
    elif "fondle ass" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Mmm, you like that? . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
            ch_l "If you insist. . ."   
        else:
            call LauraFace("bemused, 1") 
            ch_l "Yeah, ok. . ."   
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
        jump Laura_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no fondle ass" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no fondle ass" in newgirl["Laura"].DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no fondle ass" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].FondleA:
            call LauraFace("bemused")
            ch_l "Not yet, [newgirl[Laura].Petname]. . ."
        else:
            call LauraFace("bemused")
            ch_l "Let's not, ok [newgirl[Laura].Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [newgirl[Laura].Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Maybe?"
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)  
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no fondle ass")                      
                $ newgirl["Laura"].DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call LauraFace("sexy")     
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    ch_l "Oooh, beg for me. . ."                           
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                    jump Laura_FA_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Laura", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -1) 
                    ch_l "Fine, I guess."                
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3) 
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_FA_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -10)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                        
    if "no fondle ass" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "Do you want to keep those fingers?"
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)    
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")   
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].FondleA:
        call LauraFace("sad")
        ch_l "Sorry, keep your hands to yourself."        
    else:
        call LauraFace("sexy") 
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No."
    $ newgirl["Laura"].RecentActions.append("no fondle ass")                      
    $ newgirl["Laura"].DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_l "Sorry, I don't even know how I got here. . ."
return

label Laura_FA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return    
    $ Tempmod = 0      
    call Laura_Pussy_Launch("fondle ass")
    if not newgirl["Laura"].FondleA:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -20)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 20)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 15) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 12)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 20)
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
     
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0   
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no fondle ass")
    $ newgirl["Laura"].RecentActions.append("fondle ass")                      
    $ newgirl["Laura"].DailyActions.append("fondle ass") 
    
label Laura_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("fondle ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_FA_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Insert_Ass    
                                                        "Just stick a finger in without asking.":
                                                                $ Situation = "auto"
                                                                call Laura_FA_After
                                                                call Laura_Insert_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Laura_FA_After
                                                                call Laura_Lick_Ass    
                                                        "I want to stick a dildo in.":                                                                
                                                                $ Situation = "shift"
                                                                call Laura_FA_After
                                                                call Laura_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Laura_FA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_FA_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_FA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_FA_Cycle 
                                            "Never mind":
                                                        jump Laura_FA_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_FA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_FA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_FA_After
        #End menu (if Line)
        
        if newgirl["Laura"].Panties or newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call Laura_Undress("auto")
                
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_FA_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_FA_After
                       
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
                                            jump Laura_FA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].FondleA):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Mmmm. . ."  
        elif newgirl["Laura"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Laura"].FondleA) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_FA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_FA_After
        #End Count check
        
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
    
label Laura_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].FondleA += 1  
    $ newgirl["Laura"].Action -=1            
    if newgirl["Laura"].Legs != "pants" or newgirl["Laura"].Upskirt:        
        $ newgirl["Laura"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 1
    
        call Partner_Like("Laura",2)
     
    if newgirl["Laura"].FondleA == 1:            
            $ newgirl["Laura"].SEXP += 4         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was. . . nice. . ."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end newgirl["Laura"].Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Laura_Insert_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    
    if newgirl["Laura"].InsertA: #You've done it before
        $ Tempmod += 25
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if newgirl["Laura"].Lust > 85: #She's really horny
        $ Tempmod += 15
    if newgirl["Laura"].Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if newgirl["Laura"].Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25 
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no insert ass" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in newgirl["Laura"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
            "As you slide a finger in, Laura tightens around it in surprise, but seems into it."  
            call LauraFace("sexy")           
            jump Laura_IA_Prep
        else:   
            call LauraFace("surprised")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
            ch_l "Whoa, back off, [newgirl[Laura].Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Chill. . .",
            "Mmm. . ."]) 
        ch_l "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
            ch_l "If you must. . ."    
        else:
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Eyes = "closed"            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)            
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 3)
            ch_l "Mmmmm. . ."                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
        jump Laura_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call LauraFace("angry", 1)
        if "no insert ass" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no insert ass" in newgirl["Laura"].DailyActions:  
            ch_l "I told you that wasn't appropriate!" 
        elif "no insert ass" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].InsertA:
            call LauraFace("perplexed", 1)
            ch_l "That's really not my style. . ."
        else:
            call LauraFace("bemused")
            ch_l "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [newgirl[Laura].Petname]."              
                return
            "Maybe later?" if "no insert ass" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "It's. . . possible, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no insert ass")                      
                $ newgirl["Laura"].DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    ch_l "You're probably right. . ."      
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    jump Laura_IA_Prep
                else:   
                    call LauraFace("bemused") 
                    ch_l "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Laura", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):                    
                    call LauraFace("surprised", 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)                 
                    ch_l "Well hello there. . ."                     
                    call LauraFace("sad")
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_IA_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -15)  
                    call LauraFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no insert ass" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "I'm not going there today."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10) if newgirl["Laura"].Inbt > 50 else Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 3) 
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)      
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")                   
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].InsertA:
        call LauraFace("sad") 
        ch_l "I don't feel like it."    
    else:
        call LauraFace("surprised")
        ch_l "Not today, [newgirl[Laura].Petname]."
        call LauraFace
    $ newgirl["Laura"].RecentActions.append("no insert ass")                      
    $ newgirl["Laura"].DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label Laura_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Laura_Bottoms_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return    
            
    $ Tempmod = 0      
    call Laura_Pussy_Launch("insert ass")
    if not newgirl["Laura"].InsertA:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -50)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 60)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 35) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 20)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 25)
            
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
        
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    $ Line = 0    
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no insert ass")
    $ newgirl["Laura"].RecentActions.append("insert ass")                      
    $ newgirl["Laura"].DailyActions.append("insert ass") 
    
label Laura_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("insert ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_IA_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "Pull out and start rubbing again.":
                                                                $ Situation = "pullback"
                                                                call Laura_IA_After
                                                                call Laura_Fondle_Ass
                                                        "I want to lick your asshole.":
                                                                $ Situation = "shift"
                                                                call Laura_IA_After
                                                                call Laura_Lick_Ass                 
                                                        "Just start licking.":
                                                                $ Situation = "auto"
                                                                call Laura_IA_After
                                                                call Laura_Lick_Ass    
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_IA_After
                                                                call Laura_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Laura_IA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_IA_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_IA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_IA_Cycle 
                                            "Never mind":
                                                        jump Laura_IA_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_IA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_IA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_IA_After
        #End menu (if Line)
        
        if newgirl["Laura"].Panties or newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call Laura_Undress("auto")
                
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_IA_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_IA_After
                       
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
                                            jump Laura_IA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].InsertA):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "Ungh, you're really getting in there. . ."  
        elif newgirl["Laura"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Laura"].InsertA) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "Maybe change things up a little?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_IA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_IA_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
label Laura_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].InsertA += 1  
    $ newgirl["Laura"].Action -=1            
    $ newgirl["Laura"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Laura"].Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if newgirl["Laura"].InsertA == 1:            
            $ newgirl["Laura"].SEXP += 12         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was kinda wild. . ."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Did you enjoy that?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   


# end newgirl["Laura"].Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Laura_Lick_Ass: 
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
                                                                             # Will she let you lick? Modifiers         
    if newgirl["Laura"].LickA: #You've done it before
        $ Tempmod += 20
    if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if newgirl["Laura"].Lust > 95:
        $ Tempmod += 20  
    elif newgirl["Laura"].Lust > 85: #She's really horny
        $ Tempmod += 15    
    if newgirl["Laura"].Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Laura"].Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 25  
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount 
    
    if Taboo and "tabno" in newgirl["Laura"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Laura"].History:                   
        $ Tempmod -= 20 
        
    if "no lick ass" in newgirl["Laura"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in newgirl["Laura"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Laura", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call LauraFace("surprised")   
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Laura startles briefly, but then begins to melt."  
            call LauraFace("sexy")  
            jump Laura_LA_Prep
        else:   
            call LauraFace("surprised")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
            ch_l "[newgirl[Laura].Petname]! No. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in newgirl["Laura"].RecentActions:
        call LauraFace("sexy", 1)
        ch_l "Mmmm, again? I guess. . ."
        jump Laura_LA_Prep
    elif "lick ass" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        ch_l "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Laura"].Forced:
            call LauraFace("sad")
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
            ch_l "Meh. . ."    
        else:
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Eyes = "closed"            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)            
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 3)
            ch_l "Mmm. . . naughty."                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2) 
        jump Laura_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call LauraFace("angry", 1)
        if "no lick ass" in newgirl["Laura"].RecentActions:  
            ch_l "Take a breath here, before you regret it."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions and "no lick ass" in newgirl["Laura"].DailyActions:  
            ch_l "I told you not to touch me like that in public!" 
        elif "no lick ass" in newgirl["Laura"].DailyActions:       
            ch_l "Don't make me tell you again today."
        elif Taboo and "tabno" in newgirl["Laura"].DailyActions:  
            ch_l "I told you, not here, [newgirl[Laura].Petname]."  
        elif not newgirl["Laura"].LickA:                    #First time dialog
            call LauraFace("bemused", 1)
            if newgirl["Laura"].Love >= newgirl["Laura"].Obed and newgirl["Laura"].Love >= newgirl["Laura"].Inbt:            
                ch_l "Oh, we're there now?"
            elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:            
                ch_l "Is that what gets you off?"
            else:
                $ newgirl["Laura"].Eyes = "sexy"
                ch_l "Hm, I didn't know that's what you were into."
        else:
            call LauraFace("bemused")
            ch_l "Not now, [newgirl[Laura].Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in newgirl["Laura"].DailyActions:
                call LauraFace("bemused")
                ch_l "It's cool, [newgirl[Laura].Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in newgirl["Laura"].DailyActions:
                call LauraFace("sexy")  
                ch_l "Anything's possible, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Laura"].RecentActions.append("tabno")                      
                    $ newgirl["Laura"].DailyActions.append("tabno") 
                $ newgirl["Laura"].RecentActions.append("no lick ass")                      
                $ newgirl["Laura"].DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call LauraFace("sexy")           
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                    ch_l "Ok, you're probably right. . ."      
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    jump Laura_LA_Prep
                else:   
                    call LauraFace("sexy") 
                    ch_l "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Laura", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                    call LauraFace("sad")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)                 
                    ch_l "Suit yourself."  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Laura"].Forced = 1
                    jump Laura_LA_Prep
                else:                              
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -15)  
                    call LauraFace("angry", 1)
                    "She shoves your head back."   
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")   
                    
    if "no lick ass" in newgirl["Laura"].DailyActions:
        ch_l "I don't like to repeat myself, [newgirl[Laura].Petname]."   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif newgirl["Laura"].Forced:
        call LauraFace("angry", 1)
        ch_l "I don't think so."
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10) if newgirl["Laura"].Inbt > 50 else Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 3) 
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)   
        $ newgirl["Laura"].RecentActions.append("angry")
        $ newgirl["Laura"].DailyActions.append("angry")   
    elif Taboo:
        call LauraFace("angry", 1)    
        $ newgirl["Laura"].RecentActions.append("tabno")                   
        $ newgirl["Laura"].DailyActions.append("tabno") 
        ch_l "I try to stay off the radar."                   
    elif newgirl["Laura"].LickA:
        call LauraFace("sad") 
        ch_l "Sorry, no more of that."    
    else:
        call LauraFace("surprised")
        ch_l "I'm sorry, not now."
        call LauraFace
    $ newgirl["Laura"].RecentActions.append("no lick ass")                      
    $ newgirl["Laura"].DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label Laura_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not newgirl["Laura"].Forced and Situation != "auto":
        $ Tempmod = 0
        if newgirl["Laura"].Legs == "pants":
            $ Tempmod = 15
        call Laura_Bottoms_Off
        if "angry" in newgirl["Laura"].RecentActions:
            return    
    $ Tempmod = 0  
    call Laura_Pussy_Launch("lick ass")
    if not newgirl["Laura"].LickA:        
        if newgirl["Laura"].Forced:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -30)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 40)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 80) 
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 35)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 25)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 55)
    if Taboo:
        $ newgirl["Laura"].Inbt += int(Taboo/10)  
        $ newgirl["Laura"].Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ newgirl["Laura"].Upskirt = 1
    if newgirl["Laura"].Legs == "skirt":
        $ newgirl["Laura"].SeenPanties = 1
    if not newgirl["Laura"].Panties:
        call Laura_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no lick ass")
    
    $ newgirl["Laura"].RecentActions.append("lick") if "lick" not in newgirl["Laura"].RecentActions else newgirl["Laura"].RecentActions
    $ newgirl["Laura"].RecentActions.append("ass") if "ass" not in newgirl["Laura"].RecentActions else newgirl["Laura"].RecentActions
    $ newgirl["Laura"].RecentActions.append("lick ass")  
    
    $ newgirl["Laura"].DailyActions.append("lick") if "lick" not in newgirl["Laura"].DailyActions else newgirl["Laura"].RecentActions
    $ newgirl["Laura"].DailyActions.append("ass") if "ass" not in newgirl["Laura"].DailyActions else newgirl["Laura"].RecentActions                    
    $ newgirl["Laura"].DailyActions.append("lick ass")  
label Laura_LA_Cycle: #Repeating strokes
    if Trigger2 == "kiss you":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Laura") 
        call Laura_Pussy_Launch("lick ass")
        call LauraLust   
        
        if  P_Focus < 100:                                                   
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass
                                                              
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_LA_Cycle  
                                    
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
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:                                                             
                                                        "Switch to fondling.":
                                                                $ Situation = "pullback"
                                                                call Laura_LA_After
                                                                call Laura_Fondle_Ass
                                                        "I want to stick a finger in.":
                                                                $ Situation = "shift"
                                                                call Laura_LA_After
                                                                call Laura_Insert_Ass                 
                                                        "Just stick a finger in [[without asking].":
                                                                $ Situation = "auto"
                                                                call Laura_LA_After
                                                                call Laura_Insert_Ass                        
                                                        "I want to stick a dildo in.":
                                                                $ Situation = "shift"
                                                                call Laura_LA_After
                                                                call Laura_Dildo_Ass  
                                                        "Never Mind":
                                                                jump Laura_LA_Cycle
                                            else: 
                                                ch_l "Maybe we could finish this up for now?"           
                                    
                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Laura_LA_After
                                                call Laura_Offhand_Set   
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass
                                    
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura") 
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0   
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_LA_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_LA_Cycle 
                                            "Never mind":
                                                        jump Laura_LA_Cycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_LA_Cycle 
                                                   
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Laura_LA_After
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump Laura_LA_After
        #End menu (if Line)
        
        if newgirl["Laura"].Panties or newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 5: #This checks if Laura wants to strip down.
                call Laura_Undress("auto")
                
        call Shift_Focus("Laura")    
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1   
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100: 
                    #If either of you could cum   
                    if P_Focus >= 100:    
                            #If you can cum:                                                 
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_LA_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:  
                            #If Laura can cum                                             
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_LA_After
                       
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
                                            jump Laura_LA_After    
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                    
        if newgirl["Laura"].SEXP >= 100 or ApprovalCheck("Laura", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Laura"].LickA):
                    $ newgirl["Laura"].Brows = "confused"
                    ch_l "You seem to be enjoying yourself. . ."  
        elif newgirl["Laura"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Laura"].LickA) and newgirl["Laura"].SEXP >= 15 and not ApprovalCheck("Laura", 1500):
                    $ newgirl["Laura"].Brows = "confused"        
                    menu:
                        ch_l "[newgirl[Laura].Petname], could we try something different?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Laura_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Laura_LA_After
                        "No, this is fun.":   
                                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "O"):                        
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    call LauraFace("angry", 1)   
                                    call Laura_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_l "I'm kinda bored here."                         
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -4, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, -1, 1)                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1, 1)  
                                    $ newgirl["Laura"].RecentActions.append("angry")
                                    $ newgirl["Laura"].DailyActions.append("angry")   
                                    jump Laura_LA_After
        #End Count check
           
        if Round == 10:
            ch_l "It's getting late, we should wrap this up."  
        elif Round == 5:
            ch_l "Tic tock, [newgirl[Laura].Petname]."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], breaktime."
    
label Laura_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Laura_Pos_Reset
        
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].LickA += 1  
    $ newgirl["Laura"].Action -=1      
    if newgirl["Laura"].Legs != "pants" or newgirl["Laura"].Upskirt:        
        $ newgirl["Laura"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Laura"].Addictionrate += 1
    
    call Partner_Like("Laura",2)
     
    if newgirl["Laura"].LickA == 1:            
            $ newgirl["Laura"].SEXP += 15         
            if not Situation: 
                if newgirl["Laura"].Love >= 500 and "unsatisfied" not in newgirl["Laura"].RecentActions:
                    ch_l "That was. . . interesting."
                elif newgirl["Laura"].Obed <= 500 and P_Focus <= 20:
                    call LauraFace("perplexed", 1)
                    ch_l "Was that good for you?"
     
    $ Tempmod = 0  
#    if Situation == "shift":
#        ch_l "Oh? What did you have in mind?"
    call Checkout
    return   

# end newgirl["Laura"].Lick Ass /////////////////////////////////////////////////////////////////////////////

