
# star Emma chat interface
label Emma_Chat:
    call EmmaFace from _call_EmmaFace_550    
    call Shift_Focus("Emma") from _call_Shift_Focus_155
    call Change_Focus("Emma") from _call_Change_Focus_11
    
    if E_Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in E_RecentActions:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in E_RecentActions:
                ch_e "I would not press my luck if I were you."
                return

    if E_Loc == bg_current:
            ch_e "What was it you wanted to discuss, [E_Petname]?"
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if E_Loc != bg_current:
                    if Room_Full():
                        "It's already pretty crowded here."
                        menu:
                            "Did you want to ask someone to leave?"
                            "Rogue" if R_Loc == bg_current:
                                call Rogue_Dismissed from _call_Rogue_Dismissed_2
                            "Kitty" if K_Loc == bg_current:
                                call Kitty_Dismissed from _call_Kitty_Dismissed_2
                    else:
                        call Emma_Summon from _call_Emma_Summon  

        "Send a dick pic." if E_Loc != bg_current:

                    "You send Emma a picture of your dick"

                    if E_Loc == "bg teacher" and bg_current == "bg classroom":
                            $ E_Eyes = "down"
                            "Emma looks down at her phone for a while"
                    if ApprovalCheck("Emma", 1200, TabM = 3):
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                call EmmaFaceSpecial("sly", 1) from _call_EmmaFaceSpecial_5
                                "She then, scans the class with her eyes, until she finds you"
                                call EmmaFaceSpecial("sexy", 1) from _call_EmmaFaceSpecial_6
                                "Emma gives you a sexy smile and starts typing something on her phone"
                                #call EmmaFace("surprised", 1) 
                                $ E_Eyes = "down"
                            ch_e "Hard for me again my little student?"
                            call EmmaFace("sly", 1) from _call_EmmaFace_551
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                if "exhibitionist" in E_Traits:
                                    ch_e "Thinking about it in front of everyone is making me so wet"
                                    $ E_Wet = 1
                                else:
                                    ch_e "And you should be paying attention to class, [E_Petname]"
                            #call Emma_Sent_Selfie(1)
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 8)
                    elif ApprovalCheck("Emma", 500, "I", TabM=2):
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                call EmmaFaceSpecial("smile", 1) from _call_EmmaFaceSpecial_7 
                                $ E_Eyes = "down"
                                "Emma glances at it, but just smiles in amusement."
                                call EmmaFaceSpecial("sly", 1) from _call_EmmaFaceSpecial_8
                                "She then, scans the class with her eyes, until she finds you"
                                "She looks down at her phone and starts typing something"
                            $ E_Eyes = "down"
                            ch_e "wow [E_Petname]"            
                            call EmmaFaceSpecial("sly", 1) from _call_EmmaFaceSpecial_9 
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                ch_e "Should you really be sending dick pics during class, [E_Petname]?"
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 10)
                    else:
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                call EmmaFaceSpecial("angry", 1) from _call_EmmaFaceSpecial_10 
                                $ E_Eyes = "down"
                                "Emma glances down at your cock with a scowl."  
                                call EmmaFaceSpecial("angry", 1) from _call_EmmaFaceSpecial_11
                                "She then, scans the class with her eyes, until she finds you"      
                                "She looks down at her phone and starts typing something"
                            $ E_Eyes = "down"
                            ch_e "You shouldn't be sending these kind of texts to your teacher [E_Petname]"
                            call EmmaFaceSpecial("sly", 1) from _call_EmmaFaceSpecial_12 
                            if E_Loc == "bg teacher" and bg_current == "bg classroom":
                                ch_e "Specially not during classes"
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry") 

        "Ask Emma to leave" if E_Loc == bg_current:
                    call Emma_Dismissed from _call_Emma_Dismissed_2    
                    return
        
        "Flirt with her." if not E_Chat[5]:
                    call Emma_Flirt from _call_Emma_Flirt               
        "Flirt with her. (locked)" if E_Chat[5]:  
                    pass

        "Show me the plug." if E_Plugged:

                    if ApprovalCheck("Emma", 1450, TabM = 3) or ApprovalCheck("Emma", 800, "O") or "exhibitionist" in E_Traits: # 145, 160, 175, Taboo -160(355)
                        call EmmaFaceSpecial("sexy",1) from _call_EmmaFaceSpecial_13
                        ch_e "Ok [E_Petname]."
                        call Emma_Doggy_Launch("plug") from _call_Emma_Doggy_Launch_1
                        "Emma points her ass towards you."
                        #if E_Legs == "skirt" or E_Legs == "skirtshort" or E_Legs == "cheerleader skirt" or E_Legs == "cheerleader skirtshort":
                        if E_Legs:
                            $ E_Upskirt = 1
                            # if E_Legs == "orange skirt" or E_Legs == "black skirt" or E_Legs == "white skirt":
                            #     "Lifts up her skirt."
                            # else:
                            #     "She pulls down her [E_Legs]"
                            "She pulls down her [E_Legs]"
                            pause .1
                            #if E_Hose == "tights":
                            #    $ Temp_E_Hose = E_Hose            
                            #    $ E_Hose = 0
                            #    "And pulls down her tights"
                            #    pause .1
                            #if E_Panties and E_Panties != "lace panties" and E_Panties != "black panties":
                            #    $ E_PantiesDown = 1
                            #    "And pulls down her [E_Panties]"
                            #    pause .1
                            ch_e "There, are you happy, darling?"
                            call Emma_Show_Plug from _call_Emma_Show_Plug
                            #$ E_PantiesDown = 0
                            #pause .1
                            #if Temp_E_Hose:
                            #    $ E_Hose = Temp_E_Hose
                            #    pause .1
                            $ E_Upskirt = 0
                            pause
                        #elif E_Legs == "pants":
                        #    #$ Temp_E_Legs = E_Legs            
                        #    $ E_Upskirt = 1
                        #    #$ E_Legs = 0
                        #    "Emma pulls down her pants."  
                        #    pause .1
                        #    if E_Panties and E_Panties != "lace panties" and E_Panties != "black panties":
                        #        $ E_PantiesDown = 1
                        #        "And pulls down her [E_Panties]"
                        #        pause .1
                        #    ch_e "There, you happy?"
                        #    pause .1
                        #    call Emma_Show_Plug
                        #    $ E_PantiesDown = 0
                        #    pause .1
                        #    #$ E_Legs = Temp_E_Legs
                        #    $ E_Upskirt = 0
                        #    pause
                        #elif E_Panties and E_Panties != "lace panties" and E_Panties != "black panties" and E_Panties != "swimsuit1" and E_Panties != "swimsuit2":
                        #    $ E_PantiesDown = 1
                        #    "And pulls down her [E_Panties]"
                        #    ch_e "There, you happy?"
                        #    call Emma_Show_Plug
                        #    $ E_PantiesDown = 0
                        #    pause
                        else:
                            ch_e "There, you happy?"
                            call Emma_Show_Plug from _call_Emma_Show_Plug_1
                            pause


                        call Emma_Doggy_Reset from _call_Emma_Doggy_Reset_1 
                    else:
                        if Taboo:
                            ch_e "Not here [E_Petname]"
                        else:
                            ch_e "No"
            
        "Sex Menu" if E_Loc == bg_current:
                    call Taboo_Level from _call_Taboo_Level_31
                    if E_Love >= E_Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    call CleartheRoom("Emma",Check=1) from _call_CleartheRoom_29
                    if "angry" in E_RecentActions:  
                        ch_e "You should know better than that."
                    # elif Taboo:
                    #         ch_e "I don't really think we should be doing anything in public just yet. . ."                        
                    # elif _return >= 1:
                    #         # if there are other girls in the room. . .
                    #         ch_e "I don't really feel comfortable with these other girls around just yet."
                    elif ApprovalCheck("Emma", 600, "LI"):
                        call EmmaFace("sexy") from _call_EmmaFace_552
                        ch_e "I suppose. . ."
                        call Emma_SexMenu from _call_Emma_SexMenu
                        return
                    elif ApprovalCheck("Emma", 400, "OI"):
                        ch_e "If that's what you want, [E_Petname]."
                        call Emma_SexMenu from _call_Emma_SexMenu_1
                        return
                    else:
                        ch_e "No thanks, [E_Petname]."          
                                
        "I just wanted to talk. . .":
                    call Emma_Chitchat from _call_Emma_Chitchat   
                    
        "Emma's settings":
                    ch_p "Let's talk about you."
                    call Emma_Settings from _call_Emma_Settings   
        
        "Relationship status":      
                    ch_p "Could we talk about us?"       
                    if "relationship" in E_DailyActions:
                        ch_e "Now you're starting to bore me."
                    elif E_Loc == bg_current:
                        call Emma_Relationship from _call_Emma_Relationship
                    else:
                        ch_e "This seems a bit serious to discuss over the phone."
                        ch_e "Later, perhaps."
                        
        "Could I get your number?" if "Emma" not in Digits:
                    if ApprovalCheck("Emma", 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append("Emma") 
                    elif ApprovalCheck("Emma", 500, "OI"):
                        ch_e "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Emma")
                    else:
                        ch_e "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if E_Loc == bg_current:
                ch_p "I'd like to give you something."
                call Emma_Gifts from _call_Emma_Gifts
                    
        "Add her to party" if "Emma" not in Party and E_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"                                             
                    if ApprovalCheck("Emma", 1250):
                        $ Party.append("Emma")
                        ch_e "Lead away."
                        return
                    elif ApprovalCheck("Emma", 950):
                        $ Party.append("Emma")
                        ch_e "You'd better not bore me."
                        return
                    elif not ApprovalCheck("Emma", 400):
                        ch_e "I can't imagine why I would."
                    else:
                        ch_e "I'd rather not."
        "Disband party" if "Emma" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Emma")       
                    call Emma_Schedule(0) from _call_Emma_Schedule_2
                    if E_Loc == bg_current:
                        ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif E_Loc == "bg teacher" and bg_current == "bg classroom":
                        ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_e "If that's all then, I'll see you later."
                        call Set_The_Scene from _call_Set_The_Scene_131   
                    return
                
        "Lock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" not in E_RecentActions :
                    ch_p "Could you lock the door?"
                    ch_e "Ooh, certainly. . ."
                    $ E_RecentActions.append("locked")
                    call Taboo_Level from _call_Taboo_Level_32
        "Unlock the door" if bg_current == "bg classroom" and Current_Time == "Evening" and "locked" in E_RecentActions:
                    ch_p "Could you unlock the door?"
                    ch_e "I suppose. . ."
                    $ E_RecentActions.remove("locked")
                    call Taboo_Level from _call_Taboo_Level_33
            
        "Date" if Current_Time == "Evening":
                ch_p "Do you want to go on a date tonight?"
#                    call Emma_Date_Night
                ch_e "Well that certainly doesn't seem appropriate at the moment [[Not in yet]."

        "Talk with Rogue" if R_Loc == bg_current:
                jump Rogue_Chat

        "Talk with Kitty" if K_Loc == bg_current:
                jump Kitty_Chat
                
        "Talk with Mystique" if newgirl["Mystique"].Loc == bg_current:
                jump Mystique_Chat
                
        "Never mind.":
                    return
    jump Emma_Chat

label Emma_Chat_Minimal:
    call EmmaFace from _call_EmmaFace_553    
    call Shift_Focus("Emma") from _call_Shift_Focus_156
    if E_Loc != bg_current:
                show Cellphone at SpriteLoc(E_SpriteLoc)
    else:
                hide Cellphone
    if "caught" in E_RecentActions:
                ch_e "I don't think we should be seen together, if you don't mind."
                return
    if "angry" in E_RecentActions:
                ch_e "I would not press my luck if I were you."
                return
    if E_Loc == bg_current:
            ch_e "What was it you wanted to discuss, [E_Petname]?"
    #else:
    menu:
        "What would you like to do?"
        "Come on over." if E_Loc != bg_current:
                    ch_e "I don't think I should be visiting students at their whim."
                    ch_e "You know my office hours."
        "Ask Emma to leave" if E_Loc == bg_current:
                    ch_e "I'll come and go as I see fit, thank you."
                    
        "Sex Menu" if E_Loc == bg_current:
                    if E_Love >= E_Obed:
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."                        
                    ch_e "With a student? You should know better than that, [E_Petname]. [[YOU haven't unlocked this yet]"
                    menu:
                        "Wanna know how?"
                        "Yes, teach me":
                            "Come to the classroom at evening for a special event."
                            "And don't just wait there, at least go outside of the classroom and come back"
                            pass
                        "No, I'll find it by myself":
                            "It's not hard, have fun"
                            pass

        "I just wanted to talk. . .":
                    ch_e "I really don't have anything to talk about at the moment.[[Not in yet]"   
                    
        "Emma's settings":
                    ch_p "Let's talk about you."
                    ch_e "I doubt that's any of your business."
        
        "Relationship status":   
                    ch_p "Could we talk about us?"
                        
        "Could I get your number?" if "Emma" not in Digits:
                    if ApprovalCheck("Emma", 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append("Emma") 
                    elif ApprovalCheck("Emma", 500, "OI"):
                        ch_e "Hmm. . . fine, hand me your phone."             
                        $ Digits.append("Emma")
                    else:
                        ch_e "I don't think it's appropriate to give my number out to a student like that."  
                        
        "Gifts" if E_Loc == bg_current:
                    ch_p "I'd like to give you something."
                    ch_e "I'm not sure that would be appropriate at the moment.[[Not in yet]"
                        
        "Party up" if "Emma" not in Party and E_Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    ch_e "I don't think I should."
                    
        "Disband party" if "Emma" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Emma")       
                          
        "Date" if Current_Time == "Evening":
                    ch_p "Do you want to go on a date tonight?"
                    ch_e "Well that certainly doesn't seem appropriate at the moment [[Not in yet]."
                
        "Never mind.":
                    return
    jump Emma_Chat_Minimal


#Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Emma_Relationship:
    menu:
        ch_e "What did you want to talk about?"
        
        "Do you want to be my girlfriend?" if "dating" not in E_Traits and "ex" not in E_Traits:
                $ E_DailyActions.append("relationship")
                if "asked boyfriend" in E_DailyActions and "angry" in E_DailyActions:
                    call EmmaFace("angry", 1) from _call_EmmaFace_554
                    ch_e "Pest."
                    return
                elif "asked boyfriend" in E_DailyActions:
                    call EmmaFace("angry", 1) from _call_EmmaFace_555
                    ch_e "Not today, little fly."
                    return
                elif E_Break[0]:                    
                    call EmmaFace("angry", 1) from _call_EmmaFace_556                    
                    ch_e "I don't share."
                    if "dating" in R_Traits:   
                        $ E_DailyActions.append("asked boyfriend")                     
                        return
                    elif "dating" in K_Traits:   
                        $ E_DailyActions.append("asked boyfriend")                     
                        return
                    elif "ex" in R_Traits:
                        ch_p "I'm not anymore."
                    elif "ex" in K_Traits:
                        ch_p "I'm not anymore."
                                
                $ E_DailyActions.append("asked boyfriend")
                
                if E_Event[5]:
                    call EmmaFace("bemused", 1) from _call_EmmaFace_557
                    ch_e "I believe I asked you first."
                else:
                    call EmmaFace("surprised", 2) from _call_EmmaFace_558
                    ch_e "Don't you think that might be inappropriate, [E_Petname]. . ." 
                    call EmmaFace("smile", 1) from _call_EmmaFace_559
                
                call Emma_OtherWoman from _call_Emma_OtherWoman
                
                if E_Love >= 800:
                        call EmmaFace("surprised", 1) from _call_EmmaFace_560
                        $ E_Mouth = "smile"
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 40)
                        ch_e "I suppose I've become accustomed to you. . ."
                        if "boyfriend" not in E_Petnames:
                            $ E_Petnames.append("boyfriend")                
                        $ E_Traits.append("dating")
                        "Emma draws you in and kisses you deeply."
                        call EmmaFace("kiss", 1) from _call_EmmaFace_561 
                        $ E_Kissed += 1
                elif E_Obed >= 500:
                        call EmmaFace("perplexed") from _call_EmmaFace_562
                        ch_e "I don't believe \"dating\" would be the right term for it."
                elif E_Inbt >= 500:
                        call EmmaFace("smile") from _call_EmmaFace_563                
                        ch_e "I don't think we should be \"exclusive.\""
                else:
                        call EmmaFace("perplexed", 1) from _call_EmmaFace_564
                        ch_e "I really couldn't get serious about a student, [E_Petname]."
                    
        "When you said you loved me. . ." if "lover" not in E_Traits and E_Event[6] >= 20:
                call Emma_Love_Redux from _call_Emma_Love_Redux
        
        "Do you want to get back together?" if "ex" in E_Traits:
                $ E_DailyActions.append("relationship")
                if "asked boyfriend" in E_DailyActions and "angry" in E_DailyActions:
                    call EmmaFace("angry", 1) from _call_EmmaFace_565
                    ch_e "Do I have to demonstrate how unlikely that is?"
                    return
                elif "asked boyfriend" in E_DailyActions:
                    call EmmaFace("angry", 1) from _call_EmmaFace_566
                    ch_e "Now you're just embarrassing yourself."
                    return
                elif E_Break[0]: 
                    call EmmaFace("angry", 1) from _call_EmmaFace_567                    
                    if "dating" in (R_Traits,K_Traits):   
                        ch_e "I don't share."
                        return
                    elif "ex" in (R_Traits,K_Traits):
                        ch_e "I don't share."
                        ch_p "I'm not anymore."
                        $ E_Break[0] = 0
                    else:    
                        if not ApprovalCheck("Emma", 1500) or E_Break[1] > 5:
                            ch_e "Persistance will not be rewarded."
                        else:
                            call EmmaFace("sad", 1) from _call_EmmaFace_568
                            ch_e "You couldn't even wait a few days to start sniffing around again?"
                        $ E_DailyActions.append("asked boyfriend")
                        return
                
                $ E_DailyActions.append("asked boyfriend")
                
                $ Cnt = 0
                call Emma_OtherWoman from _call_Emma_OtherWoman_1
                                        
                if E_Love >= 800:
                    call EmmaFace("sly", 1) from _call_EmmaFace_569
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
                    ch_e "Try as I might, I can't stay mad at you."
                    if "boyfriend" not in E_Petnames:
                        $ E_Petnames.append("boyfriend")                
                    $ E_Traits.append("dating")          
                    $ E_Traits.remove("ex")
                    "Emma leans in and kisses you deeply."
                    call EmmaFace("kiss", 1) from _call_EmmaFace_570 
                    $ E_Kissed += 1
                elif E_Love >= 600 and ApprovalCheck("Emma", 1500):
                    call EmmaFace("smile", 1) from _call_EmmaFace_571
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)
                    ch_e "Hrm, very well."
                    if "boyfriend" not in E_Petnames:
                        $ E_Petnames.append("boyfriend")                
                    $ E_Traits.append("dating")             
                    $ E_Traits.remove("ex")
                    call EmmaFace("kiss", 1) from _call_EmmaFace_572 
                    "Emma gives you a quick kiss."
                    call EmmaFace("sly", 1) from _call_EmmaFace_573 
                    $ E_Kissed += 1
                elif E_Obed >= 500:
                    call EmmaFace("sad") from _call_EmmaFace_574
                    ch_e "Let's keep things as they are, for now."   
                elif E_Inbt >= 500:
                    call EmmaFace("perplexed") from _call_EmmaFace_575                
                    ch_e "No, \"casual\" works better for the time being."
                else:
                    call EmmaFace("perplexed", 1) from _call_EmmaFace_576
                    ch_e "I can't be bothered with second chances."
                
        # End Back Together
                    
                               
#        "I think we should break up." if "dating" in R_Traits: #ApprovalCheck("Rogue", 950, "L", Bonus = (B/3)):
#            if "breakup talk" in R_RecentActions:
#                ch_r "We were {i}just{/i} over this, not even funny."
#            elif "breakup talk" in R_DailyActions:
#                ch_r "Tired of me again that quick?" 
#                ch_r "We're not having this talk today, [R_Petname]."
#            else:
#                call Rogue_Breakup                
            
            
#        "I'd like to bring Emma into this." if "poly emma" not in R_Traits and not E_Break[0]:    #fix nonfunctional yet, switch over to Emma stuff
            
#            if "asked threesome" in R_RecentActions:
#                ch_r "Persistence will NOT be rewarded here."
#                return
#            elif "asked threesome" in R_DailyActions:
#                ch_r "I don't think my answer's changing any time soon." 
#                return
#            else:
#                $ R_DailyActions.append("asked threesome")                
#                $Cnt = int((R_LikeEmma - 500)/2)
                menu:
                    ch_r "What does she think about this?"
                        
                    "She said I can be with you too." if "poly rogue" in E_Traits:
                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
                            call RogueFace("smile", 1) from _call_RogueFace_845
                            if R_Love >= R_Obed:
                                ch_r "Just so long as we can be together, I can share."
                            elif R_Obed >= R_Inbt:
                                ch_r "I'm ok with that if she is."
                            else:
                                ch_r "Yeah, I mean I guess so."
                                $ R_Traits.append("poly emma")
                        else:
                            call RogueFace("angry", 1) from _call_RogueFace_846
                            ch_r "Well maybe she did, but I don't want to share."  
                    
                    "I could ask if she'd be ok with me dating you both." if "poly rogue" not in E_Traits:
                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt) or :
                            call RogueFace("smile", 1) from _call_RogueFace_847
                            if R_Love >= R_Obed:
                                ch_r "Just so long as we can be together, I can share."
                            elif R_Obed >= R_Inbt:
                                ch_r "I'm ok with that if she is."
                            else:
                                ch_r "Yeah, I mean I guess so."                        
                            ch_r "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                        else:
                            call RogueFace("angry", 1) from _call_RogueFace_848
                            ch_r "Well maybe she would, but I don't want to share."  
                    
                    "Could you ask?":
                        if R_LikeEmma >= 700:
                            ch_r "I have to say I've kind of been thinking about it myself."  
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
                        elif R_LikeEmma >= 500:
                            ch_r "I guess, if that's what you want. . ." 
                        elif R_Obed >= 700:
                            ch_r "If that's what you want. . ." 
                        else:
                            ch_r "I can't really stand her, I don't think so."  
                            
                        
                    "You're right, I was dumb to ask.":
                        call RogueFace("sad") from _call_RogueFace_849
                        ch_r "Yeah, you were."  
                        
            #end Emma Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in E_Petnames and "sir" in E_History:
                if "asked sub" in E_DailyActions:
                        ch_e "I did, you didn't."          
                else:
                        call Emma_Sub_Asked from _call_Emma_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in E_Petnames and "master" in E_History:
                if "asked sub" in E_DailyActions:
                        ch_e "I seem to recall something about that. . ."            
                else:
                        call Emma_Sub_Asked from _call_Emma_Sub_Asked_1                        
        "Never Mind":
            return
              
    return

label Emma_OtherWoman(Other="Rogue", Poly = 0, Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    $ Cnt = 0
    if "dating" in R_Traits:        
            # $ Other = "Rogue"
            if "poly emma" in R_Traits:
                $ Poly = 1     
            $Cnt = int((E_LikeRogue - 500)/2)
    elif "dating" in K_Traits:
            $ Other = "Kitty"
            if "poly emma" in K_Traits:
                $ Poly = 1                
            $Cnt = int((E_LikeKitty - 500)/2)
    else:
        return
        
    call EmmaFace("perplexed") from _call_EmmaFace_577
    menu: 
        ch_e "But you're with [Other] right now."
        "She said I can be with you too." if Poly:
                if ApprovalCheck("Emma", 1800, Bonus = Cnt):
                    call EmmaFace("smile", 1) from _call_EmmaFace_578
                    if E_Love >= E_Obed:
                        ch_e "I suppose you're worth sharing."
                    elif E_Obed >= E_Inbt:
                        ch_e "If she can share then I can."
                    else:
                        ch_e "Sure, why not."
                    if Other == "Rogue":
                            $ E_Traits.append("poly rogue")
                    elif Other == "Kitty":
                            $ E_Traits.append("poly kitty")
                else:
                    call EmmaFace("angry", 1) from _call_EmmaFace_579
                    ch_e "I really don't care what that little slut does."  
                    $ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return
        
        "I could ask if she'd be ok with me dating you both." if not Poly:
                if ApprovalCheck("Emma", 1800, Bonus = Cnt):
                    call EmmaFace("smile", 1) from _call_EmmaFace_580
                    if E_Love >= E_Obed:
                        ch_e "I suppose you're worth sharing."
                    elif E_Obed >= E_Inbt:
                        ch_e "If she can share then I can."
                    else:
                        ch_e "Sure, why not."                       
                    ch_e "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call EmmaFace("angry", 1) from _call_EmmaFace_581
                    ch_e "I really don't care what that little slut does."    
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
                if not ApprovalCheck("Emma", 1800, Bonus = -Cnt): #checks if Rogue likes you more than Emma
                    call EmmaFace("angry", 1) from _call_EmmaFace_582
                    if not ApprovalCheck("Emma", 1800):
                        ch_e "I don't want you either."
                    else:
                        ch_e "I don't want to share you."                    
                    $ renpy.pop_call() 
                
                else:
                    call EmmaFace("smile", 1) from _call_EmmaFace_583
                    if E_Love >= E_Obed:
                        ch_e "I suppose we could arrange something."
                    elif E_Obed >= E_Inbt:
                        ch_e "If you insist."
                    else:
                        ch_e "I don't see why not."
                    if Other == "Rogue":
                            $ E_Traits.append("poly rogue")
                    elif Other == "Kitty":
                            $ E_Traits.append("poly kitty")
                    $ E_Traits.append("downlow")
                
        "I can break it off with her.":
                    call EmmaFace("sad") from _call_EmmaFace_584
                    ch_e "Then we can talk after you have."                                   
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    call EmmaFace("sad") from _call_EmmaFace_585
                    ch_e "Obviously. . ."                    
                    $ renpy.pop_call()                     
                
    return
#End Emma Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////      
    
    
    
#Emma Settings ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
label Emma_Settings:
    menu:
        "Wardrobe":     
                ch_p "I wanted to talk about your style."
                if E_Loc != "bg player" and E_Loc != "bg emma":  
                    if Taboo:
                        if "exhibitionist" in E_Traits:
                            ch_e "Mmmmm. . ."  
                        elif ApprovalCheck("Emma", 900, TabM=4) or ApprovalCheck("Emma", 400, "I", TabM=3): 
                            ch_e "This isn't really the appropriate place for it, however. . ."
                        else:
                            ch_e "I'd rather discuss that in private."
                            return
                    call Emma_Clothes from _call_Emma_Clothes
                elif ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 300, "O"):
                    ch_e "What about my style?"
                    call Emma_Clothes from _call_Emma_Clothes_1
                else:
                    ch_e "I'll let you know when I care what you think."

        "Wear this vibrator to class" if "vibeclass" not in E_Traits:
                if "exhibitionist" in E_Traits:
                    call EmmaFaceSpecial("sexy",1) from _call_EmmaFaceSpecial_14
                    ch_e "Oooh, that could be entertaining. . ."  
                elif ApprovalCheck("Emma", 1000, TabM=3) or ApprovalCheck("Emma", 800, "I") or ApprovalCheck("Emma", 750, "O"): 
                    call EmmaFaceSpecial("surprised",1) from _call_EmmaFaceSpecial_15
                    ch_e "Well, I mean, yeah, I guess I could. . ."
                else:
                    call EmmaFaceSpecial("angry",1) from _call_EmmaFaceSpecial_16
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5) 
                    ch_e "Excuse me?!"
                    return
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 5) 
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5) 
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 5) 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5) 
                $ E_Traits.append("vibeclass")
                
        "Don't wear the vibrator to class" if "vibeclass" in E_Traits:
                ch_e "Ok"
                $ E_Traits.remove("vibeclass")
                
        "Shift her Personality" if ApprovalCheck("Emma", 900, "L", TabM=0) or ApprovalCheck("Emma", 900, "O", TabM=0) or ApprovalCheck("Emma", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Emma_Personality from _call_Emma_Personality
            
        "Your Pet Name":
                ch_p "Could we talk about my pet name?"
                if ApprovalCheck("Emma", 600, "L", TabM=0) or ApprovalCheck("Emma", 300, "O", TabM=0):
                    call Emma_Names from _call_Emma_Names    
                else:
                    $ E_Mouth = "smile"
                    ch_e "It's your name, [E_Petname]."
                
        "Her Pet Name":
                ch_p "I've got a pet name for you, you know?"
                if ApprovalCheck("Emma", 600, "L", TabM=0):
                    ch_e "I'm dying to hear it. . ." 
                elif ApprovalCheck("Emma", 300, "O", TabM=0):
                    ch_e "Do you now."
                else:
                    ch_e "You've made me curious. . ."          
                call Emma_Pet from _call_Emma_Pet   
                    
        "Other girls":
            menu:
                ch_p "How do you feel about. . ."
                "Rogue?":
                    call Emma_AboutRogue from _call_Emma_AboutRogue  
                "Kitty?":
                    call Emma_AboutKitty from _call_Emma_AboutKitty
                "Never mind.":
                    pass
        
        "Follow options" if "follow" in E_Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_e "Yes?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in E_Traits:
                            call EmmaFace("perplexed") from _call_EmmaFace_586
                            ch_e "Fine, I'll leave some mystery."
                            if "follow" not in E_DailyActions:
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -2)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 5) 
                            $ E_Traits.append("freetravels")
                            $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in E_Traits:
                            call EmmaFace("perplexed") from _call_EmmaFace_587
                            ch_e "Don't want to be left behind?"
                            if "follow" not in E_DailyActions:
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2) 
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2) 
                            $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in E_Traits:
                            if ApprovalCheck("Emma", 600, "O") or ApprovalCheck("Emma", 900, "L"):   
                                call EmmaFace("angry", Eyes="side") from _call_EmmaFace_588
                                ch_e "I don't know why I put up with your nonsense."
                                call EmmaFace("sexy",1) from _call_EmmaFace_589
                                ch_e "But {i}fine.{/i}"
                                if "follow" not in E_DailyActions:
                                        if E_Love > 90:
                                            $ E_Love = Statupdate("Emma", "Love", E_Love, 99, 2)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)                             
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -5, 1) 
                                $ Line = "lock"
                            else:
                                call EmmaFace("angry") from _call_EmmaFace_590                        
                                ch_e "Where I go is my own business."
                            
                    "Never mind.":
                            ch_e "Whatever."
                        
                if Line:
                    $ E_DailyActions.append("follow")                
                    if "freetravels" in E_Traits:
                        $ E_Traits.remove("freetravels") 
                    if "asktravels" in E_Traits:
                        $ E_Traits.remove("asktravels") 
                    if "lockedtravels" in E_Traits:
                        $ E_Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ E_Traits.append("freetravels")            
                    elif Line == "ask":
                        $ E_Traits.append("asktravels")                
                    elif Line == "lock":
                        $ E_Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in E_DailyActions and "no ask gym" not in E_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_e "I'm glad you approve."
                    $ E_Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in E_Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."   
                    ch_e "Ok, I'll keep that in mind."
                    $ E_Traits.remove("no ask gym")
                    
        "Tasks" if "sir" in E_Petnames:
                    ch_p "I have some tasks for you."
                    call Emma_Controls from _call_Emma_Controls
            
        "Never mind.":
            return  
    return

# End Emma Settings  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  



## Emma Chitchat /////////////////// #Work in progress
label Emma_Chitchat(O=0, Options = ["default","default","default"]):
    if O:                                               #adds only a specific option that was sent
        $ Options [O]
    else:
        
        if "Emma" not in Digits:
                if ApprovalCheck("Emma", 500, "L") or ApprovalCheck("Emma", 250, "I"):
                    ch_e "You know, I never got around to giving you my number, here you go."
                    $ Digits.append("Emma")  
                    return
                elif ApprovalCheck("Emma", 250, "O"):
                    ch_e "You know, you should probably have my number, here you go."             
                    $ Digits.append("Emma")
                    return
                
        if "hungry" not in E_Traits and (E_Swallow + E_Chat[2]) >= 10 and E_Loc == bg_current:  #She's swallowed a lot        
                call Emma_Hungry from _call_Emma_Hungry
                return  
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in E_DailyActions:
#            $ Options.append("caught")
        if E_Event[0] and "key" not in E_Chat:
            $ Options.append("key")
        if "lover" in E_Petnames and ApprovalCheck("Emma", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in E_DailyActions:
            $ Options.append("corruption")
        
        if E_Date >= 1:
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in E_DailyActions and "cheek" not in E_Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if E_Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in E_DailyActions:
            #If you've caught Emma showering today
            $ Options.append("showercaught")
        if "fondle breasts" in E_DailyActions or "fondle pussy" in E_DailyActions or "fondle ass" in E_DailyActions:
            #If you've fondled Emma today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in E_Inventory and "256 Shades of Grey" in E_Inventory and "Avengers Tower Penthouse" in E_Inventory:   
            #If you've given Emma the books
            if "book" not in E_Chat:
                $ Options.append("booked")
        if "lace bra" in E_Inventory or "lace panties" in E_Inventory:   
            #If you've given Emma the lingerie
            if "lingerie" not in E_Chat:
                $ Options.append("lingerie")
        if E_Hand:   
            #If Emma's given a handjob
            $ Options.append("handy")
        if E_Swallow:   
            #If Emma's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in E_DailyActions or "painted" in E_DailyActions:
            #If Emma's been facialed
            $ Options.append("facial")
        if E_Sleep:
            #If Emma's slept over
            $ Options.append("sleep")
        if E_CreamP or E_CreamA:
            #If Emma's been creampied
            $ Options.append("creampie")
        if E_Sex or E_Anal:
            #If Emma's been sexed
            $ Options.append("sexed")
        if E_Anal:
            #If Emma's been analed
            $ Options.append("anal")
            
#        if not E_Chat[0] and E_Sex:
#            $ Options.append("virgin")    
            
        if (bg_current == "bg emma" or bg_current == "bg player") and "relationship" not in E_DailyActions:
            if "boyfriend" not in E_Petnames and ApprovalCheck("Emma", 750, "L"): # E_Event[5]
                $ Options.append("boyfriend?")
            elif "lover" not in E_Petnames and ApprovalCheck("Emma", 900, "L"): # E_Event[6]        
                $ Options.append("lover?")
            elif "sir" not in E_Petnames and ApprovalCheck("Emma", 500, "O"): # E_Event[7]
                $ Options.append("sir?")      
            elif "daddy" not in E_Petnames and ApprovalCheck("Emma", 750, "L") and ApprovalCheck("Emma", 500, "O") and ApprovalCheck("Emma", 500, "I"): # E_Event[5]
                $ Options.append("daddy?")
            elif "master" not in E_Petnames and ApprovalCheck("Emma", 900, "O"): # E_Event[8]
                $ Options.append("master?")
            elif "sex friend" not in E_Petnames and ApprovalCheck("Emma", 500, "I"): # E_Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in E_Petnames and ApprovalCheck("Emma", 900, "I"): # E_Event[10]
                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Emma", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("confused") from _call_EmmaFace_591
        ch_e "(sniff, sniff). . . is that. . . chimp? . . ."
        call EmmaFace("perplexed", 1) from _call_EmmaFace_592
        ch_e ". . . but it's. . . {i}sexy{/i} chimp?"    
    elif Options[0] == "purple":              
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("sly",1) from _call_EmmaFace_593
        ch_e "(sniff, sniff). . . huh, what's that smell? . ."
        ch_e ". . . could I get you something?"    
    elif Options[0] == "corruption":              
        $ E_DailyActions.append("cologne chat") 
        call EmmaFace("confused") from _call_EmmaFace_594
        ch_e "(sniff, sniff). . . that's pretty overpowering. . ."
        call EmmaFace("sly") from _call_EmmaFace_595
        ch_e ". . . I may not be able to keep my hands to myself. . ."
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in E_Chat:
                    ch_e "We've really got to stop making a habit of getting caught."
                    if not ApprovalCheck("Emma", 500, "I"):
                         ch_e "Or not. . ."
            else:    
                    ch_e "I did not enjoy getting dragged to the Professor's office like that."
                    if not ApprovalCheck("Emma", 500, "I"):
                        ch_e "I don't know about doing it in public anymore."
                    else:
                        ch_e "It was kind of hot though. . ."
                    $ E_Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            $ Line = "I'm glad you have my key now,"
            if E_SEXP <= 15:
                $ Line = Line + " just don't use it for any funny business. . ."
            else:
                $ Line = Line + " maybe you could . . . \"surprise\" me sometime. . ."
            ch_e "[Line]"
            $ E_Chat.append("key") 
        
    elif Options[0] == "cheek":
            #Emma's response to having her cheek touched.
            ch_e "So,[E_Petname]. . .y'know how you kinda just brushed my cheek before?"
            ch_p "Yeah?  Was that okay?"
            call EmmaFace("smile",1) from _call_EmmaFace_596
            ch_e "More than just {i}okay{/i}."
            $ E_Chat.append("cheek") 
            
    elif Options[0] == "dated":
            #Emma's response to having gone on a date with the Player.
            ch_e "Heya,[E_Petname].  I had a lot of fun last night.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Emma's response to having been kissed by the Player.
            call EmmaFace("sly",1) from _call_EmmaFace_597
            ch_e " . . .i never thought you'd be such a good kisser, [E_Petname]."
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        call EmmaFace("smile",1) from _call_EmmaFace_598
                        ch_e "I think maybe you can show me {i}how{/i} good whenever you want."
                "No. You think?":
                        ch_e "Yeah.  I do.  a {i}lot{/i}."

    elif Options[0] == "dangerroom":
            #Emma's response to Player working out in the Danger Room while Emma is present
            call EmmaFace("sly",1) from _call_EmmaFace_599
            ch_e "Hey,[E_Petname].  I watched you working out in the Danger Room, earlier.  You looked {i}so{/i} cute in your X-Men uniform!"

    elif Options[0] == "showercaught":
            #Emma's response to being caught in the shower.
            if "shower" in E_Chat: 
                ch_e "Hope you liked the view earlier. . ."                       
            else:
                ch_e "So, you run into a lot of people in the shower. . .or just me?"            
                $ E_Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 5)    
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2) 
                            if ApprovalCheck("Emma", 1200):
                                call EmmaFace("sly",1) from _call_EmmaFace_600
                                ch_e "Yeah?  {i}Maybe{/i} you should have accidents like that more often."
                            call EmmaFace("smile") from _call_EmmaFace_601
                            ch_e "It's cool, [E_Petname]. Eveybody makes mistakes. . . sometimes."
                    "Just you.":        
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 5)   
                            if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 700, "L"):      
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3)    
                                    call EmmaFace("sly",1) from _call_EmmaFace_602
                                    ch_e "You know how to make a woman feel special, [E_Petname]."
                            else:                
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5) 
                                    call EmmaFace("angry") from _call_EmmaFace_603
                                    ch_e "You're {i}such{/i} a creep, [Playername], y'know that?"                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Emma", 1200):                     
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3)          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 10)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                                    call EmmaFace("sly",1) from _call_EmmaFace_604
                                    ch_e "Hmm. . .next time, we'll have to take advantage of the moment."
                            elif ApprovalCheck("Emma", 800):                          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                                    call EmmaFace("perplexed",2) from _call_EmmaFace_605
                                    ch_e "Wha. . . um. . . okay?"
                                    $ E_Blush = 1
                            else:                
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10) 
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -10)          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)  
                                    call EmmaFace("angry") from _call_EmmaFace_606
                                    ch_e "You're such a creep, [E_Petname], y'know that?"

    elif Options[0] == "fondled":
            #Emma's response to being felt up.
            if E_FondleB + E_FondleP + E_FondleA >= 15:
                ch_e "I want your hands on me." 
            else:                
                ch_e "You know how you felt me up earlier?  I could kinda get used to having your hands on me."

    elif Options[0] == "booked":
            #Emma's response after a Player gives her the books from the shop.
            ch_e "So..I read the books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        call EmmaFace("sly",2) from _call_EmmaFace_607
                        ch_e "They were . . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":                     
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -3)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 5)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                        call EmmaFace("angry") from _call_EmmaFace_608
                        ch_e "Guess {i}you'll{/i} never find out, huh?"                
            $ E_Blush = 1
            $ E_Chat.append("book") 

    elif Options[0] == "lingerie":
            #Emma's response to being given lingerie.
            call EmmaFace("sly",2) from _call_EmmaFace_609
            ch_e "[E_Petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me.  They're so cute!"
            $ E_Blush = 1
            $ E_Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Emma's response after giving the Player a handjob.
            call EmmaFace("sly",2) from _call_EmmaFace_610
            ch_e "I was just thinking about how I stroked your cock the other day. . ."
            ch_e "I loved the expression on your face. . .knowing I could make you {i}feel{/i} like that."
            $ E_Blush = 1

    elif Options[0] == "blow":
            if "blow" not in E_Chat:
                    #Emma's response after giving the Player a blowjob.
                    call EmmaFace("sly",2) from _call_EmmaFace_611
                    ch_e "So. . .uhm, be honest with me, [E_Petname]?"
                    ch_e "When I gave you head. . . have i lost my mojo? People said i was pretty good at it!"
                    ch_e "I kinda had a hard time getting all of you into my mouth."
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 10) 
                                    call EmmaFace("sexy",1) from _call_EmmaFace_612
                                    ch_e "Awesome.  'Cause I can't wait to try again."
                        "Honest? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Emma", 300, "I") or not ApprovalCheck("Emma", 800):                     
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 10) 
                                    call EmmaFace("perplexed",1) from _call_EmmaFace_613
                                    ch_e "Yeah?  Well then maybe I'll get some practice in before we do it again."
                                else:                              
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 15)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5) 
                                    call EmmaFace("sexy",1) from _call_EmmaFace_614
                                    ch_e "Yeah?  Well, I'm[E_Petname]looking forward our next training session, then."                                    
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)   
                                call EmmaFace("angry",2) from _call_EmmaFace_615
                                ch_e "Guess you're gonna have to figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
                    $ E_Blush = 1
                    $ E_Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["You know, I kinda like how you taste.", 
                            "You're a real jaw-breaker.", 
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_e "[Line]"

    elif Options[0] == "swallowed":
            #Emma's response after swallowing the Player's cum.
            if "swallow" in E_Chat:                
                ch_e "I'd like another taste sometime."
            else:
                ch_e "So. . .I was just thinking about the other day.  You know, that was the first time I swallowed a student."
                call EmmaFace("sly",1) from _call_EmmaFace_616
                ch_e "Not bad. . ."
                $ E_Chat.append("swallow") 

    elif Options[0] == "facial":
            #Emma's response after taking a facial from the Player.
            ch_e "Hey. . .this is gonna sound kinda weird, but. . ."
            call EmmaFace("sexy",2) from _call_EmmaFace_617
            ch_e "I feel so {i}sexy{/i} when you cum on my face."
            $ E_Blush = 1

    elif Options[0] == "sleepover":
            #Emma's response after sleeping with the Player.
            ch_e "I  totally can't stop thinking about the other night.  It was {i}so{/i} perfect."

    elif Options[0] == "creampie":
            #Another of Emma's responses after having sex with the Player.
            "Emma draws close to you so she can whisper into your ear."
            ch_e "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Emma after having sex with the Player.
            ch_e "So. . .I want you to know something. . ."
            call EmmaFace("sexy",2) from _call_EmmaFace_618
            ch_e ". . . every time I masturbate. . ."
            ch_e "I think about how it felt, with you inside of me."
            $ E_Blush = 1

    elif Options[0] == "anal":
            #Emma's response after getting anal from the Player.
            call EmmaFace("sly",2) from _call_EmmaFace_619
            ch_e "Y'know. . .after the other night, I'm kinda having trouble sitting down."
            call EmmaFace("sexy",2) from _call_EmmaFace_620
            ch_e "{i}Totally{/i} worth it, though."
            $ E_Blush = 1
        
    elif Options[0] == "boyfriend?":
        call Emma_BF from _call_Emma_BF
#    elif Options[0] == "lover?":
#        call Emma_Love
    elif Options[0] == "sir?":
        call Emma_Sub from _call_Emma_Sub
    elif Options[0] == "master?":
        call Emma_Master from _call_Emma_Master
#    elif Options[0] == "sexfriend?":
#        call Emma_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Emma_Fuckbuddy 
#    elif Options[0] == "daddy?":
#        call Emma_Daddy  
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to see your face.", 
                "Stop bothering me.",
                "Leave me alone."])
        ch_e "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call EmmaFace("smile") from _call_EmmaFace_621
                    ch_e "I'm {i}so{/i} excited [E_Petname]! I'm {i}totally{/i} going shopping tomorrow! I really need some new handbags!"
            elif D20 == 2:
                    call EmmaFace("down") from _call_EmmaFace_622
                    ch_e "My...my father and I aren't exactly on speaking terms"
            elif D20 == 3:
                    call EmmaFace("surprised") from _call_EmmaFace_623
                    ch_e "Come on, Emma. Picture it in your mind. Focus."
            elif D20 == 4:
                    call EmmaFace("down") from _call_EmmaFace_624
                    ch_e "Hallo, [E_Petname]. I got the world's worst sleep last night. I feel like I could curl up and go to bed right here."
            elif D20 == 5:
                    call EmmaFace("smile") from _call_EmmaFace_625
                    ch_e "Wow! Isn't it {i}so{/i} nice out right now? I think I'll take a sunbath later."
            elif D20 == 6:
                    call EmmaFace("startled") from _call_EmmaFace_626
                    ch_e "You are still so young. You still believe and trust people... And you wish to be loved. It is of course a character flaw, but a tolerable one!"
            elif D20 == 7:
                    call EmmaFace("smile") from _call_EmmaFace_627
                    ch_e "Oh, [E_Petname] You should see those new Earrings i just bought!"
            elif D20 == 8:
                    call EmmaFace("sad") from _call_EmmaFace_628
                    ch_e "What do you think? The best body money can buy, a scintillating wit, and I still rate below a corpse."
            elif D20 == 9:
                    call EmmaFace("confused") from _call_EmmaFace_629
                    ch_e "Being an X-Men means a lot to me. But it doesn't always agree with me."
            elif D20 == 10:
                    call EmmaFace("smile") from _call_EmmaFace_630
                    ch_e "Well, don't worry, darling. Emma's here to save the day."
            elif D20 == 11:
                    call EmmaFace("smile") from _call_EmmaFace_631
                    ch_e "I love Christmas Eve. Maybe even more so than Christmas itself. It's the one night of the year when the entire world just...stops."
            elif D20 == 12:
                    call EmmaFace("down") from _call_EmmaFace_632
                    ch_e "Ah, [E_Petname]. Sorry, {i}darling{/i} i have no time for you right now, got to prepare fot the class tomorrow!"
            elif D20 == 13:
                    call EmmaFace("smile") from _call_EmmaFace_633
                    ch_e "You remember Daredevil's old girlfriend? That psychotic Greek assassin with the very faint mustache?"
            elif D20 == 14:
                    call EmmaFace("sad") from _call_EmmaFace_634
                    ch_e "Unfortunatly i did not get that Gucci boots i wanted so im not in a good mood right now, [E_Petname]! "
            elif D20 == 15:
                    call EmmaFace("startled") from _call_EmmaFace_635
                    ch_e "Appearances to the contrary... I didn't spend all my money on interior decorating"
            else:
                    call EmmaFace("startled") from _call_EmmaFace_636
                    ch_e "My eyes are up here, [E_Petname]!"
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Emma_Flirt:
    
    if E_Loc == bg_current:         
        $ E_Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
#            "Compliment her":
                
#            "Say you love her":
                
            "Touch her cheek.":                                                                                 #Touch her cheek 
                    call E_TouchCheek from _call_E_TouchCheek
                            
            "Kiss her cheek":                                                                                   #Kiss her cheek
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Emma", 700, "L", TabM=2):
                        call EmmaFace("sexy", 1) from _call_EmmaFace_637 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2) 
                        ch_e ". . ."
                        ch_e "Hello. . ."
                    elif ApprovalCheck("Emma", 400, "L", TabM=3):
                        call EmmaFace("surprised", 1) from _call_EmmaFace_638
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 2)
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 1) 
                        ch_e ". . . to what do I owe the pleasure?"
                    elif Taboo and ApprovalCheck("Emma", 500, "L"):                    
                        call EmmaFace("angry", 1) from _call_EmmaFace_639
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 1) 
                        ch_e "That's highly inappropriate, [E_Petname]"
                        ch_e "[[mumbles] -in public, at least. . ."
                    else: 
                        call EmmaFace("angry", 1) from _call_EmmaFace_640
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 5)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 3) 
                        ch_e "Stop that at once."
                    if "addict emma" in P_Traits:
                        $ E_Addict -= 1
                        $ E_Addictionrate += 1
                        $ E_Addictionrate = 3 if E_Addictionrate < 3 else E_Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Emma", 1000, TabM=2) or ApprovalCheck("Emma", 600, "L", TabM=2):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 600, "L"):     
                        call EmmaFace("bemused", 1) from _call_EmmaFace_641
                        $ E_Eyes = "side"         
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -5)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                        "You lean close for a kiss, but Emma gently pushes your face away."
                        ch_e "Not in public, [E_Petname]." 
                        return
                    else:                
                        call EmmaFace("angry", 1) from _call_EmmaFace_642
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 5) 
                        "You lean close for a kiss, but Emma gently pushes your face away."
                        ch_e "No." 
                        return
                    if E_Kissed:
                            if ApprovalCheck("Emma", 800, "L", TabM=2):
                                call EmmaFace("sexy", 1) from _call_EmmaFace_643
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
                                ch_e "Mmmmmmm. . ."
                            elif ApprovalCheck("Emma", 700, "L", TabM=2):
                                call EmmaFace("sexy", 1) from _call_EmmaFace_644
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2) 
                                ch_e "Hmm, hello [E_Petname]. . ."
                            elif ApprovalCheck("Emma", 550, "L", TabM=2):
                                call EmmaFace("surprised", 1) from _call_EmmaFace_645
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1) 
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2) 
                                ch_e "You're incorrigible."
                            elif Taboo and ApprovalCheck("Emma", 750):
                                call EmmaFace("angry", 1) from _call_EmmaFace_646
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
                                ch_e "Highly inappropriate!"
                                call EmmaFace("bemused", Eyes="side") from _call_EmmaFace_647
                                ch_e "-at least while in public. . ."
                            else: 
                                call EmmaFace("angry", 1) from _call_EmmaFace_648
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 6)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 3) 
                                ch_e "Down boy."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Emma", 800, "L", TabM=2) or ApprovalCheck("Emma", 1200, TabM=2):
                                call EmmaFace("surprised", 1) from _call_EmmaFace_649
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 95, 30)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 15)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 15)
                                ch_e ". . ."
                                ch_e "Hmmm, that was a pleasant surprise. . ."
                                call EmmaFace("sexy") from _call_EmmaFace_650
                                ch_e "I could always use some more, [E_Petname]."
                            elif ApprovalCheck("Emma", 650, "L", TabM=2):
                                call EmmaFace("surprised", 1) from _call_EmmaFace_651
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 25)            
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 20)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 15)
                                ch_e "Hmm?"
                                ch_e "So we're there now, are we? . ."
                            elif ApprovalCheck("Emma", 500, "L", TabM=2):
                                call EmmaFace("surprised", 1) from _call_EmmaFace_652            
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 20)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 20)
                                ch_e "I don't think that's really appropriate, [E_Petname]."
                            elif Taboo and ApprovalCheck("Emma", 800):
                                call EmmaFace("angry", 1) from _call_EmmaFace_653
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 60, -5) 
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 35)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 20)
                                ch_e "We can't be seen doing that, [E_Petname]."
                            else: 
                                call EmmaFace("angry", 1) from _call_EmmaFace_654
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 60, -10) 
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 45)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 25)
                                ch_e "How dare you?"
                            
                    $ E_Kissed += 1  
                    if "addict emma" in P_Traits:
                        $ E_Addict -= 1
                        $ E_Addictionrate += 1
                        $ E_Addictionrate = 3 if E_Addictionrate < 3 else E_Addictionrate 
                        
                    if ApprovalCheck("Emma", 700, TabM=3) and not Taboo:
                        if E_Love > E_Obed and E_Love > E_Inbt:
                            ch_e "I hope there's more where that came from. . ."
                        elif E_Obed > E_Inbt:
                            ch_e "I wouldn't mind some more of that. . ."
                        else:
                            ch_e "Get over here. . ."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3)  
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 60, 3) 
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                                call Emma_SexAct("kissing") from _call_Emma_SexAct_5
                                return
                            "Not now [[no].":
                                call EmmaFace("bemused", 1) from _call_EmmaFace_655 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 40, 1) 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 4) 
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                                ch_e "Tease. . ."
                            "Nope.":
                                call EmmaFace("angry", 1) from _call_EmmaFace_656
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 40, 1) 
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 80, -2) 
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 4)
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)
                                ch_e "I don't appreciate games, [E_Petname]."
                    elif Taboo:
                        call EmmaFace("sad") from _call_EmmaFace_657
                        ch_e "But we just can't."
                        ch_e "Not here."
                    else:
                        ch_e "Don't try that again."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Emma", 400, TabM=2):        
                        "You lean over and wrap Emma in a warm hug."
                    else:                
                        call EmmaFace("angry", 1) from _call_EmmaFace_658
                        "You lean in with your arms wide, but Emma shoves you a step back."
                        ch_e "What exactly is that about, [E_Petname]?" 
                        return
                        
                    if E_SEXP >= 30: 
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 3)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 2) 
                        call EmmaFace("sexy") from _call_EmmaFace_659
                        ch_e "Hmmm, what did you have in mind, [E_Petname]."
                    elif ApprovalCheck("Emma", 800, "L", TabM=2):
                        call EmmaFace("sexy") from _call_EmmaFace_660
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1) 
                        ch_e "Hmm, I do enjoy this. . ."
                    elif ApprovalCheck("Emma", 550, TabM=2):
                        call EmmaFace("surprised", 1) from _call_EmmaFace_661
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 2)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)  
                        ch_e "Hm? What was it you wanted?"
                    elif Taboo and ApprovalCheck("Emma", 550):
                        call EmmaFace("angry", 1) from _call_EmmaFace_662  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)        
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 3)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
                        ch_e "We can't be seen like this. . ."
                    else: 
                        call EmmaFace("angry", 1) from _call_EmmaFace_663 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 40, -4)       
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 4)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
                        ch_e "What was that about, [E_Petname]?"   
                        
            "Slap her ass" if E_Loc == bg_current:                                                              #Slap her ass
                    call E_Slap_Ass from _call_E_Slap_Ass_5
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call EmmaFace("surprised", 1) from _call_EmmaFace_664
                    if E_SEXP >= 5 and ApprovalCheck("Emma", 700, TabM=2):        
                        "You come up to Emma from behind and quickly pinch her butt."
                    else:                
                        "You come up to Emma from behind and quickly pinch her butt."
                        call EmmaFace("angry") from _call_EmmaFace_665
                        "She slaps your hand away and rounds on you."
                        ch_e "Down boy!" 
                        return
                        
                    if E_SEXP >= 40: 
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)           
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 2)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3) 
                        call EmmaFace("sexy") from _call_EmmaFace_666
                        ch_e "Mmm, what was that for?"
                    elif ApprovalCheck("Emma", 8000, TabM=2):
                        call EmmaFace("surprised") from _call_EmmaFace_667
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)           
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 2)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 
                        ch_e "Mmm, watch it."
                    elif Taboo and ApprovalCheck("Emma", 800):
                        call EmmaFace("angry") from _call_EmmaFace_668
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -4)           
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 3)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1) 
                        ch_e "That is not something you can do in public."
                    else: 
                        call EmmaFace("angry") from _call_EmmaFace_669
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -8)           
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 4)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
                        ch_e "Would you like me to break those fingers?"  
                    
                    
            "Grab her tit":                                                                                     #Grab her tit
                    call EmmaFace("surprised", 1) from _call_EmmaFace_670
                    if E_SEXP >= 5 and ApprovalCheck("Emma", 700, TabM=3):        
                        "You come up to Emma and quickly honk her boob."
                    else:             
                        "You come up to Emma and quickly honk her boob."
                        call EmmaFace("angry") from _call_EmmaFace_671
                        show Emma_Sprite
                        with vpunch
                        "She slaps your hand away and elbows you in the ribs."
                        ch_e "You must learn to resist temptations, [E_Petname]." 
                        return
                        
                    if E_SEXP >= 40: 
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 7) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2) 
                        call EmmaFace("sly") from _call_EmmaFace_672
                        ch_e "I do enjoy this, [E_Petname]. . ."
                        $ Count = 10
                    elif ApprovalCheck("Emma", 850, "L", TabM=2):
                        call EmmaFace("sexy") from _call_EmmaFace_673
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1) 
                        ch_e "Mmmmmm. . ."
                        $ Count = 7
                    elif ApprovalCheck("Emma", 1200, TabM=2):
                        call EmmaFace("perplexed") from _call_EmmaFace_674  
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)         
                        ch_e "Rather forward of you, [E_Petname]."
                        $ Count = 5
                    elif Taboo and ApprovalCheck("Emma", 900):
                        call EmmaFace("angry") from _call_EmmaFace_675
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 4)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 1) 
                        ch_e "You should move that, immediately."
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)
                        $ Count = 1
                    else: 
                        call EmmaFace("angry") from _call_EmmaFace_676
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -8)          
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 5)            
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 2) 
                        ch_e "Do you want to lose that hand?" 
                        $ Count = 2
                              
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)                     
                    while Count > 0:
                        if Count == 5:
                            call EmmaFace("sexy", 1) from _call_EmmaFace_677
                            ch_e "Mmmmm, I do enjoy that. . ."  
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2)       
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
                        elif Count == 3:
                            call EmmaFace("perplexed") from _call_EmmaFace_678
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2) 
                            ch_e "Not that I don't enjoy that, [E_Petname]. . ."
                        elif Count == 2:
                            call EmmaFace("angry") from _call_EmmaFace_679
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2) 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1) 
                            ch_e "Ok, enough of that. . ."
                        elif Count == 1:
                            call EmmaFace("angry") from _call_EmmaFace_680
                            ch_e "Time to stop, [E_Petname]."
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2) 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5) 
                            show Emma_Sprite
                            with vpunch
                            "She elbows you in the ribs."
                            ch_e "You should learn from social cues. . ." 
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_e "It's not that I really minded. . ."  
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)         
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
                                    elif Count <= 4:
                                        ch_e "I suppose it's for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        call EmmaFace("bemused") from _call_EmmaFace_681
                                        ch_e "Hmm, so amusing."          
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 4) 
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
                                    elif Count >= 4:
                                        ch_e "How droll."
                                    else:
                                        call EmmaFace("angry") from _call_EmmaFace_682
                                        ch_e "You'd better take more care."
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 3)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if E_FondleB and ApprovalCheck("Emma", 1100, TabM=3):                                
                                        call EmmaFace("sexy",1) from _call_EmmaFace_683
                                        $ E_Eyes = "closed"
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 5) 
                                    else:
                                        call EmmaFace("perplexed") from _call_EmmaFace_684
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 3) 
                                        $ Count -= 1
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 4)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
                                    ch_e "Mmm. . ."
                                    
                                "Just leave it there.":
                                    call EmmaFace("perplexed", Eyes="down") from _call_EmmaFace_685
                                    if Count == 5:
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 4) 
                                    elif Count == 2:
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2) 
                                    ch_e "Um, [E_Petname]."                     
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, 2)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
                                    call EmmaFace("perplexed") from _call_EmmaFace_686       
                    if Taboo:
                        ch_e "Show some respect when in public, [E_Petname]."
                    elif E_FondleB and ApprovalCheck("Emma", 1200, TabM = 3): 
                        call EmmaFace("sexy", 1) from _call_EmmaFace_687
                        ch_e "Were you just sampling, or did you want to continue?"
                        menu:
                            extend ""
                            "Yeah!":
                                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                                    call Emma_SexAct("breasts") from _call_Emma_SexAct_6
                                    return
                            "Nah, that was enough.":
                                    call EmmaFace("sad", 1) from _call_EmmaFace_688
                                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2) 
                                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -2)          
                                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)            
                                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2) 
                                    ch_e "Oh. Pity."
                    elif ApprovalCheck("Emma", 900, TabM = 3):  
                        $ E_Brows = "confused"
                        $ E_Eyes = "sexy"
                        $ E_Mouth = "smile"
                        ch_e "Did you enjoy that?"
                    elif ApprovalCheck("Emma", 900): 
                        call EmmaFace("angry", 1) from _call_EmmaFace_689
                        ch_e "I can't believe you would do that in public."
                    else:
                        call EmmaFace("angry", 1) from _call_EmmaFace_690
                        ch_e "Just keep your hands to yourself."
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Emma from behind and gently rub her shoulders."
                    if E_SEXP >= 30:
                        call EmmaFace("sexy") from _call_EmmaFace_691 
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)
                        "She sinks back into your hands"
                        ch_e "Hmm, to what do I owe the pleasure, [E_Petname]?"
                    elif ApprovalCheck("Emma", 650, "L", TabM = 2):
                        call EmmaFace("sexy") from _call_EmmaFace_692
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 1) 
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 2)
                        ch_e "Well that's lovely, [E_Petname]."
                    elif ApprovalCheck("Emma", 500, TabM = 2):
                        call EmmaFace("surprised", 1) from _call_EmmaFace_693
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
                        ch_e "Well hello, [E_Petname]."
                    elif ApprovalCheck("Emma", 400):
                        call EmmaFace("angry", 1) from _call_EmmaFace_694
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1)
                        if Taboo:
                            ch_e "Do I have to explain boundaries to you, [E_Petname]?"
                        else:
                            ch_e "I'd rather you didn't. . ."
                    else: 
                        call EmmaFace("angry", 1) from _call_EmmaFace_695
                        "She slaps your hands away."
                        ch_e "That will be enough of that."           
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 3)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
                        
            "Ask for her panties" if E_Panties != "naked pool":
                    call Emma_AskPanties from _call_Emma_AskPanties
                    
            "Never mind [[exit]":
                    $ E_Chat[5] = 0  
                    return
    else:
        "Emma isn't around."
            
    return
# End Emma Flirt //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


label Emma_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not E_Panties or E_Panties == "shorts":
        if ApprovalCheck("Emma", 900):
            call EmmaFace("sexy", 1) from _call_EmmaFace_696
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 40, 10)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 10) 
            ch_e "That. . . isn't exactly an option."
            
        elif ApprovalCheck("Emma", 500):
            call EmmaFace("bemused", 2) from _call_EmmaFace_697
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -3)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)
            ch_e "I don't think that would be appropriate."
            $ E_Blush = 1
            
        else:       
            call EmmaFace("angry", 1) from _call_EmmaFace_698
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -5)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2) 
            ch_e "What nerve."
            $ E_Blush = 0
            show Emma_Sprite at SpriteLoc(E_SpriteLoc) with vpunch
            "She slaps you in the face."
            $ E_RecentActions.append("angry")
            $ E_DailyActions.append("angry")   
            
    else:
        if E_SeenPussy and ApprovalCheck("Emma", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif E_SeenPanties and ApprovalCheck("Emma", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in E_Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in E_Traits or "sex friend" in E_Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in E_RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if E_Legs == "pants" or E_Legs == "black pants" or E_Legs == "NewX" or E_Legs == "NewX black" or E_Legs == "red sports shorts" or E_Legs == "white sports shorts" or HoseNum("Emma") >= 10: 
            if ApprovalCheck("Emma", 1000, "OI", TabM = 5) or "exhibitionist" in E_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Emma", 900, TabM = 5):
                $ Line = "change"
                
        elif E_Legs == "skirt":
            if ApprovalCheck("Emma", 600, "OI", TabM = 5) or "exhibitionist" in E_Traits:   
                $ Line = "here"
            elif ApprovalCheck("Emma", 1100, TabM = 5):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Emma", 1200, TabM = 5) or "exhibitionist" in E_Traits:
                $ Line = "here"
        
        
        if Line == "here":                              #She's agreed to change and will do it here
                call EmmaFace("sly") from _call_EmmaFace_699                          
                if E_Legs == "skirt":      
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 4)
                else: #no pants or skirt         
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 6)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 6) 
                
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)    
                call Remove_Panties("Emma") from _call_Remove_Panties_4
                    
                if Taboo:
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
                    if "exhibitionist" in E_Traits: 
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 5)
                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)    
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 10)        
            
        elif Line:                                      #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           #If it's in one of your rooms                                    
                    call EmmaFace("bemused", 1) from _call_EmmaFace_700 
                    menu:
                        ch_e "I would appreciate some privacy while I change."
                        "OK.": 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 5) 
                            call EmmaFace("smile", 1) from _call_EmmaFace_701                                             
                            ch_e "Thank you, [E_Petname]."
                            call EmmaFace("sly", 1) from _call_EmmaFace_702 
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)         
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)            
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 4)
                            show blackscreen onlayer black 
                            "You exit the room for a minute"   
                            $ E_DailyActions.append("pantyless")
                            call EmmaOutfit from _call_EmmaOutfit_30                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Emma") from _call_Quick_Taboo_7
                            "When you return, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Emma", 1000, "LI"): 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                                call EmmaFace("sly", 1) from _call_EmmaFace_703 
                                ch_e "How precious."
                            else:                 
                                call EmmaFace("angry", 1) from _call_EmmaFace_704 
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -3)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                                ch_e "What show would that be, [Playername]?"
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Emma", 600, "OI"): 
                                call EmmaFace("perplexed", 1) from _call_EmmaFace_705 
                                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                                ch_e "If you must."
                                call EmmaFace("normal") from _call_EmmaFace_706 
                            else:        
                                call EmmaFace("angry", 1) from _call_EmmaFace_707 
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)          
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -5)            
                                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                                ch_e "Then I suppose we're done here."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call EmmaFace("sly", 1) from _call_EmmaFace_708 
                                if E_Legs == "pants" or E_Legs == "black pants" or E_Legs == "NewX" or E_Legs == "NewX black" or E_Legs == "red sports shorts" or E_Legs == "white sports shorts" or HoseNum("Emma") >= 10:   
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)         
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)            
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5)   
                                elif E_Legs == "skirt":
                                        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5)         
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)            
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 4) 
                                        
                                call Remove_Panties("Emma") from _call_Remove_Panties_5 
                                

                else:                                   #if she's not in one of your rooms
                    call EmmaFace("sly", 1) from _call_EmmaFace_709 
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 2)         
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 4)            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 4)
                    $ E_Loc = "hold"
                    call Set_The_Scene from _call_Set_The_Scene_132
                    "Emma nods and leaves for a minute." 
                    $ E_DailyActions.append("pantyless")
                    call EmmaOutfit from _call_EmmaOutfit_31
                    if Taboo:              
                        call Quick_Taboo("Emma") from _call_Quick_Taboo_8
                    $ E_Loc = bg_current
                    call Set_The_Scene from _call_Set_The_Scene_133
                    "She returns and quietly hands you her balled up panties."
                                        
            
        else:                                           #She refuses.    
            call EmmaFace("angry", 2) from _call_EmmaFace_710                        
            if not ApprovalCheck("Emma", 500):
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -10)          
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 3)            
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                ch_e "Out of the question."
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
                
            elif not ApprovalCheck("Emma", 500, TabM = 5):
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 5) 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -5)          
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 5)            
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5) 
                ch_e "Look around you and have some sense."                                
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")   
                
            else:
                call EmmaFace("bemused", 2) from _call_EmmaFace_711
                $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 3)            
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)
                if Taboo:            
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)
                    if E_Love >= E_Inbt or E_Obed >= E_Inbt:
                        ch_e "You know I would, [E_Petname], but not here."
                    else:       
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -2)    
                        ch_e "Nah, not around here, at least."
                else:
                    if E_Love >= E_Inbt or E_Obed >= E_Inbt:
                        ch_e "You'll have to work up to that, [E_Petname]."
                    else:
                        call EmmaFace("perplexed") from _call_EmmaFace_712       
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, -2)    
                        ch_e "I think you'd need to earn that."    
            $ E_Blush = 1
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //

# Emma Control interface ///////////////////
label Emma_Controls:
    menu:
        "I'd like you to call me something else":
            call Emma_Names from _call_Emma_Names_1            
            return
        "I'd like you to come over for some action." if E_Loc != bg_current:
            ch_e "I was already in the neighborhood."
            $ E_Loc = bg_current 
            call Set_The_Scene from _call_Set_The_Scene_134
            call Emma_SexMenu from _call_Emma_SexMenu_2
            return
        "I'd like to get busy." if E_Loc == bg_current:
            ch_e "I'm sure. . ."
            call Emma_SexMenu from _call_Emma_SexMenu_3
            return
        "I want you to stop taking your own initiative." if "sub" not in E_Traits:
            $ E_Traits.append("sub")
            ch_e "You do enjoy being in control. . ."                
        "Exit.":
            return
    jump Emma_Controls
return

# start Emma_Gifts//////////////////////////////////////////////////////////
label Emma_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Give her a dildo." if "dildo" in P_Inventory: #If you have a Dildo, you'll give it.
            $ Count = E_Inventory.count("dildo")
            if "dildo" not in E_Inventory:                            
                "You give Emma the dildo."
                $ E_Blush = 1
                $ Emma_Arms = 2
                $ E_Held = "dildo"
                if ApprovalCheck("Emma", 1000) or ApprovalCheck("Emma", 400, "I"):                    
                    call EmmaFace("bemused") from _call_EmmaFace_713
                    $ P_Inventory.remove("dildo")
                    $ E_Inventory.append("dildo")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 30)
                    ch_e "I'm sure I can find some place to store it. . ."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                elif ApprovalCheck("Emma", 800) or ApprovalCheck("Emma", 300, "I"):
                    call EmmaFace("confused") from _call_EmmaFace_714
                    $ P_Inventory.remove("dildo")
                    $ E_Inventory.append("dildo")
                    ch_e "This is not an appropriate gift from a student. . ."  
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 5)
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                    call EmmaFace("sadside",1) from _call_EmmaFace_715
                    ch_e "Hm. . ."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 10)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10)
                    call EmmaFace("sly") from _call_EmmaFace_716
                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                elif "offered gift" in E_DailyActions:
                    call EmmaFace("angry") from _call_EmmaFace_717
                    "She hands it back to you."
                    ch_e "I think I have made myself clear about inappropriate gifts?"     
                else:
                    call EmmaFace("angry") from _call_EmmaFace_718
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 20)                    
                    ch_e "[E_Petname], I don't believe this is an appropriate gift from a student."                     
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                    "She hands it back to you."
                    $ E_DailyActions.append("offered gift") 
            elif Count == 1:
                ch_e "I suppose I always have room for one more. . ."
            else: 
                ch_e "How many places do you think I could put these?"
            $ E_Held = 0
            $ Emma_Arms = 2
            
            
        "Give her the vibrator." if "vibrator" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = E_Inventory.count("vibrator")
            if "vibrator" not in E_Inventory:                            
                "You give Emma the Shocker Vibrator."
                $ E_Blush = 1
                $ Emma_Arms = 2
                $ E_Held = "vibrator"
                if ApprovalCheck("Emma", 700):                    
                    call EmmaFace("bemused") from _call_EmmaFace_719
                    $ P_Inventory.remove("vibrator")
                    $ E_Inventory.append("vibrator")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 30)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 30)
                    ch_e "How very thoughtful of you. . ."  
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                    call EmmaFace("sly") from _call_EmmaFace_720
                    ch_e "I'm sure I can put this to good use. . ."
                elif ApprovalCheck("Emma", 400):
                    call EmmaFace("confused") from _call_EmmaFace_721
                    $ P_Inventory.remove("vibrator")
                    $ E_Inventory.append("vibrator")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 10)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 10)
                    ch_e "How very thoughtful of you. . ."  
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                    call EmmaFace("sly") from _call_EmmaFace_722
                    ch_e "a back massager, I assume. . ."
                elif "offered gift" in E_DailyActions:
                    call EmmaFace("angry") from _call_EmmaFace_723
                    "She hands it back to you."
                    ch_e "I think I have made myself clear about inappropriate gifts?"   
                else:
                    call EmmaFace("angry") from _call_EmmaFace_724
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 20)       
                    ch_e "[E_Petname], I don't believe this is an appropriate gift from a student."   
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 5)
                    "She hands it back to you."
                    $ E_DailyActions.append("offered gift") 
            else: 
                ch_e "I already have plenty."
            $ E_Held = 0
            $ Emma_Arms = 2
            
            
        "Give her the lace bra." if "lace bra" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = E_Inventory.count("lace bra")
            if "lace bra" not in E_Inventory:                            
                "You give Emma the lace bra."
                if ApprovalCheck("Emma", 1200):                    
                    call EmmaFace("bemused") from _call_EmmaFace_725
                    $ P_Inventory.remove("lace bra")
                    $ E_Inventory.append("lace bra")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 25)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 20)
                    ch_e "I'm impressed, you got the size correct. . ."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                elif ApprovalCheck("Emma", 800):
                    call EmmaFace("confused",1) from _call_EmmaFace_726
                    $ P_Inventory.remove("lace bra")
                    $ E_Inventory.append("lace bra")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 30)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 15)
                    ch_e "I'm not exactly running low on this sort of thing. . ."                    
                    call EmmaFace("bemused",1) from _call_EmmaFace_727
                elif ApprovalCheck("Emma", 600):
                    call EmmaFace("confused") from _call_EmmaFace_728
                    $ P_Inventory.remove("lace bra")
                    $ E_Inventory.append("lace bra")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 20)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 25)
                    ch_e "This is an . . . unusual gift from a student. . ."                     
                    call EmmaFace("bemused",1) from _call_EmmaFace_729
                elif "no gift bra" in E_DailyActions:
                    call EmmaFace("angry") from _call_EmmaFace_730
                    ch_e "This still isn't an appropriate gift from a student."      
                else:
                    call EmmaFace("angry") from _call_EmmaFace_731
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -10)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 20)  
                    if "no gift panties" in E_DailyActions:                    
                        ch_e "This isn't any better than the last."                       
                    else:                   
                        ch_e "I don't think it's appropriate for you to be so focused on my breasts."                     
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 5)
                    $ E_Blush = 1
                    "She hands it back to you."
                    $ E_RecentActions.append("no gift bra")                      
                    $ E_DailyActions.append("no gift bra") 
            else: 
                ch_e "I already have one of those."                
            
        "Give her the lace panties." if "lace panties" in P_Inventory: #If you have a bra, you'll give it.
            $ Count = E_Inventory.count("lace panties")
            if "lace panties" not in E_Inventory:                            
                "You give Emma the lace panties."
                if ApprovalCheck("Emma", 900):
                    call EmmaFace("confused",1) from _call_EmmaFace_732
                    $ P_Inventory.remove("lace panties")
                    $ E_Inventory.append("lace panties")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 25)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 20)
                    ch_e "Not entirely out of place in my wardrobe. . ."                  
                    call EmmaFace("bemused",1) from _call_EmmaFace_733
                elif ApprovalCheck("Emma", 700):
                    call EmmaFace("confused") from _call_EmmaFace_734
                    $ P_Inventory.remove("lace panties")
                    $ E_Inventory.append("lace panties")
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 20)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 20)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 25)
                    ch_e "This is an. . . unsual gift."                  
                    call EmmaFace("sly",1) from _call_EmmaFace_735
                    ch_e "But I'll hold on to them. . ." 
                elif "no gift panties" in E_DailyActions:
                    call EmmaFace("angry") from _call_EmmaFace_736
                    ch_e "I don't recommend trying again any time soon."                      
                else:
                    call EmmaFace("angry") from _call_EmmaFace_737
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -15)
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 20, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, 20)
                    if "no gift bra" in E_DailyActions:                    
                        ch_e "These aren't appropriate either." 
                    elif E_SeenPanties:
                        ch_e "Just because you've seen my panties doesn't mean you get to pick them out."                          
                    else:
                        ch_e "I don't believe these are appropriate thoughts for you to be having."                     
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 5)
                    "She hands them back to you."
                    $ E_RecentActions.append("no gift panties")                      
                    $ E_DailyActions.append("no gift panties") 
            else: 
                ch_e "I already have one of those."                
            
            
        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: #If you have a vibrator, you'll give it.
            $ Count = E_Inventory.count("Dazzler and Longshot")
            if "Dazzler and Longshot" not in E_Inventory:                            
                "You give Emma the book."
                $ E_Blush = 1
                if ApprovalCheck("Emma", 600, "L"):                    
                    call EmmaFace("angry") from _call_EmmaFace_738
                    ch_e "Is this the type of thing you expect from me. . ."
                    call EmmaFace("sadside", Mouth="lipbite") from _call_EmmaFace_739
                    ch_e "we'll have to see. . ."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                else:
                    call EmmaFace("angry") from _call_EmmaFace_740
                    ch_e "I don't exactly read this dime store trash. . ."
                    call EmmaFace("sadside", Mouth="lipbite") from _call_EmmaFace_741
                    ch_e "but I will take it. . ."
                $ P_Inventory.remove("Dazzler and Longshot")
                $ E_Inventory.append("Dazzler and Longshot") 
                $ E_Love = Statupdate("Emma", "Love", E_Love, 200, 50) 
            else: 
                ch_e "You're repeating yourself."                
            
        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: #If you have a book, you'll give it.
            $ Count = E_Inventory.count("256 Shades of Grey")
            if "256 Shades of Grey" not in E_Inventory:                            
                "You give Emma the book."
                $ E_Blush = 1
                if ApprovalCheck("Emma", 500, "O"):                    
                    call EmmaFace("bemused") from _call_EmmaFace_742
                    ch_e "I expect it might be somewhat entertaining."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                else:
                    call EmmaFace("confused") from _call_EmmaFace_743 
                    ch_e "I've heard of that one."  
                    call EmmaFace("bemused") from _call_EmmaFace_744             
                $ P_Inventory.remove("256 Shades of Grey")
                $ E_Inventory.append("256 Shades of Grey")                    
                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 200, 50)  
            else: 
                ch_e "You're repeating yourself."                  
            
        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: #If you have a book, you'll give it.
            $ Count = E_Inventory.count("256 Shades of Grey")
            if "Avengers Tower Penthouse" not in E_Inventory:                            
                "You give Emma the book."
                $ E_Blush = 1
                if ApprovalCheck("Emma", 500, "I"):                    
                    call EmmaFace("bemused") from _call_EmmaFace_745
                    ch_e "Perhaps don't visit unannounced. . ."
                    $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 89, 10)
                else:
                    call EmmaFace("sly") from _call_EmmaFace_746
                    ch_e "I normally confiscate such things. . . I'll just do that now. . ."  
                    call EmmaFace("bemused") from _call_EmmaFace_747               
                $ P_Inventory.remove("Avengers Tower Penthouse")
                $ E_Inventory.append("Avengers Tower Penthouse")                    
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 200, 50)  
            else: 
                ch_e "You're repeating yourself."                     
            

        "Exit":
            pass
    
    return


# start Emma_Names//////////////////////////////////////////////////////////
label Emma_Names(TempName=0):    
    call LastNamer from _call_LastNamer_2
    $ TempName = _return
    menu:
        ch_e "Oh? What would you like me to call you?"
        "[TempName]'s fine.":
            # ie "Mr. Zero"
            $ E_Petname = TempName
            ch_e "I assumed it was, [E_Petname]."
        "Call me by my name.":
            $ E_Petname = Playername            
            ch_e "If you'd rather, [E_Petname]."
        "Call me \"darling\"." if "darling" in E_Petnames:
            $ E_Petname = "darling"
            ch_e "Certainly, [E_Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in E_Petnames:
            $ E_Petname = "boyfriend"
            ch_e "How pedestrian, but fine, [E_Petname]."
        "Call me \"lover\"." if "lover" in E_Petnames:
            $ E_Petname = "lover"
            ch_e "Certainly, [E_Petname]."
        "Call me \"sir\"." if "sir" in E_Petnames:
            $ E_Petname = "sir"
            ch_e "Yes, [E_Petname]."
        "Call me \"master\"." if "master" in E_Petnames:
            $ E_Petname = "master"
            ch_e "As you wish, [E_Petname]."
        "Call me \"sex friend\"." if "sex friend" in E_Petnames:
            $ E_Petname = "sex friend"
            ch_e "You naughty boy. Very well, [E_Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in E_Petnames:
            $ E_Petname = "fuck buddy"
            ch_e "How nasty, \"[E_Petname]\"."        
        "Call me \"daddy\"." if "daddy" in E_Petnames:
            $ E_Petname = "daddy"
            ch_e "Mmm, ok, [E_Petname]."
        "Nevermind.":
            return
    return
# end Emma_Names//////////////////////////////////////////////////////////

label Emma_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Ms. Frost.":
                        $ E_Pet = "Ms. Frost"            
                        $ EmmaName = "Ms. Frost"
                        ch_e "I don't see why not, [E_Petname]."
                        
                    "I think I'll just call you Emma.":
                        if ApprovalCheck("Emma", 700) or "classcaught" in E_History:
                            ch_e "I don't see why not, [E_Petname]."   
                            $ E_Pet = "Emma"            
                            $ EmmaName = "Emma"
                        else:
                            ch_e "I'd rather you didn't, [E_Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ E_Pet = "girl"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 600, "L"):
                            call EmmaFace("sexy", 1) from _call_EmmaFace_748 
                            ch_e "How droll, [E_Petname]."
                        else:      
                            call EmmaFace("angry") from _call_EmmaFace_749           
                            ch_e "I wouldn't, [E_Petname]." 
                            
                    "I think I'll call you \"diamond\".":
                        $ E_Pet = "diamond"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 800, "L"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_750 
                            ch_e "How adorable, [E_Petname]."
                        else:     
                            call EmmaFace("angry") from _call_EmmaFace_751            
                            ch_e "I'm no such thing,  [E_Petname]."
                            
                    "I think I'll call you \"teacher\".":
                        $ E_Pet = "bae"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 800, "L"):
                            call EmmaFace("sexy", 1) from _call_EmmaFace_752 
                            ch_e "I suppose I am your. . . \"teacher?\""
                        else:     
                            call EmmaFace("angry") from _call_EmmaFace_753            
                            ch_e "What does that even mean?."
                            
                    "I think I'll call you \"baby\".":
                        $ E_Pet = "baby"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 500, "L"):
                            call EmmaFace("sexy", 1) from _call_EmmaFace_754 
                            ch_e "How precious."
                        else:     
                            call EmmaFace("angry") from _call_EmmaFace_755            
                            ch_e "I think I'm a bit. . . mature for that." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ E_Pet = "sweetie"
                        if "boyfriend" in E_Petnames or ApprovalCheck("Emma", 500, "L"):
                            ch_e "Really, [E_Petname]?"
                        else:     
                            call EmmaFace("angry", 1) from _call_EmmaFace_756            
                            ch_e "Too saccharine, [E_Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ E_Pet = "sexy"
                        if "lover" in E_Petnames or ApprovalCheck("Emma", 900):
                            call EmmaFace("sexy", 1) from _call_EmmaFace_757 
                            ch_e "I can't argue there, [E_Petname]."
                        else:        
                            call EmmaFace("angry", 1) from _call_EmmaFace_758         
                            ch_e "That may be a bit much, [E_Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ E_Pet = "lover"
                        if "lover" in E_Petnames or ApprovalCheck("Emma", 900, "L"):
                            call EmmaFace("sexy", 1) from _call_EmmaFace_759 
                            ch_e "I do love you, [E_Petname]!"
                        else:      
                            call EmmaFace("angry", 1) from _call_EmmaFace_760           
                            ch_e "Not in this lifetime, [E_Petname]."  
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ E_Pet = "slave"
                        if "master" in E_Petnames or ApprovalCheck("Emma", 700, "O"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_761 
                            ch_e "As you wish, [E_Petname]."
                        else:      
                            call EmmaFace("angry", 1) from _call_EmmaFace_762           
                            ch_e "I'm not slave, [E_Petname]."
                                            
                    "I think I'll call you \"bitch\".":
                        $ E_Pet = "bitch"
                        if "master" in E_Petnames or ApprovalCheck("Emma", 600, "O"):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_763 
                            ch_e "Hmm, make me your bitch, [E_Petname]."
                        else:             
                            call EmmaFace("angry", 1) from _call_EmmaFace_764    
                            ch_e "I'm a goddamm Queen, [E_Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ E_Pet = "slut"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 1000, "OI"):
                            call EmmaFace("sexy") from _call_EmmaFace_765 
                            ch_e "If the name fits, [E_Petname]."
                        else:                
                            call EmmaFace("angry", 1) from _call_EmmaFace_766 
                            $ E_Mouth = "surprised"
                            ch_e "Not unless you want to lose some teeth!" 
                            
                    "I think I'll call you \"whore\".":
                        $ E_Pet = "whore"
                        if "fuckbuddy" in E_Petnames or ApprovalCheck("Emma", 1100, "OI"):
                            call EmmaFace("sly") from _call_EmmaFace_767 
                            ch_e "Only for you though. . ."
                        else:        
                            call EmmaFace("angry", 1) from _call_EmmaFace_768         
                            ch_e "Can you say that with a broken jaw, [E_Petname]?" 
                                                   
                    "I think I'll call you \"dairy queen\".":
                        $ E_Pet = "dairy queen"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 1400):
                            call EmmaFace("sly", 1) from _call_EmmaFace_769 
                            ch_e "So you like some Premium Milk then?"
                        else:     
                            call EmmaFace("angry", 1) from _call_EmmaFace_770            
                            ch_e "You think i'm some kind of cow, [E_Petname]." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ E_Pet = "sex friend"
                        if "sex friend" in E_Petnames or ApprovalCheck("Emma", 600, "I"):
                            call EmmaFace("sly") from _call_EmmaFace_771 
                            ch_e "Hmmm i kinda like it. . ."
                        else:                
                            call EmmaFace("angry", 1) from _call_EmmaFace_772 
                            ch_e "Not out loud, [E_Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ E_Pet = "fuckbuddy"
                        if "fuckbuddy" in E_Petnames or ApprovalCheck("Emma", 700, "I"):
                            call EmmaFace("sly") from _call_EmmaFace_773 
                            ch_e "Yup."
                        else:                
                            call EmmaFace("angry", 1) from _call_EmmaFace_774
                            $ E_Mouth = "surprised"
                            ch_e "Don't even joke, [E_Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ E_Pet = "baby girl"
                        if "daddy" in E_Petnames or ApprovalCheck("Emma", 1200):
                            call EmmaFace("smile", 1) from _call_EmmaFace_775 
                            ch_e "You know it, [E_Petname]."
                        else:                
                            call EmmaFace("angry", 1) from _call_EmmaFace_776 
                            ch_e "I'm no kid!" 
                    
                    "I think I'll call you \"mommy\".":
                        $ E_Pet = "mommy"
                        if "mommy" in E_Pets or ApprovalCheck("Emma", 1500):
                            call EmmaFace("sly", 1, Mouth="kiss") from _call_EmmaFace_777 
                            ch_e "Oooh, [E_Petname]."
                        else:     
                            call EmmaFace("angry") from _call_EmmaFace_778            
                            ch_e "That's a bit much, [E_Petname]" 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Emma_Namecheck(E_Pet = E_Pet, Cnt = 0, Ugh = 0):#E_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if E_Pet == "Emma":
        return Ugh   
    if E_Pet == "Ms. Frost":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if E_Pet == "girl":                                         #easy options
        if ApprovalCheck("Emma", 500, "L", TabM=1):            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1)
            $ Ugh = 1
    elif E_Pet == "diamond" or E_Pet == "teacher":
        if ApprovalCheck("Emma", 500, "L", TabM=1):
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -2)
            $ Ugh = 1
    elif E_Pet == "baby":    
        if ApprovalCheck("Emma", 500, "L", TabM=1):
            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 30, -1)
            $ Ugh = 1
    elif E_Pet == "kitten":
        if ApprovalCheck("Emma", 600, "L", TabM=1):
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1)
            $ Ugh = 1
    elif E_Pet == "sweetie":
        if not ApprovalCheck("Emma", 500, "L", TabM=1):
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 1)  
        else:
            $ E_Love = Statupdate("Emma", "Love", E_Love, 40, -1)
            $ Ugh = 1
            
    elif E_Pet == "sexy" or E_Pet == "lover":
        if ApprovalCheck("Emma", 900, TabM=1):                                                        #over 150
            $ E_Love = Statupdate("Emma", "Love", E_Love, 80, 2)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1) 
        else:                                                            
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "slave":                                        #tougher options
        if ApprovalCheck("Emma", 800, "O", TabM=3):                                            #over 80
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, (3+Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, (2+Cnt))
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)     
        elif ApprovalCheck("Emma", 500, "O", TabM=3):                                                  #between 50 and 80
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 81, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)        
        else:                                                                                           # under 50
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -1)
            $ Ugh = 1
    
    elif E_Pet == "bitch":                                        #tougher options
        if ApprovalCheck("Emma", 1500, TabM=2):                                            #over 150
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, (3+Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, (2+Cnt))
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)     
        elif ApprovalCheck("Emma", 1200, TabM=2):                                                  #between 120 and 150
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 60, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 81, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)        
        else:                                                                                           # under 120
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, -1)
            $ Ugh = 1
            
    elif E_Pet == "slut":
        if ApprovalCheck("Emma", 500, "O", TabM=2) or ApprovalCheck("Emma", 500, "I", TabM=2):        #over 50
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, (4+Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, (2+Cnt))
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1)
        elif ApprovalCheck("Emma", 300, "O", TabM=2) or ApprovalCheck("Emma", 300, "I", TabM=2):      #between 30 and 50
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, (2+Cnt))
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)        
        else:                                                                                           # under 40
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-2-Cnt))
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-1-Cnt), 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "whore":
        if ApprovalCheck("Emma", 600, "O", TabM=2) or ApprovalCheck("Emma", 600, "I", TabM=2):        #over 60
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 4)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1)
        elif ApprovalCheck("Emma", 400, "O", TabM=2) or ApprovalCheck("Emma", 400, "I", TabM=2):      #between 40 and 60
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 1)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-2-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
        else:                                                                                           # under 40
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-3-Cnt))
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-2-Cnt), 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 21, 1, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "dairy queen":
        if ApprovalCheck("Emma", 1500, TabM=1):                                                        #over 150
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
        else:                                                                       
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-2-Cnt))
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "sex friend":    
        if ApprovalCheck("Emma", 750, "O", TabM=1) or ApprovalCheck("Emma", 600, "I", TabM=1):        #over 75/60
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 3)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 1)
        elif ApprovalCheck("Emma", 600, "O", TabM=1) or ApprovalCheck("Emma", 400, "I", TabM=1):      #between 60/40 and 75/60
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
            $ E_Blush = 1
        else:                                                                                           # under 60/40
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -Cnt)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-1-Cnt), 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "fuckbuddy":
        if ApprovalCheck("Emma", 700, "O", TabM=2) or ApprovalCheck("Emma", 700, "I", TabM=1):        #over 70/70
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 3)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 95, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 85, 1)
        elif ApprovalCheck("Emma", 600, "O", TabM=2) or ApprovalCheck("Emma", 500, "I", TabM=1):      #between 60/50 and 70/70
            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 90, 2)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)
            $ E_Blush = 1
        else:                                                                                           #under 60/50
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, -Cnt)
            $ E_Love = Statupdate("Emma", "Love", E_Love, 60, (-2-Cnt), 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    elif E_Pet == "baby girl":
        if ApprovalCheck("Emma", 1200, TabM=1):                                                        #over 150
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 1)
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 1)            
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2)
        else:                                                                       
            $ E_Love = Statupdate("Emma", "Love", E_Love, 200, (-2-Cnt))
            $ E_Love = Statupdate("Emma", "Love", E_Love, 50, (-1-Cnt))
            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Emma_Personality//////////////////////////////////////////////////////////
label Emma_Personality(Cnt = 0):   
    if not E_Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Emma to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_e "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if E_Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_e "Anything to humor you, [E_Petname]."
            $ E_Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if E_Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_e "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ E_Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if E_Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_e "If you say so."
            $ E_Chat[4] = 3
        "More Loving. [[Obedience to Love]" if E_Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_e "I'll try to."
            $ E_Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if E_Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_e "Does that get you off?"
            $ E_Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if E_Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_e "We do have fun. . ."
            $ E_Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if E_Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_e "As if I ever do anything else?"
            $ E_Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Emma_Personality
        "Nevermind.":
            return
    return
# end Emma_Personality//////////////////////////////////////////////////////////




# Emma_Summon//////////////////////////////////////////////////////////

label Emma_Summon(Tempmod=Tempmod):
    call EmmaOutfit from _call_EmmaOutfit_32  
    if "no summon" in E_RecentActions:
                if "angry" in E_RecentActions:
                    ch_e "I'm not in the mood for this, [E_Petname]."
                elif Action_Check("Emma", "recent", "no summon") > 1:
                    ch_e "You heard me the first time."
                    $ E_RecentActions.append("angry") 
                elif Current_Time == "Night": 
                    ch_e "It's past your bedtime."
                else:
                    ch_e "As I said, I've got things to do."   
                $ E_RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Emma", 700, "L") or ApprovalCheck("Emma", 300, "O"):                              
                        #It's night time but she likes you.
                        ch_e "It's getting late, but fine, what did you want?"
                        $ E_Loc = bg_current 
                        call Set_The_Scene from _call_Set_The_Scene_135
                else:                                                           
                        #It's night time and she isn't into you
                        ch_e "It's late, [E_Petname], tell me tomorrow."       
                        $ E_RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if E_Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -30
    elif E_Loc == "bg classroom":
        $ Tempmod = 10
    elif E_Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif E_Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Emma", 700, "L") or not ApprovalCheck("Emma", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Emma", 300):
                ch_e "I don't really feel up to that, [E_Petname]."       
                $ E_RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in E_RecentActions:
                pass
        elif "goto" in E_RecentActions:
                ch_e "You only just left, why not return?"
        elif E_Loc == "bg classroom" or E_Loc == "bg teacher":
                ch_e "You can find me in the class room, [E_Petname]."
        elif E_Loc == "bg dangerroom": 
                ch_e "I'm getting some training in, [E_Petname], care to join me?"    
        elif E_Loc == "bg campus": 
                ch_e "I'm relaxing in the square, if you'd care to join me." 
        elif E_Loc == "bg emma": 
                ch_e "I'm in my room, [E_Petname]." 
        elif E_Loc == "bg player": 
                ch_e "I'm waiting in your room, [E_Petname]. . ."   
        elif E_Loc == "bg showerroom":    
            if ApprovalCheck("Emma", 1600):
                ch_e "I'm in the shower right now, [E_Petname], do you need an invitation?"
            else:            
                ch_e "I'm in the shower right now, [E_Petname], perhaps I'll see you later."       
                $ E_RecentActions.append("no summon")         
                return      
        elif E_Loc == "hold":
                ch_e "I'm off campus for a bit, I'll be back later."       
                $ E_RecentActions.append("no summon") 
                return      
        else:        
                ch_e "You could always come over here, [E_Petname]."    
           
           
        if "summoned" in E_RecentActions:
            ch_e "Again? Very well."           
            $ Line = "yes"            
        elif "goto" in E_RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_e "I'll be waiting."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_e "Very well."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Emma", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Emma", 1400):                         
                                #she is generally favorable 
                                ch_e "Hmm, very well."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Emma", 200, "O"):                                  
                                #she is not obedient  
                                ch_e "If you're lucky, I'll still be here when you arrive."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 55, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                    ch_e "I'll be waiting."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)                            
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                    ch_e "Very well."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)                   
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Emma", 600, "O"):                              
                        #she is obedient
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, 1, 1)    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 40, -1)                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Emma", 1400):       
                        #she is generally favorable
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1)  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)                                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)  
                        ch_e "Ok, fine, [E_Petname]."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Emma", 200, "O"):                                         
                        #she is not obedient   
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -2)   
                        ch_e "Who do you think is in charge here?!"                             
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)    
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, -2)
                        ch_e "You'd better hope you don't find me here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)                                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if E_Love > E_Obed:
            ch_e "I'd love to."
        else:
            ch_e "I'll be right there, [E_Petname]."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ E_RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if E_Loc == "bg teacher":
                ch_e "I can't exactly leave class, [E_Petname]." 
            elif E_Loc == "bg classroom":
                ch_e "I have a lot of paperwork, [E_Petname]." 
            elif E_Loc == "bg dangerroom": 
                ch_e "I'm just getting warmed up here."
            else:
                ch_e "I have a lot to finish up here."          
            $ E_RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ Tempmod = 0
            $ E_RecentActions.append("goto")  
            if E_Loc == "bg classroom" or E_Loc == "bg teacher":
                    ch_e "You don't want to miss too much."
                    jump Class_Room 
            elif E_Loc == "bg dangerroom": 
                    ch_e "I'll try to save some for you."
                    jump Danger_Room
            elif E_Loc == "bg emma": 
                    ch_e "I'll just meet you in your room instead."
                    $ E_Loc = "bg player"
                    jump Player_Room    
        #            ch_e "I'll clean up a few things."
        #            jump Emma_Room
            elif E_Loc == "bg player": 
                    ch_e "I'll be waiting for you."
                    jump Player_Room                
            elif E_Loc == "bg showerroom": 
                    ch_e "Don't keep me waiting. . ."
                    jump Shower_Room
            elif E_Loc == "bg campus": 
                    ch_e "I've got a nice location picked out."
                    jump Campus
            else:
                    ch_e "I'll just meet you in your room instead."
                    $ E_Loc = "bg player"
                    jump Player_Room    
        #            ch_e "You know, I'll just meet you in my room."
        #            $ E_Loc = "bg emma"
        #            jump Emma_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well, we can't have that now."
    elif Line == "command": 
            ch_e "If I must. . ."
        
    $ E_RecentActions.append("summoned")  
    $ Line = 0
    ch_e "I'll be there in a minute."                                
    $ E_Loc = bg_current 
    call EmmaOutfit from _call_EmmaOutfit_33
    call Set_The_Scene from _call_Set_The_Scene_136
    return

# End Emma Summon ///////////////////    


label Emma_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in E_RecentActions:
        call DrainWord("Emma","leaving") from _call_DrainWord_134
    else:
        return
    
    if E_Loc == "hold":   
            # Activates if she's being moved out of play
            ch_e "Sorry, I have some business to attend to." 
            return
            
    if "Emma" in Party or "lockedtravels" in E_Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ E_Loc = bg_current 
            return
      
    elif "freetravels" in E_Traits or not ApprovalCheck("Emma", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call EmmaOutfit from _call_EmmaOutfit_34           
            if GirlsNum: #if someone left before her
                        ch_e "I have to head out as well."
                        
            if E_Loc == "bg teacher":
                        ch_e "I have a class to teach."
            elif E_Loc == "bg classroom":
                        ch_e "I have some paperwork to take care of."
            elif E_Loc == "bg dangerroom": 
                        ch_e "I have a workout scheduled."   
            elif E_Loc == "bg campus": 
                        ch_e "I'm going to take in some sun." 
            elif E_Loc == "bg emma": 
                        ch_e "I'm heading back to my room." 
            elif E_Loc == "bg player": 
                        ch_e "I'll be heading to your room."   
            elif E_Loc == "bg showerroom" and ApprovalCheck("Emma", 1400):
                        ch_e "I'm going to take a quick shower."
            elif E_Loc == "bg pool": 
                        ch_e "I'm heading to the pool."               
            else:        
                        ch_e "I'll see you later."                  
            hide Emma_Sprite
            return     
            #End Free Travels
    
    call EmmaOutfit from _call_EmmaOutfit_35  
    
    if "follow" not in E_Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ E_Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if E_Loc == "bg teacher": #fix change these if changed function
        $ Tempmod = -40
    elif E_Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif E_Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif E_Loc == "bg showerroom":    
        $ Tempmod = 20
    elif E_Loc == "bg pool":
        $ Tempmod = 20
    
    
    if GirlsNum: #if someone left before her
                ch_e "I'm leaving as well."
                
    if E_Loc == "bg teacher":
        ch_e "I've got a class to teach, but you could probably learn a thing or two from it."
    elif E_Loc == "bg classroom":
        ch_e "I have some paperwork to take care of, but you could keep me company."
    elif E_Loc == "bg dangerroom": 
        ch_e "I have a workout planned, but there's room for one more."    
    elif E_Loc == "bg campus": 
        ch_e "I'm planning to get some sunning in, care to join me?" 
    elif E_Loc == "bg emma": 
        ch_e "I'm heading back to my room, but you can walk me back." 
    elif E_Loc == "bg player": 
        ch_e "I'm actually heading to your room, [E_Petname]."   
    elif E_Loc == "bg showerroom":    
        if ApprovalCheck("Emma", 1600):
            ch_e "I'm catching a quick shower, care to join me?"
        else:            
            ch_e "I'm headed for the showers, make sure to keep your distance."
            return        
    else:        
        ch_e "Would you care to come with me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in E_RecentActions:
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 55, 1) 
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in E_RecentActions:
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)                            
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 2)
                ch_e "Very well, I'll talk to you later."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Emma", 600, "L") or ApprovalCheck("Emma", 1400):                
                    if "followed" not in E_RecentActions:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)                   
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in E_RecentActions:
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                    $ Line = "no"
                
        "No, stay here.":
                if ApprovalCheck("Emma", 600, "O"):                              
                    #she is obedient
                    if "followed" not in E_RecentActions:
                        if E_Love >= 50:
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 1)    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 40, -1)                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Emma", 1400):       
                    #she is generally favorable
                    if "followed" not in E_RecentActions:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -2)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -1)  
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 2)                                
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 1)  
                    ch_e "I guess it wasn't that important. . ."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Emma", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in E_RecentActions:
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -4)  
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, -2)   
                    ch_e "Does that work with your little strumpets?"  
                    if "followed" not in E_RecentActions:                       
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 40, 2)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 1)    
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, -2)
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in E_RecentActions:
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 1)
                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 1)                                    
                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -1, 1)
                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ E_RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma") from _call_Gym_Clothes_23
            call Pool_Clothes("auto", "Emma") from _call_Pool_Clothes_17
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if E_Loc == "bg teacher":
                ch_e "I'm not \"cutting class,\" [E_Petname]." 
            elif E_Loc == "bg classroom":
                ch_e "I'm afraid not, [E_Petname], I need to get this work done." 
            elif E_Loc == "bg dangerroom": 
                ch_e "I'm sorry, but how do you think I keep this figure?"
            else:
                ch_e "I'm sorry, I'm just much too busy at the moment."         
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma") from _call_Gym_Clothes_24         
            call Pool_Clothes("auto", "Emma") from _call_Pool_Clothes_18         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving") from _call_DrainWord_135  
            call DrainWord("All","arriving") from _call_DrainWord_136        
            hide Emma_Sprite
            call Gym_Clothes("auto", "Emma") from _call_Gym_Clothes_25
            call Pool_Clothes("auto", "Emma") from _call_Pool_Clothes_19
            if E_Loc == "bg teacher":
                ch_e "I'll see you there."            
                jump Class_Room_Entry
            elif E_Loc == "bg classroom":
                ch_e "Excellent, that should pass the time."            
                jump Class_Room_Entry
            elif E_Loc == "bg dangerroom": 
                ch_e "I'll try to leave some for you."
                jump Danger_Room_Entry
            elif E_Loc == "bg emma": 
                $ E_Loc = "bg player"
                ch_e "Let's meet in your room instead."
                jump Player_Room     
#                ch_e "I'll be waiting."
#                jump Emma_Room
            elif E_Loc == "bg player": 
                ch_e "I'll be waiting."
                jump Player_Room                
            elif E_Loc == "bg showerroom": 
                ch_e "I'll get started."
                jump Shower_Room_Entry
            elif E_Loc == "bg campus": 
                ch_e "Ok, let's."
                jump Campus_Entry
            elif E_Loc == "bg pool": 
                ch_e "Ok, let's."
                jump Pool_Entry
            else:     
                $ E_Loc = "bg player"
                ch_e "Let's meet in your room instead."
                jump Player_Room       
#                ch_e "You know, I'll just meet you in my room."
#                $ E_Loc = "bg emma"
#                jump Emma_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_e "Well we wouldn't want that. . ."
    elif Line == "command": 
            ch_e "If you insist."
    
    $ Line = 0
    ch_e "I suppose I can stay for a while."                                
    $ E_Loc = bg_current 
    return

# End Emma Leave ///////////////////   

label Emma_Dismissed(Leaving = 0):
    if "Emma" in Party:        
            $ Party.remove("Emma")
    call Emma_Schedule(0) from _call_Emma_Schedule_3 #if E_Loc == bg_current then it means she wants to stay here
    menu:
        "You can leave if you like.":
                if E_Loc != bg_current and not ApprovalCheck("Emma", 600, "O"):
                        ch_e "Be that as it may, I'll stick around for a bit."
                else:
                        ch_e "Very well, [E_Petname]"
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if E_Loc != bg_current and not ApprovalCheck("Emma", 800, "LO"):
                        ch_e "As it happens, I don't have any other plans."
                elif not ApprovalCheck("Emma", 500, "LO"):
                        ch_e "I don't think that I can."               
                else:
                        if "dismissed" not in E_DailyActions:
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 30, 7)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 5)
                        ch_e "Very well. . ." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if E_Loc != bg_current and not ApprovalCheck("Emma", 450, "O"):
                        ch_e "No, I don't believe that I can."
                elif not ApprovalCheck("Emma", 250, "O"):
                        call EmmaFace("confused") from _call_EmmaFace_779 
                        ch_e "Now I am intrigued."
                else:
                        if "dismissed" not in E_DailyActions:
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 10)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 7)
                        ch_e "Very well. . ."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if E_Loc != bg_current and (ApprovalCheck("Emma", 1200, "LO") or ApprovalCheck("Emma", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in E_DailyActions:
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                ch_e "Very well. . ."  
                                $ Leaving = 1                                  
                        elif E_Loc != bg_current and (ApprovalCheck("Emma", 1000, "LO") or ApprovalCheck("Emma", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in E_DailyActions:
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -5, 1)
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -5, 1)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 60, 10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                call EmmaFace("angry") from _call_EmmaFace_780 
                                ch_e "I'll leave, but do not test me, [E_Petname]"      
                                $ Leaving = 1                         
                        elif E_Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in E_DailyActions:
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -5, 1)
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -10, 1)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -3)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 3)
                                call EmmaFace("angry") from _call_EmmaFace_781 
                                ch_e "Well now I'm definitely not."          
                        elif ApprovalCheck("Emma", 1400, "LO") or ApprovalCheck("Emma", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in E_DailyActions:
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -5, 1)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 10)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 5)
                                call EmmaFace("sad") from _call_EmmaFace_782 
                                ch_e "I suppose I could get out of your way."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in E_DailyActions:
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 50, -5, 1)
                                        $ E_Love = Statupdate("Emma", "Love", E_Love, 70, -10, 1)
                                        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, -5)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 3)
                                        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 80, 2)
                                call EmmaFace("sad") from _call_EmmaFace_783 
                                ch_e "That doesn't look like it'll be happening."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in E_DailyActions:
            $ E_DailyActions.append("dismissed")        
    if Leaving == 0:
            # Stay
            $ E_Loc = bg_current
    else:
            # Go
            if E_Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg emma":
                $ E_Loc = "bg campus"
            else:
                $ E_Loc = "bg emma"
            hide Emma_Sprite
            "Emma heads out." 
    return
    #end "you can leave"
    

label Emma_AboutRogue:
    ch_e "What do I think about her? Well. . ."
    
    if "poly rogue" in E_Traits:  
        ch_e "As you're aware, we've shared a great deal. . ."    
    elif E_LikeRogue >= 900:
        ch_e "I do find her rather mesmerizing. . ."
    elif E_LikeRogue >= 800:
        ch_e "That accent certainly did grow on me. . ."    
    elif E_LikeRogue >= 700:
        ch_e "We've become quite close."
    elif E_LikeRogue >= 600:
        ch_e "I'm rather fond of her."
    elif E_LikeRogue >= 500:
        ch_e "She's an adequate student."
    elif E_LikeRogue >= 400:
        ch_e "She can be a bit of a handful."
    elif E_LikeRogue >= 300:
        ch_e "I can barely tollerate her disrespectful nature." 
    else:
        ch_e "That swamp rat? What about her?"          
    return
label Emma_AboutKitty:
    ch_e "What do I think about her? Well. . ."
    
    if "poly kitty" in E_Traits:  
        ch_e "As you're aware, we do get along quite well. . ."    
    elif E_LikeKitty >= 900:
        ch_e "She is rather. . . flexible. . ."
    elif E_LikeKitty >= 800:
        ch_e "She is rather adorable. . ."    
    elif E_LikeKitty >= 700:
        ch_e "She's something of a friend at this point."
    elif E_LikeKitty >= 600:
        ch_e "Once you get to know her, she's not bad."
    elif E_LikeKitty >= 500:
        ch_e "She's an adequate student."
    elif E_LikeKitty >= 400:
        ch_e "She can be a bit of a know it all."
    elif E_LikeKitty >= 300:
        ch_e "I can't stand her constant questions." 
    else:
        ch_e "That little bitch?"
          
    return
    
#End Emma_AboutRogue
    

## Emma's Clothes ///////////////////
label Emma_Clothes(Public=0,Bonus=0):   
    if "exhibitionist" in E_Traits:
            $ Public += 1
    if E_Rep <= 200:
            $ Public += 2
    elif E_Rep <= 400:
            $ Public += 1        
    if "public" in E_History:
            $ Public += 2
    #This is a trait for if she's open to being sexy in public
        
    call EmmaFace from _call_EmmaFace_784
    menu:
        ch_e "You wanted to discuss my clothing choices?"
        "Let's talk about your outfits.":
                    jump Emma_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Emma_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Emma_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Emma_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Emma_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Emma_OutfitShame(3,1) from _call_Emma_OutfitShame_1
                    "Custom 2":
                                call Emma_OutfitShame(5,1) from _call_Emma_OutfitShame_2
                    "Custom 3":
                                call Emma_OutfitShame(6,1) from _call_Emma_OutfitShame_3
                    "Gym Clothes":
                                call Emma_OutfitShame(7,1) from _call_Emma_OutfitShame_4
                    "Sleepwear":
                                call Emma_OutfitShame(9,1) from _call_Emma_OutfitShame_5
                    "Never mind":
                                pass
        "Never mind, you look good like that.":
                if "wardrobe" not in E_RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if E_Chat[1] <= 1:                
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 15)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 20)
                                ch_e "I thought so as well."
                        elif E_Chat[1] <= 10:
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 5)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 7)
                                ch_e "Isn't it?" 
                        elif E_Chat[1] <= 50:
                                $ E_Love = Statupdate("Emma", "Love", E_Love, 70, 1)
                                $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 40, 1) 
                        $ E_RecentActions.append("wardrobe")   
                $ E_OutfitDay = E_Outfit           
                $ E_Chat[1] += 1                
                return
#        "Let's talk about your underwear1.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear2.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear3.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear4.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear5.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear6.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear7.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear8.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear9.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear10.":
#            jump Emma_Clothes_Under
#        "Let's talk about your underwear11.":
#            jump Emma_Clothes_Under

            
    jump Emma_Clothes
    #End of Emma Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Outfits:                                                                                 # Outfits
        "I really like that teacher's look you wear.": 
            call EmmaOutfit("teacher") from _call_EmmaOutfit_36   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ E_Outfit = "teacher"
                    $ E_Shame = E_OutfitShame[1]
                    ch_e "Yes, a very tasteful look."
                "Let's try something else though.":
                    ch_e "Very well."            
                    
        "That combat uniform you have looks really nice on you.":
            call EmmaOutfit("costume") from _call_EmmaOutfit_37
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ E_Outfit = "costume"
                    $ E_Shame = E_OutfitShame[2]
                    ch_e "I really enjoyed wearing that one."
                "Let's try something else though.":
                    ch_e "Very well."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not E_Custom[0] and not E_Custom2[0] and not E_Custom3[0] and not E_Custom4[0] and not E_Custom5[0] and not E_Custom6[0] and not E_Custom7[0]:
                        pass       
                        
        "Remember that outfit we put together?" if E_Custom[0] or E_Custom2[0] or E_Custom3[0] or E_Custom4[0] or E_Custom5[0] or E_Custom6[0] or E_Custom7[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not E_Custom[0]:
                        pass
                    "Throw on Custom 1" if E_Custom[0]:
                        call EmmaOutfit("custom1") from _call_EmmaOutfit_38
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not E_Custom2[0]:
                        pass
                    "Throw on Custom 2" if E_Custom2[0]:
                        call EmmaOutfit("custom2") from _call_EmmaOutfit_39
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not E_Custom3[0]:
                        pass
                    "Throw on Custom 3" if E_Custom3[0]:
                        call EmmaOutfit("custom3") from _call_EmmaOutfit_40
                        $ Cnt = 6
                    "Throw on Custom 4 (locked)" if not E_Custom4[0]:
                        pass
                    "Throw on Custom 4" if E_Custom4[0]:
                        call EmmaOutfit("custom4") from _call_EmmaOutfit_41
                        $ Cnt = 11
                    "Throw on Custom 5 (locked)" if not E_Custom5[0]:
                        pass
                    "Throw on Custom 5" if E_Custom5[0]:
                        call EmmaOutfit("custom5") from _call_EmmaOutfit_42
                        $ Cnt = 12
                    "Throw on Custom 6 (locked)" if not E_Custom6[0]:
                        pass
                    "Throw on Custom 6" if E_Custom6[0]:
                        call EmmaOutfit("custom6") from _call_EmmaOutfit_43
                        $ Cnt = 13
                    "Throw on Custom 7 (locked)" if not E_Custom7[0]:
                        pass
                    "Throw on Custom 7" if E_Custom7[0]:
                        call EmmaOutfit("custom7") from _call_EmmaOutfit_44
                        $ Cnt = 14
                    
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ E_Schedule[9] = "custom2"
                        elif Cnt == 6:
                            $ E_Schedule[9] = "custom3"
                        elif Cnt == 11:
                            $ E_Schedule[9] = "custom4"
                        elif Cnt == 12:
                            $ E_Schedule[9] = "custom5"
                        elif Cnt == 13:
                            $ E_Schedule[9] = "custom6"
                        elif Cnt == 14:
                            $ E_Schedule[9] = "custom7"
                        else:
                            $ E_Schedule[9] = "custom"
                        ch_e "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if E_Custom[0]:
                                ch_e "Very well."
                                $ E_Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not E_Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if E_Custom2[0]:
                                ch_e "Very well."
                                $ E_Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not E_Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if E_Custom3[0]:
                                ch_e "Very well."
                                $ E_Custom3[0] = 0
                            "Custom 3 [[clear custom 1] (locked)" if not E_Custom3[0]:
                                pass

                            "Custom 4 [[clear custom 4]" if E_Custom4[0]:
                                ch_e "Ok, no problem."
                                $ E_Custom4[0] = 0
                            "Custom 4 [[clear custom 1] (locked)" if not E_Custom4[0]:
                                pass
                            "Custom 5 [[clear custom 5]" if E_Custom5[0]:
                                ch_e "Ok, no problem."
                                $ E_Custom5[0] = 0
                            "Custom 5 [[clear custom 1] (locked)" if not E_Custom5[0]:
                                pass
                            "Custom 6 [[clear custom 6]" if E_Custom6[0]:
                                ch_e "Ok, no problem."
                                $ E_Custom6[0] = 0
                            "Custom 6 [[clear custom 1] (locked)" if not E_Custom6[0]:
                                pass
                            "Custom 7 [[clear custom 7]" if E_Custom7[0]:
                                ch_e "Ok, no problem."
                                $ E_Custom7[0] = 0
                            "Custom 7 [[clear custom 1] (locked)" if not E_Custom7[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Emma_Custom_Out(Cnt) from _call_Emma_Custom_Out
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Emma_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     
            #Nude
            call EmmaFace("sly", 1) from _call_EmmaFace_785
            $ Line = 0
            if not E_Chest and not E_Panties and not E_Over and not E_Legs and not E_Hose:  
                # if already naked (yes)
                ch_e "Apparently so. . ."  
            elif E_SeenChest and E_SeenPussy and ApprovalCheck("Emma", 1200, TabM=(5-Public)):
                #if you've seen it all and she likes you well enough (yes)
                ch_e "I'll take that as an invitation. . ."  
                $ Line = 1
            elif ApprovalCheck("Emma", 2000, TabM=(5-Public)):
                #if you haven't seen everything but she really likes you (yes)
                ch_e "I suppose you've earned it. . ."    
                $ Line = 1
            elif E_SeenChest and E_SeenPussy and ApprovalCheck("Emma", 1200, TabM=0):
                # if you've seen it but it's in public (no)
                ch_e "As you're well aware, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Emma", 2000, TabM=0):
                #if you haven't seen everything but she really likes you and it's public (no) 
                ch_e "I assure you it is, but this isn't the appropriate venue. . ."  
            elif ApprovalCheck("Emma", 1000, TabM=0):     
                #if you haven't seen everything and she kinda likes you but it's public (no)
                call EmmaFace("surprised", 1) from _call_EmmaFace_786
                ch_e "I assure you that it is, but that's not the way to ask."
                $ E_Blush = 0
            else:
                # if she refuses. (no) 
                call EmmaFace("angry", 1) from _call_EmmaFace_787
                ch_e "Not the worst line I've heard."
                ch_e ". . . but close."
                
            if Line:                                                            #If she got nude. . .                            
                call EmmaOutfit("nude") from _call_EmmaOutfit_45
                "She strips down."
                call Emma_First_Topless from _call_Emma_First_Topless_12
                call Emma_First_Bottomless(1) from _call_Emma_First_Bottomless_15
                call EmmaFace("sexy") from _call_EmmaFace_788
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in E_Traits:
                            call EmmaFace("sexy",2,Eyes="down") from _call_EmmaFace_789
                            ch_e "Mmmmm. . ." 
                            $ E_Outfit = "nude"
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 50, 10) 
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 70, 5) 
                            $ E_Shame = E_OutfitShame[0]
                            call EmmaFace("sexy",1) from _call_EmmaFace_790
                        elif ApprovalCheck("Emma", 800, "I") and ApprovalCheck("Emma", 2800, TabM=0): 
                            ch_e "Oooh, that would cause quite a stir. . ." 
                            $ E_Outfit = "nude"
                            $ E_Shame = E_OutfitShame[0]
                        elif ApprovalCheck("Emma", 400, "I") and ApprovalCheck("Emma", 1200, TabM=0): 
                            call EmmaFace("bemused", 1,Eyes="side") from _call_EmmaFace_791
                            ch_e "You shouldn't suggest such things. . ."
                        else:
                            call EmmaFace("sexy", 1,Eyes="surprised") from _call_EmmaFace_792
                            ch_e "Impossible." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in E_Traits:
                            ch_e "Too much for you to handle?"                         
                        elif ApprovalCheck("Emma", 800, "I") and ApprovalCheck("Emma", 2800, TabM=0):       
                            call EmmaFace("bemused", 1) from _call_EmmaFace_793             
                            ch_e "Because obviously I couldn't go around like this. . ."
                        else:
                            call EmmaFace("confused", 1) from _call_EmmaFace_794
                            ch_e "So long as it's just the two of us, I don't mind this."   
            $ Line = 0
                
#        "How about throwing on your sleepwear?":
#            #fix add conditions
#            call EmmaOutfit("sleep")
            
        "Let's talk about what you wear outside.":
            call Emma_Clothes_Schedule from _call_Emma_Clothes_Schedule
            
        "Never mind":    
            jump Emma_Clothes     
            
    jump Emma_Clothes
    #End of Emma Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no Overshirt?" if E_Over:
            call EmmaFace("bemused", 1) from _call_EmmaFace_795
            if ApprovalCheck("Emma", 800, TabM=(3-Public)) and (E_Chest or E_SeenChest):
                ch_e "Certainly."
            elif ApprovalCheck("Emma", 1200, TabM=0):
                call Emma_NoBra from _call_Emma_NoBra
                if not _return:
                    jump Emma_Clothes                    
            $ Line = E_Over
            $ E_Over = 0   
            call Emma_Tits_Up from _call_Emma_Tits_Up_16
            "She shrugs off her [Line]."
            if not E_Chest:
                call Emma_First_Topless from _call_Emma_First_Topless_13
            
        "Try on that white jacket you have." if E_Over != "jacket":
            call EmmaFace("bemused") from _call_EmmaFace_796
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1) from _call_EmmaFace_797
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Clothes    
            $ E_Over = "jacket"

        "Try on that black jacket you have." if E_Over != "black jacket":
            call EmmaFace("bemused") from _call_EmmaFace_798
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1) from _call_EmmaFace_799
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Clothes    
            $ E_Over = "black jacket"

        "Try on that white cape you have." if E_Over != "cape":
            call EmmaFace("bemused") from _call_EmmaFace_800
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1) from _call_EmmaFace_801
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Clothes    
            $ E_Over = "cape"   

        "Try on that black cape you have." if E_Over != "black cape":
            call EmmaFace("bemused") from _call_EmmaFace_802
            if E_Chest or E_SeenChest or ApprovalCheck("Emma", 500, TabM=(3-Public)):
                ch_e "Yeah, ok."          
            else:
                call EmmaFace("bemused", 1) from _call_EmmaFace_803
                ch_e "I'm not sure this is appropriate without something more substantial underneath."
                jump Emma_Clothes    
            $ E_Over = "black cape"   
                
#        "How about that red t-shirt you have?" if E_Over != "red shirt":
#            $ E_Over = "red shirt"  
#            ch_e "This one?"
            
        "Maybe just throw on a towel?" if E_Over != "towel":
            call EmmaFace("bemused", 1) from _call_EmmaFace_804
            $ Bonus = 5 if bg_current == "bg showerroom" else 0
            if E_Chest or (E_SeenChest and ApprovalCheck("Emma", 500, TabM=(3-Public-Bonus))):
                ch_e "Oh, you like this?"
            elif ApprovalCheck("Emma", 1000, TabM=(3-Public-Bonus)):
                call EmmaFace("perplexed", 1) from _call_EmmaFace_805
                ch_e "Fine."          
            else:
                ch_e "This wouldn't leave much to the imagination."
                jump Emma_Clothes  
            call Emma_NoBra from _call_Emma_NoBra_1
            if not _return:
                jump Emma_Clothes
            $ E_Over = "towel"       
            call Emma_Tits_Up from _call_Emma_Tits_Up_17

        "How about that nighty I got you?" if E_Over != "nighty" and "nighty" in E_Inventory:
                        if E_Legs:
                            ch_e "I can't really wear that with my [E_Legs] on."
                        elif ApprovalCheck("Emma", 1100, TabM=3):
                            ch_e "Sure. . ."
                            $ E_Over = "nighty"   
                            if "lace bra" in E_Inventory:
                                $ E_Chest = "lace bra"
                            else:
                                $ E_Chest = "bra"
                            if "lace panties" in E_Inventory:
                                $ E_Panties = "lace panties"
                            else:
                                $ E_Panties = "black panties"
                            menu:
                                extend ""
                                "Nice.":
                                    pass
                                "I meant {i}just{/i} the nighty.":
                                    if ApprovalCheck("Emma", 1400, TabM=3):
                                        "She shrugs off her bra and then pulls the nighty back up."
                                        $ E_Panties = 0
                                        $ E_Chest = 0
                                        ch_e "Hmmm, alright. . ."
                                    elif ApprovalCheck("Emma", 1200, TabM=3):
                                        $ E_Chest = 0
                                        ch_e "I'll keep my panties on, thanks."
                                    else:
                                        ch_e "Be happy with what you get."
                        else:
                            ch_e "That's a bit . . . revealing."

        "How about that nighty you have?" if E_Over != "nighty":
                        if E_Legs:
                            ch_e "I can't really wear that with my [E_Legs] on."
                            ch_p "Just take them off."
                            call EmmaFace("sexy", 1) from _call_EmmaFace_806
                            if E_SeenPanties and E_Panties and ApprovalCheck("Emma", 500, TabM=(6-Public)):
                                ch_e "Fine."
                            elif E_SeenPussy and ApprovalCheck("Emma", 900, TabM=(5-Public)):
                                ch_e "Fine."
                            elif ApprovalCheck("Emma", 1300, TabM=(2-Public)) and E_Panties:
                                ch_e "It's not like I haven't worn this look before. . ."
                            elif ApprovalCheck("Emma", 800) and not E_Panties:
                                call Emma_NoPantiesOn from _call_Emma_NoPantiesOn
                            else:
                                ch_e "I'm afraid not."
                                if not E_Panties:
                                    ch_e "You understand, it could get. . . drafty. . ."
                                jump Emma_Clothes_Over
                            $ E_Legs = 0    
                            "She peels her pants off."
                            if E_Panties:                
                                $ E_SeenPanties = 1
                            else:
                                call Emma_First_Bottomless from _call_Emma_First_Bottomless_16
                            $ E_Over = "nighty"   
                            if "lace bra" in E_Inventory:
                                $ E_Chest = "lace bra"
                            else:
                                $ E_Chest = "bra"
                            if "lace panties" in E_Inventory:
                                $ E_Panties = "lace panties"
                            else:
                                $ E_Panties = "black panties"
                            menu:
                                extend ""
                                "Nice.":
                                    pass
                                "I meant {i}just{/i} the nighty.":
                                    if ApprovalCheck("Emma", 1400, TabM=3):
                                        "She shrugs off her bra and then pulls the nighty back up."
                                        $ E_Panties = 0
                                        $ E_Chest = 0
                                        ch_e "Hmmm, alright. . ."
                                    elif ApprovalCheck("Emma", 1200, TabM=3):
                                        $ E_Chest = 0
                                        ch_e "I'll keep my panties on, thanks."
                                    else:
                                        ch_e "Be happy with what you get."
                        elif ApprovalCheck("Emma", 1100, TabM=3):
                            ch_e "Sure. . ."
                            $ E_Over = "nighty"   
                            if "lace bra" in E_Inventory:
                                $ E_Chest = "lace bra"
                            else:
                                $ E_Chest = "bra"
                            if "lace panties" in E_Inventory:
                                $ E_Panties = "lace panties"
                            else:
                                $ E_Panties = "black panties"
                            menu:
                                extend ""
                                "Nice.":
                                    pass
                                "I meant {i}just{/i} the nighty.":
                                    if ApprovalCheck("Emma", 1400, TabM=3):
                                        "She shrugs off her bra and then pulls the nighty back up."
                                        $ E_Panties = 0
                                        $ E_Chest = 0
                                        ch_e "Hmmm, alright. . ."
                                    elif ApprovalCheck("Emma", 1200, TabM=3):
                                        $ E_Chest = 0
                                        ch_e "I'll keep my panties on, thanks."
                                    else:
                                        ch_e "Be happy with what you get."
                        else:
                            ch_e "That's a bit . . . revealing."
                            
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Emma_NoBra: #fix test this
        menu:
            ch_e "I'm not wearing much of anything under this. . ."
            "Then you could slip something on under it. . .":   
                        if (E_SeenChest and ApprovalCheck("Emma", 1000, TabM=(4-Public))) or ApprovalCheck("Emma", 1200, TabM=(5-Public)):
                                ch_e "-not that I'm overly concerned about it. . ."
                        elif ApprovalCheck("Emma", 900, TabM=2) and "lace bra" in E_Inventory:
                                ch_e "I suppose I could."
                                $ E_Chest  = "lace bra"    
                                call Emma_Tits_Up from _call_Emma_Tits_Up_18
                                "She pulls out her lace bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Emma", 800, TabM=2):
                                ch_e "I suppose I could."
                                $ E_Chest = "NewX"
                                "She pulls out her X-men bra and slips it on under her [E_Over]."
                        elif ApprovalCheck("Emma", 700, TabM=(3-Public)):
                                ch_e "I suppose I could."
                                $ E_Chest = "corset"   
                                call Emma_Tits_Up from _call_Emma_Tits_Up_19
                                "She pulls out her corset and slips it on under her [E_Over]."
                        elif ApprovalCheck("Emma", 600, TabM=2):
                                ch_e "I suppose I could."
                                $ E_Chest = "white sports bra"
                                "She pulls out her sports bra and slips it on under her [E_Over]."
                        else:
                                ch_e "Yes, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Emma", 1100, "LI", TabM=(3-Public)) and E_Love > E_Inbt:               
                                ch_e "The things I do for you. . ."
                        elif ApprovalCheck("Emma", 700, "OI", TabM=(3-Public)) and E_Obed > E_Inbt:
                                ch_e "If that's what you insist. . ."
                        elif ApprovalCheck("Emma", 600, "I", TabM=(3-Public)):
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck("Emma", 1300, TabM=(3-Public)):
                                ch_e "Very well."
                        else: 
                                call EmmaFace("surprised") from _call_EmmaFace_807
                                $ E_Brows = "angry"
                                if Taboo:
                                    ch_e "I'm afraid I couldn't do that in public."
                                else:
                                    ch_e "I could, but I wouldn't."
                                return 0
                                
                    
            "Never mind.":
                        return 0
        return 1
        #End of Emma bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the pants." if PantsNum("Emma") > 5:
            call EmmaFace("sexy", 1) from _call_EmmaFace_808
            if E_SeenPanties and E_Panties and ApprovalCheck("Emma", 500, TabM=(6-Public)):
                ch_e "Fine."
            elif E_SeenPussy and ApprovalCheck("Emma", 900, TabM=(5-Public)):
                ch_e "Fine."
            elif ApprovalCheck("Emma", 1300, TabM=(2-Public)) and E_Panties:
                ch_e "It's not like I haven't worn this look before. . ."
            elif ApprovalCheck("Emma", 800) and not E_Panties:
                call Emma_NoPantiesOn from _call_Emma_NoPantiesOn_1
                if not _return:
                    jump Emma_Clothes
            else:
                ch_e "I'm afraid not."
                if not E_Panties:
                    ch_e "You understand, it could get. . . drafty. . ."
                jump Emma_Clothes
            $ E_Legs = 0    
            "She peels her pants off."
            if E_Panties:                
                $ E_SeenPanties = 1
            else:
                call Emma_First_Bottomless from _call_Emma_First_Bottomless_17
        
        "You look great in that white skirt." if E_Legs != "skirt":
            ch_e "I know."
            $ E_Legs = "skirt"

        "You look great in those white pants." if E_Legs != "pants":
            ch_e "I know."
            $ E_Legs = "pants"

        "You look great in those black pants." if E_Legs != "black pants":
            ch_e "I know."
            $ E_Legs = "black pants"

        "You look great in those white shorts." if E_Legs != "NewX":
            ch_e "I know."
            $ E_Legs = "NewX"
        
        "You look great in those black shorts." if E_Legs != "NewX black":
            ch_e "I know."
            $ E_Legs = "NewX black"

        "You look great in those white sports shorts." if E_Legs != "white sports shorts":
            ch_e "I know."
            $ E_Legs = "white sports shorts"

        "You look great in those red sports shorts." if E_Legs != "red sports shorts":
            ch_e "I know."
            $ E_Legs = "red sports shorts"
                
#        "You look great in those black jeans." if E_Legs != "black jeans":
#            ch_e "K, no problem."
#            $ E_Legs = "black jeans"
        
#        "You look great in yoga pants." if E_Legs != "yoga pants":
#            ch_e "Yeah, ok."
#            $ E_Legs = "yoga pants"
            
#        "What about wearing your yellow shorts?" if E_Legs != "shorts":
#            ch_e "K, no problem."
#            $ E_Legs = "shorts"    
                   
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Emma_NoPantiesOn: #fix test this
        call EmmaFace("sexy",Eyes="side") from _call_EmmaFace_809
        ch_e "You should be aware. . ."
        call EmmaFace("sly") from _call_EmmaFace_810
        menu:
            ch_e "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":   
                        if (E_SeenPussy and ApprovalCheck("Emma", 1100, TabM=(5-Public))) or ApprovalCheck("Emma", 1500, TabM=(5-Public)):
                                $ E_Blush = 1
                                ch_e "I didn't say that bothered me. . ."
                                $ E_Blush = 0                
                        elif ApprovalCheck("Emma", 800, TabM=(5-Public)) and "lace panties" in E_Inventory:
                                ch_e "I like how you think, turn around."
                                $ E_Panties  = "lace panties"    
                                "She pulls out her lace panties, and with your back turned she removes her pants, and slips her panties on."
                        elif ApprovalCheck("Emma", 700, TabM=(5-Public)):
                                ch_e "Yeah, I guess."
                                $ E_Panties = "white panties"
                                "She pulls out her white panties, and with your back turned she removes her pants, and slips her panties on."                   
                        elif Taboo and ApprovalCheck("Emma", 800, TabM=0):
                                ch_e "I like how you think, but not in public like this."
                                return 0
                        else:
                                ch_e "I could, but I'd rather not."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Emma", 1100, "LI", TabM=(5-Public)) and E_Love > E_Inbt:               
                                ch_e "I suppose I could. . ."
                        elif ApprovalCheck("Emma", 700, "OI", TabM=(5-Public)) and E_Obed > E_Inbt:
                                ch_e "If you'd like. . ."
                        elif ApprovalCheck("Emma", 600, "I", TabM=(5-Public)):
                                ch_e "I certainly could. . ."
                        elif ApprovalCheck("Emma", 1300, TabM=(5-Public)):
                                ch_e "Very well."
                        else: 
                                call EmmaFace("surprised") from _call_EmmaFace_811
                                $ E_Brows = "angry"
                                if Taboo:
                                    ch_e "I'm afraid not out here, [E_Petname]!"
                                else:
                                    ch_e "You wish, [E_Petname]!"
                                return 0
                                
            "Never mind.":
                ch_e "Ok. . ."
                return 0
        return 1
        #End of Emma Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Emma_Clothes_Under:                                                                                                 # Tops    
        "How about you lose the [E_Chest]?" if E_Chest:
            call EmmaFace("bemused", 1) from _call_EmmaFace_812
            if E_SeenChest and ApprovalCheck("Emma", 900, TabM=(4-Public)):
                ch_e "Of course."    
            elif ApprovalCheck("Emma", 1100, TabM=2):
                if Taboo:
                    ch_e "I'd rather not out here. . ."
                else:
                    ch_e "I suppose for you. . ."
            elif E_Over == "jacket" or E_Over == "black jacket" and ApprovalCheck("Emma", 700, TabM=(3-Public)):
                ch_e "This is a bit daring without anything under it. . ."  
            elif not E_Over:
                ch_e "I don't think that would be appropriate."
                jump Emma_Clothes 
            else:
                ch_e "I'm afraid not, [E_Petname]."
                jump Emma_Clothes 
            $ Line = E_Chest
            $ E_Chest = 0
            call Emma_Tits_Up from _call_Emma_Tits_Up_20 #flag
            if E_Over:
                "She reaches under her [E_Over] grabs her [Line], and pulls it out, dropping it to the ground."
            else:
                "She lets her [Line] fall to the ground."
            call Emma_First_Topless from _call_Emma_First_Topless_14
          
        "I like that corset you have." if E_Chest != "corset":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "corset"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that black corset you have." if E_Chest != "black corset":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "black corset"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."    

        "I like that NewX corset you have." if E_Chest != "NewX":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "NewX"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."    

        "I like that NewX black corset you have." if E_Chest != "NewX black":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "NewX black"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ." 

        "I like that white sports bra you have." if E_Chest != "white sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "white sports bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that red sports bra you have." if E_Chest != "red sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "red sports bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that sports bra you have." if E_Chest != "sports bra":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "sports bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ." 

        "I like that lace bra you have." if E_Chest != "lace bra":
            if E_SeenChest or ApprovalCheck("Emma", 1200, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "lace bra"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

        "I like that bikini top you have." if E_Chest != "bikini":
            if E_SeenChest or ApprovalCheck("Emma", 1000, TabM=(3-Public)):
                ch_e "So do I."   
                $ E_Chest = "bikini"  
                $ E_TitsUp = 1
            else:                
                ch_e "I don't think that would be appropriate. . ."  

                                                                                                                            #Panties        
        "You could lose those panties. . ." if E_Panties:
            call EmmaFace("bemused", 1) from _call_EmmaFace_813  
            if (ApprovalCheck("Emma", 900) or E_SeenPussy) and not Taboo:
                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                
                if ApprovalCheck("Emma", 850, "L"):               
                        ch_e "You like the view?"
                elif ApprovalCheck("Emma", 500, "O"):
                        ch_e "If you'd like."
                elif ApprovalCheck("Emma", 350, "I"):
                        ch_e "I do enjoy going without them. . ."
                else:
                        ch_e "Very well."         
            else:                       
                #low approval or not wearing pants or in public 
                if ApprovalCheck("Emma", 1100, "LI", TabM=(4-Public)) and E_Love > E_Inbt:               
                        ch_e "I don't exactly mind you seeing. . ."
                elif ApprovalCheck("Emma", 700, "OI", TabM=(4-Public)) and E_Obed > E_Inbt:
                        ch_e "I suppose I could. . ."
                elif ApprovalCheck("Emma", 600, "I", TabM=(4-Public)):
                        ch_e "Why not."
                elif ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                        ch_e "Fine."
                else: 
                        call EmmaFace("surprised") from _call_EmmaFace_814
                        $ E_Brows = "angry"
                        if Taboo:
                            ch_e "I don't think I could out here, [E_Petname]!"
                        else:
                            ch_e "I could, but I won't, [E_Petname]!"
                        jump Emma_Clothes
                        
                        
            $ Line = E_Panties
            $ E_Panties = 0  
            if E_Legs:
                if Taboo or ApprovalCheck("Emma", 1100) or E_SeenPussy:
                    "She pulls off her [E_Legs] then pulls her [Line] off, droping them to the ground, before putting them back on." 
                    call Emma_First_Bottomless from _call_Emma_First_Bottomless_18
                else:
                    "She asks you to turn around. After a few seconds, you turn back to her as she drops the [Line] to the ground."               
            else:
                "She pulls off her [Line] and lets them drop to the ground."
                call Emma_First_Bottomless from _call_Emma_First_Bottomless_19
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 50, 2) 

        "Why don't you wear the sports panties instead?" if E_Panties and E_Panties != "sports panties":
            if ApprovalCheck("Emma", 800, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "sports panties"  
            else:                
                    ch_e "I really don't see how that's any of your concern." 
                
        "Why don't you wear the white panties instead?" if E_Panties and E_Panties != "white panties":
            if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "white panties"  
            else:                
                    ch_e "I really don't see how that's any of your concern."

        "Why don't you wear the black panties instead?" if E_Panties and E_Panties != "black panties":
            if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "black panties"  
            else:                
                    ch_e "I really don't see how that's any of your concern."

        "Why don't you wear that bikini panties?" if E_Panties and E_Panties != "bikini":
            if ApprovalCheck("Emma", 1100, TabM=(4-Public)):
                    ch_e "Ok."
                    $ E_Panties = "bikini"  
            else:                
                    ch_e "I really don't see how that's any of your concern."
                
        "Why don't you wear the lace panties instead?" if "lace panties" in E_Inventory and E_Panties and E_Panties != "lace panties":
            if ApprovalCheck("Emma", 1300, TabM=(4-Public)):
                    ch_e "Fine."
                    $ E_Panties = "lace panties"
            else:
                    ch_e "I really don't see how that's any of your concern."
                
        "You know, you could wear some panties with that. . ." if not E_Panties:
            call EmmaFace("bemused", 1) from _call_EmmaFace_815
            if (E_Love+E_Obed) <= (2* E_Inbt):
                $ E_Mouth = "smile"
                ch_e "I could, but won't."
                $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 70, 2)
                menu:
                    "Wear them":
                        pass
                    "Ok":
                        jump Emma_Clothes
            menu:
                ch_e "If you insist. . ."
                "How about the sports ones?":
                    ch_e "Fine."
                    $ E_Panties = "sports panties"
                "How about the white ones?":
                    ch_e "Fine."
                    $ E_Panties = "white panties"
                "How about the black ones?":
                    ch_e "Fine."
                    $ E_Panties = "black panties"
                "How about the lace ones?" if "lace panties" in E_Inventory:
                    ch_e "Fine."                
                    $ E_Panties  = "lace panties"
        "Socks and Stockings": 
            
            menu Emma_Clothes_Under_Hoses:  

                "You could lose those stockings. . ." if E_Hose:
                    ch_k "Fine."
                    $ E_Hose = 0
                    jump Emma_Clothes_Under_Hoses  

                "Why don't you wear those white thigh highs?" if E_Hose != "white thigh high":
                    ch_k "Fine."
                    $ E_Hose = "white thigh high"  
                    jump Emma_Clothes_Under_Hoses

                "Why don't you wear those black thigh highs?" if E_Hose != "black thigh high":
                    ch_k "Fine."
                    $ E_Hose = "black thigh high"  
                    jump Emma_Clothes_Under_Hoses

                "Why don't you wear those boots?" if E_Hose != "boots":
                    ch_k "Fine."
                    $ E_Hose = "boots"  
                    jump Emma_Clothes_Under_Hoses

                "Go back":  
                    jump Emma_Clothes_Under
        "Never mind":
            pass
    jump Emma_Clothes
    #End of Emma Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Emma_Clothes_Misc:                     
        #Misc
        "Maybe lose the gloves." if E_Arms:
            $ E_Arms = 0
            ch_e "Ok."
        "Put your white gloves on." if E_Arms != "white gloves":
            $ E_Arms = "white gloves"
            ch_e "Ok." 
        "Put your black gloves on." if E_Arms != "black gloves":
            $ E_Arms = "black gloves"
            ch_e "Ok."     

        "Hair options":

            menu Emma_Clothes_Misc_Hair:

                "You look good with your hair flowing." if E_Hair != "wave":
                    if ApprovalCheck("Emma", 600):
                        ch_e "Like this?"
                        $ E_Hair = "wave"
                    else:
                        ch_e "Yes, I do."
                    jump Emma_Clothes_Misc_Hair
                        
                "Maybe keep your hair straight." if E_Hair != "wet":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_Hair = "wet"
                    else:
                        ch_e "I tend to prefer it a bit more loose."
                    jump Emma_Clothes_Misc_Hair
        
                "Maybe dye your hair black." if E_HairColor != "black":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_HairColor = "black"
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Clothes_Misc_Hair

                "Maybe dye your hair red." if E_HairColor != "red":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_HairColor = "red"
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Clothes_Misc_Hair


                "Maybe dye your hair white." if E_HairColor != "white":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_HairColor = "white"
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Clothes_Misc_Hair

        
                "Maybe dye your hair back to blonde." if E_HairColor and E_HairColor != "blonde":
                    if ApprovalCheck("Emma", 600):
                        ch_e "You think?"
                        $ E_HairColor = "blonde"
                    else:
                        ch_e "I tend to prefer it the way it is."
                    jump Emma_Clothes_Misc_Hair

                "Nevermind":
                    jump Emma_Clothes_Misc

        "Neck options":
            menu Emma_Clothes_Misc_Neck:
                "Why don't you try on that white choker." if E_Neck != "choker":
                    ch_e "Ok. . ."         
                    $ E_Neck = "choker"
                    jump Emma_Clothes_Misc_Neck
        
                "Why don't you try on that black choker." if E_Neck != "black choker":
                    ch_e "Ok. . ."         
                    $ E_Neck = "black choker"
                    jump Emma_Clothes_Misc_Neck
        
                "Why don't you try on that NewX neck piece." if E_Neck != "NewX":
                    ch_e "Ok. . ."         
                    $ E_Neck = "NewX"
                    jump Emma_Clothes_Misc_Neck
                "Why don't you try on that black NewX neck piece." if E_Neck != "NewX black":
                    ch_e "Ok. . ."         
                    $ E_Neck = "NewX black"
                    jump Emma_Clothes_Misc_Neck
        #        "Why don't you try on that star necklace." if E_Neck != "star necklace":
        #            ch_e "Ok. . ."         
        #            $ E_Neck = "star necklace"
                "Maybe go without a collar." if E_Neck:
                    ch_e "Ok. . ."         
                    $ E_Neck = 0
                    jump Emma_Clothes_Misc_Neck
                "Nevermind":
                    jump Emma_Clothes_Misc
                        
        "You know, I like some nice hair down there. Maybe grow it out." if not E_Pubes and "pubes" in E_Todo:
            call EmmaFace("bemused", 1) from _call_EmmaFace_816
            ch_e "Rome wasn't built in a day. . ."
        "I like some hair down there." if not E_Pubes and "pubes" not in E_Todo:
            call EmmaFace("bemused", 1) from _call_EmmaFace_817
            $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
            if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
                ch_e "If you like that sort of thing. . ."
            elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "I could go a bit more. . . wild."
            elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
                ch_e "If you insist. . ."
            else: 
                call EmmaFace("surprised") from _call_EmmaFace_818
                $ E_Brows = "angry"
                ch_e "I don't see how that's your concern, [E_Petname]."
                jump Emma_Clothes
            $ E_Todo.append("pubes")
            $ E_PubeC = 6
        
        "I like it waxed clean down there." if E_Pubes == 1:
            call EmmaFace("bemused", 1) from _call_EmmaFace_819            
            if "shave" in E_Todo:
                ch_e "Yes, yes, it's on my schedule."
            else:
                $ Approval = ApprovalCheck("Emma", 1150, TabM=0)
                
                if ApprovalCheck("Emma", 850, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed):               
                    ch_e "I know you love it."
                elif ApprovalCheck("Emma", 500, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                    ch_e "I like it kept tidy."
                elif ApprovalCheck("Emma", 400, "O", TabM=0) or Approval:
                    ch_e "If you insist."
                else: 
                    call EmmaFace("surprised") from _call_EmmaFace_820
                    $ E_Brows = "angry"
                    ch_e "I don't see how that's your concern, [E_Petname]."
                    jump Emma_Clothes
                $ E_Todo.append("shave")        
        "Piercings. [[See what she looks like without them first] (locked)" if not E_SeenPussy and not E_SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if E_Pierce != "ring" and (E_SeenPussy or E_SeenChest):
            call EmmaFace("bemused", 1) from _call_EmmaFace_821
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2* E_Obed):   
                    ch_e "A little handhold, I assume?"
            elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                    ch_e "I do like a nice ring. . ."
            elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
                    ch_e "I didn't know you were into that sort of thing."
            else: 
                    call EmmaFace("surprised") from _call_EmmaFace_822
                    $ E_Brows = "angry"
                    ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
                    jump Emma_Clothes            
            $ E_Pierce = "ring"
            #$ E_Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if E_Pierce != "barbell" and (E_SeenPussy or E_SeenChest):
            call EmmaFace("bemused", 1) from _call_EmmaFace_823
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 900, "L", TabM=0) or (Approval and E_Love > 2 * E_Obed): 
                ch_e "A little handhold, I assume?"
            elif ApprovalCheck("Emma", 600, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "They might look nice on these. . ."
            elif ApprovalCheck("Emma", 500, "O", TabM=0) or Approval:
                ch_e "I didn't know you were into that sort of thing."
            else: 
                call EmmaFace("surprised") from _call_EmmaFace_824
                $ E_Brows = "angry"
                ch_e "Well, I'm just not ready for that sort of thing, [E_Petname]."
                jump Emma_Clothes                
            #$ E_Todo.append("barbell")
            $ E_Pierce = "barbell"
            
        "You know, you'd look better without those piercings." if E_Pierce:
            call EmmaFace("bemused", 1) from _call_EmmaFace_825
            $ Approval = ApprovalCheck("Emma", 1350, TabM=0)
            if ApprovalCheck("Emma", 950, "L", TabM=0) or (Approval and E_Love > E_Obed):   
                ch_e "If they aren't working for you. . ."
            elif ApprovalCheck("Emma", 700, "I", TabM=0) or (Approval and E_Inbt > E_Obed):
                ch_e "They were being a nuisance."
            elif ApprovalCheck("Emma", 600, "O", TabM=0) or Approval:
                ch_e "I'll remove them then."
            else: 
                call EmmaFace("surprised") from _call_EmmaFace_826
                $ E_Brows = "angry"
                ch_e "Well {i}I{/i} enjoy them."
                jump Emma_Clothes            
            $ E_Pierce = 0 


            
        "Never mind":
            pass         
    jump Emma_Clothes
    #End of Emma Misc Wardrobe
    
return
#End Emma Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Emma_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Emma", 1500, "LO"):
                ch_e "I'm open to suggestions."
                $ Cnt = 3
        elif ApprovalCheck("Emma", 1000, "LO"):
                ch_e "Perhaps when I'm off the clock. . ."
                $ Cnt = 1
        else:
                ch_e "I'd prefer to handle my own wardrobe."
                return
            
        
        menu:
                extend ""
                "On Monday you should wear. . ." if Cnt > 1:
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB
                    $ E_Schedule[0] = _return
                "On Monday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Tuesday you should wear. . ." if Cnt > 2:
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_1
                    $ E_Schedule[1] = _return        
                "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Wednesday you should wear. . ." if Cnt > 1:
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_2
                    $ E_Schedule[2] = _return
                "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                    pass   
                    
                "On Thursday you should wear. . ." if Cnt > 2:
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_3
                    $ E_Schedule[3] = _return
                "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                    pass
                    
                "On Friday you should wear. . ." if Cnt > 1:
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_4
                    $ E_Schedule[4] = _return
                "On Friday you should wear. . . (locked)" if Cnt <= 1:
                    pass
                    
                "On Saturday you should wear. . .":
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_5
                    $ E_Schedule[5] = _return
                    
                "On Sunday you should wear. . .":
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_6
                    $ E_Schedule[6] = _return
                    
                "In our rooms you should wear. . .":
                    call Emma_Clothes_ScheduleB(99) from _call_Emma_Clothes_ScheduleB_7
                    $ E_Schedule[9] = _return   
                    
                "On dates you should wear. . .":
                    call Emma_Clothes_ScheduleB from _call_Emma_Clothes_ScheduleB_8
                    $ E_Schedule[7] = _return    
                    
                "Never mind":
                    return        
        jump Emma_Clothes_Schedule
    
    
    
label Emma_Clothes_ScheduleB(Count = 0):
#This is called by Emma_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That teacher outfit.":
                    $ Count = 1
                "Your superhero outfit.":
                    $ Count = 2
                "That outfit we put together [[custom]" if E_Custom[0] or E_Custom2[0] or E_Custom3[0] or E_Custom4[0] or E_Custom5[0] or E_Custom6[0] or E_Custom7[0]:
                            menu:
                                "Like, which?"
                                "The first one. (locked)" if not E_Custom[0]:
                                    pass
                                "The first one." if E_Custom[0]:
                                    if E_Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The second one. (locked)" if not E_Custom2[0]:
                                    pass
                                "The second one." if E_Custom2[0]:
                                    if E_Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_e "I said I'm not wearing that one in public."
                                        
                                "The third one. (locked)" if not E_Custom3[0]:
                                    pass
                                "The third one." if E_Custom3[0]:
                                    if E_Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_e "I said I'm not wearing that one in public."

                                "The fourth one. (locked)" if not E_Custom4[0]:
                                    pass
                                "The fourth one." if E_Custom4[0]:
                                    if E_Custom4[0] == 2 or Count == 99:
                                        $ Count = 11
                                    else:
                                        ch_e "I said I'm not wearing that one out."

                                "The fifth one. (locked)" if not E_Custom5[0]:
                                    pass
                                "The fifth one." if E_Custom5[0]:
                                    if E_Custom5[0] == 2 or Count == 99:
                                        $ Count = 12
                                    else:
                                        ch_e "I said I'm not wearing that one out."

                                "The sixth one. (locked)" if not E_Custom6[0]:
                                    pass
                                "The sixth one." if E_Custom6[0]:
                                    if E_Custom6[0] == 2 or Count == 99:
                                        $ Count = 13
                                    else:
                                        ch_e "I said I'm not wearing that one out."

                                "The seventh one. (locked)" if not E_Custom7[0]:
                                    pass
                                "The seventh one." if E_Custom7[0]:
                                    if E_Custom7[0] == 2 or Count == 99:
                                        $ Count = 14
                                    else:
                                        ch_e "I said I'm not wearing that one out."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_e "Very well."
            else:
                        ch_e "I'll wear something else instead."
            return Count    
#End Emma Clothes Scheduling Check

#label Emma_Clothes_Sleepwear: #fix fill this out
#            $ E_OutfitShame[4] = 50
            
#            if E_Chest == "tank":                                               #If she's wearing a bra of some kind
#                $ Count = 20
#            elif E_Chest == "buttoned tank":
#                $ Count = 15
#            elif E_Chest == "sports bra":
#                $ Count = 15
#            elif E_Chest == "bra":
#                $ Count = 10    
#            elif E_Chest == "lace bra":
#                $ Count = 5
#            else:     #E_Chest == 0:
#                if E_Pierce:
#                    $ Count = -5
#                else:
#                    $ Count = 0
            
#            if E_Over == "pink top":                                            #If she's wearing an overshirt 
#                $ Count += 15
#            elif E_Over == "hoodie":      
#                $ Count += 15
#            elif E_Over == "mesh top":      
#                $ Count += 5
#            elif E_Over == "towel":      
#                $ Count += 10
#            #else: nothing    
            
#            $ Count = 20 if Count >= 20 else Count
               
#            $ E_OutfitShame[4] -= Count                  #Set Outfit shame for the upper half    
#            $ Count = 0         
            
#            if not E_Legs or not E_Panties:                                     #If she's missing something on her legs        
#                        if E_Legs == "pants":                   #If wearing pants commando
#                            $ Count = 25
#                        elif E_Legs:                            #If wearing a skirt commando
#                            $ Count = 20
#                        elif E_Panties == "shorts":             #If wearing shorts
#                            $ Count = 25  
#                        elif E_Panties == "green panties":      #If wearing only green panties
#                            $ Count = 10
#                        elif E_Panties == "lace panties":       #If wearing only lace panties
#                            $ Count = 5
#                        elif E_Panties:                         #If wearing only any other panties
#                            $ Count = 7
#                        #else: nothing
                
#                        if HoseNum("Emma") >= 10:
#                            $ Count = 25 if Count < 25 else Count
#                        elif HoseNum("Emma") >= 5:            
#                            $ Count += 5        
                                
#                        if E_Over == "towel" and Count:         #If wearing a Towel and anything else
#                            $ Count = 25
#                        elif E_Over == "towel":                 #If just wearing a Towel
#                            $ Count = 15        
#            else:                                       #If wearing both legs and panties
#                        $ Count = 30        
                  
                
#            $ E_OutfitShame[4] -= Count                  #Set Outfit shame for the lower half
            
#            $ E_Sleepwear[0] = E_Arms
#            $ E_Sleepwear[1] = E_Legs
#            $ E_Sleepwear[2] = E_Over
#            $ E_Sleepwear[3] = E_Neck
#            $ E_Sleepwear[4] = E_Chest
#            $ E_Sleepwear[5] = E_Panties 
#            $ E_Sleepwear[6] = E_Hose 
#            ch_e "Ok, this could work for sleepwear."
                
#            return
##End Emma Sleepwear Set.



label Emma_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call EmmaFace("sexy", 1) from _call_EmmaFace_827
            if "exhibitionist" in E_Traits:  
                        ch_e "Hmm, I'm getting excited. . ."  
                        if Custom == 5 and E_Custom2[0] == 2:
                            $ E_Outfit = "custom2"                    
                            $ E_Shame = E_OutfitShame[5]
                        elif Custom == 6 and E_Custom3[0] == 2:
                            $ E_Outfit = "custom3"                    
                            $ E_Shame = E_OutfitShame[6]
                        elif Custom == 11 and E_Custom4[0] == 2:
                            $ E_Outfit = "custom4"                    
                            $ E_Shame = E_OutfitShame[11]
                        elif Custom == 12 and E_Custom5[0] == 2:
                            $ E_Outfit = "custom5"                    
                            $ E_Shame = E_OutfitShame[12]
                        elif Custom == 13 and E_Custom6[0] == 2:
                            $ E_Outfit = "custom6"                    
                            $ E_Shame = E_OutfitShame[13]
                        elif Custom == 14 and E_Custom7[0] == 2:
                            $ E_Outfit = "custom7"                    
                            $ E_Shame = E_OutfitShame[14]
                        else: #if custom 1:
                            $ E_Outfit = "custom1"                    
                            $ E_Shame = E_OutfitShame[3]            
                        return  
            
            if Custom == 5 and E_Custom2[0] == 2:
                        $ E_Outfit = "custom2"   
            elif Custom == 6 and E_Custom3[0] == 2:
                        $ E_Outfit = "custom3"    
            elif Custom == 11 and E_Custom4[0] == 2:
                        $ E_Outfit = "custom4"    
            elif Custom == 12 and E_Custom5[0] == 2:
                        $ E_Outfit = "custom5"    
            elif Custom == 13 and E_Custom6[0] == 2:
                        $ E_Outfit = "custom6"    
            elif Custom == 14 and E_Custom7[0] == 2:
                        $ E_Outfit = "custom7"   
            elif E_Custom[0] == 2: #if custom 1:
                        $ E_Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ E_Shame = E_OutfitShame[Custom]          
                        if E_OutfitShame[Custom] >= 50:
                            ch_e "This is. . . kinda slutty. . ."
                        elif E_OutfitShame[Custom] >= 25:
                            ch_e "I'm not really comfortable with this one. . ."
                        elif E_OutfitShame[Custom] >= 15:
                            call EmmaFace("bemused", 1) from _call_EmmaFace_828
                            ch_e "I'll give it a shot. . ."
                        else:
                            ch_e "Yeah, I like that one too."
            else:
                        #She's decided not to wear this out
                        if E_OutfitShame[Custom] >= 50:
                            call EmmaFace("angry", 1) from _call_EmmaFace_829
                            ch_e "You have GOT to be kidding me here."
                        elif E_OutfitShame[Custom] >= 25:
                            call EmmaFace("angry", 1) from _call_EmmaFace_830
                            ch_e "This is just between us."
                        else:
                            call EmmaFace("surprised", 1) from _call_EmmaFace_831
                            ch_e "I can't wear this out!"  
            return
# End Emma Custom Out
                                
                                
label Emma_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):                                                                             #sets custom outfit    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7, if private = 9
            
            if not Check and not Taboo:
                #if this is not a custom check and you're in a safe space,
                return

                        
            #If she's wearing a bra of some kind
            if E_Chest == "black corset":  
                $ Count = 15
            elif E_Chest == "corset":  
                $ Count = 15
            elif E_Chest == "white sports bra":  
                $ Count = 15
            elif E_Chest == "red sports bra":  
                $ Count = 15
            elif E_Chest == "sports bra":  
                $ Count = 15
            elif E_Chest == "NewX":  
                $ Count = 10
            elif E_Chest == "bikini":  
                $ Count = 15
            elif E_Chest == "naked pool":  
                $ Count = 15
            elif E_Chest == "NewX black":  
                $ Count = 10
#            elif E_Chest == "sports bra":
#                $ Count = 15
#            elif E_Chest == "bra":
#                $ Count = 10   
            elif E_Chest == "lace bra":
                $ Count = 5
            else:     #E_Chest == 0
                if E_Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if E_Over == "black jacket":                                             
                $ Count += 15
            elif E_Over == "jacket":                                             
                $ Count += 15
            elif E_Over == "black cape":
                $ Count += 20
            elif E_Over == "cape":
                $ Count += 20
            elif E_Over == "towel":      
                $ Count += 5
            #else: nothing    
            
            call EmmaFace("sexy", 0) from _call_EmmaFace_832
            if Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        $ Count = 20
                        if Check:
                            ch_e "This is a fashionable top."
            elif not Check:
                        pass
            elif Count >= 10: 
                        if ApprovalCheck("Emma", 1200, TabM=0) or ApprovalCheck("Emma", 500, "I", TabM=0):  
                            ch_e "A bit daring. . ."        
                        else:
                            ch_e "I'm not sure about this top."
            elif Count >= 5:
                        if ApprovalCheck("Emma", 2300, TabM=0) or ApprovalCheck("Emma", 800, "I", TabM=0):  
                            ch_e "I typically cover a {i}bit{/i} more than this."        
                        else:        
                            call EmmaFace("startled", 1) from _call_EmmaFace_833
                            ch_e "This is a bit more cleavage than even I'm comforable with."
            elif (ApprovalCheck("Emma", 2700, TabM=0) or ApprovalCheck("Emma", 950, "I", TabM=0)):  
                        ch_e "Aren't my assets a bit. . . exposed here?"        
            else:
                        call EmmaFace("bemused", 1) from _call_EmmaFace_834
                        ch_e "This is considerably more cleavage than even I'm comforable with."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half   
            $ Count = 0         
            
            if E_Legs or E_Panties:          
                if PantsNum("Emma") > 5:              
                    #If wearing pants
                    if E_Panties:
                            $ Count = 30
                    else:
                            # if commando
                            $ Count = 25  
                elif E_Legs: #if skirt
                    if E_Panties:
                            $ Count = 20
                    else:
                            # if commando
                            $ Count = 15                
                elif E_Panties == "white panties":      #If wearing only white panties
                    $ Count = 10
                elif E_Panties == "black panties":      #If wearing only black panties
                    $ Count = 10
                elif E_Panties == "sports panties":      #If wearing only white panties
                    $ Count = 15
                elif E_Panties == "bikini":      #If wearing only bikini
                    $ Count = 15
                elif E_Panties == "naked pool":      #If wearing only bikini
                    $ Count = 15
                elif E_Panties == "lace panties":       #If wearing only lace panties
                    $ Count = 5              
                #else: 0
                
                if HoseNum("Emma") >= 10:
                    # if she's wearing full coverage hose, it's at least 25
                    $ Count = 25 if Count < 25 else Count
                    
                if E_Over == "towel":         
                    #If wearing a Towel it's at least 10
                    $ Count = 10 if Count < 10 else Count
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        #It's for private only
                        pass
            elif Count >= 20:
                        if PantsNum("Emma") > 5:
                            ch_e "and these pants always did suit me."
                        elif HoseNum("Emma") >= 10:
                            ch_e "I guess these [E_Hose] will work fine."
                        else:
                            ch_e "I'm unsure about wearing a towel out, [E_Petname]. . ."
                        if not E_Panties:
                            if ApprovalCheck("Emma", 500, "I", TabM=0):
                                ch_e "I do enjoy going without panties."
                            else:
                                ch_e "I don't know about going without panties in this situation."
                    
            elif Count >= 10:
                if ApprovalCheck("Emma", 2000, TabM=0) or ApprovalCheck("Emma", 700, "I", TabM=0):
                        ch_e "I hope you don't expect me to wear this out. . ."        
                else:
                        call EmmaFace("angry", 1) from _call_EmmaFace_835
                        ch_e "I couldn't exactly wear this outside. . ."                
            elif (ApprovalCheck("Emma", 2500, TabM=0) or ApprovalCheck("Emma", 800, "I", TabM=0)):  
                        ch_e "This really tests my limits."        
            else:
                        ch_e "I'll need to put something else on to leave the room though."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                                         
                    call EmmaFace("sexy", 0) from _call_EmmaFace_836
                    if Taboo >= 40: #E_Loc != "bg player" and E_Loc != "bg emma": 
                            call EmmaFace("confused",1) from _call_EmmaFace_837
                            $ E_Mouth = "smile"
                            "She glances around."
                            ch_e "Is that a trick question?" 
                    elif "exhibitionist" in E_Traits and Tempshame <= 20:        
                            ch_e "The thought of it gets me moist. . ."
                            $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 80, 10)
                    elif Tempshame <= 5:
                            call EmmaFace("smile") from _call_EmmaFace_838
                            ch_e "Yes, it's a fine choice."
                    elif Tempshame <= 15 and (ApprovalCheck("Emma", 1700, TabM=0, C = 0) or ApprovalCheck("Emma", 400, "I", TabM=0, C = 0)):        
                            ch_e "Rather daring, how could I resist?"
                    elif Custom == 9:
                            #if it's sleepwear      
                            call EmmaFace("bemused", 1) from _call_EmmaFace_839
                            if Tempshame >= 30:
                                ch_e "You understand I only wear this sort of thing in private."  
                            else:
                                ch_e "It is a comfortable outfit."   
                    elif Tempshame <= 15:  
                            call EmmaFace("bemused", 1) from _call_EmmaFace_840
                            ch_e "Rather too daring, don't you think?."
                            $ Agree = 0
                            
                    #elif Tempshame >= 15 and "public" not in E_History:                 #maybe remove later     
                    #        ch_e "I doubt I could get away with this in public, [E_Petname]."
                    #        $ Agree = 0
                        
                    elif Tempshame <= 25 and (ApprovalCheck("Emma", 2300, TabM=0, C = 0) or ApprovalCheck("Emma", 700, "I", TabM=0, C = 0)):
                            ch_e "This is particularly inappropriate. . . in the best ways."
                    elif Tempshame <= 25:
                            call EmmaFace("angry", 1) from _call_EmmaFace_841
                            ch_e "I don't believe even I could pull off this look, [E_Petname]."
                            $ Agree = 0
                    elif (ApprovalCheck("Emma", 2500, TabM=0, C = 0) or ApprovalCheck("Emma", 800, "I", TabM=0, C = 0)):
                            call EmmaFace("bemused", 1) from _call_EmmaFace_842
                            ch_e "This look certainly pushes the boundaries."
                    else:
                            call EmmaFace("angry", 1) from _call_EmmaFace_843
                            ch_e "Even I can't pull this off."
                            $ Agree = 0
                        
                    $ E_OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ E_Custom2[1] = E_Arms  
                            $ E_Custom2[2] = E_Legs 
                            $ E_Custom2[3] = E_Over
                            $ E_Custom2[4] = E_Neck 
                            $ E_Custom2[5] = E_Chest 
                            $ E_Custom2[6] = E_Panties
                            $ E_Custom2[8] = E_Hair
                            $ E_Custom2[9] = E_Hose
                            $ E_Custom2[0] = 2 if Agree else 1           
                    elif Custom == 6:
                            $ E_Custom3[1] = E_Arms  
                            $ E_Custom3[2] = E_Legs 
                            $ E_Custom3[3] = E_Over
                            $ E_Custom3[4] = E_Neck 
                            $ E_Custom3[5] = E_Chest 
                            $ E_Custom3[6] = E_Panties
                            $ E_Custom3[8] = E_Hair
                            $ E_Custom3[9] = E_Hose
                            $ E_Custom3[0] = 2 if Agree else 1
                    elif Custom == 11:
                            $ E_Custom4[1] = E_Arms  
                            $ E_Custom4[2] = E_Legs 
                            $ E_Custom4[3] = E_Over
                            $ E_Custom4[5] = E_Chest 
                            $ E_Custom4[6] = E_Panties
                            $ E_Custom4[8] = E_Hair
                            $ E_Custom4[9] = E_Hose
                            $ E_Custom4[0] = 2 if Agree else 1           
                    elif Custom == 12:
                            $ E_Custom5[1] = E_Arms  
                            $ E_Custom5[2] = E_Legs 
                            $ E_Custom5[3] = E_Over
                            $ E_Custom5[5] = E_Chest 
                            $ E_Custom5[6] = E_Panties
                            $ E_Custom5[8] = E_Hair
                            $ E_Custom5[9] = E_Hose
                            $ E_Custom5[0] = 2 if Agree else 1           
                    elif Custom == 13:
                            $ E_Custom6[1] = E_Arms  
                            $ E_Custom6[2] = E_Legs 
                            $ E_Custom6[3] = E_Over
                            $ E_Custom6[5] = E_Chest 
                            $ E_Custom6[6] = E_Panties
                            $ E_Custom6[8] = E_Hair
                            $ E_Custom6[9] = E_Hose
                            $ E_Custom6[0] = 2 if Agree else 1           
                    elif Custom == 14:
                            $ E_Custom7[1] = E_Arms  
                            $ E_Custom7[2] = E_Legs 
                            $ E_Custom7[3] = E_Over
                            $ E_Custom7[5] = E_Chest 
                            $ E_Custom7[6] = E_Panties
                            $ E_Custom7[8] = E_Hair
                            $ E_Custom7[9] = E_Hose
                            $ E_Custom7[0] = 2 if Agree else 1
                    elif Custom == 7 and Agree:
                            $ E_Gym[1] = E_Arms  
                            $ E_Gym[2] = E_Legs 
                            $ E_Gym[3] = E_Over
                            $ E_Gym[4] = E_Neck 
                            $ E_Gym[5] = E_Chest 
                            $ E_Gym[6] = E_Panties
                            $ E_Gym[8] = E_Hair
                            $ E_Gym[9] = E_Hose
                            $ E_Gym[0] = 2   
                    elif Custom == 9 and Agree:
                            $ E_Sleepwear[1] = E_Arms  
                            $ E_Sleepwear[2] = E_Legs 
                            $ E_Sleepwear[3] = E_Over
                            $ E_Sleepwear[4] = E_Neck 
                            $ E_Sleepwear[5] = E_Chest 
                            $ E_Sleepwear[6] = E_Panties
                            $ E_Sleepwear[8] = E_Hair
                            $ E_Sleepwear[9] = E_Hose
                            $ E_Sleepwear[0] = 2 if Agree else 1                            
                    else: #Typically Custom == 3
                            $ E_Custom[1] = E_Arms  
                            $ E_Custom[2] = E_Legs 
                            $ E_Custom[3] = E_Over
                            $ E_Custom[4] = E_Neck 
                            $ E_Custom[5] = E_Chest 
                            $ E_Custom[6] = E_Panties
                            $ E_Custom[8] = E_Hair
                            $ E_Custom[9] = E_Hose
                            $ E_Custom[0] = 2 if Agree else 1
                    #End check    
            $ E_Shame = Tempshame
            
            if Check:
                    pass
            elif "exhibitionist" in E_Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif E_Over == "towel" and E_Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Emma", 1600) or ApprovalCheck("Emma", 550, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and E_Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 30 and E_Loc == "bg pool": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Emma", 2200) or ApprovalCheck("Emma", 700, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Emma", 2500) or ApprovalCheck("Emma", 900, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            elif E_Loc == "bg dangerroom":
                    ch_e "I'm afraid I'll have to change, one moment."
                    $ E_Outfit = "teacher"
#                    $ E_Outfit = renpy.random.choice(["teacher", "costume"])
                    #$ E_Water = 0
                    call EmmaOutfit(Changed = 1) from _call_EmmaOutfit_46 
                    ch_e "Sorry for the wait."
            else:
                    ch_e "I'm afraid I'll have to change, one moment."
                    $ E_Outfit = "teacher"
#                    $ E_Outfit = renpy.random.choice(["teacher", "costume"])
                    $ E_Water = 0
                    call EmmaOutfit(Changed = 1) from _call_EmmaOutfit_47 
                    ch_e "Sorry for the wait."
                    
            return        

#End Emma Custom clothes check.
    
# start emma hungry //////////////////////////////////////////////////////////
label Emma_Hungry:
    if E_Chat[3]:
        ch_e "I do enjoy your taste. . ."
    elif E_Chat[2]:
        ch_e "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_e "I do enjoy your taste. . ."
    $ E_Traits.append("hungry")
return


# end emma hungry //////////////////////////////////////////////////////////

    
# Start Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Emma_First_Les(0,1)
    if E_Les:
        return
    
    $ E_Les += 1
    $ E_RecentActions.append("lesbian")        
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 30, 2) 
    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Emma's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_e "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I, darling, but it seemed like fun."
                else:
                    ch_r "It's all right darling, I'll take care of you."
        if E_LikeRogue >= 60 and ApprovalCheck("Emma", (1500-(10*E_Les)-(10*(E_LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Emma", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif E_LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call EmmaFace("down", 2) from _call_EmmaFace_844  
                if GirlsNum:
                    "Emma also glances down at your cock"
                else:
                    "Emma glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Emma", 1500):
                call EmmaFace("surprised", 2) from _call_EmmaFace_845  
                ch_e "Um, you should put that away in public."
                call EmmaFace("bemused", 1) from _call_EmmaFace_846  
                if E_SeenPeen == 1: 
                    ch_e "Or maybe. . ."
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 15)                
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 20)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 35)  
                    
        elif E_SeenPeen > 10:
                return    
        elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                call EmmaFace("sly",1) from _call_EmmaFace_847 
                if E_SeenPeen == 1: 
                    call EmmaFace("surprised",2) from _call_EmmaFace_848  
                    ch_e "That's. . . impressive."
                    call EmmaFace("bemused",1) from _call_EmmaFace_849  
                    $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3) 
                elif E_SeenPeen == 2:  
                    ch_e "I can't get over that."               
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7) 
                elif E_SeenPeen == 5: 
                    ch_e "There it is."
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5)  
                elif E_SeenPeen == 10: 
                    ch_e "So beautiful."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 80, 10)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
        else:
                call EmmaFace("sad",1) from _call_EmmaFace_850 
                if E_SeenPeen == 1: 
                    call EmmaFace("perplexed",1 ) from _call_EmmaFace_851 
                    ch_e "Well that happened. . ."
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                elif E_SeenPeen < 5: 
                    call EmmaFace("sad",0) from _call_EmmaFace_852 
                    ch_e "Huh."
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                elif E_SeenPeen == 10: 
                    ch_e " put that away."               
                    $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                    $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if E_SeenPeen > 10:
                    return
                elif ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "L"):
                        if E_SeenPeen == 1: 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 3) 
                        elif E_SeenPeen == 2:              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7) 
                        elif E_SeenPeen == 5: 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 5)  
                        elif E_SeenPeen == 10: 
                            $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)  
                else:
                        if E_SeenPeen == 1: 
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3)  
                        elif E_SeenPeen < 5: 
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 2)  
                        elif E_SeenPeen == 10:              
                            $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 50, 7)
                            $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 3) 
                            
    if E_SeenPeen == 1:            
        $ E_Love = Statupdate("Emma", "Love", E_Love, 90, 10)                
        $ E_Obed = Statupdate("Emma", "Obed", E_Obed, 90, 25)
        $ E_Inbt = Statupdate("Emma", "Inbt", E_Inbt, 60, 20) 
        $ E_Lust = Statupdate("Emma", "Lust", E_Lust, 200, 5)
    
    return
# End Emma first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
label Emma_Tits_Up:
    $ E_Tits = 1
    if Emma_Arms == 1:
        pass    
    elif E_Chest == "corset" or E_Chest == "black corset" or E_Chest == "NewX" or E_Chest == "NewX black" or E_Chest == "bikini":
        pass
    else:
        #if all checks fail,
        $ E_Tits = 0    
    return

label Emma_Show_Plug:
    
    menu:
        "Slap her ass.":
            $ D20A = renpy.random.randint(1, 20) #Sets random seed factor for the encounter

            show Slap_Ass2 zorder 200
            call E_Slap_Ass from _call_E_Slap_Ass_6 
            hide Slap_Ass2
            if Taboo and (D20A + (int(Taboo/10)) - Stealth) >= 10:        #If there is a Taboo level, and your modified roll is over 10
                call Emma_Taboo from _call_Emma_Taboo_1
            jump Emma_Show_Plug
            

        "Very happy.":
            pass

    return