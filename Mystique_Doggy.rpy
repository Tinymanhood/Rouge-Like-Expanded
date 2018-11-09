# Start R Doggy //////////////////////////////////////////////////////////////////////////////////
# Mystique_Doggy_P //////////////////////////////////////////////////////////////////////

label Mystique_Doggy_P:  
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
            call Mystique_Doggy_Launch("L")   
            if (newgirl["Mystique"].Legs == "skirt" or newgirl["Mystique"].Legs == "cheerleader skirt"):
                "Mystique turns and backs up against your cock, sliding her skirt up as she does so."
                $ newgirl["Mystique"].Upskirt = 1
            elif newgirl["Mystique"].Legs == "pants":
                "Mystique turns and backs up against your cock, sliding her pants off as she does so."                
                $ newgirl["Mystique"].Legs = 0
            else:
                "Mystique turns and backs up against your cock."
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
                    ch_p "Come on, [newgirl[Mystique].Pet], let's do this."
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
            jump Mystique_Doggy_SexPrep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Mystique_Doggy_Launch("L")   
        if (newgirl["Mystique"].Legs == "skirt" or newgirl["Mystique"].Legs == "cheerleader skirt"):
            "You press up against Mystique's backside, sliding her skirt up as you go."
            $ newgirl["Mystique"].Upskirt = 1
        elif newgirl["Mystique"].Legs == "pants":
            "You press up against Mystique's backside, sliding her pants down as you do."                
            $ newgirl["Mystique"].Legs = 0
        else:
            "You press up against Mystique's backside."
        $ newgirl["Mystique"].SeenPanties = 1
        "You rub the tip of your cock against her moist slit."        
        call MystiqueFace("surprised", 1)
        
        if (newgirl["Mystique"].Sex and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
            ch_m "Ok, [newgirl[Mystique].Petname], let's do this."            
            jump Mystique_Doggy_SexPrep         
        else:                                                                                                            #she's questioning it
            $ newgirl["Mystique"].Brows = "angry"                
            menu:
                ch_m "Hey, what do you think you're doing with my ass?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call MystiqueFace("sexy", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_m "Well, since you're be'in so nice about it, I guess we can try it. . ."
                        jump Mystique_Doggy_SexPrep
                    "You pull back before you really get it in."                    
                    call MystiqueFace("bemused", 1)
                    if newgirl["Mystique"].Sex:
                        ch_m "Well ok, [newgirl[Mystique].Petname], no problem. Just give me a little warning next time." 
                    else:
                        ch_m "Well ok, [newgirl[Mystique].Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                    "You press inside some more."                              
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    if not ApprovalCheck("Mystique", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                        call MystiqueFace("angry")
                        "Mystique shoves you away and slaps you in the face."
                        ch_m "Dork!"
                        ch_m "If that's how you want to treat me, we're done here!"                                                  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Mystique_Doggy_Reset
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")                    
                    else:
                        call MystiqueFace("sad")
                        "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump Mystique_Doggy_SexPrep
        return             
    
   
    if not newgirl["Mystique"].Sex and "no sex" not in newgirl["Mystique"].RecentActions:                           #first time    
        call MystiqueFace("surprised", 1)
        $ newgirl["Mystique"].Mouth = "kiss"
        ch_m "So, you'd like to take this to the next level? Actual sex? . . ."    
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            ch_m "You'd really take it that far?"
            
            
    if not newgirl["Mystique"].Sex and Approval:                                                  #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -30, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -20, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "Well, I could do it, this might be fun."            
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal")
            ch_m "If that's what you want, [newgirl[Mystique].Petname]. . ."            
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Mouth = "smile"             
            ch_m "Hmm, i always wanted to try it. . ."   
            
    elif Approval:                                                                       #Second time+ dialog        
        call MystiqueFace("sexy", 1)
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's really what you want?" 
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Well, at least you got us some privacy this time. . ."        
        elif "sex" in newgirl["Mystique"].RecentActions:
            ch_m "You want to go again? Ok."
            jump Mystique_Doggy_SexPrep
        elif "sex" in newgirl["Mystique"].DailyActions:
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this. . .", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Sex < 3:        
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you'd like another go?"       
        else:       
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from me heh. . .", 
                "You want me to ride your cock?",
                "You wanna dip your wick?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine."  
        elif "no sex" in newgirl["Mystique"].DailyActions:               
            ch_m "Ok, you've complimented me in this time. . ."
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_Doggy_SexPrep   
    
    else:                                                                               #She's not into it, but maybe. . .    
        call MystiqueFace("angry")       
        if "no sex" in newgirl["Mystique"].RecentActions:  
            ch_m "I {i}just{/i} told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no sex" in newgirl["Mystique"].DailyActions:  
            ch_m "I already told you that I wouldn't bang you in public!" 
        elif "no sex" in newgirl["Mystique"].DailyActions:       
            ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I already told you this is too public!"     
        elif not newgirl["Mystique"].Sex:
            call MystiqueFace("bemused")
            ch_m "I just don't think I'm ready yet, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not, right now [newgirl[Mystique].Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no sex" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no sex" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "I'll give it some thought, [newgirl[Mystique].Petname]."
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
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_m "[Line]"
                    $ Line = 0                   
                    jump Mystique_Doggy_SexPrep       
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                    ch_m "Ok, fine. If we're going to do this, stick it in already."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump Mystique_Doggy_SexPrep
                else:                          
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)   
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if "no sex" in newgirl["Mystique"].DailyActions:
        ch_m "Learn to take \"no\" for an answer, [newgirl[Mystique].Petname]." 
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "I'm not doing that just because you have me over a barrel."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)    
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)     
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "Even if I wanted to, it certainly wouldn't be here!"      
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)
    elif newgirl["Mystique"].Sex:
        call MystiqueFace("sad") 
        ch_m "Maybe you could go and fuck yourself this time."       
    else:
        call MystiqueFace("normal", 1)
        ch_m "No way."     
    $ newgirl["Mystique"].RecentActions.append("no sex")                      
    $ newgirl["Mystique"].DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label Mystique_Doggy_SexPrep:
    call Mystique_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off       
        
        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_m "Well, I guess some things are necessary, [newgirl[Mystique].Petname]."
            
        if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
            "She quickly pulls down her pants and drops her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Mystique") >= 5 and newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Hose] and drops her [newgirl[Mystique].Panties]."
            $ newgirl["Mystique"].Hose = 0
        elif HoseNum("Mystique") >= 5:
            "She quickly pulls down her [newgirl[Mystique].Hose], exposing her bare ass."
            $ newgirl["Mystique"].Hose = 0
        elif newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Panties]."  
            
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless
        
        if Taboo: # Mystique gets started. . .
            if not newgirl["Mystique"].Sex:
                "Mystique glances around for voyeurs. . ."
                "Mystique hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Mystique glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Sex:
                "Mystique hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Mystique bends over and presses her backside against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"         
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

label Mystique_Doggy_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Doggy_Launch("sex") 
        call MystiqueLust        
        $ P_Cock = "in"
        $ Trigger = "sex"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if Cnt == (5 + newgirl["Mystique"].Sex):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + newgirl["Mystique"].Sex):
                    $ newgirl["Mystique"].Brows = "angry"        
                    ch_m "I'm . . .getting . . .worn out. . . here, . . [newgirl[Mystique].Petname]."
                    menu:
                        ch_m "Can we. . . do something. . . else?"
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Doggy_SexAfter
                                call Mystique_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Doggy_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Doggy_Reset
                                $ Situation = "shift"
                                jump Mystique_Doggy_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_m "Well if that's your attitude you can handle your own business."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Doggy_SexAfter
        #End Count check
        
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
                                    "You ask her to up the pace a bit."
                        "Speed up. . ." if Speed == 2:
                                    $ Speed = 3
                                    "You start pounding her pussy as fast as you can" #pussy

                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Gag":
                            if not newgirl["Mystique"].Gag:
                                #"You put a gag on Mystique"
                            #            $ newgirl["Mystique"].Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call Mystique_Gagging("ballgag")
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Gagging("ballgag")
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call Mystique_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call Mystique_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Mystique's gag"
                                $ newgirl["Mystique"].Gag = 0

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call Mystique_Slap_Ass 
                                    hide Slap_Ass2                                    
                                    jump Mystique_Doggy_Sex_Cycle  
                                    
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
                                            call Mystique_Doggy_SexAfter
                                            call Mystique_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Doggy_SexAfter
                                            call Mystique_Doggy_A
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call Mystique_Doggy_SexAfter
                                            call Mystique_Doggy_H
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call Mystique_Doggy_SexAfter
                                            call Mystique_Plug_Ass
                                    "Just stick the plug in her ass [[without asking]." if not newgirl["Mystique"].Plugged:
                                            $ Situation = "auto"
                                            call Mystique_Doggy_SexAfter
                                            call Mystique_Plug_Ass
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
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Doggy_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Line = 0
                                    jump Mystique_Doggy_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
        
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Doggy_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_Doggy_SexAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_Doggy"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Doggy_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Doggy_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Doggy_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Doggy_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump Mystique_Doggy_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump Mystique_Doggy_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Doggy_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Doggy_Reset
        
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
            ch_m "I think I'm getting addicted to this."               
    elif newgirl["Mystique"].Sex == 1:            
            $ newgirl["Mystique"].SEXP += 20        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was really great, [newgirl[Mystique].Petname], we'll have to do that again sometime."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "Did you get what you needed here?"
    elif newgirl["Mystique"].Sex == 5:
            ch_m "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m "I didn't exactly get off there. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   

# End R Doggy //////////////////////////////////////////////////////////////////////////////////

# Gag Mystique //////////////////////////////////////////////////////////////////////////////////////

label Mystique_Gagging(Gagtype = 0):
    if newgirl["Mystique"].Gagx >= 7: # She loves it
        $ Tempmod += 20   
    elif newgirl["Mystique"].Gagx >= 3: #You've done it before several times
        $ Tempmod += 17
    elif newgirl["Mystique"].Gagx: #You've done it before
        $ Tempmod += 15 
        
    if newgirl["Mystique"].Addict >= 75 and (newgirl["Mystique"].CreamP + newgirl["Mystique"].CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif newgirl["Mystique"].Addict >= 75: 
        $ Tempmod += 15
    
    if newgirl["Mystique"].Lust > 85:
        $ Tempmod += 10
    elif newgirl["Mystique"].Lust > 75: #She's really horny
        $ Tempmod += 5
 
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
            
    $ Approval = ApprovalCheck("Mystique", 1450, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    
    if Situation == "auto":   

        "You grab a ballgag and tries to put it on her mouth."
    
        call MystiqueFace("surprised", 1)
        
        if (newgirl["Mystique"].Gagx and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Mystique is briefly startled and turns towards you, but then smiles and nods in agreement."
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
            ch_m "Naughty. . ."            
            jump Mystique_GagPrep         
        else:                                                                                                            #she's questioning it
            $ newgirl["Mystique"].Brows = "angry"                
            menu:
                ch_m "Hey, what do you think you're doing?!" 
                "Sorry, sorry! I thought you'd like it.":
                    if Approval:     
                        call MystiqueFace("sexy", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_m "I guess if you really want to try it. . ."
                        jump Mystique_GagPrep
                    "You take the ballgag back before you really put it on her."                    
                    call MystiqueFace("bemused", 1)
                    if newgirl["Mystique"].Gagx:
                        ch_m "Well ok, [newgirl[Mystique].Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_m "Well ok, [newgirl[Mystique].Petname], I'm not really into that, but maybe if you ask nicely next time . . ."
                    #$ newgirl["Mystique"].Gagx -= 1                                               
                "Just shut up.":                    
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)
                    "You put the ballgag on her mouth."  
                    $ newgirl["Mystique"].Gag = Gagtype                           
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 15)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    if not ApprovalCheck("Mystique", 700, "O", TabM=1):                        
                        call MystiqueFace("angry")
                        "Mystique shoves you away, take the ballgag off and throw it on your face."
                        $ newgirl["Mystique"].Gag = 0
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Mystique_Doggy_Reset
                        ch_m "You shut up!"
                        ch_m "If that's how you want to treat me, we're done here!"                                                  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                        
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")  
                        #$ newgirl["Mystique"].Gagx -= 1                      
                    else:
                        $ newgirl["Mystique"].Gag = Gagtype
                        call MystiqueFace("sad")
                        "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
        return             
    
   
    if not newgirl["Mystique"].Gagx:                                                               #first time    
        call MystiqueFace("surprised", 1)
        $ newgirl["Mystique"].Mouth = "kiss"
        ch_m "Wait, you want to put a gag in my mouth?!"
  
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            ch_m "Seriously?"
        
    
    if not newgirl["Mystique"].Gagx and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "I guess if you really want to try it. . ."           
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal")
            ch_m "Ok, [newgirl[Mystique].Petname]."
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "Well. . . I bet it would feel really good."
        else: # Uninhibited 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Mouth = "smile"             
            ch_m "Hmm, it has been on my list. . ."  
        jump Mystique_GagPrep
    
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's really what you want?"
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Well, at least you got us some privacy this time. . ."   
        elif newgirl["Mystique"].Gagx < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you wanna try that again?"       
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want some bondage?",                 
                "So you wanna try that again?",                 
                "I like that."]) 
            ch_m "[Line]"
        $ Line = 0
        jump Mystique_GagPrep
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine."   
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, shut me up.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . .",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_GagPrep 
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if Taboo:
            ch_m "I already told you that I wouldn't do that out here!"  
        elif not newgirl["Mystique"].Gagx:
            call MystiqueFace("bemused")
            ch_m "I'm just not into that, [newgirl[Mystique].Petname]. . ."
        elif newgirl["Mystique"].Gagx:
            call MystiqueFace("perplexed")
            ch_m "You could have been a bit more gentle last time, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not, right now [newgirl[Mystique].Petname]. . ."
        menu:
            extend ""
            "Maybe later?":
                call MystiqueFace("sexy")  
                ch_m "I'll give it some thought, [newgirl[Mystique].Petname]."
                $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                if Taboo:                    
                    $ newgirl["Mystique"].RecentActions.append("tabno")                      
                    $ newgirl["Mystique"].DailyActions.append("tabno") 
                return
            "I bet it would feel really good. . .":             
                if Approval:
                    call MystiqueFace("sexy")     
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 2)
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 40, 2) 
                    $ Line = renpy.random.choice(["Well, sure.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_m "[Line]"
                    $ Line = 0                   
                    #jump Mystique_Doggy_AnalPrep
                else:   
                    pass
                    
            "Shut it.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                    ch_m "Ok, fine. If we're going to do this, stick it in already."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump Mystique_GagPrep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)    
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
                    call MystiqueFace("angry")
                    "Mystique shoves you away."
                    $ renpy.pop_call()
                    if Situation:
                        $ renpy.pop_call()
                    call Mystique_Doggy_Reset
                    ch_m "You shut it"
                    ch_m "If that's how you want to treat me, we're done here!"                                                  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                    

    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "That's a bit much, even for you."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)       
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -2)    
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "That you would even suggest such a thing in a place like this. . ."    
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3) 
    else:
        call MystiqueFace("normal", 1)
        ch_m "Not happening."    
    $ Tempmod = 0    
    return

# End Gag Mystique //////////////////////////////////////////////////////////////////////////////////

# newgirl["Mystique"].Gag_Prep ////////////////////////////////////////////////////////////////////////////////

label Mystique_GagPrep:    
            
    #call Mystique_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        
        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Gagx:                
                "Mystique glances around to see if anyone notices what she's doing, then you put the ballgag on her."
                
            else:         
                "Mystique glances around for voyeurs. . ."
                $ newgirl["Mystique"].Mouth = "sucking"
                "Mystique hesitantly opens her mouth."
                "You put the ballgag in her mouth."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Gagx:
                $ newgirl["Mystique"].Mouth = "sucking"
                "Mystique opens her mouth wide."

                "You carefuly put the gag on her."
            else:
                $ newgirl["Mystique"].Mouth = "sucking"

                "Mystique opens her mouth wide."
                "You put the gag on her."
                     
    else: #if Situation == "auto"       

        "You quickly put the ballgag on her mouth."
    $ newgirl["Mystique"].Gag = Gagtype
    
    if not newgirl["Mystique"].Gagx:                                                      #First time stat buffs       
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -150)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 70)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 40) 
        else:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 10)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 30)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 70) 
    elif newgirl["Mystique"].Gagx < 6:                                                   #first few times stat buffs       
        if newgirl["Mystique"].Forced:
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, -20)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 10)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5) 
        else:
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 7)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 5) 
                
    if Situation:    
        #$ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    #$ Cnt = 0
    #$ P_Cock = "anal"
    #$ Trigger = "anal"
    #$ Speed = 1
    if Taboo:
        call DrainWord("Mystique","tabno")
    #call DrainWord("Mystique","no anal")
    #$ newgirl["Mystique"].RecentActions.append("anal")                      
    #$ newgirl["Mystique"].DailyActions.append("anal") 
    return
# End Gag Prep

# Mystique_Doggy_A anal //////////////////////////////////////////////////////////////////////

label Mystique_Doggy_A:
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
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
        if Approval > 2:                                                      # fix, add Mystique auto stuff here
            call Mystique_Doggy_Launch("L")   
            if (newgirl["Mystique"].Legs == "skirt" or newgirl["Mystique"].Legs == "cheerleader skirt"):
                "Mystique turns and backs up against your cock, sliding her skirt up as she does so."
                $ newgirl["Mystique"].Upskirt = 1
            elif newgirl["Mystique"].Legs == "pants":
                "Mystique turns and backs up against your cock, sliding her pants off as she does so."                
                $ newgirl["Mystique"].Legs = 0
            else:
                "Mystique turns and backs up against your cock."
            $ newgirl["Mystique"].SeenPanties = 1
            if newgirl["Mystique"].Plugged:
                "You remove the plug from her asshole"
                $ newgirl["Mystique"].Plugged = 0
            "She slides the tip up to her anus, and presses against it."
            menu:
                "What do you do?"
                "Nothing.":                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 2)
                    "Mystique slides it in."
                "Praise her.":       
                    call MystiqueFace("sexy, 1")                    
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 3) 
                    ch_p "Ooo, dirty girl, [newgirl[Mystique].Pet], let's do this."
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
            jump Mystique_Doggy_AnalPrep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Mystique_Doggy_Launch("L")   
        if (newgirl["Mystique"].Legs == "skirt" or newgirl["Mystique"].Legs == "cheerleader skirt"):
            "You press up against Mystique's backside, sliding her skirt up as you go."
            $ newgirl["Mystique"].Upskirt = 1
        elif newgirl["Mystique"].Legs == "pants":
            "You press up against Mystique's backside, sliding her pants down as you do."                
            $ newgirl["Mystique"].Legs = 0
        else:
            "You press up against Mystique's backside."
        $ newgirl["Mystique"].SeenPanties = 1
        if newgirl["Mystique"].Plugged:
            "You remove the plug from her asshole"
            $ newgirl["Mystique"].Plugged = 0
        "You press the tip of your cock against her tight rim."        
        call MystiqueFace("surprised", 1)
        
        if (newgirl["Mystique"].Anal and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
            if newgirl["Mystique"].Plugged:
                "She removes the plug from her asshole"
                $ newgirl["Mystique"].Plugged = 0
            ch_m "Hmm, stick it in. . ."            
            jump Mystique_Doggy_AnalPrep         
        else:                                                                                                            #she's questioning it
            $ newgirl["Mystique"].Brows = "angry"                
            menu:
                ch_m "Hey, what do you think you're doing back there?!" 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call MystiqueFace("sexy", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_m "I guess if you really want to try it. . ."
                        if newgirl["Mystique"].Plugged:
                            ch_m "Let me just remove this first. . ."
                            "She removes the plug from her asshole"
                            $ newgirl["Mystique"].Plugged = 0
                        jump Mystique_Doggy_AnalPrep
                    "You pull back before you really get it in."                    
                    call MystiqueFace("bemused", 1)
                    if newgirl["Mystique"].Anal:
                        ch_m "Well ok, [newgirl[Mystique].Petname], no harm done. Just give me a little warning next time." 
                    else:
                        ch_m "Well ok, [newgirl[Mystique].Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                "Just fucking.":                    
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)
                    if newgirl["Mystique"].Plugged:
                        "You remove the plug from her asshole and press your dick into her"
                        $ newgirl["Mystique"].Plugged = 0
                    else:
                        "You press into her."                              
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    if not ApprovalCheck("Mystique", 700, "O", TabM=1):                        
                        call MystiqueFace("angry")
                        "Mystique shoves you away and slaps you in the face."
                        ch_m "Jackass!"
                        ch_m "If that's how you want to treat me, we're done here!"                                                  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Mystique_Doggy_Reset
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")                        
                    else:
                        call MystiqueFace("sad")
                        "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                        jump Mystique_Doggy_AnalPrep
        return             
    
   
    if not newgirl["Mystique"].Anal and "no anal" not in newgirl["Mystique"].RecentActions:                                                               #first time    
        call MystiqueFace("surprised", 1)
        $ newgirl["Mystique"].Mouth = "kiss"
        ch_m "Wait, so you want to stick it in my butt?!"
  
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            ch_m "Seriously?"
        
    if not newgirl["Mystique"].Loose and ("dildo anal" in newgirl["Mystique"].DailyActions or "anal" in newgirl["Mystique"].DailyActions):
        call MystiqueFace("bemused", 1)
        ch_m "I'm still a little sore from earlier."
            
    elif "anal" in newgirl["Mystique"].RecentActions:
        call MystiqueFace("sexy", 1)
        ch_m "You want to go again? Ok."
        if newgirl["Mystique"].Plugged:
            "She removes the plug from her asshole"
            $ newgirl["Mystique"].Plugged = 0
        jump Mystique_Doggy_AnalPrep
        
    
    if not newgirl["Mystique"].Anal and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "I guess if you really want to try it. . ."           
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal")
            ch_m "Ok, [newgirl[Mystique].Petname], I'm ready."
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "Well. . . I bet it would feel really good down there."
        else: # Uninhibited 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Mouth = "smile"             
            ch_m "Hmm, it has been on my list. . ."  
    
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's really what you want?"
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Well, at least you got us some privacy this time. . ."   
        elif "anal" in newgirl["Mystique"].DailyActions and not newgirl["Mystique"].Loose:
            pass      
        elif "anal" in newgirl["Mystique"].RecentActions:
            ch_m "I think I'm warmed up. . ."
            if newgirl["Mystique"].Plugged:
                "She removes the plug from her asshole"
                $ newgirl["Mystique"].Plugged = 0
            jump Mystique_Doggy_AnalPrep
        elif "anal" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "I'm still a little sore from earlier.", 
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Anal < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you'd like another go?"       
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to ride your pole?",
                "You wanna dip your wick?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine."   
        elif "no anal" in newgirl["Mystique"].DailyActions:               
            ch_m "Ok, ok, I have been itching for this. . ." 
        else:
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ Line = renpy.random.choice(["Well, sure, stick it in.",                 
                "Well. . . ok.",                 
                "Sure!", 
                "I guess I could. . . stick it in.",
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        if newgirl["Mystique"].Plugged:
            "She removes the plug from her asshole"
            $ newgirl["Mystique"].Plugged = 0
        jump Mystique_Doggy_AnalPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if "no anal" in newgirl["Mystique"].RecentActions:  
            ch_m "What part of \"no,\" did you not get, [newgirl[Mystique].Petname]?"
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no anal" in newgirl["Mystique"].DailyActions:
            ch_m "I already told you that I wouldn't do that out here!"  
        elif "no anal" in newgirl["Mystique"].DailyActions:       
            ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I already told you that I wouldn't do that out here!"  
        elif not newgirl["Mystique"].Anal:
            call MystiqueFace("bemused")
            ch_m "I'm just not into that, [newgirl[Mystique].Petname]. . ."
        elif not newgirl["Mystique"].Loose and "anal" not in newgirl["Mystique"].DailyActions:
            call MystiqueFace("perplexed")
            ch_m "You could have been a bit more gentle last time, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not, right now [newgirl[Mystique].Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no anal" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no anal" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "I'll give it some thought, [newgirl[Mystique].Petname]."
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
                    $ Line = renpy.random.choice(["Well, sure, stick it in.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_m "[Line]"
                    $ Line = 0        
                    if newgirl["Mystique"].Plugged:
                        "She removes the plug from her asshole"  
                        $ newgirl["Mystique"].Plugged = 0         
                    jump Mystique_Doggy_AnalPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -5, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)                 
                    ch_m "Ok, fine. If we're going to do this, stick it in already."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 80, 1) 
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 3)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump Mystique_Doggy_AnalPrep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)    
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1  
    if "no anal" in newgirl["Mystique"].DailyActions:
        ch_m "Learn to take \"no\" for an answer, [newgirl[Mystique].Petname]."   
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
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "That you would even suggest such a thing in a place like this. . ."    
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3) 
    elif not newgirl["Mystique"].Loose and "anal" in newgirl["Mystique"].DailyActions:
        call MystiqueFace("bemused")
        ch_m "Sorry, I just need a little break back there, [newgirl[Mystique].Petname]."    
    elif newgirl["Mystique"].Anal:
        call MystiqueFace("sad") 
        ch_m "The only thing you can do with my ass is kiss it, [newgirl[Mystique].Petname]."
        ch_m ". . .Don't get any ideas."   
    else:
        call MystiqueFace("normal", 1)
        ch_m "Not happening."    
    $ newgirl["Mystique"].RecentActions.append("no anal")                      
    $ newgirl["Mystique"].DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label Mystique_Plug_Ass:
    call Shift_Focus("Mystique")
      
    if newgirl["Mystique"].Loose:
        $ Tempmod += 30   
    elif "anal" in newgirl["Mystique"].RecentActions or "plug anal" in newgirl["Mystique"].RecentActions:
        $ Tempmod -= 20 
    elif "anal" in newgirl["Mystique"].DailyActions or "plug anal" in newgirl["Mystique"].DailyActions:
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
        
    if "no plug" in newgirl["Mystique"].DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no plug" in newgirl["Mystique"].RecentActions else 0   
        
    $ Approval = ApprovalCheck("Mystique", 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    
    if Situation == "Mystique":                                                                  
            #Mystique auto-starts   
            call Mystique_Doggy_Launch("plug") 
        
            if Approval > 2:                                                      # fix, add Mystique auto stuff here
                if newgirl["Mystique"].Legs == "skirt":
                    "Mystique grabs her plug, hiking up her skirt as she does."
                    $ newgirl["Mystique"].Upskirt = 1
                elif newgirl["Mystique"].Legs == "pants":
                    "Mystique grabs her plug, pulling down her pants as she does."              
                    $ newgirl["Mystique"].Legs = 0
                else:
                    "Mystique grabs her plug, rubbing it suggestively against her ass."
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
                        "You grab the plug and slide it in."
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 85, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 2)
                    "Ask her to stop.":
                        call MystiqueFace("surprised")       
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [newgirl[Mystique].Pet]."
                        call Mystique_Namecheck
                        "Mystique sets the plug down."
                        call MystiqueOutfit
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 90, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, 2)
                        return            
                jump MystiquePA_Prep
            else:                
                $ Tempmod = 0                               # fix, add Mystique auto stuff here
                $ Trigger2 = 0
            return            
    
    if Situation == "auto":    
            call Mystique_Doggy_Launch("massage")  

            "You rub the plug across her body, and against her tight anus."
            call MystiqueFace("surprised", 1)
            
            if (newgirl["Mystique"].DildoA and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it         
                "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                call MystiqueFace("sexy")
                $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                ch_m "Ok, [newgirl[Mystique].Petname], let's do this."            
                jump MystiquePA_Prep         
            else:                                                                                                            
                #she's questioning it
                $ newgirl["Mystique"].Brows = "angry"                
                menu:
                    ch_m "Hey, what do you think you're doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call MystiqueFace("sexy", 1)
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                            ch_m "Well, since you're be'in so nice about it, I guess we can give it a go. . ."
                            jump MystiquePA_Prep
                        "You pull back before you really get it in."                    
                        call MystiqueFace("bemused", 1)
                        if newgirl["Mystique"].DildoA:
                            ch_m "Well ok, [newgirl[Mystique].Petname], no harm done. Just give me a little warning next time." 
                        else:
                            ch_m "Well ok, [newgirl[Mystique].Petname], I'm not really ready for that, but maybe if you ask nicely next time . . ."                                               
                    "Just playing with my favorite toys.":                    
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)
                        "You press it inside some more."                              
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        if not ApprovalCheck("Mystique", 700, "O", TabM=1): #Checks if Obed is 700+                           
                            call MystiqueFace("angry")
                            "Mystique shoves you away and slaps you in the face."
                            ch_m "Jackass!"
                            ch_m "If that's how you want to treat me, we're done here!"                                                  
                            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                            if newgirl["Mystique"].Plugged:
                                "She removes the plug from her asshole"
                                $ newgirl["Mystique"].Plugged = 0
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Mystique_Doggy"):
                                call Mystique_Doggy_Reset  
                            $ newgirl["Mystique"].RecentActions.append("angry")
                            $ newgirl["Mystique"].DailyActions.append("angry")                         
                        else:
                            call MystiqueFace("sad")
                            "Mystique doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump MystiquePA_Prep
            return             
    #end auto
   
    if not newgirl["Mystique"].DildoA:                                                               
            #first time    
            call MystiqueFace("surprised", 1)
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "Hmmm, so you'd like to try out some toys?"    
            if newgirl["Mystique"].Forced:
                call MystiqueFace("sad")
                ch_m "You had to go for the butt, uh?"
    
    if not newgirl["Mystique"].Loose and ("dildo anal" in newgirl["Mystique"].RecentActions or "plug anal" in newgirl["Mystique"].RecentActions or "anal" in newgirl["Mystique"].RecentActions or "dildo anal" in newgirl["Mystique"].DailyActions or "plug anal" in newgirl["Mystique"].DailyActions or "anal" in newgirl["Mystique"].DailyActions):
            call MystiqueFace("bemused", 1)
            ch_m "I'm still a bit sore from earlier. . ."
            
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
            elif "plug anal" in newgirl["Mystique"].DailyActions and not newgirl["Mystique"].Loose:
                pass
            elif "plug anal" in newgirl["Mystique"].DailyActions:
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
                    "You want to stick it in my ass again?",
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
                    "Hells yeah.",
                    "Heh, ok, ok."]) 
                ch_m "[Line]"
                $ Line = 0
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 20, 1)
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
            jump MystiquePA_Prep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call MystiqueFace("angry")
            if "no plug" in newgirl["Mystique"].RecentActions:  
                ch_m "What part of \"no,\" did you not get, [newgirl[Mystique].Petname]?"
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no plug" in newgirl["Mystique"].DailyActions:
                ch_m "Stop swinging that thing around in public!"  
            elif "no plug" in newgirl["Mystique"].DailyActions:       
                ch_m "I already told you \"no,\" [newgirl[Mystique].Petname]."
            elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
                ch_m "I already told you that I wouldn't do that out here!"  
            elif not newgirl["Mystique"].DildoA:
                call MystiqueFace("bemused")
                ch_m "I'm just not into toys, [newgirl[Mystique].Petname]. . ."
            elif not newgirl["Mystique"].Loose and "plug anal" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("perplexed")
                ch_m "You could have been a bit more gentle last time, [newgirl[Mystique].Petname]. . ."
            else:
                call MystiqueFace("bemused")
                ch_m "I don't think we need any toys, [newgirl[Mystique].Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no plug" in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("bemused")
                    ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                    return
                "Maybe later?" if "no plug" not in newgirl["Mystique"].DailyActions:
                    call MystiqueFace("sexy")  
                    ch_m "Maybe I'll practice on my own time, [newgirl[Mystique].Petname]."
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2)  
                    if Taboo:                    
                        $ newgirl["Mystique"].RecentActions.append("tabno")                      
                        $ newgirl["Mystique"].DailyActions.append("tabno") 
                    $ newgirl["Mystique"].RecentActions.append("no plug")                      
                    $ newgirl["Mystique"].DailyActions.append("no plug") 
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
                        jump MystiquePA_Prep
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
                        jump MystiquePA_Prep
                    else:                              
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -20)    
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1   
    if "no plug" in newgirl["Mystique"].DailyActions:
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
    elif not newgirl["Mystique"].Loose and "plug anal" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("bemused")
            ch_m "Sorry, I just need a little break back there, [newgirl[Mystique].Petname]."    
    elif newgirl["Mystique"].DildoA:
            call MystiqueFace("sad") 
            ch_m "Sorry, you can keep your toys out of there."     
    else:
            call MystiqueFace("normal", 1)
            ch_m "No way." 
    $ newgirl["Mystique"].RecentActions.append("no plug")                      
    $ newgirl["Mystique"].DailyActions.append("no plug")   
    $ Tempmod = 0    
    return

label MystiquePA_Prep:  
            
    call Mystique_Doggy_Launch("massage")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_m "Well, I guess some things are necessary, [newgirl[Mystique].Petname]."
            
        if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
            "She quickly pulls down her pants and drops her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Mystique") >= 5 and newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Hose] and drops her [newgirl[Mystique].Panties]."
            $ newgirl["Mystique"].Hose = 0
        elif HoseNum("Mystique") >= 5:
            "She quickly pulls down her [newgirl[Mystique].Hose], exposing her bare ass."
            $ newgirl["Mystique"].Hose = 0
        elif newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Panties]."  
            
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless
        
        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Anal:                
                "Mystique glances around to see if anyone notices what she's doing, then backs her ass up against the plug."
                #"You guide your cock into place and ram it home."   
                
            else:         
                "Mystique glances around for voyeurs. . ."
                "Mystique slowly backs up against the plug."
                #"You guide it into place and slide it in."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Anal:
                "Mystique bends over and presses her backside against the plug suggestively."
                #"You take careful aim and then push your cock in."
            else:
                "Mystique slowly backs up against the plug."
                #"You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
            "You quickly pull down her pants and her [newgirl[Mystique].Panties] and press the plug against her ass."
        if newgirl["Mystique"].Panties and newgirl["Mystique"].Legs != "pants":
            "You quickly pull down her [newgirl[Mystique].Panties] and press the plug against her ass."  
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless(1)
        
    #call Seen_First_Peen(1)
    call Mystique_Doggy_Reset
    call Mystique_Doggy_Launch("plug")
    
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
    $ P_Cock = "plug"
    $ Trigger = "plug"
    $ Speed = 0
    if Taboo:
        call DrainWord("Mystique","tabno")
    call DrainWord("Mystique","no anal")
    $ newgirl["Mystique"].RecentActions.append("plug anal")                      
    $ newgirl["Mystique"].DailyActions.append("plug anal")


label Mystique_Anal_Plug_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Doggy_Launch("plug") 
        call MystiqueLust        
        $ P_Cock = "plug"
        $ Trigger = "plug"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Can you finish there? I'm getting a little sore."   
        elif Cnt == (10 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "angry"        
                    ch_m "I'm . . .getting . . .worn out. . . here, . . [newgirl[Mystique].Petname]."
                    menu:
                        ch_m "Can we. . . do something. . . else?"
                        "Let's try something else." if MultiAction: 
                                if Speed != 0:
                                    "But keep the plug inside you."
                                    $ newgirl["Mystique"].Plugged = 1
                                    $ Speed = 0
                                $ Line = 0
                                call Mystique_Doggy_Reset
                                $ Situation = "shift"
                                jump Mystique_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_m "Well if that's your attitude you can handle your own business."                         
                                    if newgirl["Mystique"].Plugged:
                                        "She removes the plug from her asshole"
                                        $ newgirl["Mystique"].Plugged = 0
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Doggy_AnalAfter
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
                                    "Nevermind":
                                        pass
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Gag":
                            if not newgirl["Mystique"].Gag:
                                #"You put a gag on Mystique"
                            #            $ newgirl["Mystique"].Gag = "ballgag"
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call Mystique_Gagging("ballgag")
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Gagging("ballgag")
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call Mystique_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call Mystique_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Mystique's gag"
                                $ newgirl["Mystique"].Gag = 0
                           
                        #"Leave it in" if Speed:                    
                        #            $ Speed = 2
                        #            $ newgirl["Mystique"].Plugged = 1
                        #            "You leave the plug inside her ass."

                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call Mystique_Slap_Ass 
                                    hide Slap_Ass2                                    
                                    jump Mystique_Anal_Plug_Cycle  
                                    
                           
                        "Maybe lose some clothes. . .":
                                    call Mystique_Undress             
                        
                        "Shift actions":
                            if newgirl["Mystique"].Action and MultiAction:
                                if Speed != 0:
                                    "You leave the plug inside her asshole"
                                    $ newgirl["Mystique"].Plugged = 1
                                    $ Speed = 0
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_P
                                    "Start hotdogging her.":
                                            $ Situation = "pullback"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_H
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call Mystique_Doggy_HotdogAfter
                                            call Mystique_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Doggy_HotdogAfter
                                            call Mystique_Doggy_A
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
                           
                        "Let's try something else." if MultiAction: 
                                    menu:
                                        "And keep the plug inside":
                                            $ newgirl["Mystique"].Plugged = 1
        
                                        "And you can remove the plug":
                                            $ newgirl["Mystique"].Plugged = 0
        
                                    call Mystique_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction:
                                    menu:
                                        "But keep the plug inside":
                                            $ newgirl["Mystique"].Plugged = 1
        
                                        "And you can remove the plug":
                                            $ newgirl["Mystique"].Plugged = 0
         
                                    call Mystique_Doggy_Reset
                                    $ Line = 0
                                    jump Mystique_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Doggy_Reset
                                if newgirl["Mystique"].Plugged:
                                    "She removes the plug from her asshole"
                                    $ newgirl["Mystique"].Plugged = 0
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_Doggy"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Doggy_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Doggy_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Anal_Plug_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."

    return


label Mystique_Doggy_AnalPrep:  
            
    call Mystique_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off        
        if newgirl["Mystique"].Panties or newgirl["Mystique"].Legs or HoseNum("Mystique") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_m "Well, I guess some things are necessary, [newgirl[Mystique].Petname]."
            
        if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
            "She quickly pulls down her pants and drops her [newgirl[Mystique].Panties]."
        elif newgirl["Mystique"].Legs == "pants":
            "She quickly pulls down her pants, exposing her bare ass."
        elif HoseNum("Mystique") >= 5 and newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Hose] and drops her [newgirl[Mystique].Panties]."
            $ newgirl["Mystique"].Hose = 0
        elif HoseNum("Mystique") >= 5:
            "She quickly pulls down her [newgirl[Mystique].Hose], exposing her bare ass."
            $ newgirl["Mystique"].Hose = 0
        elif newgirl["Mystique"].Panties:
            "She quickly pulls down her [newgirl[Mystique].Panties]."  
            
        $ newgirl["Mystique"].Upskirt = 1
        $ newgirl["Mystique"].PantiesDown = 1       
        $ newgirl["Mystique"].SeenPanties = 1
        call Mystique_First_Bottomless
        
        if newgirl["Mystique"].Plugged:
            "She removes the plug from her asshole."
            $ newgirl["Mystique"].Plugged = 0


        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Anal:                
                "Mystique glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Mystique glances around for voyeurs. . ."
                "Mystique hesitantly pulls down your pants and slowly backs up against your rigid member."
                "You guide it into place and slide it in."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Anal:
                "Mystique bends over and presses her backside against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                "Mystique hesitantly pulls down your pants slowly backs up against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if newgirl["Mystique"].Legs == "pants" and newgirl["Mystique"].Panties:
            "You quickly pull down her pants and her [newgirl[Mystique].Panties] and press against her ass."
        if newgirl["Mystique"].Panties and newgirl["Mystique"].Legs != "pants":
            "You quickly pull down her [newgirl[Mystique].Panties] and press against her ass."  
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

label Mystique_Doggy_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Doggy_Launch("anal") 
        call MystiqueLust        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Are you getting close here? I'm getting a little sore."   
        elif Cnt == (10 + newgirl["Mystique"].Anal):
                    $ newgirl["Mystique"].Brows = "angry"        
                    ch_m "I'm . . .getting . . .worn out. . . here, . . [newgirl[Mystique].Petname]."
                    menu:
                        ch_m "Can we. . . do something. . . else?"
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                if newgirl["Mystique"].Anal >= 5 and newgirl["Mystique"].Blow >= 10 and newgirl["Mystique"].SEXP >= 50:
                                    $ Situation = "shift"
                                    call Mystique_Doggy_AnalAfter
                                    call Mystique_Blowjob      
                                else:
                                    ch_m "No thanks, [newgirl[Mystique].Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call Mystique_Doggy_AnalAfter
                                    call MystiqueHJ_Prep   
                        "How about a Handy?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Doggy_AnalAfter
                                call Mystique_Handjob     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Doggy_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Doggy_Reset
                                $ Situation = "shift"
                                jump Mystique_Doggy_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Doggy_Reset
                                    "She scowls at you and pulls out."
                                    ch_m "Well if that's your attitude you can handle your own business."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Doggy_AnalAfter
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
                                    "Nevermind":
                                        pass
                        "Keep going. . ." if Speed:
                                    pass
                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                            
                        "Speed up. . ." if Speed < 2:                    
                                    $ Speed = 2
                                    "You ask her to up the pace a bit."
                        "Speed up. . ." if Speed == 2:
                                    $ Speed = 3  #anal
                                    "You start pounding her ass as fast as you can"

                        "Balls deep." if Speed == 3 :                    
                                    $ Speed = 4
                                    "You go balls deep."
                        
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Gag":
                            if not newgirl["Mystique"].Gag:
                                #"You put a gag on Mystique"
                            #            $ newgirl["Mystique"].Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call Mystique_Gagging("ballgag")
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Gagging("ballgag")
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call Mystique_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call Mystique_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Mystique's gag"
                                $ newgirl["Mystique"].Gag = 0

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call Mystique_Slap_Ass 
                                    hide Slap_Ass2                                   
                                    jump Mystique_Doggy_Anal_Cycle  

                                    
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
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_P
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Doggy_H
                                    "How about the plug?":
                                            $ Situation = "shift"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Plug_Ass
                                    "Just stick the plug in her ass [[without asking]." if not newgirl["Mystique"].Plugged:
                                            $ Situation = "auto"
                                            call Mystique_Doggy_AnalAfter
                                            call Mystique_Plug_Ass
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
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Doggy_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Line = 0
                                    jump Mystique_Doggy_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Doggy_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_Doggy_AnalAfter 
                            $ Line = "came"
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_Doggy"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Doggy_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Doggy_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Doggy_Launch(Trigger)
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Doggy_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Doggy_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump Mystique_Doggy_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Doggy_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Doggy_Reset
        
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
            ch_m "I. . . really think I enjoy this. . ."                  
    elif newgirl["Mystique"].Anal == 1:            
            $ newgirl["Mystique"].SEXP += 25        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was . . . interesting [newgirl[Mystique].Petname]. We'll have to do that again sometime."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "Ouch."
                    ch_m "Did you get what you needed here?"
    elif newgirl["Mystique"].Anal == 5:
            ch_m "We're making a regular habit of this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "That felt . . . good. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return   


# End R Doggy Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Mystique_Doggy_A hotdog //////////////////////////////////////////////////////////////////////

label Mystique_Doggy_H: 
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
    
    if Situation == "Mystique":                                                                  #Mystique auto-starts   
        if Approval > 2:                                                      # fix, add Mystique auto stuff here
            call Mystique_Doggy_Launch("L") 
            "Mystique turns and backs up against your cock, rubbing it against her ass."
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
            jump Mystique_Doggy_HotdogPrep
        else:                
            $ Tempmod = 0                               # fix, add Mystique auto stuff here
            $ Trigger2 = 0
        return            
    
    if Situation == "auto":   
        call Mystique_Doggy_Launch("L")   
        "You press up against Mystique's backside."    
        call MystiqueFace("surprised", 1)
        
        if (newgirl["Mystique"].Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
            "Mystique is briefly startled and turns towards you, but then smiles and makes a little humming noise."
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
            ch_m "Hmm, I've apparently got someone's attention. . ."            
            jump Mystique_Doggy_HotdogPrep         
        else:                                                                                                            #she's questioning it
            $ newgirl["Mystique"].Brows = "angry"                
            menu:
                ch_m "Hmm, kinda rude, [newgirl[Mystique].Petname]." 
                "Sorry, sorry! Never mind.":
                    if Approval:     
                        call MystiqueFace("sexy", 1)
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 1) 
                        ch_m "I guess it doesn't feel so bad. . ."
                        jump Mystique_Doggy_HotdogPrep
                    "You pull back before you really get it in."                    
                    call MystiqueFace("bemused", 1)
                    if newgirl["Mystique"].Hotdog:
                        ch_m "Well ok, [newgirl[Mystique].Petname], it has been kinda fun." 
                    else:
                        ch_m "Well ok, [newgirl[Mystique].Petname], that's a bit dirty, maybe ask a girl?"                                               
                "You'll see.":                    
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -10, 1)  
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -8)
                    "You grind against her asscrack."                              
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 70, 3)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 50, 3) 
                    if not ApprovalCheck("Mystique", 500, "O", TabM=1): #Checks if Obed is 700+  
                        call MystiqueFace("angry")
                        "Mystique shoves you away."
                        ch_m "Dick!"
                        ch_m "If that's how you want want to act, I'm out of here!"                                                  
                        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -10, 1)                        
                        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)
                        $ renpy.pop_call()
                        if Situation:
                            $ renpy.pop_call()
                        call Mystique_Doggy_Reset
                        $ newgirl["Mystique"].RecentActions.append("angry")
                        $ newgirl["Mystique"].DailyActions.append("angry")                       
                    else:
                        call MystiqueFace("sad")
                        "Mystique doesn't seem to be into this, but she's knows her place."                        
                        jump Mystique_Doggy_HotdogPrep
        return             
    
   
    if not newgirl["Mystique"].Hotdog and "no hotdog" not in newgirl["Mystique"].RecentActions:                                                               #first time    
        call MystiqueFace("surprised", 1)
        $ newgirl["Mystique"].Mouth = "kiss"
        ch_m "Wait, so you want to grind against my butt?!"
  
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            ch_m ". . . That's all?"
        
        
    if not newgirl["Mystique"].Hotdog and Approval:                                                 #First time dialog        
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
        elif newgirl["Mystique"].Love >= (newgirl["Mystique"].Obed + newgirl["Mystique"].Inbt):
            call MystiqueFace("sexy")
            $ newgirl["Mystique"].Brows = "sad"
            $ newgirl["Mystique"].Mouth = "smile" 
            ch_m "It looks like you need some relief. . ."           
        elif newgirl["Mystique"].Obed >= newgirl["Mystique"].Inbt:
            call MystiqueFace("normal")
            ch_m "If that's what you need, [newgirl[Mystique].Petname]."
        elif newgirl["Mystique"].Addict >= 50:
            call MystiqueFace("manic", 1)
            ch_m "Hmmm. . ."
        else: # Uninhibited 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Mouth = "smile"             
            ch_m "Hmm, you look ready for it, at least. . ."    
            
    elif Approval:                                                                       #Second time+ dialog
        if newgirl["Mystique"].Forced: 
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -3, 1)
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 20, -2, 1)
            ch_m "That's all you want?"  
        elif not Taboo and "tabno" in newgirl["Mystique"].DailyActions:        
            ch_m "Well, at least you got us some privacy this time. . ."   
        elif "hotdog" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("sexy", 1)
            ch_m "You want to go again? Ok."
            jump Mystique_Doggy_HotdogPrep
        elif "hotdog" in newgirl["Mystique"].DailyActions:
            call MystiqueFace("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty. . .", 
                "Are you sure that's all you want?"]) 
            ch_m "[Line]"
        elif newgirl["Mystique"].Hotdog < 3:        
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Brows = "confused"
            $ newgirl["Mystique"].Mouth = "kiss"
            ch_m "So you'd like another go?"       
        else:       
            call MystiqueFace("sexy", 1)
            $ newgirl["Mystique"].Girl_Arms = 2
            $ Line = renpy.random.choice(["You want some of this action?",                 
                "So you'd like another go?",                 
                "You can't stay away from this booty.", 
                "You want me to slick your pole?"]) 
            ch_m "[Line]"
        $ Line = 0
            
    if Approval >= 2:                                                                   #She's into it. . .               
        if newgirl["Mystique"].Forced:
            call MystiqueFace("sad")
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 1)
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 1)
            ch_m "Ok, fine."    
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
                "Hells yeah.",
                "Heh, ok, ok."]) 
            ch_m "[Line]"
            $ Line = 0
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 60, 1)
        $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 70, 2) 
        jump Mystique_Doggy_HotdogPrep   
    
    else:                                                                               #She's not into it, but maybe. . .            
        call MystiqueFace("angry")
        if "no hotdog" in newgirl["Mystique"].RecentActions:  
            ch_m "I {i}just{/i} told you \"no,\" [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions and "no hotdog" in newgirl["Mystique"].DailyActions: 
            ch_m "I told you that I didn't want you rubb'in up on me in public!" 
        elif "no hotdog" in newgirl["Mystique"].DailyActions:       
            ch_m "I told you \"no\" earlier, [newgirl[Mystique].Petname]."
        elif Taboo and "tabno" in newgirl["Mystique"].DailyActions:  
            ch_m "I told you that I didn't want you rubb'in up on me in public!"     
        elif not newgirl["Mystique"].Hotdog:
            call MystiqueFace("bemused")
            ch_m "That's kinda naughty, [newgirl[Mystique].Petname]. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "Not, right now [newgirl[Mystique].Petname]. . ."
        menu:
            extend ""
            "Sorry, never mind." if "no hotdog" in newgirl["Mystique"].DailyActions:
                call MystiqueFace("bemused")
                ch_m "Yeah, ok, [newgirl[Mystique].Petname]."              
                return
            "Maybe later?" if "no hotdog" not in newgirl["Mystique"].DailyActions:
                call MystiqueFace("sexy")  
                ch_m "Yeah, maybe, [newgirl[Mystique].Petname]."
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
                    $ Line = renpy.random.choice(["Well, sure, give it a rub.",     
                        "I suppose. . .", 
                        "You've got me there."]) 
                    ch_m "[Line]"
                    $ Line = 0                   
                    jump Mystique_Doggy_HotdogPrep
                else:   
                    pass
                    
            "Bend over.":                                               # Pressured into it
                $ Approval = ApprovalCheck("Mystique", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and newgirl["Mystique"].Forced):
                    call MystiqueFace("sad")
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -2, 1)
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -2)                 
                    ch_m "Ok, fine. Whatever."  
                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 4)
                    $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 60, 2)  
                    $ newgirl["Mystique"].Forced = 1  
                    jump Mystique_Doggy_HotdogPrep
                else:                              
                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -10)     
                    $ newgirl["Mystique"].RecentActions.append("angry")
                    $ newgirl["Mystique"].DailyActions.append("angry")   
    
    #She refused all offers.
    $ newgirl["Mystique"].Girl_Arms = 1      
    
    if "no hotdog" in newgirl["Mystique"].DailyActions:
        ch_m "I just don't want to, [newgirl[Mystique].Petname]."   
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    if newgirl["Mystique"].Forced:
        call MystiqueFace("angry", 1)
        ch_m "Even that's not worth it."
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 70, -1) if newgirl["Mystique"].Love > 300 else newgirl["Mystique"].Love
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1)  
        $ newgirl["Mystique"].RecentActions.append("angry")
        $ newgirl["Mystique"].DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call MystiqueFace("angry", 1)        
        $ newgirl["Mystique"].RecentActions.append("tabno")                      
        $ newgirl["Mystique"].DailyActions.append("tabno") 
        ch_m "I'd be a bit embarassed doing that here."  
        $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5)  
        $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -3)  
    elif newgirl["Mystique"].Hotdog:
        call MystiqueFace("sad") 
        ch_m "Eh-eh, not anymore, [newgirl[Mystique].Petname]."
    else:
        call MystiqueFace("normal", 1)
        ch_m "Not interested."    
    $ newgirl["Mystique"].RecentActions.append("no hotdog")                      
    $ newgirl["Mystique"].DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label Mystique_Doggy_HotdogPrep:  
    call Mystique_Doggy_Launch("hotdog")
    
    if Situation != "auto":
        call Mystique_Bottoms_Off    
        
        if Taboo: # Mystique gets started. . .
            if newgirl["Mystique"].Hotdog:                
                "Mystique glances around to see if anyone notices what she's doing, then backs her ass up against your cock."
                
            else:         
                "Mystique glances around for voyeurs. . ."
                "Mystique hesitantly pulls down your pants and slowly backs up against your rigid member."
            $ newgirl["Mystique"].Inbt += int(Taboo/10)  
            $ newgirl["Mystique"].Lust += int(Taboo/5)
        else:    
            if not newgirl["Mystique"].Hotdog:
                "Mystique bends over and presses her backside against you suggestively."
            else:
                "Mystique hesitantly pulls down your pants slowly backs up against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her ass."
    
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

label Mystique_Doggy_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Mystique")
        call Mystique_Doggy_Launch("hotdog") 
        call MystiqueLust        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
            
        if Cnt == (5 + newgirl["Mystique"].Hotdog):
                    $ newgirl["Mystique"].Brows = "confused"
                    ch_m "Are you getting close here?"   
        elif Cnt == (10 + newgirl["Mystique"].Hotdog):
                    $ newgirl["Mystique"].Brows = "angry"        
                    menu:
                        ch_m "I'm kinda done with this, [newgirl[Mystique].Petname]."
                        "How about a BJ?" if newgirl["Mystique"].Action and MultiAction:
                                $ Situation = "shift"
                                call Mystique_Doggy_HotdogAfter
                                call Mystique_Blowjob       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Mystique_Doggy_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Mystique_Doggy_Reset
                                $ Situation = "shift"
                                jump Mystique_Doggy_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Mystique", 1200) or ApprovalCheck("Mystique", 500, "O"):                        
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 200, -5)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, 3)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call MystiqueFace("angry", 1)   
                                    call Mystique_Doggy_Reset
                                    "She scowls at you and pulls away."
                                    ch_m "Well if that's your attitude you can handle your own business."                         
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 50, -3, 1)
                                    $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, -4, 1)
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 30, -1, 1)                    
                                    $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 50, -1, 1)  
                                    $ newgirl["Mystique"].RecentActions.append("angry")
                                    $ newgirl["Mystique"].DailyActions.append("angry")   
                                    jump Mystique_Doggy_HotdogAfter
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
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
                                        ch_p "Nice"
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

                        "Gag":
                            if not newgirl["Mystique"].Gag:
                                #"You put a gag on Mystique"
                            #            $ newgirl["Mystique"].Gag = 2
                            #        
                                menu:
                                    "How about using a ballgag?":
                                        $ Situation = "shift"
                                        call Mystique_Gagging("ballgag")
                                    "Just put the ballgag in her mouth [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Gagging("ballgag")
                                    #"How about using a ringgag?":
                                    #    $ Situation = "shift"
                                    #    call Mystique_Gagging("ringgag")
                                    #"Just put the ringgag in her mouth [[without asking].":
                                    #    $ Situation = "auto"
                                    #    call Mystique_Gagging("ringgag")
                                    "Nevermind.":
                                        pass
                            else:
                                "You remove Mystique's gag"
                                $ newgirl["Mystique"].Gag = 0

                        # "Blindfold her" if newgirl["Mystique"].Bondage and not newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You add a blindfold so she can't see a thing"
                        #     $ newgirl["Mystique"].Blindfold = 1
            
                        # "Remove blindfold" if newgirl["Mystique"].Blindfold:
                        #     call MystiqueFace("sexy", 1) 
                        #     "You remove the blindfold"
                        #     $ newgirl["Mystique"].Blindfold = 0
                            
                        "Slow Down. . ." if Speed:                    
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:                
                                    pass
                            
                        "Slap her ass":                     
                                    show Slap_Ass2 zorder 200
                                    call Mystique_Slap_Ass 
                                    hide Slap_Ass2                                   
                                    jump Mystique_Doggy_Hotdog_Cycle  
                                    
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
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Doggy_P
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Doggy_P
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Doggy_A
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Doggy_A
                                    "How about the plug?":
                                        $ Situation = "shift"
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Plug_Ass
                                    "Just stick the plug in her ass [[without asking]." if not newgirl["Mystique"].Plugged:
                                        $ Situation = "auto"
                                        call Mystique_Doggy_HotdogAfter
                                        call Mystique_Plug_Ass
                                    "Never Mind":
                                        pass
                            else:
                                ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if newgirl["Mystique"].Action and MultiAction:
                                    call Mystique_Offhand_Set
                                    if Trigger2:
                                         $ newgirl["Mystique"].Action -= 1
                                else:
                                    ch_m "I'm actually getting a little tired, so maybe we could wrap this up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump Mystique_Doggy_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Mystique_Doggy_Reset
                                    $ Line = 0
                                    jump Mystique_Doggy_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Mystique",Partner)
                
        #If either of you could cum 
        if P_Focus >= 100 or newgirl["Mystique"].Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call Mystique_P_Cumming
                            if "angry" in newgirl["Mystique"].RecentActions:  
                                call Mystique_Doggy_Reset
                                return    
                            $ newgirl["Mystique"].Lust = Statupdate("Mystique", "Lust", newgirl["Mystique"].Lust, 200, 5) 
                            if 100 > newgirl["Mystique"].Lust >= 70 and newgirl["Mystique"].OCount < 2:             
                                $ newgirl["Mystique"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Mystique"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Mystique_Doggy_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Mystique can cum
                    if renpy.showing("Mystique_Doggy"):                    #If you're still going at it,
                        if newgirl["Mystique"].Lust >= 100:                                               
                            call Mystique_Cumming
                            if Situation == "shift" or "angry" in newgirl["Mystique"].RecentActions:
                                jump Mystique_Doggy_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump Mystique_Doggy_SexAfter
                        elif "unsatisfied" in newgirl["Mystique"].RecentActions:#And Mystique is unsatisfied,                    
                            call Mystique_Doggy_Launch("hotdog")
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump Mystique_Doggy_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump Mystique_Doggy_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump Mystique_Doggy_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_m "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_m "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call MystiqueFace("bemused", 0)
    $ Line = 0
    ch_m "Ok, [newgirl[Mystique].Petname], that's enough of that for now."
    
    

    
label Mystique_Doggy_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Mystique_Doggy_Reset
        
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
    
    if "Mystique Full Buns" in Achievements:
            pass 
            
    elif newgirl["Mystique"].Hotdog >= 10:
        $ newgirl["Mystique"].SEXP += 5
        $ Achievements.append("Mystique Full Buns")
        if not Situation:
            call MystiqueFace("smile", 1)
            ch_m "I think I'm getting addicted to this."               
    elif newgirl["Mystique"].Hotdog == 1:            
            $ newgirl["Mystique"].SEXP += 10        
            if not Situation: 
                if newgirl["Mystique"].Love >= 500 and "unsatisfied" not in newgirl["Mystique"].RecentActions:
                    ch_m "That was pretty hot, [newgirl[Mystique].Petname], we'll have to do that again sometime."
                elif newgirl["Mystique"].Obed <= 500 and P_Focus <= 20:
                    $ newgirl["Mystique"].Mouth = "sad"
                    ch_m "Did you get what you needed here?"
    elif newgirl["Mystique"].Hotdog == 5:
            ch_m "This is. . . interesting."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry")
            $ newgirl["Mystique"].Eyes = "side"
            ch_m "That didn't really do it for me. . ."
        else:
            call MystiqueFace("bemused")
            ch_m "That was an interesting diversion. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_m "Mmm, so what else did you have in mind?"
    call Checkout
    return  

label Mystique_Appearance:
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
            ch_p "Nice"
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
            ch_p "Nice"
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
            ch_p "Nice"
        "Nevermind":
            pass 
    return

# End R Doggy hotdogging //////////////////////////////////////////////////////////////////////////////////

    
    