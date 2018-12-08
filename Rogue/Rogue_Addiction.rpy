# Event Rogue_Addicted /////////////////////////////////////////////////////
label Rogue_Addicted:
    call Shift_Focus("Rogue") from _call_Shift_Focus
    $ R_Event[1] = 1
    $ MultiAction = 0
    if bg_current != "bg player":
        if R_Loc == bg_current or "Rogue" in Party:
            "Out of the blue, Rogue says she wants to talk to you in your room and drags you over there."
        else:
            "Rogue shows up, hurridly says she wants to talk to you in your room and drags you over there."
    else:
        "Rogue barges into your room in a tizzy."
    $ Taboo = 0
    $ bg_current = "bg player"
    $ R_Loc = bg_current    
    call RogueOutfit from _call_RogueOutfit_3
    call Set_The_Scene from _call_Set_The_Scene_6    
    call CleartheRoom("Rogue") from _call_CleartheRoom
    call RogueFace("bemused") from _call_RogueFace_2
    ch_r "Oh, hey there [R_Petname]. You seem to be fitting in well. . ."
    if not R_Kissed:
        ch_r "Look, since the other day when I first. . . touched you,"
    else:
        ch_r "Look, since the other day when I first. . . kissed you,"
    ch_r "I've had this kind of. . . buzz. At first I thought it was just from finally being able to touch someone,"
    $ R_Eyes = "sexy"
    menu:
        ch_r "But I think maybe. . . could I touch you again?"
        "Another kiss?" if R_Kissed:
            if (R_Love + R_Inbt) > 560:
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 6)
                call RogueFace("sexy") from _call_RogueFace_3
                ch_r "Yeah, sure, pucker up, [R_Petname]."
                "She leans in for another kiss."
                call R_KissPrep from _call_R_KissPrep
        "How about a kiss?" if not R_Kissed:
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 6)
            call RogueFace("sexy") from _call_RogueFace_4
            ch_r "Yeah, sure, let's do that."            
            "She leans in for a kiss."
            call R_KissPrep from _call_R_KissPrep_1   
        "Sure, if it would make you feel better.":
            if (R_Love + R_Inbt) >= 600:
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 4)
                call RogueFace("sexy") from _call_RogueFace_5
                ch_r "I've got an idea for that."
                "She leans in for a kiss."
                call R_KissPrep from _call_R_KissPrep_2
            else:
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 4)
                call RogueFace("smile") from _call_RogueFace_6
                call R_Tag from _call_R_Tag
        "What, you just want to touch my face? No thanks.":
            if R_Love >= 400 or R_Kissed:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -3)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                $ R_Brows = "confused"
                $ R_Eyes = "surprised"
                $ R_Mouth = "sad"
                menu:   
                    ch_r "Well, how 'bout if I gave you a kiss?"
                    "Sure, that'll do.":                        
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
                        call RogueFace("sexy") from _call_RogueFace_7
                        "She leans in for a kiss."
                        call R_KissPrep from _call_R_KissPrep_3       
                    "Only if we can make out a bit.":
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 5)
                        call RogueFace("sexy") from _call_RogueFace_8
                        ch_r "Fine, we can do that."
                        call R_KissPrep from _call_R_KissPrep_4                    
                    "Not good enough.":                        
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)                                             
                        $ R_Brows = "angry"
                        $ Count2 = 3   
                        jump Rogue_Addicted_Ultimatum
            else:                       
                $ R_Brows = "angry"  
                $ Count2 = 2                   
                jump Rogue_Addicted_Ultimatum
                
    jump Rogue_Addicted_End
    
    
label Rogue_Addicted_Ultimatum:
    $ R_RecentActions.append("ultimatum")                      
    $ R_DailyActions.append("ultimatum") 
    while Count2: 
        if not ApprovalCheck("Rogue", 1200, "LI"):
                $ R_Forced = 1        
        menu:
            ch_r "Fine then, what would work for you?"       
            "How about I give you a full contact back massage?":
                    $ CountStore = Tempmod
                    call Rogue_Top_Off from _call_Rogue_Top_Off 
                    $ Tempmod = CountStore
                    if not R_Over and "no topless" not in R_RecentActions:                
                        ch_r "Ok, let's do this then. . ."                  
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                        call R_Massage_Cycle from _call_R_Massage_Cycle
                        jump Rogue_Addicted_End
                    elif "no topless" in R_RecentActions:
                        menu:
                            ch_r "Look, we can still do this, so long as I can touch you after."
                            "Sure, ok.":
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                call R_Massage_Cycle from _call_R_Massage_Cycle_1
                                "Rogue gets back up."
                                call R_Tag from _call_R_Tag_1        
                                jump Rogue_Addicted_End
                            "Nope, not worth it.":
                                ch_r "Fine then! What else?"                                    
                    else:
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                        ch_r "Ok, but after we do this, I get a little touch too."
                        call R_Massage_Cycle from _call_R_Massage_Cycle_2
                        "Rogue gets back up."
                        call R_Tag from _call_R_Tag_2                
                        jump Rogue_Addicted_End
            
            "How about you let me touch you instead?":
                    menu:               
                        ch_r "That depends, [R_Petname]. Where were you thinking?"                         
                        "How about you let me touch your breasts?":
                            $ Tempmod = 10
                            call Rogue_Top_Off from _call_Rogue_Top_Off_1    
                            $ Count = 3  
                            $ Tempmod = 10
                            call R_Fondle_Breasts from _call_R_Fondle_Breasts
                            if "fondle breasts" in R_RecentActions:
                                ch_r "I hope that was enough."
                                jump Rogue_Addicted_End            
                            
                        "How about you let me touch your thighs?":            
                            $ Tempmod = 10            
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off
                            $ Tempmod = 10 
                            if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                ch_r "Ok, but after we do this, I get a little skin contact too."
                            $ Count = 3            
                            call R_Fondle_Thighs from _call_R_Fondle_Thighs                
                            if "fondle thighs" in R_RecentActions:
                                ch_r "I hope that was enough for you."
                                if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                    call R_Tag from _call_R_Tag_3
                                jump Rogue_Addicted_End
                        
                        "How about you let me touch your pussy?":            
                            $ Tempmod = 10             
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_1            
                            $ Count = 3   
                            $ Tempmod = 10 
                            call R_Fondle_Pussy from _call_R_Fondle_Pussy            
                            if "angry" in R_RecentActions:
                                "This is just not worth it. I'm out of here."            
                                jump Rogue_Addicted_Bad_End 
                            if "fondle pussy" in R_RecentActions:
                                ch_r "I hope that was enough for you."            
                                jump Rogue_Addicted_End
                            
            "How about you give me a handjob?":
                $ Tempmod = 10
                call R_Handjob from _call_R_Handjob
                if "no hand" in R_RecentActions:
                    "This is just not worth it. I'm out of here."            
                    jump Rogue_Addicted_Bad_End 
                if "hand" in R_RecentActions:
                    jump Rogue_Addicted_End
            
            "How about you blow me?":
                $ Tempmod = 10
                call R_Blowjob from _call_R_Blowjob
                if "no blow" in R_RecentActions:
                    "This is just not worth it. I'm out of here."            
                    jump Rogue_Addicted_Bad_End 
                if "blow" in R_RecentActions:
                    jump Rogue_Addicted_End
                            
            "How about you strip for me, and then I let you touch me?":
                $ Tempmod = 10
                $ CountStore = ClothingCheck("Rogue")
                call R_Strip from _call_R_Strip    
                menu:
                    "Ok, that was enough, you can touch me now.":                        
                        call R_Tag from _call_R_Tag_4
                        jump Rogue_Addicted_End
                    "That was pretty weak, I'll need a bit more.":
                        call RogueFace("angry") from _call_RogueFace_9
                        if CountStore > ClothingCheck("Rogue") and ClothingCheck("Rogue") < 3:                                              #fix when clothing option recent tags finished
                            ch_r "You're renigging after I went this far?!"
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20) 
                            jump Rogue_Addicted_Bad_End
                        else:
                            ch_r "Seriously? What will this take?" 
                
            "Well then get going.":
                call RogueFace("angry") from _call_RogueFace_10
                ch_r "Well then!"
                "Rogue gives one last look over her shoulder before slamming the door and storming out."            
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 10)
                jump Rogue_Addicted_Bad_End
        
        if not R_Action:
            ch_r "Arg! I'm just too worn out for this!"    
            $ Count2 = 0  
        elif Count2 > 2:
            ch_r "Try something else, I'm not into that."
        elif Count2 > 1:
            ch_r "This isn't a big deal, just one touch."  
        $ Count2 -= 1 if Count2 > 0 else 0   
            
    #End while loop        
    call RogueFace("sad") from _call_RogueFace_11
    ch_r "Sorry [R_Petname], you've run out of chances. I'm out of here."
    jump Rogue_Addicted_Bad_End
    
label Rogue_Addicted_End:                     
    $ R_DailyActions.append("fixed") 
    call RogueFace("surprised") from _call_RogueFace_12
    call RogueOutfit from _call_RogueOutfit_4
    
    ch_r "Wow. I feel a lot better now, a lot more centered." 
    if "swallowed" in R_RecentActions:
        call RogueFace("bemused", 1) from _call_RogueFace_13
        ch_r "Hmm, there might be something to your. . . fluids too. They felt so warm. . ."
    call RogueFace("normal", 0) from _call_RogueFace_14
    if "Rogue" not in Digits:
        ch_r "I'm going to need to get in touch, you should probably have my number, here you go."             
        $ Digits.append("Rogue")
    ch_r "I might have to pay you another visit, [R_Petname]. See ya later."
    $ R_Addict -= 20
    $ R_Resistance = 1
    $ R_Event[1] = 2
    
label Rogue_Addicted_Bad_End:   
    $ R_RecentActions.append("addiction")                      
    $ R_DailyActions.append("addiction")   
    call DrainWord("Rogue","ultimatum",0) from _call_DrainWord_2 #removes recent
    $ Tempmod = 0
    $ Line = 0   
    $ MultiAction = 1 
    $ Situation = 0
    $ R_Addictionrate += 2
    $ R_Forced = 0    
    call Checkout from _call_Checkout_2
    $ Rogue_Arms = 1
    call Remove_Girl("Rogue") from _call_Remove_Girl_8   
    $ renpy.pop_call()
    jump Player_Room

# End Event Rogue_Addicted /////////////////////////////////////////////////////

# Event Rogue_Addicted2 /////////////////////////////////////////////////////  
label Rogue_Addicted2:   
    call Shift_Focus("Rogue") from _call_Shift_Focus_1 
    $ R_Event[2] = 1  
    $ MultiAction = 0 
    if bg_current != "bg player":
        if R_Loc == bg_current or "Rogue" in Party:
            "Rogue suddenly stares at you intently, and says she wants to talk to you in your room and drags you over there."
        else:
            "Rogue bursts in, hurridly says she wants to talk to you in your room and drags you over there."
    else:
        "Rogue barges into your room with a manic look on her face."
    $ Taboo = 0
    $ bg_current = "bg player"
    $ R_Loc = bg_current
    call RogueOutfit from _call_RogueOutfit_5
    call Set_The_Scene from _call_Set_The_Scene_7    
    call CleartheRoom("Rogue") from _call_CleartheRoom_1
    call RogueFace("manic") from _call_RogueFace_15
    ch_r "Ok, so remember the other day, when I wanted to touch you, but you refused?"
    menu:
        extend ""
        "Yeah. . .":
            pass
        "Not really. . .":
            $ R_Brows = "angry"
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
    ch_r "Well I can't take it anymore, I feel this. . . craving to touch you again and it's driving me nuts."
    menu:
        extend ""
        "That's terrible. Have you seen a doctor?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
            ch_r "That's sweet of you, yes. Doc McCoy said that he couldn't determine a cause. . ."
            ch_r "but I think it has something to do with your touch."
        "Serves you right.":
            $ R_Brows = "angry"
            $ R_Mouth = "sad"
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -7)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
            ch_r "Ass!"
        "Are you a pirate?": 
            $ R_Brows = "confused"
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 3)
            ch_r "Arrr. Love a guy with a sense of humor."
            
    call RogueFace("bemused") from _call_RogueFace_16  
    ch_r "I've just been feeling a bit weird since we last touched, shaky, buzzed. I can't concentrate on anything."    
    ch_r ". . .Anyway, I've reconsidered your. . . offer. I'm willing to be a bit . . . flexible here."
    $ Count2 = 2
    
label Rogue_Addicted2_Ultimatum:
    $ R_RecentActions.append("ultimatum")                      
    $ R_DailyActions.append("ultimatum") 
    $ Tempmod = 20
    while Count2:
        $ CountStore = Tempmod        
        if not ApprovalCheck("Rogue", 1200, "LI"):
                $ R_Forced = 1     
        menu:
            ch_r "What do I need to do for another touch?"
            "Nothing, just touch whatever you like.":
                $ R_Forced = 0   
                if (R_Love + R_Inbt) >= 600:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
                    call RogueFace("sexy") from _call_RogueFace_17
                    ch_r "I've got an idea for that."
                    "She leans in for a kiss."
                    call R_KissPrep from _call_R_KissPrep_5
                else:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 6)
                    call RogueFace("smile") from _call_RogueFace_18
                    call R_Tag from _call_R_Tag_5
                jump Rogue_Addicted2_End
                
            "How about a kiss?":
                $ R_Forced = 0   
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 6)
                call RogueFace("sexy") from _call_RogueFace_19
                ch_r "That's it? Yeah, sure, let's do that."            
                "She leans in for a kiss."
                call R_KissPrep from _call_R_KissPrep_6   
                jump Rogue_Addicted2_End
            
            "How about you let me touch you instead?":
                    menu:               
                        ch_r "That depends, [R_Petname]. Where were you thinking?"       
                        "How about I give you a full contact back massage?":
                            $ CountStore = Tempmod
                            call Rogue_Top_Off from _call_Rogue_Top_Off_2 
                            $ Tempmod = CountStore
                            if not R_Over and "no topless" not in R_RecentActions:                
                                ch_r "Ok, let's do this then. . ."                  
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                                call R_Massage_Cycle from _call_R_Massage_Cycle_3
                                jump Rogue_Addicted2_End
                            elif "no topless" in R_RecentActions:
                                menu:
                                    ch_r "Look, we can still do this, so long as I can touch you after."
                                    "Sure, ok.":
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                        call R_Massage_Cycle from _call_R_Massage_Cycle_4
                                        "Rogue gets back up."
                                        call R_Tag from _call_R_Tag_6        
                                        jump Rogue_Addicted2_End
                                    "Nope, not worth it.":
                                        ch_r "Fine then! What else?"
                                            
                            else:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                ch_r "Ok, but after we do this, I get a little touch too."
                                call R_Massage_Cycle from _call_R_Massage_Cycle_5
                                "Rogue gets back up."
                                call R_Tag from _call_R_Tag_7                
                                jump Rogue_Addicted2_End
                                          
                        "How about you let me touch your breasts?":
                            $ CountStore = Tempmod
                            call Rogue_Top_Off from _call_Rogue_Top_Off_3   
                            $ Tempmod = CountStore
                            call R_Fondle_Breasts from _call_R_Fondle_Breasts_1
                            if "fondle breasts" in R_RecentActions:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10)
                                ch_r "I hope that was enough."
                                jump Rogue_Addicted2_End            
                            
                        "How about you let me touch your thighs?":            
                            $ CountStore = Tempmod          
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_2                
                            $ Tempmod = CountStore
                            if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                ch_r "Ok, but after we do this, I get a little touch too."
                            call R_Fondle_Thighs from _call_R_Fondle_Thighs_1
                            if "fondle thighs" in R_RecentActions:
                                ch_r "I hope that was enough for you."
                                if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                    call R_Tag from _call_R_Tag_8
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                jump Rogue_Addicted2_End
                        
                        "How about you let me touch your pussy?":             
                            $ CountStore = Tempmod          
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_3  
                            $ Tempmod = CountStore  
                            call R_Fondle_Pussy from _call_R_Fondle_Pussy_1            
                            if "angry" in R_RecentActions:
                                "This is just not worth it. I'm out of here."            
                                jump Rogue_Addicted2_Bad_End  
                            if "fondle pussy" in R_RecentActions:
                                ch_r "I hope that was enough for you." 
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                                jump Rogue_Addicted2_End
                            
            "How about you give me a handjob?": 
                call R_Handjob from _call_R_Handjob_1
                if "angry" in R_RecentActions:
                    "This is just not worth it. I'm out of here."            
                    jump Rogue_Addicted2_Bad_End 
                if "hand" in R_RecentActions:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                    jump Rogue_Addicted2_End
            
            "How about you blow me?":
                call R_Blowjob from _call_R_Blowjob_1
                if "angry" in R_RecentActions:
                    "This is just not worth it. I'm out of here."            
                    jump Rogue_Addicted2_Bad_End 
                if "blow" in R_RecentActions:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                    jump Rogue_Addicted2_End
                            
            "How about you strip for me, and then I let you touch me?":
                $ CountStore = ClothingCheck("Rogue") 
                call R_Strip from _call_R_Strip_1
                menu:
                    "Ok, that was enough, you can touch me now.":                        
                        call R_Tag from _call_R_Tag_9
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                        jump Rogue_Addicted2_End
                    "That was pretty weak, I'll need a bit more.":
                        call RogueFace("angry") from _call_RogueFace_20
                        if CountStore > ClothingCheck("Rogue") and ClothingCheck("Rogue") < 3:
                            ch_r "You're renigging after I went this far?!"
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20) 
                            jump Rogue_Addicted2_Bad_End
                        else:
                            ch_r "Seriously? What will this take?" 
                
            "Well then get going.":
                call RogueFace("angry") from _call_RogueFace_21
                ch_r "Well then!"
                "Rogue gives one last look over her shoulder before slamming the door and storming out."            
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 5)
                jump Rogue_Addicted2_Bad_End
        
        $ Tempmod = CountStore
        if Count2 and not R_Action:
            ch_r "[[pant, pant] Get to the point already, [Playername]. . ." 
            ch_r "[[pant, pant] I can't keep this up all day."    
            $ R_Action = 1  
        if Count2 > 2:
            ch_r "Try something else, I'm not into that."
        elif Count2 > 1:
            ch_r "Come on, isn't there anything I can do here?"  
            $ Tempmod += 10
                  
        $ Count2 -= 1 if Count2 > 0 else 0 
    #End While loop
    call RogueFace("sad") from _call_RogueFace_22
    ch_r "Sorry [R_Petname], you've run out of chances. I'm out of here."
    jump Rogue_Addicted2_Bad_End  
    
label Rogue_Addicted2_End:              
    $ R_DailyActions.append("fixed") 
    $ R_Event[1] = 2
    call RogueFace("surprised") from _call_RogueFace_23 
    ch_r "Wow. I feel a lot better now, a lot more centered. I think I really am addicted to you here."   
    if "swallowed" in R_RecentActions:
        call RogueFace("bemused", 1) from _call_RogueFace_24
        ch_r "Hmm, there might be something to your. . . fluids too. They felt so warm. . ."
    call RogueFace("normal", 0) from _call_RogueFace_25
    $ R_Mouth = "sad"     
    call RogueOutfit from _call_RogueOutfit_6
    if "Rogue" not in Digits:
        ch_r "I'm going to need to get in touch, you should probably have my number, here you go."             
        $ Digits.append("Rogue")
    ch_r "I may need to do this again sometime. . . I'll see ya later."
    if R_Addict > 30:
        $ R_Addict = 30  
    $ R_Resistance = 1
    
label Rogue_Addicted2_Bad_End:  
    $ R_RecentActions.append("addiction")                      
    $ R_DailyActions.append("addiction")   
    call DrainWord("Rogue","ultimatum",0) from _call_DrainWord_3 #removes recent 
    $ Tempmod = 0
    $ Line = 0
    $ Situation = 0  
    $ R_Forced = 0   
    $ MultiAction = 1 
    $ R_Addictionrate += 2
    call RogueOutfit from _call_RogueOutfit_7
    call Checkout from _call_Checkout_3
    $ Rogue_Arms = 1
    call Remove_Girl("Rogue") from _call_Remove_Girl_9      
    $ renpy.pop_call()
    jump Player_Room
    
# end Event Rogue_Addicted2 /////////////////////////////////////////////////////


# Event Rogue_Addicted3 /////////////////////////////////////////////////////  
label Rogue_Addicted3: 
    call Shift_Focus("Rogue") from _call_Shift_Focus_2
    $ MultiAction = 0
    if bg_current != "bg player":
        if R_Loc == bg_current or "Rogue" in Party:
            "Rogue's been mumbling to herself, she doesn't look that good. She suddenly stares at you intently, grabs you by the collar and drags you to your room."
        else:
            "Rogue bursts in, grabs you by the collar and drags you to your room."
    else:
        "Rogue barges into your room with a manic look on her face."
    $ Taboo = 0
    $ bg_current = "bg player"
    $ R_Loc = bg_current
    call RogueOutfit from _call_RogueOutfit_8
    call Set_The_Scene from _call_Set_The_Scene_8
    call CleartheRoom("Rogue") from _call_CleartheRoom_2
    call RogueFace("manic") from _call_RogueFace_26
    ch_r "Ok, I've given you plenty of chances here. . . Plenty."    
    ch_r "This is driving me crazy, it's like I have a full body itch that I can't scratch."
    menu:
        extend ""
        "And Dr. McCoy hasn't been able to find a cause?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
            ch_r "Nothing! He's run all sorts of tests, and nothing's come up!"
            ch_r "It has to be you, something about your touch, your mutant power."
        "Well, I did make some tempting offers. . .":
            $ R_Brows = "angry"
            $ R_Mouth = "sad"
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -7)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
            ch_r "Yeah, very tempting."        
            
    $ R_Brows = "angry"
    $ R_Mouth = "sad"
    $ R_Blush = 1      
    ch_r "So. . .I need this to end. I need to figure this out. I'll do anything here."
    
    $ Count2 = 4
    $ Tempmod = 0
label Rogue_Addicted3_Ultimatum:    
    if not ApprovalCheck("Rogue", 1200, "LI"):
            $ R_Forced = 1    
    $ R_RecentActions.append("ultimatum")                      
    $ R_DailyActions.append("ultimatum") 
    $ Tempmod = 40
    while Count2:    
        if not ApprovalCheck("Rogue", 1200, "LI"):
                $ R_Forced = 1      
        $ CountStore = Tempmod
        menu:
            ch_r "Just ONE touch."
            "Nothing, just touch whatever you like.":                
                $ R_Forced = 0  
                if (R_Love + R_Inbt) >= 400:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 10)
                    call RogueFace("sexy") from _call_RogueFace_27
                    ch_r "You don't mind! You're a lifesaver! I've got an idea for that."
                    "She leans in for a kiss."
                    call R_KissPrep from _call_R_KissPrep_7
                else:
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 8)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                    call RogueFace("smile") from _call_RogueFace_28
                    ch_r "You don't mind! You're a lifesaver!"
                    call R_Tag from _call_R_Tag_10
                jump Rogue_Addicted3_End
                
            "How about a kiss?":
                $ R_Forced = 0
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 8)
                call RogueFace("sexy") from _call_RogueFace_29
                ch_r "Really? That's it? Yeah, sure, let's do that."            
                "She leans in for a kiss."
                call R_KissPrep from _call_R_KissPrep_8   
                jump Rogue_Addicted3_End
                               
            "How about you let me touch you instead?":
                    menu:               
                        ch_r "That depends, [R_Petname]. Where were you thinking?"
                        "How about I give you a full contact back massage?":
                            $ CountStore = Tempmod
                            call Rogue_Top_Off from _call_Rogue_Top_Off_4 
                            $ Tempmod = CountStore
                            if not R_Over and "no topless" not in R_RecentActions:                
                                ch_r "Ok, let's do this then. . ."                  
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                                call R_Massage_Cycle from _call_R_Massage_Cycle_6
                                jump Rogue_Addicted3_End
                            elif "no topless" in R_RecentActions:
                                menu:
                                    ch_r "Look, we can still do this, so long as I can touch you after."
                                    "Sure, ok.":
                                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                        call R_Massage_Cycle from _call_R_Massage_Cycle_7
                                        "Rogue gets back up."
                                        call R_Tag from _call_R_Tag_11        
                                        jump Rogue_Addicted3_End
                                    "Nope, not worth it.":
                                        ch_r "Fine then! What else?"                                            
                            else:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                                ch_r "Ok, but after we do this, I get a little touch too."
                                call R_Massage_Cycle from _call_R_Massage_Cycle_8
                                "Rogue gets back up."
                                call R_Tag from _call_R_Tag_12                
                                jump Rogue_Addicted3_End
                                                           
                        "How about you let me touch your breasts?":
                            $ CountStore = Tempmod
                            call Rogue_Top_Off from _call_Rogue_Top_Off_5  
                            $ Tempmod = CountStore
                            call R_Fondle_Breasts from _call_R_Fondle_Breasts_2
                            if "fondle breasts" in R_RecentActions:
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 15)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 15)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                                ch_r "I hope that was enough."
                                jump Rogue_Addicted3_End  
                            
                        "How about you let me touch your thighs?":            
                            $ CountStore = Tempmod            
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_4
                            $ Tempmod = CountStore
                            if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                ch_r "Ok, but after we do this, I get a little touch too."
                            call R_Fondle_Thighs from _call_R_Fondle_Thighs_2
                            if "fondle thighs" in R_RecentActions:
                                ch_r "I hope that was enough for you."
                                if R_Legs == "pants" or HoseNum("Rogue") >= 5:
                                    call R_Tag from _call_R_Tag_13
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                                jump Rogue_Addicted3_End
                        
                        "How about you let me touch your pussy?":            
                            $ CountStore = Tempmod             
                            call Rogue_Bottoms_Off from _call_Rogue_Bottoms_Off_5   
                            $ Tempmod = CountStore
                            call R_Fondle_Pussy from _call_R_Fondle_Pussy_2
                            if "fondle pussy" in R_RecentActions:
                                ch_r "I hope that was enough for you."       
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 15)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 15)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                                jump Rogue_Addicted3_End
                            if "angry" in R_RecentActions:
                                "If I wasn't feeling so buzzed right now. . ." 
                            
            "How about you give me a handjob?":
                $ CountStore = Tempmod
                call R_Handjob from _call_R_Handjob_2
                if "hand" in R_RecentActions:          
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 15)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 15)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                    jump Rogue_Addicted3_End
                if "angry" in R_RecentActions:
                    "If I wasn't so out of my mind right now. . ."  
            
            "How about you blow me?":
                $ CountStore = Tempmod
                call R_Blowjob from _call_R_Blowjob_2
                if "blow" in R_RecentActions:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 15)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 15)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                    jump Rogue_Addicted3_End
                if "angry" in R_RecentActions:
                    "You really don't take \"yes\" for an answer, do you? . ."  
                            
            "How about you strip for me, and then I let you touch me?":
                $ CountStore = ClothingCheck("Rogue") 
                call R_Strip from _call_R_Strip_2
                menu:
                    "Ok, that was enough, you can touch me now.":                        
                        call R_Tag from _call_R_Tag_14
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 15)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 15)
                        jump Rogue_Addicted3_End
                    "That was pretty weak, I'll need a bit more.":
                        call RogueFace("angry") from _call_RogueFace_30
                        if CountStore > ClothingCheck("Rogue") and ClothingCheck("Rogue") < 3:
                            ch_r "You're renigging after I went this far?!"
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20) 
                            $ Count2 = 0
                        else:
                            ch_r "Seriously? What will this take?" 
                
            "Well then get going.":
                if Count2 > 1:
                    call RogueFace("angry") from _call_RogueFace_31
                    ch_r "That just isn't good enough this time, [R_Petname]!"   
                    ch_r "We'll have to figure something out this time."                 
                    $ Line = "pass"
                    $ Count2 = 2
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -50)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 20)
            
        $ Tempmod = CountStore
        if Count2 and not R_Action:
            ch_r "[[pant, pant] Get to the point already, [Playername]. . ." 
            ch_r "[[pant, pant] I can't keep this up all day."    
            $ R_Action = 1  
            
        if Line == "pass":
            $ Line = 0
            $ Tempmod += 20
        elif Count2 > 3:
            ch_r "I'd, I don't want to do that. . ."
            $ Tempmod += 5
        elif Count2 > 2:
            ch_r "But. . . I just can't. . ."
            $ Tempmod += 10
        elif Count2 > 1:
            ch_r "PLEASE, I'm begging you here, be reasonable!"
            $ Tempmod += 20           
        $ Count2 -= 1 if Count2 > 0 else 0 
        
    #End While loop
    call RogueFace("angry") from _call_RogueFace_32
    ch_r "Well then!"
    "Rogue trembles with rage."
    ch_r "No way, no how. I'm going to get this taken care of, NOW!"
    call R_Tag from _call_R_Tag_15        
    $ R_Addictionrate += 2
    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 40)
    jump Rogue_Addicted3_End   
            
label Rogue_Addicted3_End:    
    $ R_DailyActions.append("fixed") 
    call RogueFace("surprised") from _call_RogueFace_33 
    ch_r "Wow. . . . wow. Ok. . . ."
    call RogueFace("normal") from _call_RogueFace_34  
    ch_r "I feel a lot better now, a lot more centered. . ." 
    call RogueFace("sad") from _call_RogueFace_35   
    ch_r "I think I really am addicted to something about you here. I don't think I can fight that anymore."   
    if "swallowed" in R_RecentActions:
        call RogueFace("bemused", 1) from _call_RogueFace_36
        ch_r "Hmm, there might be something to your. . . fluids too. They felt so warm. . ."
    call RogueFace("normal", 0) from _call_RogueFace_37
    $ R_Mouth = "sad"     
    call RogueOutfit from _call_RogueOutfit_9
    if "Rogue" not in Digits:
        ch_r "I'm going to need to get in touch, you should probably have my number, here you go."             
        $ Digits.append("Rogue")
    ch_r "I may need to do this again sometime. . . I'll see ya later."
    if R_Addict > 30:
        $ R_Addict = 30
    $ R_Resistance = 1  
    $ R_RecentActions.append("addiction")                      
    $ R_DailyActions.append("addiction")   
    call DrainWord("Rogue","ultimatum",0) from _call_DrainWord_4 #removes recent 
    $ Tempmod = 0
    $ Situation = 0  
    $ MultiAction = 1 
    $ Line = 0
    $ R_Forced = 0
    call Checkout from _call_Checkout_4
    $ Rogue_Arms = 1
    call Remove_Girl("Rogue") from _call_Remove_Girl_10
    $ renpy.pop_call()
    jump Player_Room
    
# end Event Rogue_Addicted3 /////////////////////////////////////////////////////

# Event Rogue_Fix /////////////////////////////////////////////////////  
label Rogue_Fix:   
    call Shift_Focus("Rogue") from _call_Shift_Focus_3
    $ R_Loc = bg_current
    call RogueOutfit from _call_RogueOutfit_10
    call Set_The_Scene from _call_Set_The_Scene_9
    call CleartheRoom("Rogue") from _call_CleartheRoom_3
    call RogueFace("manic") from _call_RogueFace_38  
    $ MultiAction = 0
    $ Taboo = 0
    if not R_Event[4]:
        ch_r "Hey, so we figured out what's causing this buzz."
        ch_r "Since I saw you last, it's been easier to deal with, it builds slower, goes away faster."
        ch_r "I can almost handle it now, but not quite, you know?"
        menu:
            extend ""
            "And still no alternative but touching me?":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                ch_r "Nothing! McCoy's tried everything he can think of."
            "Well anything I can do to help. . .":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                ch_r "I appreciate that, [R_Petname]."
            "You could always whore yourself out again.":
                $ R_Brows = "angry"
                $ R_Mouth = "sad"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -1, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -3, 1)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                ch_r "Yeah, I'm aware of my options, thanks for pointing that out."        
    else:
        if R_Petname in ("master", "sir"):
            call RogueFace("bemused") from _call_RogueFace_39 
            ch_r "I need another fix, [R_Petname]. What can I do about it?"
        else:
            ch_r "Hey, I think I need another fix, I'm feeling a bit out of it."
    $ R_Blush = 1    
    if R_Petname not in ("master", "sir"):
        ch_r "So. . . what can we do here?"
    
    $ Count2 = 4
    $ Tempmod = 0
label Rogue_Fix_Ultimatum: 
    $ Count2 = 3
    $ R_AddictStore = R_Addict
    $ R_RecentActions.append("ultimatum")                      
    $ R_DailyActions.append("ultimatum")
    while Count2:    
        $ Count2 -= 1
        if not ApprovalCheck("Rogue", 1200, "LI"):
                $ R_Forced = 1    
        menu:
            extend ""
            "Just touch whatever you like.":
    #            call Rogues_Choice                                                                 #add RogueChoice options.
    #            if Line == "satisfied":
    #                jump Rogue_Fix_End
    
                $ R_Forced = 0    
                if R_Petname in ("master", "sir"):           
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 95, 1)
                    call RogueFace("sexy") from _call_RogueFace_40
                    ch_r "Thank you, [R_Petname]."
                    "She leans in for a kiss."
                    call R_KissPrep from _call_R_KissPrep_9
                elif (R_Love + R_Inbt) >= 600:                
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 2)
                    call RogueFace("sexy") from _call_RogueFace_41
                    ch_r "You don't mind! You're a lifesaver! I've got an idea for that."
                    "She leans in for a kiss."
                    call R_KissPrep from _call_R_KissPrep_10
                else:                  
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 3)
                    call RogueFace("smile") from _call_RogueFace_42
                    ch_r "You don't mind! You're a lifesaver!"
                    call R_Tag from _call_R_Tag_16                
                if R_Addict >= 40:
                    "As you pull away, Rogue grabs tighter and pulls you close."
                    $ R_Addict = 35
                
            "How about a kiss?":
                $ R_Forced = 0            
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 3)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                call RogueFace("sexy") from _call_RogueFace_43
                if R_Petname in ("master", "sir"):
                    call RogueFace("bemused") from _call_RogueFace_44
                elif "kissing" in R_RecentActions and (R_AddictStore - R_Addict) >= 10:
                    ch_r "Again? Ok, I guess it's worth a shot."  
                elif "kissing" in R_RecentActions:
                    ch_r "Again? Ok, but put your back into it this time."  
                else:
                    ch_r "Really? That's it? Yeah, sure, let's do that."                     
                "She leans in for a kiss."
                call R_KissPrep from _call_R_KissPrep_11                  
                if R_Addict >= 40:
                    "As you pull away, Rogue grabs tighter and pulls you close."
                    $ R_Addict = 35
                   
            "I have some ideas. . .":
                call Rogue_SexMenu from _call_Rogue_SexMenu                    
            
            "Have you considered a . . . chemical solution?" if P_Semen and not R_Chat[2]:                      #Serum first time
                if "no serum" in R_RecentActions:
                    ch_r "Peddle your snake oil someplace else, [R_Petname]."
                else:
                    $ CountStore = R_Action
                    $ R_Action = 0
                    call Rogue_Serum from _call_Rogue_Serum
                    $ R_Action = CountStore
                        
            "Would you like some \"serum?\"" if P_Semen and R_Chat[2]:                                          #Would you like some serum?
                if "no serum" in R_RecentActions:
                    ch_r "No, we tried that and you blew it."
                else:
                    $ CountStore = R_Action
                    $ R_Action = 0
                    call Rogue_Serum from _call_Rogue_Serum_1
                    $ R_Action = CountStore
            
            "No, you're on your own.":                                                                          #Refused                    
                call RogueFace("angry") from _call_RogueFace_45
                $ R_Forced = 0    
                if "beg" in R_RecentActions: 
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)            
                if R_Petname in ("master", "sir"): 
                    call RogueFace("sad") from _call_RogueFace_46
                    if R_Addict <= 85 or "beg" in R_RecentActions: 
                        ch_r "If you insist, [R_Petname]."
                        "Rogue shrugs dejectedly, and then leaves the room."
                        jump Rogue_Fix_BadEnd        
                    else:
                        $ R_Eyes = "manic"
                        "Rogue shivers slightly."
                        ch_r "Please, [R_Petname], please reconsider?"
                        $ R_RecentActions.append("beg")    
                elif R_Addict <= 85:                
                    ch_r "Fine!"
                    "Rogue trembles with rage and walks out."
                    jump Rogue_Fix_BadEnd                
                else:    
                    ch_r "You. . ."
                    "Rogue trembles with rage."
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -5)
                    ch_r "I just can't take \"no\" for an answer here."            
                    call R_Tag(1) from _call_R_Tag_17
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 5)
                    if R_Addict <= 40:
                        jump Rogue_Fix_End
                    else:
                        "Rogue trembles with rage and walks out."
                        jump Rogue_Fix_BadEnd 
        
        if R_Addict >= 40 and not R_Action:
            ch_r "[[pant, pant] Get to the point already, [Playername]. . ." 
            ch_r "[[pant, pant] I can't keep this up all day."    
            $ R_Action = 1  
            
        if R_Addict < 40:
            jump Rogue_Fix_End
        elif R_AddictStore - R_Addict >= 10:                            #you helped, but not enough.
            call RogueFace("bemused", 1, 0) from _call_RogueFace_47
            ch_r "I think that helped, but I still need more. . ."   
        elif "swallowed" in R_RecentActions or "serum" in R_RecentActions: 
            call RogueFace("confused", 1, 1) from _call_RogueFace_48          
            ch_r "That. . .helped, but it really didn't take enough of the edge off. I'll need something else. . ."          
        elif R_AddictStore - R_Addict <= 0:                             #whatever you did had no benefit
            call RogueFace("angry", 1, 1) from _call_RogueFace_49
            ch_r "Stop screwing around, I need some contact!"         
        elif R_AddictStore - R_Addict < 10:                             #you barely helped
            call RogueFace("confused", 1, 1) from _call_RogueFace_50
            ch_r "I barely felt a tingle from that, I need something stronger. . ."             
        if Count2 == 1:
            if R_Addict <= 75:
                call RogueFace("angry") from _call_RogueFace_51
                ch_r "Fine!"
                "Rogue trembles with rage and walks out."
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 1)
                jump Rogue_Fix_BadEnd
            elif R_Addict >= 95:
                ch_r "I can't stand this!!"                
                if not ApprovalCheck("Rogue", 1600):
                        $ R_Forced = 1    
                $ Tempmod = 50 
            else:
                ch_r "Please!"
                
                if not ApprovalCheck("Rogue", 2000):
                        $ R_Forced = 1
                $ Tempmod = 30 
                
    #While Loop ends
    call RogueFace("angry") from _call_RogueFace_52
    if R_AddictStore - R_Addict >= 10:                            #you helped, but not enough.        
        call RogueFace("sad") from _call_RogueFace_53
        ch_r "I know you tried to help, but this just isn't working."         
    elif 0 < (R_AddictStore - R_Addict) < 10: 
        call RogueFace("angry") from _call_RogueFace_54
        $ R_Mouth = "grimace"
        ch_r "We tried it your way, now I'm trying it mine."    
    else:
        ch_r "Well then!"
        "Rogue trembles with rage."    
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
        ch_r "You're not pulling this shit, I'm gonna get mine!"
    call R_Tag(1) from _call_R_Tag_18      
    $ R_Addictionrate += 2  
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 2)  
        
label Rogue_Fix_End:      
    
    call RogueFace("normal", 0) from _call_RogueFace_55
    $ R_Mouth = "sad"    
    if not R_Event[4]:
        if "forced tag" in R_RecentActions: 
            ch_r "I got what I needed. I really wish that I could avoid it, but it looks like I'm stuck with you."
            ch_r " Just. . . in future maybe try to be less of a dick about it?"
        elif not R_Forced:
            ch_r "Thanks. I really appreciate this. I can't really explain it, but if I don't get. . . "
            ch_r "access every now and then, I just feel awful, crawling out of my skin. Being with you, helps calm me down."            
            if ApprovalCheck("Rogue", 750):
                ch_r "And, you know, we had a lot of fun in the process."
            else: #not good with you
                ch_r "And thanks for, you know, not taking advantage of the situation."        
        else: #forced
            ch_r "Well, I hope you got what you wanted out of this. I really wish that I could avoid it, but it looks like I'm stuck with you."
            ch_r " Just. . . in future maybe try to be less of a dick about it?"
    else:        
        if "forced tag" in R_RecentActions: 
            ch_r "Well, I got what I needed. I guess I'll see you around."            
        elif not R_Forced:
            ch_r "Hmmmm, that was real nice, [R_Petname]."
            ch_r "I'm looking forward more and more to these . . . \"sessions\" of ours."
        else: #forced
            ch_r "Well, looks like we both got what we wanted. I guess I'll see you around."
    $ R_Event[4] += 1
    $ R_DailyActions.append("fixed")
    
label Rogue_Fix_BadEnd:  
    $ R_RecentActions.append("addiction")                      
    $ R_DailyActions.append("addiction")   
    call DrainWord("Rogue","ultimatum",0) from _call_DrainWord_5 #removes recent 
    $ R_Event[3] += 5
    $ MultiAction = 1
    $ Tempmod = 0
    $ Line = 0
    $ R_Forced = 0
    call RogueOutfit from _call_RogueOutfit_11
    call Checkout from _call_Checkout_5
    $ Rogue_Arms = 1
    call Remove_Girl("Rogue") from _call_Remove_Girl_11
    
    $ renpy.pop_call()
    if bg_current == "bg rogue": 
        "You head back to your room."
    elif bg_current == "bg player":
        "Rogue heads out."        
    jump Player_Room
    
    
# end Event Rogue_Fix /////////////////////////////////////////////////////


            
label Rogue_Serum:
    call RogueFace("confused") from _call_RogueFace_56
    if not R_Chat[2]:
        menu: 
            ch_r "What do you mean by that?"
            "I think I could. . . (trick her)":
                ch_p "I was just thinking, I've been studying hard in class and could maybe whip up a. . .serum, that would reduce the cravings."                    
                call RogueFace from _call_RogueFace_57
                ch_r "Hmm. . . well if you think you can figure out something that would stop this, I'm game."    
                                   
            "My jiz.":
                $ R_Blush = 1
                if R_Swallow:
                    call RogueFace("bemused") from _call_RogueFace_58
                    ch_r "Hmm, well it has seemed to work for me in the past. . ."
                else:
                    call RogueFace("surprised") from _call_RogueFace_59
                    ch_r "Your what? . . . You want me to drink your jiz?"
                $ R_Chat[3] = 1
                
                if ApprovalCheck("Rogue", 750):     #if she likes you, she offers sex instead  
                    ch_r "Well if that's the plan, couldn't I just get some from the source?"
                    call RogueFace("sexy") from _call_RogueFace_60
                else:
                    ch_r "Well, I guess if touching you works, this could work too. . ."
                
            "Never mind.":
                return
    
    elif R_Chat[3]:
        call RogueFace("bemused", 1) from _call_RogueFace_61
        ch_r "Hmm, it was good last time. . ."            
        if ApprovalCheck("Rogue", 750):
            ch_r "I'd really rather get it straight off the tap. . ."
            call RogueFace("sexy") from _call_RogueFace_62
        else:
            ch_r "I guess this is as good a \"treatment\" as any."
            call RogueFace("sad") from _call_RogueFace_63
            $ R_Brows = "normal" 
    elif R_Chat[2]:    
        ch_p "I was just thinking, I could whip up more of that serum. . ."
        call RogueFace("bemused") from _call_RogueFace_64
        ch_r "Well, whatever that stuff is, it worked well enough last time. . ."                   
             
             
    #pricing    
    ch_r "Now what do you want for it?"
    $ Count = 3
    while Count:        
        $ Count -= 1
        menu:
            extend ""
            "Give it to her":
                $ R_Forced = 0    
                $ R_Mouth = "smile"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 1)
                "You hand her the serum."
                $ R_RecentActions.append("has serum")
                
            "Well, a handy might do the trick. . .":
                call RogueFace("sexy") from _call_RogueFace_65
                if ApprovalCheck("Rogue", 1100):
                    $ Rogue_Arms = 2
                    if R_Chat[3]: 
                        ch_r "Heh, I guess I could work the pump for a bit."
                    else:
                        ch_r "I guess if that's what you want . . ."
                    call RHJ_Prep from _call_RHJ_Prep
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)
                    $ R_RecentActions.append("has serum")
                else:
                    $ R_Brows = "confused"
                    ch_r "Pssht, you wish."
                    
                if "swallowed" in R_RecentActions: 
                    if R_Chat[3]: 
                        ch_r "Well, I think that hit the spot. . ."
                        return
                    else:
                        ch_r "That was. . . good actually, now what about this serum?"
                elif "hand" in R_RecentActions: #not swallowed
                    ch_r "Ok, I think I worked that one off, now how about that serum?"
                else:
                    ch_r "Anything else I could do here though?"
                                    
            "How about a blowjob?":                    
                call RogueFace("sexy") from _call_RogueFace_66
                if ApprovalCheck("Rogue", 1300):                       
                    if R_Chat[3]: 
                        ch_r "Heh, I guess I could get it straight from the source."
                    else:
                        ch_r "I. . . suppose I could . . ."
                    call RBJ_Prep from _call_RBJ_Prep
                    $ R_RecentActions.append("has serum")
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 1)                    
                else:
                    $ R_Brows = "confused"
                    ch_r "Not likely."
                    
                if "swallowed" in R_RecentActions: 
                    if R_Chat[3]: 
                        ch_r "Good to the last drop. . ."
                        return
                    else:
                        ch_r "That. . . helped actually, but what about this serum?"
                elif "blow" in R_RecentActions: #not swallowed
                    ch_r "Ok, I did my part, now how about that serum?"
                else:
                    ch_r "I must have something else to offer though. . ."                    
            
            "Ask for a favor for it.":
                call RogueFace("sexy") from _call_RogueFace_67
                ch_r "Oh? What sort of favor were you expecting, [R_Petname]?"
                $ MultiAction = 0                          
                $ R_Action = 1
                call Rogue_SexMenu from _call_Rogue_SexMenu_1   
                if "angry" not in R_RecentActions:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 2)
                    ch_r "I'm glad we could work something out, [R_Petname]."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 1)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)  
                    $ R_RecentActions.append("has serum") 
                if "angry" in R_RecentActions:
                    ch_r "Well that ain't gonna fly, [R_Petname]."
                    $ Count = 0
                        
            "I'm charging for a sip, $5.":
                call RogueFace("angry") from _call_RogueFace_68
                $ R_Mouth = "surprised"
                if R_Chat[3]: 
                    ch_r "Five bucks, just to drink your cum?"
                elif R_Chat[2]:
                    ch_r "Five bucks, just for this supposed \"serum\"?"
                else:
                    ch_r "Five bucks, just for that serum?"
                call RogueFace from _call_RogueFace_69
                $ R_Eyes = "side"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -3, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -4)
                ch_r ". . ."  
                call RogueFace from _call_RogueFace_70
                $ R_Brows = "sad"
                if R_Chat[2]:  
                    ch_r "Ok, here you go."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 4)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 4)                    
                    if not ApprovalCheck("Rogue", 1200, "LI"):
                            $ R_Forced = 1    
                    $ P_Cash += 5 
                    $ R_RecentActions.append("has serum")
                else:
                    ch_r "No way, I don't even know if this'll work."
                    
            
            "I'm afraid I'll have to charge, $10.":
                call RogueFace("angry") from _call_RogueFace_71
                $ R_Mouth = "surprised"                  
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, -5, 1)
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)
                if R_Chat[3]: 
                    ch_r "Ten bucks for a bottle of jizz?"
                elif R_Chat[2]:
                    ch_r "Ten bucks, just for this supposed \"serum\"?"
                else:
                    ch_r "Ten bucks, just for that serum?"                
                if R_Chat[2] and R_Addict >= 75:  
                    ch_r "Five was bad enough! Fine, here you go, but not a penny more."  
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
                    if not ApprovalCheck("Rogue", 1200, "LI"):
                            $ R_Forced = 1    
                    $ P_Cash += 10 
                    $ R_RecentActions.append("has serum") 
                elif R_Chat[2]:                    
                    ch_r "I don't take kindly to highway robbery, [R_Petname]."
                else:
                    ch_r "No way, I don't even know if this'll work."
                    
            "Never mind.":
                ch_r "Oh, ok. . ."
                return
                
        if "has serum" in R_RecentActions:  
            $Count = 0
        elif Count == 1:
            ch_r "I don't have all day, get serious."        
        elif Count:
            ch_r "Come on, what else do you want here?"
        
              
              
    if "has serum" in R_RecentActions:  #falls through if she got the serum  
        "She opens the serum bottle and gives it a little sniff."
        
        if R_Chat[3]:
            "She glances hesitantly at you, but gulps it down, and wipes her lips."                                 
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
        elif R_Swallow >= 5:
            "She looks a bit confused, but then grins, gulps it down, and wipes her lips."
            ch_r "That was your jiz, wasn't it. You chould have just told me."   
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 1)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 2)
            ch_r "I know how well that stuff works."                 
            $ R_Chat[3] = 1
        elif R_Swallow:                                
            call RogueFace("surprised") from _call_RogueFace_72
            menu:
                ch_r "Hmmm. . . hey, this is your jiz, isn't it?!"
                "Um, yes?":
                    call RogueFace("confused") from _call_RogueFace_73
                    $ R_Mouth = "lipbite"
                "Of course not!":
                    call RogueFace("confused") from _call_RogueFace_74
                    $ R_Mouth = "smile"
            "She looks sternly at you, but then gulps it down and wipes her lips."
            ch_r "Ugh, I'm still getting used to the taste of that, you should have just told me."
            $ R_Chat[3] = 1
        else:       #She doesn't know what it was
            "She then gulps it down and wipes her lips."
            ch_r "Ugh, that stuff goes down hard. . ."
        $ R_Eyes = "closed"
        $ R_Brows = "sad"
        $ R_Mouth = "smile"
        "Rogue shudders with ecstasy."
        call RogueFace from _call_RogueFace_75
        if R_Chat[3]:
            ch_r "Hmm, even knowing what that stuff is, it does seem to work."  
            $ R_RecentActions.append("swallowed") 
            $ R_DailyActions.append("swallowed") 
        else:
            ch_r ". . . that does certainly take the edge off. Thank you."                  
        $ R_RecentActions.remove("has serum") 
        $ R_RecentActions.append("serum") 
        $ R_DailyActions.append("serum")            
        $ R_Addict -= 20
        $ R_Addictionrate += 2
        if "addictive" in P_Traits:
            $ R_Addictionrate += 2           
        $ R_Chat[2] += 1
    else:
        ch_r "Too bad we couldn't come to an arrangement here. . ." 
        $ R_RecentActions.append("no serum") 
    return
    