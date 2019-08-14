# Date Night //////////////////////////////////////////////////////////////////////
# Count = price of things
# Count2 = tempmod
    
label Laura_Date_Ask:
    #From the chat menu, you ask Laura to meet you
    call Shift_Focus("Laura")
    if "yesdate" in newgirl["Laura"].DailyActions:  
        call LauraFace("bemused")
        ch_l "I already told you \"ok.\""  
        return         
    if "askeddate" in newgirl["Laura"].DailyActions:  
        call LauraFace("angry")
        ch_l "Back off."  
        return 
    if "stoodup" in newgirl["Laura"].Traits:  
        call Laura_Date_Stood_Up
        $ newgirl["Laura"].DailyActions.append("askeddate")    
        return 
    $ newgirl["Laura"].RecentActions.append("askeddate")   
    $ newgirl["Laura"].DailyActions.append("askeddate")   
    
    if newgirl["Laura"].Break[0] and "ex" in newgirl["Laura"].Traits:
        call LauraFace("angry")
        ch_l "You don't want to be hassling me right now."  
        return     
    if "ex" in newgirl["Laura"].Traits:
        if ApprovalCheck("Laura", 1200):
            call LauraFace("bemused",Brows = "sad" ) 
            ch_l "Well, we did have some fun. . ."            
        else:
            call LauraFace("angry",Eyes = "side")
            ch_l "Nah, pass." 
            return 
       
    if "stoodup" in newgirl["Laura"].History or "deadbeat" in newgirl["Laura"].History: 
        if "stoodup" in newgirl["Laura"].History:
            call LauraFace("angry",Eyes = "side")                
            ch_l "Just don't keep me waiting again." 
        if "deadbeat" in newgirl["Laura"].History:  
            call LauraFace("angry")  
            if "stoodup" in newgirl["Laura"].History:
                ch_l "And last time you just ditched me with the check."   
            else:
                ch_l "Last time you just ditched me with the check."           
        menu:
            extend ""
            "Sorry about that, I'll take care of it this time.":
                    if ApprovalCheck("Laura", 650):
                        call LauraFace("sad")
                        ch_l "Ok, you get another shot, don't screw it up."
                    else:
                        call LauraFace("angry")
                        ch_l "You had your chance, you blew it." 
                        return
            "Yeah, so?":
                    if ApprovalCheck("Laura", 1400):
                        call LauraFace("angry", Mouth = "grimace")
                        ch_l "Hmm. Ok."
                        call LauraFace("bemused")        
                    elif ApprovalCheck("Laura", 500, "O"):
                        call LauraFace("sad")
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)
                        ch_l "If you insist. . ."
                    elif ApprovalCheck("Laura", 650):
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                        ch_l "So I'm not going out with you again."  
                        return 
                    else:
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -10)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -3)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                        ch_l "Dick."  
                        return             
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
    elif ApprovalCheck("Laura", 650):
        call LauraFace("smile")
        ch_l "Sure, see you there."
    elif ApprovalCheck("Laura", 400):                
        call LauraFace("angry",Eyes = "side")
        ch_l "I've got some other stuff to do. . ."
        return
    else:
        call LauraFace("angry")
        ch_l "Nah."
        return 
    
    $ Count = 0
    #She mostly agreed, do you ask for a double date?
    menu:
        "Good, I'll meet you in the campus square." if bg_current != "bg campus" or Current_Time != "Evening": 
                    call LauraFace("smile")
        "Good, let's get going then." if bg_current == "bg campus" and Current_Time == "Evening": 
                    call LauraFace("smile")
        # "And I was thinking of asking. . .": 
        #             menu:
        #                 ch_p "And I was thinking of asking. . ."
        #                 "Rogue along too." if "yesdate" in R_DailyActions or "yesdate" not in P_DailyActions:
        #                             $ Count = newgirl["Laura"].LikeRogue
        #                 "Kitty along too." if "yesdate" in K_DailyActions or "yesdate" not in P_DailyActions:
        #                             $ Count = newgirl["Laura"].LikeKitty
        #                 "Emma along too." if "yesdate" in E_DailyActions or "yesdate" not in P_DailyActions:
        #                             $ Count = newgirl["Laura"].LikeEmma
        #                 "Never mind, probably a bad idea.":  
        #                             call LauraFace("confused")
        #                             ch_l "Um. . ."
        #                             if bg_current != "bg campus": 
        #                                     ch_p "Ok, I'll meet you in the campus square."
    if Count:
        #If you asked about another girl. . .
        if Count >= 600 and ApprovalCheck("Laura", 800, "OI"): #Count is "newgirl["Laura"].LikeX"
            call LauraFace("smile")
            ch_l "Sure, more's the merrier, I guess."                                
        elif Count >= 750:
            call LauraFace("bemused")
            ch_l "Ok. . ."                                
        elif ApprovalCheck("Laura", 1300, "LO"): 
            call LauraFace("sad")
            ch_l "If you insist. . ."             
        else:
            call LauraFace("angry")
            ch_l "I'm out."  
            $ Count = 0
            return
        $ newgirl["Laura"].DailyActions.append("yesdouble") 
        if bg_current != "bg campus" or Current_Time != "Evening": 
                ch_p "Ok, I'll meet you in the campus square."    
        $ Count = 0
    
    if bg_current != "bg campus": 
            ch_l "Right."
    $ newgirl["Laura"].DailyActions.append("yesdate")                  
    $ P_DailyActions.append("yesdate") 
    return


label Laura_Date_Stood_Up:
    # if "stoodup" in newgirl["Laura"].Traits
    if newgirl["Laura"].Loc != bg_current:
            "Laura storms into the room." 
            $ newgirl["Laura"].Loc = bg_current
            call Display_Laura
    else:
            "Laura turns to you." 
    call LauraFace("confused")
    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -10)
    ch_l "We had plans, you didn't show."
    if "stoodup" in newgirl["Laura"].History:
        call LauraFace("angry")
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5)
        ch_l "Again!"
    menu:
            extend ""
            "Oh, sorry about that, slipped my mind.":
                if ApprovalCheck("Laura", 800, "LO") or ApprovalCheck("Laura", 1200):
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 5)
                        ch_l "I'll cut you a break, but don't make me cut you."
                        if "stoodup" in newgirl["Laura"].History:
                            call LauraFace("sad",Eyes="side")
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                            ch_l "Sort out your plans."  
                elif "stoodup" in newgirl["Laura"].History:
                        call LauraFace("sad",Eyes="side")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                        ch_l "Sort out your plans."                    
                else:
                        call LauraFace("angry")
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                        ch_l "You're in the hole on this one."
                
            "I can't imagine that happening, maybe you got the date wrong?":
                if "stoodup" in newgirl["Laura"].History and ApprovalCheck("Laura", 800, "O"):                            
                        call LauraFace("confused")
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 15)
                        ch_l "i don't think. . . I pretty sure. . ."                            
                        call LauraFace("confused",Eyes="side")
                        ch_l "Eh."                                
                elif ApprovalCheck("Laura", 700, "O"):
                        call LauraFace("angry")
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 10)
                        ch_l ". . . I don't think so, but it's possible. . ."     
                elif ApprovalCheck("Laura", 500, "I"):
                        call LauraFace("angry")           
                        $ newgirl["Laura"].RecentActions.append("angry") 
                        $ newgirl["Laura"].DailyActions.append("angry")   
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -10)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 10) 
                        ch_l "Yeah right."
                else:
                        call LauraFace("sad",Eyes="side")    
                        $ newgirl["Laura"].RecentActions.append("angry") 
                        $ newgirl["Laura"].DailyActions.append("angry")  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -5)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                        ch_l "Nope, not buying it."
                        
            "Yeah, I found something better to do.": 
                if ApprovalCheck("Laura", 1200, "LO"):
                        call LauraFace("sad",Eyes="side")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                        if "stoodup" in newgirl["Laura"].History:
                                ch_l "Yeah. . . "
                                ch_l "That sounds like you. . ."                            
                        else:
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 10)
                                ch_l "Huh. . . "
                                ch_l "well don't do it again."
                elif ApprovalCheck("Laura", 800, "LO"):
                        call LauraFace("angry",Eyes="side")
                        $ newgirl["Laura"].RecentActions.append("angry") 
                        $ newgirl["Laura"].DailyActions.append("angry")  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -10)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 20) 
                        ch_l "Maybe I did too."
                else:
                        call LauraFace("angry")
                        $ newgirl["Laura"].RecentActions.append("angry") 
                        $ newgirl["Laura"].DailyActions.append("angry")  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -15)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                        ch_l "Asshole."
                        
    $ newgirl["Laura"].Traits.remove("stoodup") 
    if "stoodup" not in newgirl["Laura"].History:  
            $ newgirl["Laura"].History.append("stoodup") 
            
    call CleartheRoom("All",Check=1)
    if _return >= 3:
        #if the room is full,
        call Remove_Girl("Laura")
        "Laura wanders off." 
    return
    
# End Laura Ask / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Date_Prep:
    #This gets Laura Dressed and ready for Dinner, called by Date_Night
    $ Taboo = 40
    if newgirl["Laura"].Schedule[7]:
        #if she has a date outfit set
        if newgirl["Laura"].Schedule[7] == 2:
            $ newgirl["Laura"].Outfit = "streets"
        elif newgirl["Laura"].Schedule[7] == 3:
            $ newgirl["Laura"].Outfit = "custom1"
        elif newgirl["Laura"].Schedule[7] == 4:
            $ newgirl["Laura"].Outfit = "gym"
        elif newgirl["Laura"].Schedule[7] == 5:
            $ newgirl["Laura"].Outfit = "custom2"
        elif newgirl["Laura"].Schedule[7] == 6:
            $ newgirl["Laura"].Outfit = "custom3"
        else:
            $ newgirl["Laura"].Outfit = "mission"
    else:
        $ Options = ["mission", "streets"]
        $ Options.append("custom1") if newgirl["Laura"].Custom[0] == 2 else Options
        $ Options.append("custom2") if newgirl["Laura"].Custom2[0] == 2 else Options
        $ Options.append("custom3") if newgirl["Laura"].Custom3[0] == 2 else Options
        $ renpy.random.shuffle(Options) 
        $ newgirl["Laura"].Outfit = Options[0]
        $ del Options[:]  
    $ newgirl["Laura"].Loc = "date"
    call LauraOutfit(Changed=1)
    call LauraFace("smile")
    return

# End Laura Prep / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Laura Dinner Menu/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       
label Laura_Dinner(L_Cost = 0):
    #Called by Date Dinner, picked Laura's food
    menu:
        "For Laura you order. . ."
        "Surf and turf. ($20)":
                call LauraFace("sad",Brows = "surprised")
                ch_l "Nice. . ."  
                call LauraFace
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 5)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                $ newgirl["Laura"].Cost = 20
                $ newgirl["Laura"].RecentActions.append("surfturf")
        "Steak. ($15)":  
                call LauraFace("smile")
                ch_l "Rare."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 5)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                $ newgirl["Laura"].Cost = 15
                $ newgirl["Laura"].RecentActions.append("ribeye")
        "Chicken. ($10)":
                call LauraFace("smile")
                ch_l "Yeah, ok."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 3)
                $ newgirl["Laura"].Cost = 10
                $ newgirl["Laura"].RecentActions.append("chicken")
        "Just a salad. ($5)":
                $ newgirl["Laura"].Mouth = "sad"
                $ newgirl["Laura"].Eyes = "sexy"
                $ newgirl["Laura"].Brows = "confused"            
                ch_l "Um. no."  
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -5)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                ch_l "Steak, rare."
                $ newgirl["Laura"].Cost = 15
                $ newgirl["Laura"].RecentActions.append("ribeye")
        "Why don't you choose, Laura?":
                call Date_Bonus("Laura",2)
                call LauraFace("smile")
                ch_l "Thanks. I think I'll have the steak."            
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 7)   
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 2) 
                $ newgirl["Laura"].Cost = 15
                $ newgirl["Laura"].RecentActions.append("ribeye")
                
    if Party[0] == "Laura":
        $ Prime_Cost = newgirl["Laura"].Cost
    else:
        $ Second_Cost = newgirl["Laura"].Cost
    call Date_Bonus("Laura",newgirl["Laura"].Cost)
    return
# End Laura Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /          

    
# Start Laura Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Dinner_Sex(Previous=0,L_Bonus=0,Options=["nothing"]):
    #Called by Dinner Sex, if Laura is chosen.
    
    if Party[0] == "Laura":
        $ L_Bonus = Prime_Bonus + Prime_Cost
    else:
        $ L_Bonus = Second_Bonus + Second_Cost
        
    if newgirl["Laura"].Anal and ApprovalCheck("Laura", 1500) and L_Bonus >=15: 
        $ Options.append("anal")        
    if newgirl["Laura"].Sex and ApprovalCheck("Laura", 1500) and L_Bonus >=10:
        $ Options.append("sex")
    if newgirl["Laura"].Blow and ApprovalCheck("Laura", 1300) and L_Bonus >=10:
        $ Options.append("blow")      
    if newgirl["Laura"].Hand and ApprovalCheck("Laura", 1000) and L_Bonus >=10:
        $ Options.append("hand")
    if newgirl["Laura"].FondleP and ApprovalCheck("Laura", 1000) and L_Bonus >=10:
        $ Options.append("pussy")
    if ApprovalCheck("Laura", 1000) and L_Bonus >=10:
        $ Options.append("foot")
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Kitty" in Previous:
        $ Previous = "Kitty"
    else:
        $ Previous = 0
        
    $ renpy.random.shuffle(Options) 
    
    call LauraFace("sexy")
    if Options[0] == "nothing":
        pass
    elif Options[0] == "anal":        
        "Halfway through the meal, Laura gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                call LauraFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -10)
                call Date_Bonus("Laura",-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass while [Previous] feels you both up."
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes taking it up the ass."
                if _return == 3:
                    "[Previous] stares daggers at you both as you return to the table."
                    call Date_Bonus(Previous,-10)
                ch_l "Worth it."  
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 9)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3)
                $ newgirl["Laura"].SeenPeen += 1
                $ newgirl["Laura"].Anal += 1
                $ P_Semen -= 1
                $ newgirl["Laura"].RecentActions.append("anal")    
                $ newgirl["Laura"].RecentActions.append("dinnersex")                    
                $ newgirl["Laura"].DailyActions.append("anal") 
    elif Options[0] == "sex":        
        "Halfway through the meal, Laura gets a sly look on her face." 
        "She nods her head suggestively towards the restrooms, and then excuses herself."
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                call LauraFace("sadside", 2)
                "You wait a few minutes until she returns, seemingly a bit annoyed at you."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -10)
                call Date_Bonus("Laura",-5)
        else:
                if _return == 1: #other girl is fine
                        "A few seconds later, you and [Previous] follow her and she drags you both inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw while [Previous] feels you both up."
                else:
                        "A few seconds later, you follow her and she drags you inside, locking the door behind you." 
                        "She spends the next several minutes fucking you raw."
                if _return == 3:
                    "[Previous] stares daggers at you both as you return to the table."
                    call Date_Bonus(Previous,-10)
                ch_l "Sorry about the scratches."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 8)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                $ newgirl["Laura"].SeenPeen += 1
                $ newgirl["Laura"].Sex += 1
                $ P_Semen -= 1            
                $ newgirl["Laura"].RecentActions.append("sex")   
                $ newgirl["Laura"].RecentActions.append("dinnersex")                    
                $ newgirl["Laura"].DailyActions.append("sex") 
    elif Options[0] == "blow":
        "Halfway through the meal, Laura gets a sly look on her face, then knocks her fork off the table."
        "She ducks under the table after it, and unzips your pants." 
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                call LauraFace("sadside", 2)
                "You zip them back up and shoo her away. She gets back up from under the table."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -5)
                call Date_Bonus("Laura",-3)
        else:
                if _return == 1: #other girl is fine
                        "[Previous] shifts closer and wraps one arm around you, the other hand caressing Laura's cheek."
                        "Laura then proceeds to blow you for several minutes until you cum."
                elif _return == 2: #other girl is fine
                        "She then proceeds to blow you for several minutes until you cum, while [Previous] pretends to be occupied."
                else: 
                        "She then proceeds to blow you for several minutes until you cum."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 6)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                $ newgirl["Laura"].RecentActions.append("blow")   
                $ newgirl["Laura"].RecentActions.append("dinnersex")                    
                $ newgirl["Laura"].DailyActions.append("blow") 
                if newgirl["Laura"].Swallow:
                    "Laura wipes her mouth as she climbs out from under the table."
                    ch_l "Yum. . ."            
                    $ newgirl["Laura"].Addict -= 20
                    $ newgirl["Laura"].Swallow += 1  
                    $ newgirl["Laura"].RecentActions.append("swallow")                      
                    $ newgirl["Laura"].DailyActions.append("swallow")       
                else:
                    "Laura grabs the napkin off your lap and uses it to collect the jiz."
                    ch_l "Sorry about the mess."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 4)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                $ newgirl["Laura"].SeenPeen += 1
                $ newgirl["Laura"].Blow += 1
                $ P_Semen -= 1
                if _return == 3:
                    "[Previous] stares daggers at you both as she crawls out from under the table."  
                    call Date_Bonus(Previous,-10)
    elif Options[0] == "hand":
        "Halfway through the meal, Laura gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                call LauraFace("sadside", 2)
                "She tries to unzip your pants under the table, but you shoo her away."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -5)
                call Date_Bonus("Laura",-2)
        else:
                if _return == 1: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "On the other side, [Previous] also reaches down and gets into the action."
                        "They continue stroking it until you cum into the napkin."
                elif _return == 2: #other girl is fine
                        "She unzips your pants under the table, and proceeds to caress your cock, while [Previous] pretends to be occupied."
                        "She continues stroking it until you cum into the napkin."
                else: 
                        "She unzips your pants under the table, and proceeds to caress your cock."
                        "She continues stroking it until you cum into the napkin."
                ch_l "Sorry about the mess."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 4)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                $ newgirl["Laura"].Hand += 1
                $ P_Semen -= 1
                $ newgirl["Laura"].RecentActions.append("hand")     
                $ newgirl["Laura"].RecentActions.append("dinnersex")                  
                $ newgirl["Laura"].DailyActions.append("hand") 
                if _return == 3:
                    "[Previous] stares daggers at you both from across the table."
                    call Date_Bonus(Previous,-5)
    elif Options[0] == "pussy":
        "Halfway through the meal, Laura gets a sly look on her face, then shifts her chair around next to yours."
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                if newgirl["Laura"].Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [newgirl[Laura].Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                call LauraFace("sadside", 2)
                "With a glance at [Previous], you jerk your hand away."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -5)
                call Date_Bonus("Laura",-3)
        else:
                if newgirl["Laura"].Legs:
                    "She takes your hand and pulls it over to her crotch, shoving it under her [newgirl[Laura].Legs]."
                else:
                    "She takes your hand and shoves it into her crotch."
                "You can feel that she's warm as a furnace."
                if _return == 1: #other girl is fine
                        "On the other side, [Previous] also reaches down and gets into the action."
                        "You both stroke her pussy for several minutes, until finally she shudders in orgasm." 
                        "You slowly pulls your hands free with a sly smile."
                else: 
                    "You stroke her pussy for several minutes, until finally she shudders in orgasm." 
                    "You slowly pulls your hand free with a sly smile."
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                ch_l "Oof, that was nice."
                if _return == 1:
                    ch_l "You too, [Previous]."
                    $ newgirl["Laura"].Les += 1
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 5)            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2)
                $ newgirl["Laura"].FondleP += 1
                $ newgirl["Laura"].Org += 1
                $ newgirl["Laura"].RecentActions.append("fondle pussy") 
                $ newgirl["Laura"].RecentActions.append("dinnersex")                      
                $ newgirl["Laura"].DailyActions.append("fondle pussy") 
    elif Options[0] == "foot":
        "Halfway through the meal, Laura gets a sly look on her face, then shifts a bit lower in her seat."
        "You suddenly feel her foot in your lap, gently caressing your cock."
        call Date_Sex_Break("Laura",Previous)
        if _return == 4: #you refused
                call LauraFace("sadside", 2)
                "You shift uncomfortably and push her foot away."
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, -3)
                call Date_Bonus("Laura",-1)
        else:
                $ P_Focus = Statupdate("Emma", "Focus", P_Focus, 60, 10)
                if _return == 1: #other girl is fine
                        "[Previous] decides to join in the fun and adds her foot to the mix."
                        $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 60, 5)
                if _return == 3:
                    call Date_Bonus(Previous,-3)
                "After several minutes of this, she pulls back."
                ch_l "I've got plans for tonight, [newgirl[Laura].Petname]."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3)
                $ newgirl["Laura"].RecentActions.append("dinnersex") 
    
    call LauraFace(B = 0)
    return    
# End Laura Dinner Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Laura Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Movie_Sex(Previous=0,L_Bonus=0, Options=["nothing"]):
    # Called by Movie_Sex if Laura is chosen
    if Party[0] == "Laura":
        $ L_Bonus = Prime_Bonus
    else:
        $ L_Bonus = Second_Bonus
    
    if "horror" in P_RecentActions:
        $ L_Bonus += 20
    
    if "Rogue" in Previous:
        $ Previous = "Rogue"
    elif "Emma" in Previous:
        $ Previous = "Emma"
    elif "Kitty" in Previous:
        $ Previous = "Kitty"
    else:
        $ Previous = 0
        
    if ApprovalCheck("Laura", 500, Bonus=(10*L_Bonus)):
        call LauraFace("kiss", 1)
        if "romcom" in P_RecentActions: 
            "Halfway through the movie, inspired by the action on screen, Laura turns to you and starts to make out with you."
        elif "action" in P_RecentActions:        
            "Halfway through the movie, adrenaline pumping from the action on screen, Laura turns to you and starts to make out with you."
        elif "horror" in P_RecentActions:  
            "Halfway through the movie, bored by the \"tension\" on screen, Laura turns to you and starts to make out with you."
        elif "drama" in P_RecentActions:   
            "Halfway through the movie, Laura turns to you with a shrug and starts to make out with you."
        $ newgirl["Laura"].RecentActions.append("kissing") 
        $ newgirl["Laura"].RecentActions.append("moviesex")                       
        $ newgirl["Laura"].DailyActions.append("kissing")      
        call Date_Sex_Break("Laura",Previous)   
        if _return == 4:
                #the other girl stops you
                "You settle back into your seats and watch the rest of the film."
                return
        elif _return == 1:
                #the other girl joins in. . .
                "[Previous] also leans in and begins kissing the both of you."
        elif _return == 3:
                #the other girl is mad. . .
                "You get back to it, [Previous] settles back into her seat with a glare."
            
    
        if newgirl["Laura"].Anal and ApprovalCheck("Laura", 2000, Bonus=(10*L_Bonus)) and PantsNum("Laura") < 5:
                    call LauraFace("sexy", 1)
                    if newgirl["Laura"].Panties:
                        "As you make out, Laura reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Laura reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Laura",Previous,1)
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_l "I wonder if she's coming back."                
                    "She gingerly squeezes your cock into her ass and begins to grind up and down, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Laura's pussy."
                    if newgirl["Laura"].CreamA:
                            if newgirl["Laura"].Panties:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She pulls her panties back up and returns to her seat."
                            else:
                                "After several minutes of this, you can't take it anymore and come inside her."
                                "She wipes off as best she can and shifts back into her seat."
                            $ newgirl["Laura"].CreamA += 1
                            $ newgirl["Laura"].RecentActions.append("creampie anal")                      
                            $ newgirl["Laura"].DailyActions.append("creampie anal") 
                    else:
                            "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                            if newgirl["Laura"].Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:
                                    "You cum into the popcorn bucket, which she then finishes off."
                                $ newgirl["Laura"].Addict -= 20
                                $ newgirl["Laura"].Swallow += 1
                                $ newgirl["Laura"].Spunk.append("mouth")                          
                                $ newgirl["Laura"].RecentActions.append("swallowed")                      
                                $ newgirl["Laura"].DailyActions.append("swallowed") 
                            else:
                                "You cum into the popcorn bucket, which she slides under the seat."
                    ch_l "Hmm, I'm stuffed."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 3)
                    $ newgirl["Laura"].SeenPeen += 1
                    $ newgirl["Laura"].Anal += 1
                    $ P_Semen -= 1
                    $ newgirl["Laura"].RecentActions.append("anal")                      
                    $ newgirl["Laura"].DailyActions.append("anal")  
        elif newgirl["Laura"].Sex and ApprovalCheck("Laura", 2000, Bonus=(10*L_Bonus)) and PantsNum("Laura") < 5:
                    call LauraFace("sexy", 1)
                    if newgirl["Laura"].Panties:
                        "As you make out, Laura reaches down and undoes your fly. She pulls her panties aside and shifts into your lap."
                    else:
                        "As you make out, Laura reaches down and undoes your fly. She hikes her skirt up a bit and shifts into your lap."
                    call Date_Sex_Break("Laura",Previous,1)                    
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_l "I wonder if she's coming back."                
                    "Seconds later, she's slowly rocking on your cock, quietly enough that the other patrons don't seem to notice."
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over and toys with Laura's pussy."
                    if newgirl["Laura"].CreamP:
                        if newgirl["Laura"].Panties:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She pulls her panties up over her dripping slit and returns to her seat."
                        else:
                            "After several minutes of this, you can't take it anymore and come inside her."
                            "She wipes up as best she can and returns to her seat."
                        $ newgirl["Laura"].CreamP += 1
                        $ newgirl["Laura"].RecentActions.append("creampie sex")                      
                        $ newgirl["Laura"].DailyActions.append("creampie sex") 
                    else:
                        "After several minutes of this, she pulls out and shifts back into her seat, finishing you off with her hand."
                        if newgirl["Laura"].Swallow:
                                if 0 < _return < 3: #if 1 or 2
                                    "You cum into the popcorn bucket, which she and [Previous] then finish off together."
                                else:                                    
                                    "You cum into the popcorn bucket, which she then finishes off."   
                                $ newgirl["Laura"].Spunk.append("mouth")   
                                $ newgirl["Laura"].Addict -= 20
                                $ newgirl["Laura"].Swallow += 1
                                $ newgirl["Laura"].RecentActions.append("swallowed")                      
                                $ newgirl["Laura"].DailyActions.append("swallowed") 
                        else:
                                "You cum into the popcorn bucket, which she slides under the seat."
                    ch_l "Hmm, I'm stuffed."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 4)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 3)
                    $ newgirl["Laura"].SeenPeen += 1
                    $ newgirl["Laura"].Sex += 1
                    $ P_Semen -= 1
                    $ newgirl["Laura"].RecentActions.append("sex")                      
                    $ newgirl["Laura"].DailyActions.append("sex")             
        elif newgirl["Laura"].Blow and ApprovalCheck("Laura", 1300, Bonus=(10*L_Bonus)):
                    call LauraFace("sucking", 1)
                    "As you make out, Laura reaches down and undoes your fly. She then bends down and wraps her lips around it."
                    call Date_Sex_Break("Laura",Previous,1)                
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_l "I wonder if she's coming back."                
                    if _return == 1:
                            #the other girl joins you. . .
                            "[Previous] also leans over joins Laura at licking your cock."
                            "They take turns sucking on it contentedly for several minutes before you finally cum."   
                    else:
                            "She sucks on it contentedly for several minutes before you finally cum."            
                    $ newgirl["Laura"].Spunk.append("mouth")  
                    if newgirl["Laura"].Swallow:
                        "Laura wipes her mouth as she shifts back into her seat and washes it down with some soda."
                        call LauraFace("sexy")
                        ch_l "Mmmm, that hit the spot. . ."
                        $ newgirl["Laura"].Addict -= 20
                        $ newgirl["Laura"].Swallow += 1
                        $ newgirl["Laura"].RecentActions.append("swallowed")                      
                        $ newgirl["Laura"].DailyActions.append("swallowed") 
                    else:
                        "You cum into the popcorn bucket, which she slides under the seat."
                        ch_l "Kinda left a mess there."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                    $ newgirl["Laura"].SeenPeen += 1
                    $ newgirl["Laura"].Blow += 1
                    $ P_Semen -= 1
                    $ newgirl["Laura"].RecentActions.append("blow")                      
                    $ newgirl["Laura"].DailyActions.append("blow") 
        elif newgirl["Laura"].Hand and ApprovalCheck("Laura", 1000, Bonus=(10*Count2)):
                    call LauraFace("sexy")
                    "As you make out, Laura reaches down and pulls out your cock." 
                    call Date_Sex_Break("Laura",Previous,1)             
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_l "I wonder if she's coming back."   
                            "She then leans over and begins to stroke your cock." 
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "She then leans over and begins to stroke your cock."
                            "[Previous] leans in and joins her, and they share a smile."
                    else:
                            "She then leans over and begins to stroke it." 
                    call LauraFace("surprised")
                    if newgirl["Laura"].FondleP:
                        if _return == 1: 
                                #the other girl joins in. . .
                                "You also reach down and begin stroking their pussies."
                        else:
                            if newgirl["Laura"].Legs:
                                    "You also lean over, reach into her [newgirl[Laura].Legs], and begin to stroke her pussy."
                            elif newgirl["Laura"].Hose:
                                    "You also lean in, reach under her [newgirl[Laura].Hose], and begin to stroke her pussy."
                            elif newgirl["Laura"].Panties:
                                    "You also lean in, reach under her panties, and begin to stroke her pussy."
                            else:
                                    "You also lean over, notice she isn't wearing anything down there, and begin to stroke her pussy."
                    call LauraFace("sexy", 1, Eyes = "closed")
                    if newgirl["Laura"].FondleP:
                        if _return == 1: 
                            "After several minutes of this, Laura and [Previous] shudder in orgasm, which sets you off as well."
                        else:
                            "After several minutes of this, she shudders in orgasm, which sets you off as well."
                        "Laura catches the jiz in the popcorn bucket."
                    $ newgirl["Laura"].Eyes = "sexy"
                    if newgirl["Laura"].Swallow:
                            if 0 < _return < 3: #if 1 or 2
                                "The girls finish off the remaining popcorn with a grin."    
                            else:
                                "She finishes off the remaining popcorn with a grin."                    
                            $ newgirl["Laura"].Spunk.append("mouth")  
                            ch_l "I should order that topping next time."     
                            $ newgirl["Laura"].Addict -= 20
                            $ newgirl["Laura"].Swallow += 1
                            $ newgirl["Laura"].RecentActions.append("swallowed")                      
                            $ newgirl["Laura"].DailyActions.append("swallowed") 
                    else:
                            "You cum into the popcorn bucket, which she slides under the seat."
                            ch_l "Kinda left a mess there."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                    $ newgirl["Laura"].FondleP += 1
                    $ newgirl["Laura"].Org += 1        
                    $ newgirl["Laura"].Hand += 1
                    $ P_Semen -= 1
                    $ newgirl["Laura"].RecentActions.append("hand")                      
                    $ newgirl["Laura"].DailyActions.append("hand") 
        elif newgirl["Laura"].FondleP and ApprovalCheck("Laura", 900, Bonus=(10*L_Bonus)):
                    call LauraFace("sexy")                    
                    if newgirl["Laura"].Legs:
                            "As you make out, Laura grabs your hand and shoves it down her [newgirl[Laura].Legs]."
                    elif newgirl["Laura"].Hose:
                            "As you make out, Laura grabs your hand and shoves it down her [newgirl[Laura].Hose]."
                    elif newgirl["Laura"].Panties:
                            "As you make out, Laura grabs your hand and shoves it down her panties."
                    else:
                            "As you make out, Laura grabs your hand and shoves it between her legs."
                    call Date_Sex_Break("Laura",Previous,1)
                    $ newgirl["Laura"].Eyes = "closed"
                    if _return == 3:
                            #the other girl stormed out. . .
                            ch_l "I wonder if she's coming back." 
                            "You get back to work."
                    elif _return == 1: 
                            #the other girl joins in. . .
                            "[Previous] leans in and begins to fondle her breasts as well."   
                    "After several minutes of this, she shudders in orgasm and leans back with a contented sigh."
                    $ newgirl["Laura"].Eyes = "sexy"
                    ch_l "Hmm, that was great, [newgirl[Laura].Petname]."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                    $ newgirl["Laura"].FondleP += 1
                    $ newgirl["Laura"].Org += 1    
                    $ newgirl["Laura"].RecentActions.append("fondle pussy")                      
                    $ newgirl["Laura"].DailyActions.append("fondle pussy") 
        elif ApprovalCheck("Laura", 1200, Bonus=(5*L_Bonus)) and newgirl["Laura"].Panties:
                    call LauraFace("sexy")
                    "After making out for a few minutes, Laura gets a sly look on her face and reaches into her pocket."
                    "After a second, she hands you a cloth lump, apparently her panties." 
                    $ newgirl["Laura"].DailyActions.append("pantyless") 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                    $ newgirl["Laura"].Panties = 0
                    ch_l "Could you hold onto those for later?"
        elif ApprovalCheck("Laura", 1200, Bonus=(5*L_Bonus)):
                    call LauraFace("sexy")
                    "After making out for a few minutes, Laura gets a sly look on her face, then shifts a bit lower in her seat."
                    if PantsNum("Laura") > 5:
                        "Looking down, you notice she's pulled down her pants enough that you can see her bare pussy, lit by the movie screen."  
                    elif newgirl["Laura"].Legs == "shorts":
                        "Looking down, you notice she's pulled down her shorts enough that you can see her bare pussy, lit by the movie screen."   
                    else:
                        "Looking down, you notice she's hiked up her skirt enough that you can see her bare pussy, lit by the movie screen."            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                    call Laura_First_Bottomless(1)
                    ch_l "Just a heads up. . ."
    #End Laura movie sex options
    call LauraOutfit
    return
# End Laura Movie Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
# Start Laura Date End/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Date_End:   
    #Called if you end up with Laura at the end of the date
    if bg_current != "bg player":
            #skips this portion if you are in the player's room already
            menu:
                "Take Laura back to her room?":
                    pass
                "Just leave and head back to yours.":
                    call Date_Ditched
                    jump Date_Over    
            
            #until her room is ready. . .
            ch_l "You know, my room's. . . a mess. Let's head for yours."
            
            $ bg_current = "bg player"
            $ newgirl["Laura"].Loc = "bg player"
            if "Rogue" in Party:
                $ R_Loc = "bg player"
            if "Emma" in Party:
                $ E_Loc = "bg player"
            if "Kitty" in Party:
                $ K_Loc = "bg player"
                
#            $ bg_current = "bg laura"
#            $ newgirl["Laura"].Loc = "bg laura"
#            if "Rogue" in Party:
#                $ R_Loc = "bg laura"
#            if "Emma" in Party:
#                $ E_Loc = "bg laura"
#            if "Kitty" in Party:
#                $ K_Loc = "bg laura"
            call Set_The_Scene(Dress=0)
            call Taboo_Level    
    
    if Party[0] == "Laura":
        $ Count = Prime_Bonus
        $ Count2 = Party[1] #the other girl
    else:
        $ Count = Second_Bonus
        $ Count2 = Party[0] #the other girl
            
    if bg_current != "bg player":
        "You walk Laura back to her room."
    if Count < 0:      
        call LauraFace("angry", 0,Eyes = "side")
        ch_l "That was a real shitshow, [Playername]."
        if bg_current == "bg player":
                "She storms off down the hall."
        else:
                "She slams the door on you."
        call Set_The_Scene(Entry=1,Dress=0)
        $ Count = 0
        call Laura_Date_Over(0)
        jump Date_End
    else: 
        if Count > 20:
            call LauraFace("sexy", 1)
            if bg_current == "bg player":
                    ch_l "I had fun, [newgirl[Laura].Petname]. We done, or. . ."    
            else:
                    ch_l "I had fun, [newgirl[Laura].Petname]. We done, or . . ."             
        else:
            call LauraFace("smile", 1)
            ch_l "I had fun, [newgirl[Laura].Petname]. Talk to you later."
        
        $ newgirl["Laura"].Date += 1
        menu:
            extend ""
            "Could I get a good night kiss?":
                if ApprovalCheck("Laura", 600, Bonus=(10*Count)):
                    $ newgirl["Laura"].Mouth = "smile"
                    ch_l "Well if you insist. . ."
                    call Date_Sex_Break("Laura",Count2,2)
                    $ MultiAction = 0
                    call Laura_KissPrep 
                    $ MultiAction = 1
                if ApprovalCheck("Laura", 900, Bonus=(10*Count)):
                    call LauraFace("sexy", 1)
                    ch_l "Hmmm . . ."   
                    if bg_current == "bg player":
                            ch_l "Could I. . . borrow you for a minute?"
                    else:
                            ch_l "Could I. . . borrow you for a minute?"
                    call Date_Sex_Break("Laura",Count2)
                    if _return == 4:
                        if bg_current == "bg player":
                                ch_p "You should get going, sorry."
                        else:
                                ch_p "I should get going, sorry."
                        call Laura_Date_Over(0)
                        jump Date_End                  

                else:
                    call LauraFace("smile", 1)
                    ch_l "That was nice, talk to you later."
                    $ Count = 0
                    call Laura_Date_Over(0)
                    jump Date_End
                    
            "Want to have a little fun first?" if bg_current == "bg player":
                if ApprovalCheck("Laura", 800, Bonus=(10*Count)):
                    call LauraFace("sexy", 1)
                    ch_l "I guess, sure."
                    call Date_Sex_Break("Laura",Count2)
                    if _return == 4:
                        ch_p "You should get going, sorry."  
                        call Laura_Date_Over(0)
                        jump Date_End  
            "Could I come in for a bit?" if bg_current != "bg player":
                if ApprovalCheck("Laura", 800, Bonus=(10*Count)):
                    call LauraFace("sexy", 1)
                    ch_l "I guess, sure."
                    call Date_Sex_Break("Laura",Count2)
                    if _return == 4:
                        ch_p "I should get going, sorry."  
                        call Laura_Date_Over(0)
                        jump Date_End                   
                    
            "Ok, good night then.":
                call LauraFace("confused", 1)
                if bg_current == "bg player":
                        "Laura looks a little confused, but she heads out."
                else:
                        "Laura looks a little confused, but you head out."
                call Laura_Date_Over(0)
                jump Date_End
                
    # Laura lets you into her room:
    if bg_current != "bg player":
            $ bg_current = "bg laura"  
    call Set_The_Scene(Dress=0)
    call Taboo_Level 
    call LauraFace("sexy", 1)
    ch_l "So. . . after a date like that. . . "
    $ P_DailyActions.append("post date") 
    $ renpy.pop_call() #removes call to date
    $ renpy.pop_call() #removes call to Events
    call Laura_SexMenu                       # You have what sex you can get away with
    
    if "angry" in newgirl["Laura"].RecentActions:       
        if bg_current == "bg player":  
                "She storms off down the hall."
        else:
                "Laura shoves you out into the hall. You head back to your room."
                $ bg_current = "bg player"
        $ Count = 0
        call Remove_Girl("All",0,1)
        $ P_DailyActions.append("post date") 
        jump Player_Room
             
    call Sleepover("Laura")      
    jump Misplaced

# End Laura Date End / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

    
    
# Start Laura Date Over / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Laura_Date_Over(Angry=1):
    # Called if Laura is pissed and leaves
    if Angry:
            $ newgirl["Laura"].RecentActions.append("angry") 
            $ newgirl["Laura"].DailyActions.append("angry")  
            call LauraFace("angry")
            ch_l "What was that?" 
            ch_l "Eat a dick." 
            "Laura storms out." 
    if "study" in P_RecentActions:        
            call Remove_Girl("Laura")
            return
    if Party[0] == "Laura":
            $ Prime_Bonus = Second_Bonus
            $ Prime_Cost = Second_Cost
            $ Second_Cost = 0    
    $ Party.remove("Laura")
    $ Party.append(0)    
    call Remove_Girl("Laura")
    call Shift_Focus(Party[0])        
    return
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
