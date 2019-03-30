# star Laura chat interface
label Laura_Chat_Set(Preset=0):
    if "met" not in newgirl["Laura"].History:
            "Who?"
            return
    if Preset:   
            ch_p "Hey [newgirl[Laura].GirlName]. . ."
            call Shift_Focus("Laura")
            if newgirl["Laura"].Loc != bg_current:
                        show Cellphone at SpriteLoc(StageLeft)
            else:
                        hide Cellphone            
            if Preset == "chat":
                    $ renpy.pop_call() #removes the call to chat subroutine
                    $ renpy.pop_call() #This removes the callback to the previous chat session
            elif Preset == "settings":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    call Laura_Settings  
            elif Preset == "wardrobe":
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous settings menu
                    $ renpy.pop_call() #this removes the callback to the previous settings menu testing. . .
                    ch_p "I wanted to talk about your outfit. . ."
                    if Taboo:
                            if "exhibitionist" in newgirl["Laura"].Traits:
                                ch_l "Yes? . ."  
                            elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 400, "I", TabM=3): 
                                ch_l "I don't think I'm supposed to undress around here. . ."
                            else:
                                ch_l "I don't think I'm supposed to undress around here. . ."
                                ch_l "Can we talk about this in our rooms?"
                                jump Laura_Chat
                            call Laura_Clothes
                    elif ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 300, "O"):
                                ch_l "Oh? What about them?"
                                call Laura_Clothes
                    else:
                                ch_l "I don't think about my clothes much."
                                ch_l "You shouldn't either."   
            #end preset menu
                 
                        
label Laura_Chat:
    call LauraFace    
    call Shift_Focus("Laura")
    call Change_Focus("Laura")
    if newgirl["Laura"].Loc != bg_current:
                show Cellphone at SpriteLoc(StageLeft)
    else:
                hide Cellphone
    if "caught" in newgirl["Laura"].RecentActions:
                ch_l "I think we should lie low for a bit."
                return
    if "angry" in newgirl["Laura"].RecentActions:
                ch_l "You don't want to be around me right now."
                return
    menu:
        ch_l "Yeah?"
        "Come on over." if newgirl["Laura"].Loc != bg_current:
                    if Room_Full():
                        "I don't think there would be room."
                        menu:
                            "Did you want to ask someone to leave?"
                            "Rogue" if R_Loc == bg_current:
                                call Rogue_Dismissed
                            "Kitty" if K_Loc == bg_current:
                                call Kitty_Dismissed
                            "Emma" if E_Loc == bg_current:
                                call Emma_Dismissed
                    else:
                            call Laura_Summon    
        "Ask Laura to leave" if newgirl["Laura"].Loc == bg_current:
                    call Laura_Dismissed    
                    return
        
        "Flirt with her." if not newgirl["Laura"].Chat[5]:
                    call Laura_Flirt               
        "Flirt with her. (locked)" if newgirl["Laura"].Chat[5]:  
                    pass
            
        "Sex Menu" if newgirl["Laura"].Loc == bg_current:
                    if newgirl["Laura"].Love >= newgirl["Laura"].Obed:   
                        ch_p "Did you want to fool around?"  
                    else: 
                        ch_p "I want to get naughty."
                    if "angry" in newgirl["Laura"].RecentActions:  
                        ch_l "Bad idea right now."
                    elif ApprovalCheck("Laura", 600, "LI"):
                        call LauraFace("sexy")
                        ch_l "Cool."
                        call Laura_SexMenu
                        return
                    elif ApprovalCheck("Laura", 400, "OI"):
                        ch_l "Yes, [newgirl[Laura].Petname]."
                        call Laura_SexMenu
                        return
                    else:
                        ch_l "No thanks, [newgirl[Laura].Petname]."          
                          
        "I just wanted to talk. . .":
                    call Laura_Chitchat   
                    
        "Laura's settings":
                    ch_p "Let's talk about you."
                    call Laura_Settings   
        
        "Relationship status":
                    ch_p "Could we talk about us?"  
                    if "relationship" in newgirl["Laura"].DailyActions:
                        ch_l "I need some time to. . .  process."
                    elif newgirl["Laura"].Loc == bg_current:
                        call Laura_Relationship
                    else:
                        ch_l "Sounds heavy."
                        ch_l "Maybe later when we're face to face?"
                        
        "Could I get your number?" if "Laura" not in Digits:
                    if ApprovalCheck("Laura", 400, "L") or ApprovalCheck("Laura", 200, "I"):
                        ch_l "Oh, sure."
                        $ Digits.append("Laura") 
                    elif ApprovalCheck("Laura", 200, "O"):
                        ch_l "I guess."             
                        $ Digits.append("Laura")
                    else:
                        ch_l "Um, probably not."  
                        
        "Gifts" if newgirl["Laura"].Loc == bg_current:
                    ch_p "I'd like to give you something."
                    call Laura_Gifts
                        
        "Add her to party" if "Laura" not in Party and newgirl["Laura"].Loc == bg_current:
                    ch_p "Could you follow me for a bit?"
                    if ApprovalCheck("Laura", 650):
                        $ Party.append("Laura")
                        ch_l "Where to?"
                        return
                    elif not ApprovalCheck("Laura", 400):
                        ch_l "No."
                    else:
                        ch_l "I'd rather not."
        "Disband party" if "Laura" in Party: 
                    ch_p "Ok, you can leave if you prefer."
                    $ Party.remove("Laura")       
                    call Laura_Schedule(0)                        
                    if "leaving" in newgirl["Laura"].RecentActions:
                        call DrainWord("Laura","leaving")
                    if newgirl["Laura"].Loc == bg_current:
                        ch_l "I think i'm fine here."
                    else:
                        ch_l "Ok, see ya then."
                        call Set_The_Scene   
                    return
                
        
        "Date":
                    ch_p "Do you want to go on a date tonight?"
                    call Laura_Date_Ask

        "Talk with Rogue" if R_Loc == bg_current:
                jump Rogue_Chat

        "Talk with Kitty" if K_Loc == bg_current:
                jump Kitty_Chat

        "Talk with Emma" if E_Loc == bg_current:
                jump Emma_Chat

        "Talk with Mystique" if newgirl["Mystique"].Loc == bg_current:
                jump Mystique_Chat
                            
        "Never mind.":
                    if newgirl["Laura"].Loc != bg_current:
                        ch_l "Ok."
                    return
    jump Laura_Chat


#Laura Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Laura_Relationship:
    menu:
        ch_l "What did you want to talk about?"
        
        "Do you want to be my girlfriend?" if "dating" not in newgirl["Laura"].Traits and "ex" not in newgirl["Laura"].Traits:
                $ newgirl["Laura"].DailyActions.append("relationship")
                if "asked boyfriend" in newgirl["Laura"].DailyActions and "angry" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry", 1)
                    ch_l "Still a no."
                    return
                
                $ newgirl["Laura"].DailyActions.append("asked boyfriend")
                
                if P_Harem and "LauraYes" not in P_Traits:  
                    if len(P_Harem) >= 2:
                        ch_l "You'd need to clear it with the others first, [newgirl[Laura].Petname]."
                    else:
                        ch_l "You'd need to clear it with [P_Harem[0]] first, [newgirl[Laura].Petname]."
                    return
                                    
                if newgirl["Laura"].Event[5]:
                    call LauraFace("bemused", 1)
                    ch_l "I asked, you said \"no\". . ."
                else:
                    call LauraFace("surprised", 2)
                    ch_l "Huh? . ." 
                    call LauraFace("smile", 1)
                    
                call Laura_OtherWoman
                
                if newgirl["Laura"].Love >= 800:
                    call LauraFace("surprised", 1)
                    $ newgirl["Laura"].Mouth = "smile"
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 40)
                    ch_l "Sure!"
                    if "boyfriend" not in newgirl["Laura"].Petnames:
                        $ newgirl["Laura"].Petnames.append("boyfriend")                
                    $ newgirl["Laura"].Traits.append("dating") 
                    if "LauraYes" in P_Traits:       
                                $ P_Traits.remove("LauraYes")
                                $ P_Harem.append("Laura")
                                call Harem_Initiation
                    "Laura tackles you and kisses you deeply."
                    call LauraFace("kiss", 1) 
                    $ newgirl["Laura"].Kissed += 1
                elif newgirl["Laura"].Obed >= 500:
                    call LauraFace("perplexed")
                    ch_l "I don't know, \"dating\". . ."
                elif newgirl["Laura"].Inbt >= 500:
                    call LauraFace("smile")                
                    ch_l "Nah, this is more fun."
                else:
                    call LauraFace("perplexed", 1)
                    ch_l "Whoa, slow down, [newgirl[Laura].Petname]."
                    
        "When you said you loved me. . ." if "lover" not in newgirl["Laura"].Traits and newgirl["Laura"].Event[6] >= 20:
                call Laura_Love_Redux
        
        "Do you want to get back together?" if "ex" in newgirl["Laura"].Traits:
                $ newgirl["Laura"].DailyActions.append("relationship")
                if "asked boyfriend" in newgirl["Laura"].DailyActions and "angry" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry", 1)
                    ch_l "Like I said, not interested."
                    return
                elif "asked boyfriend" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry", 1)
                    ch_l "Still a no."
                    return
                
                $ newgirl["Laura"].DailyActions.append("asked boyfriend")
                
                if P_Harem and "LauraYes" not in P_Traits:
                    $ newgirl["Laura"].DailyActions.append("asked boyfriend")   
                    if len(P_Harem) >= 2:
                        ch_l "You'd need to clear it with the others first, [newgirl[Laura].Petname]."
                    else:
                        ch_l "You'd need to clear it with [P_Harem[0]] first, [newgirl[Laura].Petname]."
                    return
                    
                $ Cnt = 0
                call Laura_OtherWoman
                                        
                if newgirl["Laura"].Love >= 800:
                    call LauraFace("surprised", 1)
                    $ newgirl["Laura"].Mouth = "smile"
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                    ch_l "Ok, you've earned another shot!"
                    if "boyfriend" not in newgirl["Laura"].Petnames:
                        $ newgirl["Laura"].Petnames.append("boyfriend")                
                    $ newgirl["Laura"].Traits.append("dating")          
                    $ newgirl["Laura"].Traits.remove("ex")
                    if "LauraYes" in P_Traits:       
                                $ P_Traits.remove("LauraYes")
                                $ P_Harem.append("Laura")
                                call Harem_Initiation
                    "Laura pulls you in and kisses you deeply."
                    call LauraFace("kiss", 1) 
                    $ newgirl["Laura"].Kissed += 1
                elif newgirl["Laura"].Love >= 600 and ApprovalCheck("Laura", 1500):
                    call LauraFace("smile", 1)
                    $ newgirl["Laura"].Mouth = "smile"
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                    ch_l "Um, ok, I guess."
                    if "boyfriend" not in newgirl["Laura"].Petnames:
                        $ newgirl["Laura"].Petnames.append("boyfriend")                
                    $ newgirl["Laura"].Traits.append("dating")             
                    $ newgirl["Laura"].Traits.remove("ex")
                    "Laura gives you a quick kiss."
                    call LauraFace("kiss", 1) 
                    $ newgirl["Laura"].Kissed += 1
                elif newgirl["Laura"].Obed >= 500:
                    call LauraFace("sad")
                    ch_l "I think it's best we keep things simple."   
                elif newgirl["Laura"].Inbt >= 500:
                    call LauraFace("perplexed")                
                    ch_l "That ruined the fun."
                else:
                    call LauraFace("perplexed", 1)
                    ch_l "I can't trust you like that."
                
        # End Back Together
                    
                               
#        "I think we should break up." if "dating" in R_Traits: #ApprovalCheck("Rogue", 950, "L", Bonus = (B/3)):
#            if "breakup talk" in R_RecentActions:
#                ch_r "We were {i}just{/i} over this, not even funny."
#            elif "breakup talk" in R_DailyActions:
#                ch_r "Tired of me again that quick?" 
#                ch_r "We're not having this talk today, [R_Petname]."
#            else:
#                call Rogue_Breakup                
            
            
#        "I'd like to bring Laura into this." if "poly Laura" not in R_Traits and not newgirl["Laura"].Break[0]:    #fix nonfunctional yet, switch over to Laura stuff
            
#            if "asked threesome" in R_RecentActions:
#                ch_r "Persistence will NOT be rewarded here."
#                return
#            elif "asked threesome" in R_DailyActions:
#                ch_r "I don't think my answer's changing any time soon." 
#                return
#            else:
#                $ R_DailyActions.append("asked threesome")                
#                $Cnt = int((R_LikeNewGirl["Laura"] - 500)/2)
#                menu:
#                    ch_r "What does she think about this?"
                        
#                    "She said I can be with you too." if "poly Rogue" in newgirl["Laura"].Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt):
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."
#                                $ R_Traits.append("poly Laura")
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she did, but I don't want to share."  
                    
#                    "I could ask if she'd be ok with me dating you both." if "poly Rogue" not in newgirl["Laura"].Traits:
#                        if ApprovalCheck("Rogue", 1800, Bonus = Cnt) or :
#                            call RogueFace("smile", 1)
#                            if R_Love >= R_Obed:
#                                ch_r "Just so long as we can be together, I can share."
#                            elif R_Obed >= R_Inbt:
#                                ch_r "I'm ok with that if she is."
#                            else:
#                                ch_r "Yeah, I mean I guess so."                        
#                            ch_r "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
#                        else:
#                            call RogueFace("angry", 1)
#                            ch_r "Well maybe she would, but I don't want to share."  
                    
#                    "Could you ask?":
#                        if R_LikeNewGirl["Laura"] >= 700:
#                            ch_r "I have to say I've kind of been thinking about it myself."  
#                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
#                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 1)
#                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)
#                        elif R_LikeNewGirl["Laura"] >= 500:
#                            ch_r "I guess, if that's what you want. . ." 
#                        elif R_Obed >= 700:
#                            ch_r "If that's what you want. . ." 
#                        else:
#                            ch_r "I can't really stand her, I don't think so."  
                            
                        
#                    "You're right, I was dumb to ask.":
#                        call RogueFace("sad")
#                        ch_r "Yeah, you were."  
                        
            #end Laura Threesome
                
        "You said you wanted me to be more in control?" if "sir" not in newgirl["Laura"].Petnames and "sir" in newgirl["Laura"].History:
                if "asked sub" in newgirl["Laura"].RecentActions:
                        ch_l "We just had this conversation."
                elif "asked sub" in newgirl["Laura"].DailyActions:
                        ch_l "Enough of that talk for one day. . ."            
                else:
                        call Laura_Sub_Asked
        "You said you wanted me to be your Master?" if "master" not in newgirl["Laura"].Petnames and "master" in newgirl["Laura"].History:
                if "asked sub" in newgirl["Laura"].RecentActions:
                        ch_l "We just had this conversation."
                elif "asked sub" in newgirl["Laura"].DailyActions:
                        ch_l "Enough of that talk for one day. . ."          
                else:
                        call Laura_Sub_Asked
                        
        "Never Mind":
            return
              
    return

label Laura_OtherWoman:
    return                      #fix, remove this once this portion works.
    $ Cnt = 0
    if "dating" in R_Traits:
        call LauraFace("perplexed")
        menu: 
            ch_l "But you're with Rogue right now."
            "She said I can be with you too." if "poly Laura" in R_Traits:
                $Cnt = int((newgirl["Laura"].LikeRogue - 500)/2)
                if ApprovalCheck("Laura", 1800, Bonus = Cnt):
                    call LauraFace("smile", 1)
                    if newgirl["Laura"].Love >= newgirl["Laura"].Obed:
                        ch_l "Just so long as we can be together, I can share."
                    elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                        ch_l "I'm ok with that if she is."
                    else:
                        ch_l "Yeah, I mean I guess so."
                        $ newgirl["Laura"].Traits.append("poly Rogue")
                else:
                    call LauraFace("angry", 1)
                    ch_l "Well maybe she did, but I don't want to share."  
                    $ renpy.pop_call()                                          #This causes it to jump past the previous menu on the return
            
            "I could ask if she'd be ok with me dating you both." if "poly Laura" not in R_Traits:
                $Cnt = int((newgirl["Laura"].LikeRogue - 500)/2)
                if ApprovalCheck("Laura", 1800, Bonus = Cnt):
                    call LauraFace("smile", 1)
                    if newgirl["Laura"].Love >= newgirl["Laura"].Obed:
                        ch_l "Just so long as we can be together, I can share."
                    elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                        ch_l "I'm ok with that if she is."
                    else:
                        ch_l "Yeah, I mean I guess so."                        
                    ch_l "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
                else:
                    call LauraFace("angry", 1)
                    ch_l "Well maybe she would, but I don't want to share."      
                $ renpy.pop_call()
            
            "What she doesn't know won't hurt her.":
                $Cnt = int((newgirl["Laura"].LikeRogue - 500)/2)
                if not ApprovalCheck("Laura", 1800, Bonus = -(int((newgirl["Laura"].LikeRogue - 600)/2))): #checks if Rogue likes you more than Laura
                    call LauraFace("angry", 1)
                    if not ApprovalCheck("Laura", 1800):
                        ch_l "Well I don't like you that much either."
                    else:
                        ch_l "Well I'm not cool with that, Rogue's a friend of mine."                    
                    $ renpy.pop_call() 
                    
                else:
                    call LauraFace("smile", 1)
                    if newgirl["Laura"].Love >= newgirl["Laura"].Obed:
                        ch_l "I really do want to be together with you."
                    elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                        ch_l "If that's how you want it to be."
                    else:
                        ch_l "I suppose that's true."
                    $ newgirl["Laura"].Traits.append("poly Rogue")
                    $ newgirl["Laura"].Traits.append("downlow")
                
            "I can break it off with her.":
                call LauraFace("sad")
                ch_l "Well then maybe I'll see you tomorrow after you have."                                   
                $ renpy.pop_call()
                
            "You're right, I was dumb to ask.":
                call LauraFace("sad")
                ch_l "We had a good thing there. Maybe some day. . ."                    
                $ renpy.pop_call()                     
                
    return
    
label Laura_Settings:
    menu:
        ch_p "Let's talk about you."
        "Wardrobe": 
                ch_p "I wanted to talk about your style."
                if newgirl["Laura"].Loc != "bg player" and newgirl["Laura"].Loc != "bg laura":  
                    if Taboo:
                        if "exhibitionist" in newgirl["Laura"].Traits:
                            ch_l "Yes? . ."  
                        elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 400, "I", TabM=3): 
                            ch_l "I don't think I'm supposed to undress around here. . ."
                        else:
                            ch_l "I don't think I'm supposed to undress around here. . ."
                            ch_l "Can we talk about this in our rooms?"
                            return
                    call Laura_Clothes
                elif ApprovalCheck("Laura", 900, TabM=4) or ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 300, "O"):
                            ch_l "Oh? What about them?"
                            call Laura_Clothes
                else:
                            ch_l "I don't think about my clothes much."
                            ch_l "You shouldn't either."    
                
        "Shift her Personality" if ApprovalCheck("Laura", 900, "L", TabM=0) or ApprovalCheck("Laura", 900, "O", TabM=0) or ApprovalCheck("Laura", 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call Laura_Personality
        
        
        "Dirty Talk":
                    ch_p "About when we have sex. . ."
                    call Laura_SexChat
          
        "Pet names":
            menu:  
                "Your Pet Name":
                    ch_p "Could we talk about my pet name?"
                    if ApprovalCheck("Laura", 600, "L", TabM=0) or ApprovalCheck("Laura", 300, "O", TabM=0):
                        call Laura_Names    
                    else:
                        $ newgirl["Laura"].Mouth = "smile"
                        ch_l "Oh?"
                        
                "Her Pet Name":
                        ch_p "I've got a pet name for you, you know?"
                        if ApprovalCheck("Laura", 600, "L", TabM=0):
                            ch_l "Do you?" 
                        elif ApprovalCheck("Laura", 300, "O", TabM=0):
                            ch_l "What did you want to call me?"
                        else:
                            ch_l "Yeah?"            
                        call Laura_Pet   
        
                "Back":
                        pass
                        
        "About other girls":
                menu:
                    ch_p "How do you feel about. . ."
                    "Rogue?":
                        call Laura_AboutRogue  
                    "Kitty?":
                        call Laura_AboutKitty
                    "Emma?":
                        call Laura_AboutEmma  
                    "Never mind.":
                        pass
            
        "Follow options" if "follow" in newgirl["Laura"].Traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ Line = 0
                menu:
                    ch_l "Yeah?"
                    "You can go where you want, I'll catch up later." if "freetravels" not in newgirl["Laura"].Traits:
                        call LauraFace("perplexed")
                        ch_l "Oh. . . okay."
                        if "follow" not in newgirl["Laura"].DailyActions:
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -2)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 5) 
                        $ newgirl["Laura"].Traits.append("freetravels")
                        $ Line = "free"
                            
                    "You can ask if I want to follow you." if "asktravels" not in newgirl["Laura"].Traits:
                        call LauraFace("perplexed")
                        ch_l "Right. . ."
                        if "follow" not in newgirl["Laura"].DailyActions:
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2) 
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                        $ Line = "ask"
                                                
                    "Don't ever leave when I'm around." if "lockedtravels" not in newgirl["Laura"].Traits:
                        if ApprovalCheck("Laura", 500, "O") or ApprovalCheck("Laura", 900, "L"):   
                            call LauraFace("smile")
                            ch_l "That's sweet."
                            if "follow" not in newgirl["Laura"].DailyActions:
                                if newgirl["Laura"].Love > 90:
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 99, 2)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)                             
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -5, 1) 
                            $ Line = "lock"
                        else:
                            call LauraFace("angry")                        
                            ch_l "Well, who cares what you think?"
                            
                    "Never mind.":
                        ch_l "Right. . ."
                        
                if Line:
                    $ newgirl["Laura"].DailyActions.append("follow")                
                    if "freetravels" in newgirl["Laura"].Traits:
                        $ newgirl["Laura"].Traits.remove("freetravels") 
                    if "asktravels" in newgirl["Laura"].Traits:
                        $ newgirl["Laura"].Traits.remove("asktravels") 
                    if "lockedtravels" in newgirl["Laura"].Traits:
                        $ newgirl["Laura"].Traits.remove("lockedtravels") 
                
                    if Line == "free":
                        $ newgirl["Laura"].Traits.append("freetravels")            
                    elif Line == "ask":
                        $ newgirl["Laura"].Traits.append("asktravels")                
                    elif Line == "lock":
                        $ newgirl["Laura"].Traits.append("lockedtravels")    
                    $ Line = 0        
                              
        "Gym clothes" if "asked gym" in newgirl["Laura"].DailyActions and "no ask gym" not in newgirl["Laura"].Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Don't worry about that, your gym clothes are cute."   
                    ch_l "Oh. . . ok."
                    $ newgirl["Laura"].Traits.append("no ask gym")
        "Gym clothes" if "no ask gym" in newgirl["Laura"].Traits:
                    ch_p "You asked me about your gym clothes?"
                    ch_p "Forget about that, I changed my mind."      
                    ch_l "Oh. . . ok."
                    $ newgirl["Laura"].Traits.remove("no ask gym")
                    
        "Private outfit" if newgirl["Laura"].Schedule[9]:
                    #if comfy is in newgirl["Laura"].Traits, she won't ask before changing
                    ch_p "You know that outfit you wear in private?"
                    menu:
                        ch_l "Yeah?"
                        "Just put them on without asking me about it." if "comfy" not in newgirl["Laura"].Traits:
                            $ newgirl["Laura"].Traits.append("comfy")
                        "Ask before changing into that." if "comfy" in newgirl["Laura"].Traits:
                            $ newgirl["Laura"].Traits.remove("comfy")
                        "Never Mind":
                            pass     
                            
        "Tasks" if "sir" in newgirl["Laura"].Petnames:
                ch_p "I have some tasks for you."
                call Laura_Controls
        
        "Never mind.":
            return 
    jump Laura_Settings

# End Laura Chat


# Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Laura_SexChat(Line = "Yeah, what did you want to talk about?"):
    while True:
            menu:
                ch_l "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in newgirl["Laura"].DailyActions:
                        ch_l "I remember."
                    else:
                        menu:
                            "Sex.":
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "sex":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "Yeah, I know that. . ."                                
                                        elif newgirl["Laura"].Favorite == "sex":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10)
                                            ch_l "I really like it too!"
                                        elif newgirl["Laura"].Sex >= 5:
                                            ch_l "Well I don't mind that."
                                        elif not newgirl["Laura"].Sex:
                                            call LauraFace("perplexed")
                                            ch_l "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "Heh, um, yeah, it's nice. . ."
                                        $ newgirl["Laura"].PlayerFav = "sex"
                                        
                            "Anal.":
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "anal":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "So you've said. . ."                                
                                        elif newgirl["Laura"].Favorite == "anal":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10)
                                            ch_l "I love it too!"
                                        elif newgirl["Laura"].Anal >= 10:
                                            ch_l "Yeah, it's. . . nice. . ."
                                        elif not newgirl["Laura"].Anal:
                                            call LauraFace("perplexed")
                                            ch_l "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused",Eyes="side")
                                            ch_l "Heh, heh, yeah, um, it's ok. . ."
                                        $ newgirl["Laura"].PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "blow":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 3)
                                            ch_l "Yeah, I know."                                
                                        elif newgirl["Laura"].Favorite == "blow":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "I love your dick!"
                                        elif newgirl["Laura"].Blow >= 10:
                                            ch_l "Yeah, you're pretty tasty."
                                        elif not newgirl["Laura"].Blow:
                                            call LauraFace("perplexed")
                                            ch_l "Who's sucking your dick?! Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I'm. . . getting used to the taste. . ."
                                        $ newgirl["Laura"].PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        call LauraFace("sly")   
                                        if newgirl["Laura"].PlayerFav == "titjob":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "Yeah, you've said that before. . ."                           
                                        elif newgirl["Laura"].Favorite == "titjob":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 7)
                                            ch_l "Yeah, I enjoy that too. . ."
                                        elif newgirl["Laura"].Tit >= 10:
                                            ch_l "It's certainly an interesting experience . . ."
                                        elif not newgirl["Laura"].Tit:
                                            call LauraFace("perplexed")
                                            ch_l "Who's titfucking you? It's Ms. Frost, isn't it!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "That's nice of you to say. . ."
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 5)
                                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 10)
                                        $ newgirl["Laura"].PlayerFav = "titjob"   
                                        
                            "Handjobs.":
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "hand":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "Yeah, you've said that. . ."                                
                                        elif newgirl["Laura"].Favorite == "hand":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 7)
                                            ch_l "You do feel pretty comfy. . ."
                                        elif newgirl["Laura"].Hand >= 10:
                                            ch_l "I like it too . . ."
                                        elif not newgirl["Laura"].Hand:
                                            call LauraFace("perplexed")
                                            ch_l "Who's jerking you off? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "Yeah, it's nice. . ."
                                        $ newgirl["Laura"].PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = newgirl["Laura"].FondleB + newgirl["Laura"].FondleT + newgirl["Laura"].SuckB + newgirl["Laura"].Hotdog
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "fondle":
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 3)
                                            ch_l "Yeah, I think we're clear on that. . ."                                
                                        elif newgirl["Laura"].Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "I love when you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_l "Yeah, it's really nice . . ."
                                        elif not Cnt:
                                            call LauraFace("perplexed")
                                            ch_l "Who's letting you feel her up? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I do like how that feels. . ."
                                        $ newgirl["Laura"].PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        call LauraFace("sly")
                                        if newgirl["Laura"].PlayerFav == "kiss you":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3)
                                            ch_l "Such a romantic. . ."                                
                                        elif newgirl["Laura"].Favorite == "kiss you":
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                                            ch_l "Hmm, the taste of you on my lips. . ."
                                        elif newgirl["Laura"].Kissed >= 10:
                                            ch_l "I love kissing you too . . ."
                                        elif not newgirl["Laura"].Kissed:
                                            call LauraFace("perplexed")
                                            ch_l "Who are you kissing? Is it Ms. Frost?!"
                                        else:
                                            call LauraFace("bemused")
                                            ch_l "I like kissing you too. . ."
                                        $ newgirl["Laura"].PlayerFav = "kiss you" 
                                
                        $ newgirl["Laura"].DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck("Laura", 800):
                                        call LauraFace("perplexed")
                                        ch_l ". . ."                                    
                                else:
                                        if newgirl["Laura"].SEXP >= 50:
                                            call LauraFace("sly")
                                            ch_l "You should know. . ."   
                                        else:                 
                                            call LauraFace("bemused")
                                            $ newgirl["Laura"].Eyes = "side"
                                            ch_l "Hmm. . ."
                                            
                                            
                                        if not newgirl["Laura"].Favorite or newgirl["Laura"].Favorite == "kiss":
                                            ch_l "Kissing?"  
                                        elif newgirl["Laura"].Favorite == "anal":
                                                ch_l "Probably anal."  
                                        elif newgirl["Laura"].Favorite == "lick ass":
                                                ch_l "When you lick my ass." 
                                        elif newgirl["Laura"].Favorite == "insert ass":
                                                ch_l "Fingering my asshole, probably." 
                                        elif newgirl["Laura"].Favorite == "sex":
                                                ch_l "Just the usual pounding." 
                                        elif newgirl["Laura"].Favorite == "lick pussy":
                                                ch_l "When you lick my pussy." 
                                        elif newgirl["Laura"].Favorite == "fondle pussy":
                                                ch_l "When you finger me." 
                                        elif newgirl["Laura"].Favorite == "blow":
                                                ch_l "I like how your cock tastes." 
                                        elif newgirl["Laura"].Favorite == "tit":
                                                ch_l "when I use my tits." 
                                        elif newgirl["Laura"].Favorite == "hand":
                                                ch_l "I like jerking you off." 
                                        elif newgirl["Laura"].Favorite == "hotdog":
                                                ch_l "When you grind against me." 
                                        elif newgirl["Laura"].Favorite == "suck breasts":
                                                ch_l "When you suck my tits."  
                                        elif newgirl["Laura"].Favorite == "fondle breasts":
                                                ch_l "When you grabmy tits." 
                                        elif newgirl["Laura"].Favorite == "fondle thighs":
                                                ch_l "When you rub my thighs."
                                        else:
                                                ch_l "How should I know?"    
                                                
                                # End Laura's favorite things.
                    
                    
                "Don't talk as much during sex." if "vocal" in newgirl["Laura"].Traits:
                        if "setvocal" in newgirl["Laura"].DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:              
                            if ApprovalCheck("Laura", 1000) and newgirl["Laura"].Obed <= newgirl["Laura"].Love:
                                call LauraFace("bemused")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l "Stay quiet, got it."
                                $ newgirl["Laura"].Traits.remove("vocal")   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l ". . ."
                                $ newgirl["Laura"].Traits.remove("vocal")   
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -3)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5)
                                ch_l "Don't push it, [newgirl[Laura].Petname]."
                            else:
                                call LauraFace("angry")
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -3)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 10)
                                ch_l "I don't take orders from you, [newgirl[Laura].Petname]."
                                                
                            $ newgirl["Laura"].DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in newgirl["Laura"].Traits:
                        if "setvocal" in newgirl["Laura"].DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:     
                            if ApprovalCheck("Laura", 1000) and newgirl["Laura"].Obed <= newgirl["Laura"].Love:
                                call LauraFace("sly")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                                ch_l "Louder? Ok. . ."
                                $ newgirl["Laura"].Traits.append("vocal")   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                                ch_l "If you want, [newgirl[Laura].Petname]."
                                $ newgirl["Laura"].Traits.append("vocal")   
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 3)
                                ch_l "I guess?"
                                $ newgirl["Laura"].Traits.append("vocal")   
                            else:
                                call LauraFace("angry")
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5)
                                ch_l ". . ."  
                                
                            $ newgirl["Laura"].DailyActions.append("setvocal")  
                        # End Laura Dirty Talk
                    
                    
                "Don't do your own thing as much during sex." if "passive" not in newgirl["Laura"].Traits:
                        if "initiative" in newgirl["Laura"].DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:       
                            if ApprovalCheck("Laura", 1200) and newgirl["Laura"].Obed <= newgirl["Laura"].Love:
                                call LauraFace("bemused")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l "Passive, eh?"     
                                $ newgirl["Laura"].Traits.append("passive")                  
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l "I'll try to hold back."
                                $ newgirl["Laura"].Traits.append("passive")
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -3)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -1)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5)
                                ch_l "Hm, no."
                            else:
                                call LauraFace("angry")
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -3)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 10)
                                ch_l "We'll see."
                                
                            $ newgirl["Laura"].DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in newgirl["Laura"].Traits:
                        if "initiative" in newgirl["Laura"].DailyActions:
                            call LauraFace("perplexed")
                            ch_l "I heard you the first time."
                        else:   
                            if ApprovalCheck("Laura", 1000) and newgirl["Laura"].Obed <= newgirl["Laura"].Love:
                                call LauraFace("bemused")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l "More active, got it."    
                                $ newgirl["Laura"].Traits.remove("passive")                   
                            elif ApprovalCheck("Laura", 700, "O"):
                                call LauraFace("sadside")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                ch_l "If you insist."
                                $ newgirl["Laura"].Traits.remove("passive")    
                            elif ApprovalCheck("Laura", 600):
                                call LauraFace("sly")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 3)
                                ch_l "We'll see."
                                $ newgirl["Laura"].Traits.remove("passive")  
                            else:
                                call LauraFace("angry")
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5)
                                ch_l "Too much work."  
                                
                            $ newgirl["Laura"].DailyActions.append("initiative")   
                "Never Mind" if Line == "Yeah, what did you want to talk about?":
                    return
                "That's all." if Line != "Yeah, what did you want to talk about?":
                    return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Laura Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Laura Chitchat /////////////////// #Work in progress
label Laura_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        
        if "Laura" not in Digits:
                if ApprovalCheck("Laura", 500, "L") or ApprovalCheck("Laura", 250, "I"):
                    ch_l "Oh, here's my number, in case you need back-up."
                    $ Digits.append("Laura")  
                    return
                elif ApprovalCheck("Laura", 250, "O"):
                    ch_l "If you need to contact me, here's my number."             
                    $ Digits.append("Laura")
                    return
                
        if "hungry" not in newgirl["Laura"].Traits and (newgirl["Laura"].Swallow + newgirl["Laura"].Chat[2]) >= 10 and newgirl["Laura"].Loc == bg_current:  #She's swallowed a lot        
                call Laura_Hungry
                return  
        
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in newgirl["Laura"].DailyActions:
#            $ Options.append("caught")
        if newgirl["Laura"].Event[0] and "key" not in newgirl["Laura"].Chat:
            $ Options.append("key")
        if "lover" in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 900, "L"): # luvy dovey       
            $ Options.append("luv")
              
        if "mandrill" in P_Traits and "cologne chat" not in newgirl["Laura"].DailyActions:
            $ Options.append("mandrill")        
        if "purple" in P_Traits and "cologne chat" not in newgirl["Laura"].DailyActions:
            $ Options.append("purple")        
        if "corruption" in P_Traits and "cologne chat" not in newgirl["Laura"].DailyActions:
            $ Options.append("corruption")
        
        if newgirl["Laura"].Date >= 1:
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in newgirl["Laura"].DailyActions and "cheek" not in newgirl["Laura"].Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if newgirl["Laura"].Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in P_DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in newgirl["Laura"].DailyActions:
            #If you've caught Laura showering today
            $ Options.append("showercaught")
        if "fondle breasts" in newgirl["Laura"].DailyActions or "fondle pussy" in newgirl["Laura"].DailyActions or "fondle ass" in newgirl["Laura"].DailyActions:
            #If you've fondled Laura today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in newgirl["Laura"].Inventory and "256 Shades of Grey" in newgirl["Laura"].Inventory and "Avengers Tower Penthouse" in newgirl["Laura"].Inventory:   
            #If you've given Laura the books
            if "book" not in newgirl["Laura"].Chat:
                $ Options.append("booked")
        if "lace bra" in newgirl["Laura"].Inventory or "lace panties" in newgirl["Laura"].Inventory:   
            #If you've given Laura the lingerie
            if "lingerie" not in newgirl["Laura"].Chat:
                $ Options.append("lingerie")
        if newgirl["Laura"].Hand:   
            #If Laura's given a handjob
            $ Options.append("handy")
        if newgirl["Laura"].Swallow:   
            #If Laura's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in newgirl["Laura"].DailyActions or "painted" in newgirl["Laura"].DailyActions:
            #If Laura's been facialed
            $ Options.append("facial")
        if newgirl["Laura"].Sleep:
            #If Laura's slept over
            $ Options.append("sleep")
        if newgirl["Laura"].CreamP or newgirl["Laura"].CreamA:
            #If Laura's been creampied
            $ Options.append("creampie")
        if newgirl["Laura"].Sex or newgirl["Laura"].Anal:
            #If Laura's been sexed
            $ Options.append("sexed")
        if newgirl["Laura"].Anal:
            #If Laura's been analed
            $ Options.append("anal")
            
#        if not newgirl["Laura"].Chat[0] and newgirl["Laura"].Sex:
#            $ Options.append("virgin")    
            
#        if (bg_current == "bg laura" or bg_current == "bg player") and "relationship" not in newgirl["Laura"].DailyActions:
#            if "lover" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 900, "L"): # newgirl["Laura"].Event[6]        
#                $ Options.append("lover?")
#            elif "sir" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 500, "O"): # newgirl["Laura"].Event[7]
#                $ Options.append("sir?")      
#            elif "daddy" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 750, "L") and ApprovalCheck("Laura", 500, "O") and ApprovalCheck("Laura", 500, "I"): # newgirl["Laura"].Event[5]
#                $ Options.append("daddy?")
#            elif "master" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 900, "O"): # newgirl["Laura"].Event[8]
#                $ Options.append("master?")
#            elif "sex friend" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 500, "I"): # newgirl["Laura"].Event[9]
#                $ Options.append("sexfriend?")
#            elif "fuck buddy" not in newgirl["Laura"].Petnames and ApprovalCheck("Laura", 900, "I"): # newgirl["Laura"].Event[10]
#                $ Options.append("fuckbuddy?")  
            
        
        if not ApprovalCheck("Laura", 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ newgirl["Laura"].DailyActions.append("cologne chat") 
        call LauraFace("confused")
        ch_l "(sniff, sniff). . . smalls like. . . ape . . ."
        call LauraFace("sexy", 2)
        ch_l ". . . did you want to do something later?"    
    elif Options[0] == "purple":              
        $ newgirl["Laura"].DailyActions.append("cologne chat") 
        call LauraFace("sly",1)
        ch_l "(sniff, sniff). . . what is that? . ."
        call LauraFace("normal",0)
        ch_l ". . . what was it you wanted?"    
    elif Options[0] == "corruption":              
        $ newgirl["Laura"].DailyActions.append("cologne chat") 
        call LauraFace("confused")
        ch_l "(sniff, sniff). . . that's a strong scent. . ."
        call LauraFace("angry")
        ch_l ". . . a dangerous scent. . ."
        call LauraFace("sly")
                
    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in newgirl["Laura"].Chat:
                    ch_l "We should be more careful about getting caught."
                    if not ApprovalCheck("Laura", 500, "I"):
                         ch_l "Unless. . ."
            else:    
                    ch_l "Sorry we got dragged into the Professor's office like that."
                    if not ApprovalCheck("Laura", 500, "I"):
                        ch_l "I guess you wouldn't want to get it on in public anymore."
                    else:
                        ch_l "I kind of enjoyed it though. . ."
                    $ newgirl["Laura"].Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            if newgirl["Laura"].SEXP <= 15:
                ch_l "I gave you the key for convenience, don't abuse it . ."
            else:
                ch_l "I gave you a key, but you don't visit. . ."
            $ newgirl["Laura"].Chat.append("key") 
        
#    elif Options[0] == "cheek":
#            #Laura's response to having her cheek touched.
#            ch_l "So,[newgirl[Laura].Petname]. . .y'know how you[newgirl[Laura].like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            call LauraFace("smile",1)
#            ch_l "More than just {i}okay{/i}."
#            $ newgirl["Laura"].Chat.append("cheek") 
            
    elif Options[0] == "dated":
            #Laura's response to having gone on a date with the Player.
            ch_l "That was fun last night, we should do that again some time."

    elif Options[0] == "kissed":
            #Laura's response to having been kissed by the Player.
            call LauraFace("normal",1)
            ch_l "You're pretty good at kissing, [newgirl[Laura].Petname]."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        call LauraFace("smile",1)
                        ch_l "You'll have to back that claim up."
                "No. You think?":
                        ch_l "Do I look like a kidder?"

    elif Options[0] == "dangerroom":
            #Laura's response to Player working out in the Danger Room while Laura is present
            call LauraFace("sly",1)
            ch_l "Hey,[newgirl[Laura].Petname].  I saw you in the Danger Room, earlier."
            ch_l "You should probably keep your left up, you were taking too many shots to the head."

    elif Options[0] == "showercaught":
            #Laura's response to being caught in the shower.
            if "shower" in newgirl["Laura"].Chat: 
                ch_l "You saw me taking a shower again. . ."                       
            else:
                ch_l "Do you make a habit of bursting into the showers?"            
                $ newgirl["Laura"].Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident!  I promise!":             
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 5)    
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2) 
                            if ApprovalCheck("Laura", 1200):
                                call LauraFace("sly",1)
                                ch_l "I didn't mind."
                            call LauraFace("smile")
                            ch_l "We all make mistakes."
                    "Just with you.":        
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 5)   
                            if ApprovalCheck("Laura", 1000) or ApprovalCheck("Laura", 700, "L"):      
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3)    
                                    call LauraFace("sly",1)
                                    ch_l "Hmm, I guess that's a compliment."
                            else:                
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5) 
                                    call LauraFace("angry")
                                    ch_l "I think I should be insulted."                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck("Laura", 1200):                     
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3)          
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 10)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 5) 
                                    call LauraFace("sly",1)
                                    ch_l "You seem to know what you want."
                            elif ApprovalCheck("Laura", 800):                          
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 5) 
                                    call LauraFace("perplexed",2)
                                    ch_l "I guess you show initiative."
                                    $ newgirl["Laura"].Blush = 1
                            else:                
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -10) 
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -10)          
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)  
                                    call LauraFace("angry")
                                    ch_l "That's a bit disturbing."

    elif Options[0] == "fondled":
            #Laura's response to being felt up.
            if newgirl["Laura"].FondleB + newgirl["Laura"].FondleP + newgirl["Laura"].FondleA >= 15:
                ch_l "I need your hands on me." 
            else:                
                ch_l "You could feel me up, if you wanted."

    elif Options[0] == "booked":
            #Laura's response after a Player gives her the books from the shop.
            ch_l "Hey, I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        call LauraFace("sly",2)
                        ch_l "They were. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":                     
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -3)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 5)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 5) 
                        call LauraFace("angry")
                        ch_l "I don't see how."                
            $ newgirl["Laura"].Blush = 1
            $ newgirl["Laura"].Chat.append("book") 

    elif Options[0] == "lingerie":
            #Laura's response to being given lingerie.
            call LauraFace("sly",2)
            ch_l "That underwear ou got me was kind of uncomfortable, but I do like the look."
            $ newgirl["Laura"].Blush = 1
            $ newgirl["Laura"].Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Laura's response after giving the Player a handjob.
            call LauraFace("sly",1)
            ch_l "I was thinking about having your cock in my hand the other day. . ."
            ch_l "You seemed to enjoy it."
            $ newgirl["Laura"].Blush = 0

    elif Options[0] == "blow":
            if "blow" not in newgirl["Laura"].Chat:
                    #Laura's response after giving the Player a blowjob.
                    call LauraFace("sly",2)
                    ch_l "Hey, so did you like that blowjob?"
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 10) 
                                    call LauraFace("normal",1)
                                    ch_l "Cool. Cool. . . "
                                    call LauraFace("sexy",1)
                                    ch_l "I'd like another taste sometime."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck("Laura", 300, "I") or not ApprovalCheck("Laura", 800):                     
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)          
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 10)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 10) 
                                    call LauraFace("perplexed",1)
                                    ch_l "Yeah? Sorry to disappoint."
                                else:                              
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 15)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 5) 
                                    call LauraFace("sexy",1)
                                    ch_l "Yeah? I suppose we could keep trying until I get it right."                                  
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 10)   
                                call LauraFace("angry",2)
                                ch_l "Well, good luck with that then."
                    $ newgirl["Laura"].Blush = 1
                    $ newgirl["Laura"].Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_l "[Line]"

    elif Options[0] == "swallowed":
            #Laura's response after swallowing the Player's cum.
            if "swallow" in newgirl["Laura"].Chat:                
                ch_l "Hey, I wouldn't mind another taste of you some time."
            else:
                ch_l "So. . . the other day. . ."
                ch_l "That was the first time I'd really enjoyed the taste of jiz."
                call LauraFace("sly",1)
                ch_l "Good job!"
                $ newgirl["Laura"].Chat.append("swallow") 

    elif Options[0] == "facial":
            #Laura's response after taking a facial from the Player.
            ch_l "Hey. . .I know this is kind of odd. . ."
            call LauraFace("sexy",2)
            ch_l "I feel so {i}good{/i} with your jiz on my face."
            $ newgirl["Laura"].Blush = 1

    elif Options[0] == "sleepover":
            #Laura's response after sleeping with the Player.
            ch_l "I really enjoyed the other night."
            ch_l "It felt so safe sleeping next to someone else."

    elif Options[0] == "creampie":
            #Another of Laura's responses after having sex with the Player.
            "Laura draws close to you so she can whisper into your ear."
            ch_l "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Laura after having sex with the Player.
            ch_l "So. . . you should know. . ."
            call LauraFace("sexy",2)
            ch_l ". . .lately when I've been flicking the bean. . ."
            ch_l "I've been thinking about you inside of me."
            $ newgirl["Laura"].Blush = 1

    elif Options[0] == "anal":
            #Laura's response after getting anal from the Player.
            call LauraFace("sly")
            ch_l "I did't really enjoy anal much."
            call LauraFace("sexy",1)
            ch_l "Until you, at least."
        
#    elif Options[0] == "boyfriend?":
#        call Laura_BF
#    elif Options[0] == "lover?":
#        call Laura_Love
#    elif Options[0] == "sir?":
#        call Laura_Sub
#    elif Options[0] == "master?":
#        call Laura_Master
#    elif Options[0] == "sexfriend?":
#        call Laura_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Laura_Fuckbuddy 
#    elif Options[0] == "daddy?":
#        call Laura_Daddy  
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to smell you near me.", 
                "Back off.",
                "Buzz off."])
        ch_l "[Line]"
        
    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)        
            if D20 == 1:
                    call LauraFace("smile")
                    ch_l "I got a good grade on that bio test."
            elif D20 == 2:
                    call LauraFace("annoyed")
                    ch_l "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
            elif D20 == 3:
                    call LauraFace("surprised")
                    ch_l "Huh? Oh, sorry. I sort of spaced out. That's not like me."
            elif D20 == 4:
                    call LauraFace("sad")
                    ch_l "Oh, [newgirl[Laura].Petname]. I was just remembering something. Don't worry about it."
            elif D20 == 5:
                    call LauraFace("smile")
                    ch_l "I had a good nap. It's nice to be somewhere I can just doze off without worry."
            elif D20 == 6:
                    call LauraFace("perplexed")
                    ch_l "Oh, [newgirl[Laura].Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
            elif D20 == 7:
                    call LauraFace("smile")
                    ch_l "I just got a new personal best time in the Danger Room."
            elif D20 == 8:
                    call LauraFace("sad")
                    ch_l "I like being here, but sometimes there's just so much noise..."
            elif D20 == 9:
                    call LauraFace("confused")
                    ch_l "I'm still trying to figure out what the mystery meat in the cafeteria was today."
                    ch_l "I have enhanced senses, this shouldn't be so difficult!"
            elif D20 == 10:
                    call LauraFace("smile")
                    ch_l "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
            elif D20 == 11:
                    call LauraFace("smile")
                    ch_l "I tried out a dance class like Kitty said. Apparently I'm good at it."
            elif D20 == 12:
                    call LauraFace("sad")
                    ch_l "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
                    ch_l "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
            elif D20 == 13:
                    call LauraFace("smile")
                    ch_l "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
            elif D20 == 14:
                    call LauraFace("sad")
                    ch_l "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
            elif D20 == 15:
                    call LauraFace("perplexed")
                    ch_l "So they're called the \"Avengers\", but do they ever do any avenging?"
                    ch_l "At least the Fantastic Four really do things that are strange and fantastic."
            elif D20 == 16:
                    call LauraFace("perplexed")
                    ch_l "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
            elif D20 == 17:
                    call LauraFace("perplexed")
                    ch_l "Logan just walked up and told me that if I ever meet someone called. . ."
                    ch_l "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
                    ch_l "What's up with that?"
            elif D20 == 18:
                    call LauraFace("smile")
                    ch_l "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
            elif D20 == 19:
                    call LauraFace("confused")
                    ch_l "Do you smell something? Is that... nachos and... chocolate syrup?!"
            elif D20 == 20:
                    call LauraFace("smile")
                    ch_l "I like being able to just talk about nothing in particular. It's... nice."
            else:
                    call LauraFace("smile")
                    ch_l "You're fun to hang with."
        
    $ Line = 0
    return

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
label Laura_Flirt:
    
    if newgirl["Laura"].Loc == bg_current:         
        $ newgirl["Laura"].Chat[5] = 1                                         #can only flirt once per cycle. 
        menu:        
#            "Compliment her":
                
#            "Say you love her":
                
            "Touch her cheek":                                                                              
                    call Laura_TouchCheek
            "Pat her head":
                    call Laura_Headpat
            "Kiss her cheek":                                                                            
                    "You lean over, tilt her head back, and kiss her on the cheek."                
                    if ApprovalCheck("Laura", 700, "L", TabM=1):
                        call LauraFace("perplexed", 2) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2) 
                        ch_l ". . ."
                        call LauraFace("sexy", 1, Eyes="side") 
                        ch_l "Huh."
                    elif ApprovalCheck("Laura", 500, "L", TabM=1):
                        call LauraFace("surprised", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 1) 
                        ch_l ". . . hey!"
                        ch_l "What's that about?"
                    elif ApprovalCheck("Laura", 300, "L", TabM=1):                    
                        call LauraFace("angry", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1) 
                        ch_l "That's a bit forward."
                    else: 
                        call LauraFace("angry", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 5)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3) 
                        ch_l "Keep back!"
                    if "addict laura" in P_Traits:
                        $ newgirl["Laura"].Addict -= 1
                        $ newgirl["Laura"].Addictionrate += 1
                        $ newgirl["Laura"].Addictionrate = 3 if newgirl["Laura"].Addictionrate < 3 else newgirl["Laura"].Addictionrate 
                   
            "Kiss her lips":                                                                                    #Kiss her
                    if ApprovalCheck("Laura", 1000, TabM=1) or ApprovalCheck("Laura", 600, "L", TabM=1):        
                        "You lean down, tilt her head back, and plant a kiss on her lips."
                    elif ApprovalCheck("Laura", 1000) or ApprovalCheck("Laura", 600, "L"):  
                        call LauraFace("bemused", 1)
                        $ newgirl["Laura"].Eyes = "side"         
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -5)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                        "You lean close for a kiss, but Laura gently elbows your ribs."
                        ch_l "Not here, [newgirl[Laura].Petname]." 
                        return
                    else:                
                        call LauraFace("angry", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -15)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -5)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 5) 
                        "You lean close for a kiss, but Laura checks you onto your butt."
                        ch_l "Keep to yourself, [newgirl[Laura].Petname]." 
                        return
                    if newgirl["Laura"].Kissed:
                            if ApprovalCheck("Laura", 800, "L", TabM=1):
                                call LauraFace("sexy", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                ch_l "Mmmmmmm. . ."
                            elif ApprovalCheck("Laura", 700, "L", TabM=1):
                                call LauraFace("sexy", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2) 
                                ch_l "Hmm, that's nice. . ."
                            elif ApprovalCheck("Laura", 550, "L", TabM=1):
                                call LauraFace("surprised", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2) 
                                ch_l "I don't know about that."
                            elif ApprovalCheck("Laura", 300, "L", TabM=1):
                                call LauraFace("angry", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -8)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                                ch_l "Back it off, [newgirl[Laura].Petname]."
                            else: 
                                call LauraFace("angry", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -15)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 6)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3) 
                                ch_l "Fuck off."
                            
                    else:                   #If this is the first kiss
                            if ApprovalCheck("Laura", 800, "L", TabM=1):
                                call LauraFace("surprised", 2)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 95, 30)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 15)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 15)
                                call LauraFace("normal",Eyes="side")
                                ch_l ". . ."
                                call LauraFace("sexy",Eyes="side")
                                ch_l "Hmmm, that was nice. . ."
                                call LauraFace("sexy")
                            elif ApprovalCheck("Laura", 650, "L", TabM=1):
                                call LauraFace("surprised", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 25)            
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 20)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 15)
                                ch_l " ! "
                                ch_l "I'm not sure what to do with that. . ."
                            elif ApprovalCheck("Laura", 500, "L", TabM=1):
                                call LauraFace("surprised", 1)            
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 20)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 20)
                                ch_l "What are you thinking, [newgirl[Laura].Petname]?!"
                            elif ApprovalCheck("Laura", 800, TabM=1):
                                call LauraFace("angry", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -10) 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 30)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 20)
                                ch_l "What the hell, [newgirl[Laura].Petname]?!"
                            else: 
                                call LauraFace("angry", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -15) 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 40)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 25)
                                ch_l "Fuck off."
                            
                    $ newgirl["Laura"].Kissed += 1  
                    if "addict laura" in P_Traits:
                        $ newgirl["Laura"].Addict -= 1
                        $ newgirl["Laura"].Addictionrate += 1
                        $ newgirl["Laura"].Addictionrate = 3 if newgirl["Laura"].Addictionrate < 3 else newgirl["Laura"].Addictionrate 
                        
                    if ApprovalCheck("Laura", 700, TabM=1):
                        if newgirl["Laura"].Love > newgirl["Laura"].Obed and newgirl["Laura"].Love > newgirl["Laura"].Inbt:
                            ch_l "I think I'd like some more."
                        elif newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                            ch_l "Did you want to continue?"
                        else:
                            ch_l "We could keep going, [newgirl[Laura].Petname]."
                        menu:
                            "Keep kissing?"
                            "You know it.":
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 3)  
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, 3) 
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                                call Laura_SexAct("kissing")
                                call Trig_Reset(1)
                                return
                            "Not now [[no].":
                                call LauraFace("bemused", 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 4) 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                                ch_l "Ah, you were kidding."
                            "Nope.":
                                call LauraFace("sadside", 1)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -2) 
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 4)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                                ch_l "Ah, you were kidding."
                    else:
                        ch_l "Don't push me."
                    #End Kiss her
                
            "Hug her":                                                                                          #Hug her
                    if ApprovalCheck("Laura", 300, TabM=1):        
                        "You lean over and wrap Laura in a warm hug."
                    else:                
                        call LauraFace("angry", 1)
                        "You lean in with your arms wide, but Laura slips under you and takes a step back."
                        ch_l "What's was that, [newgirl[Laura].Petname]?" 
                        return
                        
                    if newgirl["Laura"].SEXP >= 30: 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 3) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 3)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2) 
                        call LauraFace("sexy")
                        ch_l "I think you're flipping my switch, [newgirl[Laura].Petname]."
                    elif ApprovalCheck("Laura", 800, "L", TabM=1):
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1) 
                        ch_l "Hmmmmm. . ."
                    elif ApprovalCheck("Laura", 550, TabM=1):
                        call LauraFace("surprised", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)        
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 2)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)  
                        ch_l "Um, [newgirl[Laura].Petname]? What is this?"
                    elif ApprovalCheck("Laura", 450, TabM=1):
                        call LauraFace("angry", 1)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)        
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
                        ch_l "This is making me uncomfortable. . ."
                    else: 
                        call LauraFace("angry", 1) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -4)       
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 4)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
                        ch_l "Hey, back off."   
                        
            "Slap her ass" if newgirl["Laura"].Loc == bg_current:                                                              #Slap her ass
                    call Laura_Slap_Ass
                
            "Pinch her ass":                                                                                    #Pinch her ass
                    call LauraFace("surprised", 1)
                    if newgirl["Laura"].SEXP >= 5 and ApprovalCheck("Laura", 700, TabM=1):        
                        "You come up to Laura from behind and quickly pinch her butt."
                    else:                
                        "You come up to Laura from behind and quickly pinch her butt."
                        call LauraFace("angry")
                        "She slaps your hand away and rounds on you."
                        ch_l "What are you thinking?" 
                        return
                        
                    if newgirl["Laura"].SEXP >= 40: 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 3) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)           
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
                        call LauraFace("sexy")
                        ch_l "Oooh! Getting rough?"
                    elif ApprovalCheck("Laura", 800, "L", TabM=1):
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)           
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2) 
                        ch_l "You like the way that feels, [newgirl[Laura].Petname]?"
                    elif ApprovalCheck("Laura", 1000, TabM=1):
                        call LauraFace("surprised")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)           
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2) 
                        ch_l "Wha?!"
                    elif ApprovalCheck("Laura", 800, TabM=1):
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -4)           
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 4)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 3)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1) 
                        ch_l "Hey!"
                    else: 
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -8)           
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 4)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
                        ch_l "Ouch! What the fuck?!"  
                    
                    
            "Grab her tit":                                                                                     #Grab her tit
                    call LauraFace("surprised", 1)
                    if newgirl["Laura"].SEXP >= 5 and ApprovalCheck("Laura", 700, TabM=2):        
                        "You come up to Laura and quickly honk her boob."
                    else:             
                        "You come up to Laura and quickly honk her boob."
                        call LauraFace("angry")
                        show Laura_Sprite
                        with vpunch
                        "She flips you onto your back."
                        ch_l "What the fuck?!" 
                        return
                        
                    if newgirl["Laura"].SEXP >= 40: 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2) 
                        call LauraFace("sexy")
                        ch_l "Hmm, that's pleasant."
                        $ Count = 10
                    elif ApprovalCheck("Laura", 850, "L", TabM=1):
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 2) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1) 
                        ch_l "Hmm, are you enjoying that as much as I am?"
                        $ Count = 7
                    elif ApprovalCheck("Laura", 1200, TabM=1):
                        call LauraFace("perplexed")  
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 1)         
                        ch_l "That's a bit inappropriate, [newgirl[Laura].Petname]."
                        $ Count = 5
                    elif ApprovalCheck("Laura", 900, TabM=1):
                        call LauraFace("angry",Eyes="down")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 4)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 1) 
                        ch_l "Are you going to move that hand or will I have to?"
                        call LauraFace("angry")
                        $ Count = 3
                    else: 
                        call LauraFace("angry")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -8)          
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 5)            
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2) 
                        $ newgirl["Laura"].Girl_Arms = 2
                        $ newgirl["Laura"].Claws = 1
                        ch_l "You wanna lose that hand?" 
                        $ Count = 2
                              
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3)            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
                    ch_l "Are you satisfied?"
                    while Count > 0:
                        if Count == 6:
                            call LauraFace("sexy", 1)
                            ch_l "That's pretty comforting. . ."  
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2)       
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                        elif Count == 3:
                            call LauraFace("perplexed")
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 1) 
                            ch_l "I like it, but maybe stop for now?"
                        elif Count == 2:
                            call LauraFace("angry")
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1) 
                            ch_l "Ok, that's enough now."
                        elif Count == 1:
                            call LauraFace("angry")
                            ch_l "Take a step back, [newgirl[Laura].Petname]!"
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5) 
                            show Laura_Sprite
                            with vpunch
                            "She gives you a quick shove."
                            $ Count = 1                     
                        $ Count -= 1 if Count >= 0 else 0
                            
                        if Count > 0:
                            menu:
                                "Your hand is still on her chest."
                                "Let go immediately":
                                    if Count >= 7:
                                        ch_l "I didn't really mind it. . ."  
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 2)         
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
                                    elif Count <= 4:
                                        ch_l "Probably for the best."
                                    $ Count = 0
                                    
                                "Honk it again and let go":
                                    if Count >= 7:
                                        ch_l "I didn't mind it so much. . ."          
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 4) 
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                                    elif Count >= 4:
                                        ch_l "Heh."
                                    else:
                                        call LauraFace("angry")
                                        ch_l "Asshole."
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)
                                    $ Count = 0 
                                        
                                "Fondle it a little":                            
                                    if newgirl["Laura"].FondleB and ApprovalCheck("Laura", 1100, TabM=2):                                
                                        call LauraFace("sexy",1)
                                        $ newgirl["Laura"].Eyes = "closed"
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
                                    else:
                                        call LauraFace("perplexed")
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2) 
                                        $ Count -= 1
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 4)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)
                                    ch_l "Hmm. . ."
                                    
                                "Just leave it there.":
                                    if Count == 5:
                                        call LauraFace("perplexed")
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 3) 
                                        ch_l "Huh."                            
                                    elif Count == 2:
                                        call LauraFace("perplexed")
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 1) 
                                        ch_l "This is getting uncomfortable."
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)            
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                                    
                            
                    $ newgirl["Laura"].Girl_Arms = 1
                    $ newgirl["Laura"].Claws = 0 
                    if newgirl["Laura"].FondleB and ApprovalCheck("Laura", 1200, TabM = 3): 
                        call LauraFace("sexy", 1)
                        ch_l "We could keep going. . ."
                        menu:
                            extend ""
                            "Yeah!":
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3) 
                                call Laura_SexAct("breasts")
                                call Trig_Reset(1)
                                return
                            "Nah, that was enough.":
                                call LauraFace("sad", 1)
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 2) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -2)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 4)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2) 
                                ch_l "Fine."
                    elif ApprovalCheck("Laura", 900, TabM = 3):  
                        $ newgirl["Laura"].Brows = "confused"
                        $ newgirl["Laura"].Eyes = "sexy"
                        $ newgirl["Laura"].Mouth = "smile"
                        ch_l "You enjoyed that?"
                    elif ApprovalCheck("Laura", 900): 
                        call LauraFace("angry", 1)
                        ch_l "You do that in public?"
                    else:
                        call LauraFace("angry", 1)
                        ch_l "Keep your hands to yourself!"
                        
                    
            "Rub her shoulders":                                                                                #Rub her shoulders
                    "You come up to Laura from behind and gently rub her shoulders."
                    if newgirl["Laura"].SEXP >= 30:
                        call LauraFace("sexy") 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 3) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                        "She sinks back into your hands"
                        ch_l "Hmm, are you thinking what I'm thinking, [newgirl[Laura].Petname]?"
                    elif ApprovalCheck("Laura", 650, "L"):
                        call LauraFace("sexy")
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 1) 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                        ch_l "Hmmm, that's nice, [newgirl[Laura].Petname]."
                    elif ApprovalCheck("Laura", 500):
                        call LauraFace("surprised", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                        ch_l "Oh, hey there, [newgirl[Laura].Petname]."
                    elif ApprovalCheck("Laura", 400):
                        call LauraFace("angry", 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)
                        if Taboo:
                            ch_l "Maybe take a step back, [newgirl[Laura].Petname]?"
                        else:
                            ch_l "Whoa, back it up."
                    else: 
                        call LauraFace("angry", 1)
                        "She slaps your hands away."
                        ch_l "No hands or you lose them."           
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
              
            "Ask for her panties":
                    call Laura_AskPanties
                                        
            "Never mind [[exit]":
                    $ newgirl["Laura"].Chat[5] = 0  
                    return
    else:
        "Laura isn't around."
            
    return



label Laura_AskPanties(Store = 0):
    $ Store = Tempmod  
    $ Line = 0
    if not newgirl["Laura"].Panties or newgirl["Laura"].Panties == "shorts":
        if ApprovalCheck("Laura", 900):
            call LauraFace("sexy", 1)
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 10)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 10) 
            ch_l "I'm not wearing any."
        elif newgirl["Laura"].Over == "towel" or not newgirl["Laura"].Legs:
            call LauraFace("bemused", 2)
            ch_l "Did you think I was wearing any?"            
        else:
            call LauraFace("bemused", 2, Eyes="side")
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 10)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)   
            ch_l "I'm not wearing any at the moment."         
       
    else:
        if newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 500): #You've seen her Pussy.
            $ Tempmod += 15
        elif newgirl["Laura"].SeenPanties and ApprovalCheck("Laura", 500): #You've seen her panties.
            $ Tempmod += 5 
        if "exhibitionist" in newgirl["Laura"].Traits:
            $ Tempmod += (Taboo * 5)
        if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames and not Taboo:
            $ Tempmod += 10
        if "no bottomless" in newgirl["Laura"].RecentActions: 
            $ Tempmod -= 20
        
        $ Line = 0
        if newgirl["Laura"].Legs == "pants" or HoseNum("Laura") >= 10: 
            if ApprovalCheck("Laura", 1000, "OI", TabM = 2) or "exhibitionist" in newgirl["Laura"].Traits:   
                $ Line = "here"
            elif ApprovalCheck("Laura", 900, TabM = 2):
                $ Line = "change"
                
        elif newgirl["Laura"].Legs == "skirt":
            if ApprovalCheck("Laura", 600, "OI", TabM = 2) or "exhibitionist" in newgirl["Laura"].Traits:   
                $ Line = "here"
            elif ApprovalCheck("Laura", 1100, TabM = 2):
                $ Line = "change"
                
        else:
            if ApprovalCheck("Laura", 1200, TabM = 2) or "exhibitionist" in newgirl["Laura"].Traits:
                $ Line = "here"
        
        
        if Line == "here":                              
                #She's agreed to change and will do it here
                call LauraFace("sly")                          
                if newgirl["Laura"].Legs == "skirt":      
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 4)            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 4)
                else: #no pants or skirt         
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 6)            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 6) 
                
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)    
                call Remove_Panties("Laura")
                    
                if Taboo:
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                    if "exhibitionist" in newgirl["Laura"].Traits: 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 5)
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5)    
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 10)            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 10)        
            
        elif Line:                                      
                    #She's agreed to change, but leaves the room to do it.       
                    call LauraFace("bemused", 1) 
                    menu:
                        ch_l "Could you turn around?"
                        "OK.": 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5) 
                            call LauraFace("smile", 1)                                             
                            ch_l "Thanks."
                            call LauraFace("sly", 1) 
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 2)         
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 4)            
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 4)
                            show blackscreen onlayer black 
                            "You turn around"   
                            $ newgirl["Laura"].DailyActions.append("pantyless")
                            call LauraOutfit                             
                            hide blackscreen onlayer black 
                            if Taboo:              
                                call Quick_Taboo("Laura")
                            "When you turn back, she quietly hands you her balled up panties."
                            $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck("Laura", 1000, "LI"): 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                                call LauraFace("sly", 1) 
                                ch_l "Oh, you'd like to watch?"
                            else:                 
                                call LauraFace("angry", 1) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -3)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                                ch_l "Yes."
                                $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck("Laura", 600, "OI"): 
                                call LauraFace("bemused", 1) 
                                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 10)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                                ch_l "Ok."
                                call LauraFace("sexy") 
                            else:        
                                call LauraFace("angry", 1) 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)          
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -5)            
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                                ch_l "I think that's rude under the circumstances."
                                $ Line = 0
                                
                    if Line:                                            #She agreed to stay  
                                call LauraFace("sly", 1) 
                                if newgirl["Laura"].Legs or HoseNum("Laura") >= 10:   
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5)         
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)            
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)  
                                        
                                call Remove_Panties("Laura") 
                                
        else:                                           #She refuses.    
            call LauraFace("angry", 2)                        
            if not ApprovalCheck("Laura", 500):
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10)          
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 3)            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3) 
                ch_l "Why do you think I would?"
                $ newgirl["Laura"].RecentActions.append("angry")
                $ newgirl["Laura"].DailyActions.append("angry")   
                
            elif not ApprovalCheck("Laura", 500, TabM = 5):
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 5) 
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5)          
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 5)            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5) 
                ch_l "In public?"                                
                $ newgirl["Laura"].RecentActions.append("angry")
                $ newgirl["Laura"].DailyActions.append("angry")   
                
            else:
                call LauraFace("bemused", 2)
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 3)            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                if Taboo:            
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                    
                if newgirl["Laura"].Love >= newgirl["Laura"].Inbt or newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                    ch_l "Maybe someday, [newgirl[Laura].Petname]."
                else:
                    call LauraFace("perplexed")       
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, -2)    
                    ch_l "Why would you want that?"
            $ newgirl["Laura"].Blush = 0
                
    $ Tempmod = Store       
    $ Line = 0
    return

    # End Ask for Panties   //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //


# Laura Control interface ///////////////////
label Laura_Controls:
    menu:
        "I'd like you to call me something else":
            call Laura_Names            
            return
        "I'd like you to come over for some action." if newgirl["Laura"].Loc != bg_current:
            ch_l "Ok, I'll be right over."
            $ newgirl["Laura"].Loc = bg_current 
            call Set_The_Scene
            call Laura_SexMenu
            return
        "I'd like to get busy." if newgirl["Laura"].Loc == bg_current:
            ch_l "How do you mean?"
            call Laura_SexMenu
            return
        "I want you to stop taking your own initiative." if "sub" not in newgirl["Laura"].Traits:
            $ newgirl["Laura"].Traits.append("sub")
            ch_l "Ok."                
        "Exit.":
            return
    jump Laura_Controls
return

# start Laura_Gifts//////////////////////////////////////////////////////////
label Laura_Gifts:  
    if P_Inventory == []:
        "You don't have anything to give her."
        return
    menu:
        "What would you like to give her?"
        "Give her a dildo." if "dildo" in P_Inventory: 
            #If you have a Dildo, you'll give it.
            $ Count = newgirl["Laura"].Inventory.count("dildo")
            if "dildo" not in newgirl["Laura"].Inventory:                            
                "You give Laura the dildo."
                $ newgirl["Laura"].Blush = 1
                $ newgirl["Laura"].Girl_Arms = 2
                $ newgirl["Laura"].Held = "dildo"
                if ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "I"):                    
                    call LauraFace("smile")
                    $ P_Inventory.remove("dildo")
                    $ newgirl["Laura"].Inventory.append("dildo")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 30)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 30)
                    ch_l "Oh, cool, I've wanted one of these. . ."
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                elif ApprovalCheck("Laura", 800) or ApprovalCheck("Laura", 300, "I"):
                    call LauraFace("confused")
                    $ P_Inventory.remove("dildo")
                    $ newgirl["Laura"].Inventory.append("dildo")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 10)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
                    ch_l "Huh, you're a weird gift giver."  
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 5)
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                    call LauraFace("smile")
                    ch_l "It's very thoughtful though."
                elif "offered gift" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry")
                    "She hands it back to you."
                    ch_l "I said I can't take something like this."     
                else:
                    call LauraFace("angry")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 20)                    
                    ch_l "I don't think you should just be handing these out to random chicks."                     
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                    "She hands it back to you."
                    $ newgirl["Laura"].DailyActions.append("offered gift") 
            elif Count == 1:
                ch_l "I don't know if I need another. . ."
            else: 
                ch_l "I'm running out of space at this point."
            $ newgirl["Laura"].Held = 0
            $ newgirl["Laura"].Girl_Arms = 1
            
            
        "Give her the vibrator." if "vibrator" in P_Inventory: 
            #If you have a vibrator, you'll give it.
            if "vibrator" not in newgirl["Laura"].Inventory:                            
                "You give Laura the Shocker Vibrator."
                $ newgirl["Laura"].Blush = 1
                $ newgirl["Laura"].Girl_Arms = 2
                $ newgirl["Laura"].Held = "vibrator"
                if ApprovalCheck("Laura", 700):                    
                    call LauraFace("confused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl["Laura"].Inventory.append("vibrator")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 30)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 30)
                    ch_l "This is. . . [[bzzzt]- "                  
                    call LauraFace("sly")
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                    ch_l "-some kind of sex thing, huh. . ."
                elif ApprovalCheck("Laura", 400):
                    call LauraFace("confused")
                    $ P_Inventory.remove("vibrator")
                    $ newgirl["Laura"].Inventory.append("vibrator")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 10)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)
                    ch_l "This is. . . [[bzzzt]- "                  
                    call LauraFace("sly")
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                    ch_l "-oooh. . ."
                elif "offered gift" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry")
                    "She hands it back to you."
                    ch_l "I don't want it."  
                else:
                    call LauraFace("angry")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 20)                    
                    ch_l "I don't need it."                     
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 5)
                    "She hands it back to you."
                    $ newgirl["Laura"].DailyActions.append("offered gift") 
            else: 
                ch_l "I already have one of these."
            $ newgirl["Laura"].Held = 0
            $ newgirl["Laura"].Girl_Arms = 1
            
            
        "Give her the corset." if "l corset" in P_Inventory: 
            #If you have a bra, you'll give it.
            if "corset" not in newgirl["Laura"].Inventory:                            
                "You give Laura the corset."
                if ApprovalCheck("Laura", 1100):                    
                    call LauraFace("bemused")
                    $ P_Inventory.remove("l corset")
                    $ newgirl["Laura"].Inventory.append("corset")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 25)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 20)
                    ch_l "You think this'd look good on me?"
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                elif ApprovalCheck("Laura", 700):
                    call LauraFace("confused",1)
                    $ P_Inventory.remove("l corset")
                    $ newgirl["Laura"].Inventory.append("corset")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 15)
                    ch_l "This is. . . kinda flimsy. . ."                    
                    call LauraFace("bemused",1)
                elif ApprovalCheck("Laura", 600):
                    call LauraFace("confused",2)
                    $ P_Inventory.remove("l corset")
                    $ newgirl["Laura"].Inventory.append("corset")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 20)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 25)
                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                    call LauraFace("bemused",1)
                elif "no gift bra" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry",2)
                    ch_l "I just told you no."   
                else:
                    call LauraFace("angry",2)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -10)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 20)  
                    if "no gift panties" in newgirl["Laura"].DailyActions:                    
                        ch_l "I don't want these either."                       
                    else:                   
                        ch_l "You have too much time on your hands."                     
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 5)
                    $ newgirl["Laura"].Blush = 1
                    "She hands it back to you."
                    $ newgirl["Laura"].RecentActions.append("no gift bra")                      
                    $ newgirl["Laura"].DailyActions.append("no gift bra") 
            else: 
                ch_l "I already have one of those."                
            
        "Give her the lace panties." if "l lace panties" in P_Inventory: 
            #If you have a bra, you'll give it.
            if "lace panties" not in newgirl["Laura"].Inventory:                            
                "You give Laura the lace panties."
                $ newgirl["Laura"].Blush = 1
                if ApprovalCheck("Laura", 1200):                    
                    call LauraFace("bemused")
                    $ P_Inventory.remove("l lace panties")
                    $ newgirl["Laura"].Inventory.append("lace panties")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 30)
                    ch_l "These are pretty hot. . ."
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                elif ApprovalCheck("Laura", 900):
                    call LauraFace("confused",1)
                    $ P_Inventory.remove("l lace panties")
                    $ newgirl["Laura"].Inventory.append("lace panties")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 25)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 20)
                    ch_l "These are kinda flimsy. . ."                  
                    call LauraFace("bemused",1)
                elif ApprovalCheck("Laura", 700):
                    call LauraFace("confused",2)
                    $ P_Inventory.remove("l lace panties")
                    $ newgirl["Laura"].Inventory.append("lace panties")
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 20)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 25)
                    ch_l "I don't think I'd wear these. . ."                  
                    call LauraFace("bemused",1)
                    ch_l "But I might need to do laundry. . ." 
                elif "no gift panties" in newgirl["Laura"].DailyActions:
                    call LauraFace("angry",2)
                    ch_l "My answer's still no, stop asking!"                      
                else:
                    call LauraFace("angry",2)
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -15)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 20)
                    if "no gift bra" in newgirl["Laura"].DailyActions:                    
                        ch_l "I don't want these either!" 
                    elif newgirl["Laura"].SeenPanties:
                        ch_l "Did you not like the ones I had?"                          
                    else:
                        ch_l "You don't need to worry about my underwear."                     
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 5)
                    $ newgirl["Laura"].Blush = 1
                    "She hands them back to you."
                    $ newgirl["Laura"].RecentActions.append("no gift panties")                      
                    $ newgirl["Laura"].DailyActions.append("no gift panties") 
            else: 
                ch_l "I already have one of those."                
            
            
        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in P_Inventory: 
            #If you have a vibrator, you'll give it.
            if "Dazzler and Longshot" not in newgirl["Laura"].Inventory:                            
                "You give Laura the book."
                $ newgirl["Laura"].Blush = 1
                if ApprovalCheck("Laura", 600, "L"):                    
                    call LauraFace("smile")
                    ch_l "A love story?"
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                else:
                    call LauraFace("confused")
                    ch_l "Huh. Is there a movie?"  
                    call LauraFace("bemused")       
                $ P_Inventory.remove("Dazzler and Longshot")
                $ newgirl["Laura"].Inventory.append("Dazzler and Longshot") 
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 50) 
            else: 
                ch_l "I already have one of those."                
            
        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in P_Inventory: 
            #If you have a book, you'll give it.
            if "256 Shades of Grey" not in newgirl["Laura"].Inventory:                            
                "You give Laura the book."
                $ newgirl["Laura"].Blush = 1
                if ApprovalCheck("Laura", 500, "O"):                    
                    call LauraFace("bemused")
                    ch_l "Looks dirty."
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                else:
                    call LauraFace("confused") 
                    ch_l "I'll give it a look."  
                    call LauraFace("bemused")             
                $ P_Inventory.remove("256 Shades of Grey")
                $ newgirl["Laura"].Inventory.append("256 Shades of Grey")                    
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 50)  
            else: 
                ch_l "I already have one of those."                
            
        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in P_Inventory: 
            #If you have a book, you'll give it.
            if "Avengers Tower Penthouse" not in newgirl["Laura"].Inventory:                            
                "You give Laura the book."
                $ newgirl["Laura"].Blush = 1
                if ApprovalCheck("Laura", 500, "I"):                    
                    call LauraFace("bemused")
                    ch_l "This is pretty hot. . ."
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10)
                else:
                    call LauraFace("confused")
                    ch_l "Huh. . . ok."  
                    call LauraFace("bemused")               
                $ P_Inventory.remove("Avengers Tower Penthouse")
                $ newgirl["Laura"].Inventory.append("Avengers Tower Penthouse")                    
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 50)  
            else: 
                ch_l "I already have one of those."                
            

        "Exit":
            pass
    
    return


# start Laura_Names//////////////////////////////////////////////////////////
label Laura_Names:    
    menu:
        ch_l "Oh? What would you like me to call you?"
        "My initial's fine.":            
            $ newgirl["Laura"].Petname = Playername[:1]  #fix test this
            ch_l "You got it, [newgirl[Laura].Petname]."
        "Call me by my name.":
            $ newgirl["Laura"].Petname = Playername            
            ch_l "If you'd rather, [newgirl[Laura].Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "boyfriend"
            ch_l "Sure thing, [newgirl[Laura].Petname]."
        "Call me \"lover\"." if "lover" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "lover"
            ch_l "Oooh, love to, [newgirl[Laura].Petname]."
        "Call me \"sir\"." if "sir" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "sir"
            ch_l "Yes, [newgirl[Laura].Petname]."
        "Call me \"master\"." if "master" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "master"
            ch_l "As you wish, [newgirl[Laura].Petname]."
        "Call me \"sex friend\"." if "sex friend" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "sex friend"
            ch_l "Heh, very cheeky, [newgirl[Laura].Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "fuck buddy"
            ch_l "I'm game if you are, [newgirl[Laura].Petname]."        
        "Call me \"daddy\"." if "daddy" in newgirl["Laura"].Petnames:
            $ newgirl["Laura"].Petname = "daddy"
            ch_l "Oh! You bet, [newgirl[Laura].Petname]."        
        "Bub works.":
            $ newgirl["Laura"].Petname = "bub"
            ch_l "You got it, bub."
        "Nevermind.":
            return
    return
# end Laura_Names//////////////////////////////////////////////////////////

label Laura_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Laura.":
                        $ newgirl["Laura"].Pet = "Laura"            
                        ch_l "I don't see why not, [newgirl[Laura].Petname]."
                        
                    "I think I'll just call you X-23.":
                        $ newgirl["Laura"].Pet = "X-23"            
                        if ApprovalCheck("Laura", 700, "L") and not ApprovalCheck("Laura", 500, "O"):
                                ch_l "Oh, if you say so, [newgirl[Laura].Petname]."
                        else:
                                ch_l "I don't see why not, [newgirl[Laura].Petname]."
                        
                    "I think I'll call you \"girl\".":
                        $ newgirl["Laura"].Pet = "girl"
                        if "boyfriend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 600, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I'm totally your girl, [newgirl[Laura].Petname]."
                        else:      
                            call LauraFace("angry")           
                            ch_l "I'm NOT your girl, [newgirl[Laura].Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ newgirl["Laura"].Pet = "boo"
                        if "boyfriend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 700, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I am your boo, [newgirl[Laura].Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I'm NOT your boo,  [newgirl[Laura].Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ newgirl["Laura"].Pet = "bae"
                        if "boyfriend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 600, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "I am your bae, [newgirl[Laura].Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I'm NOT your bae,  [newgirl[Laura].Petname]."
                            
                    "I think I'll call you \"baby\".":
                        $ newgirl["Laura"].Pet = "baby"
                        if "boyfriend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 500, "L"):
                            call LauraFace("sexy", 1) 
                            ch_l "Cute, [newgirl[Laura].Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "I am not a baby." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ newgirl["Laura"].Pet = "sweetie"
                        if "boyfriend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 600, "L"):
                            ch_l "Aw, that's sweet, [newgirl[Laura].Petname]."
                        else:     
                            call LauraFace("angry", 1)            
                            ch_l "Too sweet, [newgirl[Laura].Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ newgirl["Laura"].Pet = "sexy"
                        if "lover" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 800):
                            call LauraFace("sexy", 1) 
                            ch_l "You know it, [newgirl[Laura].Petname]."
                        else:        
                            call LauraFace("angry", 1)         
                            ch_l "Pushing a line there, [newgirl[Laura].Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ newgirl["Laura"].Pet = "lover"
                        if "lover" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 1200):
                            call LauraFace("sexy", 1) 
                            ch_l "I know."
                        else:      
                            call LauraFace("angry", 1)           
                            ch_l "I don't think so, [newgirl[Laura].Petname]."  
                    
                    "I think I'll call you \"Wolvie\".":
                        $ newgirl["Laura"].Pet = "Wolvie"
                        if ApprovalCheck("Laura", 500, "I"):
                            call LauraFace("sexy", 1) 
                            ch_l "Heh, ok, [newgirl[Laura].Petname]."
                        else:     
                            call LauraFace("angry")            
                            ch_l "Not really that cute, [newgirl[Laura].Petname]" 
                        
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ newgirl["Laura"].Pet = "slave"
                        if "master" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 800, "O"):
                            call LauraFace("bemused", 1) 
                            ch_l "As you wish, [newgirl[Laura].Petname]."
                        else:      
                            call LauraFace("angry", 1)           
                            ch_l "I am not your slave, [newgirl[Laura].Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ newgirl["Laura"].Pet = "pet"
                        if "master" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 650, "O"):
                            call LauraFace("bemused", 1) 
                            ch_l "You can pet me if you want, [newgirl[Laura].Petname]."
                        else:             
                            call LauraFace("angry", 1)    
                            ch_l "I am no one's pet, [newgirl[Laura].Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ newgirl["Laura"].Pet = "slut"
                        if "sex friend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 900, "OI"):
                            call LauraFace("sexy") 
                            ch_l "Fair enough."
                        else:                
                            call LauraFace("angry", 1) 
                            $ newgirl["Laura"].Mouth = "surprised"
                            ch_l "I'm like to see you try it with a busted jaw." 
                            
                    "I think I'll call you \"whore\".":
                        $ newgirl["Laura"].Pet = "whore"
                        if "fuckbuddy" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 1000, "OI"):
                            call LauraFace("sly") 
                            ch_l "I mean. . ."
                        else:        
                            call LauraFace("angry", 1)         
                            ch_l "If either of us is going to be turning tricks. . ." 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ newgirl["Laura"].Pet = "sugartits"
                        if "sex friend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 1400):
                            call LauraFace("sly", 1) 
                            ch_l "That doesn't even make sense."
                        else:     
                            call LauraFace("angry", 1)            
                            ch_l "Not cool." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ newgirl["Laura"].Pet = "sex friend"
                        if "sex friend" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 600, "I"):
                            call LauraFace("sly") 
                            ch_l "Yeah. . ."
                        else:                
                            call LauraFace("angry", 1) 
                            ch_l "Keep it down, [newgirl[Laura].Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ newgirl["Laura"].Pet = "fuckbuddy"
                        if "fuckbuddy" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 700, "I"):
                            call LauraFace("sly") 
                            ch_l "Yup."
                        else:                
                            call LauraFace("angry", 1)
                            $ newgirl["Laura"].Mouth = "surprised"
                            ch_l "Don't even joke, [newgirl[Laura].Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ newgirl["Laura"].Pet = "baby girl"
                        if "daddy" in newgirl["Laura"].Petnames or ApprovalCheck("Laura", 1200):
                            call LauraFace("smile", 1) 
                            ch_l "I guess?"
                        else:                
                            call LauraFace("angry", 1) 
                            ch_l "Weirdo." 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
label Laura_Namecheck(L_Pet = newgirl["Laura"].Pet, Cnt = 0, Ugh = 0):
    #L_Pet is the internal pet name, Cnt and Ugh are internal count variable
    if L_Pet == "Laura":
        return Ugh   
    if Taboo:
        $ Cnt = int(Taboo/10)
    if L_Pet == "girl":                                         #easy options
        if ApprovalCheck("Laura", 600, "L", TabM=1):            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1)
            $ Ugh = 1
    elif L_Pet == "boo" or L_Pet == "bae":
        if ApprovalCheck("Laura", 600, "L", TabM=1):
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
            $ Ugh = 1
    elif L_Pet == "baby":    
        if ApprovalCheck("Laura", 500, "L", TabM=1):
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 30, -1)
            $ Ugh = 1
    elif L_Pet == "Wolvie":
        if ApprovalCheck("Laura", 500, "I", TabM=1):
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1)
            $ Ugh = 1
    elif L_Pet == "sweetie":
        if not ApprovalCheck("Laura", 600, "L", TabM=1):
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)  
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -1)
            $ Ugh = 1
            
    elif L_Pet == "sexy":
        if ApprovalCheck("Laura", 800, TabM=1):                                                        #over 150
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
        else:                                                            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1            
    elif L_Pet == "lover":
        if ApprovalCheck("Laura", 1200, TabM=1):                                                        #over 150
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
        else:                                                            
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
    #tougher options
    elif L_Pet == "X-23":   
        if ApprovalCheck("Laura", 800, "O"):
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 3) 
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)  
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, 2)                                   
        elif ApprovalCheck("Laura", 700, "L") and not ApprovalCheck("Laura", 500, "O"):
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -1)
            $ Ugh = 1
        else:
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, 1)
            
    elif L_Pet == "slave":                             
        if ApprovalCheck("Laura", 800, "O", TabM=3):                                            #over 80
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, (3+Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, (2+Cnt))
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)  
        elif ApprovalCheck("Laura", 500, "O", TabM=3):                                                  #between 50 and 80
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 81, 2)     
        else:                                                                                           # under 50
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -1)
            $ Ugh = 1
    
    elif L_Pet == "pet":                                        #tougher options
        if ApprovalCheck("Laura", 800, "O", TabM=2):
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, (3+Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, (2+Cnt))
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)     
        elif ApprovalCheck("Laura", 650, "O", TabM=2):
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 81, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)        
        else:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -1)
            $ Ugh = 1
            
    elif L_Pet == "slut":
        if ApprovalCheck("Laura", 500, "O", TabM=2) or ApprovalCheck("Laura", 400, "I", TabM=2):        #over 50
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, (4+Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, (2+Cnt))
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1)
        elif ApprovalCheck("Laura", 300, "O", TabM=2) or ApprovalCheck("Laura", 200, "I", TabM=2):      #between 30 and 50
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, (2+Cnt))
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)        
        else:                                                                                           # under 40
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-2-Cnt))
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt), 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "whore":
        if ApprovalCheck("Laura", 500, "O", TabM=2) or ApprovalCheck("Laura", 500, "I", TabM=2):        #over 60
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 4)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1)
        elif ApprovalCheck("Laura", 400, "O", TabM=2) or ApprovalCheck("Laura", 400, "I", TabM=2):      #between 40 and 60
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 1)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-2-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
        else:                                                                                           # under 40
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-3-Cnt))
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-2-Cnt), 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 21, 1, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "sugartits":
        if ApprovalCheck("Laura", 1500, TabM=1):                                                        #over 150
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
        else:                                                                       
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-2-Cnt))
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "sex friend":    
        if ApprovalCheck("Laura", 750, "O", TabM=1) or ApprovalCheck("Laura", 600, "I", TabM=1):        #over 75/60
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 3)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1)
        elif ApprovalCheck("Laura", 600, "O", TabM=1) or ApprovalCheck("Laura", 400, "I", TabM=1):      #between 60/40 and 75/60
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
            $ newgirl["Laura"].Blush = 1
        else:                                                                                           # under 60/40
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -Cnt)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt), 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "fuckbuddy":
        if ApprovalCheck("Laura", 700, "O", TabM=2) or ApprovalCheck("Laura", 700, "I", TabM=1):        #over 70/70
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 3)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 95, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 85, 1)
        elif ApprovalCheck("Laura", 600, "O", TabM=2) or ApprovalCheck("Laura", 500, "I", TabM=1):      #between 60/50 and 70/70
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
            $ newgirl["Laura"].Blush = 1
        else:                                                                                           #under 60/50
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -Cnt)
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, (-2-Cnt), 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    elif L_Pet == "baby girl":
        if ApprovalCheck("Laura", 1200, TabM=1):                                                        #over 150
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)            
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
        else:                                                                       
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, (-2-Cnt))
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, (-1-Cnt))
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, -1)
            $ Ugh = 1
            
    return Ugh


# start Laura_Personality//////////////////////////////////////////////////////////
label Laura_Personality(Cnt = 0):   
    if not newgirl["Laura"].Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Laura to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_l "Yeah? What's up?"
        "More Obedient. [[Love to Obedience]" if newgirl["Laura"].Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_l "If you really care about that, sure."
            $ newgirl["Laura"].Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if newgirl["Laura"].Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_l "I could always be a bit more wild if that's what you want."
            $ newgirl["Laura"].Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if newgirl["Laura"].Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_l "I guess I could go all-out."
            $ newgirl["Laura"].Chat[4] = 3
        "More Loving. [[Obedience to Love]" if newgirl["Laura"].Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_l "I can try."
            $ newgirl["Laura"].Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if newgirl["Laura"].Inbt > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_l "I can give it a shot. . ."
            $ newgirl["Laura"].Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if newgirl["Laura"].Inbt > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_l "If that's somethign you need out of this. . ."
            $ newgirl["Laura"].Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if newgirl["Laura"].Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_l "Um, ok."
            $ newgirl["Laura"].Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Laura_Personality
        "Nevermind.":
            return
    return
# end Laura_Personality//////////////////////////////////////////////////////////




# Laura_Summon//////////////////////////////////////////////////////////

label Laura_Summon(Tempmod=Tempmod):
    call LauraOutfit  
    if "no summon" in newgirl["Laura"].RecentActions:
                if "angry" in newgirl["Laura"].RecentActions:
                    ch_l "Grrrrrrrrr."
                elif Action_Check("Laura", "recent", "no summon") > 1:
                    ch_l "Back off!"
                    $ newgirl["Laura"].RecentActions.append("angry") 
#                elif Current_Time == "Night": 
#                    ch_l "Like I said, it's too late for that."
                else:
                    ch_l "Like I said, I'm busy."   
                $ newgirl["Laura"].RecentActions.append("no summon")
                return
                              
    if Current_Time == "Night": 
                if ApprovalCheck("Laura", 500, "L") or ApprovalCheck("Laura", 400, "O"):                              #It's night time but she likes you.
                        ch_l "You're up too? Sure, we can hang."
                        $ newgirl["Laura"].Loc = bg_current 
                        call Set_The_Scene
                else:                                                           #It's night time and she isn't into you
                        ch_l "Nah."       
                        $ newgirl["Laura"].RecentActions.append("no summon")         
                return
                
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if newgirl["Laura"].Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif newgirl["Laura"].Loc == "bg dangerroom":    
        $ Tempmod = 10
    elif newgirl["Laura"].Loc == "bg showerroom":    
        $ Tempmod = 30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    elif not ApprovalCheck("Laura", 700, "L") or not ApprovalCheck("Laura", 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck("Laura", 300):
                ch_l "I'm busy, [newgirl[Laura].Petname]."       
                $ newgirl["Laura"].RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in newgirl["Laura"].RecentActions:
                pass
        elif "goto" in newgirl["Laura"].RecentActions:
                ch_l "You were just over here."
        elif newgirl["Laura"].Loc == "bg classroom":
                ch_l "I'm in class, did you want to come too?"
        elif newgirl["Laura"].Loc == "bg dangerroom": 
                ch_l "I'm in the Danger Room, [newgirl[Laura].Petname], want in?"    
        elif newgirl["Laura"].Loc == "bg campus": 
                ch_l "I'm napping under a tree here, want to come?" 
        elif newgirl["Laura"].Loc == "bg laura": 
                ch_l "I'm in my room, [newgirl[Laura].Petname], want to hang?" 
        elif newgirl["Laura"].Loc == "bg player": 
                ch_l "I'm in your room, [newgirl[Laura].Petname], why aren't you?"   
        elif newgirl["Laura"].Loc == "bg showerroom":    
            if ApprovalCheck("Laura", 1600):
                ch_l "I'm in the shower right now. Join me?"
            else:            
                ch_l "I'm in the shower right now, [newgirl[Laura].Petname]. We can connect later."       
                $ newgirl["Laura"].RecentActions.append("no summon")         
                return      
        elif newgirl["Laura"].Loc == "hold":
                ch_l "I'm on task right now. Sorry?"       
                $ newgirl["Laura"].RecentActions.append("no summon") 
                return      
        else:        
                ch_l "Why don't you come to me?"    
           
           
        if "summoned" in newgirl["Laura"].RecentActions:
            ch_l "Again? Ok, fine."           
            $ Line = "yes"            
        elif "goto" in newgirl["Laura"].RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_l "See you when you get here."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_l "If you say so."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck("Laura", 600, "L") or ApprovalCheck("Laura", 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck("Laura", 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck("Laura", 1400):                         
                                #she is generally favorable 
                                ch_l "Hmph."              
                                $ Line = "yes"                        
                        elif ApprovalCheck("Laura", 200, "O"):                                  
                                #she is not obedient  
                                ch_l "Whatever."    
                                ch_l "I'll be here if you change your mind."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 55, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                    ch_l "See you when you get here."
                    $ Line = "go to"
                    
                "Nah, we can talk later.":
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                            
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                    ch_l "Ok. Later then."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck("Laura", 650, "L") or ApprovalCheck("Laura", 1500):
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)                   
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                        $ Line = "no"
                        ch_l "Man, you are such a sap."
                        
                "Come on, it'll be fun.":
                    if ApprovalCheck("Laura", 400, "L") and ApprovalCheck("Laura", 800):
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)                   
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                        $ Line = "fun"
                    else: 
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck("Laura", 600, "O"):                              
                        #she is obedient
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, 1, 1)    
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -1)                
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck("Laura", 1500):       
                        #she is generally favorable
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)  
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)                                
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)  
                        ch_l "Ok, fine."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck("Laura", 200, "O"):                                         
                        #she is not obedient   
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -4)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -3)   
                        ch_l "Don't even try it."                             
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)    
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -3)
                        ch_l "I'm staying put."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)                                    
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1, 1)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if newgirl["Laura"].Love > newgirl["Laura"].Obed:
            ch_l "Sure!"
        else:
            ch_l "Ok, I'm in route."
        $ Line = "yes" 
        
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ newgirl["Laura"].RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl["Laura"].Loc == "bg classroom":
                ch_l "I can't skip this lecture." 
            elif newgirl["Laura"].Loc == "bg dangerroom": 
                ch_l "I'm just getting warmed up though!"
            else:
                ch_l "Sorry, [newgirl[Laura].Petname], I'm kinda busy."          
            $ newgirl["Laura"].RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ newgirl["Laura"].RecentActions.append("goto")  
            $ P_RecentActions.append("goto")  
            if newgirl["Laura"].Loc == "bg classroom":
                    ch_l "K, there's room next to me."
                    jump Class_Room 
            elif newgirl["Laura"].Loc == "bg dangerroom": 
                    ch_l "I'll try to leave some bots for 'ya."
                    jump Danger_Room
            elif newgirl["Laura"].Loc == "bg laura":    
                    ch_l "I'll. . . make some space."
                    
                    
                    ch_l "Never mind, it's too much, I'll meet you in your room." 
                    $ newgirl["Laura"].Loc = "bg player"
                    jump Player_Room  
                    
                    jump Laura_Room
            elif newgirl["Laura"].Loc == "bg player": 
                    ch_l "I'll be waiting."
                    jump Player_Room                
            elif newgirl["Laura"].Loc == "bg showerroom": 
                    ch_l "I'll leave you some hot water."
                    jump Shower_Room
            elif newgirl["Laura"].Loc == "bg campus": 
                    ch_l "Look for the biggest tree."
                    jump Campus
            else:
                    ch_l "Um, I'll just meet you in my room."
                    
                    
                    ch_l "Never mind, it's too much of a mess, I'll meet you in your room." 
                    $ newgirl["Laura"].Loc = "bg player"
                    jump Player_Room  
                    
                    $ newgirl["Laura"].Loc = "bg laura"
                    jump Laura_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_l "You are such a dork!"
    elif Line == "command": 
            ch_l "Yes, [newgirl[Laura].Petname]."
        
    $ newgirl["Laura"].RecentActions.append("summoned")  
    $ Line = 0
    ch_l "I'll be right there."      
    if "locked" in P_RecentActions:
            call Locked_Door("Laura")
            return                          
    $ newgirl["Laura"].Loc = bg_current 
    call LauraOutfit
    call Set_The_Scene
    return

# End Laura Summon ///////////////////    


label Laura_Leave(Tempmod=Tempmod, GirlsNum = 0):        
    if "leaving" in newgirl["Laura"].RecentActions:
        call DrainWord("Laura","leaving")
    else:
        return
    
    if newgirl["Laura"].Loc == "hold":   
            # Activates if she's being moved out of play
            ch_l "I'm taking off for a bit, later." 
            return
            
    if "Laura" in Party or "lockedtravels" in newgirl["Laura"].Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ newgirl["Laura"].Loc = bg_current 
            return
      
    elif "freetravels" in newgirl["Laura"].Traits or not ApprovalCheck("Laura", 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            call LauraOutfit           
            if GirlsNum: #if someone left before her
                        ch_l "Yeah, I'm leaving too."
                        
            if newgirl["Laura"].Loc == "bg classroom":
                        ch_l "I've got class."
            elif newgirl["Laura"].Loc == "bg dangerroom": 
                        ch_l "I'm hitting the Danger Room."   
            elif newgirl["Laura"].Loc == "bg campus": 
                        ch_l "I'm taking a nap in the quad." 
            elif newgirl["Laura"].Loc == "bg laura": 
                        ch_l "I'm headed back to my room." 
            elif newgirl["Laura"].Loc == "bg player": 
                        ch_l "I'm gonna hang out in your room for a bit."   
            elif newgirl["Laura"].Loc == "bg showerroom":    
                if ApprovalCheck("Laura", 1400):
                        ch_l "I'm hitting the showers, later."
                else:            
                        ch_l "I'm headed out."
            else:        
                        ch_l "I'm headed out, later."                  
            hide Laura_Sprite
            return     
            #End Free Travels
    
    call LauraOutfit  
    
    if "follow" not in newgirl["Laura"].Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ newgirl["Laura"].Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if newgirl["Laura"].Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif newgirl["Laura"].Loc == "bg dangerroom":    
        $ Tempmod = 20
    elif newgirl["Laura"].Loc == "bg showerroom":    
        $ Tempmod = 40
    
    
    if GirlsNum: #if someone left before her
                ch_l "Yeah, I'm headed out too."
                
    if newgirl["Laura"].Loc == "bg classroom":
        ch_l "I've got class, want in?"
    elif newgirl["Laura"].Loc == "bg dangerroom": 
        ch_l "I've got some Danger Room time, want in?"    
    elif newgirl["Laura"].Loc == "bg campus": 
        ch_l "I'm taking a nap on the quad, you want in?" 
    elif newgirl["Laura"].Loc == "bg laura": 
        ch_l "I'm headed back to my room, you want in?" 
    elif newgirl["Laura"].Loc == "bg player": 
        ch_l "I'm going to hang out in your room for a bit, you coming?"   
    elif newgirl["Laura"].Loc == "bg showerroom":    
        if ApprovalCheck("Laura", 1600):
            ch_l "I'm hitting the showers, you could use one too."
        else:            
            ch_l "I'm hitting the showers, see you later."
            return        
    else:        
        ch_l "Wanna join me?"    
    
    
    menu:
        extend ""
        "Sure, I'll catch up.":
                if "followed" not in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 55, 1) 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                $ Line = "go to"
            
        "Nah, we can talk later.":
                if "followed" not in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)                            
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                ch_l "Sure, whatever."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck("Laura", 650, "L") or ApprovalCheck("Laura", 1500):                
                    if "followed" not in newgirl["Laura"].RecentActions:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)                   
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in newgirl["Laura"].RecentActions:
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                    $ Line = "no"
                    ch_l "Man, you are such a sap."
                
        "Come on, it'll be fun.":
                if ApprovalCheck("Laura", 400, "L") and ApprovalCheck("Laura", 800):
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)                   
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                    $ Line = "fun"
                else: 
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                    $ Line = "no"
                        
        "No, stay here.":
                if ApprovalCheck("Laura", 600, "O"):                              
                    #she is obedient
                    if "followed" not in newgirl["Laura"].RecentActions: 
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 40, -2)                
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck("Laura", 1400):       
                    #she is generally favorable
                    if "followed" not in newgirl["Laura"].RecentActions:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -1)  
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)                                
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)  
                    ch_l "I guess if you need me here."              
                    $ Line = "yes"
                    
                elif ApprovalCheck("Laura", 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in newgirl["Laura"].RecentActions:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -4)  
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -2)   
                    ch_l "Don't tell me what to do."  
                    if "followed" not in newgirl["Laura"].RecentActions:                       
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)    
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -2)
                    ch_l "I'm out of here."                    
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in newgirl["Laura"].RecentActions:
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)                                    
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1, 1)                               
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -2)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    $ newgirl["Laura"].RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            if newgirl["Laura"].Loc == "bg classroom":
                ch_l "I really can't miss this one." 
            elif newgirl["Laura"].Loc == "bg dangerroom": 
                ch_l "Sorry [newgirl[Laura].Petname], but I'm going a little stir crazy."
            else:
                ch_l "Sorry, I have stuff to do."         
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            call DrainWord("All","leaving")  
            call DrainWord("All","arriving")        
            hide Laura_Sprite
            call Gym_Clothes("auto", "Laura")
            if newgirl["Laura"].Loc == "bg classroom":
                ch_l "Ok, get a move on then."            
                jump Class_Room_Entry
            elif newgirl["Laura"].Loc == "bg dangerroom": 
                ch_l "I'll get warmed up."
                jump Danger_Room_Entry
            elif newgirl["Laura"].Loc == "bg laura": 
                
                
                ch_l "Never mind, it's too much of a mess, I'll meet you in your room." 
                $ newgirl["Laura"].Loc = "bg player"
                jump Player_Room  
                    
                ch_l "Ok."
                jump Laura_Room
            elif newgirl["Laura"].Loc == "bg player": 
                ch_l "Good."
                jump Player_Room                
            elif newgirl["Laura"].Loc == "bg showerroom": 
                ch_l "Ok, nice."
                jump Shower_Room_Entry
            elif newgirl["Laura"].Loc == "bg campus": 
                ch_l "Ok, nice."
                jump Campus_Entry
            else:            
                ch_l "I'll just meet you in your room."
                $ newgirl["Laura"].Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_l "Well, I guess you should never go alone. . ."
    elif Line == "command": 
            ch_l "Yes [newgirl[Laura].Petname]."
    
    $ Line = 0
    ch_l "I'll stick around."                                
    $ newgirl["Laura"].Loc = bg_current 
    return

# End Laura Leave ///////////////////   

label Laura_Dismissed(Leaving = 0):
    if "Laura" in Party:        
            $ Party.remove("Laura")
    call Laura_Schedule(0) #if newgirl["Laura"].Loc == bg_current then it means she wants to stay here
    menu:
        "You can leave if you like.":
                if newgirl["Laura"].Loc != bg_current and not ApprovalCheck("Laura", 600, "O"):
                        ch_l "Ok. [[she does not seem to be moving. . .]"
                else:
                        ch_l "Ok."
                        $ Leaving = 1                   
        "Could you give me the room please?":                            
                if newgirl["Laura"].Loc != bg_current and not ApprovalCheck("Laura", 800, "LO"):
                        ch_l "Nobody's kicking you out [[She doesn't move]."
                elif not ApprovalCheck("Laura", 500, "LO"):
                        ch_l "Nope."               
                else:
                        if "dismissed" not in newgirl["Laura"].DailyActions:
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 7)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 5)
                        ch_l "Sure, ok." 
                        $ Leaving = 1                              
        "You can go now.":                         
                if newgirl["Laura"].Loc != bg_current and not ApprovalCheck("Laura", 450, "O"):
                        ch_l "But I won't."
                elif not ApprovalCheck("Laura", 250, "O"):
                        call LauraFace("confused") 
                        ch_l "Why?"
                else:
                        if "dismissed" not in newgirl["Laura"].DailyActions:
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 10)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 7)
                        ch_l "Ok."
                        $ Leaving = 1                               
        "Nevermind.":
                        return                                           
                
    if not Leaving:     
            menu:
                extend ""
                "I insist, get going.":  
                        if newgirl["Laura"].Loc != bg_current and (ApprovalCheck("Laura", 1200, "LO") or ApprovalCheck("Laura", 400, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in newgirl["Laura"].DailyActions:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 10)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                ch_l "Ok, fine."  
                                $ Leaving = 1                                  
                        elif newgirl["Laura"].Loc != bg_current and (ApprovalCheck("Laura", 1000, "LO") or ApprovalCheck("Laura", 250, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in newgirl["Laura"].DailyActions:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5, 1)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 10)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                call LauraFace("angry") 
                                ch_l "I've got stuff to do anyway."      
                                $ Leaving = 1                         
                        elif newgirl["Laura"].Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in newgirl["Laura"].DailyActions:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5, 1)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -10, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 5)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3)
                                call LauraFace("angry") 
                                ch_l "Not until I see what you have planned here."          
                        elif ApprovalCheck("Laura", 1400, "LO") or ApprovalCheck("Laura", 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in newgirl["Laura"].DailyActions:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                                call LauraFace("sad") 
                                ch_l "Ok."
                                $ Leaving = 1                   
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in newgirl["Laura"].DailyActions:
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -5, 1)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -10, 1)
                                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -5)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3)
                                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 2)
                                call LauraFace("sad") 
                                ch_l "Nope."          
                "Ok, nevermind.":    
                                pass
                    
    if "dismissed" not in newgirl["Laura"].DailyActions:
            $ newgirl["Laura"].DailyActions.append("dismissed")        
    if Leaving == 0:
            # Stay
            $ newgirl["Laura"].Loc = bg_current
    else:
            # Go
            if newgirl["Laura"].Loc != bg_current: #it stays the same
                pass
            elif bg_current == "bg laura":
                $ newgirl["Laura"].Loc = "bg campus"
            else:
                $ newgirl["Laura"].Loc = "bg laura"
            hide Laura_Sprite
            "Laura heads out." 
    return
    #end "you can leave"
    

label Laura_AboutRogue:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Rogue" in newgirl["Laura"].Traits:  
        ch_l "Yeah, we hook up, so. . ."    
    elif newgirl["Laura"].LikeRogue >= 900:
        ch_l "She's got a great ass. . ."
    elif newgirl["Laura"].LikeRogue >= 800:
        ch_l "She's got a nice shape on her. . ."    
    elif newgirl["Laura"].LikeRogue >= 700:
        ch_l "She's good in a fight."
    elif newgirl["Laura"].LikeRogue >= 600:
        ch_l "We get along ok."
    elif newgirl["Laura"].LikeRogue >= 500:
        ch_l "I guess I've seen her around."
    elif newgirl["Laura"].LikeRogue >= 400:
        ch_l "I don't want to talk about it."
    elif newgirl["Laura"].LikeRogue >= 300:
        ch_l "Hate her." 
    else:
        ch_l "Bitch."
          
    return
    
label Laura_AboutKitty:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Kitty" in newgirl["Laura"].Traits:  
        ch_l "Yeah, we hook up, so. . ."    
    elif newgirl["Laura"].LikeKitty >= 900:
        ch_l "I do like her little tits. . ."
    elif newgirl["Laura"].LikeKitty >= 800:
        ch_l "She keeps in shape. . ."  
    elif newgirl["Laura"].LikeKitty >= 700:
        ch_l "Tough to hold down."
    elif newgirl["Laura"].LikeKitty >= 600:
        ch_l "She's cool."
    elif newgirl["Laura"].LikeKitty >= 500:
        ch_l "I guess I've seen her around."
    elif newgirl["Laura"].LikeKitty >= 400:
        ch_l "I don't want to talk about it."
    elif newgirl["Laura"].LikeKitty >= 300:
        ch_l "Hate her." 
    else:
        ch_l "Bitch."
          
    return
#End Laura_AboutEmma
label Laura_AboutEmma:
    ch_l "What do I think about her? Well. . ."
    
    if "poly Emma" in newgirl["Laura"].Traits:  
        ch_l "Yeah, we hook up, so. . ." 
    elif newgirl["Laura"].LikeEmma >= 900:
        ch_l "Really great rack on her. . ."
    elif newgirl["Laura"].LikeEmma >= 800:
        ch_l "She smells really nice. . ."    
    elif newgirl["Laura"].LikeEmma >= 700:
        ch_l "She's nice to me after class."
    elif newgirl["Laura"].LikeEmma >= 600:
        ch_l "She's a good teacher."
    elif newgirl["Laura"].LikeEmma >= 500:
        ch_l "She's fine."
    elif newgirl["Laura"].LikeEmma >= 400:
        ch_l "I could do with less of her attitude."
    elif newgirl["Laura"].LikeEmma >= 300:
        ch_l "She needs to stay out of my head." 
    else:
        ch_l "Grrrrr."
          
    return
    
#End Laura_AboutEmma   

## Laura's Clothes ///////////////////
label Laura_Clothes:    
    call LauraFace
    menu:
        ch_l "what about my clothes?"
        "Let's talk about your outfits.":
                    jump Laura_Clothes_Outfits        
        "Let's talk about your over shirts.":
                    jump Laura_Clothes_Over        
        "Let's talk about your legwear.":
                    jump Laura_Clothes_Legs
        "Let's talk about your underwear.":
                    jump Laura_Clothes_Under
        "Let's talk about the other stuff.":
                    jump Laura_Clothes_Misc
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call Laura_OutfitShame(3,1)
                    "Custom 2":
                                call Laura_OutfitShame(5,1)
                    "Custom 3":
                                call Laura_OutfitShame(6,1)
                    "Gym Clothes":
                                call Laura_OutfitShame(7,1)
                    "Sleepwear":
                                call Laura_OutfitShame(9,1)
                    "Never mind":
                                pass
        "Save as main menu background clothes.":
                "This option will save this Laura at the main menu background, are you sure?"
                menu:
                    "Yes":
                        "do it"
                        $ persistent.L_BG_Over = newgirl["Laura"].Over
                        $ persistent.L_BG_Chest = newgirl["Laura"].Chest
                        # $ persistent.L_BG_BodySuit = newgirl["Laura"].BodySuit
                        $ persistent.L_BG_Neck = newgirl["Laura"].Neck
                        $ persistent.L_BG_Legs = newgirl["Laura"].Legs
                        $ persistent.L_BG_Panties = newgirl["Laura"].Panties
                        $ persistent.L_BG_Arms = newgirl["Laura"].Arms
                        # $ persistent.L_BG_Accessory = newgirl["Laura"].Accessory
                        # $ persistent.L_BG_Glasses = newgirl["Laura"].Glasses
                        # $ persistent.L_BG_Gloves = newgirl["Laura"].Gloves
                        # $ persistent.L_BG_Tan = newgirl["Laura"].Tan
                        # $ persistent.L_BG_DynamicTan = newgirl["Laura"].DynamicTan
                        $ persistent.L_BG_Pierce = newgirl["Laura"].Pierce
                        $ persistent.L_BG_Hair = newgirl["Laura"].Hair
                        # $ persistent.L_BG_Water = newgirl["Laura"].Water
                        # $ persistent.L_BG_HairColor = newgirl["Laura"].HairColor
                        $ persistent.L_BG_Pubes = newgirl["Laura"].Pubes
                        $ persistent.L_BG_Hose = newgirl["Laura"].Hose
                        # $ persistent.L_BG_Headband = newgirl["Laura"].Headband
                        # $ persistent.L_BG_Gag = newgirl["Laura"].Gag
                        # $ persistent.L_BG_Blindfold = newgirl["Laura"].Blindfold
                        # $ persistent.L_BG_Boots = newgirl["Laura"].Boots

                    "No":
                        pass

        "Never mind, you look good like that.":
                if "wardrobe" not in newgirl["Laura"].RecentActions: 
                        #Apply stat boosts only if it's the first time this turn 
                        if newgirl["Laura"].Chat[1] <= 1:                
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 15)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 20)
                                ch_l "Oh! Thank you."
                        elif newgirl["Laura"].Chat[1] <= 10:
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 5)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 7)
                                ch_l "Right?" 
                        elif newgirl["Laura"].Chat[1] <= 50:
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 40, 1)  
                                ch_l "Uhhuh."
                        else:
                                ch_l "Sure."                    
                        $ newgirl["Laura"].RecentActions.append("wardrobe")  
                #sets up a temporary outfit
                $ newgirl["Laura"].TempClothes[1] = newgirl["Laura"].Arms  
                $ newgirl["Laura"].TempClothes[2] = newgirl["Laura"].Legs 
                $ newgirl["Laura"].TempClothes[3] = newgirl["Laura"].Over
                $ newgirl["Laura"].TempClothes[4] = newgirl["Laura"].Neck 
                $ newgirl["Laura"].TempClothes[5] = newgirl["Laura"].Chest 
                $ newgirl["Laura"].TempClothes[6] = newgirl["Laura"].Panties
#                $ newgirl["Laura"].TempClothes[7] = newgirl["Laura"].Boots
                $ newgirl["Laura"].TempClothes[8] = newgirl["Laura"].Hair
                $ newgirl["Laura"].TempClothes[9] = newgirl["Laura"].Hose
                $ newgirl["Laura"].TempClothes[0] = 1 
                $ newgirl["Laura"].Outfit = "temporary"
                $ newgirl["Laura"].OutfitDay = "temporary"        
                $ newgirl["Laura"].Chat[1] += 1                
                return
            
    jump Laura_Clothes
    #End of Laura Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Outfits:                                                                                 # Outfits
        "I really like that leather combat outfit you wear.": 
            call LauraOutfit("mission")   
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl["Laura"].Outfit = "mission"
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[1]
                    ch_l "Yeah, I love wearing this one in the field."
                "Let's try something else though.":
                    ch_l "Ok."            
                    
        "That leather jacket and skirt really nice on you.":  
            call LauraOutfit("streets")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ newgirl["Laura"].Outfit = "streets"
                    $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[2]
                    ch_l "Yeah, I mean, my cousin got it for me."
                "Let's try something else though.":
                    ch_l "Ok."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not newgirl["Laura"].Custom[0] and not newgirl["Laura"].Custom2[0] and not newgirl["Laura"].Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if newgirl["Laura"].Custom[0] or newgirl["Laura"].Custom2[0] or newgirl["Laura"].Custom3[0]: 
            $ Cnt = 0
            while 1:
                menu:                
                    "Throw on Custom 1 (locked)" if not newgirl["Laura"].Custom[0]:
                        pass
                    "Throw on Custom 1" if newgirl["Laura"].Custom[0]:
                        call LauraOutfit("custom1")
                        $ Cnt = 3
                    "Throw on Custom 2 (locked)" if not newgirl["Laura"].Custom2[0]:
                        pass
                    "Throw on Custom 2" if newgirl["Laura"].Custom2[0]:
                        call LauraOutfit("custom2")
                        $ Cnt = 5
                    "Throw on Custom 3 (locked)" if not newgirl["Laura"].Custom3[0]:
                        pass
                    "Throw on Custom 3" if newgirl["Laura"].Custom3[0]:
                        call LauraOutfit("custom3")
                        $ Cnt = 6
                    
                    "You should wear this one in our rooms. (locked)" if not Cnt:
                        pass
                    "You should wear this one in our rooms." if Cnt:
                        if Cnt == 5:
                            $ newgirl["Laura"].Schedule[9] = "custom2"
                        elif Cnt == 6:
                            $ newgirl["Laura"].Schedule[9] = "custom3"
                        else:
                            $ newgirl["Laura"].Schedule[9] = "custom"
                        ch_l "Ok, sure."
                    
                    
                    "On second thought, forget about that one outfit. . .":
                        menu:
                            "Custom 1 [[clear custom 1]" if newgirl["Laura"].Custom[0]:
                                ch_l "Ok."
                                $ newgirl["Laura"].Custom[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not newgirl["Laura"].Custom[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if newgirl["Laura"].Custom2[0]:
                                ch_l "Ok."
                                $ newgirl["Laura"].Custom2[0] = 0
                            "Custom 2 [[clear custom 1] (locked)" if not newgirl["Laura"].Custom2[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if newgirl["Laura"].Custom3[0]:
                                ch_l "Ok."
                                $ newgirl["Laura"].Custom3[0] = 0
                            "Custom 3 [[clear custom 1] (locked)" if not newgirl["Laura"].Custom3[0]:
                                pass
                            "Never mind, [[back].":
                                pass    
                                            
                                            
                    "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                        pass
                    "You should wear this one out." if Cnt:
                        call Laura_Custom_Out(Cnt)
                    "Ok, back to what we were talking about. . .":
                        $ Cnt = 0
                        jump Laura_Clothes_Outfits                    
        
        "Your birthday suit looks really great. . .":                                     #Nude
            call LauraFace("sexy", 1)
            $ Line = 0
            if not newgirl["Laura"].Chest and not newgirl["Laura"].Panties and not newgirl["Laura"].Over and not newgirl["Laura"].Legs and not newgirl["Laura"].Hose:                
                ch_l "Yeah. . . wait, how would you know?"  
            elif newgirl["Laura"].SeenChest and newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 1200, TabM=4):
                ch_l "You know it. . ."  
                $ Line = 1
            elif ApprovalCheck("Laura", 2000, TabM=4):
                ch_l "Skipping straight to that?"    
                $ Line = 1
            elif newgirl["Laura"].SeenChest and newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 1200, TabM=0):
                ch_l "Maybe, but not here. . ."  
            elif ApprovalCheck("Laura", 2000, TabM=0):
                ch_l "Maybe, but not here. . ."  
            elif ApprovalCheck("Laura", 1000, TabM=0):                
                call LauraFace("confused", 1,Mouth="smirk")
                ch_l "Yeah, but I'm not exactly showing it off."
                call LauraFace("bemused", 0)
            else:
                call LauraFace("angry", 1)
                ch_l "What's it to you?"    
                
            if Line:                                                            #If she got nude. . .                            
                call LauraOutfit("nude")
                "She throws her clothes off at her feet."
                call Laura_First_Topless
                call Laura_First_Bottomless(1)
                call LauraFace("sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in newgirl["Laura"].Traits:
                            ch_l "mmmm. . ." 
                            $ newgirl["Laura"].Outfit = "nude"
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 10) 
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5) 
                            $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[0]
                        elif ApprovalCheck("Laura", 800, "I") or ApprovalCheck("Laura", 2800, TabM=0):                    
                            ch_l "Exciting. . ."
                            $ newgirl["Laura"].Outfit = "nude"
                            $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[0]
                        else:
                            call LauraFace("sexy", 1)
                            $ newgirl["Laura"].Eyes = "surprised"
                            ch_l "I probably shouldn't. Sorry." 
                            
                    "Let's try something else though.":
                        if "exhibitionist" in newgirl["Laura"].Traits:
                            ch_l "Are you sure?"                         
                        elif ApprovalCheck("Laura", 800, "I") or ApprovalCheck("Laura", 2800, TabM=0):       
                            call LauraFace("bemused", 1)             
                            ch_l "I was worried you expected me to wear this out."
                            ch_l ". . ."
                        else:
                            call LauraFace("confused", 1)
                            ch_l "I don't mind you seeing my body, but. . ."   
            $ Line = 0
                
        "How about throwing on your sleepwear?" if not Taboo:
            #fix add conditions
            call LauraOutfit("sleep")
            
        "Let's talk about what you wear outside.":
            call Laura_Clothes_Schedule
            
        "Never mind":    
            jump Laura_Clothes     
            
    jump Laura_Clothes
    #End of Laura Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Over:                                                                                            # Overshirts
        "Why don't you go with no [newgirl[Laura].Over]?" if newgirl["Laura"].Over:
            call LauraFace("bemused", 1)
            if ApprovalCheck("Laura", 800, TabM=3) and (newgirl["Laura"].Chest or newgirl["Laura"].SeenChest):
                ch_l "Ok."
            elif ApprovalCheck("Laura", 1200, TabM=0):
                call Laura_NoBra
                if not _return:
                    jump Laura_Clothes
            $ Line = newgirl["Laura"].Over
            $ newgirl["Laura"].Over = 0
            "She throws her [Line] at her feet."
            if not newgirl["Laura"].Chest:
                    call Laura_First_Topless
            
        "Try on that leather jacket." if newgirl["Laura"].Over != "jacket":
            call LauraFace("bemused")
            if not newgirl["Laura"].Over or newgirl["Laura"].Chest == "leather bra":
                #if she's not already wearing a top, or has the leather bra on
                ch_l "Sure."
            elif ApprovalCheck("Laura", 800, TabM=0):
                ch_l "Yeah, ok."          
            else:
                call LauraFace("bemused", 1)
                ch_l "I don't really want to take this [newgirl[Laura].Over] off at the moment."
                jump Laura_Clothes    
            $ newgirl["Laura"].Over = "jacket"   
                
#        "How about that red t-shirt you have?" if newgirl["Laura"].Over != "red shirt":
#            $ newgirl["Laura"].Over = "red shirt"  
#            ch_l "This one?"
            
        "Maybe just throw on a towel?" if newgirl["Laura"].Over != "towel":
            call LauraFace("bemused", 1)
            if newgirl["Laura"].Chest or newgirl["Laura"].SeenChest:
                ch_l "Weird."
            elif ApprovalCheck("Laura", 1000, TabM=0):
                call LauraFace("perplexed", 1)
                ch_l "Huh, ok . ."          
            else:
                ch_l "That wouldn't look right."
                jump Laura_Clothes    
            $ newgirl["Laura"].Over = "towel"    
                            
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Laura_NoBra: #fix test this
        menu:
            ch_l "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":   
                        if newgirl["Laura"].SeenChest and ApprovalCheck("Laura", 1000, TabM=3):
                                $ newgirl["Laura"].Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ newgirl["Laura"].Blush = 0                        
                        elif ApprovalCheck("Laura", 1200, TabM=4):
                                $ newgirl["Laura"].Blush = 1
                                ch_l "-I didn't say that I minded. . ."
                                $ newgirl["Laura"].Blush = 0                
                        elif ApprovalCheck("Laura", 900, TabM=2) and "corset" in newgirl["Laura"].Inventory:
                                ch_l "I guess I could find something."
                                $ newgirl["Laura"].Chest  = "corset"    
                                "She pulls out her corset and slips it under her [newgirl[Laura].Over]."
                        elif ApprovalCheck("Laura", 700, TabM=2):
                                ch_l "Yeah, I guess."
                                $ newgirl["Laura"].Chest = "leather bra"
                                "She pulls out her leather bra and slips it on under her [newgirl[Laura].Over]."
#                        elif ApprovalCheck("Laura", 600, TabM=2):
#                                ch_l "Yeah, I guess."
#                                $ newgirl["Laura"].Chest = "sports bra"
#                                "She pulls out her sports bra and passes it through her [newgirl[Laura].Over]."
                        else:
                                ch_l "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Laura", 1100, "LI", TabM=2) and newgirl["Laura"].Love > newgirl["Laura"].Inbt:               
                                ch_l "For you? I guess. . ."
                        elif ApprovalCheck("Laura", 700, "OI", TabM=2) and newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                                ch_l "Sure. . ."
                        elif ApprovalCheck("Laura", 600, "I", TabM=2):
                                ch_l "Yeah. . ."
                        elif ApprovalCheck("Laura", 1300, TabM=2):
                                ch_l "Okay, fine."
                        else: 
                                call LauraFace("surprised")
                                $ newgirl["Laura"].Brows = "angry"
                                if Taboo > 20:
                                    ch_l "Not in public, I won't!"
                                else:
                                    ch_l "You're not that cute, [newgirl[Laura].Petname]!"
                                return 0
                                
                    
            "Never mind.":
                        ch_l "Ok. . ."
                        return 0
        return 1
        #End of Laura bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Legs:                                                                                                    # Leggings    
        "Maybe go without the [newgirl[Laura].Legs]." if newgirl["Laura"].Legs:
            call LauraFace("sexy", 1)
            if newgirl["Laura"].SeenPanties and newgirl["Laura"].Panties and ApprovalCheck("Laura", 500, TabM=5):
                ch_l "Ok, sure."
            elif newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 900, TabM=4):
                ch_l "Yeah, ok."
            elif ApprovalCheck("Laura", 1300, TabM=2) and newgirl["Laura"].Panties:
                ch_l "For you, fine. . ."
            elif ApprovalCheck("Laura", 800) and not newgirl["Laura"].Panties:
                call Laura_NoPantiesOn
                if not _return:
                    jump Laura_Clothes
            else:
                ch_l "Um, not with you around."
                if not newgirl["Laura"].Panties:
                    ch_l "I'm going commando today. . ."
                jump Laura_Clothes
            if newgirl["Laura"].Legs == "leather pants" or newgirl["Laura"].Legs == "mesh pants":
                    $ newgirl["Laura"].Legs = 0    
                    "She tugs her pants off and drops them to the ground."
            else:
                    $ newgirl["Laura"].Legs = 0    
                    "She tugs her skirt off and drops it to the ground."
            if newgirl["Laura"].Panties:                
                $ newgirl["Laura"].SeenPanties = 1
            else:
                call Laura_First_Bottomless
        
        "You look great in those leather pants." if newgirl["Laura"].Legs != "leather pants":
            ch_l "Yeah, ok."
            $ newgirl["Laura"].Legs = "leather pants"
                
        "You look great in those mesh pants." if newgirl["Laura"].Legs != "mesh pants":
            if ApprovalCheck("Laura", 1000, TabM=4):
                    ch_l "Yeah, ok."
                    $ newgirl["Laura"].Legs = "mesh pants"
            else:
                    ch_l "Sorry, those are kind of. . . breezy."
        
#        "You look great in yoga pants." if newgirl["Laura"].Legs != "yoga pants":
#            ch_l "Yeah, ok."
#            $ newgirl["Laura"].Legs = "yoga pants"
            
        "What about wearing your leather skirt?" if newgirl["Laura"].Legs != "skirt":
            ch_l "Sure, why not."
            $ newgirl["Laura"].Legs = "skirt"    
            
                   
                                
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Laura_NoPantiesOn: #fix test this
        menu:
            ch_l "I'm going commando today."
            "Then you could slip on a pair of panties. . .":   
                        if newgirl["Laura"].SeenPussy and ApprovalCheck("Laura", 1100, TabM=4):
                                $ newgirl["Laura"].Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ newgirl["Laura"].Blush = 0                        
                        elif ApprovalCheck("Laura", 1500, TabM=4):
                                $ newgirl["Laura"].Blush = 1
                                ch_l "No, commando's fine. . ."
                                $ newgirl["Laura"].Blush = 0                
                        elif ApprovalCheck("Laura", 800, TabM=4) and "lace panties" in newgirl["Laura"].Inventory:
                                ch_l "I like how you think."
                                $ newgirl["Laura"].Panties  = "lace panties"  
                                if ApprovalCheck("Laura", 1200, TabM=4):   
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She pulls off her [newgirl[Laura].Legs] and slips on the lace panties."                                    
                                elif newgirl["Laura"].Legs == "skirt":
                                    "She pulls out her lace panties and pulls them up under her skirt."
                                    $ newgirl["Laura"].Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She steps away a moment and then comes back wearing only the lace panties."                                     
                                jump Laura_Clothes
                        elif ApprovalCheck("Laura", 700, TabM=4):
                                ch_l "Yeah, I guess."
                                $ newgirl["Laura"].Panties = "black panties"
                                if ApprovalCheck("Laura", 1200, TabM=4):   
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She pulls off her [newgirl[Laura].Legs] and slips on the black panties."                                    
                                elif newgirl["Laura"].Legs == "skirt":
                                    "She pulls out her black panties and pulls them up under her skirt."
                                    $ newgirl["Laura"].Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She steps away a moment and then comes back wearing only the black panties."                                     
                                jump Laura_Clothes
                        elif ApprovalCheck("Laura", 600, TabM=4):
                                ch_l "Yeah, I guess."
                                $ newgirl["Laura"].Panties = "wolvie panties"
                                if ApprovalCheck("Laura", 1200, TabM=4):   
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She pulls off her [newgirl[Laura].Legs] and slips on the wolvie panties."                                    
                                elif newgirl["Laura"].Legs == "skirt":
                                    "She pulls out her wolvie panties and pulls them up under her skirt."
                                    $ newgirl["Laura"].Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = newgirl["Laura"].Legs
                                    $ newgirl["Laura"].Legs = 0
                                    "She steps away a moment and then comes back wearing only the wolvie panties."                                     
                                jump Laura_Clothes
                        else:
                                ch_l "Nope."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck("Laura", 1100, "LI", TabM=3) and newgirl["Laura"].Love > newgirl["Laura"].Inbt:               
                                ch_l "True. . ."
                        elif ApprovalCheck("Laura", 700, "OI", TabM=3) and newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                                ch_l "Yes. . ."
                        elif ApprovalCheck("Laura", 600, "I", TabM=3):
                                ch_l "Hrmm. . ."
                        elif ApprovalCheck("Laura", 1300, TabM=3):
                                ch_l "Fine."
                        else: 
                                call LauraFace("surprised")
                                $ newgirl["Laura"].Brows = "angry"
                                if Taboo > 20:
                                    ch_l "Yeah, but not in public, [newgirl[Laura].Petname]!"
                                else:
                                    ch_l "You aren't that cute, [newgirl[Laura].Petname]!"
                                return 0
                                
            "Never mind.":
                ch_l "Ok. . ."
                return 0
        return 1
        #End of Laura Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Laura_Clothes_Under:                                                                                                 # Tops    
        "How about you lose the [newgirl[Laura].Chest]?" if newgirl["Laura"].Chest:
            call LauraFace("bemused", 1)
            if newgirl["Laura"].SeenChest and ApprovalCheck("Laura", 900, TabM=2.7):
                ch_l "Ok."    
            elif ApprovalCheck("Laura", 1100, TabM=2):
                if Taboo:
                    ch_l "I don't know, here. . ."
                else:
                    ch_l "Maybe. . ."
            elif newgirl["Laura"].Over == "jacket" and ApprovalCheck("Laura", 600, TabM=2):
                ch_l "This jacket is a bit revealing. . ."  
            elif newgirl["Laura"].Over and ApprovalCheck("Laura", 500, TabM=2):
                ch_l "I guess I could. . ."  
            elif not newgirl["Laura"].Over:
                ch_l "Not without some other top."
                jump Laura_Clothes 
            else:
                ch_l "Nah."
                jump Laura_Clothes 
            $ Line = newgirl["Laura"].Chest
            $ newgirl["Laura"].Chest = 0
            if newgirl["Laura"].Over:
                "She reaches under her [newgirl[Laura].Over] grabs her [Line], and pulls it off, dropping it to the ground."
            else:
                "She pulls off her [Line] and drops it to the ground."
                call Laura_First_Topless
            
            
        "Try on that leather bra." if newgirl["Laura"].Chest != "leather bra":
            ch_l "Ok."
            $ newgirl["Laura"].Chest = "leather bra"           
            
        "I like that corset." if newgirl["Laura"].Chest != "corset" and "corset" in newgirl["Laura"].Inventory:
            if newgirl["Laura"].SeenChest or ApprovalCheck("Laura", 1300, TabM=2):
                ch_l "K."   
                $ newgirl["Laura"].Chest = "corset"         
            else:                
                ch_l "It's a bit transparent. . ."  
                            
        "I like that wolverine tanktop." if newgirl["Laura"].Chest != "wolvie top":
            if newgirl["Laura"].SeenChest or ApprovalCheck("Laura", 1000, TabM=2):
                ch_l "K."   
                $ newgirl["Laura"].Chest = "wolvie top"         
            else:                
                ch_l "It's a {i}little{/i} embarrassing. . ."  

#        "I like that sports bra." if newgirl["Laura"].Chest != "sports bra":
#            if newgirl["Laura"].SeenChest or ApprovalCheck("Laura", 1000, TabM=2):
#                ch_l "K."   
#                $ newgirl["Laura"].Chest = "sports bra"         
#            else:                
#                ch_l "I'm not sure about that. . ."  
        
              
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if newgirl["Laura"].Hose and newgirl["Laura"].Hose != 'ripped tights' and newgirl["Laura"].Hose != 'tights':     
                                $ newgirl["Laura"].Hose = 0  
                "The thigh-high hose would look good with that." if newgirl["Laura"].Hose != "stockings":     
                                $ newgirl["Laura"].Hose = "stockings"  
#                "The pantyhose would look good with that." if newgirl["Laura"].Hose != "pantyhose":     
#                                $ newgirl["Laura"].Hose = "pantyhose" 
                "The stockings and garterbelt would look good with that." if newgirl["Laura"].Hose != "stockings and garterbelt" and "stockings and garterbelt":     
                                $ newgirl["Laura"].Hose = "stockings and garterbelt"  
#                "Your ripped pantyhose would look good with that." if newgirl["Laura"].Hose != "ripped pantyhose" and "ripped pantyhose" in newgirl["Laura"].Inventory:     
#                                $ newgirl["Laura"].Hose = "ripped pantyhose"    
                "Never mind":
                        pass  
                        
        #Panties        
        "You could lose those panties. . ." if newgirl["Laura"].Panties:
            call LauraFace("bemused", 1)  
            if ApprovalCheck("Laura", 900) and (newgirl["Laura"].Legs or (newgirl["Laura"].SeenPussy and not Taboo)):
                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                
                if ApprovalCheck("Laura", 850, "L"):               
                        ch_l "True. . ."
                elif ApprovalCheck("Laura", 500, "O"):
                        ch_l "Agreed."
                elif ApprovalCheck("Laura", 350, "I"):
                        ch_l "Heh."
                else:
                        ch_l "Sure, I guess."         
            else:                       #low approval or not wearing pants or in public 
                if ApprovalCheck("Laura", 1100, "LI", TabM=3) and newgirl["Laura"].Love > newgirl["Laura"].Inbt:               
                        ch_l "Well look, it's not about you, but. . ."
                elif ApprovalCheck("Laura", 700, "OI", TabM=3) and newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                        ch_l "Well. . ."
                elif ApprovalCheck("Laura", 600, "I", TabM=3):
                        ch_l "Hrmm. . ."
                elif ApprovalCheck("Laura", 1300, TabM=3):
                        ch_l "Okay, okay."
                else: 
                        call LauraFace("surprised")
                        $ newgirl["Laura"].Brows = "angry"
                        if Taboo > 20:
                            ch_l "This is too public."
                        else:
                            ch_l "You're not that cute, [newgirl[Laura].Petname]!"
                        jump Laura_Clothes
                        
            $ newgirl["Laura"].Panties = 0
            if not newgirl["Laura"].Legs:
                "She pulls off her panties, then drops them to the ground." 
                call Laura_First_Bottomless  
            if ApprovalCheck("Laura", 1200, TabM=4):   
                $ Line = newgirl["Laura"].Legs
                $ newgirl["Laura"].Legs = 0
                "She pulls off her [newgirl[Laura].Legs] and panties, then pulls the [newgirl[Laura].Legs] back on."  
                $ newgirl["Laura"].Legs = Line       
                call Laura_First_Bottomless(1)                             
            elif newgirl["Laura"].Legs == "skirt":
                "She reaches under her skirt and pulls her panties off."
            else:
                $ newgirl["Laura"].Blush = 1
                "She steps away a moment and then comes back."  
                $ newgirl["Laura"].Blush = 0                                    
                
        "Why don't you wear the black panties instead?" if newgirl["Laura"].Panties and newgirl["Laura"].Panties != "black panties":
            if ApprovalCheck("Laura", 1100, TabM=3):
                    ch_l "Ok."
                    $ newgirl["Laura"].Panties = "black panties"  
            else:                
                    ch_l "That's none of your busines."
                
        "Why don't you wear the wolverine panties instead?" if newgirl["Laura"].Panties and newgirl["Laura"].Panties != "wolvie panties":
            if ApprovalCheck("Laura", 1000, TabM=3):
                    ch_l "I guess."
                    $ newgirl["Laura"].Panties = "wolvie panties"
            else:
                    ch_l "That's none of your busines."
                    
        "Why don't you wear the lace panties instead?" if "lace panties" in newgirl["Laura"].Inventory and newgirl["Laura"].Panties and newgirl["Laura"].Panties != "lace panties":
            if ApprovalCheck("Laura", 1300, TabM=3):
                    ch_l "I guess."
                    $ newgirl["Laura"].Panties = "lace panties"
            else:
                    ch_l "That's none of your busines."
                
        "You know, you could wear some panties with that. . ." if not newgirl["Laura"].Panties:
            call LauraFace("bemused", 1)
            if (newgirl["Laura"].Love+newgirl["Laura"].Obed) <= (2 * newgirl["Laura"].Inbt):
                $ newgirl["Laura"].Mouth = "smile"
                ch_l "I don't know about that."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)
                menu:
                    "Fine by me":
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)
                        jump Laura_Clothes
                    "I insist, put some on.":
                        if (newgirl["Laura"].Love+newgirl["Laura"].Obed) <= (1.5 * newgirl["Laura"].Inbt):
                            call LauraFace("angry", Eyes="side")
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 99, 5)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, -5)
                            ch_l "Well I insist otherwise."
                            jump Laura_Clothes
                        else:
                            call LauraFace("sadside")
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, -5)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 5)
                            ch_l "Oh, fine."    
            else:                
                ch_l "I guess. . ."
            menu:
                extend ""
                "How about the black ones?":
                    ch_l "Sure, ok."
                    $ newgirl["Laura"].Panties = "black panties"
                "How about the wolvie ones?":
                    ch_l "Sure."                
                    $ newgirl["Laura"].Panties  = "wolvie panties"
                "How about the lace ones?" if "lace panties" in newgirl["Laura"].Inventory:
                    ch_l "Alright."                
                    $ newgirl["Laura"].Panties  = "lace panties"
        "Never mind":
            pass
    jump Laura_Clothes
    #End of Laura Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Laura_Clothes_Misc:                                                                                                                    #Misc
#        "You look good with your hair up." if newgirl["Laura"].Hair != "evo":
#            if ApprovalCheck("Laura", 600):
#                ch_l "Like this?"
#                $ newgirl["Laura"].Hair = "evo"
#            else:
#                ch_l "Yeah, I know that."
                
#        "Maybe let your hair down." if newgirl["Laura"].Hair != "long":
#            if ApprovalCheck("Laura", 600):
#                ch_l "You think?"
#                $ newgirl["Laura"].Hair = "long"
#            else:
#                ch_l "I[newgirl[Laura].like]kinda prefer to keep it up."
                
#        "You should go for that wet look with your hair." if newgirl["Laura"].Hair != "wet":
#            if ApprovalCheck("Laura", 800):
#                ch_l "You think so?"
#                "She rummages in her bag and grabs some gel, running it through her hair."
#                ch_l "Like this?"
#                $ newgirl["Laura"].Hair = "wet"
#            else:
#                ch_l "It's too high maintenance."
        
        "You know, I like some nice hair down there. Maybe grow it out." if not newgirl["Laura"].Pubes and "pubes" in newgirl["Laura"].Todo:
            call LauraFace("bemused", 1)
            ch_l "Even I can't grow it out instantly."
        "You know, I like some nice hair down there. Maybe grow it out." if not newgirl["Laura"].Pubes and "pubes" not in newgirl["Laura"].Todo:
            call LauraFace("bemused", 1)
            if ApprovalCheck("Laura", 1000, TabM=0):               
                ch_l "Sure, that's easier. . ."           
            else: 
                call LauraFace("surprised")
                $ newgirl["Laura"].Brows = "angry"
                ch_l "I think I'll do what I want down there."
                jump Laura_Clothes
            $ newgirl["Laura"].Todo.append("pubes")
            $ newgirl["Laura"].PubeC = 6
        
        "I like it waxed clean down there." if newgirl["Laura"].Pubes == 1:
            call LauraFace("bemused", 1)            
            if "shave" in newgirl["Laura"].Todo:
                ch_l "Yeah, I know, I'll get to it."
            else:
                if ApprovalCheck("Laura", 1100, TabM=0):               
                    ch_l "Really? I guess I could give it a shave. . ."        
                else: 
                    call LauraFace("surprised")
                    $ newgirl["Laura"].Brows = "angry"
                    ch_l "I think I'll do what I want down there."
                    jump Laura_Clothes
                $ newgirl["Laura"].Todo.append("shave")        
#        "Piercings. [[See what she looks like without them first] (locked)" if not newgirl["Laura"].SeenPussy and not newgirl["Laura"].SeenChest:
#            pass
            
#        "You know, you'd look really nice with some ring body piercings." if newgirl["Laura"].Pierce != "ring" and (newgirl["Laura"].SeenPussy or newgirl["Laura"].SeenChest) and "ring" not in newgirl["Laura"].Todo:
#            call LauraFace("bemused", 1)
#            $ Approval = ApprovalCheck("Laura", 1350, TabM=0)
#            if ApprovalCheck("Laura", 900, "L", TabM=0) or (Approval and newgirl["Laura"].Love > 2* newgirl["Laura"].Obed):   
#                ch_l "You think I'd look good with them?"
#            elif ApprovalCheck("Laura", 600, "I", TabM=0) or (Approval and newgirl["Laura"].Inbt > newgirl["Laura"].Obed):
#                ch_l "I've been thinking about that for a while."
#            elif ApprovalCheck("Laura", 500, "O", TabM=0) or Approval:
#                ch_l "Yes, [newgirl[Laura].Petname]."
#            else: 
#                call LauraFace("surprised")
#                $ newgirl["Laura"].Brows = "angry"
#                ch_l "Not interested, [newgirl[Laura].Petname]."
#                jump Laura_Clothes            
#            $ newgirl["Laura"].Todo.append("ring")
        
#        "You know, you'd look really nice with some barbell body piercings." if newgirl["Laura"].Pierce != "barbell" and (newgirl["Laura"].SeenPussy or newgirl["Laura"].SeenChest)and "barbell" not in newgirl["Laura"].Todo:
#            call LauraFace("bemused", 1)
#            $ Approval = ApprovalCheck("Laura", 1350, TabM=0)
#            if ApprovalCheck("Laura", 900, "L", TabM=0) or (Approval and newgirl["Laura"].Love > 2 * newgirl["Laura"].Obed):   
#                ch_l "You think I'd look good with them?"
#            elif ApprovalCheck("Laura", 600, "I", TabM=0) or (Approval and newgirl["Laura"].Inbt > newgirl["Laura"].Obed):
#                ch_l "I've been thinking about that for a while."
#            elif ApprovalCheck("Laura", 500, "O", TabM=0) or Approval:
#                ch_l "Yes, [newgirl[Laura].Petname]."
#            else: 
#                call LauraFace("surprised")
#                $ newgirl["Laura"].Brows = "angry"
#                ch_l "Not interested, [newgirl[Laura].Petname]."
#                jump Laura_Clothes                
#            $ newgirl["Laura"].Todo.append("barbell")
#            $ newgirl["Laura"].Pierce = "barbell"
            
#        "You know, you'd look better without those piercings." if newgirl["Laura"].Pierce:
#            call LauraFace("bemused", 1)
#            $ Approval = ApprovalCheck("Laura", 1350, TabM=0)
#            if ApprovalCheck("Laura", 950, "L", TabM=0) or (Approval and newgirl["Laura"].Love > newgirl["Laura"].Obed):   
#                ch_l "Make up your mind . ."
#            elif ApprovalCheck("Laura", 700, "I", TabM=0) or (Approval and newgirl["Laura"].Inbt > newgirl["Laura"].Obed):
#                ch_l "In, out, snickt."
#            elif ApprovalCheck("Laura", 600, "O", TabM=0) or Approval:
#                ch_l "Fine."
#            else: 
#                call LauraFace("surprised")
#                $ newgirl["Laura"].Brows = "angry"
#                ch_l "I've sort of grown attached."
#                jump Laura_Clothes            
#            $ newgirl["Laura"].Pierce = 0 
#        "Why don't you try on that medallion choker." if newgirl["Laura"].Neck != "leash choker":
#            ch_l "Ok. . ."         
#            $ newgirl["Laura"].Neck = "leash choker"
#        "Maybe go without a necklace." if newgirl["Laura"].Neck:
#            ch_l "Ok. . ."         
#            $ newgirl["Laura"].Neck = 0
#        "Why don't you put those wristbands on." if newgirl["Laura"].Arms != "wrists":
#            ch_l "Ok. . ."         
#            $ newgirl["Laura"].Arms = "wrists"
#        "Maybe go without the wristbands." if newgirl["Laura"].Arms:
#            ch_l "Ok. . ."         
#            $ newgirl["Laura"].Arms = 0
            
        "Never mind":
            pass         
    jump Laura_Clothes
    #End of Laura Misc Wardrobe
    
return
#End Laura Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <



# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Laura_Clothes_Schedule(Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        
        if ApprovalCheck("Laura", 1500, "LO"):
                ch_l "Fine, you pick, whatever."
                $ Cnt = 3
        elif ApprovalCheck("Laura", 1200, "LO"):
                ch_l "I don't know, you could pick a few days. . ."
                $ Cnt = 2
        elif ApprovalCheck("Laura", 1000, "LO"):
                ch_l "Maybe on weekends. . ."
                $ Cnt = 1
        else:
                ch_l "Nah, I got it covered."
                return
            
        
        menu:
                extend ""
                "Weekdays":
                    menu:
                        "On Monday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[0] = _return
                        "On Monday you should wear. . . (locked)" if Cnt <= 1:
                            pass
                            
                        "On Tuesday you should wear. . ." if Cnt > 2:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[1] = _return        
                        "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Wednesday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[2] = _return
                        "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                            pass   
                            
                        "On Thursday you should wear. . ." if Cnt > 2:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[3] = _return
                        "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                            pass
                            
                        "On Friday you should wear. . ." if Cnt > 1:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[4] = _return
                        "On Friday you should wear. . . (locked)" if Cnt <= 1:
                            pass 
                        "Back":
                            pass         
               
                "Other":
                    menu:       
                        "On Saturday you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "On Saturday you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[5] = _return
                            
                        "On Sunday you should wear. . . (locked)" if Cnt < 1:
                            pass                          
                        "On Sunday you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[6] = _return
                            
                        "In our rooms you should wear. . . (locked)" if Cnt < 1:
                            pass
                        "In our rooms you should wear. . ." if Cnt >= 1:
                            call Laura_Clothes_ScheduleB(99)
                            $ newgirl["Laura"].Schedule[9] = _return   
                            
                        "On dates you should wear. . . (locked)" if Cnt < 2:
                            pass  
                        "On dates you should wear. . ." if Cnt >= 2:
                            call Laura_Clothes_ScheduleB
                            $ newgirl["Laura"].Schedule[7] = _return     
                        "Back":
                            pass         
                    
                "Never mind":
                    return        
        jump Laura_Clothes_Schedule
    
    
    
label Laura_Clothes_ScheduleB(Count = 0):
#This is called by Laura_Clothes_Schedule when setting her outfit for a given day
#If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes
            
            menu:
                "That leather combat look.":
                    $ Count = 1
                "Your jacket and skirt.":
                    $ Count = 2
                "That outfit we put together [[custom]" if newgirl["Laura"].Custom[0] or newgirl["Laura"].Custom2[0] or newgirl["Laura"].Custom3[0]:
                            menu:
                                ch_l "Which one?"
                                "The first one. (locked)" if not newgirl["Laura"].Custom[0]:
                                    pass
                                "The first one." if newgirl["Laura"].Custom[0]:
                                    if newgirl["Laura"].Custom[0] == 2 or Count == 99:
                                        $ Count = 3
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The second one. (locked)" if not newgirl["Laura"].Custom2[0]:
                                    pass
                                "The second one." if newgirl["Laura"].Custom2[0]:
                                    if newgirl["Laura"].Custom2[0] == 2 or Count == 99:
                                        $ Count = 5
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "The third one. (locked)" if not newgirl["Laura"].Custom3[0]:
                                    pass
                                "The third one." if newgirl["Laura"].Custom3[0]:
                                    if newgirl["Laura"].Custom3[0] == 2 or Count == 99:
                                        $ Count = 6
                                    else:
                                        ch_l "I told you I wouldn't wear that out."
                                        
                                "Never mind":
                                    pass
                "Your gym clothes.":
                    $ Count = 4                
                "Your sleepwear.":
                    if Count != 99:
                        ch_l "That's kinda skimpy, [newgirl[Laura].Petname]."
                        $ Count = 0
                    else:
                        $ Count = 7
                "Whatever you like.":
                    pass
                    
            if Count:
                        ch_l "Ok, sure."
            else:
                        ch_l "I'll figure something else out."
            return Count    
#End Laura Clothes Scheduling Check


label Laura_AltClothes(Outfit=8):
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        
        if newgirl["Laura"].Schedule[Outfit] == 1 or not newgirl["Laura"].Schedule[Outfit]:
                    $ newgirl["Laura"].Outfit = "pink outfit"
        elif newgirl["Laura"].Schedule[Outfit] == 2:
                    $ newgirl["Laura"].Outfit = "red outfit"
        elif newgirl["Laura"].Schedule[Outfit] == 3:
                    $ newgirl["Laura"].Outfit = "custom1"
        elif newgirl["Laura"].Schedule[Outfit] == 5:
                    $ newgirl["Laura"].Outfit = "custom2"
        elif newgirl["Laura"].Schedule[Outfit] == 6:
                    $ newgirl["Laura"].Outfit = "custom3"
        elif newgirl["Laura"].Schedule[Outfit] == 7:
                    $ newgirl["Laura"].Outfit = "sleep"
        elif newgirl["Laura"].Schedule[Outfit] == 4:
                    $ newgirl["Laura"].Outfit = "gym"
        return
  
label Laura_Private_Outfit:
    #sets Laura's private outfit in private
    if "comfy" in newgirl["Laura"].RecentActions or "comfy" in newgirl["Laura"].Traits:
            call Laura_AltClothes(9)
            call LauraOutfit(Changed=1)
    elif "no comfy" in newgirl["Laura"].RecentActions:
            pass        
    elif (2 * newgirl["Laura"].Inbt) >= (newgirl["Laura"].Love + newgirl["Laura"].Obed +100):
            # if her inhibition is much higher than her obedience to you. . .            
            ch_l "One minute. . ."
            ch_l "I'm getting a bit more comfortable."
            call Laura_AltClothes(9)
            call LauraOutfit(Changed=1)
            $ newgirl["Laura"].RecentActions.append("comfy")
    else:           
            ch_l "One minute. . ."
            menu: 
                ch_l "I could throw on something a bit more fun. . ."
                "Sure.":
                    ch_l "Cool. . ."
                    call Laura_AltClothes(9)
                    call LauraOutfit(Changed=1)
                    $ newgirl["Laura"].RecentActions.append("comfy")
                "No thanks.":
                    ch_l "Oh, ok."       
                    $ newgirl["Laura"].RecentActions.append("no comfy")             
    return

label Laura_Custom_Out(Custom = 3, Shame = 0, Agree = 1):
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6
            
            call LauraFace("sexy", 1)
            if "exhibitionist" in newgirl["Laura"].Traits:  
                        ch_l "Mmmmmm. . ."  
                        if Custom == 5 and newgirl["Laura"].Custom2[0] == 2:
                            $ newgirl["Laura"].Outfit = "custom2"                    
                            $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[5]
                        elif Custom == 6 and newgirl["Laura"].Custom3[0] == 2:
                            $ newgirl["Laura"].Outfit = "custom3"                    
                            $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[6]
                        else: #if custom 1:
                            $ newgirl["Laura"].Outfit = "custom1"                    
                            $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[3]            
                        return    
            
            if Custom == 5 and newgirl["Laura"].Custom2[0] == 2:
                        $ newgirl["Laura"].Outfit = "custom2"   
            elif Custom == 6 and newgirl["Laura"].Custom3[0] == 2:
                        $ newgirl["Laura"].Outfit = "custom3"   
            elif newgirl["Laura"].Custom[0] == 2: #if custom 1:
                        $ newgirl["Laura"].Outfit = "custom1"   
            else: #no
                        $ Agree = 0
             
            if Agree:                              
                        #she's decided to wear this out.
                        $ newgirl["Laura"].Shame = newgirl["Laura"].OutfitShame[Custom]          
                        if newgirl["Laura"].OutfitShame[Custom] >= 50:
                            ch_l "This is. . . really brave. . ."
                        elif newgirl["Laura"].OutfitShame[Custom] >= 25:
                            ch_l "This one's pretty skimpy. . ."
                        elif newgirl["Laura"].OutfitShame[Custom] >= 15:
                            call LauraFace("bemused", 1)
                            ch_l "Yeah, ok. . ."
                        else:
                            ch_l "Yup."
            else:
                        #She's decided not to wear this out
                        if newgirl["Laura"].OutfitShame[Custom] >= 50:
                            call LauraFace("angry", 1)
                            ch_l "Perv."
                        elif newgirl["Laura"].OutfitShame[Custom] >= 25:
                            call LauraFace("angry", 1)
                            ch_l "Yeah, not in public."
                        else:
                            call LauraFace("surprised", 1)
                            ch_l "Nah."  
            return
# End Laura Custom Out
                                
                                
label Laura_OutfitShame(Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):                                                                             #sets custom outfit    
            #Custom determines which custom outfit is being checked against.    
            #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 7, if private = 9
            #if not a check, then it is only applied if it's in a taboo area
            # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
            
            if not Check and not Taboo and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if newgirl["Laura"].Schedule[9]:
                    #if there is a "private outfit" set, ask to change.
                    call Laura_Private_Outfit
                return
                        
            #If she's wearing a bra of some kind
            if newgirl["Laura"].Chest == "leather bra":  
                $ Count = 20
#            elif newgirl["Laura"].Chest == "sports bra":
#                $ Count = 15
            elif newgirl["Laura"].Chest == "wolvie top":
                $ Count = 10   
            elif newgirl["Laura"].Chest == "corset":
                $ Count = 5
            else:     #newgirl["Laura"].Chest == 0
                if newgirl["Laura"].Pierce:
                    $ Count = -5
                else:
                    $ Count = 0
                    
            #If she's wearing an overshirt
            if newgirl["Laura"].Over == "jacket":                                             
                $ Count += 10
#            elif newgirl["Laura"].Over == "red shirt":      
#                $ Count += 20
            elif newgirl["Laura"].Over == "towel":      
                $ Count += 10
            #else: nothing    
            
            call LauraFace("sexy", 0)
            if Custom == 9:
                pass
            elif Count >= 20:
                $ Count = 20
                if Check:
                    ch_l "This top works."
            elif not Check:
                pass
            elif Count >= 10 and (ApprovalCheck("Laura", 1200, TabM=0) or ApprovalCheck("Laura", 500, "I", TabM=0)):  
                ch_l "This top works."     
            elif Count >= 10:
                ch_l "The top's not really a good look."
            elif Count >= 5 and (ApprovalCheck("Laura", 2300, TabM=0) or ApprovalCheck("Laura", 800, "I", TabM=0)):  
                ch_l "I don't know, the top's a little light."
            elif Count >= 5:        
                call LauraFace("startled", 1)
                ch_l "I can't really wear this top out."
            elif (ApprovalCheck("Laura", 2700, TabM=0) or ApprovalCheck("Laura", 950, "I", TabM=0)):  
                ch_l ". . ."        
            else:
                call LauraFace("bemused", 1)
                ch_l "I wouldn't go out with my tits out."
             
            $ Tempshame -= Count                  #Set Outfit shame for the upper half    
            $ Count = 0         
            
            if newgirl["Laura"].Legs and newgirl["Laura"].Panties and newgirl["Laura"].Legs != "mesh pants": 
                        $ Count = 30               
            else: #If she's missing something on her legs    
                        if PantsNum("Laura") >= 5:               #If wearing pants commando
                            $ Count = 25                            
#                        elif newgirl["Laura"].Legs == "shorts":                #If wearing shorts
#                            $ Count = 20  
                        elif newgirl["Laura"].Legs == "skirt":                 #If wearing a skirt commando
                            $ Count = 20        
                        elif newgirl["Laura"].Panties == "wolvie panties":      #If wearing only wolvie panties
                            $ Count = 10
                        elif newgirl["Laura"].Panties == "lace panties":       #If wearing only lace panties
                            $ Count = 5
                        elif newgirl["Laura"].Panties:                         #If wearing only any other panties
                            $ Count = 7
                        #else: 0
                        
                        if newgirl["Laura"].Legs == "mesh pants":
                            $ Count += 5
                        
                        if HoseNum("Laura") >= 10:
                            $ Count = 25 if Count < 25 else Count
                            
                        if newgirl["Laura"].Over == "towel" and Count:         #If wearing a Towel and anything else
                            $ Count = 25
                        elif newgirl["Laura"].Over == "towel":                 #If just wearing a Towel
                            $ Count = 15   
                            
            if not Check:
                        #If this isn't a custom check, skip this dialog stuff
                        pass
            elif Custom == 9:
                        pass
            elif Count >= 20:
                        if PantsNum("Laura") >= 5:
                            ch_l "and these pants work."
                        elif HoseNum("Laura") >= 10:
                            ch_l "and these [newgirl[Laura].Hose] will work fine."
                        elif newgirl["Laura"].Over == "towel":
                            ch_l "The towel's an odd choice. . ."
                        else:
                            ch_l "but there's a draft."
                        if not newgirl["Laura"].Panties and ApprovalCheck("Laura", 500, "I", TabM=0):
                            ch_l "Commando's cool."           
                        elif not newgirl["Laura"].Panties:
                            ch_l "I might accidentally flash some people like this though."
                    
            elif Count >= 10 and (ApprovalCheck("Laura", 2000, TabM=0) or ApprovalCheck("Laura", 700, "I", TabM=0)):
                    ch_l "I don't think I'm fully covered. . ."        
            elif Count >= 10:
                    call LauraFace("angry", 1)
                    ch_l "I'm not covered like this. . ."                
            elif (ApprovalCheck("Laura", 2500, TabM=0) or ApprovalCheck("Laura", 800, "I", TabM=0)):  
                    ch_l "It's pretty minimal. . ."        
            else:
                    ch_l "I wouldn't show off my cooch either. . ."
                
            $ Tempshame -= Count                  #Set Outfit shame for the lower half
            
            if Check:
                    #if this is a custom outfit check
                    if Custom == 7:
                        ch_p "So would you work out in that?"
                    elif Custom == 9:
                        ch_p "So would you sleep in that?"
                    else:
                        ch_p "So would you wear that outside?"  
                        
                    call LauraFace("sexy", 0)
                    if Taboo >= 40: #newgirl["Laura"].Loc != "bg player" and newgirl["Laura"].Loc != "bg laura": 
                        call LauraFace("confused",1)
                        $ newgirl["Laura"].Mouth = "smile"
                        ch_l "Well a bit late for that, I guess." 
                    elif "exhibitionist" in newgirl["Laura"].Traits and Tempshame <= 20: 
                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10) 
                        call LauraFace("sexy", 2)      
                        ch_l ". . ."
                        call LauraFace("sexy", 1)      
                    elif Tempshame <= 5:
                        call LauraFace("smile")
                        ch_l "I don't see why not."
                    elif Tempshame <= 15 and (ApprovalCheck("Laura", 1700, TabM=0, C = 0) or ApprovalCheck("Laura", 400, "I", TabM=0, C = 0)):        
                        ch_l "It looks good, right?"
                    elif Custom == 9:
                        #if it's sleepwear      
                        call LauraFace("bemused", 1)
                        if Tempshame >= 30:
                            ch_l "Sure, perv."   
                        elif Tempshame >= 15:
                            ch_l "Sure, why not."  
                        else:
                            ch_l "Yeah, I guess."                       
                    elif Tempshame <= 15:  
                        call LauraFace("bemused", 1)
                        ch_l "I can't move freely in this without showing off the goods."
                        $ Agree = 0
                    elif Tempshame <= 25 and (ApprovalCheck("Laura", 2300, TabM=0, C = 0) or ApprovalCheck("Laura", 700, "I", TabM=0, C = 0)):
                        ch_l "I can handle this."
                    elif Tempshame <= 25:
                        call LauraFace("angry", 1)
                        ch_l "Nah, too slutty."
                        $ Agree = 0
                    elif (ApprovalCheck("Laura", 2500, TabM=0, C = 0) or ApprovalCheck("Laura", 800, "I", TabM=0, C = 0)):
                        call LauraFace("bemused", 1)
                        ch_l "Pretty daring, eh?"
                    else:
                        call LauraFace("angry", 1)
                        ch_l "As if."
                        $ Agree = 0
                        
                    $ newgirl["Laura"].OutfitShame[Custom] = Tempshame                     
                    if Custom == 5:
                            $ newgirl["Laura"].Custom2[1] = newgirl["Laura"].Arms  
                            $ newgirl["Laura"].Custom2[2] = newgirl["Laura"].Legs 
                            $ newgirl["Laura"].Custom2[3] = newgirl["Laura"].Over
                            $ newgirl["Laura"].Custom2[4] = newgirl["Laura"].Neck 
                            $ newgirl["Laura"].Custom2[5] = newgirl["Laura"].Chest 
                            $ newgirl["Laura"].Custom2[6] = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Custom2[8] = newgirl["Laura"].Hair
                            $ newgirl["Laura"].Custom2[9] = newgirl["Laura"].Hose
                            $ newgirl["Laura"].Custom2[0] = 2 if Agree else 1           
                    elif Custom == 6:
                            $ newgirl["Laura"].Custom3[1] = newgirl["Laura"].Arms  
                            $ newgirl["Laura"].Custom3[2] = newgirl["Laura"].Legs 
                            $ newgirl["Laura"].Custom3[3] = newgirl["Laura"].Over
                            $ newgirl["Laura"].Custom3[4] = newgirl["Laura"].Neck 
                            $ newgirl["Laura"].Custom3[5] = newgirl["Laura"].Chest 
                            $ newgirl["Laura"].Custom3[6] = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Custom3[8] = newgirl["Laura"].Hair
                            $ newgirl["Laura"].Custom3[9] = newgirl["Laura"].Hose
                            $ newgirl["Laura"].Custom3[0] = 2 if Agree else 1
                    elif Custom == 7 and Agree:
                            $ newgirl["Laura"].Gym[1] = newgirl["Laura"].Arms  
                            $ newgirl["Laura"].Gym[2] = newgirl["Laura"].Legs 
                            $ newgirl["Laura"].Gym[3] = newgirl["Laura"].Over
                            $ newgirl["Laura"].Gym[4] = newgirl["Laura"].Neck 
                            $ newgirl["Laura"].Gym[5] = newgirl["Laura"].Chest 
                            $ newgirl["Laura"].Gym[6] = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Gym[8] = newgirl["Laura"].Hair
                            $ newgirl["Laura"].Gym[9] = newgirl["Laura"].Hose
                            $ newgirl["Laura"].Gym[0] = 2   
                    elif Custom == 9:                            
                            $ newgirl["Laura"].Sleepwear[1] = newgirl["Laura"].Arms  
                            $ newgirl["Laura"].Sleepwear[2] = newgirl["Laura"].Legs 
                            $ newgirl["Laura"].Sleepwear[3] = newgirl["Laura"].Over
                            $ newgirl["Laura"].Sleepwear[4] = newgirl["Laura"].Neck 
                            $ newgirl["Laura"].Sleepwear[5] = newgirl["Laura"].Chest 
                            $ newgirl["Laura"].Sleepwear[6] = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Sleepwear[8] = newgirl["Laura"].Hair
                            $ newgirl["Laura"].Sleepwear[9] = newgirl["Laura"].Hose
                            $ newgirl["Laura"].Sleepwear[0] = 2 if Agree else 1   
                    else: #Typically Custom == 3
                            $ newgirl["Laura"].Custom[1] = newgirl["Laura"].Arms  
                            $ newgirl["Laura"].Custom[2] = newgirl["Laura"].Legs 
                            $ newgirl["Laura"].Custom[3] = newgirl["Laura"].Over
                            $ newgirl["Laura"].Custom[4] = newgirl["Laura"].Neck 
                            $ newgirl["Laura"].Custom[5] = newgirl["Laura"].Chest 
                            $ newgirl["Laura"].Custom[6] = newgirl["Laura"].Panties
                            $ newgirl["Laura"].Custom[8] = newgirl["Laura"].Hair
                            $ newgirl["Laura"].Custom[9] = newgirl["Laura"].Hose
                            $ newgirl["Laura"].Custom[0] = 2 if Agree else 1
                    #End check                       
            elif Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2
                
            $ newgirl["Laura"].Shame = Tempshame
            
            if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return
                
            if Check:
                    pass
            elif "exhibitionist" in newgirl["Laura"].Traits: 
                    #If she's an exhibitionist
                    pass
            elif Tempshame <= 5:
                    #If the outfit is very tame
                    pass
            elif newgirl["Laura"].Over == "towel" and newgirl["Laura"].Loc == "bg showerroom": 
                    #If she's in a towel but it's appropriate
                    pass
            elif Tempshame <= 15 and (ApprovalCheck("Laura", 1700) or ApprovalCheck("Laura", 600, "I")):
                    #If the outfit is hot but she's ok     
                    pass
            elif Tempshame <= 20 and newgirl["Laura"].Loc == "bg dangerroom": 
                    #If the outfit is light but she's in the gym
                    pass
            elif Tempshame <= 20 and (ApprovalCheck("Laura", 1800) or ApprovalCheck("Laura", 650, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif Tempshame <= 25 and (ApprovalCheck("Laura", 2300) or ApprovalCheck("Laura", 800, "I")):
                    #If the outfit is sexy but she's cool with that
                    pass
            elif (ApprovalCheck("Laura", 2600) or ApprovalCheck("Laura", 950, "I")):
                    #If the outfit is very scandelous but she's ok with that      
                    pass
            elif Custom == 9 and not Taboo:
                    pass
            else:
                    ch_l "One sec, I gotta change real quick."
                    $ newgirl["Laura"].Outfit = renpy.random.choice(["mission", "streets"])
                    $ newgirl["Laura"].Water = 0
                    call LauraOutfit(Changed = 1) 
                    ch_l "That's not really outdoors wear."
                    
            return        

#End Laura Custom clothes check.
    
# start laura hungry //////////////////////////////////////////////////////////
label Laura_Hungry:
    if newgirl["Laura"].Chat[3]:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    elif newgirl["Laura"].Chat[2]:
        ch_l "I really enjoy that serum you whipped up."
    else:
        ch_l "[[licks her lips] I'm a little thirsty. . ."
    $ newgirl["Laura"].Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

    
# Start Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_First_Les(Silent = 0, Undress = 0, GirlsNum = 0): #checked when she engages in a les scene  ## call Laura_First_Les(0,1)
    if newgirl["Laura"].Les:
        return
    
    $ newgirl["Laura"].Les += 1
    $ newgirl["Laura"].RecentActions.append("lesbian")        
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2) 
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 1)
    
    if not Silent: 
        #example previous line: Line + " and cups " + Primary + "'s breasts in her delicate hands" 
        "Laura's head jerks up and she looks at what [Partner] is doing. [Partner] pauses and glances up at her with a mischievous grin." 
        ch_l "I, um, I haven't done that sort of thing before."
        if Partner == "Rogue":
                if R_Les:
                    ch_r "Neither have I Sugar, but it seemed like fun."
                else:
                    ch_r "It's all right Sugar, I'll take care of you."
        if newgirl["Laura"].LikeRogue >= 60 and ApprovalCheck("Laura", (1500-(10*newgirl["Laura"].Les)-(10*(newgirl["Laura"].LikeRogue-60)))): #If she likes both of you a lot, threeway
                $ State = "threeway"
        elif ApprovalCheck("Laura", 1000): #If she likes you well enough, Hetero
                $ State = "hetero"            
        elif newgirl["Laura"].LikeRogue >= 70: #if she doesn't like you but likes Rogue, lesbian
                $ State = "lesbian"
        
        
        
        
        
        if "cockout" in P_RecentActions:
                call LauraFace("down", 2)  
                if GirlsNum:
                    "Laura also glances down at your cock"
                else:
                    "Laura glances down at your exposed cock"
        elif Undress:
                "You strip nude."
        else:
                "You whip your cock out."
        $ P_RecentActions.append("cockout") 
        
        if Taboo and not ApprovalCheck("Laura", 1500):
                call LauraFace("surprised", 2)  
                ch_l "Um, you should[newgirl[Laura].like]put that away in public."
                call LauraFace("bemused", 1)  
                if newgirl["Laura"].SeenPeen == 1: 
                    ch_l "Or[newgirl[Laura].like]maybe. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 15)                
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 20)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 35)  
                    
        elif newgirl["Laura"].SeenPeen > 10:
                return    
        elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                call LauraFace("sly",1) 
                if newgirl["Laura"].SeenPeen == 1: 
                    call LauraFace("surprised",2)  
                    ch_l "That's. . . impressive."
                    call LauraFace("bemused",1)  
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3) 
                elif newgirl["Laura"].SeenPeen == 2:  
                    ch_l "I can't get over that."               
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7) 
                elif newgirl["Laura"].SeenPeen == 5: 
                    ch_l "There it is."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)  
                elif newgirl["Laura"].SeenPeen == 10: 
                    ch_l "So beautiful."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 10)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
        else:
                call LauraFace("sad",1) 
                if newgirl["Laura"].SeenPeen == 1: 
                    call LauraFace("perplexed",1 ) 
                    ch_l "Well that happened. . ."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                elif newgirl["Laura"].SeenPeen < 5: 
                    call LauraFace("sad",0) 
                    ch_l "Huh."
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)  
                elif newgirl["Laura"].SeenPeen == 10: 
                    ch_l "[newgirl[Laura].Like]put that away."               
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
    
    else: #Silent mode
                $ P_RecentActions.append("cockout") 
                if newgirl["Laura"].SeenPeen > 10:
                    return
                elif ApprovalCheck("Laura", 1200) or ApprovalCheck("Laura", 500, "L"):
                        if newgirl["Laura"].SeenPeen == 1: 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 3) 
                        elif newgirl["Laura"].SeenPeen == 2:              
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7) 
                        elif newgirl["Laura"].SeenPeen == 5: 
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 5)  
                        elif newgirl["Laura"].SeenPeen == 10: 
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)  
                else:
                        if newgirl["Laura"].SeenPeen == 1: 
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                        elif newgirl["Laura"].SeenPeen < 5: 
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)  
                        elif newgirl["Laura"].SeenPeen == 10:              
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 7)
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3) 
                            
    if newgirl["Laura"].SeenPeen == 1:            
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)                
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 25)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 20) 
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5)
    
    return
# End Laura first Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    