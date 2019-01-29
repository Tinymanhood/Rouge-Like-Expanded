# //////////////////////////////////////////////////////////////////////                World Map Interface 

label Worldmap:
    if Current_Time == 'Evening':    
        scene Crossroads_E onlayer backdrop
    elif Current_Time == 'Night':
        scene Crossroads_N onlayer backdrop        
    else: 
        scene Crossroads_D onlayer backdrop
    scene 
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
                    $ renpy.pop_call() 
                    jump Player_Room_Entry  
        "Testbed" if config.developer:          
                    $ renpy.pop_call() 
                    #jump Rogue_Room_Test
        "Girl's Rooms":
            menu:
                "Rogue's Room":   
                            $ renpy.pop_call() 
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            $ renpy.pop_call() 
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            $ renpy.pop_call() 
                            jump Emma_Room_Entry  
                "Mystique's Room" if "metgym" in newgirl["Mystique"].History:
                            $ renpy.pop_call() 
                            jump Mystique_Room_Entry            
                "Back":
                            jump Worldmap
        "University Square":
                    $ renpy.pop_call() 
                    jump Campus_Entry 
        "Class":
            if Current_Time != "Night":
                $ renpy.pop_call() 
                jump Class_Room_Entry 
            elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        $ renpy.pop_call() 
                        jump Class_Room_Entry 
            else:
                        "It's late for classes and the classrooms are locked down."
                        jump Worldmap
        "The Danger Room":         
                    $ renpy.pop_call()    
                    jump Danger_Room_Entry

        "The Pool": 
                    $ renpy.pop_call() 
                    jump Pool_Entry

        "The Football Field": 
                    $ renpy.pop_call() 
                    jump Field_Entry

        "The showers":
                    $ renpy.pop_call() 
                    jump Shower_Room_Entry         
        "Xavier's Study":
                    $ renpy.pop_call() 
                    jump Study_Room_Entry 
        "Stay where I am.":
                    return
    return          
                    
# end World Map Interface //////////////////////////////////////////////////////////////////////

# start Misplaced location checker  //////////////////////////////////////////////////////////////////////
label Misplaced:
        if "caught" in R_RecentActions:        
                call DrainWord("Rogue","caught",1,0) from _call_DrainWord_40
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Rogue") from _call_Remove_Girl_12
                $ Trigger = 0
                jump Player_Room
        if "caught" in K_RecentActions:        
                call DrainWord("Kitty","caught",1,0) from _call_DrainWord_41
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Kitty") from _call_Remove_Girl_13
                $ Trigger = 0
                jump Player_Room
        if "caught" in E_RecentActions:        
                call DrainWord("Emma","caught",1,0) from _call_DrainWord_42
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Emma") from _call_Remove_Girl_14
                $ Trigger = 0
                jump Player_Room
        if "caught" in newgirl["Mystique"].RecentActions:        
                call DrainWord("Mystique","caught",1,0) from _call_DrainWord_43
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Mystique") from _call_Remove_Girl_15
                $ Trigger = 0
                jump Player_Room
        if bg_current == "bg player":
                jump Player_Room 
        if bg_current == "bg rogue":
                jump Rogue_Room 
        if bg_current == "bg kitty":
                jump Kitty_Room
        if bg_current == "bg emma":
                jump Emma_Room 
        if bg_current == "bg mystique":
                jump Mystique_Room  
        if bg_current == "bg dangerroom":
                jump Danger_Room 
        if bg_current == "bg classroom":
                jump Class_Room 
        jump Campus 
            
        return
# end Misplaced location checker  //////////////////////////////////////////////////////////////////////


# Player's Room Interface //////////////////////////////////////////////////////////////////////
label Player_Room_Entry:
    $ bg_current = "bg player"            
    call Gym_Clothes from _call_Gym_Clothes
    call EventCalls from _call_EventCalls
    call Set_The_Scene(Entry = 1) from _call_Set_The_Scene_10    
    
label Player_Room:
    $ bg_current = "bg player"
    call Set_The_Scene from _call_Set_The_Scene_11
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level from _call_Taboo_Level_1
    call QuickEvents from _call_QuickEvents
    call Checkout(1) from _call_Checkout_23
    if Round <= 10:
                call Round10 from _call_Round10
                call Girls_Location from _call_Girls_Location_4
                call EventCalls from _call_EventCalls_1
                
    call GirlsAngry from _call_GirlsAngry      
    call Set_The_Scene from _call_Set_The_Scene_12

# Player Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in your room. What would you like to do?"
        "Chat":
                    call Chat from _call_Chat

        "Would you like to study [[Rogue]?" if R_Loc == bg_current:
                    call Rogue_Study from _call_Rogue_Study
        "Would you like to study [[Kitty]?" if K_Loc == bg_current:
                    call Kitty_Study from _call_Kitty_Study
        "Would you like to help me study [[Emma]?" if E_Loc == bg_current:
                    call Emma_Study from _call_Emma_Study
        "Would you like to help me study [[Mystique]?" if newgirl["Mystique"].Loc == bg_current:
                    call Mystique_Study from _call_Mystique_Study
        "Sleep" if Current_Time == "Night":            
                    call Round10 from _call_Round10_1
                    $ R_Spank = 0
                    $ K_Spank = 0
                    $ E_Spank = 0
                    $ newgirl["Mystique"].Spank = 0
                    call Girls_Location from _call_Girls_Location_5
                    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie 
                    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie 
                    call EventCalls from _call_EventCalls_2 
        "Wait" if Current_Time != "Night":
                    "You wait around a bit."
                    call Wait from _call_Wait                 
                    call Girls_Location from _call_Girls_Location_6
                    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_1
                    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_1
                    call EventCalls from _call_EventCalls_3   

        "Shop":
                    call Shop from _call_Shop                
        "Special Options":
                    call SpecialMenu from _call_SpecialMenu
        
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Mystique's Room" if "metgym" in newgirl["Mystique"].History:  
                            jump Mystique_Room_Entry
                "Back":
                            pass
        "Go to the Showers" if TravelMode:         
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                            jump Campus_Entry
                    else:
                            call Worldmap from _call_Worldmap
    jump Player_Room

label Emma_Study:                       #study events
            call Shift_Focus("Emma") from _call_Shift_Focus_40
            if Current_Time == "Night":
                ch_e "Don't you think it's a bit late?"
                return
            elif Round <= 30:        
                ch_e "I don't know that there's time for that, maybe if we wait a bit. . ."
                return
            else:
                ch_e "Sure."
                        
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["You study for a while, it was fairly boring.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and watch a movie instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test."
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
            $ D20 = renpy.random.randint(1, 20)    
            if D20 > 10:
                call Emma_Frisky_Study from _call_Emma_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait from _call_Wait_1
            call Emma_Leave from _call_Emma_Leave
            call Kitty_Leave from _call_Kitty_Leave
            call Rogue_Leave from _call_Rogue_Leave
            return
#End Emma Study
            
label Emma_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Emma", 1000) and E_Blow > 5:
                        "Emma reaches her hand through your textbook and you can feel it in your lap."
                        "She unzips you pants and pulls your dick out, stroking it slowly."
                        "She then dives her head under the book, and starts to lick it."        
                        call Emma_SexAct("blow") from _call_Emma_SexAct 
            elif D20 > 14 and ApprovalCheck("Emma", 1000) and E_Hand >= 5:
                        "Emma reaches her hand through your textbook and you can feel it in your lap."
                        "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                        "She unzips you pants and pulls your dick out, stroking it slowly."  
                        call Emma_SexAct("hand") from _call_Emma_SexAct_1 
            elif D20 > 10 and (ApprovalCheck("Emma", 1300) or (E_Mast and ApprovalCheck("Emma", 1000)))and E_Lust >= 70:
                        "Emma wriggles against your shoulder, and her hand starts to stroke her crotch."  
                        if "unseen" in E_RecentActions:
                                $ E_RecentActions.remove("unseen")
                        $ Trigger = "masturbation"
                        call Emma_SexAct("masturbate") from _call_Emma_SexAct_2      
            elif D20 >5 and ApprovalCheck("Emma", 700) and E_Kissed > 1:
                        "Emma leans close to you, and presses her lips to yours."         
                        call Emma_SexAct("kissing") from _call_Emma_SexAct_3
            elif ApprovalCheck("Emma", 500):
                        "Emma squeezes close to you, and you spend the rest of the night cuddling."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return

label Mystique_Study:                       #study events
            call Shift_Focus("Mystique") from _call_Shift_Focus_41
            if Current_Time == "Night":
                ch_m "Don't you think it's a bit late?"
                return
            elif Round <= 30:        
                ch_m "I don't know that there's time for that, maybe if we wait a bit. . ."
                return
            else:
                ch_m "Sure."
                        
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["You study for a while, it was fairly boring.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and watch a movie instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test."
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 80, 2)
            $ D20 = renpy.random.randint(1, 20)    
            if D20 > 10:
                call Mystique_Frisky_Study from _call_Mystique_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait from _call_Wait_2
            call Mystique_Leave from _call_Mystique_Leave
            call Kitty_Leave from _call_Kitty_Leave_1
            call Rogue_Leave from _call_Rogue_Leave_1
            return
#End Mystique Study
            
label Mystique_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Mystique", 1000) and newgirl["Mystique"].Blow > 5:
                        "Mystique reaches her hand through your textbook and you can feel it in your lap."
                        "She unzips you pants and pulls your dick out, stroking it slowly."
                        "She then dives her head under the book, and starts to lick it."        
                        call Mystique_SexAct("blow") from _call_Mystique_SexAct 
            elif D20 > 14 and ApprovalCheck("Mystique", 1000) and newgirl["Mystique"].Hand >= 5:
                        "Mystique reaches her hand through your textbook and you can feel it in your lap."
                        "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                        "She unzips you pants and pulls your dick out, stroking it slowly."  
                        call Mystique_SexAct("hand") from _call_Mystique_SexAct_1 
            elif D20 > 10 and (ApprovalCheck("Mystique", 1300) or (newgirl["Mystique"].Mast and ApprovalCheck("Mystique", 1000)))and newgirl["Mystique"].Lust >= 70:
                        "Mystique wriggles against your shoulder, and her hand starts to stroke her crotch."  
                        if "unseen" in newgirl["Mystique"].RecentActions:
                                $ newgirl["Mystique"].RecentActions.remove("unseen")
                        $ Trigger = "masturbation"
                        call Mystique_SexAct("masturbate") from _call_Mystique_SexAct_2      
            elif D20 >5 and ApprovalCheck("Mystique", 700) and newgirl["Mystique"].Kissed > 1:
                        "Mystique leans close to you, and presses her lips to yours."         
                        call Mystique_SexAct("kissing") from _call_Mystique_SexAct_3
            elif ApprovalCheck("Mystique", 500):
                        "Mystique squeezes close to you, and you spend the rest of the night cuddling."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return

# end Player's Room Interface //////////////////////////////////////////////////////////////////////

# Rogue's Room Interface //////////////////////////////////////////////////////////////////////
label Rogue_Room_Entry:
    call Shift_Focus("Rogue") from _call_Shift_Focus_42
    $ bg_current = "bg rogue"           
    call Gym_Clothes from _call_Gym_Clothes_1
    call Set_The_Scene(Entry = 1) from _call_Set_The_Scene_13    
    call Taboo_Level from _call_Taboo_Level_2
    $ D20 = renpy.random.randint(1, 20)
    
    if "Rogue" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI"):     #It's late but she really likes you
                                ch_r "It's pretty late, [R_Petname], but you can come in for a little bit."    
                        elif R_Addict >= 50:
                                ch_r "Um, yeah, you'd better come in. . ."         
                        elif ApprovalCheck("Rogue", 500, "LI") or ApprovalCheck("Rogue", 300, "OI"):      #she likes you well enough but it's late
                                ch_r "It's a little late [R_Petname]. See you tomorrow."
                                $ R_RecentActions.append("noentry")                      
                                $ R_DailyActions.append("noentry")  
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Rogue is in the party and it's not late in the day        
                                ch_r "Come on in, [R_Petname]."
                    call EventCalls from _call_EventCalls_4
                    jump Rogue_Room   
    #End if Rogue in Party
    
                    
    if Round >= 10 and R_Loc == "bg rogue" and (D20 >=15 and R_Lust >= 70): #Rogue caught fapping      
                "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
                menu:
                    extend ""
                    "Knock politely":
                        $ Line = "knock"
                    "Peek inside":
                        call Set_The_Scene from _call_Set_The_Scene_14
                        "You see Rogue, eyes closed and stroking herself vigorously."
                        menu:
                            extend ""
                            "Enter Quietly":
                                    call Rogue_Caught_Masturbating from _call_Rogue_Caught_Masturbating
                            "Pull back and knock":                        
                                    $ Line = "knock"
                            "Leave quietly":
                                    "You leave Rogue to her business and slip out."
                                    $ R_Lust = 20
                                    jump Campus_Map
                    "Enter quietly":
                            call Rogue_Caught_Masturbating from _call_Rogue_Caught_Masturbating_1
                    "Leave quietly":
                            "You leave Rogue to her business and slip out."
                            $ R_Lust = 20
                            jump Campus_Map
                if Line == "knock":
                        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                        "After several seconds and some more shuffling of clothing, Rogue comes to the door."
                        $ R_Brows = "confused"
                        $ R_Eyes = "surprised"
                        $ R_Mouth = "smile"
                        $ R_Blush = 1
                        call Set_The_Scene from _call_Set_The_Scene_15
                        ch_r "Sorry about that [R_Petname], I was. . . working out."
                        $ Tempmod += 10
    # End Rogue caught Fapping
    
    else: #not auto-caught fapping
            if "Rogue" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg rogue"
                            call Set_The_Scene from _call_Set_The_Scene_16
                        
            if Line != "knock" and "Rogue" in Keys: 
                if R_Loc == "bg rogue":
                        if Round <= 10:        #add "no" condtion here
                                if R_RecentActions in ("noentry", "angry"):
                                        call RogueFace("angry") from _call_RogueFace_77
                                        ch_r "Buzz off already."  
                                        "Rogue shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif (D20 >=19 and R_Lust >= 50) or (D20 >=15 and R_Lust >= 70) or (D20 >=10 and R_Lust >= 80):     #Rogue caught fapping
                                call Rogue_Caught_Masturbating from _call_Rogue_Caught_Masturbating_2 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           #Rogue caught changing
                                call Rogue_Caught_Changing from _call_Rogue_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Rogue's door."        
                        if R_Loc != "bg rogue":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and R_Lust >= 50) or (D20 >=15 and R_Lust >= 70) or (D20 >=10 and R_Lust >= 80):    #Rogue caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Rogue comes to the door."
                                $ R_Brows = "confused"
                                $ R_Eyes = "surprised"
                                $ R_Mouth = "smile"
                                $ R_Blush = 1
                                call Set_The_Scene from _call_Set_The_Scene_17
                                ch_r "Sorry about that [R_Petname], I was. . . working out."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          #Rogue caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Rogue comes to the door."
                                call Set_The_Scene from _call_Set_The_Scene_18
                                ch_r "Sorry about that [R_Petname], I was just getting changed."        
                        elif "angry" in R_RecentActions:
                                ch_r "I don't want to deal with you right now."
                                "Rogue pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene from _call_Set_The_Scene_19
                                "Rogue opens it a bit and pops out and you ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if R_Loc != "bg rogue":
                    "Looks like she's not home right now."                
                    if "Rogue" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Rogue_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif R_RecentActions in ("noentry", "angry"):
                    call RogueFace("angry") from _call_RogueFace_78
                    ch_r "Buzz off already."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in R_RecentActions:
                    ch_r "Hey, I told you you're not welcome. I'll see you tomorrow"
                    jump Campus_Map 
                    
            elif "noentry" in R_RecentActions:
                    call RogueFace("angry") from _call_RogueFace_79
                    ch_r "Hey, I told you you're not welcome."  
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -5)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, -2)
                    $ R_RecentActions.append("angry")                      
                    $ R_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (R_Sleep or R_SEXP >= 30):                                                   #It's late but she really likes you
                    ch_r "It's pretty late, [R_Petname], but it's always nice to see you."                    
            elif Current_Time == "Night" and (ApprovalCheck("Rogue", 1000, "LI") or ApprovalCheck("Rogue", 600, "OI")):     #It's late but she really likes you
                    ch_r "It's pretty late, [R_Petname], but you can come in for a little bit."                
            elif R_Addict >= 50:
                    ch_r "Um, yeah, you'd better come in. . ."
                    
            elif Current_Time == "Night" and (ApprovalCheck("Rogue", 500, "LI") or ApprovalCheck("Rogue", 300, "OI")):      #she likes you well enough but it's late
                    ch_r "It's a little late [R_Petname]. Maybe tomorrow."
                    $ R_RecentActions.append("noentry")                      
                    $ R_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Rogue", 600, "LI") or ApprovalCheck("Rogue", 300, "OI"):                                    #She quite likes you and lets you in   
                    ch_r "Sure, come on in [R_Petname]."        
            else:                                                                                                           #She doesn't like you      
                    ch_r "I'd rather you didn't come in, thanks."
                    $ R_RecentActions.append("noentry")                      
                    $ R_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg rogue"         
    call EventCalls from _call_EventCalls_5
    if R_Loc == "bg rogue" and "angry" in R_RecentActions:
        "Rogue pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg rogue":
        jump Misplaced
            
label Rogue_Room:
    $ bg_current = "bg rogue"
    call Set_The_Scene from _call_Set_The_Scene_20
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level from _call_Taboo_Level_3
    call QuickEvents from _call_QuickEvents_1
    call Checkout(1) from _call_Checkout_24    
    if Round <= 10:
                call Round10 from _call_Round10_2
                call Girls_Location from _call_Girls_Location_7
                call EventCalls from _call_EventCalls_6    
    call GirlsAngry from _call_GirlsAngry_1    
    call Set_The_Scene from _call_Set_The_Scene_21  
    
# Rogue's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_2
    if R_Loc == bg_current:
        $ Line = "You are in Rogue's room. What would you like to do?"
    else:
        $ Line = "You are in Rogue's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat from _call_Chat_1
        
        "Would you like to study?" if R_Loc == bg_current:                
                    call Rogue_Study from _call_Rogue_Study_1
            
        "Sleep." if Current_Time == "Night":
                    call Round10 from _call_Round10_3
                    call Girls_Location from _call_Girls_Location_8
                    call EventCalls from _call_EventCalls_7    
                    
        "Wait." if Current_Time != "Night":
                    call Round10 from _call_Round10_4
                    call Girls_Location from _call_Girls_Location_9
                    call EventCalls from _call_EventCalls_8 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry         
        "Other Girl's Rooms" if TravelMode:
            menu:
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Go to Mystique's Room" if "metgym" in newgirl["Mystique"].History:  
                            jump Mystique_Room_Entry
                "Back":
                            pass     
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap from _call_Worldmap_1 
    
    if "angry" in R_RecentActions:
            call RogueFace("angry") from _call_RogueFace_80
            ch_r "I really think you should leave."
            "Rogue pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Rogue_Room


label Rogue_Study:                       #study events
            call Shift_Focus("Rogue") from _call_Shift_Focus_43
            if Current_Time == "Night":
                ch_r "It's a little late for studying, maybe tomorrow."
                return
            elif Round <= 30:        
                ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
                return
            else:
                ch_r "Sure."
                        
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["You study for a while, it was fairly boring.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and watch a movie instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test."
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
            $ D20 = renpy.random.randint(1, 20)    
            if D20 > 10:
                call Rogue_Frisky_Study from _call_Rogue_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait from _call_Wait_3 
            call Rogue_Leave from _call_Rogue_Leave_2
            call Kitty_Leave from _call_Kitty_Leave_2
            return
#End Rogue Study
            
label Rogue_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Rogue", 1000) and R_Blow > 5:
                        "Rogue get a mischievous look on her face, and begins to unzip your pants."
                        "She pulls your dick out and pops it into her mouth."        
                        call Rogue_SexAct("blow") from _call_Rogue_SexAct 
            elif D20 > 14 and ApprovalCheck("Rogue", 1000) and R_Hand >= 5:
                        "Rogue get a mischievous look on her face, and begins to unzip your pants."
                        "She pulls your dick out and begins to slowly stroke it."        
                        call Rogue_SexAct("hand") from _call_Rogue_SexAct_1 
            elif D20 > 10 and (ApprovalCheck("Rogue", 1300) or (R_Mast and ApprovalCheck("Rogue", 1000))) and R_Lust >= 70:
                        "Rogue get a mischievous look on her face, and starts to rub herself."          
                        $ R_RecentActions.remove("unseen") if "unseen" in R_RecentActions else R_RecentActions #she sees you're there
                        $ Trigger = "masturbation"
                        call Rogue_SexAct("masturbate") from _call_Rogue_SexAct_2      
            elif D20 > 10 and ApprovalCheck("Rogue", 1200) and R_Lust >= 30:                
                        if not R_Over and not R_Legs and R_Panties != "shorts":
                                #if she's mostly naked, cheat
                                call RogueFace("sly") from _call_RogueFace_81                                
                                ch_r "Well, I did consider suggesting we do some \"strip studying,\". . ." 
                                $ R_Eyes = "down"
                                ch_r "but it looks like I got ahead of myself. . ."
                                $ R_Eyes = "squint"
                                ch_r "Did you have anything else in mind?"                                
                                call Rogue_SexMenu from _call_Rogue_SexMenu_2   
                        else:
                                "Rogue moves a bit closer to you, and then suggests \"strip studying.\""
                                call Rogue_Strip_Study from _call_Rogue_Strip_Study
            elif ApprovalCheck("Rogue", 700) and R_Kissed > 1:
                        "Rogue leans close to you, and leans in for a kiss."         
                        call Rogue_SexAct("kissing") from _call_Rogue_SexAct_3
            elif ApprovalCheck("Rogue", 500):
                        "Rogue leans close to you and you spend the rest of the study session nuzzled close."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return
    
label Rogue_Caught_Changing:
            call Shift_Focus("Rogue") from _call_Shift_Focus_44
            $ D20 = renpy.random.randint(1, 20)
            
            call RogueFace("surprised", 1) from _call_RogueFace_82
            $ R_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call RogueOutfit("nude") from _call_RogueOutfit_12
            elif D20 >15:       
                    #She's bottomless
                    $ R_Legs = 0
                    $ R_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ R_Over = 0
                    $ R_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ R_Over = 0
                    $ R_Legs = 0
                    $ R_Panties = "black panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ R_Over = 0
            #else: #fully dressed
            call Set_The_Scene from _call_Set_The_Scene_22
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Rogue is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Rogue is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Rogue is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Rogue has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Rogue has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Rogue", (D20 *70)) or (not R_SeenPussy and not R_Panties) or (not R_SeenChest and not R_Chest):
                            # She is mad
                            call RogueFace("surprised") from _call_RogueFace_83
                            $R_Brows = "angry"  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -50)
                            if not R_Over or not R_Legs:
                                $ R_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call RogueFace("surprised", 1) from _call_RogueFace_84      
                            $R_Brows = "confused"
                            if "exhibitionist" in R_Traits:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (2*D20))  
                            else:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, D20)
                          
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20)
                    if D20 > 17:
                        call Rogue_First_Topless from _call_Rogue_First_Topless
                        call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless
                    elif D20 > 15:
                        call Rogue_First_Bottomless from _call_Rogue_First_Bottomless_1
                    elif D20 > 14:
                        call Rogue_First_Topless from _call_Rogue_First_Topless_1
                    menu:
                        ch_r "Hey! Learn to knock maybe?!"
                        "Sorry, I should have knocked.":  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 4)
                        "And miss the view?":
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Rogue", 800) and (not R_SeenPussy or not R_SeenChest):            
                            call RogueFace("angry") from _call_RogueFace_85
                            $R_Brows = "confused"
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                    else:
                            call RogueFace("sexy") from _call_RogueFace_86
                            $R_Brows = "confused"
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                    menu:
                        ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                        "Sorry, I should have knocked.":   
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                        "Well, to be honest. . .":
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, -2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
            call RogueFace("sexy") from _call_RogueFace_87                
            if ApprovalCheck("Rogue", 750) and R_SeenPussy and R_SeenChest:
                    ch_r "You could have just asked, [R_Petname]."  
                    if R_Over != "blue dress" and R_Over != "red dress":
                        $ R_Over = 0
                    $ R_Upskirt = 1
                    pause 1     
                    call RogueOutfit
                    $ R_Upskirt = 0
                    "She flashes you real quick."  
            else:
                    ch_r "Well, it happens, just be careful next time."   
            menu:
                    ch_r "Well, are you planning to stick around?" 
                    "Sure, for a bit.":
                        pass
                    "Actually, I should get going. . .":
                        call RogueOutfit from _call_RogueOutfit_14
                        call Worldmap from _call_Worldmap_2            
            jump Rogue_Room
            return
            #End Rogue Caught Changing
# end Rogue's Room Interface //////////////////////////////////////////////////////////////////////



# University Square Interface //////////////////////////////////////////////////////////////////////

label Campus_Map:
    $ Line = 0
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ bg_current = "bg campus"
    call Set_The_Scene from _call_Set_The_Scene_23
    if not TravelMode: 
        call Worldmap from _call_Worldmap_3
    jump Campus
    
label Campus_Entry:
    $ bg_current = "bg campus"             
    call Gym_Clothes from _call_Gym_Clothes_2  
    call Taboo_Level from _call_Taboo_Level_4
    $ P_RecentActions.append("traveling")
    call EventCalls from _call_EventCalls_9
    call Set_The_Scene from _call_Set_The_Scene_24
    
label Campus:
    $ bg_current = "bg campus"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Set_The_Scene from _call_Set_The_Scene_25
    call Taboo_Level from _call_Taboo_Level_5
    call QuickEvents from _call_QuickEvents_2    
    call Checkout(1) from _call_Checkout_25    
    call GirlsAngry from _call_GirlsAngry_2      

# Uni Square Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in the university square. What would you like to do?"
        
        "Chat":
            call Chat from _call_Chat_2
            
        "Wait." if Current_Time != "Night":
            "You wait around a bit."
            call Wait from _call_Wait_4   
            call EventCalls from _call_EventCalls_10            
            call Girls_Location from _call_Girls_Location_10
            
        "Go to my Room" if TravelMode:
                    jump Player_Room_Entry  
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Mystique's Room" if "metgym" in newgirl["Mystique"].History:
                            jump Mystique_Room_Entry
                "Back":
                            pass
        "Go to the classroom" if TravelMode: 
                    if Current_Time != "Night":
                        jump Class_Room_Entry 
                    elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        jump Class_Room_Entry 
                    else:
                        "It's late for classes and the classrooms are locked down."   
        "Go to the Danger Room" if TravelMode: 
                    jump Danger_Room_Entry

        "Go to the Pool" if TravelMode: 
                    jump Pool_Entry

        "Go to the football field" if TravelMode: 
                    jump Field_Entry     

        "Go to the showers" if TravelMode: 
                    jump Shower_Room_Entry            
        "Xavier's Study" if TravelMode: 
                    jump Study_Room_Entry 
        "Leave [[Navigation map]" if not TravelMode: 
                    call Worldmap from _call_Worldmap_4                      
    jump Campus

# end University Square Interface //////////////////////////////////////////////////////////////////////



# Classroom Interface //////////////////////////////////////////////////////////////////////

label Class_Room_Entry:
    $ Adjacent = 0
    $ bg_current = "bg classroom"              
    call Gym_Clothes from _call_Gym_Clothes_3 
    call Taboo_Level from _call_Taboo_Level_6
    $ P_RecentActions.append("traveling")
    call EventCalls from _call_EventCalls_11
    call Set_The_Scene from _call_Set_The_Scene_26
    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_3
    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_2
    if Current_Time != "Night" and Current_Time != "Evening" and Weekday < 5:   
            call Class_Room_Seating from _call_Class_Room_Seating    
    if E_Loc == "bg teacher":
        $ Line = "As you sit down, you see "+ EmmaName +" at the podium. What would you like to do?" 
    elif Current_Time == "Evening" or Weekday > 5:   
        $ Line = "You enter the classroom. What would you like to do?" 
    else:
        $ Line = "You sit down at a desk. What would you like to do?" 
        
label Class_Room:    
    $ bg_current = "bg classroom"    
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Set_The_Scene from _call_Set_The_Scene_27
    call Taboo_Level from _call_Taboo_Level_7
    call QuickEvents from _call_QuickEvents_3    
    call Checkout(1) from _call_Checkout_26
    if "vcame" in K_RecentActions:
        $ K_Wet = 2
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait from _call_Wait_5   
                call EventCalls from _call_EventCalls_12
                call Girls_Location from _call_Girls_Location_11
                call Set_The_Scene from _call_Set_The_Scene_28
    call GirlsAngry from _call_GirlsAngry_3      
    if not Line:
        $ Line = "You are in class right now. What would you like to do?" 
    #End Room Set-up
    
# Class Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<        
    menu:
        "[Line]" 
        "Take the morning class" if Weekday < 5 and Current_Time == "Morning":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until the next one."             
        "Take the afternoon class" if Weekday < 5 and Current_Time == "Midday":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until they lock up for the night." 
        "There are no classes right now (locked)" if Weekday >= 5 or Current_Time == "Evening" or Current_Time == "Night":
                pass
            
        "Chat":
                call Chat from _call_Chat_3
                $ Line = "You are in class right now. What would you like to do?"

        "Turn Kitty's vibrator on" if Weekday < 5 and (Current_Time == "Morning" or Current_Time == "Midday") and K_Loc == bg_current and "vibeclass" in K_Traits:
                "You turn Kitty's vibrator on"
                $ K_Vibrator = 1
                play music "sounds/vibrator1.wav" fadein 1 fadeout 1
                if K_Loc == bg_current:
                    call KittyFaceSpecial("surprised", 1) from _call_KittyFaceSpecial 
                    
                    with Shake((0, 0, 0, 0), 3.0, dist=5)
                    if "vibratorclass" not in K_History:
                        ch_k "What are you doing [K_Petname]??"
                        if "exhibitionist" in K_Traits:
                            call KittyFaceSpecial("sexy", 1) from _call_KittyFaceSpecial_1 
                            "Kitty starts moving in her seat. She can't keep still."
                            "She looks at you with a sexy smile."
                            if Adjacent == "Kitty":
                                ch_k "I like how you think, [K_Petname]."
                        else:
                            call KittyFaceSpecial("sad", 1) from _call_KittyFaceSpecial_2 
                            "Kitty starts moving in her seat. She can't keep still."
                            "She looks at you with a begging face."
                            if Adjacent == "Kitty":
                                ch_k "Please stop this, [K_Petname]."
                        $ K_History.append("vibratorclass")
                    elif "exhibitionist" not in K_Traits:
                        ch_k "Not this again."
                        "She looks at you with a begging face."
                        if Adjacent == "Kitty":
                            ch_k "Please [K_Petname], not in public."
                    else:
                        ch_k "This again huh"
                        call KittyFaceSpecial("sexy", 1) from _call_KittyFaceSpecial_3
                        "She looks at you with a sexy smile"
                        if Adjacent == "Kitty":
                            ch_k "Please [K_Petname], make it go faster."
                    
                    label V_Kitty_On:

                        if K_Vibrator == 2:
                            with Shake((0, 0, 0, 0), 3.0, dist=5)
    
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 100, 5)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 10)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)  

                        with Shake((0, 0, 0, 0), 3.0, dist=5)
                        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 100, 5)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 10)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 2)  

                        if K_Lust <= 50:
                            if K_Legs or K_Panties:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "She tugs her bottoms.",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])
                            else:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])

                        else:

                            $ Line = renpy.random.choice(["Her hand traces slowly down her body", 
                                "Her fingers move lightly across her pubic region",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "Her hands move along her sides, carefully caressing them",
                                "She gently rubs her breasts", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])  

                        "[Line]"
                        call KittyLust from _call_KittyLust 
                        if K_Lust >= 100:                                               
                            call K_Cumming from _call_K_Cumming
                            $ K_Lust = 45
                            $ K_RecentActions.append("vcame")
                            if Situation == "shift" or "angry" in K_RecentActions:
                                jump KFB_After
                        menu:
                            "Keep it on":
                                jump V_Kitty_On
                            "Turn it up" if K_Vibrator != 2:
                                play music "sounds/vibrator2.wav"
                                $ K_Vibrator = 2
                                $ K_Mouth = "tongue"
                                $ K_Eyes = "surprised"
                                $ K_Blush = 2
                                "You increase the vibrator speed startling her"

                                jump V_Kitty_On

                            "Turn it off":
                                stop music fadeout 1

                                if "exhibitionist" not in K_Traits:
                                    if Adjacent == "Kitty":
                                        ch_k "Thanks, [K_Petname]."
                                else:
                                    call KittyFaceSpecial("sad", 1) from _call_KittyFaceSpecial_4
                                    "She looks at you with a sad face"
                                    if Adjacent == "Kitty":
                                        ch_k "Why did you stop, [K_Petname]?"

        "Turn Rogue's vibrator on" if Weekday < 5 and (Current_Time == "Morning" or Current_Time == "Midday") and R_Loc == bg_current and "vibeclass" in R_Traits:
                "You turn Rogue's vibrator on"
                $ R_Vibrator = 1
                play music "sounds/vibrator1.wav" fadein 1 fadeout 1
                if R_Loc == bg_current:
                    call RogueFaceSpecial("surprised", 1) from _call_RogueFaceSpecial 
                    
                    with Shake((0, 0, 0, 0), 3.0, dist=5)
                    if "vibratorclass" not in R_History:
                        ch_r "What are you doing [R_Petname]??"
                        if "exhibitionist" in R_Traits:
                            call RogueFaceSpecial("sexy", 1) from _call_RogueFaceSpecial_1 
                            "Rogue starts moving in her seat. She can't keep still."
                            "She looks at you with a sexy smile."
                            if Adjacent == "Rogue":
                                ch_r "I like how you think, [R_Petname]."
                        else:
                            call RogueFaceSpecial("sad", 1) from _call_RogueFaceSpecial_2 
                            "Rogue starts moving in her seat. She can't keep still."
                            "She looks at you with a begging face."
                            if Adjacent == "Rogue":
                                ch_r "Please stop this, [R_Petname]."
                        $ R_History.append("vibratorclass")
                    elif "exhibitionist" not in R_Traits:
                        ch_r "Not this again."
                        "She looks at you with a begging face."
                        if Adjacent == "Rogue":
                            ch_r "Please [R_Petname], not in public."
                    else:
                        ch_r "This again huh"
                        call RogueFaceSpecial("sexy", 1) from _call_RogueFaceSpecial_3
                        "She looks at you with a sexy smile"
                        if Adjacent == "Rogue":
                            ch_r "Please [R_Petname], make it go faster."
                    
                    label V_Rogue_On:

                        if R_Vibrator == 2:
                            with Shake((0, 0, 0, 0), 3.0, dist=5)
    
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 100, 5)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)  

                        with Shake((0, 0, 0, 0), 3.0, dist=5)
                        $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 100, 5)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 1)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)  

                        if R_Lust <= 50:
                            if R_Legs or R_Panties:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "She tugs her bottoms.",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])
                            else:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])

                        else:

                            $ Line = renpy.random.choice(["Her hand traces slowly down her body", 
                                "Her fingers move lightly across her pubic region",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "Her hands move along her sides, carefully caressing them",
                                "She gently rubs her breasts", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])  

                        "[Line]"
                        call RogueLust from _call_RogueLust 
                        if R_Lust >= 100:                                               
                            call R_Cumming from _call_R_Cumming
                            $ R_Lust = 45
                            $ R_RecentActions.append("vcame")
                            if Situation == "shift" or "angry" in R_RecentActions:
                                jump RFB_After
                        menu:
                            "Keep it on":
                                jump V_Rogue_On
                            "Turn it up" if R_Vibrator != 2:
                                play music "sounds/vibrator2.wav"
                                $ R_Vibrator = 2
                                $ R_Mouth = "tongue"
                                $ R_Eyes = "surprised"
                                $ R_Blush = 2
                                "You increase the vibrator speed startling her"

                                jump V_Rogue_On

                            "Turn it off":
                                stop music fadeout 1

                                if "exhibitionist" not in R_Traits:
                                    if Adjacent == "Rogue":
                                        ch_r "Thanks, [R_Petname]."
                                else:
                                    call RogueFaceSpecial("sad", 1) from _call_RogueFaceSpecial_4
                                    "She looks at you with a sad face"
                                    if Adjacent == "Rogue":
                                        ch_r "Why did you stop, [R_Petname]?"

        "Turn Emma's vibrator on" if Weekday < 5 and (Current_Time == "Morning" or Current_Time == "Midday") and (E_Loc == bg_current or E_Loc == "bg teacher") and "vibeclass" in E_Traits:
                "You turn Emma's vibrator on"
                $ E_Vibrator = 1
                play music "sounds/vibrator1.wav" fadein 1 fadeout 1
                if (E_Loc == bg_current or E_Loc == "bg teacher"):
                    call EmmaFaceSpecial("surprised", 1) from _call_EmmaFaceSpecial 
                    
                    with Shake((0, 0, 0, 0), 3.0, dist=5)
                    if "vibratorclass" not in E_History:
                        #ch_e "What are you doing [E_Petname]??"
                        if "exhibitionist" in E_Traits:
                            call EmmaFaceSpecial("sexy", 1) from _call_EmmaFaceSpecial_1 
                            "Emma starts moving her body. She can't keep still."
                            "She looks at you with a sexy smile."
                            if Adjacent == "Emma":
                                ch_e "I like how you think, [E_Petname]."
                        else:
                            call EmmaFaceSpecial("sad", 1) from _call_EmmaFaceSpecial_2 
                            "Emma starts moving her body. She can't keep still."
                            "She looks at you with a begging face."
                            if Adjacent == "Emma":
                                ch_e "Please stop this, [E_Petname]."
                        $ E_History.append("vibratorclass")
                    elif "exhibitionist" not in E_Traits:
                        #ch_e "Not this again."
                        "She looks at you with a begging face."
                        if Adjacent == "Emma":
                            ch_e "Please [E_Petname], not in public."
                    else:
                        #ch_e "This again huh"
                        call EmmaFaceSpecial("sexy", 1) from _call_EmmaFaceSpecial_3
                        "She looks at you with a sexy smile"
                        if Adjacent == "Emma":
                            ch_e "Please [E_Petname], make it go faster."
                    
                    label V_Emma_On:

                        if E_Vibrator == 2:
                            with Shake((0, 0, 0, 0), 3.0, dist=5)
    
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 100, 5)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 10)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)  

                        with Shake((0, 0, 0, 0), 3.0, dist=5)
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 100, 5)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 10)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)  

                        if E_Lust <= 50:
                            if E_Legs or E_Panties:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "She tugs her bottoms.",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])
                            else:
                                $ Line = renpy.random.choice(["She tries to keep it together", 
                                    "She keeps moving her body as if that movement would reduce the vibrations",
                                    "Her hands move along her sides",
                                    "She looks around trying to see if anyone can notice the noise", 
                                    "She moves her hands to rub her neck",
                                    "She gasps as her movements only makes her hornier"])

                        else:

                            $ Line = renpy.random.choice(["Her hand traces slowly down her body", 
                                "Her fingers move lightly across her pubic region",
                                "Her fingers move up and down her inner thighs, slowing building towards their center",
                                "Her hands move along her sides, carefully caressing them",
                                "She gently rubs her breasts", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])  

                        "[Line]"
                        call EmmaLust from _call_EmmaLust_6 
                        if E_Lust >= 100:                                               
                            call E_Cumming from _call_E_Cumming_6
                            $ E_Lust = 45
                            $ E_RecentActions.append("vcame")
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_FB_After
                        menu:
                            "Keep it on":
                                jump V_Emma_On
                            "Turn it up" if E_Vibrator != 2:
                                play music "sounds/vibrator2.wav"
                                $ E_Vibrator = 2
                                $ E_Mouth = "tongue"
                                $ E_Eyes = "surprised"
                                $ E_Blush = 2
                                "You increase the vibrator speed startling her"

                                jump V_Emma_On

                            "Turn it off":
                                stop music fadeout 1

                                if "exhibitionist" not in E_Traits:
                                    if Adjacent == "Emma":
                                        ch_e "Thanks, [E_Petname]."
                                else:
                                    call EmmaFaceSpecial("sad", 1) from _call_EmmaFaceSpecial_4
                                    "She looks at you with a sad face"
                                    if Adjacent == "Emma":
                                        ch_e "Why did you stop, [E_Petname]?"

            
        "Wait" if Current_Time != "Night":
                "You hang out for a bit."
                call Wait from _call_Wait_6   
                call EventCalls from _call_EventCalls_13            
                call Girls_Location from _call_Girls_Location_12 
                    
                if Current_Time == "Midday":
                            $ Line = "A new class is in session. What would you like to do?"
                if Current_Time == "Evening":
                            $ Line = "Classes have let out for the day. What would you like to do?"
            
        "Leave [[Go to Campus Square]":
                if TravelMode:
                    jump Campus_Entry
                else:
                    call Worldmap from _call_Worldmap_5 
    
    $ Line = 0
    jump Class_Room

# End Core Classroom menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
label Take_Class:                       #Class events 
    call Set_The_Scene from _call_Set_The_Scene_29  
    if "vcame" in K_RecentActions:
        $ K_Wet = 2
    if "vcame" in R_RecentActions:
        $ R_Wet = 2
    if "vcame" in E_RecentActions:
        $ E_Wet = 2
    if "class" in P_DailyActions:
            $ Line = "The session begins."
    elif Round >= 80:
            $ Line = "You make it in time for the start of the class."
    elif Round >= 50:
            $ Line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
            $ Line = "You're pretty late, but catch the tail end of the class."
    $ Trigger = 0
    
    $ D20 = renpy.random.randint(1, 20)
    if Adjacent == "Rogue" and D20 > 10 and R_Inbt >= 500 and R_Loc == "bg classroom":        
        "[Line]"    
        call Rogue_Frisky_Class from _call_Rogue_Frisky_Class
    else:        
        $ Line = Line + renpy.random.choice([" It was fairly boring.", 
                " It was a lesson in mutant biology.", 
                " You took a math course.",
                " You watched a movie about sealions.",
                " That was fun.",
                " Mutant History, Apocalypse to Dark Phoenix.",
                " Game writing for dummies, eh?"]) 
        "[Line]"    
    $ P_RecentActions.append("class")                      
    $ P_DailyActions.append("class")   
    $ P_XP += (5 + (int(Round / 10)))
        
    call Wait from _call_Wait_7   
    call Girls_Location from _call_Girls_Location_13
    call Set_The_Scene from _call_Set_The_Scene_30 
    call EventCalls from _call_EventCalls_14
    $ Line = "What would you like to do next?"    
    jump Class_Room
    
# End "Taking Class" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<          


label Class_Room_Seating(Line = 0):
    $ Adjacent = 0
    if R_Loc == bg_current:
                if K_Loc == bg_current:                  
                        $ D20 = renpy.random.randint(1, 20) 
                        $ Line = "You see that Rogue and Kitty are sitting next to each other, which do you sit next to?"
                        if D20 >= 5 and (R_LikeKitty + K_LikeRogue) >= 1400:
                                pass
                        elif D20 >= 10 and (R_LikeKitty + K_LikeRogue) >= 1000:
                                pass
                        elif D20 >= 15:
                                pass
                        else:
                                "You see that Rogue and Kitty are in the room, but on opposite sides."
                                $ Line = "Which do you sit next to?"     
                        menu:
                            "[Line]"
                            "Rogue":
                                    $ Adjacent = "Rogue"
                            "Kitty":
                                    $ Adjacent = "Kitty"                                    
                            "Neither":
                                    "You decide to sit a distance away from either of them."
                else: #Just Rogue
                        menu:
                            "You see Rogue is there, do you sit next to her?"
                            "Yes":
                                    $ Adjacent = "Rogue"
                            "No, I'll sit away from her a bit.":
                                    pass
    elif K_Loc == bg_current and not Adjacent:     
                        menu:
                            "You see Kitty is there, do you sit next to her?"
                            "Yes":
                                    $ Adjacent = "Kitty"
                            "No, I'll sit away from her a bit.":
                                    pass
    return
    
# end Class Room Interface //////////////////////////////////////////////////////////////////////

# Pool Room Interface //////////////////////////////////////////////////////////////////////

label Pool_Entry:
    $ bg_current = "bg pool"    
    call Taboo_Level from _call_Taboo_Level_8
    $ P_RecentActions.append("traveling")
    call EventCalls from _call_EventCalls_15
    call Pool_Clothes("pre") from _call_Pool_Clothes#Automatically puts them in pool clothes if they've been here
    call Set_The_Scene from _call_Set_The_Scene_31
    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_4
    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_3
    "This is the Pool. What would you like to do?" 
    
label Pool_Room:
    $ bg_current = "bg pool"  
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")  

    call Set_The_Scene from _call_Set_The_Scene_32
    call Taboo_Level from _call_Taboo_Level_9  
    call QuickEvents from _call_QuickEvents_4
  
    if "cockout" in P_RecentActions:
        call Checkout(1) from _call_Checkout_27
        $ P_RecentActions.append("cockout")
    else:
        call Checkout(1) from _call_Checkout_28



    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                        
                call Wait from _call_Wait_8   
                call EventCalls from _call_EventCalls_16
                call Girls_Location from _call_Girls_Location_14 
                call Set_The_Scene from _call_Set_The_Scene_33
                call Pool_Clothes from _call_Pool_Clothes_1                
    call GirlsAngry from _call_GirlsAngry_4  
    
    call Check_Outfit_Event from _call_Check_Outfit_Event

# Pool Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "This is the Pool. What would you like to do?" 
#        extend ""        
                    
        "Chat":
                call Chat from _call_Chat_4
            
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait from _call_Wait_9   
                call EventCalls from _call_EventCalls_17
                call Pool_Clothes from _call_Pool_Clothes_2
                call Girls_Location from _call_Girls_Location_15 
                call Pool_Clothes from _call_Pool_Clothes_3
                #jump Pool_Area

        "Go for a swim" if Round > 30 and Current_Time != "Night":
                call Swimming from _call_Swimming
        "Go for a swim (locked)" if Round <= 30 or Current_Time == "Night":            
                pass

        # "Go for a swim." if Current_Time != "Night":
        #         if R_Loc == bg_current or K_Loc == bg_current or E_Loc == bg_current:
        #             "Let's go for a swim"
        #             if R_Loc == bg_current:
        #                 ch_r "yay"

        #                 if R_Outfit != "swimsuit2" and R_Outfit != "swimsuit1":
        #                     #ch_r "I'l be right there, let me just put on my swimsuit"
        #                     call Pool_Clothes("goswim", "Rogue")
        #                     ch_r "Let's go"
                        
        #                 call RogueFace("happy")                            
        #                 $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 4)          
        #                 $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 2)            
        #                 $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 4)
        #                 $ R_Water = 2


        #             if K_Loc == bg_current:
        #                 ch_k "yay"

        #                 if K_Outfit != "purple bikini" and K_Outfit != "swimsuit3":
        #                     #ch_k "I'l be right there, let me just put on my bikini"
        #                     call Pool_Clothes("goswim", "Kitty")
        #                     ch_k "Let's go"

        #                 call KittyFace("happy")                            
        #                 $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 4)          
        #                 $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)            
        #                 $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 4)
        #                 $ K_Water = 2


        #             if E_Loc == bg_current:
        #                 ch_e "yay"

        #                 if E_Outfit != "bikini" and E_Outfit != "naked pool":
        #                     #ch_e "I'l be right there, let me just put on my bikini"
        #                     call Pool_Clothes("goswim", "Emma")
        #                     ch_e "Let's go"

        #                 call EmmaFace("happy")                            
        #                 $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 4)          
        #                 $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)            
        #                 $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 4)
        #                 $ E_Water = 2

        #             if newgirl["Mystique"].Loc == bg_current:
        #                 ch_e "yay"

        #                 if newgirl["Mystique"].Outfit != "bikini" and newgirl["Mystique"].Outfit != "naked pool":
        #                     #ch_e "I'l be right there, let me just put on my bikini"
        #                     call Pool_Clothes("goswim", "Mystique")
        #                     ch_m "Let's go"

        #                 call MystiqueFace("happy")                            
        #                 $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 4)          
        #                 $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)            
        #                 $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 4)
        #                 $ newgirl["Mystique"].Water = 2
        #                 #$ K_RecentActions.append("showered")                      
        #             #"You take a swim"

        #                 #$ K_DailyActions.append("showered")
        #                 #call Set_The_Scene
        #             "That felt great"
        #             call Wait   
        #             call EventCalls
        #             call Pool_Clothes
        #             call Girls_Location 
        #             call Pool_Clothes

        #             #if R_Loc == bg_current:

        #         else:
        #             "You take a swim by yourself"
        #             call Wait   
        #             call EventCalls
        #             call Pool_Clothes
        #             call Girls_Location 
        #             call Pool_Clothes

        "Skinny dipping?" if Current_Time == "Night":# and (R_Loc == bg_current or K_Loc == bg_current or E_Loc == bg_current):
                call Skinny_Dipping from _call_Skinny_Dipping


            

        "Leave [[Go to Campus Square]":    
                if TravelMode:        
                    call Pool_Clothes("change") from _call_Pool_Clothes_4
                    jump Campus_Entry
                else:
                    call Worldmap from _call_Worldmap_6         
        "Go to the showers" if TravelMode:             
                call Pool_Clothes("change") from _call_Pool_Clothes_5
                jump Shower_Room_Entry         
    jump Pool_Room


label Swimming(Occupants = 0, Agreed = 0, RogueCount = 0, KittyCount = 0, EmmaCount = 0, Showered = 0, Line = 0):
    
    if R_Loc == bg_current or K_Loc == bg_current or E_Loc == bg_current or newgirl["Mystique"].Loc == bg_current:
        "Let's go for a swim"
        if R_Loc == bg_current:
            ch_r "yay"
            if R_Outfit != "swimsuit2" and R_Outfit != "swimsuit1":
                #ch_r "I'l be right there, let me just put on my swimsuit"
                call Pool_Clothes("goswim", "Rogue") from _call_Pool_Clothes_6
                ch_r "Let's go"
            
            call RogueFace("happy") from _call_RogueFace_88                            
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 4)          
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 40, 2)            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, 4)
            $ R_Water = 2
            $ R_Spunk = []
        if K_Loc == bg_current:
            ch_k "yay"
            if K_Outfit != "purple bikini" and K_Outfit != "swimsuit3":
                #ch_k "I'l be right there, let me just put on my bikini"
                call Pool_Clothes("goswim", "Kitty") from _call_Pool_Clothes_7
                ch_k "Let's go"
            call KittyFace("happy") from _call_KittyFace_1                            
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 4)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 2)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, 4)
            $ K_Water = 2
            $ K_Spunk = []
        if E_Loc == bg_current:
            ch_e "yay"
            if E_Outfit != "bikini" and E_Outfit != "naked pool":
                #ch_e "I'l be right there, let me just put on my bikini"
                call Pool_Clothes("goswim", "Emma") from _call_Pool_Clothes_8
                ch_e "Let's go"
            call EmmaFace("happy") from _call_EmmaFace_227                            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 4)          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 4)
            $ E_Water = 2
            $ E_Spunk = []
        if newgirl["Mystique"].Loc == bg_current:
            ch_e "yay"
            if newgirl["Mystique"].Outfit != "bikini" and newgirl["Mystique"].Outfit != "naked pool":
                #ch_e "I'l be right there, let me just put on my bikini"
                call Pool_Clothes("goswim", "Mystique") from _call_Pool_Clothes_9
                ch_m "Let's go"
            call MystiqueFace("happy") from _call_MystiqueFace_328                            
            $ newgirl["Mystique"].Love = Statupdate("Mystique", "Love", newgirl["Mystique"].Love, 90, 4)          
            $ newgirl["Mystique"].Obed = Statupdate("Mystique", "Obed", newgirl["Mystique"].Obed, 40, 2)            
            $ newgirl["Mystique"].Inbt = Statupdate("Mystique", "Inbt", newgirl["Mystique"].Inbt, 30, 4)
            $ newgirl["Mystique"].Water = 2
            $ newgirl["Mystique"].Spunk = []
            #$ K_RecentActions.append("showered")                      
        #"You take a swim"
            #$ K_DailyActions.append("showered")
            #call Set_The_Scene
        "That felt great"
        $ Round -= 30
        # call Wait   
        # call EventCalls
        # call Pool_Clothes
        # call Girls_Location 
        # call Pool_Clothes
        #if R_Loc == bg_current:
    else:
        "You take a swim by yourself"
        $ Round -= 30
        # call Wait   
        # call EventCalls
        # call Pool_Clothes
        # call Girls_Location 
        # call Pool_Clothes

            
    if Round < 1:
        call Wait from _call_Wait_10   
        call EventCalls from _call_EventCalls_18
        call Pool_Clothes from _call_Pool_Clothes_10
        call Girls_Location from _call_Girls_Location_16 
        call Pool_Clothes from _call_Pool_Clothes_11
    return
# End Swimming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Pool Room Skinny Dipping Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

label Skinny_Dipping(Occupants = 0, Agreed = 0, RogueCount = 0, KittyCount = 0, EmmaCount = 0, Showered = 0, Line = 0):

    $ MystiqueCount = 0
    if R_Loc == "bg pool":
            $ Occupants += 1
            $ RogueCount = 1
    if K_Loc == "bg pool":        
            $ Occupants += 1
            $ KittyCount = 1
    if E_Loc == "bg pool":        
            $ Occupants += 1
            $ EmmaCount = 1
    if newgirl["Mystique"].Loc == "bg pool":        
            $ Occupants += 1
            $ MystiqueCount = 1
        
    if Occupants:
            ch_p "Hey, it's just us here, i'm going for a skinny dip, wanna join?" 
            ch_p "It's gonna be fun" 
            
            #if RogueCount and "showered" in R_RecentActions:
            #    if Occupants >1:
            #        ch_r "We actually just finished up, so we'll head out."
            #    else:
            #        ch_r "I actually just finished up, so I'll head out."
            #    $ Showered = 1
            #elif KittyCount and "showered" in K_RecentActions:
            #        ch_k "I actually just showered, so I'm head out."
            #        $ Showered = 1
            #else:   #girl not showered
            if RogueCount:
                if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                    ch_r "I suppose I could. . ."
                    $ RogueCount = 2
                    $ Agreed += 1
                else:
                    ch_r "Nah, I should probably get going."
            if KittyCount:
                if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                    if RogueCount > 1:                          #If Rogue said yes
                        ch_k "I guess I could join too. . ."
                    elif Occupants > 1:                     #If Rogue said no
                        ch_k "Well, I could join you, [K_Petname]."
                    else:                                   #If Rogue isn't there
                        ch_k "Yeah, I could stick around, [K_Petname]."
                    $ KittyCount = 2
                    $ Agreed += 1
                else:
                    if RogueCount > 1:                          #If Rogue said yes
                        ch_k "I've really got to go though. . ."
                    elif Occupants > 1:                     #If Rogue said no
                        ch_k "Yeah, I should head out too."
                    else:                                   #If Rogue isn't there
                        ch_k "No, I've got to get going."

            if EmmaCount:
                if ApprovalCheck("Emma", 1500) or (ApprovalCheck("Emma", 800) and E_SeenChest and E_SeenPussy):
                    if RogueCount > 1 or KittyCount > 1:                          #If Rogue or Kitty said yes
                        ch_e "I guess I could join too. . ."
                    elif Occupants > 1:                     #If Rogue and Kitty said no
                        ch_e "Well, I could join you, [E_Petname]."
                    else:                                   #If Rogue and Kitty aren't there
                        ch_e "Yeah, I could stick around, [E_Petname]."
                    $ EmmaCount = 2
                    $ Agreed += 1
                else:
                    if RogueCount > 1 or KittyCount > 1:                          #If Rogue or Kitty said yes
                        ch_e "I've really got to go though. . ."
                    elif Occupants > 1:                     #If Rogue and Kitty said no
                        ch_e "Yeah, I should head out too."
                    else:                                   #If Rogue and Kitty aren't there
                        ch_e "No, I've got to get going."

            if MystiqueCount:
                if ApprovalCheck("Mystique", 1500) or (ApprovalCheck("Mystique", 800) and E_SeenChest and E_SeenPussy):
                    if RogueCount > 1 or KittyCount > 1:                          #If Rogue or Kitty said yes
                        ch_m "I guess I could join too. . ."
                    elif Occupants > 1:                     #If Rogue and Kitty said no
                        ch_m "Well, I could join you, [E_Petname]."
                    else:                                   #If Rogue and Kitty aren't there
                        ch_m "Yeah, I could stick around, [E_Petname]."
                    $ MystiqueCount = 2
                    $ Agreed += 1
                else:
                    if RogueCount > 1 or KittyCount > 1:                          #If Rogue or Kitty said yes
                        ch_m "I've really got to go though. . ."
                    elif Occupants > 1:                     #If Rogue and Kitty said no
                        ch_m "Yeah, I should head out too."
                    else:                                   #If Rogue and Kitty aren't there
                        ch_m "No, I've got to get going."
                            
            if Occupants > Agreed:                    #if either said no     
                # If they're at NameCount = 2 here, they have already agreed.
                
                menu:
                    extend ""
                    "Ok, see you later then.":
                        if RogueCount == 1:
                            ch_r "Yeah, later."
                        if KittyCount == 1:
                            ch_k "Bye!"
                        if EmmaCount == 1:
                            ch_e "Bye, [E_Petname]!"
                        if MystiqueCount == 1:
                            ch_m "Bye!"
                        
                    "Sure you you don't wanna join? The night is perfect for a swim.":
                        $ Line = "night"
                                                        
                    #fix Add "Take off your own clothes" option.
                    
                    "Sure you you don't wanna join? It's very dark, I won't even see a thing.":
                        $ Line = "dark"
                        
                    #"But I didn't get to watch." if Showered:
                    #    $ Line = "watch you"
                        
                if Line:
                    if RogueCount == 1: 
                        if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                            $ RogueCount = 2
                        elif Line == "night" and ApprovalCheck("Rogue", 1000, "LI"):                                
                            $ RogueCount = 2
                        elif Line == "dark" and ApprovalCheck("Rogue", 600, "O"):                                
                            $ RogueCount = 2
                        #else, she doesn't agree
                            
                    if KittyCount == 1:
                        if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                            ch_k "yes"
                            $ KittyCount = 2
                        elif Line == "night" and ApprovalCheck("Kitty", 1200, "LI"):                                
                            $ KittyCount = 2
                        elif Line == "dark" and ApprovalCheck("Kitty", 600, "O"):                                
                            $ KittyCount = 2
                        #else, she doesn't agree

                    if EmmaCount == 1:
                        if ApprovalCheck("Emma", 1500) or (ApprovalCheck("Emma", 800) and E_SeenChest and E_SeenPussy):
                            ch_e "yes"
                            $ EmmaCount = 2
                        elif Line == "night" and ApprovalCheck("Emma", 1300, "LI"):                                
                            $ EmmaCount = 2
                        elif Line == "dark" and ApprovalCheck("Emma", 700, "O"):                                
                            $ EmmaCount = 2

                    if MystiqueCount == 1:
                        if ApprovalCheck("Mystique", 1500) or (ApprovalCheck("Mystique", 800) and newgirl["Mystique"].SeenChest and newgirl["Mystique"].SeenPussy):
                            ch_m "yes"
                            $ MystiqueCount = 2
                        elif Line == "night" and ApprovalCheck("Mystique", 1300, "LI"):                                
                            $ MystiqueCount = 2
                        elif Line == "dark" and ApprovalCheck("Mystique", 700, "O"):                                
                            $ MystiqueCount = 2
                    
                    
                    if Line == "night":      #"Sure you got every spot?"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Fine, I could use a good swim."
                                if KittyCount == 2:
                                    ch_k "Um, me too!"
                                if EmmaCount == 2:
                                    ch_e "Yeah, me too!"
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "Oh, I guess I could enjoy a good swim before sleep."
                                if EmmaCount == 2:
                                    ch_e "Yeah, me too!"
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            elif EmmaCount == 2:
                                ch_e "Yeah, I guess I could use a good swim."
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            elif MystiqueCount == 2:
                                    ch_m "Ok"
                            
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Perfect for a swim, not a naked one."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "Ha, I'm not gonna swim naked with you, [K_Petname], see you later."
                            if EmmaCount == 1:                                  #Rogue agreed, Emma refused
                                ch_e "Ha, I'm not gonna swim, [E_Petname], specially not with a student."  
                            if MystiqueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_m "Perfect for a swim, not a naked one."        
                        
                    elif Line == "dark":  #"its dark"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Yeah, I guess it's dark enough."
                                if KittyCount == 2:
                                    ch_k "Um, yeah, I guess. . ."
                                if EmmaCount == 2:
                                    ch_e "Yeah, me too!"
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            elif KittyCount == 2:                               #Kitty
                                ch_k "I. . . guess you're right. . ."
                                if EmmaCount == 2:
                                    ch_e "Yeah, I guess so!"
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            elif EmmaCount == 2:                               #Emma only
                                ch_e "You do have a point there, [E_Petname]."
                                if MystiqueCount == 2:
                                    ch_m "Yeah, me too!"
                            
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Yeah, not dark enough, [R_Petname]."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "[K_Like]I can see everything perfect, [K_Petname], so no."
                            if EmmaCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_e "Are you sure you're not blind, [E_Petname]? I can see everything perfectly."        

                                
                    #fix, add jeolousy angle here, if roguelikekitty low, get rid of her. . .
                        
                        
            if RogueCount == 1:     
                    #If Rogue leaves
                    $ Occupants -= 1
                    $ RogueCount = 0
                    call Remove_Girl("Rogue") from _call_Remove_Girl_16
            elif RogueCount == 2:                                    
                    #If Rogue Stays
                    if not R_Water:
                        "Rogue strips naked and goes in the water"
                        call RogueOutfit("nude") from _call_RogueOutfit_15
                    else:
                        call RogueOutfit("nude") from _call_RogueOutfit_16
                    $ R_Water = 1
                    $ R_Spunk = []                    
                    #$ R_RecentActions.append("showered")                      
                    #$ R_DailyActions.append("showered")   
                    
            if KittyCount == 1:     
                    #If Kitty leaves
                    $ Occupants -= 1
                    $ KittyCount = 0
                    call Remove_Girl("Kitty") from _call_Remove_Girl_17
            elif KittyCount == 2: 
                    #If Kitty Stays
                    if not K_Water:
                        "Kitty strips naked and jumps on the water"
                        call KittyOutfit("nude") from _call_KittyOutfit_3
                    else:
                        call KittyOutfit("nude") from _call_KittyOutfit_4
                    $ K_Water = 1
                    $ K_Spunk = []
                    #$ K_RecentActions.append("showered")                      
                    #$ K_DailyActions.append("showered") 

            if EmmaCount == 1:     
                    #If Emma leaves
                    $ Occupants -= 1
                    $ EmmaCount = 0
                    call Remove_Girl("Emma") from _call_Remove_Girl_18
            elif EmmaCount == 2: 
                    #If Emma Stays
                    if not E_Water:
                        "Emma strips naked and jumps on the water"
                        call EmmaOutfit("nude") from _call_EmmaOutfit_6
                    else:
                        call EmmaOutfit("nude") from _call_EmmaOutfit_7
                    $ E_Water = 1
                    $ E_Spunk = []
                    
            call Seen_First_Peen (0,1) from _call_Seen_First_Peen_7 #You get naked
                
            
    $ Line = "You swim naked"
    $ Round -= 30
    $ Trigger = 0
    
    if RogueCount and KittyCount and EmmaCount:
                    $ Line = "You swim around with Rogue, Kitty and Emma."
                    call Change_Focus("Rogue", "Kitty") from _call_Change_Focus 
                    $ R_Water = 1
                    $ K_Water = 1
                    $ E_Water = 1
    elif RogueCount and KittyCount:
                    $ Line = "You swim around with Rogue and Kitty."
                    call Shift_Focus("Rogue", "Kitty") from _call_Shift_Focus_45
                    $ R_Water = 1
                    $ K_Water = 1
    elif KittyCount:
                    $ Line = "You swim around with Kitty."  
                    call Shift_Focus("Kitty") from _call_Shift_Focus_46   
                    $ K_Water = 1
    else:
                $ Line = Line + renpy.random.choice([". It was fairly uneventful.", 
                        ". It's cold.", 
                        ". That was refreshing."])   
                
    #insert random events here
    "[Line]"    
    #$ P_DailyActions.append("showered")
    
    if RogueCount :
        ch_r "That was real nice, [R_Petname]."            
        if KittyCount:
            ch_k "Yeah, I had fun."
        if EmmaCount:
            ch_e "Really nice indeed."
    elif KittyCount:
        ch_k "That was. . . nice." 
        if EmmaCount:
            ch_e "Really nice indeed."
    elif EmmaCount:
        ch_e "That was. . . nice."
            
    #call RogueOutfit
    #call KittyOutfit
    if Round < 1:
        if Current_Time != "Night":
                call Wait from _call_Wait_11
                call Girls_Location from _call_Girls_Location_17
                call Set_The_Scene from _call_Set_The_Scene_34
        else:
                $ renpy.pop_call()
                "After the swim, it's getting late, you head back to your room."
                jump Player_Room
    return
# end Skinny Dipping / 

# end Pool Room Interface //////////////////////////////////////////////////////////////////////

# Football Field Interface //////////////////////////////////////////////////////////////////////
  
label Field_Entry:
    $ bg_current = "bg field"               
    call Taboo_Level from _call_Taboo_Level_10
    $ P_RecentActions.append("traveling")
    call EventCalls from _call_EventCalls_19
    call Set_The_Scene from _call_Set_The_Scene_35
    
label Field:
    $ bg_current = "bg field"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Set_The_Scene from _call_Set_The_Scene_36
    call Taboo_Level from _call_Taboo_Level_11
    call QuickEvents from _call_QuickEvents_5    
    call Checkout(1) from _call_Checkout_29    
    call GirlsAngry from _call_GirlsAngry_5      

# Football Field Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are at the football field. What would you like to do?"
        
        "Chat":
            call Chat from _call_Chat_5
            
        "Watch the match." if Weekday > 3 and Current_Time == "Evening":
            "You watch the match that is going on. It was an entertaining match."
            call Wait from _call_Wait_12
            call EventCalls from _call_EventCalls_20
            call Girls_Location from _call_Girls_Location_18
            
        "Wait." if Current_Time != "Night":
            "You wait around a bit."
            call Wait from _call_Wait_13   
            call EventCalls from _call_EventCalls_21            
            call Girls_Location from _call_Girls_Location_19
            
        "Leave [[Go to Campus Square]":
                if TravelMode:
                    jump Campus_Entry
                else:
                    call Worldmap from _call_Worldmap_7               
    jump Field

# end Football Field Interface //////////////////////////////////////////////////////////////////////

# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Danger_Room_Entry:
    $ bg_current = "bg dangerroom"    
    call Taboo_Level from _call_Taboo_Level_12
    $ P_RecentActions.append("traveling")
    call EventCalls from _call_EventCalls_22
    call Gym_Clothes("pre") from _call_Gym_Clothes_4#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene from _call_Set_The_Scene_37
    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_5
    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_4
    "This is the Danger Room. What would you like to do?" 
    
label Danger_Room:
    $ bg_current = "bg dangerroom"  
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")  
    call Set_The_Scene from _call_Set_The_Scene_38
    call Taboo_Level from _call_Taboo_Level_13    
    call QuickEvents from _call_QuickEvents_6
    call Checkout(1) from _call_Checkout_30
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                        
                call Wait from _call_Wait_14   
                call EventCalls from _call_EventCalls_23
                call Girls_Location from _call_Girls_Location_20 
                call Set_The_Scene from _call_Set_The_Scene_39
                call Gym_Clothes from _call_Gym_Clothes_5                
    call GirlsAngry from _call_GirlsAngry_6  
    #End Room Set-up
    
# Danger Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "This is the Danger Room. What would you like to do?" 
#        extend ""        
        "Train" if Current_Time != "Night":
                if Current_Time == "Night":
                        "The Danger Room has been powered off for the night, maybe take a break."
                if Round >= 30:
                        jump Training
                else:
                        "There really isn't time to do much before the next rotation, maybe wait a bit."
                    
        "Chat":
                call Chat from _call_Chat_6
            
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait from _call_Wait_15   
                call EventCalls from _call_EventCalls_24
                call Gym_Clothes from _call_Gym_Clothes_6
                call Girls_Location from _call_Girls_Location_21 
                call Gym_Clothes from _call_Gym_Clothes_7
               
        "Leave [[Go to Campus Square]":    
                if TravelMode:        
                    call Gym_Clothes("change") from _call_Gym_Clothes_8
                    jump Campus_Entry
                else:
                    call Worldmap from _call_Worldmap_8         
        "Go to the showers" if TravelMode:             
                call Gym_Clothes("change") from _call_Gym_Clothes_9
                jump Shower_Room_Entry         
    jump Danger_Room

label Training:
#    $ D20 = renpy.random.randint(1, 20)
#    if D20 > 10 and R_Inbt >= 500:
#        call Rogue_Frisky_Danger
        
    $ P_XP += (5 + (int(Round / 10)))
    $ P_DailyActions.append("dangerroom")
    call Set_The_Scene from _call_Set_The_Scene_40
    
    if Round >= 80:
            $ Line = "You have a long session in the Danger Room."
    elif Round >= 50:
            $ Line = "You have a short workout in the Danger Room."
    else:
            $ Line = "You squeeze in a quick session in the Danger Room."
        
    $ Trigger = 0
    $ Line = Line + renpy.random.choice([" It was fairly boring.", 
            " You do some training with basic firearms.", 
            " You run the obstacle course.",
            " You fight in a simulated battle against the Brotherhood.",
            " You help take down a holographic Sentinel.",
            " During the exercise, Cyclops accidentally shoots you. Luckily you're immune to the beams, but your clothes weren't so lucky.", #fix this, for length
            " You fight a simulation of Magneto."])      
    "[Line]"    
    if R_Loc == bg_current:
        call Rogue_TightsRipped from _call_Rogue_TightsRipped
    
    call Wait from _call_Wait_16
    call Girls_Location from _call_Girls_Location_22 
    call Set_The_Scene from _call_Set_The_Scene_41
    call Gym_Clothes from _call_Gym_Clothes_10 
    $ Line = "The training session has ended, what would you like to do next?"
    
    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if R_Hose == "tights":
                $ Count = 1
                $ R_Hose = "ripped tights"    
                call RogueFace("angry") from _call_RogueFace_89
                if "ripped tights" in R_Inventory:  
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "Well that's a good pair of tights down the chute."                
        elif R_Hose == "pantyhose":
                $ Count = 1
                $ R_Hose = "ripped pantyhose"              
                call RogueFace("angry") from _call_RogueFace_90
                if "ripped pantyhose" in R_Inventory:  
                    ch_r "Tsk, another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "I hate getting a run in these things."     
        if Count:
                #If they ripped
                if not R_Legs and R_Panties != "shorts":
                        if R_Panties: 
                            if R_SeenPanties:
                                $ Count = 3 if not ApprovalCheck("Rogue", 600) else Count
                            else:
                                $ R_SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck("Rogue", 900) else Count                            
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 2)
                        else:
                            if R_SeenPussy:
                                $ Count = 3 if not ApprovalCheck("Rogue", 900) else Count
                            else:
                                call Rogue_First_Bottomless from _call_Rogue_First_Bottomless_2 
                                $ Count = 3 if not ApprovalCheck("Rogue", 1400) else Count
                            
                if Count == 2: 
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":                
                                call RogueFace("smile", 1) from _call_RogueFace_91                     
                                $ R_Inventory.append(R_Hose) 
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand." 
                            "Yeah, too bad.":             
                                call RogueFace("bemused") from _call_RogueFace_92    
                                ch_r ". . ."         
                            "Ha! Those don't leave much to the imagination!":                        
                                ch_r "Thanks for that. . ."
                                
                elif Count == 3: #She is embarassed and takes off             
                    call RogueFace("startled", 2) from _call_RogueFace_93  
                    ch_r "I, um, I should get out of here."
                    $ R_Blush = 1
                    call Remove_Girl("Rogue") from _call_Remove_Girl_19
                    call RogueOutfit from _call_RogueOutfit_17
                #end "if they ripped"
        return
                
# end Danger Room Interface //////////////////////////////////////////////////////////////////////


# Showers Interface //////////////////////////////////////////////////////////////////////
label Shower_Room_Entry:
    $ bg_current = "bg showerroom"             
    call Gym_Clothes from _call_Gym_Clothes_11  
    call Set_The_Scene(0,1,0) from _call_Set_The_Scene_42
    call Taboo_Level from _call_Taboo_Level_14
    $ D20 = renpy.random.randint(1, 20)
    if Round <= 10: 
        jump Shower_Room
    $ Options.append("nothing")
    if "showered" not in R_DailyActions and (R_Loc == "bg rogue" or R_Loc == "bg dangerroom"):  #Checks if Rogue is in the shower
            $ Options.append("Rogue")   
    if "showered" not in K_DailyActions and (K_Loc == "bg kitty" or K_Loc == "bg dangerroom") and "met" in K_History:  #Checks if Kitty is in the shower
            $ Options.append("Kitty")     
    if "showered" not in E_DailyActions and (E_Loc == "bg emma" or E_Loc == "bg dangerroom") and "met" in E_History:  #Checks if Emma is in the shower
            $ Options.append("Emma")
    
    if len(Options) == 0:
            # if nobody is around, skip it.
            jump Shower_Room
        
    $ renpy.random.shuffle(Options)
    if Options[0] == "Rogue":  
                if D20 > 10:
                    if (D20 >= 18 and R_Lust >= 70) or (D20 >= 15 and R_Lust >= 80):
                        "As you approach the showers, you hear some shallow moans from inside."
                        $ R_Wet = 2
                    else:
                        "As you approach the showers, you hear some humming noises from inside." 
                    $ Options = []         
                    jump Rogue_Caught_Shower
    if Options[0] == "Kitty":  
                if D20 > 10:
                    if (D20 >= 18 and K_Lust >= 70) or (D20 >= 15 and K_Lust >= 80):
                        "As you approach the showers, you hear some shallow moans from inside."
                        $ K_Wet = 2
                    else:
                        "As you approach the showers, you hear some humming noises from inside." 
                    $ Options = []                    
                    jump Kitty_Caught_Shower
    if Options[0] == "Emma":  
                if D20 > 10: 
                    if (D20 >= 18 and E_Lust >= 70) or (D20 >= 15 and E_Lust >= 80):
                        "As you approach the showers, you hear some shallow moans from inside."
                        $ E_Wet = 2
                    else:
                        "As you approach the showers, you hear some humming noises from inside." 
                    $ Options = []                    
                    jump Emma_Caught_Shower
    #End Caught Check
    
    # If none of the caught dialogs plays, checks to see if anyone is in the room, and allows them to be there if they are. 
    if "Rogue" in Options:
            $ R_Loc = bg_current  
    if "Kitty" in Options:
            $ K_Loc = bg_current  
    if "Emma" in Options:
            $ E_Loc = bg_current  
    call Present_Check from _call_Present_Check_3
    
    $ Count = 0
    $ Count2 = 0
    if R_Loc == bg_current and "Rogue" not in Party:
            $ Count = "Rogue"
            if D20 >= 5:
                    $ R_RecentActions.append("showered")                      
                    $ R_DailyActions.append("showered")   
    if K_Loc == bg_current and "Kitty" not in Party:
            if Count:
                $ Count2 = "Kitty"
            else:            
                $ Count = "Kitty"
            if D20 >= 5:
                    $ K_RecentActions.append("showered")                      
                    $ K_DailyActions.append("showered")   
    if E_Loc == bg_current and "Emma" not in Party:
            if Count:
                $ Count2 = "Emma"
            else:            
                $ Count = "Emma"
            if D20 >= 5:
                    $ E_RecentActions.append("showered")                      
                    $ E_DailyActions.append("showered")   
    #End Count set-up
    
    call Set_The_Scene from _call_Set_The_Scene_43
    if Count2:
        "As you enter, you see [Count] and [Count2] standing there."
    elif Count:
        "As you enter, you see [Count] standing there."
    
    if Count:
            if R_Loc == bg_current and "Rogue" not in Party:
                    ch_r "Hey, [R_Petname]."
                    if "showered" in R_RecentActions:
                        ch_r "I was just getting ready to head out."
            if K_Loc == bg_current and "Kitty" not in Party:
                    if Count2 == "Kitty":
                        ch_k "Yeah, hi."
                    else:            
                        ch_k "Hey, [K_Petname]."
                        if "showered" in K_RecentActions:
                            ch_k "I just got finished."
            if E_Loc == bg_current and "Emma" not in Party:
                    if Count2 == "Emma":
                        ch_e "Yes, nice to see you."
                    else:      
                        ch_e "Oh, hello, [E_Petname]." 
                        if "showered" in E_RecentActions:
                            ch_e "I was about finished here." 
            # End welcomes
            if "Rogue" in Party:
                    ch_r "Hey, [Count]."
            if "Kitty" in Party:
                    ch_k "Hi, [Count]."
            if "Emma" in Party:
                    ch_e "Oh, hello, [Count]."
                    
    # End Reply portion
    
    $ Count = 0
    $ Count2 = 0
    $ Options = []
            
    
# Shower Room Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Shower_Room:
    $ bg_current = "bg showerroom"    
    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_44
    call Taboo_Level from _call_Taboo_Level_15
    call QuickEvents from _call_QuickEvents_7
    call Checkout(1) from _call_Checkout_31
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                    
                call Wait from _call_Wait_17   
                call EventCalls from _call_EventCalls_25
                call Girls_Location from _call_Girls_Location_23 
                call Set_The_Scene from _call_Set_The_Scene_45
    call GirlsAngry from _call_GirlsAngry_7      
    #End Room Set-up

# Shower Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You're in the showers. What would you like to do?"

        "Chat":
                call Chat from _call_Chat_7
            
        "Shower" if Round > 30:
                call Showering from _call_Showering
        "Shower (locked)" if Round <= 30:            
                pass
            
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                "In the showers."
                "Not gonna lie, kinda weird."
                call Wait from _call_Wait_18   
                call EventCalls from _call_EventCalls_26            
                call Girls_Location from _call_Girls_Location_24
                call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_6 
                call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_5 
         
        "Go to the Danger Room" if TravelMode: 
                jump Danger_Room_Entry 
        "Return to Your Room" if TravelMode:  
                jump Player_Room_Entry   
        "Girl's Rooms" if TravelMode:
            menu:
                "Rogue's Room":   
                            jump Rogue_Room_Entry 
                "Kitty's Room" if "met" in K_History:   
                            jump Kitty_Room_Entry   
                "Emma's Room" if "met" in E_History:   
                            jump Emma_Room_Entry  
                "Mystique's Room" if "metgym" in newgirl["Mystique"].History:
                            jump Mystique_Room_Entry        
                "Back":
                            pass 
        "Leave [[Go to Campus Square]":
                if TravelMode:
                    jump Campus_Entry
                else:
                    call Worldmap from _call_Worldmap_9   
    jump Shower_Room

# Shower Room Menu End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Showering(Occupants = 0, Agreed = 0, RogueCount = 0, KittyCount = 0, EmmaCount = 0, Showered = 0, Line = 0):
    if R_Loc == "bg showerroom":
            $ Occupants += 1
            $ RogueCount = 1
    if K_Loc == "bg showerroom":        
            $ Occupants += 1
            $ KittyCount = 1
    if E_Loc == "bg showerroom":        
            $ Occupants += 1
            $ EmmaCount = 1
        
    if Occupants:
            ch_p "I'm taking a shower, care to join me?" 
            if RogueCount and "showered" in R_RecentActions:
                if Occupants >1:
                    ch_r "We actually just finished up, so we'll head out."
                else:
                    ch_r "I actually just finished up, so I'll head out."
                $ Showered = 1
            elif KittyCount and "showered" in K_RecentActions:
                ch_k "I actually just showered, so I'll head out."
                $ Showered = 1
            elif EmmaCount and "showered" in E_RecentActions:
                ch_e "I just finished, [E_Petname]. Maybe some other time."
                $ Showered = 1
            else:
                if RogueCount:
                    if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                        ch_r "I suppose I could stick around. . ."
                        $ RogueCount = 2
                        $ Agreed += 1
                    else:
                        ch_r "Nah, I should probably get going."
                if KittyCount:
                    if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                        if RogueCount > 1:                          #If Rogue said yes
                            ch_k "I guess I could stay too. . ."
                        elif Occupants > 1:                     #If Rogue said no
                            ch_k "Well, I could stay though."
                        else:                                   #If Rogue isn't there
                            ch_k "Yeah, I could stick around."
                        $ KittyCount = 2
                        $ Agreed += 1
                    else:
                        if RogueCount > 1:                          #If Rogue said yes
                            ch_k "I've really got to go though. . ."
                        elif Occupants > 1:                     #If Rogue/Emma said no
                            ch_k "Yeah, I should head out too."
                        else:                                   #If Rogue/Emma isn't there
                            ch_k "I've got to get going."
                if EmmaCount:
                    if ApprovalCheck("Emma", 1200) or (ApprovalCheck("Emma", 600) and E_SeenChest and E_SeenPussy):
                        if RogueCount > 1 or KittyCount > 1:                          #If Rogue said yes
                            ch_e "I like where this is going."
                        #if KittyCount > 1:                          #If Kitty said yes
                        #    ch_e "I like where this is going."
                        elif Occupants > 1:                     #If Rogue/Kitty said no
                            ch_e "Don't worry, [E_Petname], we can still have some fun."
                        else:                                   #If Rogue/Kitty isn't there
                            ch_e "Sure, but let's hurry before someone sees us."
                        $ EmmaCount = 2
                        $ Agreed += 1
                    else:
                        if RogueCount > 1 or KittyCount > 1:                          #If Rogue said yes
                            ch_e "I think it's best if I leave."
                        #if KittyCount > 1:                          #If Kitty said yes
                        #    ch_e "I think it's best if I leave."
                        elif Occupants > 1:                     #If Rogue/Kitty said no
                            ch_e "I better get going too. See you in class, [E_Petname]."
                        else:                                   #If Rogue/Kitty isn't there
                            ch_e "The shower is all yours, [E_Petname]."
                            
            if Occupants > Agreed:                    #if either said no     
                # If they're at NameCount = 2 here, they have already agreed.
                
                menu:
                    extend ""
                    "Ok, see you later then.":
                        if RogueCount == 1:
                            ch_r "Yeah, later."
                        if KittyCount == 1:
                            ch_k "Bye!"
                        if EmmaCount == 1:
                            ch_k "Bye, [E_Petname]."
                        
                    "Sure you got every spot?" if Showered:
                        $ Line = "spot"
                                                        
                    #fix Add "Take off your own clothes" option.
                    
                    "Maybe you could stay and watch?":
                        $ Line = "watch me"
                        
                    "But I didn't get to watch." if Showered:
                        $ Line = "watch you"
                        
                if Line:
                    if RogueCount == 1: 
                        if ApprovalCheck("Rogue", 1200) or (ApprovalCheck("Rogue", 600) and R_SeenChest and R_SeenPussy):
                            $ RogueCount = 2
                        elif Line == "spot" and ApprovalCheck("Rogue", 1000, "LI"):                                
                            $ RogueCount = 2
                        elif Line == "watch you" and ApprovalCheck("Rogue", 600, "O"):                                
                            $ RogueCount = 2
                        #else, she doesn't agree
                            
                    if KittyCount == 1:
                        if ApprovalCheck("Kitty", 1400) or (ApprovalCheck("Kitty", 700) and K_SeenChest and K_SeenPussy):
                            ch_k "yes"
                            $ KittyCount = 2
                        elif Line == "spot" and ApprovalCheck("Kitty", 1200, "LI"):                                
                            $ KittyCount = 2
                        elif Line == "watch you" and ApprovalCheck("Kitty", 600, "O"):                                
                            $ KittyCount = 2
                        #else, she doesn't agree
                        
                    if EmmaCount == 1:
                        if ApprovalCheck("Emma", 1400) or (ApprovalCheck("Emma", 700) and E_SeenChest and E_SeenPussy):
                            ch_e "Yup!"
                            $ EmmaCount = 2
                        elif Line == "spot" and ApprovalCheck("Emma", 1200, "LI"):                                
                            $ EmmaCount = 2
                        elif Line == "watch you" and ApprovalCheck("Emma", 600, "O"):                                
                            $ EmmaCount = 2
                        #else, she doesn't agree
                    
                    
                    if Line == "spot":      #"Sure you got every spot?"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Fine, I could use another scrub."
                                if KittyCount == 2:
                                    ch_k "Um, me too!"
                                if EmmaCount == 2:
                                    ch_e "I think I'll stay too."
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "Oh, I guess I could take another pass at it."
                            elif EmmaCount == 2:                                #Emma only
                                ch_e "Oh alright then!"
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "No, [R_Petname], I think I'm covered."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "Ha, I'm squeeky clean, [K_Petname], see you later."
                            if EmmaCount == 1:                                   #Kitty/Rogue agreed, Emma refused
                                ch_e "Not this time, [R_Petname]."
                        
                    elif Line == "watch me":  #"Maybe you could stay and watch?"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Yeah, I guess I do enjoy the view."
                                if KittyCount == 2:
                                    ch_k "Um, me too!"
                                if EmmaCount == 2:
                                    ch_e "This could be fun."
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "I. . . guess I wouldn't mind that. . ."
                            elif EmmaCount == 2:                                #Emma only
                                ch_e "Let's hope no one sees us."
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Yeah, I'm gonna pass on that, [R_Petname]."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "[K_Like]I don't need to see that."
                            if EmmaCount == 1:                                   #Rogue/Kitty agreed, Emma refused
                                ch_e "I should be going."
                        
                    elif Line == "watch you": #"But I didn't get to watch."
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Well, I don't mind putting on a show."
                                if KittyCount == 2:
                                    ch_k "I- yeah, me neither!"
                                if EmmaCount == 2:
                                    ch_e "Here, let me help you."
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "You want to watch me. . ."
                                ch_k "Ok."
                            elif EmmaCount == 2:                                #Emma only
                                ch_e "Sure, why not."
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Keep dreaming, [R_Petname]."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "[K_Like]no way!"
                            if EmmaCount == 1:                                   #Rogue/Kitty agreed, Emma refused
                                ch_e "You'd better leave, [E_Petname]."
                                
                    #fix, add jeolousy angle here, if roguelikekitty low, get rid of her. . .
                        
                        
            if RogueCount == 1:     
                    #If Rogue leaves
                    $ Occupants -= 1
                    $ RogueCount = 0
                    call Remove_Girl("Rogue") from _call_Remove_Girl_20
            elif RogueCount == 2:                                    
                    #If Rogue Stays
                    call RogueOutfit("nude") from _call_RogueOutfit_18
                    $ R_Water = 1
                    $ R_Spunk = []                    
                    $ R_RecentActions.append("showered")                      
                    $ R_DailyActions.append("showered")   
                    
            if KittyCount == 1:     
                    #If Kitty leaves
                    $ Occupants -= 1
                    $ KittyCount = 0
                    call Remove_Girl("Kitty") from _call_Remove_Girl_21
            elif KittyCount == 2: 
                    #If Kitty Stays
                    call KittyOutfit("nude") from _call_KittyOutfit_5
                    $ K_Water = 1
                    $ K_Spunk = []
                    $ K_RecentActions.append("showered")                      
                    $ K_DailyActions.append("showered")

            if EmmaCount == 1:     
                    #If Emma leaves
                    $ Occupants -= 1
                    $ EmmaCount = 0
                    call Remove_Girl("Emma") from _call_Remove_Girl_22
            elif EmmaCount == 2: 
                    #If Emma Stays
                    call EmmaOutfit("nude") from _call_EmmaOutfit_8
                    $ E_Water = 1
                    $ E_Spunk = []
                    $ E_RecentActions.append("showered")                      
                    $ E_DailyActions.append("showered")
                    
            call Seen_First_Peen (0,1) from _call_Seen_First_Peen_8 #You get naked
                
            
    $ Line = "You take a quick shower"
    $ Round -= 30
    $ Trigger = 0
    
    if RogueCount and KittyCount and EmmaCount:
                    $ Line = "You take a quick shower with Rogue, Kitty and Emma."
                    call Shift_Focus("Rogue", "Kitty") from _call_Shift_Focus_47
    if RogueCount and KittyCount:
                    $ Line = "You take a quick shower with Rogue and Kitty."
                    call Shift_Focus("Rogue", "Kitty") from _call_Shift_Focus_48
    if EmmaCount and RogueCount:
                    $ Line = "You take a quick shower with Emma and Rogue."
                    call Shift_Focus("Emma", "Rogue") from _call_Shift_Focus_49
    if EmmaCount and KittyCount:
                    $ Line = "You take a quick shower with Emma and Kitty."
                    call Shift_Focus("Emma", "Kitty") from _call_Shift_Focus_50
    elif RogueCount:
                    $ Line = "You take a quick shower with Rogue."
                    call Shift_Focus("Rogue") from _call_Shift_Focus_51 
    elif KittyCount:
                    $ Line = "You take a quick shower with Kitty."  
                    call Shift_Focus("Kitty") from _call_Shift_Focus_52
    elif EmmaCount:
                    $ Line = "You take a quick shower with Emma."  
                    call Shift_Focus("Emma") from _call_Shift_Focus_53
    else:
                $ Line = Line + renpy.random.choice([". It was fairly uneventful.", 
                        ". A few people came and went as you did so.", 
                        ". That was refreshing."])   
                
    #insert random events here
    "[Line]"    
    $ P_DailyActions.append("showered")
    
    if RogueCount :
        ch_r "That was real nice, [R_Petname]."            
        if KittyCount:
            ch_k "Yeah, I had fun."
        if EmmaCount:
            ch_e "We should do this again."
    elif KittyCount:
        ch_k "that was. . . nice."
        if EmmaCount:
            ch_e "We should do this again."
    elif EmmaCount:
            ch_e "I enjoyed that, [E_Petname]"
            
    call RogueOutfit from _call_RogueOutfit_19
    call KittyOutfit from _call_KittyOutfit_6
    call EmmaOutfit from _call_EmmaOutfit_9
    if Round < 1:
        if Current_Time != "Night":
                call Wait from _call_Wait_19
                call Girls_Location from _call_Girls_Location_25
                call Set_The_Scene from _call_Set_The_Scene_46
        else:
                $ renpy.pop_call()
                "After the shower, it's getting late, you head back to your room."
                jump Player_Room
    return
# End Showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




label Rogue_Caught_Shower:  
    call Shift_Focus("Rogue") from _call_Shift_Focus_54     
    $ R_RecentActions.append("showered")                      
    $ R_DailyActions.append("showered")     
    call Remove_Girl("All") from _call_Remove_Girl_23
    $ R_Loc = "bg showerroom"
    call RogueOutfit("nude") from _call_RogueOutfit_20
    $ R_Blush = 2
    $ R_Water = 1
    $ R_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ R_Loc = "bg rogue"
                call RogueOutfit from _call_RogueOutfit_21
                $ R_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ R_Over = "towel"       
            if (D20 >=18 and R_Lust >= 70) or (D20 >=15 and R_Lust >= 80):                                          
                    #Rogue caught fapping
                    "You hear a startled gasp, followed by some shuffling around as a brush hits the floor."
                    "After several seconds and some more shuffling, Rogue comes to the door."
                    $ R_Brows = "confused"
                    $ R_Eyes = "surprised"
                    $ R_Mouth = "smile"
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_47
                    ch_r "Sorry about that [R_Petname], I was. . . just wrapping up my shower."
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Rogue caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Rogue comes to the door."
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_48
                    ch_r "Sorry about that [R_Petname], I was just wrapping up my shower."
            #end "knocked"
    else:                                                                                                       
        #You don't knock    
        $ Line = 0    
        if (D20 >=18 and R_Lust >= 70) or (D20 >=15 and R_Lust >= 80):                                         
                #Caught masturbating in the shower. 
                call RogueFace("sexy") from _call_RogueFace_94
                $ R_Eyes = "closed"
                $ Rogue_Arms = 2
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_49
                $ Count = 0        
                "You see Rogue under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ R_DailyActions.append("unseen") if "unseen" not in R_DailyActions else R_DailyActions   
                $ R_RecentActions.append("unseen") if "unseen" not in R_RecentActions else R_RecentActions 
                call Rogue_SexAct("masturbate") from _call_Rogue_SexAct_4   
                jump Shower_Room
            
        elif D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_50                
                call RogueFace("surprised", 1) from _call_RogueFace_95
                "As you enter the showers, you see Rogue washing up."        
                if not ApprovalCheck("Rogue", 1200) or not R_SeenPussy or not R_SeenChest:
                        $ R_Brows = "angry"     
                        $ R_Over = "towel"
                        "She grabs a towel and covers up."             
                        call RogueFace("angry", 1) from _call_RogueFace_96
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5) 
                else:
                        if "exhibitionist" in R_Traits:
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, (2*D20)) 
                        else:
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, D20)
                        $ R_Brows = "confused"        
                
                call Rogue_First_Topless(1) from _call_Rogue_First_Topless_2
                call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_3 
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 3)
                menu:
                        ch_r "Hey! Learn to knock maybe?!"
                        "Sorry, I should have knocked.":  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 4)
                        "And miss the view?":
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ R_Over = "towel"
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_51
                "As you enter the showers, you see Rogue putting on a towel."        
                if not ApprovalCheck("Rogue", 1100) and (not R_SeenPussy or not R_SeenChest):          
                        call RogueFace("angry") from _call_RogueFace_97
                        $R_Brows = "confused"
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                else:
                        call RogueFace("sexy") from _call_RogueFace_98
                        $R_Brows = "confused"        
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                menu:
                        ch_r "Well hello there, [R_Petname]. Hoping to see something more?"
                        "Sorry, I should have knocked.":   
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 2)
                        "Well, to be honest. . .":                
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 2)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 1)
                #end caught in towel
                    
        call RogueFace("sexy") from _call_RogueFace_99          
        if not ApprovalCheck("Rogue", 750) and (R_SeenPussy < 3 or R_SeenChest < 3): 
                ch_r "Well, it happens, just be careful next time."
        elif not ApprovalCheck("Rogue", 1300): 
                ch_r "Well, it happens, just be careful next time."
        else:                
                ch_r "You could have just asked, [R_Petname]."      
                if R_Over == "towel": 
                    $ R_Over = 0
                    pause 0.5                      
                    $ R_Over = "towel"  
                    "She flashes you real quick."                        
                    $ R_Over = "towel" 
                call Rogue_First_Topless(1) from _call_Rogue_First_Topless_3
                call Rogue_First_Bottomless(1) from _call_Rogue_First_Bottomless_4 
        #end didn't knock
    
    menu:
        ch_r "Well, I should probably get going. . ." 
        "Sure, see you later then.":
                call Remove_Girl("Rogue") from _call_Remove_Girl_24
                $ R_Water = 0
                call RogueOutfit from _call_RogueOutfit_22
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Rogue", 900):
                $ R_Loc = "bg showerroom"            
                ch_r "Sure, what's up?"
            else:
                ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                ch_r "I'll just see you around later."
                call Remove_Girl("Rogue") from _call_Remove_Girl_25
                $ R_Water = 0
                call RogueOutfit from _call_RogueOutfit_23               
            
    jump Shower_Room
# End Rogue Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Caught_Shower:  
    call Shift_Focus("Kitty") from _call_Shift_Focus_55     
    $ K_RecentActions.append("showered")                      
    $ K_DailyActions.append("showered")     
    call Remove_Girl("All") from _call_Remove_Girl_26
    $ K_Loc = "bg showerroom"
    call KittyOutfit("nude") from _call_KittyOutfit_7
    $ K_Blush = 2
    $ K_Water = 1
    $ K_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ K_Loc = "bg kitty"
                call KittyOutfit from _call_KittyOutfit_8
                $ K_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ K_Over = "towel"       
            if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and K_Lust >= 80):                                          
                    #Kitty caught fapping
                    "You hear a startled gasp, followed by some shuffling around as a shampoo bottle hits the floor."
                    "After several seconds and some more shuffling, Kitty comes to the door."
                    $ K_Brows = "confused"
                    $ K_Eyes = "surprised"
                    $ K_Mouth = "smile"
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_52
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Kitty caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Kitty comes to the door."
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_53
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
            #end knocked
            
    else:                                                                                                       
        #You don't knock   
        if not K_SeenPussy or not K_SeenChest:
            $ D20 -=5 if D20 > 5 else D20
        $ Line = 0    
        if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and K_Lust >= 80):                                          
                #Caught masturbating in the shower. 
                call KittyFace("sexy") from _call_KittyFace_2
                $ K_Eyes = "closed"
                $ Kitty_Arms = 2
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_54
                $ Count = 0        
                "You see Kitty under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ K_DailyActions.append("unseen") if "unseen" not in K_DailyActions else K_DailyActions   
                $ K_RecentActions.append("unseen") if "unseen" not in K_RecentActions else K_RecentActions 
                call Kitty_SexAct("masturbate") from _call_Kitty_SexAct   
                jump Shower_Room
        
        #change to elif when I fix the above option
        if D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_55                
                call KittyFace("surprised", 1) from _call_KittyFace_3
                "As you enter the showers, you see Kitty washing up."        
                if not ApprovalCheck("Kitty", 1200) or not K_SeenPussy or not K_SeenChest:
                        $ K_Brows = "angry"     
                        $ K_Over = "towel"
                        "She grabs a towel and covers up."             
                        call KittyFace("angry", 1) from _call_KittyFace_4
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5) 
                else:
                        if "exhibitionist" in K_Traits:
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, (2*D20)) 
                        else:
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, D20)
                        $ K_Brows = "confused"        
                
                call Kitty_First_Topless(1) from _call_Kitty_First_Topless
                call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless 
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 3)
                menu:
                    ch_k "Did you[K_like]get a good look?"
                    "Sorry, I should have knocked.":  
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 4)
                    "Definitely.":
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ K_Over = "towel"
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_56
                "As you enter the showers, you see Kitty putting on a towel."        
                if not ApprovalCheck("Kitty", 1100) and (not K_SeenPussy or not K_SeenChest):          
                        call KittyFace("angry") from _call_KittyFace_5
                        $K_Brows = "confused"
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                else:
                        call KittyFace("sexy") from _call_KittyFace_6
                        $K_Brows = "confused"        
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                menu:
                    ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    "Sorry, I should have knocked.":   
                            call KittyFace("smile",1) from _call_KittyFace_7
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                            if ApprovalCheck("Kitty", 850) and K_SeenPussy and K_SeenChest: 
                                ch_k "Well, it's not like I totally mind. . ."  
                            else:
                                ch_k "Yeah, appreciated."
                    "Now that you mention it. . .":                
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 1)
                            
                            call KittyFace("sexy") from _call_KittyFace_8       
                            if not ApprovalCheck("Kitty", 850) and (K_SeenPussy < 3 or K_SeenChest < 3): 
                                    ch_k "Well too bad." 
                            elif not ApprovalCheck("Kitty", 1400): 
                                    ch_k "Well too bad." 
                            else:
                                ch_k "Well, it's not like it's totally off the table. . ."      
                                if K_Over == "towel": 
                                    $ K_Over = 0
                                    pause 0.5                      
                                    $ K_Over = "towel"  
                                    "She flashes you real quick."                        
                                    $ K_Over = "towel"   
                                call Kitty_First_Topless(1) from _call_Kitty_First_Topless_1
                                call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_1 
                #end done showering naked
    
    menu:
        ch_k "I'm done here, see you later?" 
        "Sure, see you later then.":
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty") from _call_Remove_Girl_27
                $ K_Water = 0
                call KittyOutfit from _call_KittyOutfit_9
                "Kitty heads out."
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Kitty", 900):
                call KittyFace("sexy",1) from _call_KittyFace_9
                $ K_Loc = "bg showerroom"            
                ch_k "Yeah?"
            else: 
                call KittyFace("perplexed",1) from _call_KittyFace_10
                ch_k "I'm[K_like]totally exposed here?"
                ch_k "I'm just going to head out."
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty") from _call_Remove_Girl_28
                $ K_Water = 0
                call KittyOutfit from _call_KittyOutfit_10               
            
    jump Shower_Room
# End Kitty Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_Caught_Shower:  
    call Shift_Focus("Emma") from _call_Shift_Focus_56     
    $ E_RecentActions.append("showered")                      
    $ E_DailyActions.append("showered")     
    call Remove_Girl("All") from _call_Remove_Girl_29
    $ E_Loc = "bg showerroom"
    call EmmaOutfit("nude") from _call_EmmaOutfit_10
    $ E_Blush = 2
    $ E_Water = 1
    $ E_Spunk = []
    menu:
            "What do you do?"
            "Enter":     
                $ Line = "enter"                
            "Knock":
                $ Line = "knock"
            "Come back later":
                $ E_Loc = "bg emma"
                call EmmaOutfit from _call_EmmaOutfit_11
                $ E_Water = 0
                jump Campus_Map
            
    if Line == "knock":                                                                                         
            #You knock
            $ Line = 0
            "You knock on the door. You hear some shuffling inside"        
            $ E_Over = "towel"       
            if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and E_Lust >= 80):                                          
                    #Emma caught fapping
                    "You hear a startled gasp, followed by some shuffling around as a shampoo bottle hits the floor."
                    "After several seconds and some more shuffling, Emma comes to the door."
                    $ E_Brows = "confused"
                    $ E_Eyes = "surprised"
                    $ E_Mouth = "smile"
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_57
                    ch_e "Oh, it's just you, [E_Petname]. I was just finishing up."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Emma caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Emma comes to the door."
                    call Set_The_Scene(Dress=0) from _call_Set_The_Scene_58
                    ch_k "Oh, it's just you, [E_Petname]. I was just finishing up."
            #end knocked
            
    else:                                                                                                       
        #You don't knock   
        if not E_SeenPussy or not E_SeenChest:
            $ D20 -=5 if D20 > 5 else D20
        $ Line = 0    
        if (D20 >=18 and E_Lust >= 70) or (D20 >=15 and E_Lust >= 80):                                          
                #Caught masturbating in the shower. 
                call EmmaFace("sexy") from _call_EmmaFace_228
                $ E_Eyes = "closed"
                $ Emma_Arms = 2
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_59
                $ Count = 0        
                "You see Emma under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ E_DailyActions.append("unseen") if "unseen" not in E_DailyActions else E_DailyActions   
                $ E_RecentActions.append("unseen") if "unseen" not in E_RecentActions else E_RecentActions 
                call Emma_SexAct("masturbate") from _call_Emma_SexAct_4   
                jump Shower_Room
        
        #change to elif when I fix the above option
        if D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_60                
                call EmmaFace("surprised", 1) from _call_EmmaFace_229
                "As you enter the showers, you see Emma washing up."        
                if not ApprovalCheck("Emma", 1200) or not E_SeenPussy or not E_SeenChest:
                        $ E_Brows = "angry"     
                        $ E_Over = "towel"
                        "She grabs a towel and covers up."             
                        call EmmaFace("angry", 1) from _call_EmmaFace_230
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -5) 
                else:
                        if "exhibitionist" in E_Traits:
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, (2*D20)) 
                        else:
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, D20)
                        $ E_Brows = "confused"        
                
                call Emma_First_Topless(1) from _call_Emma_First_Topless
                call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless 
                $ K_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 3)
                menu:
                    ch_e "[E_Petname]! Maybe I should have locked the door.."
                    "Sorry, I should have knocked.":  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 4)
                    "Definitely.":
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                #end caught showering naked
            
        else:                                                                                   
                #She's done showering and in a towel
                $ E_Over = "towel"
                call Set_The_Scene(Dress=0) from _call_Set_The_Scene_61
                "As you enter the showers, you see Emma putting on a towel."        
                if not ApprovalCheck("Emma", 1100) and (not E_SeenPussy or not E_SeenChest):          
                        call EmmaFace("angry") from _call_EmmaFace_231
                        $E_Brows = "confused"
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -5)
                else:
                        call EmmaFace("sexy") from _call_EmmaFace_232
                        $E_Brows = "confused"        
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                menu:
                    ch_e "[E_Petname], I had a feeling we would end up meeting here."
                    "Sorry, I should have knocked.":   
                            call EmmaFace("smile",1) from _call_EmmaFace_233
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                            if ApprovalCheck("Emma", 850) and E_SeenPussy and E_SeenChest: 
                                ch_e "Why don't you come in?"  
                            else:
                                ch_e "Make sure you do so next time."
                    "Let's have some fun.":                
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                            
                            call EmmaFace("sexy") from _call_EmmaFace_234       
                            if not ApprovalCheck("Emma", 850) and (E_SeenPussy < 3 or E_SeenChest < 3): 
                                    ch_e "Another time, [E_Petname], someone might see us." 
                            elif not ApprovalCheck("Kitty", 1400): 
                                    ch_e "Another time, [E_Petname], someone might see us." 
                            else:
                                ch_e "Is this was you were hoping to see?"      
                                if E_Over == "towel": 
                                    $ E_Over = 0
                                    pause 0.5                      
                                    $ E_Over = "towel"  
                                    "She flashes you real quick."                        
                                    $ E_Over = "towel"   
                                call Emma_First_Topless(1) from _call_Emma_First_Topless_1
                                call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_1 
                #end done showering naked
    
    menu:
        ch_e "I'm heading up. See you later, [E_Petname]" 
        "Sure, see you later then.":
                hide Emma_Sprite with easeoutright
                call Remove_Girl("Emma") from _call_Remove_Girl_30
                $ E_Water = 0
                call EmmaOutfit from _call_EmmaOutfit_12
                "Emma heads out."
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Emma", 900):
                call EmmaFace("sexy",1) from _call_EmmaFace_235
                $ E_Loc = "bg showerroom"            
                ch_e "I thought you'd never ask."
            else: 
                call EmmaFace("perplexed",1) from _call_EmmaFace_236
                ch_e "You shouldn't be seeing me like this, [E_Petname]!"
                ch_e "I'm just going to leave. Please don't mention this to anyone."
                hide Emma_Sprite with easeoutright
                call Remove_Girl("Emma") from _call_Remove_Girl_31
                $ E_Water = 0
                call EmmaOutfit from _call_EmmaOutfit_13               
            
    jump Shower_Room
# End Emma Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /        

# end Shower Interface //////////////////////////////////////////////////////////////////////


# Kitty's Room Interface //////////////////////////////////////////////////////////////////////
label Kitty_Room_Entry:
    call Shift_Focus("Kitty") from _call_Shift_Focus_57
    $ bg_current = "bg kitty"           
    call Gym_Clothes from _call_Gym_Clothes_12
    call Set_The_Scene(Entry = 1) from _call_Set_The_Scene_62    
    call Taboo_Level from _call_Taboo_Level_16
    $ D20 = renpy.random.randint(1, 20)
    
    if "Kitty" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI"):     #It's late but she really likes you
                                ch_k "It's kinda late, [K_Petname], but you can have a minute."    
                        elif K_Addict >= 50:
                                ch_k "I'd really like to see you. . ."            
                        elif ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI"):      #she likes you well enough but it's late
                                ch_k "It's a little late [K_Petname]. Tmorrow?"
                                $ K_RecentActions.append("noentry")                      
                                $ K_DailyActions.append("noentry")  
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Kitty is in the party and it's not late in the day        
                                ch_k "Come on in!"
                    call EventCalls from _call_EventCalls_27
                    jump Kitty_Room   
    #End if Kitty in Party
    
                    
    if Round >= 10 and K_Loc == "bg kitty" and (D20 >=15 and K_Lust >= 70): #Kitty caught fapping      
                "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
                menu:
                    extend ""
                    "Knock politely":
                        $ Line = "knock"
                    "Peek inside":
                        call Set_The_Scene from _call_Set_The_Scene_63
                        "You see Kitty, eyes closed and stroking herself vigorously."
                        menu:
                            extend ""
                            "Enter Quietly":
                                    call Kitty_Caught_Masturbating from _call_Kitty_Caught_Masturbating
                            "Pull back and knock":                        
                                    $ Line = "knock"
                            "Leave quietly":
                                    "You leave Kitty to her business and slip out."
                                    $ K_Lust = 20
                                    jump Campus_Map
                    "Enter quietly":
                            call Kitty_Caught_Masturbating from _call_Kitty_Caught_Masturbating_1
                    "Leave quietly":
                            "You leave Kitty to her business and slip out."
                            $ K_Lust = 20
                            jump Campus_Map
                if Line == "knock":
                        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                        "After several seconds and some more shuffling of clothing, Kitty comes to the door."
                        $ K_Brows = "confused"
                        $ K_Eyes = "surprised"
                        $ K_Mouth = "smile"
                        $ K_Blush = 1
                        call Set_The_Scene from _call_Set_The_Scene_64
                        ch_k "Oh, hey, [K_Petname], I was. . . never mind."
                        $ Tempmod += 10
    # End Kitty caught Fapping
    
    else: #not auto-caught fapping
            if "Kitty" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg kitty"
                            call Set_The_Scene from _call_Set_The_Scene_65
                        
            if Line != "knock" and "Kitty" in Keys: 
                if K_Loc == "bg kitty":
                        if Round <= 10:        
                                if K_RecentActions in ("noentry", "angry"):
                                        call KittyFace("angry") from _call_KittyFace_11
                                        ch_k "GTFO."    
                                        "Kitty shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):     
                                #Kitty caught fapping
                                call Kitty_Caught_Masturbating from _call_Kitty_Caught_Masturbating_2 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
                                #Kitty caught changing
                                call Kitty_Caught_Changing from _call_Kitty_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Kitty's door."        
                        if K_Loc != "bg kitty":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):    
                                #Kitty caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Kitty comes to the door."
                                $ K_Brows = "confused"
                                $ K_Eyes = "surprised"
                                $ K_Mouth = "smile"
                                $ K_Blush = 1
                                call Set_The_Scene from _call_Set_The_Scene_66
                                ch_k "Oh, hey, [K_Petname], I was. . . never mind."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Kitty caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Kitty comes to the door."
                                call Set_The_Scene from _call_Set_The_Scene_67
                                ch_k "Oh, hi [K_Petname], I was[K_like]just getting changed."   
                        elif "angry" in K_RecentActions:
                                ch_k "Nooope."
                                "Kitty pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene from _call_Set_The_Scene_68
                                "Kitty opens it a bit and pops out and you ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if K_Loc != "bg kitty":
                    "Looks like she's not home right now."                
                    if "Kitty" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Kitty_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif K_RecentActions in ("noentry", "angry"):
                    call KittyFace("angry") from _call_KittyFace_12
                    ch_k "What part of \"GTFO\" was unclear?"  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in K_RecentActions:
                    ch_k "Scram. I'll see you tomorrow"  
                    jump Campus_Map 
                    
            elif "noentry" in K_RecentActions:
                    call KittyFace("angry") from _call_KittyFace_13
                    ch_k "GTFO."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
                    $ K_RecentActions.append("angry")                      
                    $ K_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (K_Sleep or K_SEXP >= 30):                                                   
                    #It's late but she really likes you
                    ch_k "It's late, [K_Petname], but you're so cute."                   
            elif Current_Time == "Night" and (ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI")):     
                    #It's late but she really likes you
                    ch_k "It's late, [K_Petname], but I could hang out a bit."                  
            elif K_Addict >= 50:
                    ch_k "I could use some attention. . ."
                    
            elif Current_Time == "Night" and (ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI")):     
                    #she likes you well enough but it's late
                    ch_k "It's late [K_Petname]. Tomorrow?"
                    $ K_RecentActions.append("noentry")                      
                    $ K_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Kitty", 600, "LI") or ApprovalCheck("Kitty", 300, "OI"):                                    
                    #She quite likes you and lets you in   
                    ch_k "Sure, come on in [K_Petname]."        
            else:                                                                                                          
                    #She doesn't like you      
                    ch_k "Nah, you can stay out."
                    $ K_RecentActions.append("noentry")                      
                    $ K_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg kitty"         
    call EventCalls from _call_EventCalls_28
    if K_Loc == "bg kitty" and "angry" in K_RecentActions:
        "Kitty pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg kitty":
        jump Misplaced
            
label Kitty_Room:
    $ bg_current = "bg kitty"
    call Set_The_Scene from _call_Set_The_Scene_69
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level from _call_Taboo_Level_17
    call QuickEvents from _call_QuickEvents_8
    call Checkout(1) from _call_Checkout_32
    if Round <= 10: 
                call Round10 from _call_Round10_5
                call Girls_Location from _call_Girls_Location_26
                call EventCalls from _call_EventCalls_29 
    
    call GirlsAngry from _call_GirlsAngry_8            
    call Set_The_Scene from _call_Set_The_Scene_70  
    
# Kitty's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_6
    if K_Loc == bg_current:
        $ Line = "You are in Kitty's room. What would you like to do?"
    else:
        $ Line = "You are in Kitty's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat from _call_Chat_8
        
        "Would you like to study?" if K_Loc == bg_current:                
                    call Kitty_Study from _call_Kitty_Study_1
            
        "Sleep." if Current_Time == "Night" and K_Loc == bg_current:
                    call Round10 from _call_Round10_6
                    call Girls_Location from _call_Girls_Location_27
                    call EventCalls from _call_EventCalls_30 
                    
        "Wait." if Current_Time != "Night":
                    call Round10 from _call_Round10_7
                    call Girls_Location from _call_Girls_Location_28
                    call EventCalls from _call_EventCalls_31 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap from _call_Worldmap_10 
    
    if "angry" in K_RecentActions:
            call KittyFace("angry") from _call_KittyFace_14
            ch_k "Go. Now."
            "Kitty pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Kitty_Room


label Kitty_Study:                       #study events
            call Shift_Focus("Kitty") from _call_Shift_Focus_58
            if Current_Time == "Night":
                ch_k "It's kinda late for studying. . . Tomorrow?"
                return
            elif Round <= 30:        
                ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                return
            else:
                ch_k "Sure."
                        
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["You study for a while, it was fairly boring.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and watch a movie instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test."
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
            $ D20 = renpy.random.randint(1, 20)    
            if D20 > 10:
                call Kitty_Frisky_Study from _call_Kitty_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait from _call_Wait_20 
            call Kitty_Leave from _call_Kitty_Leave_3
            call Rogue_Leave from _call_Rogue_Leave_3
            return
#End Kitty Study
            
label Kitty_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Kitty", 1000) and K_Blow > 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She unzips you pants and pulls your dick out, stroking it slowly."
                        "She then dives her head under the book, and starts to lick it."        
                        call Kitty_SexAct("blow") from _call_Kitty_SexAct_1 
            elif D20 > 14 and ApprovalCheck("Kitty", 1000) and K_Hand >= 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                        "She unzips you pants and pulls your dick out, stroking it slowly."  
                        call Kitty_SexAct("hand") from _call_Kitty_SexAct_2 
            elif D20 > 10 and (ApprovalCheck("Kitty", 1300) or (K_Mast and ApprovalCheck("Kitty", 1000)))and K_Lust >= 70:
                        "Kitty wriggles against your shoulder, and her hand starts to stroke her crotch."  
                        if "unseen" in K_RecentActions:
                                $ K_RecentActions.remove("unseen")
                        $ Trigger = "masturbation"
                        call Kitty_SexAct("masturbate") from _call_Kitty_SexAct_3      
            elif D20 > 10 and ApprovalCheck("Kitty", 1200) and K_Lust >= 30:
                        "Kitty takes the book from your hand, and sets it aside."
                        if not K_Over and not K_Legs:
                                #if she's mostly naked, cheat
                                call KittyFace("sly") from _call_KittyFace_15                                
                                ch_k "I was[K_like]thinking about maybe \"strip studying,\". . ." 
                                $ K_Eyes = "down"
                                ch_k "but it would be a pretty short game. . ."
                                $ K_Eyes = "squint"
                                ch_k "Was there something you'd rather do?"                                
                                call Kitty_SexMenu from _call_Kitty_SexMenu   
                        else:
                                "She then asks if maybe you want to do some \"strip studying?\""
                                call Kitty_Strip_Study from _call_Kitty_Strip_Study
            elif D20 >5 and ApprovalCheck("Kitty", 700) and K_Kissed > 1:
                        "Kitty leans close to you, and presses her lips to yours."         
                        call Kitty_SexAct("kissing") from _call_Kitty_SexAct_4
            elif ApprovalCheck("Kitty", 500):
                        "Kitty squeezes close to you, and you spend the rest of the night cuddling."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return
    
label Kitty_Caught_Changing:
            call Shift_Focus("Kitty") from _call_Shift_Focus_59
            $ D20 = renpy.random.randint(1, 20)
            
            call KittyFace("surprised", 1) from _call_KittyFace_16
            $ K_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call KittyOutfit("nude") from _call_KittyOutfit_11
            elif D20 >15:       
                    #She's bottomless
                    $ K_Legs = 0
                    $ K_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ K_Over = 0
                    $ K_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ K_Over = 0
                    $ K_Legs = 0
                    $ K_Panties = "black panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ K_Over = 0
            #else: #fully dressed
            call Set_The_Scene from _call_Set_The_Scene_71
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Kitty is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Kitty is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Kitty is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Kitty has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Kitty has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Kitty", (D20 *70)) or (not K_SeenPussy and not K_Panties) or (not K_SeenChest and not K_Chest):
                            # She is mad
                            call KittyFace("surprised") from _call_KittyFace_17
                            $K_Brows = "angry"  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -50)
                            if not K_Over or not K_Legs:
                                $ K_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call KittyFace("surprised", 1) from _call_KittyFace_18      
                            $K_Brows = "confused"
                            if "exhibitionist" in K_Traits:
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (2*D20))  
                            else:
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, D20)
                          
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 20)
                    if D20 > 17:
                        call Kitty_First_Topless from _call_Kitty_First_Topless_2
                        call Kitty_First_Bottomless(1) from _call_Kitty_First_Bottomless_2
                    elif D20 > 15:
                        call Kitty_First_Bottomless from _call_Kitty_First_Bottomless_3
                    elif D20 > 14:
                        call Kitty_First_Topless from _call_Kitty_First_Topless_3
                    menu:
                        ch_k "Why didn't you knock?!"
                        "Sorry, I should have.":  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 3)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 2)
                        "And miss the view?":
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Kitty", 900) and (not K_SeenPussy or not K_SeenChest):            
                            call KittyFace("angry") from _call_KittyFace_19
                            $K_Brows = "confused"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                    else:
                            call KittyFace("sexy") from _call_KittyFace_20
                            $K_Brows = "confused"
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 4)
                    menu:
                        ch_k "Hey, [K_Petname]. . . {i}you{/i} were hoping I'd be naaaked."
                        "Sorry, I should have knocked.":   
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, 2)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 1)
                        "Well, to be honest. . .":
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 50, -2)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)
            call KittyFace("sexy") from _call_KittyFace_21                
            if ApprovalCheck("Kitty", 750) and K_SeenPussy and K_SeenChest:
                    ch_k "I didn't say that I {i}minded{/i}. . ."                
                    $ K_Over = 0
                    pause 1     
                    call KittyOutfit from _call_KittyOutfit_12
                    "She flashes you real quick."  
            else:
                    ch_k "Yeah. . . we wouldn't want any accidents. . ."   
            menu:
                    ch_k "So were you planning on staying?" 
                    "Sure, for a bit.":
                        pass
                    "Actually, I should get going. . .":
                        call KittyOutfit from _call_KittyOutfit_13
                        call Worldmap from _call_Worldmap_11            
            jump Kitty_Room
            return
            #End Kitty Caught Changing
# end Kitty's Room Interface //////////////////////////////////////////////////////////////////////


# Emma's Room Interface //////////////////////////////////////////////////////////////////////
label Emma_Room_Entry:   
    $ Nearby = []     
    call Shift_Focus("Emma")
    $ bg_current = "bg emma"           
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)
    
    if "Emma" in Party:
                    if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                        if ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI"):     #It's late but she really likes you
                                ch_e "It's rather late, [E_Petname], but I can spare you some time." 
                        elif ApprovalCheck("Emma", 500, "LI") or ApprovalCheck("Emma", 300, "OI"):      #she likes you well enough but it's late
                                ch_e "It's late [E_Petname]. I'll see you tomorrow."
                                $ E_RecentActions.append("noentry")                      
                                $ E_DailyActions.append("noentry")  
                                if "Emma" in Party:
                                        $ Party.remove("Emma")   
                                "She heads inside and closes the door behind her."
                                jump Campus_Map         
                    else: #If Emma is in the party and it's not late in the day        
                                ch_e "Don't just stand at the door."
                    call EventCalls
                    jump Emma_Room   
    #End if Emma in Party
    
                    
    if Round >= 10 and E_Loc == "bg emma" and (D20 >=15 and E_Lust >= 70): #Emma caught fapping      
                "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
                menu:
                    extend ""
                    "Knock politely":
                        $ Line = "knock"
                    "Peek inside":
                        call Set_The_Scene
                        "You see Emma, eyes closed and stroking herself vigorously."
                        menu:
                            extend ""
                            "Enter Quietly":
                                    call Emma_Caught_Masturbating
                            "Pull back and knock":                        
                                    $ Line = "knock"
                            "Leave quietly":
                                    "You leave Emma to her business and slip out."
                                    $ E_Lust = 20
                                    jump Campus_Map
                    "Enter quietly":
                            call Emma_Caught_Masturbating
                    "Leave quietly":
                            "You leave Emma to her business and slip out."
                            $ E_Lust = 20
                            jump Campus_Map
                if Line == "knock":
                        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                        "After several seconds and some more shuffling of clothing, Emma comes to the door."
                        call EmmaFace("sexy", 1)     
                        call Set_The_Scene
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                        $ Tempmod += 10
    # End Emma caught Fapping
    
    else: #not auto-caught fapping
            if "Emma" in Keys:
                menu:
                    "You have a key, what do you do?"
                    "Knock politely":
                            $ Line = "knock"
                            
                    "Use the key to enter.":
                            $ bg_current = "bg emma"
                            call Set_The_Scene
                        
            if Line != "knock" and "Emma" in Keys: 
                if E_Loc == "bg emma":
                        if Round <= 10:        
                                if E_RecentActions in ("noentry", "angry"):
                                        call EmmaFace("angry")
                                        ch_e "Out!"    
                                        "Emma shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif (D20 >=19 and E_Lust >= 50) or (D20 >=15 and E_Lust >= 70) or (D20 >=10 and E_Lust >= 80):     
                                #Emma caught fapping
                                call Emma_Caught_Masturbating 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
                                #Emma caught changing
                                call Emma_Caught_Changing
            #End "if you enter without knocking"
                
            else:#You knocked
                        $ Round -= 10 
                        "You knock on Emma's door."        
                        if E_Loc != "bg emma":
                                "Looks like she's not home right now."
                                jump Campus_Map
                            
                        if Round <= 10:
                                if Current_Time == "Night" :
                                    "There's no answer, she's probably asleep."  
                                    jump Campus_Map    
                    
                        if (D20 >=19 and E_Lust >= 50) or (D20 >=15 and E_Lust >= 70) or (D20 >=10 and E_Lust >= 80):    
                                #Emma caught fapping
                                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                "After several seconds and some more shuffling of clothing, Emma comes to the door." 
                                call EmmaFace("perplexed")
                                call Set_The_Scene
                                ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Emma caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Emma comes to the door."
                                call Set_The_Scene
                                ch_e "Oh, do come in [E_Petname], don't mind that I was just getting changed."   
                        elif "angry" in E_RecentActions:
                                ch_e "I haven't any time for this."
                                "Emma pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
                                "Emma opens the door and leans out."
                                "You ask if you can come inside."
            #End "if you knocked"
                    
            #if you reach this point then you've asked to enter.               
            if E_Loc != "bg emma":
                    "Looks like she's not home right now."                
                    if "Emma" in Keys:
                            menu:
                                "Go in and wait for her?"
                                "Yes":
                                        $ Line = 0
                                        jump Emma_Room
                                "No":
                                        pass
                    "You head back."
                    jump Campus_Map 
                    
            elif E_RecentActions in ("noentry", "angry"):
                    call EmmaFace("angry")
                    ch_e "I believe I've made myself clear."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in E_RecentActions:
                    ch_e "Later, [E_Petname]."  
                    jump Campus_Map 
                    
            elif "noentry" in E_RecentActions:
                    call EmmaFace("angry")
                    ch_e "Out."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -5)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -2)
                    $ E_RecentActions.append("angry")                      
                    $ E_DailyActions.append("angry") 
                    jump Campus_Map  
            
            elif Current_Time == "Night" and (E_Sleep or E_SEXP >= 30):                                                   
                    #It's late but she really likes you
                    ch_e "It is getting late, [E_Petname]."
                    ch_e "but you are so adorable."                   
            elif Current_Time == "Night" and (ApprovalCheck("Emma", 1000, "LI") or ApprovalCheck("Emma", 600, "OI")):     
                    #It's late but she really likes you
                    ch_e "It is getting late, [E_Petname], but I could make some time."    
                    
            elif Current_Time == "Night" and (ApprovalCheck("Emma", 500, "LI") or ApprovalCheck("Emma", 300, "OI")):     
                    #she likes you well enough but it's late
                    ch_e "It's late [E_Petname]. I'll see you tomorrow."
                    $ E_RecentActions.append("noentry")                      
                    $ E_DailyActions.append("noentry")  
                    jump Campus_Map    
                    
            elif ApprovalCheck("Emma", 600, "LI") or ApprovalCheck("Emma", 300, "OI"):                                    
                    #She quite likes you and lets you in   
                    ch_e "Come in, [E_Petname]."        
            else:                                                                                                          
                    #She doesn't like you      
                    ch_e "I don't think that would be appropriate."
                    $ E_RecentActions.append("noentry")                      
                    $ E_DailyActions.append("noentry")  
                    jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg emma"         
    call EventCalls
    if E_Loc == "bg emma" and "angry" in E_RecentActions:
        "Emma pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg emma":
        jump Misplaced
            
label Emma_Room:
    $ bg_current = "bg emma"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Set_The_Scene
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    call GirlsAngry        
    
# Emma's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if E_Loc == bg_current:
        $ Line = "You are in Emma's room. What would you like to do?"
    else:
        $ Line = "You are in Emma's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":                
                    call Emma_Study
            
        "Sleep." if Current_Time == "Night" and E_Loc == bg_current:
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 

        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in E_RecentActions:
            call EmmaFace("angry")
            ch_e "I think you should leave now."
            "Emma pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Emma_Room
    
    


label Emma_Caught_Changing:
            call Shift_Focus("Emma")
            $ D20 = renpy.random.randint(1, 20)
            
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call EmmaOutfit("nude")
            elif D20 >15:       
                    #She's bottomless
                    $ E_Legs = 0
                    $ E_Panties = 0
            elif D20 >14:       
                    #She's Topless
                    $ E_Over = 0
                    $ E_Chest = 0
            elif D20 >10:       
                    #She's in her underwear
                    $ E_Over = 0
                    $ E_Legs = 0
                    $ E_Panties = "white panties"
            elif D20 >5:        
                    #She's wearing pants/skirt
                    $ E_Over = 0
            #else: #fully dressed
            call Set_The_Scene(Dress=0)
            if D20 > 17:        
                    #She's naked
                    "As you enter the room, you see Emma is naked, and seems to be getting dressed."      
            elif D20 >14:       
                    #She's Topless
                    "As you enter the room, you see Emma is practically naked, and seems to be getting dressed."  
            elif D20 >10:       
                    #She's in her underwear
                    "As you enter the room, you see Emma is in her underwear, and seems to be getting dressed." 
            elif D20 >5:        
                    #She's wearing pants/skirt
                    "As you enter the room, you see Emma has her top off, and seems to be getting dressed." 
            else:
                    #She's done
                    "As you enter the room, you see Emma has just pulled her top on, and seems to have been getting dressed." 
                 
            if D20 > 5: 
                    if not ApprovalCheck("Emma", (D20 *70)) or (not E_SeenPussy and not E_Panties) or (not E_SeenChest and not E_Chest):
                            # She is mad
                            call EmmaFace("surprised")
                            $E_Brows = "angry"  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -50)
                            if not E_Over or not E_Legs:
                                $ E_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call EmmaFace("surprised", 1)      
                            $E_Brows = "confused"
                            if "exhibitionist" in E_Traits:
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, (2*D20))  
                            else:
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, D20)
                          
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 20)
                    if D20 > 17:
                        call Emma_First_Topless
                        call Emma_First_Bottomless(1)
                    elif D20 > 15:
                        call Emma_First_Bottomless
                    elif D20 > 14:
                        call Emma_First_Topless
                    menu:
                        ch_e "Did you consider knocking?"
                        "Sorry, I should have.":  
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 3)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
                        "And miss the view?":
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
                    #end if she's partially nude
            else:              
                    #She's fully dressed      
                    if not ApprovalCheck("Emma", 900) and (not E_SeenPussy or not E_SeenChest):            
                            call EmmaFace("angry")
                            $E_Brows = "confused"
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -5)
                    else:
                            call EmmaFace("sexy")
                            $E_Brows = "confused"
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 4)
                    menu:
                        ch_e "Were you hoping to catch me in a compromising position?."
                        "Sorry, I should have knocked.":   
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 2)
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
                        "Well, to be honest. . .":
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 3)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
            call EmmaFace("sexy")                
            if ApprovalCheck("Emma", 750) and E_SeenPussy and E_SeenChest:
                    ch_e "That does show initiative. . ."                
                    $ E_Over = 0
                    pause 1     
                    call EmmaOutfit
                    "She flashes you real quick."  
            else:
                    ch_e "Hmm, show a bit more care next time. . ."   
            menu:
                    ch_e "Did you have business with me?" 
                    "Yeah, a little.":
                        pass
                    "Actually, I should get going. . .":
                        call EmmaOutfit
                        call Worldmap            
            jump Emma_Room
            return
            #End Emma Caught Changing
            
# end Emma's Room Interface //////////////////////////////////////////////////////////////////////


label Study_Room_Entry:
    $ bg_current = "bg study"           
    call Gym_Clothes from _call_Gym_Clothes_13
    call Set_The_Scene(Entry = 1) from _call_Set_The_Scene_72    
    call Taboo_Level from _call_Taboo_Level_18
    menu:
            "You're at the door, what do you do?"
            "Knock politely":
                    $ Line = "knock"
                    
            "Enter without knocking":
                 if Current_Time == "Night":
                         "The door is locked. It's not like you could just walk through it."
                         jump Study_Room_Entry
                                                 
            "Use the key to enter" if Current_Time == "Night" and "Xavier" in Keys:
                    "You use your key."
                    $ Line = 0
            
            "Ask Kitty" if Current_Time == "Night" and "Kitty" in Party:
                    $ Line = "kitty"
                    
            "Leave":
                    "You head back."
                    jump Campus_Map 
     
    if Line == "knock": 
        if Current_Time == "Night":
            "There's no answer, he's probably asleep." 
            jump Study_Room_Entry
        else:           
            ch_x "Yes, enter. . ."
            "You enter the room."
    elif Line == "kitty":
            ch_k "Yeah?"
            while True:
                menu:
                    extend ""
                    "Could you phase through the door and open it for me?":
                            if "Sneakthief" in K_Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in K_RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck("Kitty", 400, "I") or ApprovalCheck("Kitty", 1400):
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 10)  
                                ch_k "Heh, you have a wicked mind. . ."
                                $ K_Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                                ch_k "Um, I don't really feel comfortable doing that. . ."
                                $ K_RecentActions.append("no thief")
                    "Open the door.":
                            if "Sneakthief" in K_Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in K_RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck("Kitty", 500, "O") or ApprovalCheck("Kitty", 1600):
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 15) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 10)  
                                ch_k "Heh, if you say so. . ."
                                $ K_Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                                ch_k "Um, no."
                                $ K_RecentActions.append("no thief")
                    "Never mind. [[Leave]":
                            "You head back."
                            jump Campus_Map 
            jump Study_Room_Entry
    elif Current_Time != "Night":                
            ch_x "You know, [Playername], it is not polite to enter a room unannounced."
    $ Cnt = 0                        
                
label Study_Room:
    $ bg_current = "bg study"
    call Set_The_Scene from _call_Set_The_Scene_73
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level from _call_Taboo_Level_19
    call QuickEvents from _call_QuickEvents_9
    call Checkout(1) from _call_Checkout_33
    if Round <= 10:         
            if Current_Time == "Night":                         
                "It's late, you head back to your room."
                jump Player_Room
            else:
                call Wait from _call_Wait_21                 
                call Girls_Location from _call_Girls_Location_29
    
    call GirlsAngry from _call_GirlsAngry_9
    call Set_The_Scene from _call_Set_The_Scene_74      
    
# Study Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Current_Time == "Night":
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"        
        "Chat" if Current_Time == "Night": #fix, open up once sex while in office is fine
                    call Chat from _call_Chat_9
        
#        "Plan Omega!" if R_Loc == bg_current:
#                    if ApprovalCheck("Rogue", 1500, TabM=1, Loc="No") and P_Lvl >= 5:
#                        jump Plan_Omega
#                    else:
#                        ch_r "What?"
#        "Plan Kappa!" if K_Loc == bg_current:
#                    if "Xavier's photo" in P_Inventory and P_Lvl >= 5 and ApprovalCheck("Kitty", 1500, TabM=1, Loc="No"):                   
#                        jump Plan_Kappa
#                    else:
#                        ch_k "What?"
        
            
        "Explore" if Current_Time == "Night" and "explore" not in P_RecentActions: 
                    $ Cnt = 0    
                    $ P_RecentActions.append("explore")
                    jump Study_Room_Explore
            
        "Wait":
                    if Current_Time == "Night":
                            "You probably don't want to be here when Xavier gets in."
                    elif Current_Time == "Evening":
                            ch_x "If you don't mind, I would like to close up for the evening?"
                            "You return to your room."
                            jump Player_Room                    
                    else:           
                            call Wait from _call_Wait_22  
                            call Girls_Location from _call_Girls_Location_30
                            ch_x "Not that I mind the company, but is there something I can do for you?"
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap from _call_Worldmap_12 
    jump Study_Room
    
    
label Study_Room_Explore:
    $ Line = 0
    #$ D20 = renpy.random.randint(1, 20)    
    menu:
        "Where would you like to look?"
        "Bookshelf":
            #if D20 >= 15 + Cnt:
                    $ Line = "book"
            #else:
            #        "As you search the bookshelf, you accidentally knock one of the books off."
            #        "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            #elif D20 >= 10 + Cnt:
            else:
                    $ Line = "left"
            #        "As you open the drawer, it makes a loud a squeak."
            #        "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            #elif D20 >= 15 + Cnt:
            else:
                    $ Line = "mid"
            #        "As you open the drawer, it makes a loud a squeak."
            #        "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            #elif D20 >= 15 + Cnt:
            else:
                    $ Line = "right"
            #        "As you open the drawer, it makes a loud a squeak."
            #        "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]": 
                    jump Study_Room
    
    $ D20 = renpy.random.randint(1, 20)
    if not Line:
                "Probably best to get out of here."
                "You slip out and head back to your room."
                jump Player_Room_Entry 
    elif Line == "book":
            if D20 >= 5 and "Well Studied" not in Achievements:            
                "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
                if K_Loc == bg_current:
                    menu:
                        "Since Kitty is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck("Kitty", 700, "I") or ApprovalCheck("Kitty", 1800):
                                if "Well Studied" not in Achievements:
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10) 
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 15)  
                                        ch_k "Sounds like a plan."
                                        "Kitty swipes her hand through the box, and pulls out a stack of bills."
                                        "Looks like Xavier was hiding a rainy day fund in here."
                                        $ P_Cash += 500
                                        "[[$500 acquired.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Looks like this has been thoroughly looted."
                            else:#Kitty doesn't approve 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -3) 
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 1) 
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 60, 2)  
                                ch_k "I really don't think we should do that."                            
                        "Put it back.":
                            "You place the box back on the shelf."
                else:#Kitty's not there
                            "You can't think of any way to get it open, too bad you aren't a ghost or something."
                            "You place the box back on the shelf."
            elif D20 >= 5:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through the books for a few minutes, but don't find anything."
                "It would probably take a more thorough search."            
    elif Line == "left":
            if D20 >= 5 and "Xavier's photo" not in P_Inventory:            
                "Buried under a pile of documents, you find a printed out photo."
                #"It appears to be a selfie of Mystique making out with Xavier."
                "It appears to be a selfie of Mystique naked with Xavier."
                #"She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                "Oh, {i}that's{/i} interesting."
                #show Mystique_Picture
                show screen Mystique_Pic
            #     textbutton "Mystique Picture" text_size 15 action Show("Mystique_Pic",transition=Pause(1))
            # if renpy.get_screen("Mystique_Pic"):
            #     textbutton "Hide Picture" text_size 15 action Hide("Mystique_Pic",transition=Pause(1))
                "[[Xavier's photo acquired.]"
                #pause
                hide screen Mystique_Pic
                #Hide("Mystique_Pic",transition=Pause(1))
                #hide Mystique_Picture
                $ P_Inventory.append("Xavier's photo")
            elif D20 >= 5:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."            
    elif Line == "mid":
            if "All" not in Keys:
                "Under a few trinkets, you find a small keyring."
                "[[Keyring acquired.]"
                if "Xavier" not in Keys:
                    $ Keys.append("Xavier") 
                if "Rogue" not in Keys:
                    $ Keys.append("Rogue")
                if "Kitty" not in Keys:
                    $ Keys.append("Kitty")
                if "All" not in Keys:
                    $ Keys.append("All")
    elif Line == "right":
            "There doesn't seem to be anything more of interest in here, maybe later?"
    $ Cnt += 3
    jump Study_Room_Explore
# end Study's Room Interface //////////////////////////////////////////////////////////////////////

label Kitty_Sent_Selfie(test=0):
    if K_Loc != bg_current and K_Nudes == 1 and "Kitty" in Digits:
        if test == 0:
            $ test = renpy.random.randint(1, 3)
            #$ test = 1

        $ K_OverTemp = K_Over
        $ K_ChestTemp = K_Chest
        if test == 1:
            $test = 0
        
            if ApprovalCheck("Kitty", 1250, TabM = 3) or (K_SeenChest and not Taboo):
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)   
                $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)    
                #$ Line = K_Over
                $ K_Over = 0
                $ K_Chest = 0                         
                if not K_SeenChest:
                    call KittyFace("bemused", 1) from _call_KittyFace_22
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)  
                    #"She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
                    call Kitty_First_Topless(1) from _call_Kitty_First_Topless_4        
                #else: 
                #    "She pulls her [Line] over her head, tossing it to the ground." 
                call Set_The_Scene from _call_Set_The_Scene_75
                show Kitty_Selfie at center zorder 200
                "Kitty sent you a picture"
                ch_k "It's hot huh, [K_Petname]?" 
    
            elif (ApprovalCheck("Kitty", 1000, TabM = 3) or (K_SeenChest and not Taboo)) and K_Chest != 0:
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)      
                #$ Line = K_Chest
                $ K_Over = 0                        
                if not K_SeenChest:
                    call KittyFace("bemused", 1) from _call_KittyFace_23
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)                              
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 4)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 3)   
                    #"She hesitantly glances your way, and then with a shrug pulls her [Line] through herself, tossing it to the ground."
                    #call Kitty_First_Topless(1)
                call Set_The_Scene from _call_Set_The_Scene_76
                show Kitty_Selfie at center zorder 200
                "Kitty sent you a picture" 
        
            elif ApprovalCheck("Kitty", 600):
                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 60, 5)                
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 2)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 1)
                $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 15)
                call Set_The_Scene from _call_Set_The_Scene_77
                show Kitty_Selfie at center zorder 200
                "Kitty sent you a picture" 
                ch_k "What do you think of this look, [K_Petname]?" 
        hide Kitty_Selfie 
        $ K_Over = K_OverTemp
        $ K_Chest = K_ChestTemp
    return

label Rogue_Sent_Selfie(test=0):
    if R_Loc != bg_current and R_Nudes == 1 and "Rogue" in Digits:
        if R_Resistance and R_Addict >= 60 and not R_Event[3]:
            return
        if test == 0:
            $ test = renpy.random.randint(1, 3)
            #$ test = 1

        #$ R_OverTemp = K_Over
        #$ R_ChestTemp = K_Chest
        if test == 1:
            $test = 0
        
            if ApprovalCheck("Rogue", 1250, TabM = 3) or (K_SeenChest and not Taboo):
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 60, 5)                
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)   
                $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 15)    
                #$ R_Over = 0
                #$ R_Chest = 0                         
                if not R_SeenChest:
                    call RogueFace("bemused", 1) from _call_RogueFace_100
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 3)                              
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 4)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 3)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 3)  
                    #"She hesitantly glances your way, and then with tug her [Line] passes through her, tossing it to the ground."   
                    call Rogue_First_Topless(1) from _call_Rogue_First_Topless_4        
                #else: 
                #    "She pulls her [Line] over her head, tossing it to the ground." 
                $ R_SelfieOverlay = renpy.random.randint(0, 1)
                call Set_The_Scene from _call_Set_The_Scene_78
                show Rogue_Selfie at SpriteLoc(-2,-46) zorder 200
                "Rogue sent you a picture"
                ch_r "It's hot huh, [R_Petname]?" 

        hide Rogue_Selfie 

    return

# Kitty's Room Interface //////////////////////////////////////////////////////////////////////
label Mystique_Room_Entry:
    call Shift_Focus("Mystique") from _call_Shift_Focus_60
    $ bg_current = "bg Mystique"           
    call Gym_Clothes from _call_Gym_Clothes_14
    call Set_The_Scene(Entry = 1) from _call_Set_The_Scene_79    
    call Taboo_Level from _call_Taboo_Level_20
    $ D20 = renpy.random.randint(1, 20)
    
    # if "Kitty" in Party:
    #                 if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
    #                     if ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI"):     #It's late but she really likes you
    #                             ch_k "It's kinda late, [K_Petname], but you can have a minute."    
    #                     elif K_Addict >= 50:
    #                             ch_k "I'd really like to see you. . ."            
    #                     elif ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI"):      #she likes you well enough but it's late
    #                             ch_k "It's a little late [K_Petname]. Tmorrow?"
    #                             $ K_RecentActions.append("noentry")                      
    #                             $ K_DailyActions.append("noentry")  
    #                             "She heads inside and closes the door behind her."
    #                             jump Campus_Map         
    #                 else: #If Kitty is in the party and it's not late in the day        
    #                             ch_k "Come on in!"
    #                 call EventCalls
    #                 jump Kitty_Room   
    # #End if Kitty in Party
    
                    
    # if Round >= 10 and K_Loc == "bg kitty" and (D20 >=15 and K_Lust >= 70): #Kitty caught fapping      
    #             "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
    #             menu:
    #                 extend ""
    #                 "Knock politely":
    #                     $ Line = "knock"
    #                 "Peek inside":
    #                     call Set_The_Scene
    #                     "You see Kitty, eyes closed and stroking herself vigorously."
    #                     menu:
    #                         extend ""
    #                         "Enter Quietly":
    #                                 call Kitty_Caught_Masturbating
    #                         "Pull back and knock":                        
    #                                 $ Line = "knock"
    #                         "Leave quietly":
    #                                 "You leave Kitty to her business and slip out."
    #                                 $ K_Lust = 20
    #                                 jump Campus_Map
    #                 "Enter quietly":
    #                         call Kitty_Caught_Masturbating
    #                 "Leave quietly":
    #                         "You leave Kitty to her business and slip out."
    #                         $ K_Lust = 20
    #                         jump Campus_Map
    #             if Line == "knock":
    #                     "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
    #                     "After several seconds and some more shuffling of clothing, Kitty comes to the door."
    #                     $ K_Brows = "confused"
    #                     $ K_Eyes = "surprised"
    #                     $ K_Mouth = "smile"
    #                     $ K_Blush = 1
    #                     call Set_The_Scene
    #                     ch_k "Oh, hey, [K_Petname], I was. . . never mind."
    #                     $ Tempmod += 10
    # # End Kitty caught Fapping
    
    # else: #not auto-caught fapping
    #         if "Kitty" in Keys:
    #             menu:
    #                 "You have a key, what do you do?"
    #                 "Knock politely":
    #                         $ Line = "knock"
                            
    #                 "Use the key to enter.":
    #                         $ bg_current = "bg kitty"
    #                         call Set_The_Scene
                        
    #         if Line != "knock" and "Kitty" in Keys: 
    #             if K_Loc == "bg kitty":
    #                     if Round <= 10:        
    #                             if K_RecentActions in ("noentry", "angry"):
    #                                     call KittyFace("angry")
    #                                     ch_k "GTFO."    
    #                                     "Kitty shoves you back into the hall."
    #                                     jump Campus_Map   
    #                             if Current_Time == "Night" :    
    #                                     "She's asleep in bed. You slip out quietly." #fix add options here.                            
    #                                     jump Campus_Map   
    #                     elif (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):     
    #                             #Kitty caught fapping
    #                             call Kitty_Caught_Masturbating 
    #                     elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
    #                             #Kitty caught changing
    #                             call Kitty_Caught_Changing
    #         #End "if you enter without knocking"
                
    #         else:#You knocked
    #                     $ Round -= 10 
    #                     "You knock on Kitty's door."        
    #                     if K_Loc != "bg kitty":
    #                             "Looks like she's not home right now."
    #                             jump Campus_Map
                            
    #                     if Round <= 10:
    #                             if Current_Time == "Night" :
    #                                 "There's no answer, she's probably asleep."  
    #                                 jump Campus_Map    
                    
    #                     if (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):    
    #                             #Kitty caught fapping
    #                             "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
    #                             "After several seconds and some more shuffling of clothing, Kitty comes to the door."
    #                             $ K_Brows = "confused"
    #                             $ K_Eyes = "surprised"
    #                             $ K_Mouth = "smile"
    #                             $ K_Blush = 1
    #                             call Set_The_Scene
    #                             ch_k "Oh, hey, [K_Petname], I was. . . never mind."
    #                             $ Tempmod += 10
    #                     elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
    #                             #Kitty caught changing
    #                             "You hear the rustling of fabric and some knocking around, but after a few seconds Kitty comes to the door."
    #                             call Set_The_Scene
    #                             ch_k "Oh, hi [K_Petname], I was[K_like]just getting changed."   
    #                     elif "angry" in K_RecentActions:
    #                             ch_k "Nooope."
    #                             "Kitty pushes you back into the hall and slams the door."
    #                             $ Trigger = 0
    #                             jump Campus_Map    
    #                     else:
    #                             call Set_The_Scene
    #                             "Kitty opens it a bit and pops out and you ask if you can come inside."
    #         #End "if you knocked"
                    
    #         #if you reach this point then you've asked to enter.               
    #         if K_Loc != "bg kitty":
    #                 "Looks like she's not home right now."                
    #                 if "Kitty" in Keys:
    #                         menu:
    #                             "Go in and wait for her?"
    #                             "Yes":
    #                                     $ Line = 0
    #                                     jump Kitty_Room
    #                             "No":
    #                                     pass
    #                 "You head back."
    #                 jump Campus_Map 
                    
    #         elif K_RecentActions in ("noentry", "angry"):
    #                 call KittyFace("angry")
    #                 ch_k "What part of \"GTFO\" was unclear?"  
    #                 jump Campus_Map    
                    
    #         elif Current_Time == "Night" and "noentry" in K_RecentActions:
    #                 ch_k "Scram. I'll see you tomorrow"  
    #                 jump Campus_Map 
                    
    #         elif "noentry" in K_RecentActions:
    #                 call KittyFace("angry")
    #                 ch_k "GTFO."
    #                 $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
    #                 $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, -2)
    #                 $ K_RecentActions.append("angry")                      
    #                 $ K_DailyActions.append("angry") 
    #                 jump Campus_Map  
            
    #         elif Current_Time == "Night" and (K_Sleep or K_SEXP >= 30):                                                   
    #                 #It's late but she really likes you
    #                 ch_k "It's late, [K_Petname], but you're so cute."                   
    #         elif Current_Time == "Night" and (ApprovalCheck("Kitty", 1000, "LI") or ApprovalCheck("Kitty", 600, "OI")):     
    #                 #It's late but she really likes you
    #                 ch_k "It's late, [K_Petname], but I could hang out a bit."                  
    #         elif K_Addict >= 50:
    #                 ch_k "I could use some attention. . ."
                    
    #         elif Current_Time == "Night" and (ApprovalCheck("Kitty", 500, "LI") or ApprovalCheck("Kitty", 300, "OI")):     
    #                 #she likes you well enough but it's late
    #                 ch_k "It's late [K_Petname]. Tomorrow?"
    #                 $ K_RecentActions.append("noentry")                      
    #                 $ K_DailyActions.append("noentry")  
    #                 jump Campus_Map    
                    
    #         elif ApprovalCheck("Kitty", 600, "LI") or ApprovalCheck("Kitty", 300, "OI"):                                    
    #                 #She quite likes you and lets you in   
    #                 ch_k "Sure, come on in [K_Petname]."        
    #         else:                                                                                                          
    #                 #She doesn't like you      
    #                 ch_k "Nah, you can stay out."
    #                 $ K_RecentActions.append("noentry")                      
    #                 $ K_DailyActions.append("noentry")  
    #                 jump Campus_Map
    
    # If you get this far, she's allowed you in
    $ bg_current = "bg Mystique"         
    call EventCalls from _call_EventCalls_32
    # if K_Loc == "bg kitty" and "angry" in K_RecentActions:
    #     "Kitty pushes you back into the hall and slams the door. You head back to your room."
    #     $ Line = 0
    #     $ Trigger = 0
    #     jump Player_Room
    if bg_current != "bg Mystique":
        jump Misplaced
            
label Mystique_Room:
    $ bg_current = "bg Mystique"
    call Set_The_Scene from _call_Set_The_Scene_80
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level from _call_Taboo_Level_21
    call QuickEvents from _call_QuickEvents_10
    call Checkout(1) from _call_Checkout_34
    if Round <= 10: 
                call Round10 from _call_Round10_8
                call Girls_Location from _call_Girls_Location_31
                call EventCalls from _call_EventCalls_33 
    
    call GirlsAngry from _call_GirlsAngry_10            
    call Set_The_Scene from _call_Set_The_Scene_81  
    
# Kitty's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    call Rogue_Sent_Selfie from _call_Rogue_Sent_Selfie_7
    call Kitty_Sent_Selfie from _call_Kitty_Sent_Selfie_7
    if newgirl["Mystique"].Loc == bg_current:
        $ Line = "You are in Mystique's room. What would you like to do?"
    else:
        $ Line = "You are in Mystique's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat from _call_Chat_10
        
        "Would you like to study?" if newgirl["Mystique"].Loc == bg_current:                
                    call Mystique_Study from _call_Mystique_Study_1
            
        "Sleep." if Current_Time == "Night" and newgirl["Mystique"].Loc == bg_current:
                    call Round10 from _call_Round10_9
                    call Girls_Location from _call_Girls_Location_32
                    call EventCalls from _call_EventCalls_34 
                    
        "Wait." if Current_Time != "Night":
                    call Round10 from _call_Round10_10
                    call Girls_Location from _call_Girls_Location_33
                    call EventCalls from _call_EventCalls_35 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap from _call_Worldmap_13 
    
    if "angry" in newgirl["Mystique"].RecentActions:
            call MystiqueFace("angry") from _call_MystiqueFace_329
            ch_m "Go. Now."
            "Mystique pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Mystique_Room           