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
                    jump Rogue_Room_Test
        "Rogue's Room":   
                    $ renpy.pop_call() 
                    jump Rogue_Room_Entry 
        "Kitty's Room" if "met" in K_History:   
                    $ renpy.pop_call() 
                    jump Kitty_Room_Entry            
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
                call DrainWord("Rogue","caught",1,0)
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Rogue")
                $ Trigger = 0
                jump Player_Room
        if "caught" in K_RecentActions:        
                call DrainWord("Kitty","caught",1,0)
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Kitty")
                $ Trigger = 0
                jump Player_Room
        if "caught" in E_RecentActions:        
                call DrainWord("Emma","caught",1,0)
                "You immediately return to your rooms."
                $ bg_current = "bg player"
                call Remove_Girl("Emma")
                $ Trigger = 0
                jump Player_Room
        if bg_current == "bg player":
                jump Player_Room 
        if bg_current == "bg rogue":
                jump Rogue_Room 
        if bg_current == "bg kitty":
                jump Kitty_Room 
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
    call Gym_Clothes
    call EventCalls
    call Set_The_Scene(Entry = 1)    
    
label Player_Room:
    $ bg_current = "bg player"
    call Set_The_Scene
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls
                
    call GirlsAngry      
    call Set_The_Scene

# Player Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in your room. What would you like to do?"
        "Chat":
                    call Chat
            
        "Would you like to study [[Rogue]?" if R_Loc == bg_current:
                    call Rogue_Study
        "Would you like to study [[Kitty]?" if K_Loc == bg_current:
                    call Kitty_Study
                    
        "Sleep" if Current_Time == "Night":            
                    call Round10
                    call Girls_Location
                    call EventCalls  
        "Wait" if Current_Time != "Night":
                    "You wait around a bit."
                    call Wait                 
                    call Girls_Location
                    call EventCalls      
            
        "Shop":
                    call Shop                
        "Special Options":
                    call SpecialMenu
        
        "Go to Rogue's Room" if TravelMode:           
                    jump Rogue_Room_Entry 
        "Go to Kitty's Room" if TravelMode and "met" in K_History:           
                    jump Kitty_Room_Entry 
        "Go to the Showers" if TravelMode:         
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                            jump Campus_Entry
                    else:
                            call Worldmap
    jump Player_Room

# end Player's Room Interface //////////////////////////////////////////////////////////////////////

# Rogue's Room Interface //////////////////////////////////////////////////////////////////////
label Rogue_Room_Entry:
    call Shift_Focus("Rogue")
    $ bg_current = "bg rogue"           
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
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
                    call EventCalls
                    jump Rogue_Room   
    #End if Rogue in Party
    
                    
    if Round >= 10 and R_Loc == "bg rogue" and (D20 >=15 and R_Lust >= 70): #Rogue caught fapping      
                "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
                menu:
                    extend ""
                    "Knock politely":
                        $ Line = "knock"
                    "Peek inside":
                        call Set_The_Scene
                        "You see Rogue, eyes closed and stroking herself vigorously."
                        menu:
                            extend ""
                            "Enter Quietly":
                                    call Rogue_Caught_Masturbating
                            "Pull back and knock":                        
                                    $ Line = "knock"
                            "Leave quietly":
                                    "You leave Rogue to her business and slip out."
                                    $ R_Lust = 20
                                    jump Campus_Map
                    "Enter quietly":
                            call Rogue_Caught_Masturbating
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
                        call Set_The_Scene
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
                            call Set_The_Scene
                        
            if Line != "knock" and "Rogue" in Keys: 
                if R_Loc == "bg rogue":
                        if Round <= 10:        #add "no" condtion here
                                if R_RecentActions in ("noentry", "angry"):
                                        call RogueFace("angry")
                                        ch_r "Buzz off already."  
                                        "Rogue shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif (D20 >=19 and R_Lust >= 50) or (D20 >=15 and R_Lust >= 70) or (D20 >=10 and R_Lust >= 80):     #Rogue caught fapping
                                call Rogue_Caught_Masturbating 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           #Rogue caught changing
                                call Rogue_Caught_Changing
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
                                call Set_The_Scene
                                ch_r "Sorry about that [R_Petname], I was. . . working out."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          #Rogue caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Rogue comes to the door."
                                call Set_The_Scene
                                ch_r "Sorry about that [R_Petname], I was just getting changed."        
                        elif "angry" in R_RecentActions:
                                ch_r "I don't want to deal with you right now."
                                "Rogue pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
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
                    call RogueFace("angry")
                    ch_r "Buzz off already."  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in R_RecentActions:
                    ch_r "Hey, I told you you're not welcome. I'll see you tomorrow"
                    jump Campus_Map 
                    
            elif "noentry" in R_RecentActions:
                    call RogueFace("angry")
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
    call EventCalls
    if R_Loc == "bg rogue" and "angry" in R_RecentActions:
        "Rogue pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg rogue":
        jump Misplaced
            
label Rogue_Room:
    $ bg_current = "bg rogue"
    call Set_The_Scene
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)    
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls    
    call GirlsAngry    
    call Set_The_Scene  
    
# Rogue's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if R_Loc == bg_current:
        $ Line = "You are in Rogue's room. What would you like to do?"
    else:
        $ Line = "You are in Rogue's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?" if R_Loc == bg_current:                
                    call Rogue_Study
            
        "Sleep." if Current_Time == "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls    
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry         
        "Go to Kitty's Room" if TravelMode and "met" in K_History:             
                jump Kitty_Room_Entry 
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap 
    
    if "angry" in R_RecentActions:
            call RogueFace("angry")
            ch_r "I really think you should leave."
            "Rogue pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Rogue_Room


label Rogue_Study:                       #study events
            call Shift_Focus("Rogue")
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
                call Rogue_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait 
            call Rogue_Leave
            call Kitty_Leave
            return
#End Rogue Study
            
label Rogue_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Rogue", 1000) and R_Blow > 5:
                        "Rogue get a mischievous look on her face, and begins to unzip your pants."
                        "She pulls your dick out and pops it into her mouth."        
                        call Rogue_SexAct("blow") 
            elif D20 > 14 and ApprovalCheck("Rogue", 1000) and R_Hand >= 5:
                        "Rogue get a mischievous look on her face, and begins to unzip your pants."
                        "She pulls your dick out and begins to slowly stroke it."        
                        call Rogue_SexAct("hand") 
            elif D20 > 10 and (ApprovalCheck("Rogue", 1300) or (R_Mast and ApprovalCheck("Rogue", 1000))) and R_Lust >= 70:
                        "Rogue get a mischievous look on her face, and starts to rub herself."          
                        $ R_RecentActions.remove("unseen") if "unseen" in R_RecentActions else R_RecentActions #she sees you're there
                        $ Trigger = "masturbation"
                        call Rogue_SexAct("masturbate")      
            elif D20 > 10 and ApprovalCheck("Rogue", 1200) and R_Lust >= 30:                
                        if not R_Over and not R_Legs and R_Panties != "shorts":
                                #if she's mostly naked, cheat
                                call RogueFace("sly")                                
                                ch_r "Well, I did consider suggesting we do some \"strip studying,\". . ." 
                                $ R_Eyes = "down"
                                ch_r "but it looks like I got ahead of myself. . ."
                                $ R_Eyes = "squint"
                                ch_r "Did you have anything else in mind?"                                
                                call Rogue_SexMenu   
                        else:
                                "Rogue moves a bit closer to you, and then suggests \"strip studying.\""
                                call Rogue_Strip_Study
            elif ApprovalCheck("Rogue", 700) and R_Kissed > 1:
                        "Rogue leans close to you, and leans in for a kiss."         
                        call Rogue_SexAct("kissing")
            elif ApprovalCheck("Rogue", 500):
                        "Rogue leans close to you and you spend the rest of the study session nuzzled close."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return
    
label Rogue_Caught_Changing:
            call Shift_Focus("Rogue")
            $ D20 = renpy.random.randint(1, 20)
            
            call RogueFace("surprised", 1)
            $ R_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call RogueOutfit("nude")
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
            call Set_The_Scene
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
                            call RogueFace("surprised")
                            $R_Brows = "angry"  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -50)
                            if not R_Over or not R_Legs:
                                $ R_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call RogueFace("surprised", 1)      
                            $R_Brows = "confused"
                            if "exhibitionist" in R_Traits:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, (2*D20))  
                            else:
                                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, D20)
                          
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20)
                    if D20 > 17:
                        call Rogue_First_Topless
                        call Rogue_First_Bottomless(1)
                    elif D20 > 15:
                        call Rogue_First_Bottomless
                    elif D20 > 14:
                        call Rogue_First_Topless
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
                            call RogueFace("angry")
                            $R_Brows = "confused"
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                    else:
                            call RogueFace("sexy")
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
            call RogueFace("sexy")                
            if ApprovalCheck("Rogue", 750) and R_SeenPussy and R_SeenChest:
                    ch_r "You could have just asked, [R_Petname]."                
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
                        call RogueOutfit
                        call Worldmap            
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
    call Set_The_Scene
    if not TravelMode: 
        call Worldmap
    jump Campus
    
label Campus_Entry:
    $ bg_current = "bg campus"             
    call Gym_Clothes  
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene
    
label Campus:
    $ bg_current = "bg campus"
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Set_The_Scene
    call Taboo_Level
    call QuickEvents    
    call Checkout(1)    
    call GirlsAngry      

# Uni Square Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in the university square. What would you like to do?"
        
        "Chat":
            call Chat
            
        "Wait." if Current_Time != "Night":
            "You wait around a bit."
            call Wait   
            call EventCalls            
            call Girls_Location
            
        "Go to my Room" if TravelMode:
                    jump Player_Room_Entry  
        "Go to Rogue's Room" if TravelMode: 
                    jump Rogue_Room_Entry 
        "Go to Kitty's Room" if TravelMode and "met" in K_History:
                    jump Kitty_Room_Entry 
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
        "Go to the showers" if TravelMode: 
                    jump Shower_Room_Entry            
        "Xavier's Study" if TravelMode: 
                    jump Study_Room_Entry 
        "Leave [[Navigation map]" if not TravelMode: 
                    call Worldmap                      
    jump Campus

# end University Square Interface //////////////////////////////////////////////////////////////////////



# Classroom Interface //////////////////////////////////////////////////////////////////////

label Class_Room_Entry:
    $ Adjacent = 0
    $ bg_current = "bg classroom"              
    call Gym_Clothes 
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene
    if Current_Time != "Night" and Current_Time != "Evening" and Weekday < 5:   
            call Class_Room_Seating    
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
    call Set_The_Scene
    call Taboo_Level
    call QuickEvents    
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location
                call Set_The_Scene
    call GirlsAngry      
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
                call Chat
                $ Line = "You are in class right now. What would you like to do?" 
            
        "Wait" if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls            
                call Girls_Location 
                    
                if Current_Time == "Midday":
                            $ Line = "A new class is in session. What would you like to do?"
                if Current_Time == "Evening":
                            $ Line = "Classes have let out for the day. What would you like to do?"
            
        "Leave [[Go to Campus Square]":
                if TravelMode:
                    jump Campus_Entry
                else:
                    call Worldmap 
    
    $ Line = 0
    jump Class_Room

# End Core Classroom menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
label Take_Class:                       #Class events 
    call Set_The_Scene  
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
        call Rogue_Frisky_Class
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
        
    call Wait   
    call Girls_Location
    call Set_The_Scene 
    call EventCalls
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


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Danger_Room_Entry:
    $ bg_current = "bg dangerroom"    
    call Taboo_Level
    $ P_RecentActions.append("traveling")
    call EventCalls
    call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene
    "This is the Danger Room. What would you like to do?" 
    
label Danger_Room:
    $ bg_current = "bg dangerroom"  
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")  
    call Set_The_Scene
    call Taboo_Level    
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                        
                call Wait   
                call EventCalls
                call Girls_Location 
                call Set_The_Scene
                call Gym_Clothes                
    call GirlsAngry  
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
                call Chat
            
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls
                call Gym_Clothes
                call Girls_Location 
                call Gym_Clothes
               
        "Leave [[Go to Campus Square]":    
                if TravelMode:        
                    call Gym_Clothes("change")
                    jump Campus_Entry
                else:
                    call Worldmap         
        "Go to the showers" if TravelMode:             
                call Gym_Clothes("change")
                jump Shower_Room_Entry         
    jump Danger_Room

label Training:
#    $ D20 = renpy.random.randint(1, 20)
#    if D20 > 10 and R_Inbt >= 500:
#        call Rogue_Frisky_Danger
        
    $ P_XP += (5 + (int(Round / 10)))
    $ P_DailyActions.append("dangerroom")
    call Set_The_Scene
    
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
        call Rogue_TightsRipped
    
    call Wait
    call Girls_Location 
    call Set_The_Scene
    $ Line = "The training session has ended, what would you like to do next?"
    
    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if R_Hose == "tights":
                $ Count = 1
                $ R_Hose = "ripped tights"    
                call RogueFace("angry")
                if "ripped tights" in R_Inventory:  
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "Well that's a good pair of tights down the chute."                
        elif R_Hose == "pantyhose":
                $ Count = 1
                $ R_Hose = "ripped pantyhose"              
                call RogueFace("angry")
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
                                call Rogue_First_Bottomless 
                                $ Count = 3 if not ApprovalCheck("Rogue", 1400) else Count
                            
                if Count == 2: 
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":                
                                call RogueFace("smile", 1)                     
                                $ R_Inventory.append(R_Hose) 
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand." 
                            "Yeah, too bad.":             
                                call RogueFace("bemused")    
                                ch_r ". . ."         
                            "Ha! Those don't leave much to the imagination!":                        
                                ch_r "Thanks for that. . ."
                                
                elif Count == 3: #She is embarassed and takes off             
                    call RogueFace("startled", 2)  
                    ch_r "I, um, I should get out of here."
                    $ R_Blush = 1
                    call Remove_Girl("Rogue")
                    call RogueOutfit
                #end "if they ripped"
        return
                
# end Danger Room Interface //////////////////////////////////////////////////////////////////////


# Showers Interface //////////////////////////////////////////////////////////////////////
label Shower_Room_Entry:
    $ bg_current = "bg showerroom"             
    call Gym_Clothes  
    call Set_The_Scene(0,1,0)
    call Taboo_Level
    $ D20 = renpy.random.randint(1, 20)
    if Round <= 10: 
        jump Shower_Room
    $ Options.append("nothing")
    if "showered" not in R_DailyActions and (R_Loc == "bg rogue" or R_Loc == "bg dangerroom"):  #Checks if Rogue is in the shower
            $ Options.append("Rogue")   
    if "showered" not in K_DailyActions and (K_Loc == "bg kitty" or K_Loc == "bg dangerroom") and "met" in K_History:  #Checks if Kitty is in the shower
            $ Options.append("Kitty")     
#    if "showered" not in E_DailyActions and (E_Loc == "bg emma" or E_Loc == "bg dangerroom") and "met" in E_History:  #Checks if Emma is in the shower
#            $ Options.append("Emma")
    
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
    call Present_Check
    
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
    
    call Set_The_Scene
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
    call Set_The_Scene(Dress=0)
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                    
                call Wait   
                call EventCalls
                call Girls_Location 
                call Set_The_Scene
    call GirlsAngry      
    #End Room Set-up

# Shower Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You're in the showers. What would you like to do?"

        "Chat":
                call Chat
            
        "Shower" if Round > 30:
                if E_Loc == bg_current:
                    ch_e "I should probably be going. . ."  
                    call Remove_Girl("Emma")
                call Showering
        "Shower (locked)" if Round <= 30:            
                pass
            
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                "In the showers."
                "Not gonna lie, kinda weird."
                call Wait   
                call EventCalls            
                call Girls_Location 
         
        "Go to the Danger Room" if TravelMode: 
                jump Danger_Room_Entry 
        "Return to Your Room" if TravelMode:  
                jump Player_Room_Entry   
        "Go to Rogue's Room" if TravelMode:  
                jump Rogue_Room_Entry   
        "Go to Kitty's Room" if TravelMode and "met" in K_History:  
                jump Kitty_Room_Entry        
        "Leave [[Go to Campus Square]":
                if TravelMode:
                    jump Campus_Entry
                else:
                    call Worldmap   
    jump Shower_Room

# Shower Room Menu End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Showering(Occupants = 0, Agreed = 0, RogueCount = 0, KittyCount = 0, Showered = 0, Line = 0):
    if R_Loc == "bg showerroom":
            $ Occupants += 1
            $ RogueCount = 1
    if K_Loc == "bg showerroom":        
            $ Occupants += 1
            $ KittyCount = 1
        
    if Occupants:
            ch_p "I'm taking a shower, care to join me?" 
            if RogueCount and "showered" in R_RecentActions:
                if Occupants >1:
                    ch_r "We actually just finished up, so we'll head out."
                else:
                    ch_r "I actually just finished up, so I'll head out."
                $ Showered = 1
            elif KittyCount and "showered" in K_RecentActions:
                    ch_k "I actually just showered, so I'm head out."
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
                        elif Occupants > 1:                     #If Rogue said no
                            ch_k "Yeah, I should head out too."
                        else:                                   #If Rogue isn't there
                            ch_k "I've got to get going."
                            
            if Occupants > Agreed:                    #if either said no     
                # If they're at NameCount = 2 here, they have already agreed.
                
                menu:
                    extend ""
                    "Ok, see you later then.":
                        if RogueCount == 1:
                            ch_r "Yeah, later."
                        if KittyCount == 1:
                            ch_k "Bye!"
                        
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
                    
                    
                    if Line == "spot":      #"Sure you got every spot?"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Fine, I could use another scrub."
                                if KittyCount == 2:
                                    ch_k "Um, me too!"
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "Oh, I guess I could take another pass at it."
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "No, [R_Petname], I think I'm covered."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "Ha, I'm squeeky clean, [K_Petname], see you later."          
                        
                    elif Line == "watch me":  #"Maybe you could stay and watch?"
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Yeah, I guess I do enjoy the view."
                                if KittyCount == 2:
                                    ch_k "Um, me too!"
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "I. . . guess I wouldn't mind that. . ."
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Yeah, I'm gonna pass on that, [R_Petname]."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "[K_Like]I don't need to see that."        
                        
                    elif Line == "watch you": #"But I didn't get to watch."
                            if RogueCount == 2:                                 #Rogue agreed, maybe both
                                ch_r "Well, I don't mind putting on a show."
                                if KittyCount == 2:
                                    ch_k "I- yeah, me neither!"
                            elif KittyCount == 2:                               #Kitty only
                                ch_k "You want to watch me. . ."
                                ch_k "Ok."
                            if RogueCount == 1:                                  #Kitty agreed, Rogue refused
                                ch_r "Keep dreaming, [R_Petname]."
                            if KittyCount == 1:                                  #Rogue agreed, Kitty refused
                                ch_k "[K_Like]no way!"
                                
                    #fix, add jeolousy angle here, if roguelikekitty low, get rid of her. . .
                        
                        
            if RogueCount == 1:     
                    #If Rogue leaves
                    $ Occupants -= 1
                    $ RogueCount = 0
                    call Remove_Girl("Rogue")
            elif RogueCount == 2:                                    
                    #If Rogue Stays
                    call RogueOutfit("nude")
                    $ R_Water = 1
                    $ R_Spunk = []                    
                    $ R_RecentActions.append("showered")                      
                    $ R_DailyActions.append("showered")   
                    
            if KittyCount == 1:     
                    #If Kitty leaves
                    $ Occupants -= 1
                    $ KittyCount = 0
                    call Remove_Girl("Kitty")
            elif KittyCount == 2: 
                    #If Kitty Stays
                    call KittyOutfit("nude")
                    $ K_Water = 1
                    $ K_Spunk = []
                    $ K_RecentActions.append("showered")                      
                    $ K_DailyActions.append("showered")  
                    
            call Seen_First_Peen (0,1) #You get naked
                
            
    $ Line = "You take a quick shower"
    $ Round -= 30
    $ Trigger = 0
    
    if RogueCount and KittyCount:
                    $ Line = "You take a quick shower with Rogue and Kitty."
                    call Shift_Focus("Rogue", "Kitty") 
    elif RogueCount:
                    $ Line = "You take a quick shower with Rogue."
                    call Shift_Focus("Rogue") 
    elif KittyCount:
                    $ Line = "You take a quick shower with Kitty."  
                    call Shift_Focus("Kitty")       
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
    elif KittyCount:
            ch_k "that was. . . nice." 
            
    call RogueOutfit
    call KittyOutfit
    if Round < 1:
        if Current_Time != "Night":
                call Wait
                call Girls_Location
                call Set_The_Scene
        else:
                $ renpy.pop_call()
                "After the shower, it's getting late, you head back to your room."
                jump Player_Room
    return
# End Showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




label Rogue_Caught_Shower:  
    call Shift_Focus("Rogue")     
    $ R_RecentActions.append("showered")                      
    $ R_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ R_Loc = "bg showerroom"
    call RogueOutfit("nude")
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
                call RogueOutfit
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
                    call Set_The_Scene(Dress=0)
                    ch_r "Sorry about that [R_Petname], I was. . . just wrapping up my shower."
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Rogue caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Rogue comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_r "Sorry about that [R_Petname], I was just wrapping up my shower."
            #end "knocked"
    else:                                                                                                       
        #You don't knock    
        $ Line = 0    
        if (D20 >=18 and R_Lust >= 70) or (D20 >=15 and R_Lust >= 80):                                         
                #Caught masturbating in the shower. 
                call RogueFace("sexy")
                $ R_Eyes = "closed"
                $ Rogue_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Rogue under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ R_DailyActions.append("unseen") if "unseen" not in R_DailyActions else R_DailyActions   
                $ R_RecentActions.append("unseen") if "unseen" not in R_RecentActions else R_RecentActions 
                call Rogue_SexAct("masturbate")   
                jump Shower_Room
            
        elif D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call RogueFace("surprised", 1)
                "As you enter the showers, you see Rogue washing up."        
                if not ApprovalCheck("Rogue", 1200) or not R_SeenPussy or not R_SeenChest:
                        $ R_Brows = "angry"     
                        $ R_Over = "towel"
                        "She grabs a towel and covers up."             
                        call RogueFace("angry", 1)
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5) 
                else:
                        if "exhibitionist" in R_Traits:
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, (2*D20)) 
                        else:
                            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, D20)
                        $ R_Brows = "confused"        
                
                call Rogue_First_Topless(1)
                call Rogue_First_Bottomless(1) 
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
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Rogue putting on a towel."        
                if not ApprovalCheck("Rogue", 1100) and (not R_SeenPussy or not R_SeenChest):          
                        call RogueFace("angry")
                        $R_Brows = "confused"
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                else:
                        call RogueFace("sexy")
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
                    
        call RogueFace("sexy")          
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
                call Rogue_First_Topless(1)
                call Rogue_First_Bottomless(1) 
        #end didn't knock
    
    menu:
        ch_r "Well, I should probably get going. . ." 
        "Sure, see you later then.":
                call Remove_Girl("Rogue")
                $ R_Water = 0
                call RogueOutfit
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Rogue", 900):
                $ R_Loc = "bg showerroom"            
                ch_r "Sure, what's up?"
            else:
                ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                ch_r "I'll just see you around later."
                call Remove_Girl("Rogue")
                $ R_Water = 0
                call RogueOutfit               
            
    jump Shower_Room
# End Rogue Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Kitty_Caught_Shower:  
    call Shift_Focus("Kitty")     
    $ K_RecentActions.append("showered")                      
    $ K_DailyActions.append("showered")     
    call Remove_Girl("All")
    $ K_Loc = "bg showerroom"
    call KittyOutfit("nude")
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
                call KittyOutfit
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
                    call Set_The_Scene(Dress=0)
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5)
                    $ Tempmod += 10
            else:                                                                                                   
                    #Kitty caught showering
                    "You hear the rustling of a towel and some knocking around, but after a few seconds Kitty comes to the door."
                    call Set_The_Scene(Dress=0)
                    ch_k "Oh, hey, [K_Petname]. I was just[K_like]showering."
            #end knocked
            
    else:                                                                                                       
        #You don't knock   
        if not K_SeenPussy or not K_SeenChest:
            $ D20 -=5 if D20 > 5 else D20
        $ Line = 0    
        if (D20 >=18 and K_Lust >= 70) or (D20 >=15 and K_Lust >= 80):                                          
                #Caught masturbating in the shower. 
                call KittyFace("sexy")
                $ K_Eyes = "closed"
                $ Kitty_Arms = 2
                call Set_The_Scene(Dress=0)
                $ Count = 0        
                "You see Kitty under the shower, feeling herself up."
                $ Trigger = "masturbation"
                $ K_DailyActions.append("unseen") if "unseen" not in K_DailyActions else K_DailyActions   
                $ K_RecentActions.append("unseen") if "unseen" not in K_RecentActions else K_RecentActions 
                call Kitty_SexAct("masturbate")   
                jump Shower_Room
        
        #change to elif when I fix the above option
        if D20 >= 15:                                                                                         
                #She's just showering and naked
                call Set_The_Scene(Dress=0)                
                call KittyFace("surprised", 1)
                "As you enter the showers, you see Kitty washing up."        
                if not ApprovalCheck("Kitty", 1200) or not K_SeenPussy or not K_SeenChest:
                        $ K_Brows = "angry"     
                        $ K_Over = "towel"
                        "She grabs a towel and covers up."             
                        call KittyFace("angry", 1)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5) 
                else:
                        if "exhibitionist" in K_Traits:
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, (2*D20)) 
                        else:
                            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, D20)
                        $ K_Brows = "confused"        
                
                call Kitty_First_Topless(1)
                call Kitty_First_Bottomless(1) 
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
                call Set_The_Scene(Dress=0)
                "As you enter the showers, you see Kitty putting on a towel."        
                if not ApprovalCheck("Kitty", 1100) and (not K_SeenPussy or not K_SeenChest):          
                        call KittyFace("angry")
                        $K_Brows = "confused"
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                else:
                        call KittyFace("sexy")
                        $K_Brows = "confused"        
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 3)
                menu:
                    ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
                    "Sorry, I should have knocked.":   
                            call KittyFace("smile",1)
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
                            
                            call KittyFace("sexy")       
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
                                call Kitty_First_Topless(1)
                                call Kitty_First_Bottomless(1) 
                #end done showering naked
    
    menu:
        ch_k "I'm done here, see you later?" 
        "Sure, see you later then.":
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty")
                $ K_Water = 0
                call KittyOutfit
                "Kitty heads out."
        "Actually, could you stick around a minute?":
            if ApprovalCheck("Kitty", 900):
                call KittyFace("sexy",1)
                $ K_Loc = "bg showerroom"            
                ch_k "Yeah?"
            else: 
                call KittyFace("perplexed",1)
                ch_k "I'm[K_like]totally exposed here?"
                ch_k "I'm just going to head out."
                hide Kitty_Sprite with easeoutright
                call Remove_Girl("Kitty")
                $ K_Water = 0
                call KittyOutfit               
            
    jump Shower_Room
# End Kitty Caught Shower / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

# end Shower Interface //////////////////////////////////////////////////////////////////////


# Kitty's Room Interface //////////////////////////////////////////////////////////////////////
label Kitty_Room_Entry:
    call Shift_Focus("Kitty")
    $ bg_current = "bg kitty"           
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
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
                    call EventCalls
                    jump Kitty_Room   
    #End if Kitty in Party
    
                    
    if Round >= 10 and K_Loc == "bg kitty" and (D20 >=15 and K_Lust >= 70): #Kitty caught fapping      
                "As you approach her room, you hear soft moaning from inside, and notice that the door is slightly ajar."
                menu:
                    extend ""
                    "Knock politely":
                        $ Line = "knock"
                    "Peek inside":
                        call Set_The_Scene
                        "You see Kitty, eyes closed and stroking herself vigorously."
                        menu:
                            extend ""
                            "Enter Quietly":
                                    call Kitty_Caught_Masturbating
                            "Pull back and knock":                        
                                    $ Line = "knock"
                            "Leave quietly":
                                    "You leave Kitty to her business and slip out."
                                    $ K_Lust = 20
                                    jump Campus_Map
                    "Enter quietly":
                            call Kitty_Caught_Masturbating
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
                        call Set_The_Scene
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
                            call Set_The_Scene
                        
            if Line != "knock" and "Kitty" in Keys: 
                if K_Loc == "bg kitty":
                        if Round <= 10:        
                                if K_RecentActions in ("noentry", "angry"):
                                        call KittyFace("angry")
                                        ch_k "GTFO."    
                                        "Kitty shoves you back into the hall."
                                        jump Campus_Map   
                                if Current_Time == "Night" :    
                                        "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                        jump Campus_Map   
                        elif (D20 >=19 and K_Lust >= 50) or (D20 >=15 and K_Lust >= 70) or (D20 >=10 and K_Lust >= 80):     
                                #Kitty caught fapping
                                call Kitty_Caught_Masturbating 
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                           
                                #Kitty caught changing
                                call Kitty_Caught_Changing
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
                                call Set_The_Scene
                                ch_k "Oh, hey, [K_Petname], I was. . . never mind."
                                $ Tempmod += 10
                        elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                #Kitty caught changing
                                "You hear the rustling of fabric and some knocking around, but after a few seconds Kitty comes to the door."
                                call Set_The_Scene
                                ch_k "Oh, hi [K_Petname], I was[K_like]just getting changed."   
                        elif "angry" in K_RecentActions:
                                ch_k "Nooope."
                                "Kitty pushes you back into the hall and slams the door."
                                $ Trigger = 0
                                jump Campus_Map    
                        else:
                                call Set_The_Scene
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
                    call KittyFace("angry")
                    ch_k "What part of \"GTFO\" was unclear?"  
                    jump Campus_Map    
                    
            elif Current_Time == "Night" and "noentry" in K_RecentActions:
                    ch_k "Scram. I'll see you tomorrow"  
                    jump Campus_Map 
                    
            elif "noentry" in K_RecentActions:
                    call KittyFace("angry")
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
    call EventCalls
    if K_Loc == "bg kitty" and "angry" in K_RecentActions:
        "Kitty pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ Trigger = 0
        jump Player_Room
    if bg_current != "bg kitty":
        jump Misplaced
            
label Kitty_Room:
    $ bg_current = "bg kitty"
    call Set_The_Scene
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    
    call GirlsAngry            
    call Set_The_Scene  
    
# Kitty's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if K_Loc == bg_current:
        $ Line = "You are in Kitty's room. What would you like to do?"
    else:
        $ Line = "You are in Kitty's room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?" if K_Loc == bg_current:                
                    call Kitty_Study
            
        "Sleep." if Current_Time == "Night" and K_Loc == bg_current:
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
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap 
    
    if "angry" in K_RecentActions:
            call KittyFace("angry")
            ch_k "Go. Now."
            "Kitty pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Kitty_Room


label Kitty_Study:                       #study events
            call Shift_Focus("Kitty")
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
                call Kitty_Frisky_Study   
            else:        
                $ P_XP += 5  
            call Wait 
            call Kitty_Leave
            call Rogue_Leave
            return
#End Kitty Study
            
label Kitty_Frisky_Study:
            if D20 > 17 and ApprovalCheck("Kitty", 1000) and K_Blow > 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She unzips you pants and pulls your dick out, stroking it slowly."
                        "She then dives her head under the book, and starts to lick it."        
                        call Kitty_SexAct("blow") 
            elif D20 > 14 and ApprovalCheck("Kitty", 1000) and K_Hand >= 5:
                        "Kitty reaches her hand through your textbook and you can feel it in your lap."
                        "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                        "She unzips you pants and pulls your dick out, stroking it slowly."  
                        call Kitty_SexAct("hand") 
            elif D20 > 10 and (ApprovalCheck("Kitty", 1300) or (K_Mast and ApprovalCheck("Kitty", 1000)))and K_Lust >= 70:
                        "Kitty wriggles against your shoulder, and her hand starts to stroke her crotch."  
                        if "unseen" in K_RecentActions:
                                $ K_RecentActions.remove("unseen")
                        $ Trigger = "masturbation"
                        call Kitty_SexAct("masturbate")      
            elif D20 > 10 and ApprovalCheck("Kitty", 1200) and K_Lust >= 30:
                        "Kitty takes the book from your hand, and sets it aside."
                        if not K_Over and not K_Legs:
                                #if she's mostly naked, cheat
                                call KittyFace("sly")                                
                                ch_k "I was[K_like]thinking about maybe \"strip studying,\". . ." 
                                $ K_Eyes = "down"
                                ch_k "but it would be a pretty short game. . ."
                                $ K_Eyes = "squint"
                                ch_k "Was there something you'd rather do?"                                
                                call Kitty_SexMenu   
                        else:
                                "She then asks if maybe you want to do some \"strip studying?\""
                                call Kitty_Strip_Study
            elif D20 >5 and ApprovalCheck("Kitty", 700) and K_Kissed > 1:
                        "Kitty leans close to you, and presses her lips to yours."         
                        call Kitty_SexAct("kissing")
            elif ApprovalCheck("Kitty", 500):
                        "Kitty squeezes close to you, and you spend the rest of the night cuddling."
            else:
                        return
                
            "Well that was certainly a productive use of your study time. . ."    
            return
    
label Kitty_Caught_Changing:
            call Shift_Focus("Kitty")
            $ D20 = renpy.random.randint(1, 20)
            
            call KittyFace("surprised", 1)
            $ K_Mouth = "kiss"
            if D20 > 17:        
                    #She's naked
                    call KittyOutfit("nude")
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
            call Set_The_Scene
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
                            call KittyFace("surprised")
                            $K_Brows = "angry"  
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -50)
                            if not K_Over or not K_Legs:
                                $ K_Over = "towel"
                                "She grabs a towel and covers up."
                    else:       
                            #She's cool with it, but confused.
                            call KittyFace("surprised", 1)      
                            $K_Brows = "confused"
                            if "exhibitionist" in K_Traits:
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, (2*D20))  
                            else:
                                $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, D20)
                          
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 20)
                    if D20 > 17:
                        call Kitty_First_Topless
                        call Kitty_First_Bottomless(1)
                    elif D20 > 15:
                        call Kitty_First_Bottomless
                    elif D20 > 14:
                        call Kitty_First_Topless
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
                            call KittyFace("angry")
                            $K_Brows = "confused"
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -5)
                    else:
                            call KittyFace("sexy")
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
            call KittyFace("sexy")                
            if ApprovalCheck("Kitty", 750) and K_SeenPussy and K_SeenChest:
                    ch_k "I didn't say that I {i}minded{/i}. . ."                
                    $ K_Over = 0
                    pause 1     
                    call KittyOutfit
                    "She flashes you real quick."  
            else:
                    ch_k "Yeah. . . we wouldn't want any accidents. . ."   
            menu:
                    ch_k "So were you planning on staying?" 
                    "Sure, for a bit.":
                        pass
                    "Actually, I should get going. . .":
                        call KittyOutfit
                        call Worldmap            
            jump Kitty_Room
            return
            #End Kitty Caught Changing
# end Kitty's Room Interface //////////////////////////////////////////////////////////////////////

label Study_Room_Entry:
    $ bg_current = "bg study"           
    call Gym_Clothes
    call Set_The_Scene(Entry = 1)    
    call Taboo_Level
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
    call Set_The_Scene
    if "traveling" in P_RecentActions:
        $ P_RecentActions.remove("traveling")
    call Taboo_Level
    call QuickEvents
    call Checkout(1)
    if Round <= 10:         
            if Current_Time == "Night":                         
                "It's late, you head back to your room."
                jump Player_Room
            else:
                call Wait                 
                call Girls_Location
    
    call GirlsAngry
    call Set_The_Scene      
    
# Study Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Current_Time == "Night":
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"        
        "Chat" if Current_Time == "Night": #fix, open up once sex while in office is fine
                    call Chat
        
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
                            call Wait  
                            call Girls_Location
                            ch_x "Not that I mind the company, but is there something I can do for you?"
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Leave [[Go to Campus Square]":
                    if TravelMode:
                        jump Campus_Entry
                    else:
                        call Worldmap 
    jump Study_Room
    
    
label Study_Room_Explore:
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)    
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + Cnt:
                    $ Line = "book"
            else:
                    "As you search the bookshelf, you accidentally knock one of the books off."
                    "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + Cnt:
                    $ Line = "left"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + Cnt:
                    $ Line = "mid"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if K_Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + Cnt:
                    $ Line = "right"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]": 
                    jump Study_Room
    
    $ D20 = renpy.random.randint(1, 20)
    if not Line:
                "Probably best to get out of here."
                "You slip out and head back to your room."
                jump Player_Room_Entry 
    elif Line == "book":
            if D20 >= 15 and "Well Studied" not in Achievements:            
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
            elif D20 >= 15:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through the books for a few minutes, but don't find anything."
                "It would probably take a more thorough search."            
    elif Line == "left":
            if D20 >= 15:
                "yeah?"
            if D20 >= 15 and "Xavier's photo" not in P_Inventory:            
                "Buried under a pile of documents, you find a printed out photo."
                "It appears to be a selfie of Mystique making out with Xavier."
                "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                "[[Xavier's photo acquired.]"
                $ P_Inventory.append("Xavier's photo")
            elif D20 >= 15:
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