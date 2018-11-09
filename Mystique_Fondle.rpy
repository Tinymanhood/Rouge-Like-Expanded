# Mystique_Massage /////////////////////////////////////////////////////////////////////////////
label Mystique_Massage:
    call Shift_Focus("Mystique")
    $ Tempmod = 0    
    
    $ Approval = ApprovalCheck("Mystique", 500, TabM = 2) # 95, 110, 125 -120(215)
    
    if Approval >= 2:             
        call MystiqueFace("bemused", 1)
        if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
        ch_m "I could use it, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
        jump Mystique_Massage_Prep
        
    else:
        call MystiqueFace("angry", 1)
        if "no massage" in newgirl["Mystique"].RecentActions:  
            ch_m "I only {i}just{/i} refused you, [newgirl[Mystique].Petname]."
        elif "no massage" in newgirl["Mystique"].DailyActions:       
            ch_m "I told you \"no\" earlier, [newgirl[Mystique].Petname]."
        else:
            call MystiqueFace("bemused")
            ch_m "I'm not interested at the moment, [newgirl[Mystique].Petname]."   
        menu:
            extend ""
            "Sorry, never mind." if "no massage" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Don't concern yourself, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no massage" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "Perhaps."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 20, 1)
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)  
                $ newgirl["Mystique"].RecentActions.append("no massage")                      
                $ newgirl["Mystique"].DailyActions.append("no massage")            
                return                
            "Come on, Please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                    ch_m "I do have some tension built up. . ."                
                    jump Mystique_Massage_Prep
                else:   
                    call MystiqueFace("sly", Brows="confused") 
                    ch_m "No." 
    
    if "no massage" in newgirl["Mystique"].DailyActions:
        ch_m "I've made myself clear on this, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "You'll have to keep your hands limber for yourself."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        ch_m "I can't been seen doing that with you."                  
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "I really can't."    
    $ newgirl["Mystique"].RecentActions.append("no massage")                      
    $ newgirl["Mystique"].DailyActions.append("no massage") 
    $ Tempmod = 0    
    return

label Mystique_Massage_Prep:
    call Mystique_Top_Off("massage")
    if "angry" in newgirl["Mystique"].RecentActions:
        return    
    
label Mystique_Massage_Cycle: 
    $ newgirl["Mystique"].RecentActions.append("massage")                      
    $ newgirl["Mystique"].DailyActions.append("massage") 
        
    "You massage her back and shoulders."
    if not newgirl["Mystique"].Over:
        $ D20 = renpy.random.randint(10, 20)
        $ Round -= D20 if Round > D20 else (Round-1)
        $ newgirl["Mystique"].Addict -= D20 if newgirl["Mystique"].Addict > D20 else newgirl["Mystique"].Addict
            
    ch_m "That was very. . . pleasant, [newgirl[Mystique].Petname]"
    if "massage" not in newgirl["Mystique"].RecentActions:        
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 2)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
    return

# end Mystique_Massage /////////////////////////////////////////////////////////////////////////////

# Mystique_Fondle /////////////////////////////////////////////////////////////////////////////
label Mystique_Fondle:
    
    $ newgirl["Mystique"].Mouth = "smile"
    if not newgirl["Mystique"].Action:
        ch_m "Sorry, i'm really tired right now, [newgirl[Mystique].Petname], raincheck?"
        return
    menu:
        ch_m "Well? Where do you want to touch me, [newgirl[Mystique].Petname]?"
        "Your breasts?" if newgirl["Mystique"].Action:
                jump Mystique_Fondle_Breasts
        "Your thighs?" if newgirl["Mystique"].Action:
                jump Mystique_Fondle_Thighs
        "Your pussy?" if newgirl["Mystique"].Action:
                jump Mystique_Fondle_Pussy
        "Your Ass?" if newgirl["Mystique"].Action:
                jump Mystique_Fondle_Ass
        "Never mind.":
                return
    return


# Mystique_Fondle Breasts /////////////////////////////////////////////////////////////////////////////
label Mystique_Fondle_Breasts:
    call Shift_Focus("Mystique")
    
    # Will she let you fondle? Modifiers
    if newgirl["Mystique"].FondleB: #You've done it before
        $ Tempmod += 15
    if newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 20
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 20
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle breasts" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle breasts" in newgirl["Mystique"].RecentActions else 0        
        
    $ Approval = ApprovalCheck("Mystique", 950, TabM = 3) # 95, 110, 125 -120(215)
    
    if Situation == "auto":  
        if Approval:
            call MystiqueFace("sexy")       
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)            
            "As you cup her breast, Mystique gently nods."            
            jump Mystique_FB_Prep        
        else:   
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)
            ch_m "Down boy, you were doing so well. . ."
            $ Tempmod = 0
            $ Trigger2 = 0
            return
                    
    # fondle yes:    
    
    if Approval:                                                                       #Second time+ dialog        
        call MystiqueFace("sexy", 1)
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)           
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "This does seem less. . . exposed"   
            
    if "fondle breasts" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_FB_Prep
    elif "fondle breasts" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_m "[Line]"
            
    if Approval >= 2:             
        call MystiqueFace("bemused", 1)
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
        ch_m "That sounds lovely, ravish me."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
        jump Mystique_FB_Prep
        
    else:
        call MystiqueFace("angry", 1)
        if "no fondle breasts" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no fondle breasts" in newgirl["Mystique"].DailyActions:  
            ch_m "You've been warned." 
        elif "no fondle breasts" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].FondleB:
            call MystiqueFace("bemused")
            ch_m "I don't think you are worthy now, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "You wish."   
        menu:
            extend ""
            "Sorry, never mind." if "no fondle breasts" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Don't concern yourself, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no fondle breasts" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                "She re-adjusts her cleavage."
                ch_m "Well, I can't rule it out. . ."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no fondle breasts")                      
                $ newgirl["Mystique"].DailyActions.append("no fondle breasts")            
                return                
            "Come on, Please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                    ch_m "Oh i can't resist to your begging, [newgirl[Mystique].Petname]!"                
                    jump Mystique_FB_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "This wasn't a \"tone\" issue." 
            
            
            "[[Grab her chest anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Mystique", 350, "OI", TabM = 3) # 35, 50, 65
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)                 
                    ch_m "That is not appropriate. . ."
                    ch_m "but neither is it entirely unwelcome. . ."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)   
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_FB_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)  
                    call MystiqueFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    if "no fondle breasts" in newgirl["Mystique"].DailyActions:
        ch_m "You need to pay attention when I speak to you."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Don't push your luck."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")                   
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I can't been seen doing that with you."                   
    elif newgirl["Mystique"].FondleB:
        call MystiqueFace("sad")
        ch_m "I'm afraid you haven't earned back my good graces."        
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "No."    
    $ newgirl["Mystique"].RecentActions.append("no fondle breasts")                      
    $ newgirl["Mystique"].DailyActions.append("no fondle breasts") 
    $ Tempmod = 0   
    return 
            
   
label Mystique_FB_Prep: #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle breasts" 
        return
        
    if Trigger2 == "fondle breasts": 
        return
    
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Mystique_Top_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return
        
    $ Tempmod = 0  
    call Mystique_Breasts_Launch("fondle breasts")
    if not newgirl["Mystique"].FondleB:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 5)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
            
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
    call DrainWord("Mystique","no fondle breasts")
    $ newgirl["Mystique"].RecentActions.append("fondle breasts")                      
    $ newgirl["Mystique"].DailyActions.append("fondle breasts") 
    
label Mystique_FB_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Breasts_Launch("fondle breasts")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].FondleB):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "They really are magnificent, aren't they?" 
        elif newgirl["Mystique"].Lust >= 85:
                    pass  
        elif Cnt == (15 + newgirl["Mystique"].FondleB) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused" 
                    menu:
                        ch_m "Perhaps we could try something else, [newgirl[Mystique].Petname]?"
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_FB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_FB_After
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
                                    ch_m "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_FB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                     
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_FB_Cycle  
                                
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
                            if newgirl["Mystique"].Action and MultiAction:
                                menu:
                                    "Ask to suck on them.":
                                            if newgirl["Mystique"].Action and MultiAction:                        
                                                $ Situation = "shift"
                                                call Mystique_FB_After
                                                call Mystique_Suck_Breasts
                                            else:
                                                ch_m "I could use a break, are you about finished here?"
                                    "Just suck on them without asking.":
                                            if newgirl["Mystique"].Action and MultiAction:                            
                                                $ Situation = "auto"
                                                call Mystique_FB_After
                                                call Mystique_Suck_Breasts
                                            else:
                                                "As you lean in to suck on her breast, she grabs your head and pushes back."
                                                ch_m "I could use a break, are you about finished here?"
                                            
                                    "Never Mind":
                                            pass
                            else:
                                ch_m "I could use a break, are you about finished here?" 
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_FB_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_FB_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_FB_After
        #End menu (if Line)
        
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
                                jump Mystique_FB_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_FB_After
                       
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
                                    jump Mystique_FB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_FB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].FondleB += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].FondleB == 1:            
            $ newgirl["Mystique"].SEXP += 4         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "I'm sure it exceeded your expectations. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Well you certainly hit the jackpot."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   

# End Fondle Breasts


# R Suck Breasts /////////////////////////////////////////////////////////////////////////////

label Mystique_Suck_Breasts:
    call Shift_Focus("Mystique")
                                                                                        # Will she let you suck? Modifiers
    if newgirl["Mystique"].SuckB: #You've done it before
        $ Tempmod += 15
    if not newgirl["Mystique"].Chest and not newgirl["Mystique"].Over:
        $ Tempmod += 15
    if newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 20
    if newgirl["Mystique"].Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no suck breasts" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no suck breasts" in newgirl["Mystique"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Mystique", 1050, TabM = 4) # 105, 120, 135, Taboo -160(265)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call MystiqueFace("sexy")       
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)            
            "As you dive in, Mystique seems a bit surprised, but just \"moans.\" a little!"               
            jump Mystique_SB_Prep      
        else:               
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)
            ch_m "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
    
    if "suck breasts" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_SB_Prep
    elif "suck breasts" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_m "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call MystiqueFace("bemused", 1)
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
        ch_m "Oh very well. . ."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
        jump Mystique_SB_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no suck breasts" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no suck breasts" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you I couldn't be seen like that." 
        elif "no suck breasts" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].SuckB:
            call MystiqueFace("bemused")
            ch_m "Let's work up to that, perhaps. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no suck breasts" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "No offense taken. I get it."              
                return
            "Maybe later?" if "no suck breasts" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "I'll give it some thought, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no suck breasts")                      
                $ newgirl["Mystique"].DailyActions.append("no suck breasts")            
                return
            "Come on, Please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                    ch_m "Well, if you insist. . ."                
                    jump Mystique_SB_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "This wasn't a \"tone\" issue."     
            
            "[[Start sucking anyway]":                                               # Pressured into licking. 
                $ Approval = ApprovalCheck("Mystique", 450, "OI", TabM = 3) # 45, 60, 75, -120(165)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)                 
                    ch_m "You'd better shower them with praise. . ."                         
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_SB_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)  
                    call MystiqueFace("angry", 1)
                    "She shoves your head back out."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no suck breasts" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Not worth it."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:   
        call MystiqueFace("angry", 1)      
        $ newgirl["Mystique"].RecentActions.append("tabno")    
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].SuckB:
        call MystiqueFace("sad")
        ch_m "I am sorry about that, but perhaps later?"            
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "No."
    $ newgirl["Mystique"].RecentActions.append("no suck breasts")                      
    $ newgirl["Mystique"].DailyActions.append("no suck breasts") 
    $ Tempmod = 0    
    return
         

label Mystique_SB_Prep:                                                                 #Animation set-up 
            
    if Trigger2 == "suck breasts":
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0   
        call Mystique_Top_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return
    
    $ Tempmod = 0      
    call Mystique_Breasts_Launch("suck breasts")
    if not newgirl["Mystique"].SuckB:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -25)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 17) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
    
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
    call DrainWord("Mystique","no suck breasts")
    $ newgirl["Mystique"].RecentActions.append("suck breasts")                      
    $ newgirl["Mystique"].DailyActions.append("suck breasts") 
    
label Mystique_SB_Cycle: #Repeating strokes  
    if Trigger2 == "kissing":
            $ Trigger2 = 0 
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Breasts_Launch("suck breasts")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].SuckB):
                    $ newgirl["Mystique"].Brows = "sly"
                    ch_m "Lovely, aren't they?"   
        elif newgirl["Mystique"].Lust >= 85:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].SuckB) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_SB_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_SB_After
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
                                    ch_m "You may be enjoying yourself, but I'm getting a bit sore."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_SB_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                   
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_SB_Cycle  
                                
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
                                    
                        "Pull back to fondling.":  
                            if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "pullback"
                                call Mystique_SB_After
                                call Mystique_Fondle_Breasts
                            else:
                                "As you pull back, Mystique pushes you back in close."
                                ch_m "I could use a break, are you about finished here?"
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_SB_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_SB_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_SB_After
        #End menu (if Line)
        
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
                                jump Mystique_SB_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_SB_After
                       
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
                                    jump Mystique_SB_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_SB_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].SuckB += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].SuckB == 1:            
            $ newgirl["Mystique"].SEXP += 4         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "Delectable , weren't they."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Did you get enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   
    
# End Suck breasts    

# Fondle Thighs start //////////////////////////////////////////

label Mystique_Fondle_Thighs:
    call Shift_Focus("Mystique")
                                                                                        # Will she let you fondle her thighs? Modifiers
    if newgirl["Mystique"].FondleT: #You've done it before
        $ Tempmod += 10
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 5    
    if newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 10    
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += Taboo   
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25 
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount      
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle thighs" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle thighs" in newgirl["Mystique"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Mystique", 750, TabM=1) # 75, 90, 105, Taboo -40(105)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call MystiqueFace("sexy")       
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)            
            "As you caress her thigh, Mystique glances at you, and smiles."             
            jump Mystique_FT_Prep      
        else:               
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)
            ch_m "Perhaps we keep it above the waist, [newgirl[Mystique].Petname]."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call MystiqueFace("surprised")    
        $ newgirl["Mystique"].Brows = "sad"
        if newgirl["Mystique"].Lust > 60:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
        "As you pull back, Mystique looks a little sad."              
        jump Mystique_FT_Prep  
    elif "fondle thighs" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_FT_Prep
    elif "fondle thighs" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)       
        ch_m "You didn't get enough earlier?"
    
    if Approval >= 2:                                                                   #She's into it. . .
        call MystiqueFace("bemused", 1)
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
        ch_m "Ok [newgirl[Mystique].Petname], go ahead."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
        jump Mystique_FT_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no fondle thighs" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no fondle thighs" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you not to touch me like that in public!" 
        elif "no fondle thighs" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].FondleT:
            call MystiqueFace("bemused")
            ch_m "Seems a bit forward, [newgirl[Mystique].Petname]."
        else:
            call MystiqueFace("bemused")
            ch_m "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle thighs" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint."             
                return
            "Maybe later?" if "no fondle thighs" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "Perhaps."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)    
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no fondle thighs")                      
                $ newgirl["Mystique"].DailyActions.append("no fondle thighs")            
                return
            "Come on, Please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
                    ch_m "Politeness can be rewarded. . ."             
                    jump Mystique_FT_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "This wasn't a \"tone\" issue."     
            
            "[[Start caressing her thigh anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Mystique", 350, "OI", TabM = 2) # 35, 50, 65, -80(105)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)                 
                    ch_m "Hmmph."                         
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_FT_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)  
                    call MystiqueFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no fondle thighs" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Don't push your luck."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 2)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1)   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")          
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].FondleT:
        call MystiqueFace("sad")
        ch_m "Hands."            
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "No."
    $ newgirl["Mystique"].RecentActions.append("no fondle thighs")                      
    $ newgirl["Mystique"].DailyActions.append("no fondle thighs") 
    $ Tempmod = 0    
    return
    
label Mystique_FT_Prep:                                                                 #Animation set-up 
    if Trigger == "kissing": 
        $ Trigger = "fondle thighs" 
        return
        
    if Trigger2 == "fondle thighs": 
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Mystique_Bottoms_Off 
        if "angry" in newgirl["Mystique"].RecentActions:
            return 
            
    $ Tempmod = 0    
    call Mystique_Pussy_Launch("fondle thighs")
    if not newgirl["Mystique"].FondleT:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 15)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 5)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
            
    if Taboo:               
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, (int(Taboo/5)))                               
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 200, (2*(int(Taboo/5))))
     
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0 
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no fondle thighs")
    $ newgirl["Mystique"].RecentActions.append("fondle thighs")                      
    $ newgirl["Mystique"].DailyActions.append("fondle thighs")  
    
label Mystique_FT_Cycle:                                                                #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("fondle thighs")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].FondleT):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Luxurious, yes?"   
        elif Cnt == (15 + newgirl["Mystique"].FondleT) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_FT_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_FT_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_FT_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                       
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_FT_Cycle  
                                
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
                                    
                        "Can I do a little deeper?":
                                if newgirl["Mystique"].Action and MultiAction:
                                    $ Situation = "shift"
                                    call Mystique_FT_After
                                    call Mystique_Fondle_Pussy                
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        "Shift your hands a bit higher without asking":
                                if newgirl["Mystique"].Action and MultiAction:
                                    $ Situation = "auto"
                                    call Mystique_FT_After
                                    call Mystique_Fondle_Pussy    
                                else:
                                    "As your hands creep upwards, she grabs your wrists."
                                    ch_m "I could use a break, are you about finished here?" 
                
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_FT_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                                    
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_FT_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_FT_After
        #End menu (if Line)
        
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
                                jump Mystique_FT_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_FT_After
                       
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
                                    jump Mystique_FT_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_FT_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].FondleT += 1  
    $ newgirl["Mystique"].Action -=1
    if newgirl["Mystique"].Legs != "pants" or newgirl["Mystique"].Upskirt:        
        $ newgirl["Mystique"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].FondleT == 1:            
            $ newgirl["Mystique"].SEXP += 3         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was. . . pleasant."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Was that enough?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   
    
# ////////////////////////////////////////////////////////////////////////Start Fondle Pussy    
label Mystique_Fondle_Pussy:
    call Shift_Focus("Mystique")
                                                                                        # Will she let you fondle? Modifiers
    if newgirl["Mystique"].FondleP: #You've done it before
        $ Tempmod += 20
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 10    
    if newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 15
    if newgirl["Mystique"].Lust > 75 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (2*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle pussy" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle pussy" in newgirl["Mystique"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Mystique", 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:
            call MystiqueFace("sexy")       
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2)
            "As your hand creeps up her thigh, Mystique seems a bit surprised, but then nods."            
            jump Mystique_FP_Prep      
        else:               
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)
            ch_m "Down boy, you were doing so well. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call MystiqueFace("surprised")   
        $ newgirl["Mystique"].Brows = "sad"        
        if newgirl["Mystique"].Lust > 80:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -4)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
        "As your hand pulls out, Mystique gasps and looks upset."              
        jump Mystique_FP_Prep     
    elif "fondle pussy" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_FP_Prep
    elif "fondle pussy" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Take it a bit gently, I'm still shaking from earlier.",
            "Mmm. . ."]) 
        ch_m "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .
        call MystiqueFace("bemused", 1)
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
        ch_m "Mmmm, I couldn't refuse. . ."   
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
        jump Mystique_FP_Prep   
        
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no fondle pussy" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no fondle pussy" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you not to touch me like that in public!" 
        elif "no fondle pussy" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].FondleP:
            call MystiqueFace("bemused")
            ch_m "I don't think we're there yet, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "You wish."  
        menu:
            extend ""
            "Sorry, never mind." if "no fondle pussy" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no fondle pussy" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "I'll give it some thought, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no fondle pussy")                      
                $ newgirl["Mystique"].DailyActions.append("no fondle pussy")            
                return
            "Come on, Please?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    ch_m "I enjoy hearing you beg, [newgirl[Mystique].Petname]!"                
                    jump Mystique_FP_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "No."
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Mystique", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Oh, if you insist. . ."
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_FP_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)  
                    call MystiqueFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no fondle pussy" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I don't think so, [newgirl[Mystique].Petname]."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 70, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")                   
        $ newgirl["Mystique"].DailyActions.append("tabno")
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].FondleP:
        call MystiqueFace("sad")
        ch_m "Sorry, keep your hands out of there."           
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "No thank you, [newgirl[Mystique].Petname]."
    $ newgirl["Mystique"].RecentActions.append("no fondle pussy")                      
    $ newgirl["Mystique"].DailyActions.append("no fondle pussy") 
    $ Tempmod = 0    
    return
                    
label Mystique_FP_Prep: #Animation set-up 
    if Trigger2 == "fondle pussy":
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Mystique_Bottoms_Off   
        if "angry" in newgirl["Mystique"].RecentActions:
            return 
    $ Tempmod = 0
    
    call Mystique_Pussy_Launch("fondle pussy")
    if not newgirl["Mystique"].FondleP:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -50)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 35)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 25) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
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
    call DrainWord("Mystique","no fondle pussy")
    $ newgirl["Mystique"].RecentActions.append("fondle pussy")                      
    $ newgirl["Mystique"].DailyActions.append("fondle pussy") 
    
    $ Speed = 1
    
label Mystique_FP_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("fondle pussy")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].FondleP):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "You like how that feels, huh?"  
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].FondleP) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "You certainly seem to be enjoying yourself, but perhaps we could add some variety?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_FP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_FP_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_FP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                        
                        "I want to stick a finger in. . ." if Speed != 2:
                            if newgirl["Mystique"].InsertP: 
                                $ Speed = 2
                            else:
                                menu:                                
                                    "Ask her first":
                                        $ Situation = "shift"
                                    "Don't ask first [[just stick it in]":                                    
                                        $ Situation = "auto"
                                call Mystique_Insert_Pussy  
                       
                        "Pull back to fondling" if Speed == 2:
                                $ Speed = 1   
                                      
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_FP_Cycle  
                                
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
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:                                                                                         
                                            "I want to lick your pussy.":
                                                    $ Situation = "shift"
                                                    call Mystique_FP_After
                                                    call Mystique_Lick_Pussy                 
                                            "Just start licking":
                                                    $ Situation = "auto"
                                                    call Mystique_FP_After
                                                    call Mystique_Lick_Pussy         
                                            "Pull back to the thighs":
                                                    $ Situation = "pullback"
                                                    call Mystique_FP_After
                                                    call Mystique_Fondle_Thighs
#                                            "I want to stick a dildo in.":
#                                                    call Mystique_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call Mystique_FP_After
#                                                        call Mystique_Dildo_Pussy  
#                                                    else:
#                                                        jump Mystique_FP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_m "I could use a break, are you about finished here?"           
                                        
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_FP_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_FP_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_FP_After
        #End menu (if Line)
        
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
                                jump Mystique_FP_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_FP_After
                       
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
                                    jump Mystique_FP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_FP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].FondleP += 1  
    $ newgirl["Mystique"].Action -=1
    if newgirl["Mystique"].Legs != "pants" or newgirl["Mystique"].Upskirt:        
        $ newgirl["Mystique"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].FondleP == 1:            
            $ newgirl["Mystique"].SEXP += 7         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "I do appreciate some rather. . . aggressive attention down there."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Did you find what you were looking for?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   

# end Mystique_Fondle Pussy /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Mystique_Insert_Pussy:
    call Shift_Focus("Mystique")
    if Situation == "auto":                                                                  #You auto-start                    
        if ApprovalCheck("Mystique", 1100, TabM = 2):
            call MystiqueFace("surprised")       
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
            "As you slide a finger in, Mystique seems a bit surprised, but seems into it."              
            jump Mystique_IP_Prep
        else:   
            call MystiqueFace("surprised",2)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
            ch_m "Oooh!"
            "She slaps your hand back."
            call MystiqueFace("perplexed",1)
            ch_m "Careful what you put in there, you may not get it back."
            return            
    
    if ApprovalCheck("Mystique", 1100, TabM = 2):                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "If you must. . ."    
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            ch_m "Mmmmmm. . ."                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_IP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .  
        call MystiqueFace("bemused", 2)
        ch_m "No. Thank you."
        $ newgirl["Mystique"].Blush = 1
    return
    
                
label Mystique_IP_Prep: #Animation set-up     
    if not newgirl["Mystique"].InsertP:
        $ newgirl["Mystique"].InsertP = 1
        $ newgirl["Mystique"].SEXP += 10          
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -60)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 55)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 25)
                
    if not newgirl["Mystique"].Forced and Situation != "auto":        
        call Mystique_Undress("bottom")
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
            
#    call Mystique_Pussy_Launch("insert pussy")
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
        
    $ Line = 0 
    $ Cnt = 0     
    $ Speed = 2
    return

# end newgirl["Mystique"].Insert Pussy /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Pussy    
label Mystique_Lick_Pussy: 
    call Shift_Focus("Mystique")
                                                                                  # Will she let you fondle? Modifiers     
    if newgirl["Mystique"].LickP: #You've done it before
        $ Tempmod += 15
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 15  
    if newgirl["Mystique"].Lust > 95:
        $ Tempmod += 20  
    elif newgirl["Mystique"].Lust > 85: #She's really horny
        $ Tempmod += 15
    if Situation == "shift":
        $ Tempmod += 10
    if newgirl["Mystique"].Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount     
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no lick pussy" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick pussy" in newgirl["Mystique"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Mystique", 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
            "As you crouch down and start to lick her pussy, Mystique jumps, but then softens."  
            call MystiqueFace("sexy")           
            jump Mystique_LP_Prep
        else:   
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
            ch_m "I like where your head is at, so to speak, but perhaps hold off on that." 
            call MystiqueFace("perplexed",1)
            "She pushes your head back away from her."
            $ Tempmod = 0
            $ Trigger2 = 0
            return            
    
    if "lick pussy" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_LP_Prep
    elif "lick pussy" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "Just what i deserve. . .",
            "Mmm. . ."]) 
        ch_m "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "If you must. . ."    
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Eyes = "closed"            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)            
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)
            ch_m "Mmmmmm. . ."                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_LP_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no lick pussy" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no lick pussy" in newgirl["Mystique"].DailyActions:  
            ch_m "You already got your answer!" 
        elif "no lick pussy" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].LickP:
            call MystiqueFace("bemused")
            ch_m "I'm not sure we're at that stage, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "I'm really not comfortable with that. . ." 
        menu:
            extend ""
            "Sorry, never mind." if "no lick pussy" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint, [newgirl[Mystique].Petname]."              
                return            
            "I'm sure I can convince you later. . ." if "no lick pussy" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "I'll be thinking about it, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no lick pussy")                      
                $ newgirl["Mystique"].DailyActions.append("no lick pussy")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call MystiqueFace("sexy")           
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    ch_m "You present a compelling case. . ."      
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                    jump Mystique_LP_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "I would, but still no, [newgirl[Mystique].Petname]."    
            
            "[[Get in there anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Mystique", 750, "OI", TabM = 4) # 75, 90, 105, -160(235)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "If you insist. . ."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_LP_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)  
                    call MystiqueFace("angry", 1)
                    "She shoves your head back."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no lick pussy" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I really can't, [newgirl[Mystique].Petname]."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)     
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")                   
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].LickP:
        call MystiqueFace("sad") 
        ch_m "Keep your head out of there."    
    else:
        call MystiqueFace("surprised")
        ch_m "I know, I'm as disappointed as you are."
        call MystiqueFace
    $ newgirl["Mystique"].RecentActions.append("no lick pussy")                      
    $ newgirl["Mystique"].DailyActions.append("no lick pussy") 
    $ Tempmod = 0    
    return
    
label Mystique_LP_Prep: #Animation set-up  
    if Trigger2 == "lick pussy": #fix pull down pants now an option, make it work
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        if newgirl["Mystique"].Legs == "pants":
            $ Tempmod = 15
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return  
            
    $ Tempmod = 0      
    call Mystique_Pussy_Launch("lick pussy")
    if not newgirl["Mystique"].LickP:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -30)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 35)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 75) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 35)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 15)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35)
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
        
    if newgirl["Mystique"].Legs == "skirt":
        $ newgirl["Mystique"].Upskirt = 1  
        $ newgirl["Mystique"].SeenPanties = 1
    if not newgirl["Mystique"].Panties:
        call Mystique_First_Bottomless(1)
    
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no lick pussy")
    $ newgirl["Mystique"].RecentActions.append("lick pussy")                      
    $ newgirl["Mystique"].DailyActions.append("lick pussy") 
    
label Mystique_LP_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("lick pussy")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].LickP):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "You like my taste right?"  
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].LickP) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], I know you're having fun down there, but maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_LP_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_LP_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_LP_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                                  
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_LP_Cycle  
                                
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
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    if newgirl["Mystique"].Action and MultiAction:
                                                        $ Situation = "pullback"
                                                        call Mystique_LP_After
                                                        call Mystique_Fondle_Pussy
                                                    else:
                                                        ch_m "I could use a break, are you about finished here?"  
#                                            "I want to stick a dildo in.":
#                                                    call Mystique_Dildo_Check
#                                                    if _return:
#                                                        $ Situation = "shift"
#                                                        call Mystique_LP_After
#                                                        call Mystique_Dildo_Pussy  
#                                                    else:
#                                                        jump Mystique_LP_Cycle   
                                            "Never Mind":
                                                    pass
                                else:
                                    ch_m "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_LP_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_LP_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_LP_After
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
                                jump Mystique_LP_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_LP_After
                       
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
                                    jump Mystique_LP_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_LP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].LickP += 1  
    $ newgirl["Mystique"].Action -=1     
    if newgirl["Mystique"].Legs != "pants" or newgirl["Mystique"].Upskirt:        
        $ newgirl["Mystique"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 3 if R_LikeNewGirl["Mystique"] >= 800 else 2
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].LickP == 1:            
            $ newgirl["Mystique"].SEXP += 10         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "I could really take advantage of your services more often. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "I suppose that worked out for both of us. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   


# end newgirl["Mystique"].Lick Pussy /////////////////////////////////////////////////////////////////////////////

    
# ////////////////////////////////////////////////////////////////////////Start Fondle Ass    
label Mystique_Fondle_Ass: 
    call Shift_Focus("Mystique")
                                                                                     # Will she let you fondle? Modifiers
    if newgirl["Mystique"].FondleA: #You've done it before
        $ Tempmod += 10
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 5     
    if newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 15
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += Taboo  
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25 
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount      
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no fondle ass" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no fondle ass" in newgirl["Mystique"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Mystique", 850, TabM=1) # 85, 100, 115, Taboo -40(125)
    
    if Situation == "auto":                                                                  #You auto-start
        if Approval:  
            call MystiqueFace("surprised", 1)  
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
            "As your hand creeps down her backside, Mystique jumps a bit, and then relaxes."              
            call MystiqueFace("sexy")  
            jump Mystique_FA_Prep  
        else:          
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
            ch_m "Hands off, [newgirl[Mystique].Petname]."   
            call MystiqueFace("bemused")
            $ Tempmod = 0
            $ Trigger2 = 0
            return
            
    if Situation == "pullback":     
        call MystiqueFace("surprised")   
        $ newgirl["Mystique"].Brows = "sad"        
        if newgirl["Mystique"].Lust > 80:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -4)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
        "As your finger slides out, Mystique gasps and looks upset."              
        jump Mystique_FA_Prep     
    elif "fondle ass" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_FA_Prep
    elif "fondle ass" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Perhaps not so rough this time?",
            "Mmm. . ."]) 
        ch_m "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .        
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
            ch_m "If you insist. . ."   
        else:
            call MystiqueFace("bemused, 1") 
            ch_m "I can't exactly refuse. . ."   
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
        jump Mystique_FA_Prep
        
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no fondle ass" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no fondle ass" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you not to touch me like that in public!" 
        elif "no fondle ass" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].FondleA:
            call MystiqueFace("bemused")
            ch_m "Not yet, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Let's not, ok [newgirl[Mystique].Petname]?"
        menu:
            extend ""
            "Sorry, never mind." if "no fondle ass" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no fondle ass" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "Perhaps."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)  
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no fondle ass")                      
                $ newgirl["Mystique"].DailyActions.append("no fondle ass")            
                return
            "Just one good squeeze?":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    ch_m "I do enjoy hearing you beg. . ."                           
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    jump Mystique_FA_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "No."     
            
            "[[Start fondling anyway]":                                               # Pressured into fondling. 
                $ Approval = ApprovalCheck("Mystique", 250, "OI", TabM = 3) # 25, 40, 55, -120(145)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -1) 
                    ch_m "Fine, I suppose."                
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3) 
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_FA_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)  
                    call MystiqueFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                        
    if "no fondle ass" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Do you want to keep those fingers?"
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 60, 5)    
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")   
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].FondleA:
        call MystiqueFace("sad")
        ch_m "I'm sorry, keep your hands to yourself."        
    else:
        call MystiqueFace("sexy") 
        $ newgirl["Mystique"].Mouth = "sad"
        ch_m "No."
    $ newgirl["Mystique"].RecentActions.append("no fondle ass")                      
    $ newgirl["Mystique"].DailyActions.append("no fondle ass") 
    $ Tempmod = 0    
    return
        
ch_m "Sorry, I don't even know how I got here. . ."
return

label Mystique_FA_Prep: #Animation set-up  
    if Trigger2 == "fondle ass":
        return
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
    $ Tempmod = 0      
    call Mystique_Pussy_Launch("fondle ass")
    if not newgirl["Mystique"].FondleA:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 15) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 12)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)
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
    call DrainWord("Mystique","no fondle ass")
    $ newgirl["Mystique"].RecentActions.append("fondle ass")                      
    $ newgirl["Mystique"].DailyActions.append("fondle ass") 
    
label Mystique_FA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("fondle ass")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].FondleA):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Mmmm I do enjoy that. . ."  
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].FondleA) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], this is nice, but could we do something else?"                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_FA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_FA_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_FA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_FA_Cycle  
                                
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
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call Mystique_FA_After
                                                    call Mystique_Insert_Ass                 
                                            "Just stick a finger in without asking.":
                                                    $ Situation = "auto"
                                                    call Mystique_FA_After
                                                    call Mystique_Insert_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call Mystique_FA_After
                                                    call Mystique_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call Mystique_FA_After
                                                    call Mystique_Lick_Ass    
#                                            "I want to stick a dildo in.":
#                                                    call Mystique_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call Mystique_FA_After
#                                                        call Mystique_Dildo_Ass  
#                                                    else:
#                                                        jump Mystique_FA_Cycle   
                                            "Never Mind":
                                                        pass              
                                else:
                                    ch_m "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_FA_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_FA_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_FA_After
        #End menu (if Line)
        
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
                                jump Mystique_FA_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_FA_After
                       
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
                                    jump Mystique_FA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_FA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].FondleA += 1  
    $ newgirl["Mystique"].Action -=1            
    if newgirl["Mystique"].Legs != "pants" or newgirl["Mystique"].Upskirt:        
        $ newgirl["Mystique"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].FondleA == 1:            
            $ newgirl["Mystique"].SEXP += 4         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was. . . nice. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Did you enjoy that?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   


# end Mystique_Fondle Ass /////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Mystique_Insert_Ass:
    call Shift_Focus("Mystique")
    
    if newgirl["Mystique"].InsertA: #You've done it before
        $ Tempmod += 25
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 15    
    if newgirl["Mystique"].Lust > 85: #She's really horny
        $ Tempmod += 15
    if newgirl["Mystique"].Lust > 95:
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if newgirl["Mystique"].Lust > 85 and Situation == "auto": #She's really horny
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25 
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no insert ass" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no insert ass" in newgirl["Mystique"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Mystique", 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
            "As you slide a finger in, Mystique tightens around it in surprise, but seems into it."  
            call MystiqueFace("sexy")           
            jump Mystique_IA_Prep
        else:   
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
            ch_m "Hey, back off, [newgirl[Mystique].Petname]."                 
            $ Tempmod = 0
            $ Trigger2 = 0
            return          
    
    if "insert ass" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        $ Line = renpy.random.choice(["You didn't get enough earlier?",
            "Relax, gently. . .",
            "Mmm. . ."]) 
        ch_m "[Line]"
        
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "If you must. . ."    
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Eyes = "closed"            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)            
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)
            ch_m "Mmmmm. . ."                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_IA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry", 1)
        if "no insert ass" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no insert ass" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you that wasn't appropriate!" 
        elif "no insert ass" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].InsertA:
            call MystiqueFace("perplexed", 1)
            ch_m "That's really not my usual style. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "I'd rather not today. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no insert ass" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no insert ass" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "It's. . . possible, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no insert ass")                      
                $ newgirl["Mystique"].DailyActions.append("no insert ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call MystiqueFace("sexy")           
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    ch_m "You're probably right. . ."      
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                    jump Mystique_IA_Prep
                else:   
                    call MystiqueFace("bemused") 
                    ch_m "I don't think that I would."     
            
            "[[Slide a finger in anyway]":                                               # Pressured into being fingered. 
                $ Approval = ApprovalCheck("Mystique", 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):                    
                    call MystiqueFace("surprised", 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Well hello there. . ."                     
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_IA_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)  
                    call MystiqueFace("angry", 1)
                    "She slaps your hand away."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no insert ass" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I'm not going that far today."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 10) if newgirl["Mystique"].Inbt > 50 else Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 3) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)      
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")                   
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].InsertA:
        call MystiqueFace("sad") 
        ch_m "I don't feel like it."    
    else:
        call MystiqueFace("surprised")
        ch_m "Not today, [newgirl[Mystique].Petname]."
        call MystiqueFace
    $ newgirl["Mystique"].RecentActions.append("no insert ass")                      
    $ newgirl["Mystique"].DailyActions.append("no insert ass") 
    $ Tempmod = 0    
    return
    
        
label Mystique_IA_Prep: #Animation set-up 
    if Trigger2 == "insert ass":
        return
        
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
            
    $ Tempmod = 0      
    call Mystique_Pussy_Launch("insert ass")
    if not newgirl["Mystique"].InsertA:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -50)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 60)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 35) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 25)
            
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
    call DrainWord("Mystique","no insert ass")
    $ newgirl["Mystique"].RecentActions.append("insert ass")                      
    $ newgirl["Mystique"].DailyActions.append("insert ass") 
    
label Mystique_IA_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("insert ass")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].InsertA):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Ungh, You're getting going there. . ."  
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].InsertA) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], this is getting kind sore, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_IA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_IA_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_IA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                             
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_IA_Cycle  
                                
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
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:
                                            "Pull out and start rubbing again.":
                                                    $ Situation = "pullback"
                                                    call Mystique_IA_After
                                                    call Mystique_Fondle_Ass
                                            "I want to lick your asshole.":
                                                    $ Situation = "shift"
                                                    call Mystique_IA_After
                                                    call Mystique_Lick_Ass                 
                                            "Just start licking.":
                                                    $ Situation = "auto"
                                                    call Mystique_IA_After
                                                    call Mystique_Lick_Ass    
#                                            "I want to stick a dildo in.":
#                                                    call Mystique_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call Mystique_IA_After
#                                                        call Mystique_Dildo_Ass  
#                                                    else:
#                                                        jump Mystique_IA_Cycle  
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_m "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_IA_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_IA_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_IA_After
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
                                jump Mystique_IA_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_IA_After
                       
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
                                    jump Mystique_IA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_IA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].InsertA += 1  
    $ newgirl["Mystique"].Action -=1            
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].InsertA == 1:            
            $ newgirl["Mystique"].SEXP += 12         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "You certainly surprise me. . ."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Was it everything you dreamed?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   


# end newgirl["Mystique"].Insert Ass /////////////////////////////////////////////////////////////////////////////




# ////////////////////////////////////////////////////////////////////////Start Insert Ass    
label Mystique_Lick_Ass: 
    call Shift_Focus("Mystique")
                                                                             # Will she let you lick? Modifiers         
    if newgirl["Mystique"].LickA: #You've done it before
        $ Tempmod += 20
    if newgirl["Mystique"].Legs == "pants" or HoseNum("Mystique") >= 5: # she's got pants on.
        $ Tempmod -= 25 
    if newgirl["Mystique"].Lust > 95:
        $ Tempmod += 20  
    elif newgirl["Mystique"].Lust > 85: #She's really horny
        $ Tempmod += 15    
    if newgirl["Mystique"].Lust > 85 and Situation == "auto": #auto
        $ Tempmod += 10 
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in newgirl["Mystique"].Traits:
        $ Tempmod += (4*Taboo) 
    if "dating" in newgirl["Mystique"].Traits or "sex friend" in newgirl["Mystique"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Mystique"].Traits:
        $ Tempmod -= 25  
    if newgirl["Mystique"].ForcedCount and not newgirl["Mystique"].Forced:
        $ Tempmod -= 5 * newgirl["Mystique"].ForcedCount 
    
    if Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
        $ Tempmod -= 10 
    if Taboo and "public" not in newgirl["Mystique"].History:                   
        $ Tempmod -= 20 
        
    if "no lick ass" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no lick ass" in newgirl["Mystique"].RecentActions else 0   
            
    $ Approval = ApprovalCheck("Mystique", 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    
    if Situation == "auto":                                                                  #You auto-start                    
        if Approval:            
            call MystiqueFace("surprised")   
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
            "As you crouch down and start to lick her asshole, Mystique startles briefly, but then begins to melt."  
            call MystiqueFace("sexy")  
            jump Mystique_LA_Prep
        else:   
            call MystiqueFace("surprised")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -2)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
            ch_m "[newgirl[Mystique].Petname]! Not now. . ."               
            $ Tempmod = 0
            $ Trigger2 = 0
            return  
    
    if "lick ass" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "Mmmm, again? I suppose. . ."
        jump Mystique_LA_Prep
    elif "lick ass" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("sexy", 1)
        ch_m "You didn't get enough earlier?"
    
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)
            ch_m "If you must. . ."    
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Eyes = "closed"            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)            
            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 3)
            ch_m "I'd rather you didn't."                
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
        jump Mystique_LA_Prep   
    
    else:                                                                               #She's not into it, but maybe. . .           
        call MystiqueFace("angry", 1)
        if "no lick ass" in newgirl["Mystique"].RecentActions:  
            ch_m "Your persistance is doing you no favors, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no lick ass" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you not to touch me like that in public!" 
        elif "no lick ass" in newgirl["Mystique"].DailyActions:       
            ch_m "I believe you know my answer on this matter."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "As I said, not here, [newgirl[Mystique].Petname]."  
        elif not newgirl["Mystique"].LickA:                    #First time dialog
            call MystiqueFace("bemused", 1)
            if newgirl["Mystique"].Love >= newgirl["Mystique"].Obed and newgirl["Mystique"].Love >= newgirl["Mystique"].Inbt:            
                ch_m "Oh, are we there now?"
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:            
                ch_m "Is that what gets you off?"
            else:
                $ newgirl["Mystique"].Eyes = "sexy"
                ch_m "Hm, I didn't know that's what you were into."
        else:
            call MystiqueFace("bemused")
            ch_m "Not now, [newgirl[Mystique].Petname]."  
        menu:
            extend ""
            "Sorry, never mind." if "no lick ass" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "I appreciate your restraint, [newgirl[Mystique].Petname]."              
                return
            "I'm sure I can convince you later. . ." if "no lick ass" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "Anything's possible, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                $ newgirl["Mystique"].RecentActions.append("no lick ass")                      
                $ newgirl["Mystique"].DailyActions.append("no lick ass")            
                return
            "I think you'd really enjoy it. . .":            
                if Approval:
                    call MystiqueFace("sexy")           
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    ch_m "Ok, you're probably right. . ."      
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2)
                    jump Mystique_LA_Prep
                else:   
                    call MystiqueFace("sexy") 
                    ch_m "I really don't think so."        
            
            "[[Start licking anyway]":                                               # Pressured into being licked. 
                $ Approval = ApprovalCheck("Mystique", 1100, "OI", TabM = 4) # 110, 125, 140, -160(270)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Suit yourself."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    if Approval < 2:                          
                        $ newgirl["Mystique"].Forced = 1
                    jump Mystique_LA_Prep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -15)  
                    call MystiqueFace("angry", 1)
                    "She shoves your head back."   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    
    if "no lick ass" in newgirl["Mystique"].DailyActions:
        ch_m "I don't appreciate having to repeat myself, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I don't think so."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 80, 10) if newgirl["Mystique"].Inbt > 50 else Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 50, 3) 
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:
        call MystiqueFace("angry", 1)    
        $ newgirl["Mystique"].RecentActions.append("tabno")                   
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I have a reputation to maintain."                   
    elif newgirl["Mystique"].LickA:
        call MystiqueFace("sad") 
        ch_m "Sorry, no more of that."    
    else:
        call MystiqueFace("surprised")
        ch_m "I'm sorry, not now."
        call MystiqueFace
    $ newgirl["Mystique"].RecentActions.append("no lick ass")                      
    $ newgirl["Mystique"].DailyActions.append("no lick ass") 
    $ Tempmod = 0    
    return
        
label Mystique_LA_Prep: #Animation set-up  
    if Trigger2 == "lick ass":
        return
    if not newgirl["Mystique"].Forced and Situation != "auto":
        $ Tempmod = 0
        if newgirl["Mystique"].Legs == "pants":
            $ Tempmod = 15
        call Mystique_Bottoms_Off
        if "angry" in newgirl["Mystique"].RecentActions:
            return    
    $ Tempmod = 0  
    call Mystique_Pussy_Launch("lick ass")
    if not newgirl["Mystique"].LickA:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -30)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 40)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 80) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 35)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 25)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 55)
    if Taboo:
        $ newgirl["Mystique"].Inbt += int(Taboo/10)  
        $ newgirl["Mystique"].Lust += int(Taboo/5)
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
    
    $ newgirl["Mystique"].Upskirt = 1
    if newgirl["Mystique"].Legs == "skirt":
        $ newgirl["Mystique"].SeenPanties = 1
    if not newgirl["Mystique"].Panties:
        call Mystique_First_Bottomless(1)
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no lick ass")
    
    $ newgirl["Mystique"].RecentActions.append("lick") if "lick" not in newgirl["Mystique"].RecentActions else newgirl["Mystique"].RecentActions
    $ newgirl["Mystique"].RecentActions.append("ass") if "ass" not in newgirl["Mystique"].RecentActions else newgirl["Mystique"].RecentActions
    $ newgirl["Mystique"].RecentActions.append("lick ass")  
    
    $ newgirl["Mystique"].DailyActions.append("lick") if "lick" not in newgirl["Mystique"].DailyActions else newgirl["Mystique"].RecentActions
    $ newgirl["Mystique"].DailyActions.append("ass") if "ass" not in newgirl["Mystique"].DailyActions else newgirl["Mystique"].RecentActions                    
    $ newgirl["Mystique"].DailyActions.append("lick ass")  
label Mystique_LA_Cycle: #Repeating strokes
    if Trigger2 == "kissing":
            $ Trigger2 = 0
    while Round >=0:  
        call Shift_Focus("Mystique") 
        call Mystique_Pussy_Launch("lick ass")
        call MystiqueLust     
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].LickA):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "You certainly are enthusiastic. . ."  
        elif newgirl["Mystique"].Lust >= 80:
                    pass
        elif Cnt == (15 + newgirl["Mystique"].LickA) and newgirl["Mystique"].SEXP >= 15 and not ApprovalCheck("Mystique", 1500):
                    $ newgirl["Mystique"].Brows = "confused"        
                    menu:
                        ch_m "[newgirl[Mystique].Petname], this is getting weird, maybe we could try something else."                         
                        "Finish up.":
                                "You let go. . ."   
                                jump Mystique_LA_After
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                $ Situation = "shift"
                                jump Mystique_LA_After
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
                                    ch_m "Well perhaps you are enjoying yourself, but I'm tired of this."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_LA_After
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Keep going. . .":
                                    pass
                           
                        "Slap her ass":                     
                                call Mystique_Slap_Ass
                                jump Mystique_LA_Cycle  
                                
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
                                if newgirl["Mystique"].Action and MultiAction:
                                        menu:   
                                            "Switch to fondling.":
                                                    $ Situation = "pullback"
                                                    call Mystique_LA_After
                                                    call Mystique_Fondle_Ass
                                            "I want to stick a finger in.":
                                                    $ Situation = "shift"
                                                    call Mystique_LA_After
                                                    call Mystique_Insert_Ass                 
                                            "Just stick a finger in [[without asking].":
                                                    $ Situation = "auto"
                                                    call Mystique_LA_After
                                                    call Mystique_Insert_Ass                        
#                                            "I want to stick a dildo in.":
#                                                    call Mystique_Dildo_Check
#                                                    if Line == "yes":
#                                                        $ Situation = "shift"
#                                                        call Mystique_LA_After
#                                                        call Mystique_Dildo_Ass  
#                                                    else:
#                                                        jump Mystique_LA_Cycle   
                                            "Never Mind":
                                                    pass              
                                else:
                                    ch_m "I could use a break, are you about finished here?"           
                    
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I could use a break, are you about finished here?"  
                        
                        "Shift your focus" if Trigger2:
                                    $ Situation = "shift focus"
                                    call Mystique_LA_After
                                    call Mystique_Offhand_Set   
                        "Shift your focus (locked)" if not Trigger2:
                                    pass
                
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_LA_After
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Pos_Reset
                                    $ Line = 0
                                    jump Mystique_LA_After
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
                                jump Mystique_LA_After 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if newgirl["Mystique"].Lust >= 100:                                               
                        call Mystique_Cumming
                        if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                            jump Mystique_LA_After
                       
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
                                    jump Mystique_LA_After  
        #End orgasm
        
   
        if Round == 10:
            ch_m "It's getting late. . ."  
        elif Round == 5:
            ch_m "We should take a break soon."       
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "We need to stop for a moment, let me catch my breath."
    
    
label Mystique_LA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        call Mystique_Pos_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].LickA += 1  
    $ newgirl["Mystique"].Action -=1      
    if newgirl["Mystique"].Legs != "pants" or newgirl["Mystique"].Upskirt:        
        $ newgirl["Mystique"].Addictionrate += 1
        if "addictive" in P_Traits:
            $ newgirl["Mystique"].Addictionrate += 1
    
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
     
    if newgirl["Mystique"].LickA == 1:            
            $ newgirl["Mystique"].SEXP += 15         
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was. . . invigorating."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    call MystiqueFace("perplexed", 1)
                    ch_m "Was it all you dreamed of?"
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Oh? What did you have in mind?"
    call Checkout
    return   

# end newgirl["Mystique"].Lick Ass /////////////////////////////////////////////////////////////////////////////

