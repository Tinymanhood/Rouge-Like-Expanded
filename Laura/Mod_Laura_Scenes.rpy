
# start LauraMeet//////////////////////////////////////////////////////////


label LauraMeet(Topics=[],Loop=1):
    $ newgirl["Laura"].Pubes = 1
    
    $ newgirl["Laura"].GirlName = "???"
    
    $ bg_current = "bg dangerroom"   
    call CleartheRoom("All",0,1)
    $ newgirl["Laura"].Loc = "bg dangerroom"  
    $ newgirl["Laura"].Love = 400        
    $ newgirl["Laura"].Obed = 0            
    $ newgirl["Laura"].Inbt = 200  
    call Shift_Focus("Laura")    
    $ newgirl["Laura"].SpriteLoc = StageCenter
    call Set_The_Scene(0)
    $ newgirl["Laura"].Petname = Playername   
    
    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."   
    call LauraFace("normal", 0) 
    show Laura_Sprite at SpriteLoc(newgirl["Laura"].SpriteLoc)
    "When you come to, a girl pulls you up by your arm."     
    call LauraFace("surprised", 0, Eyes="squint",Brows="sad") 
    ch_u "Oh, good, you don't look too damaged." 
    call LauraFace("smile", 0, Brows="sad") 
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door." 
    call LauraFace("smile", 0) 
    while Loop:
        menu:
            extend ""
            "Who are you?" if newgirl["Laura"].GirlName == "???":
                    call LauraFace("normal", 0) 
                    ch_l "I go by \"X-23\" in the field."
                    $ newgirl["Laura"].GirlName = "X-23"        
            "X-23? Is that your real name?" if newgirl["Laura"].GirlName == "X-23" and "X23" not in Topics:
                    call LauraFace("confused", 0) 
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and "Laura" not in Topics:
                    call Statup("Laura", "Love", 70, 5) # Love
                    call LauraFace("normal", 0) 
                    ch_l "I also go by Laura. Laura Kinney."
                    call LauraFace("confused", 0, Mouth="normal") 
                    $ newgirl["Laura"].GirlName = "Laura"       
                    $ Topics.append("Laura")    
                    menu:
                        extend ""
                        "Nice to meet you Laura.": 
                            call Statup("Laura", "Love", 70, 5) # Love  
                            call LauraFace("normal", 0)                
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            call LauraFace("confused", 0,Mouth="sucking")   
                            ch_l "It's just-"
                            call LauraFace("smile", 0,Brows="surprised")   
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Inbt", 70, 2) # Inbt   
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            call LauraFace("angry", 1,Eyes="side") 
                            call Statup("Laura", "Love", 70, -2) # Love   
                            call Statup("Laura", "Obed", 70, 2) # Obed 
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if newgirl["Laura"].GirlName == "Laura" and "Laura" in Topics:
                    call Statup("Laura", "Love", 70, -2) # Love   
                    call Statup("Laura", "Obed", 70, 5) # Obed 
                    call LauraFace("sadside", 0,Brows="normal") 
                    ch_l "Suit yourself."
                    $ newgirl["Laura"].GirlName = "X-23"     
            "My name is [Playername]" if newgirl["Laura"].GirlName != "???" and "player" not in Topics:
                    call LauraFace("normal", 0) 
                    ch_l "Ok."     
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            call Statup("Laura", "Love", 70, 1) # Love 
                            call LauraFace("confused", 0,Mouth="normal")   
                            ch_l "Yeah, you too." 
                        "So. . .[[moving on]":
                            call Statup("Laura", "Love", 70, 3) # Love   
                            call Statup("Laura", "Obed", 70, 1) # Obed
                            call Statup("Laura", "Inbt", 70, 1) # Inbt  
                            
            "What are you doing here?" if "Training" not in Topics:
                    call Statup("Laura", "Obed", 70, -2) # Obed
                    call LauraFace("confused", 0) 
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                call Statup("Laura", "Obed", 70, 2) # Obed 
                        "Ok, that's fair.":
                                call LauraFace("normal", 0) 
                                ch_p "But are you new to this school?"
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 4) # Obed
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."   
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:  
                    call Statup("Laura", "Love", 70, 2) # Love   
                    call LauraFace("normal", 0,Eyes="side") 
                    ch_l "I'll be heading out again soon." 
                    call LauraFace("normal", 0) 
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")
                
                        
            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    call Statup("Laura", "Love", 70, -2) # Love   
                    call Statup("Laura", "Obed", 70, 8) # Obed  
                    call LauraFace("confused", 0) 
                    ch_l "It was a robot arm." 
                    call LauraFace("sad", 1,Eyes="leftside") 
                    ch_l "Like I said, sorry."                   
                    call Statup("Laura", "Obed", 70, -3) # Obed
                    call Statup("Laura", "Inbt", 70, 3) # Inbt  
                    call LauraFace("smile", 0,Brows="confused") 
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")
                
            "So what's your mutant power?" if newgirl["Laura"].GirlName != "???" and "claws" not in Topics:
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 1) # Obed                    
                    call LauraFace("normal", 0) 
                    ch_l "I can heal fast."
                    $ newgirl["Laura"].Girl_Arms = 2
                    ch_l "Also I have claws."
                    $ newgirl["Laura"].Claws = 1
                    call LauraFace("smile", 0,Brows="confused") 
                    "snikt"
                    $ Topics.append("claws")
                    menu:                        
                        "Those claws look pretty sharp.":
                                call Statup("Laura", "Inbt", 70, 3) # Inbt   
                                ch_l "Yeah, indestructible too." 
                        "Cool.":
                                call Statup("Laura", "Love", 70, 3) # Love   
                                call Statup("Laura", "Obed", 70, 2) # Obed
                                call Statup("Laura", "Inbt", 70, 1) # Inbt   
                                call LauraFace("smile", 0,Brows="surprised") 
                                ch_l "Yeah, indestructible too." 
                        "Ouch.": 
                                $ newgirl["Laura"].Claws = 0
                                call LauraFace("confused", 0) 
                                call Statup("Laura", "Love", 70, -2) # Love   
                                call Statup("Laura", "Obed", 70, -5) # Obed  
                                ch_l "Don't worry, I won't stab you." 
                                call LauraFace("confused", 0,Mouth="normal")      
                                call Statup("Laura", "Inbt", 70, 7) # Inbt   
                                ch_l "Probably."  
                    $ newgirl["Laura"].Claws = 0
                    $ newgirl["Laura"].Girl_Arms = 1
                            
            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if newgirl["Laura"].Love >= 405: 
                            call LauraFace("smile", 0,Brows="confused") 
                            ch_l "Yeah, I guess."
                    else:
                            call LauraFace("normal", 0) 
                            ch_l "Not really."
                    call Statup("Laura", "Inbt", 70, 3) # Inbt   
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off." 
                    call LauraFace("smile", 0,Brows="confused") 
                    call Statup("Laura", "Love", 70, 3) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed  
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."  
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust   
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 2) # Obed 
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    call LauraFace("confused", 0) 
                    ch_l "Huh." 
                    call LauraFace("sexy", 1,Eyes="closed") 
                    "You can feel her shudder a little." 
                    call LauraFace("sexy", 1) 
                    call Statup("Laura", "Love", 70, 1) # Love   
                    call Statup("Laura", "Obed", 70, 3) # Obed
                    call Statup("Laura", "Lust", 70, 5) # Lust  
                    ch_l "That feels weird."  
                    call LauraFace("sexy", 1,Eyes="leftside") 
                    call Statup("Laura", "Obed", 70, 1) # Obed 
                    call Statup("Laura", "Lust", 70, 3) # Lust  
                    ch_l "-a little more \"alive\" than usual." 
                    call Statup("Laura", "Inbt", 70, 5) # Inbt  
                    call Statup("Laura", "Lust", 70, 5) # Lust 
                    call LauraFace("sexy", 1,Brows="confused")   
                    ch_l "Almost. . . dangerous."
                
            "Never mind that. . . [[moving on]" if newgirl["Laura"].GirlName != "???":
                    $ Loop = 0
            
        if len(Topics) >= 3 and newgirl["Laura"].GirlName == "???":
                call Statup("Laura", "Love", 70, -2) # Love   
                call Statup("Laura", "Obed", 70, 5) # Obed
                call Statup("Laura", "Inbt", 70, 5) # Inbt   
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ newgirl["Laura"].GirlName = "X-23"  
        if len(Topics) >= 8:
                $ Loop = 0
        
        
    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            call Statup("Laura", "Love", 70, 2) # Love   
            call Statup("Laura", "Lust", 70, 1) # Lust  
            call LauraFace("smile",0) 
            ch_l "Maybe I'll see you when I get back, [Playername]."
    else:
            call LauraFace("normal", 0) 
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            call Statup("Laura", "Obed", 70, 2) # Obed
            call Statup("Laura", "Inbt", 70, 2) # Inbt  
            call Statup("Laura", "Lust", 70, 3) # Lust   
            call LauraFace("smile", 1, Brows="confused") 
            ch_l "We should. . . spar."
         
    $ newgirl["Laura"].Loc = "bg laura"         
    call Set_The_Scene
    
    "She dashes out of the room, headed for the hanger."
    
    $ newgirl["Laura"].History.append("met")
    $ bg_current = "bg dangerroom"            
    $ Round -= 10      
    call Shift_Focus("Rogue")
    return

# end LauraMeet//////////////////////////////////////////////////////////

                       
label Laura_Key:
        call Set_The_Scene
        call LauraFace("bemused")
        ch_l "Hey, so... this isn't something I usually do but..."
        ch_l "Look, you've been sleeping over a lot and I was thinking..."
        ch_l "Just take it already."
        "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
        $ Keys.append("Laura")
        $ newgirl["Laura"].Event[0] = 1
        ch_p "Thanks."
        return
        


# Event Laura_Caught_Masturbating  /////////////////////////////////////////////////////  

#Not updated

label Laura_Caught_Masturbating:
            #This label is called from a Location
            call Shift_Focus("Laura")
            "You hear some odd noises coming from Laura's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call LauraOutfit(Changed=1)    
            $ newgirl["Laura"].Upskirt = 1
            $ newgirl["Laura"].PantiesDown = 1
            $ newgirl["Laura"].Loc = bg_current
            call Set_The_Scene(0)
            call Display_Laura(0)
            call LauraFace("sexy")
            $ newgirl["Laura"].Eyes = "closed"
            $ newgirl["Laura"].Girl_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ newgirl["Laura"].DailyActions.append("unseen")
            $ newgirl["Laura"].RecentActions.append("unseen")    
            call Laura_SexAct("masturbate")
            if "angry" in newgirl["Laura"].RecentActions:
                return
        
#After caught masturbating. . .
            $ newgirl["Laura"].Eyes = "sexy"
            $ newgirl["Laura"].Brows = "confused"
            $ newgirl["Laura"].Mouth = "smile"
            if newgirl["Laura"].Mast == 1:        
                    $ newgirl["Laura"].Mouth = "kiss"
                    ch_l "So what are you doing here? . ."
                    $ newgirl["Laura"].Eyes = "side"
                    $ newgirl["Laura"].Mouth = "lipbite"        
                    ch_l "not that I mind the company. . ."
                    $ newgirl["Laura"].Eyes = "sexy"
                    $ newgirl["Laura"].Brows = "normal"         
                    $ newgirl["Laura"].Mouth = "smile"
                    ch_l "But you know, give me a heads up first." 
            else:
                    ch_l "You're around a lot. . ."            
            $ newgirl["Laura"].Girl_Arms = 1  
            call LauraOutfit      
            return
    
# end Laura_Caught_Masturbating/////////////////////////////////////////////////////


# Event Laura_Caught /////////////////////////////////////////////////////  

#Not updated

label Laura_Caught(TotalCaught=0):
    $ TotalCaught = R_Caught + K_Caught + E_Caught + newgirl["Laura"].Caught
    call Shift_Focus("Laura")
    call Checkout
    ch_l "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call LauraOutfit
    if R_Loc == bg_current:         
        $ R_Loc = "bg study"
    if K_Loc == bg_current:                
        $ K_Loc = "bg study" 
    if E_Loc == bg_current:                
        $ E_Loc = "bg study"        
    $ bg_current = "bg study"  
    $ newgirl["Laura"].Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    show Laura_Sprite at SpriteLoc(StageRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if E_Loc == bg_current:         
        show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call LauraFace("sad")
    ch_x "I'm very disappointed in your behavior, the both of you."
    
    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"
    
    if newgirl["Laura"].Shame >= 40:
        ch_x "Laura, my dear, you're practically naked! At least throw a towel on!"
        "He throws Laura the towel."
        show blackscreen onlayer black 
        $ newgirl["Laura"].Over = "towel"         
        hide blackscreen onlayer black
    elif newgirl["Laura"].Shame >= 20:
        ch_x "Laura, my dear, that attire is positively scandalous."
    
    if newgirl["Laura"].Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        if "Rogue" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1, Eyes="side")
    elif K_Loc == bg_current:             #fix, might not currently work?
        call KittyFace("surprised",2)
        if "Kitty" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Kitty, you were just watching this occur!"        
        call KittyFace("bemused",1,Eyes="side")
    elif E_Loc == bg_current:             #fix, might not currently work?
        call EmmaFace("surprised",2)
        if "Emma" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Emma, you were just watching this occur!" 
            ch_x "Unacceptable. . ."        
        call EmmaFace("bemused",1, Eyes="side")
        
    if "rules" in Rules: #if the rules had been removed in a previous game
            call XavierFace("hypno")
            ch_x ". . ."
            ch_x "Hmm, I seem to be having a bit of deja vu here. . ."
            ch_x "I could swear that we've had a conversation like this before, but I cannot recall when. . ."
            call XavierFace("angry")
            ch_x "Regardless, this is a serious issue."
            $ Rules.remove("rules")
            
    $ Count = newgirl["Laura"].Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if newgirl["Laura"].Caught < 5:
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, -20)            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -10) 
            call XavierFace("happy")  
            if newgirl["Laura"].Caught:
                ch_x "But you know you've done this before. . . at least [newgirl[Laura].Caught] times. . ." 
            elif TotalCaught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [newgirl[Laura].Pet]?":
            call Laura_Namecheck
            call LauraFace("bemused")         
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
            if newgirl["Laura"].Caught < 5:            
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 10)   
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."    
            if newgirl["Laura"].Caught < 5:            
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 20)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 20)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Chi, Laura!" if P_Lvl >= 5:
            if newgirl["Laura"].Lvl >= 5 and ApprovalCheck("Laura", 1500, TabM=1, Loc="No") and ApprovalCheck("Laura", 750, "I"):                   
                    jump Plan_Chi
            elif ApprovalCheck("Laura", 1000, TabM=1, Loc="No"):
                    call LauraFace("angry",Eyes="side") 
                    $ newgirl["Laura"].Brows = "angry"
                    ch_l "I told you that was a stupid idea. . ."
                    menu:
                        "Dammit Laura. . .":
                                call LauraFace("angry")
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 5)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call LauraFace("bemused") 
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5) 
            else:
                    call LauraFace("confused") 
                    ch_l "Yeah!"
                    ch_l ". . ."
                    ch_l "Wait, plan \"key,\" what??"
                    ch_p "Plan {i}Chi!{/i} . . you know. . ."
                    ch_l "Um. No?"
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call LauraFace("bemused") 
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."  
            if newgirl["Laura"].Caught < 5:              
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 10)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 10)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, -10)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call LauraFace("surprised")
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 10)
            if newgirl["Laura"].Caught < 5:
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 25)
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if newgirl["Laura"].Caught < 5:
                if newgirl["Laura"].Inbt > 50:
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 15)             
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, -15)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, -10)    
            ch_x "Now get out of my sight."
    
    if "Xavier's photo" not in P_Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            "There probably isn't a way available right now though. . ."
#            if newgirl["Laura"].Caught > 1: 
#                "Maybe I should try searching the office when he's not around."
#            if newgirl["Laura"].Caught > 2:
#                "I bet Laura could help me get in."
    $ PunishmentX += Count            
    $ newgirl["Laura"].Caught += 1
    $ newgirl["Laura"].RecentActions.append("caught")
    $ newgirl["Laura"].DailyActions.append("caught") 
    call Remove_Girl("All")  
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Chi:
    call LauraFace("sly")         
    "As you say this, a sly grin crosses Laura's face."
    $ newgirl["Laura"].Girl_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."   
    show Laura_Sprite at SpriteLoc(StageLeft+100,150) with ease
    $ newgirl["Laura"].SpriteLoc = StageCenter
    "Laura moves in sits on his lap, placing one hand on his."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    elif K_Loc == bg_current and "Kappa" not in P_Traits:        
        call KittyFace("surprised")      
        "Kitty looks a bit caught off guard, but goes along with the idea."        
        call KittyFace("sly")
    elif E_Loc == bg_current and "Psi" not in P_Traits:        
        call EmmaFace("surprised")      
        "Emma looks a bit caught off guard, but goes along with the idea."        
        call EmmaFace("sly")
    call XavierFace("angry")
    
    if "Chi" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1)   
    else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "Laura and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [newgirl[Laura].Pet] here has a very particular set of skills, you know. . ."
            call Laura_Namecheck
            $ newgirl["Laura"].Claws = 1
            call LauraFace("sly")     
            ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
            "Laura draws her claws along the arm of the Professor's chair, tracing fine lines into the metal." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 40)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 30)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 30)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_l "Well, [newgirl[Laura].Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if "Laura" not in Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules.append("Laura")
            "You know, it's kinda fun dodging you, catch us if you can." if "Laura" in Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules.remove("Laura")
            "Raise my stipend." if P_Income < 30 and "Chi" not in P_Traits:    
                    ch_x "Very well. . . but I can only raise it by so much. . ."        
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Chi" in P_Traits:           
                    pass
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, take it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Laura's room." if "Laura" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Laura")
                    "Give me the key to Laura's room.[[Owned] (locked)" if "Laura" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conclude our business. Please leave." 
    if "Chi" not in P_Traits:
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 10)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 10)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 10)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, 20)
        $ P_Traits.append("Chi")
    $ newgirl["Laura"].Girl_Arms = 1
    $ newgirl["Laura"].Claws = 0
    "You return to your room"
    jump Player_Room
                              
# end Laura_Caught/////////////////////////////////////////////////////
