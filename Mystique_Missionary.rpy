# Start Mystique Sex pose //////////////////////////////////////////////////////////////////////////////////
# Mystique_Sex_P //////////////////////////////////////////////////////////////////////

label Mystique_Sex_P:  
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Sex >= 7: # She loves it
        $ Tempmod += 15
    elif newgirl["Mystique"].Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif newgirl["Mystique"].Sex: #You've done it before
        $ Tempmod += 10    
        
    if newgirl["Mystique"].Addict >= 75 and (newgirl["Mystique"].CreamP + newgirl["Mystique"].CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif newgirl["Mystique"].Addict >= 75:
        $ Tempmod += 15
        
    if newgirl["Mystique"].Lust > 85:
        $ Tempmod += 10
    elif newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
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
        
    if "no sex" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in newgirl["Mystique"].RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Mystique", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
                if Approval > 2:                                                      # fix, add Mystique auto stuff here
                    call Mystique_Sex_Launch("L")   
                    if newgirl["Mystique"].Legs == "skirt":
                        "Mystique slides onto her back and pulls you against her, sliding her skirt up as she does so."
                        $ newgirl["Mystique"].Upskirt = 1
                    elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
                        "Mystique slides onto her back and pulls you against her, sliding her pants off as she does so." 
                        $ newgirl["Mystique"].Upskirt = 1
                    elif newgirl["Mystique"].Legs == "shorts":
                        "Mystique slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                        $ newgirl["Mystique"].Upskirt = 1
                    else:
                        "Mystique slides onto her back and pulls you against her."
                    $ newgirl["Mystique"].SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                            "Mystique slides it in."
                        "Praise her.":       
                            call MystiqueFace("sexy, 1")                    
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                            ch_p "Oh yeah, [newgirl[Mystique].Pet], let's do this."
                            call Mystique_Namecheck
                            "Mystique slides it in."
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        "Ask her to stop.":
                            call MystiqueFace("surprised")       
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                            call Mystique_Namecheck
                            "Mystique pulls back."
                            call MystiqueOutfit
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                            return            
                    jump Mystique_Missionary_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add Mystique auto stuff here
                    $ Trigger2 = 0
                return   
    #End Mystique's lead
    
    if Situation == "auto":   
                call Mystique_Sex_Launch("L")   
                if newgirl["Mystique"].Legs == "skirt":
                    "You press Mystique down onto her back, sliding her skirt up as you go."
                    $ newgirl["Mystique"].Upskirt = 1                
                elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
                    "You press Mystique down onto her back, sliding her pants down as you do."    
                    $ newgirl["Mystique"].Upskirt = 1
                elif newgirl["Mystique"].Legs == "shorts":
                    "You press Mystique down onto her back, sliding her shorts down as you do."                
                    $ newgirl["Mystique"].Upskirt = 1
                else:
                    "You press Mystique down onto her back."
                $ newgirl["Mystique"].SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call MystiqueFace("surprised", 1)
                
                if (newgirl["Mystique"].Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Mystique is briefly startled, but melts into a sly smile."
                    call MystiqueFace("sexy")
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                    ch_m "Yeah. . . come on, [newgirl[Mystique].Petname]."            
                    jump Mystique_Missionary_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ newgirl["Mystique"].Brows = "angry"                
                    menu:
                        ch_m "What do you think you're doing down there?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call MystiqueFace("sexy", 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                                    ch_m "{i}Well. . .{/i} I didn't say I don't want to. . ."
                                    jump Mystique_Missionary_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call MystiqueFace("bemused", 1)
                                    if newgirl["Mystique"].Sex:
                                        ch_m "Maybe you could warn me?" 
                                    else:
                                        ch_m "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                            
                        "Just fucking.":                    
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                            "You press inside some more."                              
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            if not ApprovalCheck("Mystique", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call MystiqueFace("angry")
                                "Mystique shoves you away and punches you in the stomach."
                                ch_m "Jerk!"
                                ch_m "Stop it little brat!"                                                  
                                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Mystique_Sex_Reset
                                $ newgirl["Mystique"].RecentActions.append("angry")
                                $ newgirl["Mystique"].DailyActions.append("angry")                    
                            else:
                                call MystiqueFace("sad")
                                "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump Mystique_Missionary_SexPrep
                return   
    #End Auto
    
   
    if not newgirl["Mystique"].Sex and "no sex" not in newgirl["Mystique"].RecentActions:                           
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "I think i'm quite good at it, wanna try? "    
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "You'd really do this when you have me over a barrel?"
            
            
    if not newgirl["Mystique"].Sex and Approval:                                                  
            #First time dialog        
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -30, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -20, 1)
            elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "I don't want you to think I'm some kind of slut. . ."            
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "Ok, but only because it's you, [newgirl[Mystique].Petname]. . ."            
            elif newgirl["Mystique"].Addict >= 50:
                call MystiqueFace("manic", 1)
                ch_m "I have kind of been hoping you might. . ."
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "I can't say it hasn't crossed my mind. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call MystiqueFace("sexy", 1)
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "Again? Why do you do this to me?" 
            elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
                ch_m "I guess this is more secluded. . ."        
            elif "sex" in newgirl["Mystique"].RecentActions:
                ch_m "Another round? {i}Fine.{/i}"
                jump Mystique_Missionary_SexPrep
            elif "sex" in newgirl["Mystique"].DailyActions:
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from me. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_m "[Line]"
            elif newgirl["Mystique"].Sex < 3:        
                $ newgirl["Mystique"].Brows = "confused"
                $ newgirl["Mystique"].Mouth = "kiss"
                ch_m "So you'd like another round?"       
            else:       
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from me. . .", 
                    "You gonna make me purr?",
                    "You wanna slide into me?"]) 
                ch_m "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Ok, im horny too."  
            elif "no sex" in newgirl["Mystique"].DailyActions:               
                ch_m "You've made your case. . ."
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump Mystique_Missionary_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call MystiqueFace("angry")       
            if "no sex" in newgirl["Mystique"].RecentActions:  
                ch_m "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no sex" in newgirl["Mystique"].DailyActions:  
                ch_m "I already told you. . .not in public!" 
            elif "no sex" in newgirl["Mystique"].DailyActions:       
                ch_m "I already told you \"no.\""
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "I already told you this is too public!"     
            elif not newgirl["Mystique"].Sex:
                call MystiqueFace("bemused")
                ch_m "I don't know that I'm. . . ready? . ."
            else:
                call MystiqueFace("bemused")
                ch_m "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in newgirl["Mystique"].DailyActions:
                        call MystiqueFace("bemused")
                        ch_m "It's ok."
                        return
                "Maybe later?" if "no sex" not in newgirl["Mystique"].DailyActions:
                        call MystiqueFace("sexy")  
                        ch_m "Maybe, eventually."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)   
                        if Taboo:                    
                            $ newgirl["Mystique"].RecentActions.append("tabno")                      
                            $ newgirl["Mystique"].DailyActions.append("tabno") 
                        $ newgirl["Mystique"].RecentActions.append("no sex")                      
                        $ newgirl["Mystique"].DailyActions.append("no sex")            
                        return
                "I think you'd enjoy it as much as I would. . .":             
                        if Approval:
                            call MystiqueFace("sexy")     
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                            $ Line = renpy.random.choice(["That's. . . true. . .",     
                                "I suppose. . .", 
                                "That's. . . that's a good point. . ."]) 
                            ch_m "[Line]"
                            $ Line = 0                   
                            jump Mystique_Missionary_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Mystique", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                            call MystiqueFace("sad")
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                            ch_m "Well! . .  ok, fine, do me."  
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                            $ newgirl["Mystique"].Forced = 1  
                            jump Mystique_Missionary_SexPrep
                        else:                          
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)   
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if "no sex" in newgirl["Mystique"].DailyActions:
        ch_m "Maybe take \"no\" for an answer?" 
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Not even."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)     
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I can't believe you'd even consider it around here!"      
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
    elif newgirl["Mystique"].Sex:
        call MystiqueFace("sad") 
        ch_m "Maybe just fuck yourself, huh?."       
    else:
        call MystiqueFace("normal", 1)
        ch_m "Nuhuh."     
    $ newgirl["Mystique"].RecentActions.append("no sex")                      
    $ newgirl["Mystique"].DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label Mystique_Missionary_SexPrep:
    call Mystique_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off       
        
        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_m "We can't exactly do much like this, huh."
        
        if newgirl["Mystique"].Panties == "zipper panties":
            "She pulls the zippers down"
            $ newgirl["Mystique"].Panties = "zipper panties open"
            if newgirl["Mystique"].Chest == "bustier bra":
                $ newgirl["Mystique"].Chest = "bustier bra open"
        elif newgirl["Mystique"].Panties == "zipper panties open":
            ch_m "I'm ready"    
        elif newgirl["Mystique"].Panties and (newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans"):
            "She quickly drops her pants and her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Panties and newgirl["Mystique"].Legs == "shorts":
            "She quickly drops her shorts and her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif newgirl["Mystique"].Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Mystique") >= 5 and newgirl["Mystique"].Panties:
            "She shrugs and her [newgirl[Mystique].Hose] and [newgirl[Mystique].Panties] fall to the ground."
            $ newgirl["Mystique"].Hose = 0
        elif HoseNum("Mystique") >= 5:
            "She shrugs and her [newgirl[Mystique].Hose] fall to the ground."
            $ newgirl["Mystique"].Hose = 0
        elif newgirl["Mystique"].Panties:
            "She shrugs as her [newgirl[Mystique].Panties] fall to the ground."  
            
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless
        
        if Taboo: # Mystique gets started. . .
            if not newgirl["Mystique"].Sex:
                "Mystique glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Mystique slowly presses against your rigid member."
                else:
                    "Mystique hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Mystique glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Sex:
                if "cockout" in P_RecentActions:
                    "Mystique slowly presses against your rigid member."
                else:
                    "Mystique hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Mystique leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"  
        if newgirl["Mystique"].Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ newgirl["Mystique"].Panties = "zipper panties open"
            if newgirl["Mystique"].Chest == "bustier bra":
                $ newgirl["Mystique"].Chest = "bustier bra open"
        elif newgirl["Mystique"].Panties == "zipper panties open":
            "You get ready"    
        else:     
            if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
                "You quickly pull down her pants and her [newgirl[Mystique].Panties] and press against her slit."
            if newgirl["Mystique"].Panties and newgirl["Mystique"].Legs != "pants":
                "You quickly pull down her [newgirl[Mystique].Panties] and press against her slit."  
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
    if not newgirl["Mystique"].Sex:        
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -150)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 60)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 50) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 30)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 30)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no sex")
    $ newgirl["Mystique"].RecentActions.append("sex")                      
    $ newgirl["Mystique"].DailyActions.append("sex") 

label Mystique_Missionary_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Sex_Launch("sex") 
        call MystiqueLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].Sex):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "So are we getting close here?"   
        elif Cnt == (10 + newgirl["Mystique"].Sex):
                    $ newgirl["Mystique"].Brows = "angry"        
                    ch_m "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_m "Can we. . . do something. . . else?"
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Missionary_SexAfter
                                call Mystique_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Missionary_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Sex_Reset
                                $ Situation = "shift"
                                jump Mystique_Missionary_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_m "Not with that attitude, mister!"
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Missionary_SexAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Appearance" if P_Lvl >= 4:
                                menu:
                                    "I preffer the real Raven" if newgirl["Mystique"].LooksLike != "Mystique":
                                        ch_m "Sure"
                                        $ newgirl["Mystique"].LooksLike = "Mystique"
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns back into her original form with your cock still inside her."
                                        else:
                                            "She turns back into her original form."
                                        ch_p "Perfection"
                                    "Why don't you turn into Emma" if newgirl["Mystique"].LooksLike != "Emma":
                                        ch_m "So you like blondes huh?"
                                        $ newgirl["Mystique"].LooksLike = "Emma"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Emma with your cock still inside her."
                                        else:
                                            "She turns into Emma."
                                        ch_p "That's so hot!"
                                    "Why don't you turn into Rogue" if newgirl["Mystique"].LooksLike != "Rogue":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "You want me to turn into my own daughter?"
                                        ch_m "That's dirty."
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "I like it."
                                        $ newgirl["Mystique"].LooksLike = "Rogue"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Rogue with your cock still inside her."
                                        else:
                                            "She turns into Rogue."
                                        ch_p "Oh, kinky!"
                                    "Why don't you turn into Kitty" if newgirl["Mystique"].LooksLike != "Kitty":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "So you want me to turn into that brat, huh?"
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "Ok."
                                        $ newgirl["Mystique"].LooksLike = "Kitty"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Kitty with your cock still inside her."
                                        else:
                                            "She turns into Kitty."
                                        ch_p "Uhhh, naugthy Kitten! "
                                    "Nevermind":
                                        pass
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed > 0:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass

                        # "How about you put that armbinder" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "armbinder"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the armbinder" if newgirl["Mystique"].Over == "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put that bondage outfit" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put those bondage cuffs" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage cuffs"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the bondage outfit" if newgirl["Mystique"].Over == "bondage" or newgirl["Mystique"].Over == "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call Mystique_Slap_Ass                                    
                                    jump Mystique_Missionary_Sex_Cycle 

                        "Put her legs up" if not newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 0
                                    "You put her legs down."
                                    
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
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call Mystique_Missionary_SexAfter
                                            call Mystique_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Missionary_SexAfter
                                            call Mystique_Sex_A
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call Mystique_Missionary_SexAfter
                                            call Mystique_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_m "I'm kinda tired here? Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Missionary_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Line = 0
                                    jump Mystique_Missionary_SexAfter
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
                                jump Mystique_Missionary_SexAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_SexSprite"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Missionary_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Missionary_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Sex_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Missionary_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump Mystique_Missionary_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump Mystique_Missionary_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_m "Are you finished soon? It's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Missionary_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Sex_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Sex += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 2) 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if E_Loc == bg_current and "noticed Mystique" in E_RecentActions: #If Emma was participating
        $ E_LikeNewGirl["Mystique"] += 2 if E_LikeNewGirl["Mystique"] >= 800 else 1
    
    if "Mystique Sex Addict" in Achievements:
            pass 
            
    elif newgirl["Mystique"].Sex >= 10:
        $ newgirl["Mystique"].SEXP += 5
        $ Achievements.append("Mystique Sex Addict")
        if not Situation:
            call MystiqueFace("smile", 1)
            ch_m "I just can't seem to get enough from you."               
    elif newgirl["Mystique"].Sex == 1:            
            $ newgirl["Mystique"].SEXP += 20        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "I feel like I've been waiting a million years for that."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "I hope that was worth the wait."
    elif newgirl["Mystique"].Sex == 5:
            ch_m "Why did we not do this sooner?!"  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m "Could you have maybe paid more attention? . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Did you want to try something else?"
    call Checkout
    return   

# End Mystique sex //////////////////////////////////////////////////////////////////////////////////


# Mystique anal //////////////////////////////////////////////////////////////////////

label Mystique_Sex_A:
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif newgirl["Mystique"].Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif newgirl["Mystique"].Anal: #You've done it before
        $ Tempmod += 15 
        
    if newgirl["Mystique"].Addict >= 75 and (newgirl["Mystique"].CreamP + newgirl["Mystique"].CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif newgirl["Mystique"].Addict >= 75: 
        $ Tempmod += 15
    
    if newgirl["Mystique"].Lust > 85:
        $ Tempmod += 10
    elif newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if newgirl["Mystique"].Loose:
        $ Tempmod += 10  
    elif "anal" in newgirl["Mystique"].RecentActions:
        $ Tempmod -= 20 
    elif "anal" in newgirl["Mystique"].DailyActions:
        $ Tempmod -= 10
        
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
    if "no anal" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in newgirl["Mystique"].RecentActions else 0  
            
    $ Approval = ApprovalCheck("Mystique", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Mystique":                                                                  
            #Mystique auto-starts   
            if Approval > 2:                                                      # fix, add Mystique auto stuff here
                call Mystique_Sex_Launch("L")   
                if newgirl["Mystique"].Legs == "skirt":
                    "Mystique slides onto her back and pulls you against her, sliding her skirt up as she does so."
                    $ newgirl["Mystique"].Upskirt = 1
                elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
                    "Mystique slides onto her back and pulls you against her, sliding her pants off as she does so." 
                    $ newgirl["Mystique"].Upskirt = 1
                elif newgirl["Mystique"].Legs == "shorts":
                    "Mystique slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                    $ newgirl["Mystique"].Upskirt = 1
                else:
                    "Mystique slides onto her back and pulls you against her."
                $ newgirl["Mystique"].SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                        "Mystique slides it in."
                    "Praise her.":       
                        call MystiqueFace("sexy, 1")                    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                        ch_p "Ooo, dirty, [newgirl[Mystique].Pet], let's do this."
                        call Mystique_Namecheck
                        "Mystique slides it in."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    "Ask her to stop.":
                        call MystiqueFace("surprised")       
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                        call Mystique_Namecheck
                        "Mystique pulls back."
                        call MystiqueOutfit
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)                    
                        return            
                jump Mystique_Missionary_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add Mystique auto stuff here
                $ Trigger2 = 0
            return  
            #end if Mystique initiates
    
    if Situation == "auto":   
            call Mystique_Sex_Launch("L")   
            if newgirl["Mystique"].Legs == "skirt":
                "You press Mystique down onto her back, sliding her skirt up as you go."
                $ newgirl["Mystique"].Upskirt = 1                
            elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
                "You press Mystique down onto her back, sliding her pants down as you do."    
                $ newgirl["Mystique"].Upskirt = 1
            elif newgirl["Mystique"].Legs == "shorts":
                "You press Mystique down onto her back, sliding her shorts down as you do."                
                $ newgirl["Mystique"].Upskirt = 1
            else:
                "You press Mystique down onto her back."
            $ newgirl["Mystique"].SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call MystiqueFace("surprised", 1)
            
            if (newgirl["Mystique"].Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                if newgirl["Mystique"].Loose:
                    "Mystique is briefly startled, but melts into a sly smile."
                    ch_m "Oooh, stick it in. . ."            
                else:
                    "Mystique is briefly startled, but shrugs."
                    ch_m "Okay. . ."                  
                jump Mystique_Missionary_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ newgirl["Mystique"].Brows = "angry"                
                menu:
                    ch_m "Um what are you doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call MystiqueFace("sexy", 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_m "Well just take it easy, ok? . ."
                            jump Mystique_Missionary_AnalPrep
                        "You pull back before you really get it in."                    
                        call MystiqueFace("bemused", 1)
                        
                        if newgirl["Mystique"].Anal:
                            ch_m "Maybe you could warn me?" 
                        else:
                            ch_m "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                           
                    "Just fucking.":                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)
                        "You press into her."                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        if not ApprovalCheck("Mystique", 700, "O", TabM=1):                        
                            call MystiqueFace("angry")
                            "Mystique shoves you away and slaps you in the face."
                            ch_m "Asshole!"
                            ch_m "You need to ask nicer than that!"                                                  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Mystique_Sex_Reset
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")                        
                        else:
                            call MystiqueFace("sad")
                            "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump Mystique_Missionary_AnalPrep
            return  
            #end "auto" 
    
   
    if not newgirl["Mystique"].Anal and "no anal" not in newgirl["Mystique"].RecentActions:                                                               
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "You want to go in the \"back\" door?!"
      
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "Anal? Really?"
        
    if not newgirl["Mystique"].Loose and ("dildo anal" in newgirl["Mystique"].DailyActions or "anal" in newgirl["Mystique"].DailyActions):
            #if she's done anal stuff today
            call MystiqueFace("bemused", 1)
            ch_m "I'm not really over the last time."            
    elif "anal" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "Again? Come on then."
            jump Mystique_Missionary_AnalPrep
        
    
    if not newgirl["Mystique"].Anal and Approval:                                                 
            #First time dialog        
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "I guess? . ."           
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "Well. . ."
            elif newgirl["Mystique"].Addict >= 50:
                call MystiqueFace("manic", 1)
                ch_m "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "Anything's worth a shot. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "You really ask a lot here. . ."
            elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
                ch_m "I guess this is out of the discussion. . ."   
            elif "anal" in newgirl["Mystique"].DailyActions and not newgirl["Mystique"].Loose:
                pass      
            elif "anal" in newgirl["Mystique"].RecentActions:
                ch_m "I guess I'm warmed up. . ."
                jump Mystique_Missionary_AnalPrep
            elif "anal" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_m "[Line]"    
            else:       
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Girl_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I do have booty for days. . .", 
                    "You gonna make me Scream?",
                    "You wanna slide into me?"]) 
                ch_m "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Ok, fine."   
            elif "no anal" in newgirl["Mystique"].DailyActions:               
                ch_m "Well, ok, I've given it some thought, fine. . ." 
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "What are you waiting for?"]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump Mystique_Missionary_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call MystiqueFace("angry")
            if "no anal" in newgirl["Mystique"].RecentActions:  
                ch_m "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no anal" in newgirl["Mystique"].DailyActions:
                ch_m "I already told you. . .not in public!" 
            elif "no anal" in newgirl["Mystique"].DailyActions:       
                ch_m "I already told you \"no.\""
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "I already told you this is too public!"      
            elif not newgirl["Mystique"].Anal:
                call MystiqueFace("bemused")
                ch_m "I don't know that I'm. . . that kind of girl?"
            elif not newgirl["Mystique"].Loose and "anal" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("perplexed")
                ch_m "That was kind of. . . rough last time?"
            else:
                call MystiqueFace("bemused")
                ch_m "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("bemused")
                    ch_m "It's okay."              
                    return
                "Maybe later?" if "no anal" not in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("sexy")  
                    ch_m "Maybe, you never know."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                    if Taboo:                    
                        $ newgirl["Mystique"].RecentActions.append("tabno")                      
                        $ newgirl["Mystique"].DailyActions.append("tabno") 
                    $ newgirl["Mystique"].RecentActions.append("no anal")                      
                    $ newgirl["Mystique"].DailyActions.append("no anal") 
                    return
                "I bet it would feel really good. . .":             
                    if Approval:
                        call MystiqueFace("sexy")     
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["That's. . . true. . .",     
                            "I suppose. . .", 
                            "Maybe you are right. . ."]) 
                        ch_m "[Line]"
                        $ Line = 0                   
                        jump Mystique_Missionary_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Mystique", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                        call MystiqueFace("sad")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                        ch_m "Well! . .  ok, fine, stick it in."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                        $ newgirl["Mystique"].Forced = 1  
                        jump Mystique_Missionary_AnalPrep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)    
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if "no anal" in newgirl["Mystique"].DailyActions:
        ch_m "Maybe take \"no\" for an answer?"   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "That's a bit much, even for you."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)       
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "You're being ridiculous. That? Here?!"    
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3) 
    elif not newgirl["Mystique"].Loose and "anal" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("bemused")
        ch_m "I'm a little sore here?"    
    elif newgirl["Mystique"].Anal:
        call MystiqueFace("sad") 
        ch_m "That's totally off the table."
    else:
        call MystiqueFace("normal", 1)
        ch_m "Noooop."    
    $ newgirl["Mystique"].RecentActions.append("no anal")                      
    $ newgirl["Mystique"].DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label Mystique_Missionary_AnalPrep:    
            
    call Mystique_Sex_Launch("hotdog")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_m "We can't exactly do much like this, huh."

        if newgirl["Mystique"].Panties == "zipper panties":
            "She pulls the zippers down"
            $ newgirl["Mystique"].Panties = "zipper panties open"
            if newgirl["Mystique"].Chest == "bustier bra":
                $ newgirl["Mystique"].Chest = "bustier bra open"
        elif newgirl["Mystique"].Panties == "zipper panties open":
            ch_m "I'm ready"  
        elif newgirl["Mystique"].Panties and (newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans"):
            "She quickly drops her pants and her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Panties and newgirl["Mystique"].Legs == "shorts":
            "She quickly drops her shorts and her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Legs == "capris" or newgirl["Mystique"].Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif newgirl["Mystique"].Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Mystique") >= 5 and newgirl["Mystique"].Panties:
            "She shrugs and her [newgirl[Mystique].Hose] and [newgirl[Mystique].Panties] fall to the ground."
            $ newgirl["Mystique"].Hose = 0
        elif HoseNum("Mystique") >= 5:
            "She shrugs and her [newgirl[Mystique].Hose] fall to the ground."
            $ newgirl["Mystique"].Hose = 0
        elif newgirl["Mystique"].Panties:
            "She shrugs as her [newgirl[Mystique].Panties] fall to the ground."  
            
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless
        
        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Anal:                
                "Mystique glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Mystique glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Mystique slowly presses against your rigid member."
                else:
                    "Mystique hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Anal:
                "Mystique leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in P_RecentActions:
                    "Mystique slowly presses against your rigid member."
                else:
                    "Mystique hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if newgirl["Mystique"].Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ newgirl["Mystique"].Panties = "zipper panties open"
            if newgirl["Mystique"].Chest == "bustier bra":
                $ newgirl["Mystique"].Chest = "bustier bra open"
        elif newgirl["Mystique"].Panties == "zipper panties open":
            "You get ready"  
        else: 
            if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
                "You quickly pull down her pants and her [newgirl[Mystique].Panties] and press against her back door."
            if newgirl["Mystique"].Panties and newgirl["Mystique"].Legs != "pants":
                "You quickly pull down her [newgirl[Mystique].Panties] and press against her back door."  
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless(1)
        
    call Seen_First_Peen(1)
    
    if not newgirl["Mystique"].Anal:                                                      #First time stat buffs       
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -150)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 70)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 40) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 30)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 70) 
    elif not newgirl["Mystique"].Loose:                                                   #first few times stat buffs       
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5) 
        else:
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 7)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no anal")
    $ newgirl["Mystique"].RecentActions.append("anal")                      
    $ newgirl["Mystique"].DailyActions.append("anal") 

label Mystique_Missionary_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Sex_Launch("anal") 
        call MystiqueLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "confused"
                    if newgirl["Mystique"].Loose:
                        ch_m "So are you getting close here?"  
                    else:
                        ch_m "So are you getting close here? This is not super pleasant. . ."   
        elif Cnt == (10 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "angry"        
                    ch_m "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_m "Can we. . . do something. . . else?"
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                if newgirl["Mystique"].Anal >= 5 and newgirl["Mystique"].Blow >= 10 and newgirl["Mystique"].SEXP >= 50:
                                    $ Situation = "shift"
                                    call Mystique_Missionary_AnalAfter
                                    call Mystique_Blowjob      
                                else:
                                    ch_m "No thanks, [newgirl[Mystique].Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call Mystique_Missionary_AnalAfter
                                    call MystiqueHJ_Prep   
                        "How about a Handy?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Missionary_AnalAfter
                                call Mystique_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Missionary_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Sex_Reset
                                $ Situation = "shift"
                                jump Mystique_Missionary_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_m "Not with that attitude, mister!"                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Missionary_AnalAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Appearance" if P_Lvl >= 4:
                                menu:
                                    "I preffer the real Raven" if newgirl["Mystique"].LooksLike != "Mystique":
                                        ch_m "Sure"
                                        $ newgirl["Mystique"].LooksLike = "Mystique"
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns back into her original form with your cock still inside her."
                                        else:
                                            "She turns back into her original form."
                                        ch_p "Perfection"
                                    "Why don't you turn into Emma" if newgirl["Mystique"].LooksLike != "Emma":
                                        ch_m "So you like blondes huh?"
                                        $ newgirl["Mystique"].LooksLike = "Emma"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Emma with your cock still inside her."
                                        else:
                                            "She turns into Emma."
                                        ch_p "That's so hot!"
                                    "Why don't you turn into Rogue" if newgirl["Mystique"].LooksLike != "Rogue":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "You want me to turn into my own daughter?"
                                        ch_m "That's dirty."
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "I like it."
                                        $ newgirl["Mystique"].LooksLike = "Rogue"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Rogue with your cock still inside her."
                                        else:
                                            "She turns into Rogue."
                                        ch_p "Oh, kinky"
                                    "Why don't you turn into Kitty" if newgirl["Mystique"].LooksLike != "Kitty":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "So you want me to turn into that brat, huh?"
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "Ok."
                                        $ newgirl["Mystique"].LooksLike = "Kitty"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Kitty with your cock still inside her."
                                        else:
                                            "She turns into Kitty."
                                        ch_p "Uhhh, naughty Kitten!"
                                    "Nevermind":
                                        pass
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 3:                    
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass
                            
                        "Slow Down. . ." if Speed > 0:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass

                        # "How about you put that armbinder" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "armbinder"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the armbinder" if newgirl["Mystique"].Over == "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put that bondage outfit" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put those bondage cuffs" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage cuffs"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the bondage outfit" if newgirl["Mystique"].Over == "bondage" or newgirl["Mystique"].Over == "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call Mystique_Slap_Ass                                    
                                    jump Mystique_Missionary_Anal_Cycle  

                        "Put her legs up" if not newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 0
                                    "You put her legs down."
                                    
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
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call Mystique_Missionary_AnalAfter
                                            call Mystique_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Missionary_AnalAfter
                                            call Mystique_Sex_P
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call Mystique_Missionary_AnalAfter
                                            call Mystique_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_m "I'm tired here. Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Missionary_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Line = 0
                                    jump Mystique_Missionary_AnalAfter
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
                                jump Mystique_Missionary_AnalAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_SexSprite"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Missionary_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Missionary_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Sex_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Missionary_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Missionary_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Missionary_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_m "Are you finished? It's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Missionary_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Sex_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Anal += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 3) 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if E_Loc == bg_current and "noticed Mystique" in E_RecentActions: #If Emma was participating
        $ E_LikeNewGirl["Mystique"] += 2 if E_LikeNewGirl["Mystique"] >= 800 else 1
    
    if "Mystique Anal Addict" in Achievements:
            pass 
            
    elif newgirl["Mystique"].Anal >= 10:
        $ newgirl["Mystique"].SEXP += 7
        $ Achievements.append("Mystique Anal Addict")
        if not Situation:
            call MystiqueFace("bemused", 1)
            ch_m "I love this so much!"                  
    elif newgirl["Mystique"].Anal == 1:            
            $ newgirl["Mystique"].SEXP += 25        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "Anal. . . huh, who knew?"
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "Ouch."
                    ch_m "I guess you got what you needed?"
    elif newgirl["Mystique"].Anal == 5:
            ch_m "I'm really starting to love this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Ok, pretty good actually. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End Mystique Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Mystique hotdog //////////////////////////////////////////////////////////////////////

label Mystique_Sex_H: 
    call Shift_Focus("Mystique")
    if newgirl["Mystique"].Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif newgirl["Mystique"].Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if newgirl["Mystique"].Lust > 85:
        $ Tempmod += 10
    elif newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
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
        
    if "no hotdog" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in newgirl["Mystique"].RecentActions else 0      
        
    $ Approval = ApprovalCheck("Mystique", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Mystique":                                                                  
            #Mystique auto-starts   
            if Approval > 2:                                                      # fix, add Mystique auto stuff here
                call Mystique_Sex_Launch("L") 
                "Mystique slides onto her back and pulls you against her, rubbing it against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3)
                        "Mystique starts to grind against you."
                    "Praise her.":       
                        call MystiqueFace("sexy, 1")                    
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 2) 
                        ch_p "Hmmm, that's good, [newgirl[Mystique].Pet]."
                        call Mystique_Namecheck
                        "Mystique starts to grind against you."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 2)
                    "Ask her to stop.":
                        call MystiqueFace("surprised")       
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                        call Mystique_Namecheck
                        "Mystique pulls back."
                        call MystiqueOutfit
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)                    
                        return            
                jump Mystique_Missionary_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add Mystique auto stuff here
                $ Trigger2 = 0
            return            
            #end Mystique initates
    
    if Situation == "auto":   
            call Mystique_Sex_Launch("L")   
            "You press Mystique down onto her back and press your cock against her."    
            call MystiqueFace("surprised", 1)
            
            if (newgirl["Mystique"].Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Mystique is briefly startled, but melts into a sly smile."
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                ch_m "Hmm, I've apparently got someone's attention. . ."            
                jump Mystique_Missionary_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ newgirl["Mystique"].Brows = "angry"                
                menu:
                    ch_m "Hmm, how rude, [newgirl[Mystique].Petname]." 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call MystiqueFace("sexy", 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_m "I guess it does feel pretty good. . ."
                            jump Mystique_Missionary_HotdogPrep
                        "You pull back from her."                    
                        call MystiqueFace("bemused", 1)
                        ch_m "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"                                             
                    "You'll see.":                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)
                        "You grind against her crotch."                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        if not ApprovalCheck("Mystique", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call MystiqueFace("angry")
                            "Mystique shoves you away."
                            ch_m "Dork!"
                            ch_m "I'm not into that!"                                                  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Mystique_Sex_Reset
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")                       
                        else:
                            call MystiqueFace("sad")
                            "Mystique doesn't seem to be into this, but she's knows her place."                        
                            jump Mystique_Missionary_HotdogPrep
            return     
            #end auto
    
   
    if not newgirl["Mystique"].Hotdog and "no hotdog" not in newgirl["Mystique"].RecentActions:                                                               
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So, just grinding against me?"
      
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m ". . . That's it?"
        
        
    if not newgirl["Mystique"].Hotdog and Approval:                                                
            #First time dialog        
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Brows = "sad"
                $ newgirl["Mystique"].Mouth = "smile" 
                ch_m "It does look a bit swolen. . ."           
            elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
                call MystiqueFace("normal")
                ch_m "If you want. . ."
            elif newgirl["Mystique"].Addict >= 50:
                call MystiqueFace("manic", 1)
                ch_m "Hmmm. . ."
            else: # Uninhibited 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Mouth = "smile"             
                ch_m "Yeah, you look ready to go. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if newgirl["Mystique"].Forced: 
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
                ch_m "That's {i}all{/i} you want?"  
            elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
                ch_m "I guess this is a better location . ."   
            elif "hotdog" in newgirl["Mystique"].RecentActions:
                call MystiqueFace("sexy", 1)
                ch_m "Again? Ok."
                jump Mystique_Missionary_HotdogPrep
            elif "hotdog" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really digging this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_m "[Line]"    
            else:       
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Girl_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really digging this. . .", 
                    "You want another rub?"]) 
                ch_m "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
                ch_m "Ok, come on."    
            elif "no hotdog" in newgirl["Mystique"].DailyActions:               
                ch_m "Well, I guess it's not so bad. . ."
            else:
                call MystiqueFace("sexy", 1)
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump Mystique_Missionary_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call MystiqueFace("angry")
            if "no hotdog" in newgirl["Mystique"].RecentActions:  
                ch_m "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no hotdog" in newgirl["Mystique"].DailyActions: 
                ch_m "I{i}just{/i} told, not in public!" 
            elif "no hotdog" in newgirl["Mystique"].DailyActions:       
                ch_m "I{i}just{/i} told you \"no\" earlier!"
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "I{i}just{/i} told you, not in public!"  
            elif not newgirl["Mystique"].Hotdog:
                call MystiqueFace("bemused")
                ch_m "That's kinda hot, [newgirl[Mystique].Petname]. . ."
            else:
                call MystiqueFace("bemused")
                ch_m "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("bemused")
                    ch_m "No problem."              
                    return
                "Maybe later?" if "no hotdog" not in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("sexy")  
                    ch_m "Well, maybe, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 1)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 1)   
                    if Taboo:                    
                        $ newgirl["Mystique"].RecentActions.append("tabno")                      
                        $ newgirl["Mystique"].DailyActions.append("tabno") 
                    $ newgirl["Mystique"].RecentActions.append("no hotdog")                      
                    $ newgirl["Mystique"].DailyActions.append("no hotdog")                          
                    return
                "You might like it. . .":             
                    if Approval:
                        call MystiqueFace("sexy")     
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 2)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2) 
                        $ Line = renpy.random.choice(["Well, sure, ok.",     
                            "I suppose. . .", 
                            "Ok, let's try it then. . ."]) 
                        ch_m "[Line]"
                        $ Line = 0                   
                        jump Mystique_Missionary_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Mystique", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                        call MystiqueFace("sad")
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2, 1)
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                        ch_m "Ok, fine. Whatever."  
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                        $ newgirl["Mystique"].Forced = 1  
                        jump Mystique_Missionary_HotdogPrep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)     
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1      
    
    if "no hotdog" in newgirl["Mystique"].DailyActions:
        ch_m "I'm just not into that."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    if newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Not happening."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -1) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1)  
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)        
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m " not here!"  
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)  
    elif newgirl["Mystique"].Hotdog:
        call MystiqueFace("sad") 
        ch_m "Yeah, not again."
    else:
        call MystiqueFace("normal", 1)
        ch_m "No way."    
    $ newgirl["Mystique"].RecentActions.append("no hotdog")                      
    $ newgirl["Mystique"].DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label Mystique_Missionary_HotdogPrep:  
    call Mystique_Sex_Launch("hotdog")
    
    if Situation != "auto":
#        call Mystique_Bottoms_Off    
        
        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Hotdog:                
                "Mystique glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                
            else:         
                "Mystique glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Mystique slowly presses against your rigid member."
                else:
                    "Mystique hesitantly pulls down your pants and slowly presses against your rigid member."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:                
            if "cockout" in P_RecentActions:
                "Mystique slowly presses against your rigid member."
            else:
                "Mystique hesitantly pulls down your pants slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her mound."
    
    call Seen_First_Peen(1)
    if not newgirl["Mystique"].Hotdog:                                                      #First time stat buffs      
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -5)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 10) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 20)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no hotdog")
    $ newgirl["Mystique"].RecentActions.append("hotdog")                      
    $ newgirl["Mystique"].DailyActions.append("hotdog") 

label Mystique_Missionary_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Sex_Launch("hotdog") 
        call MystiqueLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if newgirl["Mystique"].SEXP >= 100 or ApprovalCheck("Mystique", 1200, "LO"):
            pass
        elif Cnt == (5 + newgirl["Mystique"].Hotdog):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Are you getting close here?"   
        elif Cnt == (10 + newgirl["Mystique"].Hotdog):
                    $ newgirl["Mystique"].Brows = "angry"        
                    menu:
                        ch_m "This is getting a bit dull."
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Missionary_HotdogAfter
                                call Mystique_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Missionary_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Sex_Reset
                                $ Situation = "shift"
                                jump Mystique_Missionary_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_m "Not with that attitude, mister!"                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Missionary_HotdogAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    menu:
                        "[Line]"
                        "Appearance" if P_Lvl >= 4:
                                menu:
                                    "I preffer the real Raven" if newgirl["Mystique"].LooksLike != "Mystique":
                                        ch_m "Sure"
                                        $ newgirl["Mystique"].LooksLike = "Mystique"
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns back into her original form with your cock still inside her."
                                        else:
                                            "She turns back into her original form."
                                        ch_p "Perfection"
                                    "Why don't you turn into Emma" if newgirl["Mystique"].LooksLike != "Emma":
                                        ch_m "So you like blondes huh?"
                                        $ newgirl["Mystique"].LooksLike = "Emma"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Emma with your cock still inside her."
                                        else:
                                            "She turns into Emma."
                                        ch_p "That's so hot!"
                                    "Why don't you turn into Rogue" if newgirl["Mystique"].LooksLike != "Rogue":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "You want me to turn into my own daughter?"
                                        ch_m "That's dirty."
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "I like it."
                                        $ newgirl["Mystique"].LooksLike = "Rogue"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Rogue with your cock still inside her."
                                        else:
                                            "She turns into Rogue."
                                        ch_p "Oh, kinky!"
                                    "Why don't you turn into Kitty" if newgirl["Mystique"].LooksLike != "Kitty":
                                        call NewGirl_FaceSpecial("Mystique", "surprised")
                                        ch_m "So you want me to turn into that brat, huh?"
                                        call NewGirl_FaceSpecial("Mystique", "smile")
                                        ch_m "Ok."
                                        $ newgirl["Mystique"].LooksLike = "Kitty"
                                        call NewGirl_RemoveClothes("Mystique")
                                        if P_Cock == "anal" or P_Cock == "in":
                                            "She turns into Kitty with your cock still inside her."
                                        else:
                                            "She turns into Kitty."
                                        ch_p "Uhhh, naughty Kitten!"
                                    "Nevermind":
                                        pass
                        "Keep going. . ." if Speed:
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

                        # "How about you put that armbinder" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "armbinder"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the armbinder" if newgirl["Mystique"].Over == "armbinder":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put that bondage outfit" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     "She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "How about you put those bondage cuffs" if newgirl["Mystique"].Bondage and newgirl["Mystique"].Over != "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her with the binder, making sure she can't move her arms"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = "bondage cuffs"
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]

                        # "Remove the bondage outfit" if newgirl["Mystique"].Over == "bondage" or newgirl["Mystique"].Over == "bondage cuffs":
                        #     call MystiqueFace("sexy", 1) 
                        #     #if newgirl["Mystique"].Over or newgirl["Mystique"].Chest or newgirl["Mystique"].Panties or newgirl["Mystique"].Legs:
                        #     #    "She glances up at you as her clothes drop to the ground."
                        #     #$ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Legs = 0
                        #     #$ newgirl["Mystique"].Chest = 0
                        #     #$ newgirl["Mystique"].Panties = 0
                        #     #"She starts dressing the new outfit"
                        #     "You help her remove the binder"
                        #     #"And add a blindfold so she can't see a thing"
                        #     #$ newgirl["Mystique"].Blindfold = 1
                        #     $ newgirl["Mystique"].Over = 0
                        #     #$ newgirl["Mystique"].Chest = "bustier bra"
                        #     #$ newgirl["Mystique"].Panties = "zipper panties"
                        #     #$ newgirl["Mystique"].Outfit = "zipper bondage"
                        #     #$ newgirl["Mystique"].Shame = newgirl["Mystique"].OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call Mystique_Slap_Ass                                    
                                    jump Mystique_Missionary_Hotdog_Cycle  

                        "Put her legs up" if not newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if newgirl["Mystique"].LegsUp:
                                    $ newgirl["Mystique"].LegsUp = 0
                                    "You put her legs down."
                                    
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
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call Mystique_Missionary_HotdogAfter
                                        call Mystique_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Missionary_HotdogAfter
                                        call Mystique_Sex_P
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call Mystique_Missionary_HotdogAfter
                                        call Mystique_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Missionary_HotdogAfter
                                        call Mystique_Sex_A
                                    "Never Mind":
                                        pass
                            else:
                                ch_m "I'm tired! Could we wrap it up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm tired here? Could end it now?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Missionary_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Sex_Reset
                                    $ Line = 0
                                    jump Mystique_Missionary_HotdogAfter
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
                                jump Mystique_Missionary_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_SexSprite"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Missionary_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Missionary_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Sex_Launch("hotdog")
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Missionary_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump Mystique_Missionary_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump Mystique_Missionary_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_m "Are you finished now? It's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Missionary_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Sex_Reset
        
    call MystiqueFace("sexy") 
    
    $ newgirl["Mystique"].Hotdog += 1  
    $ newgirl["Mystique"].Action -=1
    $ newgirl["Mystique"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Mystique"].Addictionrate += 1        
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 1) 
    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
    
    if K_Loc == bg_current and "noticed Mystique" in K_RecentActions: #If Kitty was participating
        $ K_LikeNewGirl["Mystique"] += 2 if K_LikeNewGirl["Mystique"] >= 800 else 1
    if R_Loc == bg_current and "noticed Mystique" in R_RecentActions: #If Rogue was participating
        $ R_LikeNewGirl["Mystique"] += 2 if R_LikeNewGirl["Mystique"] >= 800 else 1
    if E_Loc == bg_current and "noticed Mystique" in E_RecentActions: #If Emma was participating
        $ E_LikeNewGirl["Mystique"] += 2 if E_LikeNewGirl["Mystique"] >= 800 else 1
    
    if newgirl["Mystique"].Hotdog == 10:
        $ newgirl["Mystique"].SEXP += 5             
    elif newgirl["Mystique"].Hotdog == 1:            
            $ newgirl["Mystique"].SEXP += 10        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "I. . . liked that a lot."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "Well, did that work for you?"
    elif newgirl["Mystique"].Hotdog == 5:
            ch_m "I'm not surprised that I enjoy this so much."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m "I didn't get much out of that. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "I could get into that. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End Mystique hotdogging //////////////////////////////////////////////////////////////////////////////////
