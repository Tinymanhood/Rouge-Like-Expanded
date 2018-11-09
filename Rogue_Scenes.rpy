# Prologue //////////////////////////////////////////////////////////////////////

label Prologue:
    $ Day = 1
    $ Time_Count = 2
    $ bg_current = "bg study"    
    scene setting onlayer backdrop 
    "You recently discovered that you were a mutant when a Sentinel attacked your home.\nYou were rescued by a squad of X-Men and given this address."
    "You've arrived in the early evening at the Xavier Institute, where you've been promised a new home."
    "Things have been tough for mutants in the years since Apocalypse's fall, but this sounds like it might be a good deal."
    python:
        Playername = renpy.input("What is your name?", default="Zero", length = 10)
        Playername = Playername.strip()        
        if not Playername:
            Playername = "Zero"
        if Playername in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
            Line = "Nice try, smartass."
            Playername = "Zero"    
    if Line:
        "[Line]"        
    menu:
        "What is your skin color?"        
        "Green":
            $ P_Color = "green"
        "White":
            $ P_Color = "pink"
        "Black":
            $ P_Color = "brown"
    show Professor at SpriteLoc(StageLeft)
    with dissolve
    ch_x "Welcome to the Xavier Institute for Higher Learning. This is a home for all mutants to learn and grow."
    ch_x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    ch_x "I know that you've had a difficult time, but you will be safe here."
    ch_x "You'll have classes in the day to teach you the skills you'll need, and training in the danger room for self defense."
    ch_x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    ch_x "Did you have any questions for me young man?"    
    ch_p "Why did you even bring me here, I don't have any \"super powers.\""
    ch_x "Nonsense, my boy. You have an incredibly useful ability. . ."
    ch_x "the power to negate other powers, even including my own."
    call RogueFace("surprised")
    $ R_SpriteLoc = StageFarRight
    show Rogue at SpriteLoc(R_SpriteLoc)
    with easeinright
    ch_r "What's that Prof? This new kid can negate mutant powers?"    
    $ R_Mouth = "normal"
    $ R_SpriteLoc = StageRight
    show Rogue at SpriteLoc(R_SpriteLoc) with ease
    ch_r "Maybe even my own?"
    ch_x "That is correct, Rogue, though currently, his powers are weak and uncontrolled."
    ch_x "One day, however, he may even be able to help you turn your powers off permanently."
    ch_r "! . . ."
    call RogueFace("smile")
    ch_x "Since you're here, why don't you show our new guest around the mansion?"
    
    ch_x "This young lady is named Rogue, one of our veteran students."
    ch_x "And Rogue, this young man goes by the name \"[Playername]\"."
    
    hide Professor
    with easeoutright
    
    $ R_SpriteLoc = StageCenter
    show Rogue at SpriteLoc(R_SpriteLoc)  
    with ease
    
    menu:
        ch_r "A pleasure ta meet ya, [R_Petname]. Let me give ya the lay of the place." 
        "It's nice to meet you too.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
            call RogueFace("smile", 1)
            ch_r "Oh, a gentleman. I think we'll really get along."                          
            $ R_Blush = 0
            ch_r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
            $ R_Brows = "normal"     
            $ R_Eyes = "surprised"
            $ R_Mouth = "smile"
            $ R_Blush = 1
            ch_r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"
            call RogueFace("bemused")
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
            ch_r "Hmm. . ."           
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 3)
            call RogueFace("normal")
            $ R_Eyes = "surprised"
            ch_r "Anyways, let's get this back on track. . ."
            call RogueFace("smile", 0)
        "Whatever.":            
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
            call RogueFace("sad")
            $ R_Brows = "normal"
            ch_r "Tsk, well ok, let's get started."
        "Screw off.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
            call RogueFace("angry")
            show Rogue at SpriteLoc(R_SpriteLoc)  
            with vpunch
            ch_r "Well I never!"
            ch_r "Hmph, I have to give the tour anyways, so get mov'in. . ."
          
        
# End Prologue //////////////////////////////////////////////////////////////////////

# Tour //////////////////////////////////////////////////////////////////////
label tour_start:
    $ bg_current = "bg campus"    
    call Set_The_Scene(0)
    show Rogue at SpriteLoc(R_SpriteLoc)  
    ch_r "This is the campus square. It links up to all the major locations on campus and you'll probably pass through here a lot."


# Player's room
    $ bg_current = "bg player"    
    call Set_The_Scene(0)
    show Rogue at SpriteLoc(R_SpriteLoc)  
    ch_r "This will be your room, we each get private rooms now that the campus has been expanded."
    menu:
        ch_r "Pretty nice, right?"
        "It is with you in it.":            
            $ R_Blush = 1
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
        "It'll do.":
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 10)
    ch_p "And where do you live?"
    $ R_Blush = 0
    ch_r "Oh, right down the hall, all the doors are labeled."
    if R_Love <= 500:
        ch_r "I wouldn't recommend bothering me though."
    else:
        ch_r "You can stop by sometime, but not after curfew."
    
# Classrooms
    $ bg_current = "bg classroom"    
    call Set_The_Scene(0)
    show Rogue at SpriteLoc(R_SpriteLoc)  
    ch_r "And this is one of our state-of-the-art classrooms. They're multi-purpose so they can teach almost anything in them."
    ch_r "This used to just be an after school training facility, but over the past few years it's grown into a full service university."


# Danger Room
    $ bg_current = "bg dangerroom"   
    call Set_The_Scene(0)
    show Rogue at SpriteLoc(R_SpriteLoc)  
    ch_r "And this is the Danger Room. It's been upgraded to a fully holographic experience, allowing realistic battlefield simulations."
    $ Count = 0
    while Count < 3:
        menu:
            extend ""
            "Why would you need battlefield simulations?" if Count != 1:
                ch_r "The world is a dangerous place, [R_Petname], especially for us mutants."
                ch_r "This place helps us train to use our powers. Coming here can help you to get a grasp on yours as well."
                if Count == 2:
                    $ Count = 3
                else:
                    $ Count = 1
            "So can this place make some more. . . erotic simulations?" if Count != 2:
                $ R_Eyes = "side"
                $ R_Mouth = "lipbite"
                $ R_Blush = 1
                $ R_Inbt= Statupdate("Rogue", "Inbt", R_Inbt, 200, 30)
                $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)
                ch_r "Well. . . I suppose it could. . . if one were into such things."
                call RogueFace (B = 0)
                if Count == 1:
                    $ Count = 3
                else:
                    $ Count = 2
            "Ok, let's move on.":
                $ Count = 3        
    $ Count = 0
    ch_r "Moving on then. . ."

label tour_end: 
    $ bg_current = "bg campus"   
    call Set_The_Scene(0)
    show Rogue at SpriteLoc(R_SpriteLoc)  
    ch_r "Well, that's the nickel tour, now you know where everything is. . ."
    $ R_Mouth = "normal"
    $ R_Eyes = "normal"
    $ R_Brows = "confused"
    menu:
        ch_r "I was curious about your ability. Is it true that other mutant powers don't work on you?"
        "Sure.":
            ch_p "That's what they tell me, but to be honest, I don't know much about it."
        "What's it to you?":
            ch_p "What do you care?"
            $ R_Eyes = "sexy"
            ch_r ". . ."
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
    ch_r "Well, you see, my power is the ability to absorb the mutant powers and memories of those I touch."
    $ Head = 0
    ch_r "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    ch_r "So I was hoping that maybe with your power. . ."
    call RogueFace("sexy")
    $ R_Brows = "sad"    
    menu:
        ch_r "So I was hoping that maybe with your power. . . I could touch you?"
        "Like, a Kiss?":
            if R_Love >= 500:    
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 20, 20)
                call RogueFace("surprised", 1)
                ch_r "Well, aren't you fresh." 
                call RogueFace("sexy")
                $ R_Mouth = "smile"
                ch_r "Just this once."
                call RogueFace("kiss") 
                "She gives you a little peck on the cheek."
                call RogueFace("smile")
            else:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 30)
                call RogueFace("bemused")
                ch_r "Heh, You'll have to earn that [R_Petname]."                
                $ R_Arms = 0
                $ Rogue_Arms = 2          
                call RogueFace("sexy")
                $ R_Brows = "sad"
                "She pulls off her glove and touches your face."      
        "Ok, be my guest.":        
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 30)
            call RogueFace("smile")
            $ R_Arms = 0
            $ Rogue_Arms = 2
            call RogueFace("sexy")
            $ R_Brows = "sad"
            "She pulls off her glove and touches your face."
        "No, that's weird.":       
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -30)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 30)
            call RogueFace("sad")
            $ R_Brows = "normal"
            ch_r "Well I'm just too damned curious, sorry."
            $ R_Arms = 0
            $ Rogue_Arms = 2
            "She pulls off her glove and touches your face."
    
    call RogueFace("surprised")
    ch_r "Wow."
    ch_r "This is amazing! With anyone else I would have drained their powers and they'd be out by now."
    call RogueFace("sexy")    
    menu:
        ch_r "Do you know how long it's been since I've felt human contact without hurting them?"
        "Glad I could help.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
        "I'm guessing it's been quite a while.":
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)
            call RogueFace("bemused", 1)
            ch_r ". . ."
    call RogueFace("smile")   
    ch_r "What a rush. I guess that's it then, I'm heading back to my room, you can head to yours."
    $ R_Blush = 0
    if R_Love >= 500:
        ch_r "Maybe I'll see you around though. Here's my number, you can give me a call."
        $ Digits.append("Rogue")
    $ R_Arms = "gloved"
    $ Rogue_Arms = 1
    $ R_Addictionrate = 5
    
label tour_parting:
    $ R_Emote = "normal"
    $ R_Blush = 0
    $ R_Loc = "bg rogue"
    menu:
        extend ""
        "Ok, See you later.":
            "You head back to your room."
        "Want to make out a little?":
            if R_Love >= 560:
                call RogueFace("bemused", 1)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 10, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 10)
                call R_Makeout
                if "angry" in R_RecentActions:                    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
                    ch_r "What the hell, [Playername]?!"
                    ch_r "Way to take advantage of a girl's feelings there!"             
                    hide Rogue with easeoutright
                    "Rogue tears off and you head back to your room."
                else:
                    call RogueFace("bemused", 1)
                    ch_r "That was real nice, [R_Petname]. I'll definitely be seeing you later."                
                    hide Rogue with easeoutright
                    "You head back to your room."
                    $ R_Emote = "normal"
            else:
                if R_Love >= 530 or R_Obed > 50 and not R_Kissed:
                    $ R_Addictionrate += 1
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 200, 5)
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
                    $ R_Kissed += 1
                    call RogueFace("bemused", 1)
                    ch_r "Well, maybe one kiss."
                    call RogueFace("kiss")
                    "She gives you a quick kiss. No tongue."                    
                    jump tour_parting
                else: 
                    call RogueFace("bemused")
                    ch_r "Nah, I think you've had enough for today, [R_Petname]."
                    "You head back to your room."
                    hide Rogue
                    $ R_Emote = "normal"
    call Wait            
    $ bg_current = "bg player"  
    call Set_The_Scene(0)
    "This is a short tutorial on the game's features. Feel free to skip it, you can always view it later in this room."
    call Tutorial    
    jump Player_Room    
return

# End Tour //////////////////////////////////////////////////////////////////////



            

# Event Sleepover /////////////////////////////////////////////////////  
label Rogue_Sleepover(sleepover = 0):
            #This event gets called from the Location menus when time passes in the Night timeframe.
            call Shift_Focus("Rogue")
            if bg_current == "bg rogue":
                    ch_r "It's getting late and I'm turning in."
            else:
                    ch_r "It's getting late and I'm getting a bit tired."  
            if Day <= 7:        
                ch_r "You seem nice and all, but we've only just met, so I'll see you tomorrow."  
            else:      
                call RogueFace("sexy", 1)
                if R_Sleep >= 3 and ApprovalCheck("Rogue", 800):                                 #You've slept over several times and she still likes you
                        if bg_current == "bg rogue":
                                ch_r "Are you staying over tonight?"
                        else:
                                ch_r "I'm staying over, right?"
                        $ sleepover = 1
                    
                elif R_Sleep < 3 and ApprovalCheck("Rogue", 1100, "LI"):                        #You haven't slept over much, but she wants you to
                        call RogueFace("bemused", 1)
                        if bg_current == "bg rogue":
                            ch_r "I was thinking. . . maybe you wanted to stay the night?"  
                        else:
                            ch_r "I was thinking. . . maybe I could stay the night?" 
                        $ sleepover = 1    
                    
                elif R_Sleep < 3 or not ApprovalCheck("Rogue", 600):                            #She doesn't especially want you there.  
                        if bg_current == "bg rogue":
                            ch_r "So I would kind of appreciate if you'd clear out. I'll see you later though." 
                        else:
                            ch_r "I suppose I should get going. . ."
                        
                else: #If she's uninterested
                        if bg_current == "bg rogue":
                            ch_r "You should get going, it's late." 
                        else:
                            ch_r "I'm heading out, see you tomorrow."
                                              
                menu:
                    extend ""
                    "Sure." if sleepover:
                            if R_Sleep <= 5:
                                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 10) if R_Love >= 500 else R_Love
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10)
                                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
                                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 20)                
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 5)
                            ch_r "Great, I'll get ready and we can get to bed."
                        
                    "No, sorry." if sleepover:                  
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 2)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 30, 5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 40, 3)
                            $ R_Brows = "sad"
                            ch_r "Ok, see you tomorrow then. 'Night."
                            $ sleepover = 0
                            
                    "Ok, I'll head out. Good night." if not sleepover and bg_current == "bg rogue":                        
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 2)            
                            call RogueFace("smile")
                            ch_r "Yeah, good night, [R_Petname]. . ."
                    "Ok, see you later then. Good night." if not sleepover and bg_current != "bg rogue":                        
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 25, 2)            
                            call RogueFace("smile")
                            ch_r "Yeah, good night, [R_Petname]. . ."
                        
                    "Are you sure I can't stay the night? . ." if not sleepover and not R_Sleep and bg_current == "bg rogue": 
                            if ApprovalCheck("Rogue", 1000) or ApprovalCheck("Rogue", 700, "L") or ApprovalCheck("Rogue", 500, "O"):
                                call RogueFace("bemused", 1)                   
                                ch_r "Well. . . I suppose it would be alright."
                                $ sleepover = 1 
                            else:                    
                                call RogueFace("smile")
                                $ R_Brows = "confused"
                                ch_r "I'm afraid not, [R_Petname]. Head home, I'll see you later." 
                    "Are you sure you can't stay? . ." if not sleepover and not R_Sleep and bg_current != "bg rogue": 
                            if ApprovalCheck("Rogue", 1000) or ApprovalCheck("Rogue", 700, "L") or ApprovalCheck("Rogue", 500, "O"):
                                call RogueFace("bemused", 1)                   
                                ch_r "Well. . . I suppose it would be alright."
                                $ sleepover = 1 
                            else:                    
                                call RogueFace("smile")
                                $ R_Brows = "confused"
                                ch_r "I'm afraid not, [R_Petname]. I'll head out, see you later." 
                                
                    "That's not what you said the other night . ." if not sleepover and R_Sleep: #if she wants you gone  
                            if ApprovalCheck("Rogue", 900)or ApprovalCheck("Rogue", 700, "L") or ApprovalCheck("Rogue", 500, "O"):
                                call RogueFace("bemused", 1)                  
                                ch_r "Well. . . that didn't turn out so bad, I suppose. . ." 
                                $ sleepover = 1
                            else:                    
                                call RogueFace("smile")
                                $ R_Brows = "confused"
                                if bg_current == "bg rogue":
                                    ch_r "I'm afraid not this time, [R_Petname]. Head home, I'll see you later." 
                                else:                        
                                    ch_r "I'm afraid not this time, [R_Petname]. I'll head out, see you later."
                    
            if sleepover: #If she agreed
                    if R_SEXP < 10 and not ApprovalCheck("Rogue", 500, "I") and not ApprovalCheck("Rogue", 500, "O"):
                            ch_r "No funny business though."        
                    jump Rogue_Morning
                     
            jump Return_Player
            
label Return_Player:    
            # This label is jumped to by the Sleep labels if the player or girl leaves after a sleepover (fail state).
            $ del Party[:]
            if bg_current != "bg rogue" and R_Loc == bg_current:
                    "Rogue heads out."        
                    $ R_Loc = "bg rogue"
            if bg_current != "bg kitty" and K_Loc == bg_current:
                    "Kitty heads out."        
                    $ K_Loc = "bg kitty"
            if bg_current != "bg player":
                    "You head back to your room."
            $ bg_current = "bg player"
            call Set_The_Scene
            $ renpy.pop_call()
            jump Player_Room
            
label Rogue_Morning:
            #This label is jumped too from Rogue Sleepover if you successfully stay the night
            call Shift_Focus("Rogue")
            call RogueOutfit("sleep")
            "Rogue changes into her sleepwear."
            ch_r "Hmm, that's a bit more comfortable."
            ch_r "Let's turn in."                                               #fix add sex option here
            show blackscreen onlayer black   
            pause 2
            call Wait(Lights = 0) 
            $ R_Loc = bg_current
            call RogueOutfit("sleep")
            
            $ D20 = renpy.random.randint(40, 70)                                #This element sends player to the Morningwood event        
            if "hungry" in R_Traits and D20 > 50:
                    $ Cnt = 1
            elif D20 >= R_Lust:
                    $ Cnt = 0     
            elif R_SEXP <= 15:
                    $ Cnt = 0         
            elif R_Blow >= 5 or ApprovalCheck("Rogue", 900, "I"):
                    $ Cnt = 1
            elif R_Blow and ApprovalCheck("Rogue", 900):
                    $ Cnt = 1
            elif ApprovalCheck("Rogue", 1400): # Trinity < 1400
                    $ Cnt = 1
            else:
                    $ Cnt = 0 
                    
            if Cnt:   
                    call Rogue_SexAct("morningwood") 
                    ch_r "Not a bad way to start the day. . ." 
                                    
            call RogueFace("smile")
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            ch_r "'Morning [R_Petname]. Sleep well?"
            menu:
                extend ""
                "It's always nice sleeping with you." if R_Sleep: 
                        if R_Sleep < 5:
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 10)    
                        $ R_Blush = 1
                        ch_r "Aw, that's right sweet of ya, [R_Petname]."
                        ch_r "We'll have to keep this regular."
                "I loved sleeping next to you." if not R_Sleep:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15)            
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 15)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 10)  
                        $ R_Blush = 1
                        ch_r "Aw, that's right sweet of ya, [R_Petname]."
                        ch_r "Makes me want to do it again sometime."
                "Sure.":
                        if R_Sleep < 5:
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 10)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 35, 20)             
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 10)
                        if R_Love >= 800:
                            call RogueFace("bemused")
                        else:
                            call RogueFace("confused")
                        ch_r "Ok, well glad I wasn't {i}too{/i} much bother."
                "You were constantly tossing around.":            
                        $ R_Blush = 1
                        if ApprovalCheck("Rogue", 800, "L"):
                            call RogueFace("bemused")
                        else:
                            call RogueFace("angry")
                        if R_Sleep < 5:
                            ch_r "Well! . . ."
                            ch_r "It's not like I've had much experience sleeping next to someone. . ."                       
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 60, -10)
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 20)  
                        else:
                            ch_r "Well you should probably be used to that by now."
                "You need to learn to stick to your side.":  
                        if R_Sleep < 5:
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10) 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 40)  
                        if ApprovalCheck("Rogue", 500, "O"):
                            call RogueFace("normal")
                            ch_r "Yes, [R_Petname], I'll try my best."
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10) if R_Sleep < 5 else R_Obed
                        else:
                            call RogueFace("angry")
                            ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that." 
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 35, 20) if R_Sleep < 5 else R_Inbt  
                        
            #fix add sex option here
            $ R_Blush = 0
            $ R_Sleep += 1    
            call Rogue_Schedule
            call RogueFace("normal")
            if R_Outfit != "sleep":
                "Rogue changes out of her sleepwear."
            call RogueOutfit
            call Girls_Location
            return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Rogue_MorningWood:
            # this label is called from the Rogue_SexAct("morningwood"), 
            # which was called from Rogue_Sleepover, which was called from a Location.
            call Shift_Focus("Rogue")
            $ P_Focus = 30
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 5)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)    
            call Rogue_BJ_Launch
            "You feel a pleasant sensation. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 5)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)
            "It's somewhere below your waist. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 10)
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)
            $ Trigger = "blow"
            $ R_Eyes = "down"
            "You open your eyes. . ."
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            $Speed = 3
            $ Count = 3
            $ Line = 0
            call Rogue_First_Peen(1)
            while Count > 0:
                    $ P_Focus = Statupdate("Rogue", "Focus", P_Focus, 80, 10)
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 80, 5)
                    menu:
                        extend ""
                        "Stay Quiet":
                            if Count >2:
                                "You just let her do her thing and pretend to still be asleep."
                            elif Count:
                                "It does feel nice. . ."
                            elif not Count:
                                "You wouldn't want to disturb her. . ."
                            ch_r "\"Slurp, slurp, slurp.\""
                        "Um, [R_Pet]? What're you doing?":
                            $ Line = "question"
                            $ Count = 1
                        "That feels great, keep going. . .":
                            $ Line = "praise"
                            $ Count = 1
                        "Hey, quit that!":
                            $ Line = "no"
                            $ Count = 1
                    $ Count -= 1
            $ Speed = 1
            $ R_Blush = 1
            "She pulls back with a pop."
            if Line == "question":
                call RogueFace("smile")
                ch_r "Well I ain't whistlin Dixie, [R_Petname]." 
            elif Line == "praise":
                call RogueFace("smile")
                ch_r "Mmm, you know it, [R_Petname]."
            elif Line == "no":
                $ Speed = 0
                call RogueFace("angry")
                $R_Brows = "confused"
                ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!"
            else:
                ch_r "Heh, I can tell you're awake, [R_Petname]. . ."
                ch_r "You've been. . . more responsive."
            menu:
                extend ""
                "So, um, you want to get back to it?":
                        if Line != "no":
                            call RogueFace("smile")
                            ch_r "My pleasure."
                        elif Line == "no" and ApprovalCheck("Rogue", 1750):
                            call RogueFace("bemused")
                            ch_r "You're lucky I'm so into you. . ."
                            $ Line = "maybe"
                        else:
                            call RogueFace("angry")
                            ch_r "Well not when you're rude to me."                
                            ch_r "You can polish yourself off."
                "Were you more interested in something else?":
                        if Line != "no":
                            call RogueFace("sexy")
                            ch_r "Ooh, what did you have in mind?"
                            $ Line = "sex"
                        elif Line == "no" and ApprovalCheck("Rogue", 1650):
                            call RogueFace("bemused")
                            ch_r "Well, you're a jerk, but you're a cute jerk."
                            ch_r "What were you thinking?"
                            $ Line = "sex"
                        else:
                            call RogueFace("angry")
                            ch_r "Well not when you're rude to me."                
                            ch_r "You can polish yourself off."
                "Sorry, sorry, please continue." if Line == "no":
                        if (R_Love + R_Obed + R_Inbt) >= 1450:
                            call RogueFace("bemused")
                            ch_r "Well, since you asked so nice. . ."
                            $ Line = "maybe"
                        else:
                            call RogueFace("angry")
                            ch_r "Pssht, maybe next time, [R_Petname]."
                "Sorry, but we could do something else." if Line == "no":
                        if ApprovalCheck("Rogue", 1350):
                            call RogueFace("sexy")
                            ch_r "Well, since you asked so nice. . ."
                            ch_r "What did you have in mind?"
                            $ Line = "sex"
                        else:
                            call RogueFace("angry")
                            ch_r "Pssht, maybe next time, [R_Petname]."
                "Not when I'm just waking up.":
                        call RogueFace("angry")
                        ch_r "Fine, whatever!"
                        $R_Eyes = "side"
                        ch_r "[[mumbles] Girl tries to do a favor. . ."
                        $ Line = "no"
            if Line == "no":
                    call Rogue_BJ_Reset
                    ch_r "You should probably get out of here."
                    call RogueOutfit
        #            $ renpy.pop_call()
                    $ renpy.pop_call()
                    jump Return_Player
            elif Line == "sex":
                    call Rogue_BJ_Reset
                    $ Situation = "shift"
                    return
            else:
                    $ Line = 0
                    $ Speed = 1
                    $ Situation = "blow"
                    return 
            $ renpy.pop_call()
            return
    
# end Event Morning Wood /////////////////////////////////////////////////////    


# Event Rogue_Caught_Masturbating  /////////////////////////////////////////////////////  
label Rogue_Caught_Masturbating:
            call Shift_Focus("Rogue")
            "You hear some odd noises coming from Rogue's room as you enter."                           #fix this scene, pants option
            show blackscreen onlayer black
            $ R_Outfit = "evo_green"
            call RogueOutfit(Changed=1)    
            $ R_Upskirt = 1
            $ R_PantiesDown = 1 
            $ R_Loc = bg_current
            call Set_The_Scene(0)
            call Display_Rogue(0)
            call RogueFace("sexy")
            $ R_Eyes = "closed"
            $ Rogue_Arms = 2
            $ Count = 0    
            $ Trigger = "masturbation"
            hide blackscreen onlayer black
            $ R_DailyActions.append("unseen")
            $ R_RecentActions.append("unseen")    
            call Rogue_SexAct("masturbate")
            if "angry" in R_RecentActions:
                return
        
#After caught masturbating. . .
            $ R_Eyes = "sexy"
            $ R_Brows = "confused"
            $ R_Mouth = "smile"
            if R_Mast == 1:        
                $ R_Mouth = "kiss"
                ch_r "Well that was a bit unexpected. . ."
                $ R_Eyes = "side"
                $ R_Mouth = "lipbite"        
                ch_r "but not exactly unpleasant. . ."
                $ R_Eyes = "sexy"
                $ R_Brows = "normal"         
                $ R_Mouth = "smile"
                ch_r "Maybe next time I'll give you a heads up first." 
            else:
                ch_r "Fancy seeing you here again, [R_Petname]. Almost like it was intentional. . ."
            $ Rogue_Arms = 1  
            call RogueOutfit      
            return
            
# end Rogue_Caught_Masturbating/////////////////////////////////////////////////////

# Event Rogue_Key /////////////////////////////////////////////////////  
label Rogue_Key:
            call Shift_Focus("Rogue")
            call Set_The_Scene
            call RogueFace("bemused")
            $ Rogue_Arms = 2
            ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
            ch_p "Thanks."
            $ Rogue_Arms = 1    
            $ Keys.append("Rogue")
            $ R_Event[0] = 1
            return
# end Event Rogue_Key /////////////////////////////////////////////////////


# Event Rogue_Caught /////////////////////////////////////////////////////  
label Rogue_Caught:
    call Shift_Focus("Rogue")
    call Checkout
    ch_r "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call RogueOutfit
    if K_Loc == bg_current:         
        $ K_Loc = "bg study"
    if E_Loc == bg_current:                
        $ E_Loc = "bg study"                
    $ bg_current = "bg study"  
    $ R_Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)
    show Rogue at SpriteLoc(StageRight) with ease
    if E_Loc == bg_current:         
        show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call RogueFace("sad")
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
    
    if R_Shame >= 40:
        ch_x "Rogue, my dear, you're practically naked! At least throw a towel on!"
        "He throws Rogue the towel."
        show blackscreen onlayer black 
        $ R_Over = "towel"         
        hide blackscreen onlayer black
    elif R_Shame >= 20:
        ch_x "Rogue, my dear, that attire is positively scandalous."
    
    if R_Caught:
        "And this isn't even the first time this has happened!"
    
    if K_Loc == bg_current:
        call KittyFace("surprised",2)
        ch_x "And Kitty, you were just watching this occur!"        
        call KittyFace("bemused",1)
        $ K_Eyes = "side"
        
    $ Count = R_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if R_Caught < 5:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, -20)            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -5)             
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
            call XavierFace("happy")  
            if R_Caught:
                ch_x "But you know you've done this before. . . at least [R_Caught] times. . ."  
            elif K_Caught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [K_Caught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [R_Pet]?":
            call Rogue_Namecheck
            call RogueFace("bemused")         
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 20)
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, -20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -10)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Omega, Rogue." if ApprovalCheck("Rogue", 1500, TabM=1, Loc="No") and P_Lvl >= 5:
            jump Plan_Omega
            
        "You can suck it, old man.":
            call RogueFace("surprised")
            $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!"              
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 30, -20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -10)    
            ch_x "Now get out of my sight."
            
    $ PunishmentX += Count            
    $ R_Caught += 1
    $ R_RecentActions.append("caught")
    $ R_DailyActions.append("caught")     
    call Remove_Girl("All")
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Omega:
    $ R_Eyes = "sexy"
    $ R_Mouth = "lipbite"
    $ R_Brows = "confused"            
    "As you say this, a sly grin crosses Rogue's face."
    $ R_Arms = 0
    $ Rogue_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."    
    show Rogue at SpriteLoc(StageLeft+100,85) zorder 24 with ease
    "Rogue moves in and also grabs his head, duplicating his powers as he watches helplessly."
    "Now that she posesses his full power, while his are negated, he has no defenses."
    if K_Loc == bg_current:        
        call KittyFace("surprised")      
        "Kitty looks a bit caught off guard, but goes along with the idea."        
        call KittyFace("sly")
    call XavierFace("hypno")
    
    $ Count = 3
    $ PunishmentX = 0    
    if "Omega" in P_Traits:
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 40)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 20)
    else:
            $ P_Traits.append("Omega")
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 10)
    ch_r "I think we'll only get three tries at this. . ."
    while Count:
        $ Count -= 1
        menu:
            ch_r "Well, [R_Petname], what would you like to do with this opportunity?"
            "Don't bother us anymore when we're having fun." if Rules:
                    $ Rules = 0
            "You know, it's kinda fun dodging you, catch us if you can." if not Rules:
                    $ Rules = 1
            "Raise my stipend." if P_Income < 30 and "Omega" not in P_Traits:             
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Omega" in P_Traits:             
                    pass
            "I was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, although you don't seem to need it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study. [[Owned](locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."                              
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room. [[Owned](locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Kitty's room." if "Kitty" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Kitty")
                    "Give me the key to Kitty's room. [[Owned](locked)" if "Kitty" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."    
    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 10)
    $ R_Love = Statupdate("Rogue", "Love", R_Love, 70, 30)
    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
    $ R_Arms = "gloved"
    $ Rogue_Arms = 1
    "You return to your room"
    jump Player_Room
                              
# end Rogue_Caught/////////////////////////////////////////////////////

# start Rogue_BF//////////////////////////////////////////////////////////
label Rogue_BF:
    call Shift_Focus("Rogue")
    
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."    
                
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    $ R_DailyActions.append("relationship")
    call RogueFace("bemused", 1)
    ch_r "So, [R_Petname], we've been hanging out for a while now."
    ch_r ". . ."
    $R_Eyes = "sexy"
    menu:
        ch_r "Right?"
        "Yeah, it's been great.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
        "Yeah, I guess":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
        "Um, maybe?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
    if R_SEXP >= 10:
        ch_r "I mean, we've done some stuff. . ."
    if R_SEXP >= 15:
        ch_r "Like {i}sex{/i} stuff. . ."
    if "dating" in K_Traits and "dating?" in R_Traits:    
        ch_r "I know you've been going with Kitty for a while now, but we got talking and . . ."
    elif "dating" in K_Traits:
        ch_r "I know you've been going with Kitty for a while now, but . . ."
    if not R_Event[5]:
        ch_r "Right, so I was thinking. . ."
        ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
        ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
        ch_r "Let's make it official, you want to be my boyfriend?"
    elif "dating?" in R_Traits: 
        ch_r "Kitty said it would be cool if we were dating too." 
    elif "dating" in K_Traits: 
        ch_r "I'd still like to be your girlfriend too."
    else:        
        ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
        ch_r "I think I want to be your girlfriend. . . officially"
    $ R_Event[5] += 1
    menu: 
        extend ""
        "I'd love to!":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 30)
            $ R_Petnames.append("boyfriend")
            $ R_Traits.append("dating")
            "Rogue leaps in and kisses you deeply."
            call RogueFace("kiss") 
            $ R_Kissed += 1
        "Um, ok.":
            $ R_Petnames.append("boyfriend")
            $ R_Traits.append("dating")
            $R_Brows = "confused"
            "Rogue is a bit put off by your casual acceptence of reality, but takes it as a positive sign and hugs you."    
        "I'm with Kitty now." if "dating" in K_Traits:             
            call RogueFace("sad",1)    
            ch_r "I know, I know, i just thought maybe you could go out with me too?"
            menu:
                extend ""
                "Sure":
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 30)
                    $ R_Petnames.append("boyfriend")
                    $ R_Traits.append("dating")
                    "Rogue leaps in and kisses you deeply."
                    call RogueFace("kiss") 
                    $ R_Kissed += 1
                "No, sorry.":
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    ch_r "I get it. that's fine." 
                "No way.":
                    jump Rogue_BF_Jerk
        "Not really.":
            jump Rogue_BF_Jerk
    call RogueFace("sexy")    
    ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"
    $ Tempmod = 10
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_BF_Jerk:
    call RogueFace("angry", 1)
    ch_r "Well fine!" 
    $ Count = (20* R_Event[5])
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 40)
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, Count)
    if R_Event[5] >= 3:
        call RogueFace("sad")
        ch_r "Hrmph. I don't care what you want, we're dating. Deal with it."   
        $ R_Petnames.append("boyfriend")
        $ R_Traits.append("dating")
        $ Achievements.append("I am not your Boyfriend!")
        ch_r "Now I need some alone time though."
        $ bg_current = "bg player"          
        call Remove_Girl("Rogue")
        call Set_The_Scene
        return        
    if R_Event[5] > 1:
        ch_r "I don't know why I keep asking, I should know you haven't changed."          
    $ Count = (50* R_Event[5])                                  #fix test to see if negatives can work here.
    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -Count)
    ch_r "Jerk! Out!"
    $ R_Loc = "bg rogue"
    $ bg_current = "bg player"         
    call Remove_Girl("Rogue")
    call Set_The_Scene
    $ renpy.pop_call()
    jump Player_Room     

# end Rogue_BF//////////////////////////////////////////////////////////

# start Rogue_Love//////////////////////////////////////////////////////////
label Rogue_Love:
    call Shift_Focus("Rogue")
    
    if bg_current != "bg rogue":
        if R_Loc == bg_current or "Rogue" in Party:
            "Suddenly, Rogue says she wants to talk to you in her room and drags you over there."
        else:
            "Rogue shows up, hurridly says she wants to talk to you in her room and drags you over there."
    else:
        "Rogue suddenly stares at you very intently."
    
    $ bg_current = "bg rogue"
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    $ R_DailyActions.append("relationship")
    call RogueFace("bemused", 1)       
    if "dating" in R_Traits:
        ch_r "We've been dating for a while now, and I'm really feeling close to you."
    else:
        ch_r "We've been hanging out for a while now, and I'm really feeling close to you."
    ch_r ". . ."
    $R_Eyes = "sexy"
    menu:
        ch_r "Right?"
        "I love you, Rogue.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 50)
            $ R_Event[6] = 10
        "Yeah, it's been great.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
        "Yeah, I guess":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
        "Um, maybe?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
    if not R_Event[6]:
        ch_r "Right, so I was thinking. . ."
        ch_r "I love you."
    elif R_Event[6] == 10:        
        call RogueFace("confused")
        ch_r "So. . . wait, what?"
        call RogueFace("smile")
        $R_Brows = "surprised"        
        ch_r "I love you too!"
        call RogueFace("kiss")
        "Rogue leaps into your arms and gives you a kiss." 
        call RogueFace("sexy")
        $ R_Kissed += 1
    else:        
        ch_r "Even though we've had our rough patches from time to time. . ."
        ch_r "I still love you."
    $ R_Event[6] += 1
    if R_Event[6] < 10:
        menu:
            extend ""
            "I love you too.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 50)
                "Rogue collapses into your arms."
            "That's great!":
                $R_Brows = "confused"
                "Rogue seems a bit perplexed, but takes it as a positive sign and hugs you."   
            "I know.":
                call RogueFace("smile")
                $R_Brows = "confused"                
                "Rogue punches you in the arm and then gives you a huge hug."                         
            "So?":
                jump Rogue_Love_Jerk
            "Well I don't think of you like that.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -50)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 50)
                jump Rogue_Love_Jerk
    call RogueFace("sexy")
    $ R_Petnames.append("lover")
    if not R_Sex:
        ch_r "So. . . did you want to . . . consumate this?"
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
        menu:
            extend ""
            "Yeah. . . [[have sex]":      
                $ R_Inbt = Statupdate("Rogue", "R_Inbt", R_Inbt, 30, 30) 
                ch_r "Hmm. . ."  
                call Rogue_SexAct("sex")
                return
            "I have something else in mind. . .[[choose another activity]":
                $ R_Brows = "confused"
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 20)
                ch_r "Well now you've got me curious. . ."
                pass
            "Ew. [[do nothing]":                
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 40)                
                call RogueFace("perplexed",1)
                ch_r "Um, ok?"
                ch_r "{size=-5}What the fuck was that?{/size}"          #fix test this      
                return
    else:
        ch_r "Now, lover. . . was there anything else you felt like doing to celebrate?"  
    if "stockings and garterbelt" not in R_Inventory:
            $ R_Inventory.append("stockings and garterbelt")
    $ Tempmod = 20
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Love_Jerk:    
    $ renpy.pop_call()
    call RogueFace("angry", 1)
    ch_r "Well fine!" 
    $ Count = (20* R_Event[6])
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 40)
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, Count)
    if R_Event[6] == 3:
        call RogueFace("sad")
        ch_r "I. . . I don't care, I love you too much anyways."   
        $ R_Petnames.append("lover")
        $ Achievements.append("One Sided Love")
        ch_r "I need some time to myself though."
        $ R_Loc = "bg rogue"
        $ bg_current = "bg player"
        call Remove_Girl("Rogue")
        jump Player_Room  
    if R_Event[6] > 1:
        ch_r "Fool me once, shame on you. . . I thought you'd grown." 
    ch_r "If that's how you want to be, you can get the hell out of here!"
    $ Count = (100* R_Event[6])
    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -Count)
    $ R_Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl("Rogue")
    jump Player_Room  

# end Rogue_Love//////////////////////////////////////////////////////////


# start Rogue_Sub//////////////////////////////////////////////////////////
label Rogue_Sub:  
    call Shift_Focus("Rogue")
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."
    
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    $ R_DailyActions.append("relationship")
    call RogueFace("bemused", 1)
    ch_r ". . ."
    if "dating" in R_Traits:
        ch_r "We've been dating for a bit now."  
    else:    
        ch_r "We've been hanging out for a while now."   
    if R_FondleB or R_FondleP or R_FondleA: 
        ch_r "I've let you touch me. . ."
    if R_Hand or R_Blow:
        ch_r "I've touched you. . ."
    if R_Love >= 900 and "dating" in R_Traits:
        ch_r "I love you so much. . ."
    elif R_Love >= 800:
        ch_r "I really care about you."
    elif R_Love >= 500:
        ch_r "We don't exactly get along, but. . . we work, right?"
    else:
        $ R_Brows = "angry" 
        ch_r "I really don't like you much, but something about you just. . ."
        ch_r "works for me."
    menu:
        extend ""
        "Yeah, it's been great.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
        "Yeah, I guess":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
        "Um, maybe?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
    if not R_Event[7]:
        ch_r "Right, so I was thinking. . ."
        $ R_Eyes = "sexy"
        ch_r "I'd like you to provide some . . .structure to my life."
    else:        
        ch_r "I'd like you to reconsider the offer I made. . ."
        ch_r "the one about giving me some . . .structure."
    $ R_Event[7] += 1
    menu:
        extend ""
        "Sounds interesting, yes.":
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 100)
            $ R_Petnames.append("sir")
            "Rogue nods obediently."            
        "What do you mean by that?": 
            call RogueFace("bemused") 
            ch_r "When you. . . encourage me to try new things, it really turns me on."
            ch_r "I'd like you to continue to. . . encourage me."
            menu:
                ch_r "I mean that I would like you to give me orders, and I will follow them as best I can."
                "Sounds interesting, ok.":
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 100)
                    "Rogue nods obediently."  
                "Oh, ok, sure.":
                    "Rogue seems a bit put out, but takes it as a positive sign and nods."  
                "Oh, no thanks. Take care of things yourself.":
                    jump Rogue_Sub_Jerk 
            $ R_Petnames.append("sir")         
        "Nah, you can handle things yourself.":
            jump Rogue_Sub_Jerk
    call RogueFace("sexy") 
    "She gives you a piece of paper with the password for her cellphone calender."
    "Apparently, whatever you enter into it, she intends to do. . . within reason."
    ch_r "Now, sir. . . was there anything else you wished me to do to celebrate?"
    if "stockings and garterbelt" not in R_Inventory:
            $ R_Inventory.append("stockings and garterbelt")
    $ Tempmod = 10
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Sub_Jerk:
    call RogueFace("sad", 1)
    ch_r "Hrmph!"
    $ Count = (20* R_Event[7])
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 30)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, Count)    
    $ renpy.pop_call()
    if R_Event[7] == 2:
        call RogueFace("sad")
        ch_r "Well, maybe you'll change your mind. I'll just leave this here, sir."
        "She gives you a piece of paper with the password for her cellphone calender."
        "Apparently, whatever you enter into it, she intends to do. . . within reason."
        $ R_Petnames.append("sir")
        $ Achievements.append("Nosiree")
        ch_r "I need some time to myself though."        
        $ bg_current = "bg player"        
        $ R_Loc = "bg rogue"
        call Remove_Girl("Rogue")
        jump Player_Room  
    if R_Event[7] > 1:
        ch_r "I thought you may have learned to respect my needs by now." 
    ch_r "If that's how it is, I would appreciate some time alone."           
    $ Count = (20* R_Event[7])
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, -Count)
    $ R_Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl("Rogue")
    jump Player_Room  

# end Rogue_Sub//////////////////////////////////////////////////////////


# start Rogue_Slave//////////////////////////////////////////////////////////
label Rogue_Slave:    
    call Shift_Focus("Rogue")
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."
    
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    $ R_DailyActions.append("relationship")
    call RogueFace("bemused", 1)
    ch_r ". . ."
    
    if "dating" in R_Traits:
        ch_r "This situation we have has really added some . . . spice to our relationship." 
    else:     
        ch_r "This situation we have has been very. . . interesting."   #fix add in tags based on public favors
    if R_Anal or R_DildoA:
        ch_r "We've even done some butt stuff."  
    if R_Love >= 900 and "dating" in R_Traits:
        ch_r "I'm devoted to you. . ."
    elif R_Love >= 800:
        ch_r "I really care about you."
    elif R_Love >= 500:
        ch_r "I can't be without you."
    else:
        $ R_Brows = "angry" 
        ch_r "I can't stand being with you, but can't stand being without you either."
    menu:
        ch_r "Have I been pleasing you, [R_Petname]?"
        "Certainly.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
        "Yeah, I guess.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
        "Not especially.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)            
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)        
    if not R_Event[8]:
        ch_r "Yes, well, given that. . ."
        ch_r "I think that I would like you to be my master, formally."
    else:        
        ch_r "I'd like you to reconsider the offer I made. . ."
        ch_r "please be my master."
    $ R_Event[8] += 1
    menu:
        extend ""
        "Very well.":
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 100)
            $ R_Petnames.append("master")
            "Rogue bows obediently."
        "What do you mean by that?":            
            $R_Brows = "confused"
            ch_r "Well, when you tell me what to do. . ."            
            call RogueFace("bemused", 1)     
            ch_r "I get really horny." 
            ch_r "I just really need for you to tell me what to do."
            menu:
                ch_r "I mean that I would follow your orders to the letter, so long as I am able."
                "Oh, ok, sure.":
                    "Rogue seems a bit put out, but takes it as a positive sign and nods."  
                    $ R_Petnames.append("master")
                "You should do your own thing, you don't need me telling you what to do.":                                            
                    $R_Brows = "confused" 
                    ch_r "Ok, if that's what you want. . ."
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 100)  
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 50)  
                    ch_r "For now at least. . ."
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, -200)
                    $ R_Event[8] = 3
                "Oh, no, sounds like too much work.":
                    jump Rogue_Obed_Jerk                
        "Nah, take care of yourself.":
            jump Rogue_Obed_Jerk
    call RogueFace("sexy")       
    ch_r "Now, master. . . was there anything else you wished me to do to celebrate?"
    $ Tempmod = 20
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Obed_Jerk:
    call RogueFace("sad", 1)
    ch_r "Well fine!"
    $ Count = (20* R_Event[8])
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, 30)
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, Count) 
    $ renpy.pop_call()   
    if R_Event[8] == 2:
        call RogueFace("sad")
        ch_r "I don't care what you say, this is something I need. MASTER."   
        $ R_Petnames.append("master")
        $ Achievements.append("Heavy is the Head")
        ch_r "I need some time to myself though."        
        $ bg_current = "bg player"        
        $ R_Loc = "bg rogue"       
        call Remove_Girl("Rogue")
        jump Player_Room  
    if R_Event[8] > 1:
        ch_r "I thought you may have learned to respect my needs by now." 
    ch_r "If that's how it is, I would appreciate some time alone."          
    $ Count = (50* R_Event[8])
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, -Count)
    $ R_Loc = "bg rogue"
    $ bg_current = "bg player"       
    call Remove_Girl("Rogue")
    jump Player_Room  

# end Rogue_Slave//////////////////////////////////////////////////////////


# start Rogue_Sexfriend//////////////////////////////////////////////////////////
label Rogue_Sexfriend:  
    call Shift_Focus("Rogue")
    $ R_DailyActions.append("relationship")
    if "dating" in R_Traits:       
        if R_Loc != bg_current and "Rogue" not in Party:
            return
        $ R_Petnames.append("sex friend") 
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 50) 
        "Rogue suddenly gives your butt a little squeeze."
        return
        
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."
    
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    call RogueFace("smile", 1)
    ch_r ". . ."
    ch_r "We've been having fun, right?"   
    if R_SEXP >= 40:
        ch_r "I mean, we've been getting up to some pretty wild stuff."
    if "ex" in R_Traits:
        ch_r "And we were actually dating for a while. . ."
    else:
        ch_r "And I know we're not \"dating\" dating, but you know. . ."
    menu:
        ch_r "Haven't I been fun to have around?"
        "Yeah, you've been great.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 20)
        "Hmmm. . . yes?":
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 20)
        "Maybe. . .":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)
    if not R_Event[9]:
        ch_r "Ok, so since we've been having so much fun. . ."
        if "ex" in R_Traits:
            ch_r "I think that even though we aren't dating, I still want to be sex friends."
        else:
            ch_r "I think I'm ready to accept just being casual sex friends."
    else:        
        ch_r "I'd like you to reconsider my generous offer. . ."
        ch_r "come on, sex friend? Eh?"
    $ R_Event[9] += 1
    menu:
        extend ""
        "Sounds fun!":
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 100) 
            $ R_Petnames.append("sex friend")
            "Rogue nods obediently."            
        "What do you mean by that?":            
            $R_Brows = "confused"              
            ch_r "You know, casual sex, no real strings, for now at least."
            menu:
                ch_r "Well?"
                "Oh, ok, sure.":
                    "Rogue is a bit put off, but grabs you in a big hug anyway."  
                    $ R_Petnames.append("sex friend") 
                "Oh, no thanks. Not interested.":
                    jump Rogue_Sexfriend_Jerk                
        "Nah, you're on your own.":
            jump Rogue_Sexfriend_Jerk
    call RogueFace("sexy")  
    ch_r "Now, sex friend. . . how would you like to celebrate?"
    if "stockings and garterbelt" not in R_Inventory:
            $ R_Inventory.append("stockings and garterbelt")
    $ Tempmod = 25
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Sexfriend_Jerk:    
    call RogueFace("sad", 1)
    $ R_DailyActions.append("relationship")
    ch_r "Your loss." 
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 30) 
    $ renpy.pop_call()   
    if R_Event[9] == 3:
        ch_r "Well, it's not really up to you anyways."
        ch_r "Just let me know if you want a roll in the hay."
        $ R_Petnames.append("sex friend")
        $ Achievements.append("Man of Virtue")
        ch_r "I need some alone time though."        
        $ bg_current = "bg player"        
        $ R_Loc = "bg rogue"
        call Remove_Girl("Rogue")
        jump Player_Room  
    $ Count = (10 * R_Event[9])
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, -Count)
    if bg_current == "bg rogue":
        ch_r "Ok, you can go now."
        $ bg_current = "bg player"
    else:
        ch_r "Ok, I'm out."   
        $ R_Loc = "bg rogue"
    call Remove_Girl("Rogue")
    jump Player_Room  

# end Rogue_Sexfriend//////////////////////////////////////////////////////////


# start Rogue_Fuckbuddy//////////////////////////////////////////////////////////
label Rogue_Fuckbuddy:    
    call Shift_Focus("Rogue")
    if "dating" in R_Traits:        
        if R_Loc != bg_current and "Rogue" not in Party:
            return
        $ R_Petnames.append("fuck buddy") 
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 50) 
        "Rogue suddenly reaches down and gives your package a little squeeze."
        return
        
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."
    
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    call RogueFace("bemused", 1)
    ch_r ". . ."
    ch_r "I've been having a lot of fun with this \"sex friend\" thing."       
    if "exhibitionist" in R_Traits:
        ch_r "And I've really been getting off on all the stuff we've been doing."
    menu:
        extend ""       
        "You bet!":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 20)          
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 30)  
        "Yeah?":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 20)
        "Whatever.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 200, 30)            
    if not R_Event[10]:
        ch_r "So, since it's worked so far. . ."
        ch_r "I'd like to be full on casual fuck buddies."
    else:        
        ch_r "Come on, please?. . . fuck buddy?"
    $ R_Event[10] += 1
    menu:
        extend ""
        "Heh, ok, fuck buddy.":
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, 100) 
            $ R_Petnames.append("fuck buddy")
            $ Rogue_Arms = 2
            ch_r "Whoo hoo!"
            $ R_Over = 0
            $ R_Chest = 0              
            call Rogue_First_Topless(1)
            call R_Breasts_Launch
            "Rogue, throws her top off, grabs you and shoves your head into her cleavage."
            call R_Pos_Reset
        "What do you mean by that?":            
            $R_Brows = "confused"
            menu:
                ch_r "I mean, you know, we'd fuck. And be buddies. Both of those."
                "Oh, ok, sure.":
                    call R_Kissing_Launch
                    "Rogue laughs and tackles you into a hug." 
                    call R_Pos_Reset
                    $ R_Petnames.append("fuck buddy")  
                "Oh, no, not my style.":
                    jump Rogue_Fuckbuddy_Jerk                
        "No thanks.":
            jump Rogue_Fuckbuddy_Jerk
    call RogueFace("sexy")      
    ch_r "Now, -heh-, fuck buddy. . . let's make this official!"
    $ Tempmod = 30
    call Rogue_SexMenu
    $ Tempmod = 0
    return
    
label Rogue_Fuckbuddy_Jerk:
    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 50, 30)   
    call RogueFace("bemused", 1)
    if R_Event[10] > 1:
        $ Rogue_Arms = 2
        $ R_Over = 0
        $ R_Chest = 0
        call Rogue_First_Topless(1)
        ch_r "I offer these things on a silver platter, and nothing!" 
        call RogueOutfit 
        ch_r "Look, I don't care what you call it. Just let me know if you want a tumble."   
        $ R_Petnames.append("fuck buddy")
        $ Achievements.append("Stalwart as the mount")
        return      
    else:
        ch_r "Too bad."
    $ renpy.pop_call()
    $ Count = (10*R_Event[10])
    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 200, -Count)
    if bg_current == "bg rogue":
        ch_r "Ok, you can go now."
        $ bg_current = "bg player"
    else:
        ch_r "Ok, I'm out."   
        $ R_Loc = "bg rogue"    
    call Remove_Girl("Rogue")
    jump Player_Room  
# end Rogue_Fuckbuddy//////////////////////////////////////////////////////////

# start Rogue_Daddy//////////////////////////////////////////////////////////
label Rogue_Daddy:      
    $ R_DailyActions.append("relationship")
    call Shift_Focus("Rogue")
    ch_r ". . ."
    if "dating" in R_Traits:
        ch_r "You know, even though we've been dating,"  
    else:    
        ch_r "Even though we've been hanging out," 
    if R_Love > R_Obed and R_Love > R_Inbt:
        ch_r "and you're really sweet to me. . ."
    elif R_Obed > R_Inbt:
        ch_r "and you know what I need. . ."
    else:
        ch_r "and I've really been spreading my wings. . ."        
    ch_r "So I was thinking, could I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
            call RogueFace("smile") 
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20)          
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 10)            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 30) 
            ch_r "Squee!"   
            $ R_Petname = "daddy"
        "What do you mean by that?": 
            call RogueFace("bemused") 
            ch_r "I just sort of get turned on by it, you know, being your baby girl. . ."
            ch_r "I'd like to call you that."
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                    call RogueFace("smile") 
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15)          
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 60, 20)            
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 25) 
                    ch_r "Great! . . daddy."  
                    $ R_Petname = "daddy"
                "Could you not, please?":             
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 40)            
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 20)  
                    call RogueFace("sad") 
                    ch_r "   . . .   "
                    ch_r "Well, ok."
                "No, that creeps me out.":    
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -10)          
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 45)            
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 5)  
                    call RogueFace("angry") 
                    ch_r "Hrmph." 
        "No, that creeps me out.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5)          
            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 40)            
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 70, 10) 
            call RogueFace("angry") 
            ch_r "Hrmph."  
    $ R_Petnames.append("daddy")
    return

# end Rogue_Daddy//////////////////////////////////////////////////////////

# Start RogueBreakup //////////////////////////////////////////////////////////   

label Rogue_Cheated(Resolution = 0, B = 0):  #Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
    $ R_DailyActions.append("relationship")
    call Shift_Focus("Rogue")
    
    call RogueFace("angry") 
    if R_Loc != bg_current and "Rogue" not in Party:
        "Suddenly, Rogue shows up and says she needs to talk to you."   
    $ Rogue_Arms = 1        
    $ R_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Rogue
    call CleartheRoom("Rogue")
    call Taboo_Level
    
    if "saw with kitty" in R_Traits:
        if R_LikeKitty >= 900:
            $ Resolution += 2
        elif R_LikeKitty >= 800:
            $ Resolution += 1
        $ B = int((R_LikeKitty - 500)/2)
    
    $ Resolution -= R_Cheated if R_Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
    
    if R_Cheated:
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -50) 
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -20)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -50)    
        ch_r "Why're you screw'in around on me again?"
    else:
        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -100) 
        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -30)
        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -20)  
        ch_r "What the hell was that about earlier?"  
        
    menu:
            extend ""
            "I'm sorry.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 30) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -10)
                $ Line = "sorry"     
                $ Resolution += 1
                
            "What do you mean?":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 15)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 5)   
                
                if "saw with kitty" in R_Traits:
                    ch_r "I {i}mean{/i} you screwing around with Kitty like that."
                else:
                    ch_r "You {i}know{/i} what I mean."
                    
                menu:
                        extend ""
                        "Oh! I'm sorry!":         
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20) 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -10)           
                            $ Line = "sorry"
                        "Oh, that. Yeah.":
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20) 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10)  
                            $ Line = "yeah"
                            $ Resolution -= 1
                        
            "You mean with Kitty?" if "saw with kitty" in R_Traits:
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 20)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10)  
                
                ch_r "Yes, \"I mean with Kitty.\"" 
                if R_Cheated:
                    ch_r "Y'all were screwing around behind my back! Again!"
                else:
                    ch_r "Y'all were screwing around behind my back!"
                menu: 
                        extend ""
                        "Oh! I'm sorry!":
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 15) 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -10)                            
                            $ Line = "sorry"
                        "Oh, yeah.":
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20) 
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 10)  
                            $ Line = "yeah"
                            $ Resolution -= 2
    
    if Line == "sorry":  
        $ R_Eyes = "side"
        if "saw with kitty" in R_Traits:
            ch_r "Well 'course you are, but that don't make it right. Screwing around with Kitty like that. . ."
        else:
            ch_r "Well 'course you are, but that don't make it right."        
        $ R_Eyes = "sexy"
    else:
        ch_r "Oh? So what do you have to say for yourself?"
    
    menu:
            extend ""
            "I really hurt you, and I'm sorry.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 25) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, -5)
                "Well at least you're owning up to it."
                $ Resolution += 2
                
            "We were just messing around, nothing serious.":
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -25) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 30)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 80, 10)  
                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
                if not ApprovalCheck("Rogue", 700, "O", Bonus = (B/3)):
                    $ Resolution -= 2
                
            "I think she's really cute.":
                if R_LikeKitty >= 700 or ApprovalCheck("Rogue", 500, "I", Bonus = (B/3)):                    
                    $ R_Eyes = "side"
                    $ R_Brows = "confused"
                    ch_r "Well. . . yeah, she is kinda cute, but so what?"                     
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                    $ Line = "threeway"  
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 30)
                    ch_r "Well that don't mean shit, [Playername], you're with me!"
                    $ Resolution -= 2
                
            "Don't you like her?":
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 30)
                if R_LikeKitty >= 700 or R_Inbt >= 500:                    
                    $ R_Eyes = "side"
                    $ R_Brows = "confused"
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 25)                  
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                    ch_r "I mean, sorta. Not like that really though. . ."   
                    $ Line = "threeway" 
                elif R_LikeKitty >= 600:    
                    $ R_Brows = "confused" 
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -10)
                    ch_r "We're friends, but that doesn't mean I'm cool with her hooking up with my man!"
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -20) 
                    ch_r "Whether I like her or not, don't give you rights to hook up with her."
                    $ Resolution -= 1
                 
    $ R_Eyes = "sexy"
    menu:
            extend ""
            "I won't do it again.":
                if R_Cheated:        
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)  
                    ch_r "Like last time you told me that, you mean?"                    
                    $ Resolution -= 1
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20) 
                    $ R_Brows = "angry"
                    $ Resolution += 2 if Resolution < 3 else 0
                    ch_r "I'll hold you to that."
                    
            "I can't make any promises, she's pretty hot.":
                $ R_Brows = "angry"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -40) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 40)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 10)  
                ch_r "Then I don't know what you tell you, I think we're through."
                $ Resolution -= 2
                
            "Have you considered maybe letting her join us?":
                call RogueFace("oh")
                if ApprovalCheck("Rogue", 2200, Bonus = B) or ApprovalCheck("Rogue", 950, "L", Bonus = (B/3)):
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 30)                  
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 89, 10)
                    $ Resolution += 2
                elif ApprovalCheck("Rogue", 1500, Bonus = B) or R_LikeKitty >= 700:
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 10)                  
                    $ R_Lust = Statupdate("Rogue", "Lust", R_Lust, 90, 5)
                else:
                    $ Resolution -= 3
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -25) 
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 10) 
                    
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 40) 
                ch_r "I don't know what to do with that, you talk'in a three-way?"
                call RogueFace("startled")
                $ Line = "threeway"
    
    if Resolution >= 5 and Line == "threeway": #she agrees to a threeway
                    if R_Cheated:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 25) 
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 30)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 60)   
                    else:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 50) 
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 40)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 40)  
                    ch_r "So I catch you fool'in around on me, and you want to make it official?"
                    if "saw with kitty" in R_Traits:                         
                        ch_r "I guess I could live with that, I'll talk to Kitty."
                        $ R_Traits.append("poly kitty")
                        $ R_Traits.append("ask kitty")
                        
    elif Resolution >= 5: #she suggests a threeway
                    if R_Cheated:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20) 
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 100)   
                    else:
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 40) 
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 60)   
                    ch_r "You're just a regular polecat in heat. I guess I can't tame you."
                    if "saw with kitty" in R_Traits: 
                        ch_r "Not alone, at least. Maybe me and Kitty can work something out."
                        $ R_Traits.append("poly kitty")
                        $ R_Traits.append("ask kitty")
                        
    elif Resolution >= 2: #she agrees to forgive you   
                if R_Cheated:     
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 25)       
                    ch_r "I've given you a chance to do right by me, and you keep screwing it up."
                    ch_r "I don't know how many more chances I can give you here."
                else:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 80, 40) 
                    ch_r "You betrayed my trust, [R_Petname]."
                    ch_r "Don't let it happen again." 
                    
    else: #she doesn't agree to forgive you
                if Line == "threeway":
                    ch_r "I can't even believe you would suggest a fucking {i}threeway!{/i}"
                if R_Cheated:         
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -50)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 30)  
                    ch_r "You done this too many times for me to keep let'in you back."
                    ch_r "Sorry, [R_Petname], this is the end."
                else:
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -50)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 20)  
                    ch_r "I just don't think I can trust you anymore, [R_Petname]."
                    ch_r "This is it for us." 
                $ R_Traits.remove("dating")
                $ R_Traits.append("ex")
                $ R_DailyActions.append("angry")
                $ R_Break[0] = 5 + R_Break[1] + R_Cheated
                    
        
    $ R_Cheated += 1
    if "saw with kitty" in R_Traits:                                    #Clean up the trait for this event
        $ R_Traits.remove("saw with kitty")
        if "poly kitty" not in R_Traits:
            $ R_LikeKitty -= 50
            
    if "dating" in R_Traits:
        menu:
            extend ""
            "I'm glad we could work this out." if "dating" in R_Traits:
                call RogueFace("sad") 
                if Resolution >= 3:            
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 5)    
                    ch_r "I am too, [R_Petname]."
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5) 
                    ch_r "Yeah, we'll see, [R_Petname]."
                    
            "Want to fool around a bit?" if "dating" in R_Traits and not Taboo:
                if (R_Obed + R_Inbt) >= (1 * R_Love) or R_Lust >= 70:
                    call RogueFace("sly")
                    $ R_Eyes = "side"
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 20) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 10)
                    ch_r "Sure, whatever."
                    call Rogue_SexMenu
                else:        
                    call RogueFace("sad")             
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -10) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -10)
                    ch_r "It's still too raw, [R_Petname]."
                    
            "I'm sorry it didn't work out." if "dating" not in R_Traits: 
                    call RogueFace("sad") 
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 10) 
                    ch_r "I am too, [R_Petname]."
                    
            "Want to have some break-up sex?" if "dating" not in R_Traits and not Taboo:
                call RogueFace("angry")
                if (R_Obed + R_Inbt) >= (1.5 * R_Love) or R_Lust >= 70:
                    $ R_Eyes = "side"
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 90, 10)
                    ch_r "Sure, whatever." 
                    call DrainWord("Rogue","angry",0,1)
                    call Rogue_SexMenu
                    $ R_DailyActions.append("angry")
                else:
                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -20) 
                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, -10)
                    ch_r "You have got to be kidding me."
                    
            "Let me know if you change your mind." if "dating" not in R_Traits:
                call RogueFace("angry")
                $ R_Eyes = "side"
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, -5) 
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 90, 10)
                ch_r "Yeah, I'll get right on that."
                
            "Ok, see you later then.":
                call RogueFace("confused")
                
                
    if bg_current == "bg rogue":                                        #remove Rogue from the scene (or the player)
        ch_r "I need some time alone, [R_Petname]. I'll see you later."
        $ bg_current = "bg player"
        $ renpy.pop_call() 
        jump Player_Room
    else:
        ch_r "I need some time alone, [R_Petname]. I'll see you later."
        call Remove_Girl("Rogue")
    return

# end RogueBreakup //////////////////////////////////////////////////////////    
 
# start Tutorial //////////////////////////////////////////////////////////

menu Tutorial:
    "What did you want to know about?"
    "UI":
        while True:
            menu:                
                "Which UI element did you want to hear about?"
                "Relationship Bar":
                    "The bar covering the top left of the screen displays the stats of the primary girl in the scene. These stats are described elsewhere in the tutorial."
                    "If the bar is green, it represents Rogue's stats. If it's dark blue, it represents Kitty's."
                "Focus Button":
                    "You can switch between available girls by hitting the small blue icon to the right of the Relationship Bar." 
                    "This changes which girl is currently the focus of your attention. You can do this as often as you like."
                "Inventory":
                    "The small backpack to the left of that is your inventory."
                "Time":
                    "The next panel shows the day since you started, the day of the week, and the time of day."
                    "There are four periods in the day, Morning, Midday, Evening, and Night, representing roughly 4 hours each (not counting sleep time"   
                "Menus":
                    "Much of the gameplay choices are made via menus along the left side of the screen."
                    "Don't worry too much about making \"bad\" choices, they are only temporary setbacks."
                    "There are no absolute fail states, and even choices that upset a girl can have eventual payoffs."
                    "Play how you want to play, have fun."
                "Back":
                    jump Tutorial
    "Stats":
        menu Tutorial_Stats: 
            "Which stat were you interested in?"
            "Relationship Stats":
                "Stats are what is used to track your progress with the various girls in the mansion."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Love Stat":
                                "If you look at the top-left of the screen, there is a red bar."
                                "This represents the girl's \"love level.\""
                                "You can raise this stat by doing things that make the girl happy. This produces a red +X number."
                                $ Statupdate("Rogue", "Love", R_Love, 200, 1)
                                "You can also lower this number if you do things that make the girl upset, which is represented by a red -X."
                                $ Statupdate("Rogue", "Love", R_Love, 200, -1)
                        "Obedience Stat":
                                "The blue bar to the right of that is the \"Obedience level.\""
                                "This represents the girl's willingness to do what you want, and raises when you convince her to do something."
                                $ Statupdate("Rogue", "Obed", R_Obed, 200, 1)
                                "It lowers when you push her too far and she refuses."
                                $ Statupdate("Rogue", "Obed", R_Obed, 200, -1)
                        "Inhibition Stat":
                                "The yellow bar to the right of that is the \"Inhibition level.\""
                                "This represent's the girl's own sexual interest, and raises when she decides to do something on her own, or something naughty for the first time."
                                $ Statupdate("Rogue", "Inbt", R_Inbt, 200, 1)
                                "It lowers when she becomes overly ashamed, like when caught doing something sexier than she's comfortable with."
                                $ Statupdate("Rogue", "Inbt", R_Inbt, 200, -1)
                                "These are the three core relationship stats, and most activities in the game are gated by how high each is, either alone or in combinations."
                                "If you can reach 1000 in all three stats, she will be up for just about anything, although some activities do require special conditions." 
                        "Back":
                                jump Tutorial_Stats
            "Sexual stats":
                "There are several stats which are used in sexual encounters."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Lust":                    
                                "The bar underneath \"Love\" represents the girl's \"Lust.\""
                                "This stat raises as she becomes excited, and falls as she gets turned off or after she orgasms (at 100\%)."
                                $ Statupdate("Rogue", "Lust", R_Lust, 200, 1)
                                $ R_Lust -= 1
                        "Player Excitement":
                                "The rather \"suggestive\" bar to the right of Inhibitions represents your own excitement." 
                                $ Statupdate("Rogue", "Focus", P_Focus, 200, 1)
                                $ P_Focus -= 1
                                "When it reaches 100\%, you orgasm. If you wish to delay this, you can learn to \"focus\" during sex and slow the progression."                
                                "The better you get at each sexual activity, the faster these stats will rise."
                                "The bar underneath this represents the amount of times you can \"get it up\" before needing some time out. You can raise this stat when you level."
                                "It's also worth noting that each girl will only be up for doing a certain number of activities in a given time period."
                        "Back":
                                jump Tutorial_Stats                            
            "Player Stats":
                "Aside from the sexual ones mentioned above, the player has a few stats of note."                
                "One is his XP. This raises as you study, attend classes, or attend training sessions."
                "It represents your advancement as a mutant student of the academy. As you gain levels, you gain stat points."
                "You can spend these to unlock new traits, either refining your powers or your sexual prowess."
                "The girls also gain traits which unlock new abilities."
                "You also have an income level, based on the stipend Xavier grants you. This rises as you level, but may be reduced for bad behavior."            
            "Addiction":
                "The Addiction stat is represented by the bar below Obedience. This stat is unique to Rogue, and rises as she begins to crave your touch."
                "It lowers when she comes into physical contact with you, the more intense the contact, the lower the craving gets."
                "At high Addiction levels, she is highly susceptible to your advances, but will not be happy about it if you press her."
                "The Addiction Rate is represented by the bar to the right of it. This stat represents how quickly her cravings build, and falls off over time."
                "There are various ways that you can increase or decrease how addictive your touch becomes to her. Use this capability at your own risk." 
                "If this aspect does not interest you, you can just choose the more benign options to satisfy her cravings until her interest dies down."
            "Back":                
                jump Tutorial
        jump Tutorial_Stats
    "Activities":
        while True:
            menu:
                "So what can you do with your time?"
                "Wait/Sleep":
                    "You can always just \"Wait.\" This causes you to waste time, but who knows, maybe something interesting will happen."
                    "Of course when it's night time, this becomes \"Sleep.\" You can only sleep in your own room at first, but maybe someone else would let you sleep in her room."
                "Shop":
                    "You can also access the school's fabricator store, where you can order various items to be delivered to your room."
                "Class":
                    "You can always attend classes. These are typically not that interesting, but will raise your XP, and various events might occur in class."
                    "Classes are open during weekday morning and midday periods. You might bump into Rogue there."
                    "You can access the classroom by using \"Leave [[Go to Campus Square].\""
                        
                "Danger Room":
                    "You can also attend a Danger Room training session. These also raise your XP."
                    "The Danger Room is open any time except late at night (students need their sleep)."
                    "You can access the Danger Room by using \"Leave [[Go to Campus Square].\""
                "Shower": 
                    "You can also take a shower, but don't worry, you'll do that off camera automatically if you don't get around to it."
                    "You can access the showers by using \"Leave [[Go to Campus Square].\""
                "Study":
                    "You can also choose to study with one of the other students. This will gain you XP, and who knows what else might happen?"
                "Dating":    
                    "You can also go out on a date with one of the other students in the evenings. She will probably expect you to pay, so be prepared."
                "Chat":    
                    "And of course you can just hang out with one of the other students, or talk to them on the phone if you have their number." 
                "Back":                
                    jump Tutorial
              
    "Never mind.":
        return
jump Tutorial


label SpecialMenu:
    while True:
        menu:
            "Tutorial":
                jump Tutorial                        
            "Statchecker":
                    "This element will check all the stats and make sure that they work in your current savegame."
                    "This is a good idea if you're getting 'variable not found' syle errors."
                    menu:
                        "Do you want to do this?"
                        "Yes":
                            $ renpy.pop_call()
                            call Failsafe
                            jump Player_Room
                        "Never mind.":
                            pass
            "Visit McCoy's lab to change things about myself.":
                    call Hanks_Lab    
                   
            "Leveling Menu":
                while P_Lvl:
                    menu:
                        "Level Yourself":
                                call P_Level_Up
                        "Level Rogue":
                                call R_Level_Up 
                        "Level Kitty":
                                call K_Level_Up 
                        "Level Emma":
                                call E_Level_Up 
                        "Back":
                                jump SpecialMenu
                "You need to gain experience first by training or going to class."
                
            "Activate Travel Mode" if not TravelMode:
                    "This mode causes you to travel directly to adjacent areas, but not directly to more distant ones."
                    "If you would prefer to use the default, more \"world map\" style of travel, you can toggle this back off."
                    "You can use \"Leave\" to open the location directory." 
                    $ TravelMode = 1
            "Deactivate Travel Mode" if TravelMode:
                    $ TravelMode = 0
                    
            "Never mind.":
                return
    return
# end Tutorial//////////////////////////////////////////////////////////

# start Hank's Lab//////////////////////////////////////////////////////////
label Hanks_Lab(Line=0):
    "This is Professor McCoy's lab. You can do various self-modifications here."
    "The changes will be so seemless, it's almost like nobody will even notice!"
    while True:
        $ Line = 0
        menu:
            "What would you like to do?"
            "Alter skin color":  
                    menu:
                        "What skin color would you like?"        
                        "Green":
                            $ P_Color = "green"
                        "White":
                            $ P_Color = "pink"
                        "Black":
                            $ P_Color = "brown"
                        "Never mind":
                            $ Line = 1
                    if not Line:
                        "You fiddle with some of McCoy's machinery and a glowing blue liquid pours into a flask."                    
                        "You down it in a single gulp, and within minutes your skin tone shifts to be more [P_Color]ish."
                
            "Change my name.":
                    "You log in to McCoy's high end computer, this should allow you to change your name in all offical databases."  
                    $ Playername = renpy.input("What name would you like?", default="Zero", length = 10)
                    $ Playername = Playername.strip()        
                    if not Playername:
                       $ Playername = "Zero"
                    if Playername in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                        "Nice try, smartass."
                        $ Playername = "Zero"  
                    $ K_Petname = Playername[:1]                      
                    call LastNamer                         
                    $ E_Petnames.append(_return)
                    $ E_Petname = _return
                    "That should do it, your name has been updated and an email has been sent out to everyne on campus about the change."
                    
            "Leave.":
                    return
    
    return

# end Hank's Lab//////////////////////////////////////////////////////////



label Rogue_Frisky_Class:
    $ Line = 0        
    if E_Loc == "bg teacher":   
        "[EmmaName] is giving a lecture on mutant relations. In her seat next to you, you notice Rogue shifting uncomfortably in her seat."
    else:
        "Professor McCoy is giving a lecture on the X-Gene. In her seat next to you, you notice Rogue shifting uncomfortably in her seat."
    "Occasionally, you catch her glancing over your way."
    if not ApprovalCheck("Rogue", 600):
        jump Rogue_Frisky_Class_End
        
    "Rogue opens her notebook and begins scratching out a note. She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note. In looping penstrokes, it reads: {i}You like biology?{/i}"
    "You look back and see that she's blushing slightly. She slides her pen over to you so you can reply."
    menu:
        "You reply. . ."
        "What are you talking about?":
            pass
            
        "Naah. Not so much.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -3)
            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, -3)   
            call RogueFace("confused")    

        "It's my favorite subject.":
            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)   
            call RogueFace("smile")    
            "Rogue reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. {i}\"Then maybe we could study together tonight?\"{/i}." 
            $ Line = "continue"
        
        "I do when it's about you.":
            if ApprovalCheck("Rogue", 500, "I") or R_SEXP >= 30:  
                call RogueFace("sly")    
                "Rogue reads your note and smiles at you suggestively."
                $ Line = "flirt"
            elif ApprovalCheck("Rogue", 900):  
                call RogueFace("confused",2)    
                "Rogue reads your note and blushes furiously, looking down at her notes."
                $ R_Blush = 1
                $ Line = "flirt"                
            else: 
                call RogueFace("perplexed",2)  
                "Rogue reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. {i}\"I meant the class! Maybe we could study tonight?\"{/i}." 
                $ R_Blush = 1
                $ Line = "continue"
        
        
    if Line == "continue":
            "Rogue's drawn a little heart as the period at the bottom of the question mark." 
            "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."
            menu:
                "You respond. . ."
                "Maybe later.":                     
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -3)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, -3)  
                        call RogueFace("confused")
                        $ Line = 0
                "Naah. I've got better things to do.":
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, -3) 
                        $ Line = 0    
                        call RogueFace("angry")
                        $ R_DailyActions.append("angry")                          
                "Count on it.":
                        "She smiles when she reads your reply, and throws you a wink."
                        $ R_DailyActions.append("studydate")  
                        call RogueFace("smile")
                        jump Rogue_Frisky_Class_End
                "We could get some \"studying\" done right now.":
                        if ApprovalCheck("Rogue", 1200):
                            call RogueFace("sly",1)
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3) 
                            "Rogue gets a mischevious grin on her face and leans towards you."
                            $ Line = "flirt"
                        elif ApprovalCheck("Rogue", 700):
                            call RogueFace("smile",1)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2) 
                            "Rogue blushes and smiles your way."
                            $ Line = "flirt"
                        else:
                            call RogueFace("confused",1)
                            "Rogue looks a bit surprised, then scowls at you."
                            jump Rogue_Frisky_Class_End
                        
    #End if Line == "continue"
    
    if Line == "flirt":
            $ D20 = renpy.random.randint(1, 20)
            call RogueFace("sly")                
            "You notice one of Rogue's shoes slip from her foot beneath the desk. She tosses you a sly grin." 
            if R_Hose:
                "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
            else:
                "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."
                
            while D20 <= 21:
                menu:
                    extend ""                        
                    "Pull away from her.":
                            if Line == "fondle pussy":
                                    "You slowly slide your hand from her lap and start taking notes again."
                                    $ Line = "tease"                                
                            elif Line == "fondle breast":
                                    "With a final squeeze, you move your hand back to the desktop."
                                    $ Line = "tease"
                            else:
                                    $ Line = "rejected"
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, -15)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 2)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, -2) 
                            jump Rogue_Frisky_Class_End
                                
                    "Look into her eyes and smile slightly." if Line == "flirt": 
                            call RogueFace("smile")                
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 5)
                            "Rogue smiles back." 
                            "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."
                            $ Line = "handholding"                            
                    "Grasp her hand gently, stroking the top of it." if Line == "handholding":                         
                            $ R_Love = Statupdate("Rogue", "Love", R_Love, 200, 5)
                            call RogueFace("smile")                
                            "Rogue sighs contentedly and holds your hand for the remainder of class." 
                            jump Rogue_Frisky_Class_End
                                            
                    "Try and slip your hand to her lap." if Line != "fondle pussy":
                            $ Line = "fondle pussy"
                            if ApprovalCheck("Rogue", 1500) and R_FondleP and R_SEXP >= 40:
                                    call RogueFace("sly")           
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 90, 5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 5)      
                                    "Rogue gets a mischievous grin and places her hand on your arm."
                            elif ApprovalCheck("Rogue", 1800) and R_FondleP:
                                    call RogueFace("smile")                
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 7)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                                    "Rogue starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                            elif ApprovalCheck("Rogue", 2000):
                                    call RogueFace("perplexed",2)     
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)             
                                    "Rogue glances at you in alarm, but then slowly calms down." 
                                    call RogueFace("smile",1)                                           
                                    $ D20 += 2
                            else:
                                    $ Line = "too far"
                                    
                            if Line == "fondle pussy":
                                    call RogueFace("sly")    
                                    if R_Legs == "skirt":
                                        "Rogue's sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound." 
                                    elif R_Legs == "pants":
                                        "Rogue's sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound." 
                                    else: #No pants
                                        "Rogue's sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound." 
                                        
                                    if R_Panties == "shorts":
                                        "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                    elif R_Panties:
                                        "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                    elif R_Pubes:
                                        "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                    else:
                                        "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                                    $ D20 += 5

                    "Keep fondling her pussy." if Line == "fondle pussy":
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                            "As the class drones on, you continue to slowly massage her warm delta."
                            $ D20 += 5
                            
                    "Start fondling her tits." if Line != "fondle breasts":
                            $ Line = "fondle breasts"
                            if ApprovalCheck("Rogue", 1500) and R_FondleB and R_SEXP >= 40:
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 5)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                                    call RogueFace("sly")                
                                    "Rogue closes her eyes and caresses your arm."
                            elif ApprovalCheck("Rogue", 1800) and R_FondleB:
                                    $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, 3)
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 7)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                                    call RogueFace("smile",1)                
                                    "Rogue flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                            elif ApprovalCheck("Rogue", 2000):
                                    $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 10)
                                    $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 3)  
                                    call RogueFace("perplexed",2) 
                                    "Rogue glances at you in alarm, but then slowly calms down." 
                                    call RogueFace("smile",2) 
                                    $ D20 += 5
                            else:
                                    $ Line = "too far"
                                    
                            if Line == "fondle breasts":  
                                    call RogueFace("sly")                
                                    "Rogue's sly eyes spakle as your hand cups her breast, giving it a casual caress." 
                                    "her nipples begin to firm up and she lets out a small moan of pleasure."
                                    $ D20 += 7
                    "Keep fondling her tits." if Line == "fondle breasts":
                            $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 5)
                            $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 60, 2)  
                            "Barely paying attention to the lecture, you continue to pulse her breast in your palm."
                            $ D20 += 7
                                    
                if Line == "too far":
                        call RogueFace("surprised",2)   
                        $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -5)
                        $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, 7)
                        $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -3)               
                        "Rogue sits up straight in her seat and makes a little yelping noise." 
                        call RogueFace("angry",1)                
                        "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."
                        $ D20 += 10
                
            #After D20:
            if Line not in ("rejected", "handholding", "tease"):                
                $ R_Love = Statupdate("Rogue", "Love", R_Love, 80, -10)
                $ R_Obed = Statupdate("Rogue", "Obed", R_Obed, 70, -5)
                $ R_Inbt = Statupdate("Rogue", "Inbt", R_Inbt, 50, -10)  
                call RogueFace("surprised")      
                if E_Loc == "bg teacher":                   
                        "[EmmaName] stops her lecture in mid-sentence when she notices that the whole class is looking at you and Rogue." 
                        ch_e "[E_Petname], Rogue, if you could perhaps pay more attention to the lecture, and less to each other's bodies?"                
                        ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                else:
                        "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and Rogue." 
                        ch_b "Oh, my stars and garters!"                
                        ch_b "[Playername]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"
                if Rules:
                        jump Rogue_Caught
                else:
                        "Since Xavier isn't concerned with your activities, you both head back to your room instead."
                        $ R_Loc = "bg player"
                        call CleartheRoom("Rogue",0,1)
                        jump Player_Room
                    
    
label Rogue_Frisky_Class_End:  
    if not Line:        
            call RogueFace("confused")
            "She unfolds the note and quickly reads it over." 
            call RogueFace("sad")
            "As she does, you immediately see disappointment come over her features." 
            "She scratches out a reply and slides it back in front of you." 
            "When you open it up, it reads: {i}Never mind.{/i}"   
    elif Line == "tease":        
            call RogueFace("sly",1)
            "Rogue takes in a deep breath and exhales it in a sigh, leaning in to whisper." 
            ch_r "Tonight's \"study session\" just got a whole lot more interesting." # attempt smaller text?
    elif Line == "rejected":
            call RogueFace("sadside")
            "Rogue looks surprised and hurt. For the rest of the class, she says nothing." 
            "It seems like she has a hard time looking you in the eye."
    
    "Eventually, Rogue seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    return