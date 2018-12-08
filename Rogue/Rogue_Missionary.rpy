# Start Rogue Sex pose //////////////////////////////////////////////////////////////////////////////////
# R_Sex_P //////////////////////////////////////////////////////////////////////

label R_Sex_P:  
    call Shift_Focus("Rogue") from _call_Shift_Focus_281
    if R_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif R_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif R_Sex: #You've done it before
        $ Tempmod += 10    
        
    if R_Addict >= 75 and (R_CreamP + R_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif R_Addict >= 75:
        $ Tempmod += 15
        
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if Situation == "shift":
        $ Tempmod += 10 
    if "exhibitionist" in R_Traits:    
        $ Tempmod += (4*Taboo)      
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
    
    
        
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no sex" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no sex" in R_RecentActions else 0                  
             
        
    $ Approval = ApprovalCheck("Rogue", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    
    if Situation == "Rogue":                                                                  #Rogue auto-starts   
                if Approval > 2:                                                      # fix, add Rogue auto stuff here
                    call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_1   
                    if R_Legs == "skirt":
                        "Rogue slides onto her back and pulls you against her, sliding her skirt up as she does so."
                        $ R_Upskirt = 1
                    elif R_Legs == "capris" or R_Legs == "black jeans":
                        "Rogue slides onto her back and pulls you against her, sliding her pants off as she does so." 
                        $ R_Upskirt = 1
                    elif R_Legs == "shorts":
                        "Rogue slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                        $ R_Upskirt = 1
                    else:
                        "Rogue slides onto her back and pulls you against her."
                    $ R_SeenPanties = 1
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":                    
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                            "Rogue slides it in."
                        "Praise her.":       
                            call RogueFace("sexy, 1") from _call_RogueFace_1267                    
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                            ch_p "Oh yeah, [R_Pet], let's do this."
                            call Rogue_Namecheck from _call_Rogue_Namecheck_10
                            "Rogue slides it in."
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                        "Ask her to stop.":
                            call RogueFace("surprised") from _call_RogueFace_1268       
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                            ch_p "Let's not do that right now, [R_Pet]."
                            call Rogue_Namecheck from _call_Rogue_Namecheck_11
                            "Rogue pulls back."
                            call RogueOutfit from _call_RogueOutfit_72
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)
                            return            
                    jump R_Missionary_SexPrep
                    # End high approval
                else:                
                    $ Tempmod = 0                               # fix, add Rogue auto stuff here
                    $ Trigger2 = 0
                return   
    #End Rogue's lead
    
    if Situation == "auto":   
                call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_2   
                if R_Legs == "skirt":
                    "You press Rogue down onto her back, sliding her skirt up as you go."
                    $ R_Upskirt = 1                
                elif R_Legs == "capris" or R_Legs == "black jeans":
                    "You press Rogue down onto her back, sliding her pants down as you do."    
                    $ R_Upskirt = 1
                elif R_Legs == "shorts":
                    "You press Rogue down onto her back, sliding her shorts down as you do."                
                    $ R_Upskirt = 1
                else:
                    "You press Rogue down onto her back."
                $ R_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."        
                call RogueFace("surprised", 1) from _call_RogueFace_1269
                
                if (R_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it         
                    "Rogue is briefly startled, but melts into a sly smile."
                    call RogueFace("sexy") from _call_RogueFace_1270
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                    ch_r "Oh. . . game on, [R_Petname]."            
                    jump R_Missionary_SexPrep         
                else:                                                                                                            
                    #she's questioning it
                    $ R_Brows = "angry"                
                    menu:
                        ch_r "Um, what do you think you're doing?" 
                        "Sorry, sorry! Never mind.":
                            if Approval:     
                                    call RogueFace("sexy", 1) from _call_RogueFace_1271
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                                    ch_r "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                                    jump R_Missionary_SexPrep
                            else:
                                    "You pull back before you really get it in."                    
                                    call RogueFace("bemused", 1) from _call_RogueFace_1272
                                    if R_Sex:
                                        ch_r "Maybe you could warn me?" 
                                    else:
                                        ch_r "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                            
                        "Just fucking.":                    
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                            "You press inside some more."                              
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                            if not ApprovalCheck("Rogue", 700, "O", TabM=1):   #Checks if Obed is 700+                          
                                call RogueFace("angry") from _call_RogueFace_1273
                                "Rogue shoves you away and slaps you in the face."
                                ch_r "Jerk!"
                                ch_r "I am not putting up with that shit!"                                                  
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_1
                                $ R_RecentActions.append("angry")
                                $ R_DailyActions.append("angry")                    
                            else:
                                call RogueFace("sad") from _call_RogueFace_1274
                                "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                                jump R_Missionary_SexPrep
                return   
    #End Auto
    
   
    if not R_Sex and "no sex" not in R_RecentActions:                           
            #first time    
            call RogueFace("surprised", 1) from _call_RogueFace_1275
            $ R_Mouth = "kiss"
            ch_r "I haven't really had much experience with this. . . "    
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1276
                ch_r "You'd really do this when you have me over a barrel?"
            
            
    if not R_Sex and Approval:                                                  
            #First time dialog        
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1277
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -30, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -20, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy") from _call_RogueFace_1278
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "I don't want you to think I'm some kind of slut. . ."            
            elif R_Obed >= R_Inbt:
                call RogueFace("normal") from _call_RogueFace_1279
                ch_r "I suppose if it's you, [R_Petname]. . ."            
            elif R_Addict >= 50:
                call RogueFace("manic", 1) from _call_RogueFace_1280
                ch_r "I have kind of been hoping you might. . ."
            else: # Uninhibited 
                call RogueFace("sad") from _call_RogueFace_1281
                $ R_Mouth = "smile"             
                ch_r "I can't say it hasn't crossed my mind. . ."   
            #End first time dialog
            
    elif Approval:                                                                      
            #Second time+ dialog        
            call RogueFace("sexy", 1) from _call_RogueFace_1282
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1283
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
                ch_r "Again? Why do you do this to me?" 
            elif not Taboo and "tabno" in R_DailyActions:        
                ch_r "I guess this is more secluded. . ."        
            elif "sex" in R_RecentActions:
                ch_r "Another round? {i}Fine.{/i}"
                jump R_Missionary_SexPrep
            elif "sex" in R_DailyActions:
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_r "[Line]"
            elif R_Sex < 3:        
                $ R_Brows = "confused"
                $ R_Mouth = "kiss"
                ch_r "So you'd like another round?"       
            else:       
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "You can't stay away from this. . .", 
                    "You gonna make me purr?",
                    "You wanna slide into me?"]) 
                ch_r "[Line]"
            $ Line = 0
            #end Second time+ dialog
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1284
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                ch_r "Ok, fiiiiine."  
            elif "no sex" in R_DailyActions:               
                ch_r "You've made your case. . ."
            else:
                call RogueFace("sexy", 1) from _call_RogueFace_1285
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
            jump R_Missionary_SexPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .    
            call RogueFace("angry") from _call_RogueFace_1286       
            if "no sex" in R_RecentActions:  
                ch_r "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in R_DailyActions and "no sex" in R_DailyActions:  
                ch_r "I already told you. . .not in public!" 
            elif "no sex" in R_DailyActions:       
                ch_r "I already told you \"no.\""
            elif Taboo and "tabno" in R_DailyActions:  
                ch_r "I already told you this is too public!"     
            elif not R_Sex:
                call RogueFace("bemused") from _call_RogueFace_1287
                ch_r "I don't know that I'm. . . ready? . ."
            else:
                call RogueFace("bemused") from _call_RogueFace_1288
                ch_r "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in R_DailyActions:
                        call RogueFace("bemused") from _call_RogueFace_1289
                        ch_r "It's cool."
                        return
                "Maybe later?" if "no sex" not in R_DailyActions:
                        call RogueFace("sexy") from _call_RogueFace_1290  
                        ch_r "Maybe, you never know."
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)   
                        if Taboo:                    
                            $ R_RecentActions.append("tabno")                      
                            $ R_DailyActions.append("tabno") 
                        $ R_RecentActions.append("no sex")                      
                        $ R_DailyActions.append("no sex")            
                        return
                "I think you'd enjoy it as much as I would. . .":             
                        if Approval:
                            call RogueFace("sexy") from _call_RogueFace_1291     
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                            $ Line = renpy.random.choice(["That's. . . true. . .",     
                                "I suppose. . .", 
                                "That's. . . that's a good point. . ."]) 
                            ch_r "[Line]"
                            $ Line = 0                   
                            jump R_Missionary_SexPrep       
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Rogue", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and R_Forced):
                            call RogueFace("sad") from _call_RogueFace_1292
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                 
                            ch_r "Well! . .  ok, fine, stick it in."  
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                            $ R_Forced = 1  
                            jump R_Missionary_SexPrep
                        else:                          
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20)   
                            $ R_RecentActions.append("angry")
                            $ R_DailyActions.append("angry")  
                #end menu
    #end Approval check
    
    #She refused all offers.
    $ Rogue_Arms = 1  
    if "no sex" in R_DailyActions:
        ch_r "Maybe take \"no\" for an answer?" 
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1293
        ch_r "Not even."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)    
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)     
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1) from _call_RogueFace_1294
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r "I can't believe you'd even consider it around here!"      
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)
    elif R_Sex:
        call RogueFace("sad") from _call_RogueFace_1295 
        ch_r "Maybe just fuck yourself, huh?."       
    else:
        call RogueFace("normal", 1) from _call_RogueFace_1296
        ch_r "Nuhuh."     
    $ R_RecentActions.append("no sex")                      
    $ R_DailyActions.append("no sex") 
    $ Tempmod = 0    
    return

label R_Missionary_SexPrep:
    call Rogue_Sex_Launch("hotdog") from _call_Rogue_Sex_Launch_3
    
    if Situation != "auto":
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_16       
        
        
        if R_Panties or R_Legs or HoseNum("Rogue") >= 5: #If she refuses to take off her pants but agreed to sex
            ch_r "We can't exactly do much like this, huh."
        
        if R_Panties == "zipper panties":
            "She pulls the zippers down"
            $ R_Panties = "zipper panties open"
            if R_Chest == "bustier bra":
                $ R_Chest = "bustier bra open"
        elif R_Panties == "zipper panties open":
            ch_r "I'm ready"    
        elif R_Panties and (R_Legs == "capris" or R_Legs == "black jeans"):
            "She quickly drops her pants and her [R_Panties]."
        elif R_Panties and R_Legs == "shorts":
            "She quickly drops her shorts and her [R_Panties]."
        elif R_Legs == "capris" or R_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif R_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Rogue") >= 5 and R_Panties:
            "She shrugs and her [R_Hose] and [R_Panties] fall to the ground."
            $ R_Hose = 0
        elif HoseNum("Rogue") >= 5:
            "She shrugs and her [R_Hose] fall to the ground."
            $ R_Hose = 0
        elif R_Panties:
            "She shrugs as her [R_Panties] fall to the ground."  
            
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless from _call_Rogue_First_Bottomless_30
        
        if Taboo: # Rogue gets started. . .
            if not R_Sex:
                "Rogue glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Rogue slowly presses against your rigid member."
                else:
                    "Rogue hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Rogue glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:    
            if not R_Sex:
                if "cockout" in P_RecentActions:
                    "Rogue slowly presses against your rigid member."
                else:
                    "Rogue hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Rogue leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."
                            
    else:  #if Situation == "auto"  
        if R_Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ R_Panties = "zipper panties open"
            if R_Chest == "bustier bra":
                $ R_Chest = "bustier bra open"
        elif R_Panties == "zipper panties open":
            "You get ready"    
        else:     
            if R_Legs == "pants" and R_Panties:
                "You quickly pull down her pants and her [R_Panties] and press against her slit."
            if R_Panties and R_Legs != "pants":
                "You quickly pull down her [R_Panties] and press against her slit."  
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_31
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_31
    
    if not R_Sex:        
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -150)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 60)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 50) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 30)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 60) 
    
    if Situation:   
        $ renpy.pop_call() 
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_214
    call DrainWord("Rogue","no sex") from _call_DrainWord_215
    $ R_RecentActions.append("sex")                      
    $ R_DailyActions.append("sex") 

label R_Missionary_Sex_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_282
        call Rogue_Sex_Launch("sex") from _call_Rogue_Sex_Launch_4 
        call RogueLust from _call_RogueLust_15        
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ R_Upskirt = 1
        $ R_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Sex):
                    $ R_Brows = "confused"
                    ch_r "So are we getting close here?"   
        elif Cnt == (10 + R_Sex):
                    $ R_Brows = "angry"        
                    ch_r "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_Missionary_SexAfter from _call_R_Missionary_SexAfter
                                call R_Blowjob from _call_R_Blowjob_6       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Missionary_Sex_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_2
                                $ Situation = "shift"
                                jump R_Missionary_SexAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1297   
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_3
                                    "She scowls at you and pulls out."
                                    ch_r "Not with that attitude, mister!"
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_Missionary_SexAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    if ("master" in R_Petnames or "sir" in R_Petnames or R_Pet == "slave") and ApprovalCheck("Rogue", 750, "O") and not R_Bondage: # bondage event
                        $ R_Bondage = 1
                        ch_r "Hey, [R_Petname], I've got some new things here, do you think we could try them?"
                        "She grabs what it looks like some bondage gear"
                        menu:
                            "Yep":
                                call RogueFace("sexy", 1) from _call_RogueFace_1298 
                                #if R_Over or R_Chest or R_Panties or R_Legs:
                                #    "She glances up at you as her clothes drop to the ground."
                                #$ R_Over = 0
                                #$ R_Legs = 0
                                #$ R_Chest = 0
                                #$ R_Panties = 0
                                "She starts dressing the new outfit"
                                "You help her with the armbinder, making sure she can't move her arms"
                                #"And add a blindfold so she can't see a thing"
                                #$ R_Blindfold = 1
                                $ R_Over = "armbinder"
                                #$ R_Chest = "bustier bra"
                                #$ R_Panties = "zipper panties"
                                #$ R_Outfit = "zipper bondage"
                                #$ R_Shame = R_OutfitShame[1]
                                #if R_Over == "armbinder":
                                #call RogueFace("sly")
                                $ Line = "Rogue can't move her arms. She licks her lips in anticipation"
                                $ TempLust += 3 if R_Lust < 40 else 1  

                                #if R_Blow <= 1 or (R_Obed >= 500 and R_Obed > R_Inbt):
                                #        $ TempLust += 2 if R_Lust > 60 else 0                 
                                #        $ Line = Line + ", but she seems to be waiting for some instruction"
                                #else:
                                #        $ Line = Line + ", and then she gets started licking your cock"
                                #        $ Speed = 1
                                #jump R_HotdogPrep
                                #pass
                                #call Rogue_Bottoms_Off_Legs
                                #call Rogue_Top_Off
                                #call Rogue_Bottoms_Off
                                #shes gonna wear it
                            "Not now, but let's save it for another time":
                                pass
                                #nope
                    menu:
                        "[Line]"
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

                        "How about you put that armbinder" if R_Bondage and R_Over != "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1299 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "armbinder"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the armbinder" if R_Over == "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1300 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put that bondage outfit" if R_Bondage and R_Over != "bondage":
                            call RogueFace("sexy", 1) from _call_RogueFace_1301 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put those bondage cuffs" if R_Bondage and R_Over != "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1302 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage cuffs"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the bondage outfit" if R_Over == "bondage" or R_Over == "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1303 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_14                                    
                                    jump R_Missionary_Sex_Cycle 

                        "Put her legs up" if not R_LegsUp:
                                    $ R_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if R_LegsUp:
                                    $ R_LegsUp = 0
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
                                    call R_Undress from _call_R_Undress_16  
                        
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about anal?":
                                            $ Situation = "shift"
                                            call R_Missionary_SexAfter from _call_R_Missionary_SexAfter_1
                                            call R_Sex_A from _call_R_Sex_A
                                    "Just stick it in her ass [[without asking].":
                                            $ Situation = "auto"
                                            call R_Missionary_SexAfter from _call_R_Missionary_SexAfter_2
                                            call R_Sex_A from _call_R_Sex_A_1
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call R_Missionary_SexAfter from _call_R_Missionary_SexAfter_3
                                            call R_Sex_H from _call_R_Sex_H
                                    "Never Mind":
                                            pass
                            else:
                                ch_r "I'm kinda tired here? Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_20
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_4
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_Missionary_SexAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_5
                                    $ Line = 0
                                    jump R_Missionary_SexAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_72
        
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                     
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_12
                            if "angry" in R_RecentActions:  
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_6
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_Missionary_SexAfter 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_SexSprite"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming from _call_R_Cumming_23
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_Missionary_SexAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_Missionary_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Sex_Launch(Trigger) from _call_Rogue_Sex_Launch_5
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Missionary_Sex_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."
                                    jump R_Missionary_SexAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump R_Missionary_SexAfter
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1304
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_Missionary_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_7
        
    call RogueFace("sexy") from _call_RogueFace_1305 
    
    $ R_Sex += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 2) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed Rogue" in R_RecentActions: #If Rogue was participating
        $ R_LikeRogue += 2 if R_LikeRogue >= 800 else 1
    
    if "Rogue Sex Addict" in Achievements:
            pass 
            
    elif R_Sex >= 10:
        $ R_SEXP += 5
        $ Achievements.append("Rogue Sex Addict")
        if not Situation:
            call RogueFace("smile", 1) from _call_RogueFace_1306
            ch_r "I just can't seem to quit you."               
    elif R_Sex == 1:            
            $R_SEXP += 20        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I feel like I've been waiting a million years for that."
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "I hope that was worth the wait."
    elif R_Sex == 5:
            ch_r "Why did we not do this sooner?!"  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry") from _call_RogueFace_1307
            $ R_Eyes = "side"
            ch_r "Could you have maybe paid more attention? . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1308
            ch_r "Hmm. . ."
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Did you want to try something else?"
    call Checkout from _call_Checkout_101
    return   

# End Rogue sex //////////////////////////////////////////////////////////////////////////////////


# Rogue anal //////////////////////////////////////////////////////////////////////

label R_Sex_A:
    call Shift_Focus("Rogue") from _call_Shift_Focus_283
    if R_Anal >= 7: # She loves it
        $ Tempmod += 20   
    elif R_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif R_Anal: #You've done it before
        $ Tempmod += 15 
        
    if R_Addict >= 75 and (R_CreamP + R_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif R_Addict >= 75: 
        $ Tempmod += 15
    
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
        
    if R_Loose:
        $ Tempmod += 10  
    elif "anal" in R_RecentActions:
        $ Tempmod -= 20 
    elif "anal" in R_DailyActions:
        $ Tempmod -= 10
        
    if Situation == "shift":
        $ Tempmod += 10    
    if "exhibitionist" in R_Traits:
        $ Tempmod += (5*Taboo) 
        
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10      
    elif "ex" in R_Traits:
        $ Tempmod -= 40  
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount
        
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
    if "no anal" in R_DailyActions:               
        $ Tempmod -= 5         
        $ Tempmod -= 10 if "no anal" in R_RecentActions else 0  
            
    $ Approval = ApprovalCheck("Rogue", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    
    if Situation == "Rogue":                                                                  
            #Rogue auto-starts   
            if Approval > 2:                                                      # fix, add Rogue auto stuff here
                call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_6   
                if R_Legs == "skirt":
                    "Rogue slides onto her back and pulls you against her, sliding her skirt up as she does so."
                    $ R_Upskirt = 1
                elif R_Legs == "capris" or R_Legs == "black jeans":
                    "Rogue slides onto her back and pulls you against her, sliding her pants off as she does so." 
                    $ R_Upskirt = 1
                elif R_Legs == "shorts":
                    "Rogue slides onto her back and pulls you against her, sliding her shorts off as she does so."    
                    $ R_Upskirt = 1
                else:
                    "Rogue slides onto her back and pulls you against her."
                $ R_SeenPanties = 1
                "She slides the tip up to her back door, and presses against it."
                menu:
                    "What do you do?"
                    "Nothing.":                    
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                        "Rogue slides it in."
                    "Praise her.":       
                        call RogueFace("sexy, 1") from _call_RogueFace_1309                    
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 3) 
                        ch_p "Ooo, dirty girl, [R_Pet], let's do this."
                        call Rogue_Namecheck from _call_Rogue_Namecheck_12
                        "Rogue slides it in."
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    "Ask her to stop.":
                        call RogueFace("surprised") from _call_RogueFace_1310       
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [R_Pet]."
                        call Rogue_Namecheck from _call_Rogue_Namecheck_13
                        "Rogue pulls back."
                        call RogueOutfit from _call_RogueOutfit_73
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                    
                        return            
                jump R_Missionary_AnalPrep
            else:                
                $ Tempmod = 0                               # fix, add Rogue auto stuff here
                $ Trigger2 = 0
            return  
            #end if Rogue initiates
    
    if Situation == "auto":   
            call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_7   
            if R_Legs == "skirt":
                "You press Rogue down onto her back, sliding her skirt up as you go."
                $ R_Upskirt = 1                
            elif R_Legs == "capris" or R_Legs == "black jeans":
                "You press Rogue down onto her back, sliding her pants down as you do."    
                $ R_Upskirt = 1
            elif R_Legs == "shorts":
                "You press Rogue down onto her back, sliding her shorts down as you do."                
                $ R_Upskirt = 1
            else:
                "You press Rogue down onto her back."
            $ R_SeenPanties = 1
            "You press the tip of your cock against her tight rim."        
            call RogueFace("surprised", 1) from _call_RogueFace_1311
            
            if (R_Anal and Approval) or (Approval > 1):                                                                      
                #this is not the first time you've had sex, or she's into it    
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                if R_Loose:
                    "Rogue is briefly startled, but melts into a sly smile."
                    ch_r "Hmm, stick it in. . ."            
                else:
                    "Rogue is briefly startled, but shrugs."
                    ch_r "Oookay. . ."                  
                jump R_Missionary_AnalPrep         
            else:                                                                                                            
                #she's questioning it
                $ R_Brows = "angry"                
                menu:
                    ch_r "Um what are you doing back there?!" 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call RogueFace("sexy", 1) from _call_RogueFace_1312
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                            ch_r "Well just take it easy, ok? . ."
                            jump R_Missionary_AnalPrep
                        "You pull back before you really get it in."                    
                        call RogueFace("bemused", 1) from _call_RogueFace_1313
                        
                        if R_Anal:
                            ch_r "Maybe you could warn me?" 
                        else:
                            ch_r "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."                                           
                    "Just fucking.":                    
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -8)
                        "You press into her."                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        if not ApprovalCheck("Rogue", 700, "O", TabM=1):                        
                            call RogueFace("angry") from _call_RogueFace_1314
                            "Rogue shoves you away and slaps you in the face."
                            ch_r "Asshole!"
                            ch_r "You need to ask nicer than that!"                                                  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_8
                            $ R_RecentActions.append("angry")
                            $ R_DailyActions.append("angry")                        
                        else:
                            call RogueFace("sad") from _call_RogueFace_1315
                            "Rogue doesn't seem to be into this, you're lucky she's so obedient."                        
                            jump R_Missionary_AnalPrep
            return  
            #end "auto" 
    
   
    if not R_Anal and "no anal" not in R_RecentActions:                                                               
            #first time    
            call RogueFace("surprised", 1) from _call_RogueFace_1316
            $ R_Mouth = "kiss"
            ch_r "You want to go in the \"out\" door?!"
      
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1317
                ch_r "Anal? Really?"
        
    if not R_Loose and ("dildo anal" in R_DailyActions or "anal" in R_DailyActions):
            #if she's done anal stuff today
            call RogueFace("bemused", 1) from _call_RogueFace_1318
            ch_r "I'm not really over the last time."            
    elif "anal" in R_RecentActions:
            call RogueFace("sexy", 1) from _call_RogueFace_1319
            ch_r "Again? K."
            jump R_Missionary_AnalPrep
        
    
    if not R_Anal and Approval:                                                 
            #First time dialog        
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1320
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy") from _call_RogueFace_1321
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "I guess? . ."           
            elif R_Obed >= R_Inbt:
                call RogueFace("normal") from _call_RogueFace_1322
                ch_r "Well. . ."
            elif R_Addict >= 50:
                call RogueFace("manic", 1) from _call_RogueFace_1323
                ch_r "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited 
                call RogueFace("sad") from _call_RogueFace_1324
                $ R_Mouth = "smile"             
                ch_r "Anything's worth a shot. . ."  
    
    elif Approval:                                                                       
            #Second time+ dialog
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1325
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
                ch_r "You really ask a lot here. . ."
            elif not Taboo and "tabno" in R_DailyActions:        
                ch_r "I guess this is out of the way. . ."   
            elif "anal" in R_DailyActions and not R_Loose:
                pass      
            elif "anal" in R_RecentActions:
                ch_r "I guess I'm warmed up. . ."
                jump R_Missionary_AnalPrep
            elif "anal" in R_DailyActions:
                call RogueFace("sexy", 1) from _call_RogueFace_1326
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "I'm still a little sore from earlier.", 
                    "Didn't get enough earlier?",
                    "You're wearing me out here!."]) 
                ch_r "[Line]"    
            else:       
                call RogueFace("sexy", 1) from _call_RogueFace_1327
                $ Rogue_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                 
                    "I do have booty for days. . .", 
                    "You gonna make me purr?",
                    "You wanna slide into me?"]) 
                ch_r "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                   
            #She's into it. . .               
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1328
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                ch_r "Ok, fine."   
            elif "no anal" in R_DailyActions:               
                ch_r "Well, ok, I've given it some thought, fine. . ." 
            else:
                call RogueFace("sexy", 1) from _call_RogueFace_1329
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Well. . . ok.",                 
                    "Sure!", 
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 20, 1)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
            jump R_Missionary_AnalPrep   
               
    else:                                                                               
            #She's not into it, but maybe. . .            
            call RogueFace("angry") from _call_RogueFace_1330
            if "no anal" in R_RecentActions:  
                ch_r "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in R_DailyActions and "no anal" in R_DailyActions:
                ch_r "I already told you. . .not in public!" 
            elif "no anal" in R_DailyActions:       
                ch_r "I already told you \"no.\""
            elif Taboo and "tabno" in R_DailyActions:  
                ch_r "I already told you this is too public!"      
            elif not R_Anal:
                call RogueFace("bemused") from _call_RogueFace_1331
                ch_r "I don't know that I'm. . . that kind of girl?"
            elif not R_Loose and "anal" not in R_DailyActions:
                call RogueFace("perplexed") from _call_RogueFace_1332
                ch_r "That was kind of. . . rough last time?"
            else:
                call RogueFace("bemused") from _call_RogueFace_1333
                ch_r "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in R_DailyActions:
                    call RogueFace("bemused") from _call_RogueFace_1334
                    ch_r "It's cool."              
                    return
                "Maybe later?" if "no anal" not in R_DailyActions:
                    call RogueFace("sexy") from _call_RogueFace_1335  
                    ch_r "Maybe, you never know."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)  
                    if Taboo:                    
                        $ R_RecentActions.append("tabno")                      
                        $ R_DailyActions.append("tabno") 
                    $ R_RecentActions.append("no anal")                      
                    $ R_DailyActions.append("no anal") 
                    return
                "I bet it would feel really good. . .":             
                    if Approval:
                        call RogueFace("sexy") from _call_RogueFace_1336     
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["That's. . . true. . .",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_r "[Line]"
                        $ Line = 0                   
                        jump R_Missionary_AnalPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and R_Forced):
                        call RogueFace("sad") from _call_RogueFace_1337
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                 
                        ch_r "Well! . .  ok, fine, stick it in."  
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 1) 
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                        $ R_Forced = 1  
                        jump R_Missionary_AnalPrep
                    else:                              
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20)    
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1  
    if "no anal" in R_DailyActions:
        ch_r "Maybe take \"no\" for an answer?"   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1338
        ch_r "That's a bit much, even for you."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)       
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)    
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             
        # she refuses and this is too public a place for her
        call RogueFace("angry", 1) from _call_RogueFace_1339
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r "You're being ridiculous. That? Here?!"    
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3) 
    elif not R_Loose and "anal" in R_DailyActions:
        call RogueFace("bemused") from _call_RogueFace_1340
        ch_r "I'm a little sore here?"    
    elif R_Anal:
        call RogueFace("sad") from _call_RogueFace_1341 
        ch_r "That's totally off the table."
    else:
        call RogueFace("normal", 1) from _call_RogueFace_1342
        ch_r "Noooop."    
    $ R_RecentActions.append("no anal")                      
    $ R_DailyActions.append("no anal") 
    $ Tempmod = 0    
    return

label R_Missionary_AnalPrep:    
            
    call Rogue_Sex_Launch("hotdog") from _call_Rogue_Sex_Launch_8
    
    if Situation != "auto":
        call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_17        
        if R_Panties or R_Legs or HoseNum("Rogue") >= 5: #If she refuses to take off her pants but agreed to anal
            ch_r "We can't exactly do much like this, huh."

        if R_Panties == "zipper panties":
            "She pulls the zippers down"
            $ R_Panties = "zipper panties open"
            if R_Chest == "bustier bra":
                $ R_Chest = "bustier bra open"
        elif R_Panties == "zipper panties open":
            ch_r "I'm ready"  
        elif R_Panties and (R_Legs == "capris" or R_Legs == "black jeans"):
            "She quickly drops her pants and her [R_Panties]."
        elif R_Panties and R_Legs == "shorts":
            "She quickly drops her shorts and her [R_Panties]."
        elif R_Legs == "capris" or R_Legs == "black jeans":
            "She shrugs and her pants drop through her, exposing her bare pussy."
        elif R_Legs == "shorts":
            "She shrugs and her shorts drop through her, exposing her bare pussy."
        elif HoseNum("Rogue") >= 5 and R_Panties:
            "She shrugs and her [R_Hose] and [R_Panties] fall to the ground."
            $ R_Hose = 0
        elif HoseNum("Rogue") >= 5:
            "She shrugs and her [R_Hose] fall to the ground."
            $ R_Hose = 0
        elif R_Panties:
            "She shrugs as her [R_Panties] fall to the ground."  
            
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless from _call_Rogue_First_Bottomless_32
        
        if Taboo: # Rogue gets started. . .
            if R_Anal:                
                "Rogue glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."   
                
            else:         
                "Rogue glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Rogue slowly presses against your rigid member."
                else:
                    "Rogue hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:    
            if not R_Anal:
                "Rogue leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in P_RecentActions:
                    "Rogue slowly presses against your rigid member."
                else:
                    "Rogue hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."
                     
    else: #if Situation == "auto"       
        if R_Panties == "zipper panties":
            "You quickly pull the zippers down"
            $ R_Panties = "zipper panties open"
            if R_Chest == "bustier bra":
                $ R_Chest = "bustier bra open"
        elif R_Panties == "zipper panties open":
            "You get ready"  
        else: 
            if R_Legs == "pants" and R_Panties:
                "You quickly pull down her pants and her [R_Panties] and press against her back door."
            if R_Panties and R_Legs != "pants":
                "You quickly pull down her [R_Panties] and press against her back door."  
        $ R_Upskirt = 1
        $ R_PantiesDown = 1       
        $ R_SeenPanties = 1
        call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_33
        
    call Seen_First_Peen(1) from _call_Seen_First_Peen_32
    
    if not R_Anal:                                                      #First time stat buffs       
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -150)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 70)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 40) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 70) 
    elif not R_Loose:                                                   #first few times stat buffs       
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5) 
        else:
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 7)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5) 
                
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_216
    call DrainWord("Rogue","no anal") from _call_DrainWord_217
    $ R_RecentActions.append("anal")                      
    $ R_DailyActions.append("anal") 

label R_Missionary_Anal_Cycle: #Repeating strokes
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_284
        call Rogue_Sex_Launch("anal") from _call_Rogue_Sex_Launch_9 
        call RogueLust from _call_RogueLust_16        
        $ P_Cock = "anal"
        $ Trigger = "anal"
        $ R_Upskirt = 1
        $ R_PantiesDown = 1  
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Anal):
                    $ R_Brows = "confused"
                    if R_Loose:
                        ch_r "So are we getting close here?"  
                    else:
                        ch_r "So are we getting close here? This is not super pleasant. . ."   
        elif Cnt == (10 + R_Anal):
                    $ R_Brows = "angry"        
                    ch_r "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_r "Can we. . . do something. . . else?"
                        "How about a BJ?" if R_Action and MultiAction:
                                if R_Anal >= 5 and R_Blow >= 10 and R_SEXP >= 50:
                                    $ Situation = "shift"
                                    call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter
                                    call R_Blowjob from _call_R_Blowjob_7      
                                else:
                                    ch_r "No thanks, [R_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter_1
                                    call RHJ_Prep from _call_RHJ_Prep_2   
                        "How about a Handy?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter_2
                                call R_Handjob from _call_R_Handjob_4     
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Missionary_Anal_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_9
                                $ Situation = "shift"
                                jump R_Missionary_AnalAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1343   
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_10
                                    "She scowls at you and pulls out."
                                    ch_r "Not with that attitude, mister!"                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_Missionary_AnalAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    if ("master" in R_Petnames or "sir" in R_Petnames or R_Pet == "slave") and ApprovalCheck("Rogue", 750, "O") and not R_Bondage: # bondage event
                        $ R_Bondage = 1
                        ch_r "Hey, [R_Petname], I've got some new things here, do you think we could try them?"
                        "She grabs what it looks like some bondage gear"
                        menu:
                            "Yep":
                                call RogueFace("sexy", 1) from _call_RogueFace_1344 
                                #if R_Over or R_Chest or R_Panties or R_Legs:
                                #    "She glances up at you as her clothes drop to the ground."
                                #$ R_Over = 0
                                #$ R_Legs = 0
                                #$ R_Chest = 0
                                #$ R_Panties = 0
                                "She starts dressing the new outfit"
                                "You help her with the armbinder, making sure she can't move her arms"
                                #"And add a blindfold so she can't see a thing"
                                #$ R_Blindfold = 1
                                $ R_Over = "armbinder"
                                #$ R_Chest = "bustier bra"
                                #$ R_Panties = "zipper panties"
                                #$ R_Outfit = "zipper bondage"
                                #$ R_Shame = R_OutfitShame[1]
                                #if R_Over == "armbinder":
                                #call RogueFace("sly")
                                $ Line = "Rogue can't move her arms. She licks her lips in anticipation"
                                $ TempLust += 3 if R_Lust < 40 else 1  

                                #if R_Blow <= 1 or (R_Obed >= 500 and R_Obed > R_Inbt):
                                #        $ TempLust += 2 if R_Lust > 60 else 0                 
                                #        $ Line = Line + ", but she seems to be waiting for some instruction"
                                #else:
                                #        $ Line = Line + ", and then she gets started licking your cock"
                                #        $ Speed = 1
                                #jump R_HotdogPrep
                                #pass
                                #call Rogue_Bottoms_Off_Legs
                                #call Rogue_Top_Off
                                #call Rogue_Bottoms_Off
                                #shes gonna wear it
                            "Not now, but let's save it for another time":
                                pass
                                #nope
                    menu:
                        "[Line]"
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

                        "How about you put that armbinder" if R_Bondage and R_Over != "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1345 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "armbinder"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the armbinder" if R_Over == "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1346 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put that bondage outfit" if R_Bondage and R_Over != "bondage":
                            call RogueFace("sexy", 1) from _call_RogueFace_1347 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put those bondage cuffs" if R_Bondage and R_Over != "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1348 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage cuffs"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the bondage outfit" if R_Over == "bondage" or R_Over == "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1349 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_15                                    
                                    jump R_Missionary_Anal_Cycle  

                        "Put her legs up" if not R_LegsUp:
                                    $ R_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if R_LegsUp:
                                    $ R_LegsUp = 0
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
                                    call R_Undress from _call_R_Undress_17  
                        
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                            $ Situation = "shift"
                                            call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter_3
                                            call R_Sex_P from _call_R_Sex_P
                                    "Just stick it in her pussy [[without asking].":
                                            $ Situation = "auto"
                                            call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter_4
                                            call R_Sex_P from _call_R_Sex_P_1
                                    "Pull back to hotdog her.":
                                            $ Situation = "pullback"
                                            call R_Missionary_AnalAfter from _call_R_Missionary_AnalAfter_5
                                            call R_Sex_H from _call_R_Sex_H_1
                                    "Never Mind":
                                            pass
                            else:
                                ch_r "I'm kinda tired here? Could we wrap it up?" 
                    
                        "I also want to. . . [[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_21
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_11
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_Missionary_AnalAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_12
                                    $ Line = 0
                                    jump R_Missionary_AnalAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_73
                
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                        
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_13
                            if "angry" in R_RecentActions:  
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_13
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_Missionary_AnalAfter 
                            $ Line = "came"
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_SexSprite"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming from _call_R_Cumming_24
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_Missionary_AnalAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_Missionary_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Sex_Launch(Trigger) from _call_Rogue_Sex_Launch_10
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs inside her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Missionary_Anal_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                
                                    jump R_Missionary_AnalAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."                                
                                    jump R_Missionary_AnalAfter
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1350
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_Missionary_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_14
        
    call RogueFace("sexy") from _call_RogueFace_1351 
    
    $ R_Anal += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 3) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed Rogue" in R_RecentActions: #If Rogue was participating
        $ R_LikeRogue += 2 if R_LikeRogue >= 800 else 1
    
    if "Rogue Anal Addict" in Achievements:
            pass 
            
    elif R_Anal >= 10:
        $ R_SEXP += 7
        $ Achievements.append("Rogue Anal Addict")
        if not Situation:
            call RogueFace("bemused", 1) from _call_RogueFace_1352
            ch_r "I didn't think I'd love this so much!"                  
    elif R_Anal == 1:            
            $R_SEXP += 25        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "Anal. . . huh, who knew?"
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "Ouch."
                    ch_r "I guess you got what you needed?"
    elif R_Anal == 5:
            ch_r "I'm really starting to love this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry") from _call_RogueFace_1353
            $ R_Eyes = "side"
            ch_r  "Hmm, you seemed to get more out of that then me. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1354
            ch_r "Ok, that was fun. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_102
    return   


# End Rogue Anal //////////////////////////////////////////////////////////////////////////////////
    

  
# Rogue hotdog //////////////////////////////////////////////////////////////////////

label R_Sex_H: 
    call Shift_Focus("Rogue") from _call_Shift_Focus_285
    if R_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif R_Hotdog: #You've done it before
        $ Tempmod += 5    
    
    if R_Lust > 85:
        $ Tempmod += 10
    elif R_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10   
    if "exhibitionist" in R_Traits:
        $ Tempmod += (3*Taboo)  
    if "dating" in R_Traits or "sex friend" in R_Petnames:
        $ Tempmod += 10
    elif "ex" in R_Traits:
        $ Tempmod -= 40 
    if R_ForcedCount and not R_Forced:
        $ Tempmod -= 5 * R_ForcedCount 
    
    if Taboo and "tabno" in R_DailyActions:        
        $ Tempmod -= 10 
        
    if "no hotdog" in R_DailyActions:               
        $ Tempmod -= 5 
        $ Tempmod -= 10 if "no hotdog" in R_RecentActions else 0      
        
    $ Approval = ApprovalCheck("Rogue", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
    
    if Situation == "Rogue":                                                                  
            #Rogue auto-starts   
            if Approval > 2:                                                      # fix, add Rogue auto stuff here
                call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_11 
                "Rogue slides onto her back and pulls you against her, rubbing it against her mound."
                menu:
                    "What do you do?"
                    "Nothing.":                     
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        "Rogue starts to grind against you."
                    "Praise her.":       
                        call RogueFace("sexy, 1") from _call_RogueFace_1355                    
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 2) 
                        ch_p "Hmmm, that's good, [R_Pet]."
                        call Rogue_Namecheck from _call_Rogue_Namecheck_14
                        "Rogue starts to grind against you."
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 85, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 2)
                    "Ask her to stop.":
                        call RogueFace("surprised") from _call_RogueFace_1356       
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                        ch_p "Let's not do that right now, [R_Pet]."
                        call Rogue_Namecheck from _call_Rogue_Namecheck_15
                        "Rogue pulls back."
                        call RogueOutfit from _call_RogueOutfit_74
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 2)                    
                        return            
                jump R_Missionary_HotdogPrep
            else:                
                $ Tempmod = 0                               # fix, add Rogue auto stuff here
                $ Trigger2 = 0
            return            
            #end Rogue initates
    
    if Situation == "auto":   
            call Rogue_Sex_Launch("L") from _call_Rogue_Sex_Launch_12   
            "You press Rogue down onto her back and press your cock against her."    
            call RogueFace("surprised", 1) from _call_RogueFace_1357
            
            if (R_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it         
                "Rogue is briefly startled, but melts into a sly smile."
                call RogueFace("sexy") from _call_RogueFace_1358
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                ch_r "Hmm, I've apparently got someone's attention. . ."            
                jump R_Missionary_HotdogPrep         
            else:                                                                                                            #she's questioning it
                $ R_Brows = "angry"                
                menu:
                    ch_r "Hmm, kinda rude, [R_Petname]." 
                    "Sorry, sorry! Never mind.":
                        if Approval:     
                            call RogueFace("sexy", 1) from _call_RogueFace_1359
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
                            ch_r "I guess it doesn't feel so bad. . ."
                            jump R_Missionary_HotdogPrep
                        "You pull back from her."                    
                        call RogueFace("bemused", 1) from _call_RogueFace_1360
                        ch_r "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"                                             
                    "You'll see.":                    
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10, 1)  
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -8)
                        "You grind against her crotch."                              
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3) 
                        if not ApprovalCheck("Rogue", 500, "O", TabM=1): #Checks if Obed is 700+  
                            call RogueFace("angry") from _call_RogueFace_1361
                            "Rogue shoves you away."
                            ch_r "Jerk!"
                            ch_r "I'm not into that!"                                                  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -10, 1)                        
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_15
                            $ R_RecentActions.append("angry")
                            $ R_DailyActions.append("angry")                       
                        else:
                            call RogueFace("sad") from _call_RogueFace_1362
                            "Rogue doesn't seem to be into this, but she's knows her place."                        
                            jump R_Missionary_HotdogPrep
            return     
            #end auto
    
   
    if not R_Hotdog and "no hotdog" not in R_RecentActions:                                                               
            #first time    
            call RogueFace("surprised", 1) from _call_RogueFace_1363
            $ R_Mouth = "kiss"
            ch_r "So, just grinding against me?"
      
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1364
                ch_r ". . . That's it?"
        
        
    if not R_Hotdog and Approval:                                                
            #First time dialog        
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1365
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
            elif R_Love >= (R_Obed + R_Inbt):
                call RogueFace("sexy") from _call_RogueFace_1366
                $ R_Brows = "sad"
                $ R_Mouth = "smile" 
                ch_r "It does look a bit swolen. . ."           
            elif R_Obed >= R_Inbt:
                call RogueFace("normal") from _call_RogueFace_1367
                ch_r "If you want. . ."
            elif R_Addict >= 50:
                call RogueFace("manic", 1) from _call_RogueFace_1368
                ch_r "Hmmm. . ."
            else: # Uninhibited 
                call RogueFace("sad") from _call_RogueFace_1369
                $ R_Mouth = "smile"             
                ch_r "Hmm, you look ready to go. . ."    
            
    elif Approval:                                                                      
            #Second time+ dialog
            if R_Forced: 
                call RogueFace("sad") from _call_RogueFace_1370
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 20, -2, 1)
                ch_r "That's {i}all{/i} you want?"  
            elif not Taboo and "tabno" in R_DailyActions:        
                ch_r "I guess this is a better location . ."   
            elif "hotdog" in R_RecentActions:
                call RogueFace("sexy", 1) from _call_RogueFace_1371
                ch_r "Again? Ok."
                jump R_Missionary_HotdogPrep
            elif "hotdog" in R_DailyActions:
                call RogueFace("sexy", 1) from _call_RogueFace_1372
                $ Line = renpy.random.choice(["Back again so soon?",                 
                    "So you'd like another round?",                 
                    "You're really digging this. . .", 
                    "Are you sure that's all you want?"]) 
                ch_r "[Line]"    
            else:       
                call RogueFace("sexy", 1) from _call_RogueFace_1373
                $ Rogue_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",                 
                    "So you'd like another round?",                       
                    "You're really digging this. . .", 
                    "You want another rub?"]) 
                ch_r "[Line]"
            $ Line = 0
            
    if Approval >= 2:                                                                  
            #She's into it. . .               
            if R_Forced:
                call RogueFace("sad") from _call_RogueFace_1374
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                ch_r "Ok, fine."    
            elif "no hotdog" in R_DailyActions:               
                ch_r "Well, I guess it's not so bad. . ."
            else:
                call RogueFace("sexy", 1) from _call_RogueFace_1375
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
                $ Line = renpy.random.choice(["Well, sure, give it a rub.",                 
                    "Well. . . ok.",                 
                    "Sure!", 
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."]) 
                ch_r "[Line]"
                $ Line = 0
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2) 
            jump R_Missionary_HotdogPrep   
    
    else:                                                                               
            #She's not into it, but maybe. . .            
            call RogueFace("angry") from _call_RogueFace_1376
            if "no hotdog" in R_RecentActions:  
                ch_r "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in R_DailyActions and "no hotdog" in R_DailyActions: 
                ch_r "I{i}just{/i} told, not in public!" 
            elif "no hotdog" in R_DailyActions:       
                ch_r "I{i}just{/i} told you \"no\" earlier!"
            elif Taboo and "tabno" in R_DailyActions:  
                ch_r "I{i}just{/i} told you, not in public!"  
            elif not R_Hotdog:
                call RogueFace("bemused") from _call_RogueFace_1377
                ch_r "That's kinda hot, [R_Petname]. . ."
            else:
                call RogueFace("bemused") from _call_RogueFace_1378
                ch_r "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in R_DailyActions:
                    call RogueFace("bemused") from _call_RogueFace_1379
                    ch_r "No problem."              
                    return
                "Maybe later?" if "no hotdog" not in R_DailyActions:
                    call RogueFace("sexy") from _call_RogueFace_1380  
                    ch_r "Yeah, maybe, [R_Petname]."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)   
                    if Taboo:                    
                        $ R_RecentActions.append("tabno")                      
                        $ R_DailyActions.append("tabno") 
                    $ R_RecentActions.append("no hotdog")                      
                    $ R_DailyActions.append("no hotdog")                          
                    return
                "You might like it. . .":             
                    if Approval:
                        call RogueFace("sexy") from _call_RogueFace_1381     
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 2)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2) 
                        $ Line = renpy.random.choice(["Well, sure, ok.",     
                            "I suppose. . .", 
                            "That's. . . that's a good point. . ."]) 
                        ch_r "[Line]"
                        $ Line = 0                   
                        jump R_Missionary_HotdogPrep
                    else:   
                        pass
                        
                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Rogue", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and R_Forced):
                        call RogueFace("sad") from _call_RogueFace_1382
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -2, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -2)                 
                        ch_r "Ok, fine. Whatever."  
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 4)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                        $ R_Forced = 1  
                        jump R_Missionary_HotdogPrep
                    else:                              
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)     
                        $ R_RecentActions.append("angry")
                        $ R_DailyActions.append("angry")   
    
    #She refused all offers.
    $ Rogue_Arms = 1      
    
    if "no hotdog" in R_DailyActions:
        ch_r "I'm just not into that."   
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    if R_Forced:
        call RogueFace("angry", 1) from _call_RogueFace_1383
        ch_r "Yeah, not happening."
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -1) if R_Love > 300 else R_Love
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1)  
        $ R_RecentActions.append("angry")
        $ R_DailyActions.append("angry")   
    elif Taboo:                             # she refuses and this is too public a place for her
        call RogueFace("angry", 1) from _call_RogueFace_1384        
        $ R_RecentActions.append("tabno")                      
        $ R_DailyActions.append("tabno") 
        ch_r " not here though?"  
        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)  
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -3)  
    elif R_Hotdog:
        call RogueFace("sad") from _call_RogueFace_1385 
        ch_r "Yeah, not again."
    else:
        call RogueFace("normal", 1) from _call_RogueFace_1386
        ch_r "Noooop."    
    $ R_RecentActions.append("no hotdog")                      
    $ R_DailyActions.append("no hotdog") 
    $ Tempmod = 0    
    return

label R_Missionary_HotdogPrep:  
    call Rogue_Sex_Launch("hotdog") from _call_Rogue_Sex_Launch_13
    
    if Situation != "auto":
#        call Rogue_Bottoms_Off    
        
        if Taboo: # Rogue gets started. . .
            if R_Hotdog:                
                "Rogue glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                
            else:         
                "Rogue glances around for voyeurs. . ."                
                if "cockout" in P_RecentActions:
                    "Rogue slowly presses against your rigid member."
                else:
                    "Rogue hesitantly pulls down your pants and slowly presses against your rigid member."
            $ R_Inbt += int(Taboo/10)  
            $ R_Lust += int(Taboo/5)
        else:                
            if "cockout" in P_RecentActions:
                "Rogue slowly presses against your rigid member."
            else:
                "Rogue hesitantly pulls down your pants slowly presses against your rigid member."
                     
    else: #if Situation == "auto"       
        "You press yourself against her mound."
    
    call Seen_First_Peen(1) from _call_Seen_First_Peen_33
    if not R_Hotdog:                                                      #First time stat buffs      
        if R_Forced:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10) 
        else:
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 20)  
    
            
    if Situation:    
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Rogue","tabno") from _call_DrainWord_218
    call DrainWord("Rogue","no hotdog") from _call_DrainWord_219
    $ R_RecentActions.append("hotdog")                      
    $ R_DailyActions.append("hotdog") 

label R_Missionary_Hotdog_Cycle: #Repeating strokes  
    
    while Round >=0:  
        call Shift_Focus("Rogue") from _call_Shift_Focus_286
        call Rogue_Sex_Launch("hotdog") from _call_Rogue_Sex_Launch_14 
        call RogueLust from _call_RogueLust_17        
        $ P_Cock = "out"
        $ Trigger = "hotdog"
        
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
        
        if R_SEXP >= 100 or ApprovalCheck("Rogue", 1200, "LO"):
            pass
        elif Cnt == (5 + R_Hotdog):
                    $ R_Brows = "confused"
                    ch_r "Are you getting close here?"   
        elif Cnt == (10 + R_Hotdog):
                    $ R_Brows = "angry"        
                    menu:
                        ch_r "This is getting a bit dull."
                        "How about a BJ?" if R_Action and MultiAction:
                                $ Situation = "shift"
                                call R_Missionary_HotdogAfter from _call_R_Missionary_HotdogAfter
                                call R_Blowjob from _call_R_Blowjob_8       
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."             
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump R_Missionary_Hotdog_Cycle
                        "Let's try something else." if MultiAction: 
                                $ Line = 0
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_16
                                $ Situation = "shift"
                                jump R_Missionary_HotdogAfter
                        "No, get back down there.":                                
                                if ApprovalCheck("Rogue", 1200) or ApprovalCheck("Rogue", 500, "O"):                        
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call RogueFace("angry", 1) from _call_RogueFace_1387   
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_17
                                    "She scowls at you and pulls away."
                                    ch_r "Not with that attitude, mister!"                         
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -3, 1)
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -4, 1)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, -1, 1)                    
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -1, 1)  
                                    $ R_RecentActions.append("angry")
                                    $ R_DailyActions.append("angry")   
                                    jump R_Missionary_HotdogAfter
        #End Count check
        
        if Line and P_Focus < 100:                                                    #Player Command menu
                    $ Cnt += 1
                    $ Round -= 1
                    if ("master" in R_Petnames or "sir" in R_Petnames or R_Pet == "slave") and ApprovalCheck("Rogue", 750, "O") and not R_Bondage: # bondage event
                        $ R_Bondage = 1
                        ch_r "Hey, [R_Petname], I've got some new things here, do you think we could try them?"
                        "She grabs what it looks like some bondage gear"
                        menu:
                            "Yep":
                                call RogueFace("sexy", 1) from _call_RogueFace_1388 
                                #if R_Over or R_Chest or R_Panties or R_Legs:
                                #    "She glances up at you as her clothes drop to the ground."
                                #$ R_Over = 0
                                #$ R_Legs = 0
                                #$ R_Chest = 0
                                #$ R_Panties = 0
                                "She starts dressing the new outfit"
                                "You help her with the armbinder, making sure she can't move her arms"
                                #"And add a blindfold so she can't see a thing"
                                #$ R_Blindfold = 1
                                $ R_Over = "armbinder"
                                #$ R_Chest = "bustier bra"
                                #$ R_Panties = "zipper panties"
                                #$ R_Outfit = "zipper bondage"
                                #$ R_Shame = R_OutfitShame[1]
                                #if R_Over == "armbinder":
                                #call RogueFace("sly")
                                $ Line = "Rogue can't move her arms. She licks her lips in anticipation"
                                $ TempLust += 3 if R_Lust < 40 else 1  

                                #if R_Blow <= 1 or (R_Obed >= 500 and R_Obed > R_Inbt):
                                #        $ TempLust += 2 if R_Lust > 60 else 0                 
                                #        $ Line = Line + ", but she seems to be waiting for some instruction"
                                #else:
                                #        $ Line = Line + ", and then she gets started licking your cock"
                                #        $ Speed = 1
                                #jump R_HotdogPrep
                                #pass
                                #call Rogue_Bottoms_Off_Legs
                                #call Rogue_Top_Off
                                #call Rogue_Bottoms_Off
                                #shes gonna wear it
                            "Not now, but let's save it for another time":
                                pass
                                #nope
                    menu:
                        "[Line]"
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

                        "How about you put that armbinder" if R_Bondage and R_Over != "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1389 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "armbinder"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the armbinder" if R_Over == "armbinder":
                            call RogueFace("sexy", 1) from _call_RogueFace_1390 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put that bondage outfit" if R_Bondage and R_Over != "bondage":
                            call RogueFace("sexy", 1) from _call_RogueFace_1391 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            "She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "How about you put those bondage cuffs" if R_Bondage and R_Over != "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1392 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her with the binder, making sure she can't move her arms"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = "bondage cuffs"
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]

                        "Remove the bondage outfit" if R_Over == "bondage" or R_Over == "bondage cuffs":
                            call RogueFace("sexy", 1) from _call_RogueFace_1393 
                            #if R_Over or R_Chest or R_Panties or R_Legs:
                            #    "She glances up at you as her clothes drop to the ground."
                            #$ R_Over = 0
                            #$ R_Legs = 0
                            #$ R_Chest = 0
                            #$ R_Panties = 0
                            #"She starts dressing the new outfit"
                            "You help her remove the binder"
                            #"And add a blindfold so she can't see a thing"
                            #$ R_Blindfold = 1
                            $ R_Over = 0
                            #$ R_Chest = "bustier bra"
                            #$ R_Panties = "zipper panties"
                            #$ R_Outfit = "zipper bondage"
                            #$ R_Shame = R_OutfitShame[1]
                            
                        "Slap her ass":                     
                                    call R_Slap_Ass from _call_R_Slap_Ass_16                                    
                                    jump R_Missionary_Hotdog_Cycle  

                        "Put her legs up" if not R_LegsUp:
                                    $ R_LegsUp = 1
                                    "You put her legs up."

                        "Put her legs down" if R_LegsUp:
                                    $ R_LegsUp = 0
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
                                    call R_Undress from _call_R_Undress_18
                                    
                        "Shift actions":
                            if R_Action and MultiAction:
                                menu:
                                    "How about sex?":
                                        $ Situation = "shift"
                                        call R_Missionary_HotdogAfter from _call_R_Missionary_HotdogAfter_1
                                        call R_Sex_P from _call_R_Sex_P_2
                                    "Just stick it in her pussy [[without asking].":
                                        $ Situation = "auto"
                                        call R_Missionary_HotdogAfter from _call_R_Missionary_HotdogAfter_2
                                        call R_Sex_P from _call_R_Sex_P_3
                                    "How about anal?":
                                        $ Situation = "shift"
                                        call R_Missionary_HotdogAfter from _call_R_Missionary_HotdogAfter_3
                                        call R_Sex_A from _call_R_Sex_A_2
                                    "Just stick it in her ass [[without asking].":
                                        $ Situation = "auto"
                                        call R_Missionary_HotdogAfter from _call_R_Missionary_HotdogAfter_4
                                        call R_Sex_A from _call_R_Sex_A_3
                                    "Never Mind":
                                        pass
                            else:
                                ch_r "I'm kinda tired here? Could we wrap it up?"  
                    
                        "I also want to. . .[[Offhand]":
                                if R_Action and MultiAction:
                                    call Rogue_Offhand_Set from _call_Rogue_Offhand_Set_22
                                    if Trigger2:
                                         $ R_Action -= 1
                                else:
                                    ch_r "I'm kinda tired here? Could we wrap it up?"  
                           
                        "Let's try something else." if MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_18
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump R_Missionary_HotdogAfter
                        "Let's stop for now." if not MultiAction: 
                                    call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_19
                                    $ Line = 0
                                    jump R_Missionary_HotdogAfter
        #End menu (if Line)
        
        call Sex_Dialog("Rogue",Partner) from _call_Sex_Dialog_74
                
        #If either of you could cum 
        if P_Focus >= 100 or R_Lust >= 100:                      
                    #If you can cum:
                    if P_Focus >= 100:                                                     
                            call PR_Cumming from _call_PR_Cumming_14
                            if "angry" in R_RecentActions:  
                                call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_20
                                return    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5) 
                            if 100 > R_Lust >= 70 and R_OCount < 2:             
                                $ R_RecentActions.append("unsatisfied")                      
                                $ R_DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump R_Missionary_HotdogAfter 
                            $ Line = "came"
     
     
                    #If Rogue can cum
                    if renpy.showing("Rogue_SexSprite"):                    #If you're still going at it,
                        if R_Lust >= 100:                                               
                            call R_Cumming from _call_R_Cumming_25
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump R_Missionary_HotdogAfter
                       
                    if Line == "came": #ex P_Focus <= 20: #If you've just cum,  
                        $ Line = 0
                        if not P_Semen:
                            "She's emptied you out, you'll need to take a break."
                            jump R_Missionary_SexAfter
                        elif "unsatisfied" in R_RecentActions:#And Rogue is unsatisfied,                    
                            call Rogue_Sex_Launch("hotdog") from _call_Rogue_Sex_Launch_15
                            $ Line = renpy.random.choice(["She continues to shake a little with pleasure.", 
                                "She is breathing heavily as your cock rubs against her.", 
                                "She slowly turns back towards you and smiles.",
                                "She doesn't seem ready to stop."])
                            "[Line] Keep going?"
                            menu:
                                extend ""
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump R_Missionary_Hotdog_Cycle  
                                "No, I'm done." if P_Semen:
                                    "You pull back."                                    
                                    jump R_Missionary_HotdogAfter
                                "No, I'm spent." if not P_Semen:
                                    "You pull back."
                                    jump R_Missionary_HotdogAfter
                        
        #End orgasm
        
   
        if Round == 10:
            ch_r "You might want to wrap this up, it's getting late."  
        elif Round == 5:
            ch_r "Seriously, it'll be time to stop soon."        
    
    #Round = 0 loop breaks
    call RogueFace("bemused", 0) from _call_RogueFace_1394
    $ Line = 0
    ch_r "Ok, [R_Petname], that's enough of that for now."
    
    

    
label R_Missionary_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback": 
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Rogue_Sex_Reset from _call_Rogue_Sex_Reset_21
        
    call RogueFace("sexy") from _call_RogueFace_1395 
    
    $ R_Hotdog += 1  
    $ R_Action -=1
    $ R_Addictionrate += 1
    if "addictive" in P_Traits:
        $ R_Addictionrate += 1        
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 1) 
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1) 
    
    if R_Loc == bg_current and "noticed Rogue" in R_RecentActions: #If Rogue was participating
        $ R_LikeRogue += 1
    
    if R_Hotdog == 10:
        $ R_SEXP += 5             
    elif R_Hotdog == 1:            
            $R_SEXP += 10        
            if not Situation: 
                if R_Love >= 500 and "unsatisfied" not in R_RecentActions:
                    ch_r "I. . . liked that a lot."
                elif R_Obed <= 500 and P_Focus <= 20:
                    $ R_Mouth = "sad"
                    ch_r "Well, did that work for you?"
    elif R_Hotdog == 5:
            ch_r "I'm surprised how much I enjoy this."  
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":       
        if "unsatisfied" in R_RecentActions:
            call RogueFace("angry") from _call_RogueFace_1396
            $ R_Eyes = "side"
            ch_r "I didn't get much out of that. . ."
        else:
            call RogueFace("bemused") from _call_RogueFace_1397
            ch_r "I could get into that. . ."  
     
    $ Tempmod = 0  
    if Situation == "shift":
        ch_r "Mmm, so what else did you have in mind?"
    call Checkout from _call_Checkout_103
    return   

# End Rogue hotdogging //////////////////////////////////////////////////////////////////////////////////
