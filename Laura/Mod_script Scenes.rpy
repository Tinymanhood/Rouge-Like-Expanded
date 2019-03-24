label Sleepover(Lead=0,Sleep=0,Room=0,Line = 0):
            #This event gets called from Round10, should never be called without the room's owner
            # If there's a Lead, she's been sent to this from elsewhere
            # Sleep tracks number of previous sleepovers

            $ Party = []
            if R_Loc == bg_current:
                    $ Party.append("Rogue")
            if K_Loc == bg_current:
                    $ Party.append("Kitty")
            if E_Loc == bg_current:
                    $ Party.append("Emma")
            if newgirl["Laura"].Loc == bg_current:
                    $ Party.append("Laura")
            if not Party and bg_current == "bg player":
                    #if nobody is around.
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "It's getting late, so you go to sleep."
                    call Wait
                    return    
                      
            while len(Party) > 2:  
                    #culls out extra members
                    $ Party.remove(Party[2])
                            
            if Day <= 7:
                    # prevents anyone agreeing before day 7.
                    $ Party = [0]   
            elif Party and Party[0]:            
                    call Shift_Focus(Party[0])
            
            if bg_current == "bg rogue":
                    $ Room = "Rogue"
            elif bg_current == "bg kitty":
                    $ Room = "Kitty"          
            elif bg_current == "bg emma":
                    $ Room = "Emma"
            elif bg_current == "bg laura":
                    $ Room = "Laura"
            elif bg_current == "bg player":
                    $ Room = "Player"
            else:
                    #it's somehow not any room?
                    "Tell Oni you're in room [bg_current] somehow."
            
            if Room not in Party and bg_current != "bg player":
                    # If the owner of the room isn't in the party
                    if Sleep >= 5 and not Party: 
                                #If you've slept in that room many times but she isn't home
                                "She probably wouldn't mind you taking a quick nap. . ."
                                call Wait
                                call DrainWord(Room,"arriving")
                                if bg_current == R_Loc:
                                        ch_r "Morning, [R_Petname]. Sleep well?" 
                                if bg_current == K_Loc:
                                        ch_k "Well morning, sleepy head."
                                if bg_current == E_Loc:
                                        ch_e "Well look whos sleeping in my bed. . ."
                                if bg_current == newgirl["Laura"].Loc:
                                        ch_l "Ah, you're up."
                                return
                    else:
                                #either another girl is around or she wouldn't want you sleeping there
                                "She probably wouldn't appreciate you staying over, you head back to your own room."
                                $ renpy.pop_call()
                                jump Player_Room
                                
            # the previous statemetn should cull out all situations where the owner isn't there
            if Room == "Player":
                    if len(Party) == 2:                    
                        $ renpy.random.shuffle(Party)
                        if ApprovalCheck(Party[0],Check=1) <= ApprovalCheck(Party[1],Check=1):
                            # If second one likes you more, pick her
                            $ Party.reverse()   
                    if Party[0] == "Rogue":
                        ch_r "It's getting late and I'm getting a bit tired."  
                        $ Sleep = R_Sleep               
                    elif Party[0] == "Kitty": 
                        ch_k "It's late, I'm thinking of heading out. . ." 
                        $ Sleep = K_Sleep
                    elif Party[0] == "Emma":            
                        ch_e "It's late, I should be going. . ."  
                        $ Sleep = E_Sleep
                    elif Party[0] == "Laura":            
                        ch_l "I need some sleep. . ."  
                        $ Sleep = newgirl["Laura"].Sleep
            elif Room == "Rogue":
                    ch_r "It's getting late and I'm turning in."
                    $ Sleep = R_Sleep     
                    if Party[0] != "Rogue":
                            $ Party.reverse()  
            elif Room == "Kitty":
                    ch_k "I'm getting kinda tired. . ."
                    $ Sleep = K_Sleep     
                    if Party[0] != "Kitty":
                            $ Party.reverse() 
            elif Room == "Emma":
                    ch_e "It's getting late, [E_Petname]. . ."
                    $ Sleep = E_Sleep     
                    if Party[0] != "Emma":
                            $ Party.reverse() 
            elif Room == "Laura":
                    ch_l "I'm tired. . ."
                    $ Sleep = newgirl["Laura"].Sleep     
                    if Party[0] != "Laura":
                            $ Party.reverse() 
            else:
                "Something went wrong." 
                "Tell Oni \"[Party] - [bg_current] - [Room]\""
                    
            
            if Day <= 7:
                    # If it's too early for sleepovers, 
                    jump Return_Player               
                
            if "Emma" in Party and len(Party) >= 2 and "three" not in E_History:
                    #if Emma's around but can't do threesome stuff yet
                    if (Room == "Emma" or Room == "Player") and ApprovalCheck("Emma", 1100, "LI"):
                        if Party[0] != "Emma":
                                $ Party.reverse() 
                        ch_e "[Party[1]] dear, I need a moment with [Playername], but you can leave." 
                        call AnyFace(Party[1],"confused",1)                           
                        call AnyLine(Party[1],"Oh, ok. . .")                            
                        call Remove_Girl(Party[1])
                        ch_e "Sorry about that, but I had to discuss something with you in private."
                    else:
                        #if it's not her room, or she doesn't like you enough to stay
                        ch_e "Yes, I really should be leaving, don't let me bother you two."                        
                        call Remove_Girl("Emma")
                    if "sleeptime" not in E_History:
                        $ E_History.append("sleeptime")
                            
            call AnyFace(Party[0],"sexy",1)
            
            if Sleep >= 3 and ApprovalCheck(Party[0], 800):                                 
                    #You've slept over several times and she still likes you
                    if Party[0] == Room:
                            $ Line = "Are you staying over tonight?"
                    else:
                            $ Line = "I'm staying over, right?"
                    call AnyLine(Party[0],Line)
                
            elif Sleep < 3 and ApprovalCheck(Party[0], 1100, "LI"):                        
                    #You haven't slept over much, but she wants you to
                    call AnyFace(Party[0],"bemused",1)
                    if Party[0] == "Rogue":
                            if bg_current == "bg rogue":
                                ch_r "I was thinking. . . maybe you wanted to stay the night?"  
                            else:
                                ch_r "I was thinking. . . maybe I could stay the night?" 
                    elif Party[0] == "Kitty":
                            if bg_current == "bg kitty":
                                ch_k "So[K_like]did you want to stay over?"  
                            else:
                                ch_k "So[K_like]could I stay over?"
                    elif Party[0] == "Emma":
                            if bg_current == "bg emma":
                                ch_e "I was wondering, have you considered staying over?"  
                            else:
                                ch_e "I was wondering, could I stay over?" 
                    elif Party[0] == "Laura":
                            if bg_current == "bg laura":
                                ch_l "So, are you staying over?"  
                            else:
                                ch_l "So, can I stay here tonight?" 
                    $ Line = 1
                    
            else: #If she's uninterested                
                    if Party[0] == "Rogue":
                            if bg_current == "bg rogue":
                                ch_r "You should get going." 
                            else:
                                ch_r "I'm heading out, see you tomorrow."
                    elif Party[0] == "Kitty":
                            if bg_current == "bg kitty":
                                ch_k "You should[K_like]head out." 
                            else:
                                ch_k "See ya tomorrow, [K_Petname]."
                    elif Party[0] == "Emma":
                            if bg_current == "bg emma":
                                ch_e "Could you please clear the room?"
                            else:
                                ch_e "I should leave." 
                    elif Party[0] == "Laura":
                            if bg_current == "bg laura":
                                ch_l "Clear out."
                            else:
                                ch_l "So, later." 
            
            if Line:
                #she offered to sleep over
                menu:
                    extend ""
                    "Sure.":
                            if Sleep <= 5:
                                call Statup(Party[0], "Love", 70, 10)
                                call Statup(Party[0], "Obed", 80, 10)
                                call Statup(Party[0], "Obed", 50, 20)
                                call Statup(Party[0], "Inbt", 25, 20)              
                            call Statup(Party[0], "Love", 70, 5) 
                            call AnyFace(Party[0],"smile")
                            # Line = 1
                        
                    "No, sorry.":                  
                            call Statup(Party[0], "Obed", 50, 2)
                            call Statup(Party[0], "Obed", 30, 5)
                            call Statup(Party[0], "Inbt", 40, 3) 
                            call AnyFace(Party[0],"sad")
                            $ Line = 0
                            if Party[0] == "Rogue":
                                    ch_r "Ok, see you tomorrow then. 'Night."                
                            elif Party[0] == "Kitty":
                                    ch_k "Alright. . . see you tomorrow. . ."
                            elif Party[0] == "Emma":
                                    ch_e "Well, if you insist. See you tomorrow then."
                            elif Party[0] == "Laura":
                                    ch_l "Ok."  
                            
                            
            else:
                #if she didn't offer to sleep over
                menu: 
                    extend ""
                    "Ok, I'll head out. Good night." if Party[0] == Room:    
                            #if she didn't agree and this is her room
                            $ Line = "leave"
                    "Ok, see you later then. Good night." if Party[0] != Room:     
                            #if she didn't agree and this is not her room    
                            $ Line = "leave"   
                        
                    "Are you sure I can't stay the night? . ." if not Sleep and Party[0] == Room: 
                            $ Line = "please"   
                    "Are you sure you can't stay? . ." if not Sleep and Party[0] != Room: 
                            $ Line = "please"   
                                
                    "That's not what you said the other night . ." if Sleep: 
                            #if she wants you gone  
                            if ApprovalCheck(Party[0],900)or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                                call AnyFace(Party[0],"bemused",1)  
                                $ Line = 1       
                                if Party[0] == "Rogue":
                                        ch_r "Well. . . that didn't turn out so bad, I suppose. . ."              
                                elif Party[0] == "Kitty":      
                                        ch_k "and that went pretty well. . ."
                                elif Party[0] == "Emma":
                                        ch_e "It was a nice evening."
                                elif Party[0] == "Laura":
                                        ch_l "Yeah, it was."   
                            else:                    
                                call AnyFace(Party[0],"smile",Brows="confused")
                                # Line = 0
                                if Party[0] == "Rogue":
                                        ch_r "I'm afraid not this time, [R_Petname]. I'll see you later."               
                                elif Party[0] == "Kitty":
                                        ch_k "Um, no, 'fraid not. I'll see ya tomorrow." 
                                elif Party[0] == "Emma":
                                        ch_e "Well, not tonight, [E_Petname]."
                                elif Party[0] == "Laura":
                                        ch_l "Yeah, but not this time."  
                                if Party[0] == Room:
                                        #if it's a girl's room, you leave.
                                        ch_p "Ok, I'll be going then."   
                #if she didn't offer to sleep over
        
            if Line == "leave":           
                # if you agreed to leave
                call Statup(Party[0], "Love", 90, 3)
                call Statup(Party[0], "Inbt", 25, 2)    
                call AnyFace(Party[0],"smile") 
                $ Line = 0 
                if Party[0] == "Rogue":
                        ch_r "Yeah, good night, [R_Petname]. . ."                
                elif Party[0] == "Kitty":
                        ch_k "Yeah, 'night, [K_Petname]. . ."
                elif Party[0] == "Emma":
                        ch_e "Yes, good night, [E_Petname]."
                elif Party[0] == "Laura":
                        ch_l "Ok, good night then."
                        
            if Line == "please": 
                #if she said no but you asked nicely
                if ApprovalCheck(Party[0],1000) or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                    call AnyFace(Party[0],"bemused") 
                    $ Line = 1 
                    if Party[0] == "Rogue":
                            ch_r "Well. . . I suppose it would be alright."                
                    elif Party[0] == "Kitty":
                            ch_k "Well, Maaaybeee. . ."
                    elif Party[0] == "Emma":
                            ch_e "I suppose we could make an exception. . ."
                    elif Party[0] == "Laura":
                            ch_l "Suit yourself."                    
                else:                    
                    call AnyFace(Party[0],"smile",Brows="confused")
                    $ Line = 0
                    if Party[0] == "Rogue":
                            ch_r "I'm afraid not, [R_Petname]. Head home, I'll see you later."               
                    elif Party[0] == "Kitty":
                            ch_k "Ehhhh. . . no, not tonight, [K_Petname]. Sorry." 
                    elif Party[0] == "Emma":
                            ch_e "I'm afraid not."
                    elif Party[0] == "Laura":
                            ch_l "Don't push it."

            if not Line:
                #if the primary girl refused to sleep over
                if Room == Party[0]:
                        #if it's her room, removes any other girls around
                        call CleartheRoom(Party[0],1)    
                        jump Return_Player                        
                else:   
                        #if it's not her room, remove her, and try again
                        call Remove_Girl(Party[0])
                        call Sleepover
                      
            #If the primary girl agreed  
            if len(Party) >= 2:
                #if there is another girl
                if GirlLikeCheck(Party[0],Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                        # If she likes the other girl quite a bit and likes you a decent amount
                        if Party[0] == "Rogue":
                                ch_r "And you, [Party[1]]?"                   
                        elif Party[0] == "Kitty":
                                ch_k "How about you, [Party[1]]?"
                        elif Party[0] == "Emma":
                                ch_e "And what about you, [Party[1]]?"
                        elif Party[0] == "Laura":
                                ch_l "And you, [Party[1]]?"
                else:
                        if Party[0] == "Rogue":
                                ch_r "Are you leaving, [Party[1]]?"                   
                        elif Party[0] == "Kitty":
                                ch_k "You heading out, [Party[1]]?"
                        elif Party[0] == "Emma":
                                ch_e "I assume you're leaving, [Party[1]]?"
                        elif Party[0] == "Laura":
                                ch_l "Later, [Party[1]]."
                                
                if GirlLikeCheck(Party[1],Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                        # If second girl likes the other girl a bit and likes you a decent amount  
                        call AnyFace(Party[1],"smile") 
                        if Party[1] == "Rogue":
                                ch_r "I'd like to stay too."                   
                        elif Party[1] == "Kitty":
                                ch_k "Can I stay too?"
                        elif Party[1] == "Emma":
                                ch_e "I'd rather join the fun."
                        elif Party[1] == "Laura":
                                ch_l "Me too, right?"
                        $ Line = 1
                else:  
                        call AnyFace(Party[0],"smile",1) 
                        if Party[1] == "Rogue":
                                ch_r "I guess I should be going."                   
                        elif Party[1] == "Kitty":
                                ch_k "I should go, right?"
                        elif Party[1] == "Emma":
                                ch_e "I suppose three is a crowd."
                        elif Party[1] == "Laura":
                                ch_l "I should leave."
                        $ Line = 0
                menu:
                    extend ""
                    "You should stay, [Party[1]].":
                            #this checks the second girl's response.
                            if GirlLikeCheck(Party[1],Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):
                                    # If second girl likes the first girl a bit and likes you a decent amount
                                    if Party[1] == "Rogue":
                                            ch_r "Oh, I'd love to."                   
                                    elif Party[1] == "Kitty":
                                            ch_k "Roomies!"
                                    elif Party[1] == "Emma":
                                            ch_e "I'd love to."
                                    elif Party[1] == "Laura":
                                            ch_l "Great."
                                    $ Line = 1
                            else:  
                                    call AnyFace(Party[1],"sadside",1,Mouth="smile") 
                                    if Party[1] == "Rogue":
                                            ch_r "I don't want to be a bother."                   
                                    elif Party[1] == "Kitty":
                                            ch_k "No way."
                                    elif Party[1] == "Emma":
                                            ch_e "I couldn't."
                                    elif Party[1] == "Laura":
                                            ch_l "Nah."
                                    $ Line = 0
                            
                            #This checks the first girl's response
                            if Line:
                                if GirlLikeCheck(Party[0],Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):
                                    # If first girl likes the other girl quite a bit and likes you a decent amount
                                    if Party[0] == "Rogue":
                                            ch_r "Great!"                   
                                    elif Party[0] == "Kitty":
                                            ch_k "Roomies!"
                                    elif Party[0] == "Emma":
                                            ch_e "Lovely."
                                    elif Party[0] == "Laura":
                                            ch_l "Ok."  
                                elif GirlLikeCheck(Party[0],Party[1]) >= 400 and ApprovalCheck(Party[0], 1400):
                                    # If she barely likes the other girl but likes you a a lot
                                    call AnyFace(Party[0],"sadside",1,Mouth="smile") 
                                    if Party[0] == "Rogue":
                                            ch_r "Sure, I guess."                   
                                    elif Party[0] == "Kitty":
                                            ch_k "Um, Ok."
                                    elif Party[0] == "Emma":
                                            ch_e "I suppose we could find room for one more."
                                    elif Party[0] == "Laura":
                                            ch_l "Whatever."
                                else:
                                    call AnyFace(Party[0],"angry",1) 
                                    if Party[0] == "Rogue":
                                            ch_r "I'm not cool with that."                   
                                    elif Party[0] == "Kitty":
                                            ch_k "No way."
                                    elif Party[0] == "Emma":
                                            ch_e "I don't think so."
                                    elif Party[0] == "Laura":
                                            ch_l "Um, no."
                                    $ Line = 0
                    
                    "You should get going, [Party[1]].":
                            if Party[1] == "Rogue":
                                    ch_r "Oh, ok."                   
                            elif Party[1] == "Kitty":
                                    ch_k "Yeah."
                            elif Party[1] == "Emma":
                                    ch_e "I assumed."
                            elif Party[1] == "Laura":
                                    ch_l "Yeah."
                            $ Line = 0
                            
            if Line == 0:
                #if the second girl got the boot:
                if len(Party) >= 2:
                    if Party[0] == "Rogue":
                            ch_r "Later, [Party[1]]."                   
                    elif Party[0] == "Kitty":
                            ch_k "Night, [Party[1]]." 
                    elif Party[0] == "Emma":
                            ch_e "Goodnight, [Party[1]]." 
                    elif Party[0] == "Laura":
                            ch_l "Night." 
                        
                    if Party[1] == "Rogue":
                            ch_r "Later guys."                   
                    elif Party[1] == "Kitty":
                            ch_k "Night." 
                    elif Party[1] == "Emma":
                            ch_e "Goodnight." 
                    elif Party[1] == "Laura":
                            ch_l "Night." 
                if Party:        
                    call CleartheRoom(Party[0],1,1) #removes any other girls around   
            
            if Party:
                    jump Sleepover_Morning
            else:
                    #if nobody is around.
                    $ bg_current = "bg player"
                    call CleartheRoom("All",1)
                    #if nobody is here, you just go to sleep
                    "It's getting late, so you go to sleep."
                    call Wait
                    return    
                    
            jump Return_Player

  
label Return_Player_:    
        # This label is jumped to by the Sleep labels if the player or girl leaves after a sleepover (fail state).
        $ del Party[:]
        if bg_current != "bg rogue" and R_Loc == bg_current:
                "Rogue heads out."        
                $ R_Loc = "bg rogue"
        if bg_current != "bg kitty" and K_Loc == bg_current:
                "Kitty heads out."        
                $ K_Loc = "bg kitty"
        if bg_current != "bg emma" and E_Loc == bg_current:
                "Emma heads out."        
                $ E_Loc = "bg emma"
        if bg_current != "bg laura" and newgirl["Laura"].Loc == bg_current:
                "Laura heads out."        
                $ newgirl["Laura"].Loc = "bg laura"
        if bg_current != "bg player":
                "You head back to your room."
        $ bg_current = "bg player"
        call Set_The_Scene
        $ renpy.pop_call()
        jump Player_Room
          
label Sleepover_Morning:
        #This label is jumped too from Sleepover if you successfully stay the night
        if R_Loc == bg_current and "Rogue" not in Party:
               call Remove_Girl("Rogue")
        if K_Loc == bg_current and "Kitty" not in Party:
               call Remove_Girl("Kitty")
        if E_Loc == bg_current and "Emma" not in Party:
               call Remove_Girl("Emma")
        if newgirl["Laura"].Loc == bg_current and "Laura" not in Party:
               call Remove_Girl("Laura")
        call Shift_Focus(Party[0])            
        call AnyOutfit(Party[0],"sleep")
        if len(Party) >= 2:
                #If there are two girls. . .       
                call AnyOutfit(Party[1],"sleep")
                "The girls change into their sleepwear."
        else:        
                "[Party[0]] changes into her sleepwear."
        
        if Party[0] == "Rogue":
                ch_r "Hmm, that's a bit more comfortable."  
                $ Sleep = R_Sleep    
                $ R_Traits.append("sleepover")
        elif Party[0] == "Kitty":
                ch_k "Ah, that's better."
                $ Sleep = K_Sleep
                $ K_Traits.append("sleepover")
        elif Party[0] == "Emma":
                ch_e "Mmmm, that's better." 
                $ Sleep = E_Sleep
                $ E_Traits.append("sleepover")
        elif Party[0] == "Laura":
                ch_l ". . ."
                $ Sleep = newgirl["Laura"].Sleep
                $ newgirl["Laura"].Traits.append("sleepover")
                
        if len(Party) >= 2:
                if Party[1] == "Rogue":
                        ch_r "Let's turn in."    
                        $ R_Traits.append("sleepover")               
                elif Party[1] == "Kitty":
                        ch_k "Night, [K_Petname]"
                        $ K_Traits.append("sleepover")    
                elif Party[1] == "Emma":
                        ch_e "Lights out." 
                        $ E_Traits.append("sleepover")    
                elif Party[1] == "Laura":
                        ch_l "Night."
                        $ newgirl["Laura"].Traits.append("sleepover")    
        else:
                if Party[0] == "Rogue":
                        ch_r "Let's turn in."                    
                elif Party[0] == "Kitty":
                        ch_k "Night, [K_Petname]"
                elif Party[0] == "Emma":
                        ch_e "Goodnight." 
                elif Party[0] == "Laura":
                        ch_l "Night."
            
        show blackscreen onlayer black    
        pause 1
        call Wait(0,0) #shouldn't change outfit or lighting 
        $ Party = []
        if "sleepover" in R_Traits: 
                $ R_Loc = bg_current
                $ Party.append("Rogue")
        elif R_Loc == bg_current:
               call Remove_Girl("Rogue")
        if "sleepover" in K_Traits:
                $ K_Loc = bg_current
                $ Party.append("Kitty")
        elif K_Loc == bg_current:
               call Remove_Girl("Kitty")
        if "sleepover" in E_Traits:
                $ E_Loc = bg_current
                $ Party.append("Emma")
        elif E_Loc == bg_current:
               call Remove_Girl("Emma")
        if "sleepover" in newgirl["Laura"].Traits:
                $ newgirl["Laura"].Loc = bg_current
                $ Party.append("Laura") 
        elif newgirl["Laura"].Loc == bg_current:
               call Remove_Girl("Laura")
               
        call AnyOutfit(Party[0],"sleep",Perm=1)
        if len(Party) >= 2:
                call AnyOutfit(Party[1],"sleep",Perm=1)
        
        call Morningwood_Check
                                
        call AnyFace(Party[0],"smile")
        if len(Party) >= 2:
                call AnyFace(Party[1],"smile")
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        if "morningwood" in P_DailyActions:
            if Party[0] == "Rogue":
                    ch_r "So, that aside, Sleep well?"             
            elif Party[0] == "Kitty":
                    ch_k "So anyway. . . G'morning . . ."
            elif Party[0] == "Emma":
                    ch_e "Now that we've got that out of our system. . ."
                    ch_e "Morning, [E_Petname]."
            elif Party[0] == "Laura":
                    ch_l "Anyway, 'Morning."
        else:
            if Party[0] == "Rogue":
                    ch_r "'Morning [R_Petname]. Sleep well?"             
            elif Party[0] == "Kitty":
                    ch_k "G'morning . . ."
            elif Party[0] == "Emma":
                    ch_e "Hrmph. . ."
                    ch_e "Oh. You're here."
            elif Party[0] == "Laura":
                    ch_l "'Morning."     
                
        menu:
            extend ""
            "It's always nice sleeping with you." if Sleep: 
                    if Sleep < 5:
                        call Statup(Party[0], "Love", 90, 8)
                        call Statup(Party[0], "Obed", 50, 10)
                        call Statup(Party[0], "Inbt", 70, 8)   
                    call AnyFace(Party[0],B=1)
                    
                    if Party[0] == "Rogue":
                            ch_r "Aw, that's right sweet of ya, [R_Petname]."
                            ch_r "We'll have to keep this regular."          
                    elif Party[0] == "Kitty":
                            ch_k "And that's always nice to hear."
                            ch_k "We'll have to keep this up."
                    elif Party[0] == "Emma":
                            ch_e "Well. . ."
                            ch_e "We'll have to make a habit of it then."
                    elif Party[0] == "Laura":
                            ch_l "Yeah. . ."
                            ch_l "Warm. . ."
                
            "I loved sleeping next to you." if not Sleep:
                    call Statup(Party[0], "Love", 90, 15)
                    call Statup(Party[0], "Love", 70, 10)
                    call Statup(Party[0], "Obed", 50, 12)
                    call Statup(Party[0], "Inbt", 70, 12)
                    $ Line = "nice"
                    
            "It was fun.":
                    if not Sleep:                    
                        call Statup(Party[0], "Love", 90, 10)
                        call Statup(Party[0], "Love", 70, 8)
                        call Statup(Party[0], "Obed", 50, 15)
                        call Statup(Party[0], "Inbt", 70, 15)
                    elif Sleep < 5:
                        call Statup(Party[0], "Love", 70, 8)
                        call Statup(Party[0], "Obed", 80, 10)
                        call Statup(Party[0], "Inbt", 35, 8)    
                    call Statup(Party[0], "Obed", 50, 8)       
                    if ApprovalCheck(Party[0], 800, "L"):
                        call AnyFace(Party[0],"bemused")
                    else:
                        call AnyFace(Party[0],"confused")
                        
                    if Party[0] == "Rogue":
                            ch_r "Ok, well glad I wasn't {i}too{/i} much bother."       
                    elif Party[0] == "Kitty":
                            ch_k "Yeah, I mean I guess it was. . ."
                    elif Party[0] == "Emma":
                            ch_e "\"Fun\" is certainly how I would describe it."
                    elif Party[0] == "Laura":
                            ch_l "Yeah, I guess?"
                            
            "You were constantly tossing around.":    
                    call AnyFace(Party[0],B=1)
                    if ApprovalCheck(Party[0], 800, "L") or ApprovalCheck(Party[0], 1200):
                        call AnyFace(Party[0],"bemused")     
                        call AnyLine(Party[0],"Hmm?")
                    else:
                        call AnyFace(Party[0],"angry")     
                        call AnyLine(Party[0],"!!!")
                    if Sleep < 5:                       
                        if Party[0] == "Rogue":
                                ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                        elif Party[0] == "Kitty":
                                ch_k "I don't make a habit out of it. . ."    
                        elif Party[0] == "Emma":
                                ch_e "I haven't had a lot of practice lately."
                        elif Party[0] == "Laura":
                                ch_l "Deal with it."                                
                        call Statup(Party[0], "Love", 60, -8)
                        call Statup(Party[0], "Obed", 50, 22)
                        call Statup(Party[0], "Inbt", 50, 22)                   
                    else:
                        if Party[0] == "Rogue":
                                ch_r "Well you should probably be used to that by now."     
                        elif Party[0] == "Kitty":
                                ch_k "Yeah, well. . . you should be used to that!"
                        elif Party[0] == "Emma":
                                ch_e "I don't plan on changing any time soon."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, it'll be like that."
                    $Line = "toss"
                                
            "You need to learn to stick to your side.":  
                    if Sleep < 5:
                        call Statup(Party[0], "Love", 80, -8)
                        call Statup(Party[0], "Obed", 50, 40)
                    if ApprovalCheck(Party[0], 500, "O"):
                        call Statup(Party[0], "Love", 80, -2)
                        call Statup(Party[0], "Obed", 90, 5)
                        call AnyFace(Party[0],"normal")
                        if Party[0] == "Rogue":
                                ch_r "Yes, [R_Petname], I'll try my best."
                        elif Party[0] == "Kitty":
                                ch_k "Fine, whatever."
                        elif Party[0] == "Emma":
                                ch_e "I do try."
                        elif Party[0] == "Laura":
                                ch_l "Ok."
                        if Sleep < 5:
                                call Statup(Party[0], "Obed", 80, 8)
                    else:
                        call AnyFace(Party[0],"angry")
                        call Statup(Party[0], "Obed", 90, 5)
                        if Party[0] == "Rogue":
                                ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                        elif Party[0] == "Kitty":
                                ch_k "That's not how you get me to come back." 
                        elif Party[0] == "Emma":
                                ch_e "I'll sleep how I please."
                        elif Party[0] == "Laura":
                                ch_l "Good luck with that."
                        if Sleep < 5:
                                call Statup(Party[0], "Inbt", 35, 20) 
                    $Line = "toss"
                                                                
        if not Sleep and Line == "nice":  
                if Party[0] == "Rogue":
                        $ R_Blush = 1
                        ch_r "Aw, that's right sweet of ya, [R_Petname]."
                        ch_r "Makes me want to do it again sometime."       
                elif Party[0] == "Kitty":
                        $ K_Blush = 2
                        ch_k "Yeah, I. . [K_like]I had fun too."
                        $ K_Blush = 1
                        ch_k "I wouldn't[K_like]mind doing it again."   
                        $ K_Blush = 2
                        ch_k "You know, some other time. . . "
                        $ K_Blush = 1
                elif Party[0] == "Emma":
                        call EmmaFace("smile",1)
                        ch_e "You're a hopeless romantic, [E_Petname]."
                        call EmmaFace("smile",2,Eyes="side")
                        ch_e "I suppose I can be a bit hopeless too. . ."
                elif Party[0] == "Laura":
                        call LauraFace("confused",1)
                        ch_l "Oh. . ."
                        call LauraFace("surprised",2,Brows="confused")
                        ch_l "Yeah, so did I, now that you mention it. . ."
                        call LauraFace("confused",1)
                        ch_l "Huh."
                            
        call AnyFace(Party[0],B=0)
            
        if len(Party) >= 2:        
            #second girl's lines
            if "morningwood" in P_DailyActions:
                if Party[1] == "Rogue":
                        ch_r "And what about me?"   
                        $ Sleep = R_Sleep                     
                elif Party[1] == "Kitty":
                        ch_k "Me too?"
                        $ Sleep = K_Sleep           
                elif Party[1] == "Emma":
                        ch_e "And me?"
                        $ Sleep = E_Sleep           
                elif Party[1] == "Laura":
                        ch_l "Ung, 'morning."
                        $ Sleep = newgirl["Laura"].Sleep           
            else:            
                "[Party[1]] rolls over in bed."
                if Party[1] == "Rogue":                        
                        ch_r "Mmm, yeah, 'Morning [R_Petname]."  
                        $ Sleep = R_Sleep           
                elif Party[1] == "Kitty":
                        ch_k "Yeah, G'morning . . ."
                        $ Sleep = K_Sleep
                elif Party[1] == "Emma":
                        ch_e "Hrmph. . ."
                        ch_e "Oh. Not so loud, you two."
                        $ Sleep = E_Sleep
                elif Party[1] == "Laura":
                        ch_l "Yeah, 'Morning."
                        $ Sleep = newgirl["Laura"].Sleep
                    
            menu:
                extend ""
                "I always love sleeping with you too, [Party[1]]." if Sleep: 
                        if Sleep < 5:
                            call Statup(Party[1], "Love", 90, 8)
                            call Statup(Party[1], "Obed", 50, 10)
                            call Statup(Party[1], "Inbt", 70, 8)   
                        call AnyFace(Party[1],B=1)
                        
                        if Party[1] == "Rogue":
                                ch_r "That's sweet of ya to say, [R_Petname]."
                        elif Party[1] == "Kitty":
                                ch_k "So cute!"
                        elif Party[1] == "Emma":
                                ch_e "Mmmm. . . yes, lovely."
                        elif Party[1] == "Laura":
                                ch_l "Sure. . ."
                    
                "And it was great sleeping with you as well, [Party[1]]." if not Sleep:
                        call Statup(Party[1], "Love", 90, 15)
                        call Statup(Party[1], "Love", 70, 10)
                        call Statup(Party[1], "Obed", 50, 12)
                        call Statup(Party[1], "Inbt", 70, 12)
                        $ Line = "nice"
                        
                "I had fun sleeping with you too, [Party[1]].":
                        if not Sleep:                    
                            call Statup(Party[1], "Love", 90, 10)
                            call Statup(Party[1], "Love", 70, 8)
                            call Statup(Party[1], "Obed", 50, 15)
                            call Statup(Party[1], "Inbt", 70, 15)
                        elif Sleep < 5:
                            call Statup(Party[1], "Love", 70, 8)
                            call Statup(Party[1], "Obed", 80, 10)
                            call Statup(Party[1], "Inbt", 35, 8)    
                        call Statup(Party[1], "Obed", 50, 8)       
                        if ApprovalCheck(Party[1], 800, "L"):
                            call AnyFace(Party[1],"bemused")
                        else:
                            call AnyFace(Party[1],"confused")
                            
                        if Party[1] == "Rogue":
                                ch_r "Yeah, uh, fun."       
                        elif Party[1] == "Kitty":
                                ch_k "Yeah, I mean I guess it was. . ."
                        elif Party[1] == "Emma":
                                ch_e "\"Fun\" is certainly how I would describe it."
                        elif Party[1] == "Laura":
                                ch_l "Yeah, I guess?"
                        $Line = "fun"
                                
                "You were constantly tossing around, [Party[1]]." if Line == "toss":   
                        $ Line = "toss"                                 
                "You were tossing around constantly too, [Party[1]]." if Line != "toss":   
                        $ Line = "toss" 
                                    
                "You need to learn to stick to your side, [Party[1]]." if Line == "toss":  
                        $ Line = "turn"        
                "And you need to learn to stick to your side too, [Party[1]]." if Line != "toss":  
                        $ Line = "turn"
                                                                    
            if not Sleep and Line == "nice":  
                    if Party[1] == "Rogue":
                            $ R_Blush = 1
                            ch_r "Aw, that's right sweet of ya, [R_Petname]."
                            ch_r "I think I'd want to do that again."    
                            ch_r "And, uh, you too, [Party[0]]."
                    elif Party[1] == "Kitty":
                            $ K_Blush = 2
                            ch_k "Yeah, I. . [K_like]I had fun too."
                            $ K_Blush = 1
                            ch_k "I wouldn't[K_like]mind doing it again."   
                            $ K_Blush = 2
                            ch_k "You know, some other time. . . "
                            $ K_Blush = 1  
                            ch_k "And[K_like]you too, [Party[0]]."
                    elif Party[1] == "Emma":
                            call EmmaFace("smile",1)
                            ch_e "You're a hopeless romantic, [E_Petname]."
                            call EmmaFace("smile",2,Eyes="side")
                            ch_e "I suppose I can be a bit hopeless too. . ."  
                            ch_e "You know what I'm talking about, [Party[0]]."
                    elif Party[1] == "Laura":
                            call LauraFace("confused",1)
                            ch_l "Oh. . ."
                            call LauraFace("surprised",2,Brows="confused")
                            ch_l "Yeah, so did I, now that you mention it. . ."
                            call LauraFace("confused",1)
                            ch_l "Huh."  
                            ch_l "Weird, right, [Party[0]]?"
                                
            
            elif Line == "toss":   
                        call AnyFace(Party[1],B=1)
                        if ApprovalCheck(Party[1], 800, "L") or ApprovalCheck(Party[1], 1200):
                            call AnyFace(Party[1],"bemused")     
                            call AnyLine(Party[1],"Hmm?")
                        else:
                            call AnyFace(Party[1],"angry")     
                            call AnyLine(Party[1],"!!!")
                        if Sleep < 5:                       
                            if Party[1] == "Rogue":
                                    ch_r "It's not like I've had much experience sleeping next to someone. . ."      
                            elif Party[1] == "Kitty":
                                    ch_k "I don't make a habit out of it. . ."    
                            elif Party[1] == "Emma":
                                    ch_e "I haven't had a lot of practice lately."
                            elif Party[1] == "Laura":
                                    ch_l "Deal with it."                                
                            call Statup(Party[1], "Love", 60, -8)
                            call Statup(Party[1], "Obed", 50, 22)
                            call Statup(Party[1], "Inbt", 50, 22)                   
                        else:
                            if Party[1] == "Rogue":
                                    ch_r "Well you should probably be used to that by now."     
                            elif Party[1] == "Kitty":
                                    ch_k "Yeah, well. . . you should be used to that!"
                            elif Party[1] == "Emma":
                                    ch_e "I don't plan on changing any time soon."
                            elif Party[1] == "Laura":
                                    ch_l "Yeah, it'll be like that."
            
            elif Line == "turn":  
                        if Sleep < 5:
                            call Statup(Party[1], "Love", 80, -8)
                            call Statup(Party[1], "Obed", 50, 40)
                        if ApprovalCheck(Party[1], 500, "O"):
                            call Statup(Party[1], "Love", 80, -2)
                            call Statup(Party[1], "Obed", 90, 5)
                            call AnyFace(Party[1],"normal")
                            if Party[1] == "Rogue":
                                    ch_r "Yes, [R_Petname], I'll try my best."
                            elif Party[1] == "Kitty":
                                    ch_k "Fine, whatever."
                            elif Party[1] == "Emma":
                                    ch_e "I do try."
                            elif Party[1] == "Laura":
                                    ch_l "Ok."
                            if Sleep < 5:
                                    call Statup(Party[1], "Obed", 80, 8)
                        else:
                            call AnyFace(Party[1],"angry")
                            call Statup(Party[1], "Obed", 90, 5)
                            if Party[1] == "Rogue":
                                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."   
                            elif Party[1] == "Kitty":
                                    ch_k "That's not how you get me to come back." 
                            elif Party[1] == "Emma":
                                    ch_e "I'll sleep how I please."
                            elif Party[1] == "Laura":
                                    ch_l "Good luck with that."
                            if Sleep < 5:
                                    call Statup(Party[1], "Inbt", 35, 20) 
            
            call AnyFace(Party[1],B=0)            
        #end second girl's lines
        
        #fix add sex option here
        
        
        if "Rogue" in Party:
                $ R_Sleep += 1 
                $ R_Traits.remove("sleepover")
                call Rogue_Schedule(2)          
        if "Kitty" in Party:
                $ K_Sleep += 1   
                $ K_Traits.remove("sleepover")
                call Kitty_Schedule(2)
        if "Emma" in Party:
                $ E_Sleep += 1  
                $ E_Traits.remove("sleepover")
                call Emma_Schedule(2) 
        if "Laura" in Party:
                $ newgirl["Laura"].Sleep += 1   
                $ newgirl["Laura"].Traits.remove("sleepover")
                call Laura_Schedule(2)
                 
        call AnyFace(Party[0],"normal")
        call AnyOutfit(Party[0],6,Changed = 1)
        if len(Party) >= 2:
                call AnyFace(Party[1],"normal")
                call AnyOutfit(Party[1],6,Changed = 1)
                "The girls get changed for the day."
        else:                
                "[Party[0]] gets changed for the day."
        
        if "Rogue" in Party:
                $ Party.remove("Rogue")
                call Rogue_Schedule           
        if "Kitty" in Party:
                $ Party.remove("Kitty")
                call Kitty_Schedule
        if "Emma" in Party:
                $ Party.remove("Emma")
                call Emma_Schedule 
        if "Laura" in Party:
                $ Party.remove("Laura")
                call Laura_Schedule
                
        return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Sleepover_MorningWood:
        # this label is called from the Kitty_SexAct("morningwood"), 
        # which was called from Kitty_Sleepover, which was called from a Location.
        
                    
        call Shift_Focus(Party[0])
        $ P_Focus = 30
        ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 5)
        call Statup(Party[0], "Lust", 80, 5)        
        $ P_DailyActions.append("morningwood") 
        
        $ Partner = Party[1] if len(Party) >= 2 else 0  
        #display other girl here if necessary
        
        if Partner:
            if Partner == "Rogue":  
                    show Rogue:
                        pos (900,250)
                    $ R_RecentActions.append("threesome")
            elif Partner == "Kitty":     
                    show Kitty_Sprite:
                        pos (900,250)
                    $ K_RecentActions.append("threesome")
            elif Partner == "Emma":      
                    show Emma_Sprite:
                        pos (900,250)
                    $ E_RecentActions.append("threesome")
            elif Partner == "Laura":     
                    show Laura_Sprite:
                        pos (900,250)  
                    $ newgirl["Laura"].RecentActions.append("threesome") 
                
        if Party[0] == "Rogue":       
                $ R_RecentActions.append("blanket") 
                call Rogue_BJ_Launch
                $ X_Psychic = R_Pet
        elif Party[0] == "Kitty":
                $ K_RecentActions.append("blanket")           
                call Kitty_BJ_Launch
                $ X_Psychic = K_Pet
        elif Party[0] == "Emma":
                $ E_RecentActions.append("blanket")           
                call Emma_BJ_Launch
                $ X_Psychic = E_Pet
        elif Party[0] == "Laura":
                $ newgirl["Laura"].RecentActions.append("blanket")           
                call Laura_BJ_Launch   
                $ X_Psychic = newgirl["Laura"].Pet                                 
        
        $ P_RecentActions.append("cockout")
        call AnyFace(Party[0],"closed",1) 
        call AnyFace(Partner,"closed",1,Mouth="tongue") 
        
        "You feel a pleasant sensation. . ."
        if Trigger4 == "blow":
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 5)
        call Statup(Party[0], "Lust", 80, 5)
        
        "It's somewhere below your waist. . ."   
        if Trigger4 == "blow":
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
        call Statup(0, "Focus", 80, 10)
        call Statup(Party[0], "Lust", 80, 5)
        
        $ Trigger = "blow"
        "You open your eyes. . ."
        
        hide NightMask onlayer nightmask  
        hide blackscreen onlayer black
        
        $ Speed = 3
        $ Count = 3
        $ Line = 0
        $ P_RecentActions.append("cockout")
        call Seen_First_Peen(1)
                         
        while Count > 0:
                #Looping portion
                call Statup(0, "Focus", 80, 10)
                call Statup(Party[0], "Lust", 80, 5)
                menu:
                    extend ""
                    "Stay Quiet":
                        if Count >2:  
                            if Trigger4 == "blow":
                                "You just let them do their thing and pretend to still be asleep."
                            else:
                                "You just let her do her thing and pretend to still be asleep."
                        elif Count:
                            "It does feel nice. . ."
                        elif not Count:  
                            if Trigger4 == "blow":
                                "You wouldn't want to disturb them. . ."  
                            else:                            
                                "You wouldn't want to disturb her. . ." 
                        $ Line = "\"Slurp, slurp, slurp.\""
                        call AnyLine(Party[0],Line)    
                        if Trigger4 == "blow":
                            call AnyLine(Party[1],Line) 
                    "Um. . . [X_Psychic], what're you doing?":
                        $ Line = "question"
                        $ Count = 1
                    "That feels great, keep going. . .":
                        $ Line = "praise"
                        $ Count = 1
                    "Hey, quit that!":
                        $ Line = "no"
                        $ Count = 1
                $ Count -= 1
        $ X_Psychic = 0
        $ Speed = 1
        call AnyFace(Party[0],B=1)  
        if Trigger4 == "blow":
            "[Party[0]] pulls back with a pop and [Party[1]] sits back."
            $ Trigger4 = 0
        else:
            "[Party[0]] pulls back with a pop."
        if Line == "question":                    
                        call AnyFace(Party[0],"smile",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Well I ain't whistlin Dixie, [R_Petname]."    
                        elif Party[0] == "Kitty":
                                ch_k "I wasn't[K_like]being subtle about it, [K_Petname]." 
                        elif Party[0] == "Emma":
                                ch_e "Surely your education hasn't been that poor, [E_Petname]."
                        elif Party[0] == "Laura":
                                ch_l "Guess."
        elif Line == "praise":
                        call AnyFace(Party[0],"smile",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Mmm, you know it, [R_Petname]."   
                        elif Party[0] == "Kitty":
                                ch_k "Mmm, hehe."
                        elif Party[0] == "Emma":
                                ch_e "Practice, [E_Petname]."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
        elif Line == "no":
                        $ Speed = 0
                        call AnyFace(Party[0],"angry",B=1,Brows="confused")
                        if Party[0] == "Rogue":
                                 ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!" 
                        elif Party[0] == "Kitty":
                                ch_k "{i}That's{/i} the thanks I get?!"
                        elif Party[0] == "Emma":
                                ch_e "A little \"gratitude\" wouldn't be uncalled for. . ."
                        elif Party[0] == "Laura":
                                ch_l "Huh?"
        else: #if it fell through due to time
                        if Party[0] == "Rogue":
                                ch_r "Heh, I can tell you're awake, [R_Petname]. . ."
                                ch_r "You've been. . . more responsive."    
                        elif Party[0] == "Kitty":
                                ch_k "You can stop faking it, [K_Petname]. . ."
                                ch_k "This guy's telling me you're awake now."
                        elif Party[0] == "Emma":
                                ch_e "I don't know who you think you're fooling."
                                ch_e "You've been awake for a while, [E_Petname]. . ."    
                        elif Party[0] == "Laura":
                                ch_l "You can stop playing dead, [newgirl[Laura].Petname]. . ."
                                ch_l "Oldest trick in the book."   
        #end first response phase
                                
        if Partner:        
                #second girl's lines
                if Line == "question":                    
                                call AnyFace(Party[0],"smile",B=1) 
                elif Line == "praise":
                                call AnyFace(Party[0],"smile",B=1) 
                elif Line == "no":
                                call AnyFace(Party[0],"angry",B=1,Brows="confused")
                        
                if Partner == "Rogue":       
                        if "blow" in R_RecentActions:
                            ch_r "I don't know 'bout that, [R_Petname]."
                        else:
                            "Rogue rolls over in bed."
                            ch_r "Don't stop on my account, [R_Petname]."  
                elif Partner == "Kitty":
                        if "blow" in K_RecentActions:
                            ch_k "Huh. . ."
                        else:
                            "Kitty rolls over in bed."
                            ch_k "Looked like you were having some fun there . . ."
                elif Partner == "Emma":
                        if "blow" in E_RecentActions:
                            ch_e "Well. . ."
                        else:
                            "Emma rolls over in bed."
                            ch_e "Oh, don't let me stop you two."
                elif Partner == "Laura":
                        if "blow" in newgirl["Laura"].RecentActions:
                            ch_l "Hmm. . ."
                        else:
                            "Laura rolls over in bed and stares at you both."
                                
        #start second question phase
        menu:
            extend ""
            "So, um, you want to get back to it?":
                    if Line != "no":
                        #assuming you weren't rude
                        call AnyFace(Party[0],"smile",B=1)                              
                        if Party[0] == "Rogue":
                                ch_r "My pleasure."     
                        elif Party[0] == "Kitty":
                                ch_k "Hehe, mmmm. . ."
                        elif Party[0] == "Emma":
                                ch_e "If you insist. . ."
                        elif Party[0] == "Laura":
                                ch_l "That's the plan. . ."    
                    elif Line == "no" and ApprovalCheck(Party[0], 1750):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused")
                        if Party[0] == "Rogue":
                                ch_r "You're lucky I'm so into you. . ."    
                        elif Party[0] == "Kitty":
                                ch_k "Wha? Well. . . I guess. . ."
                        elif Party[0] == "Emma":
                                ch_e "Do try not to be a prat this time. . ."
                        elif Party[0] == "Laura":
                                ch_l "Fine. . ."   
                        $ Line = "maybe"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Were you more interested in something else?":
                    if Line != "no":
                        #assuming you weren't rude
                        call AnyFace(Party[0],"sexy",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Ooh, what did you have in mind?"  
                        elif Party[0] == "Kitty":
                                ch_k "Maaaybee. . . like what?"
                        elif Party[0] == "Emma":
                                ch_e "Perhaps. . . What did you have in mind?"
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "sex"
                    elif Line == "no" and ApprovalCheck(Party[0], 1650):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, you're a jerk, but you're a cute jerk."
                                ch_r "What were you thinking?"     
                        elif Party[0] == "Kitty":
                                ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                                ch_k "Like what?"
                        elif Party[0] == "Emma":
                                ch_e "Hmm, second chance [E_Petname], what were you considering?"
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "sex"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Sorry, sorry, please continue." if Line == "no":
                    if ApprovalCheck(Party[0], 1450):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"bemused",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, since you asked so nice. . ."    
                        elif Party[0] == "Kitty":
                                ch_k "I guess I can forgive you. . ."
                        elif Party[0] == "Emma":
                                ch_e "Ok, I'll give you another chance here."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"
                        $ Line = "maybe"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Sorry, but we could do something else." if Line == "no":
                    if ApprovalCheck(Party[0], 1350):
                        #if you were a dick but she's ok
                        call AnyFace(Party[0],"sexy",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Well, since you asked so nice. . ."
                                ch_r "What did you have in mind?"   
                        elif Party[0] == "Kitty":
                                ch_k "I guess, maybe. . ."
                                ch_k "Like what?"
                        elif Party[0] == "Emma":
                                ch_e "Mmm, I'll consider it. . ."
                        elif Party[0] == "Laura":
                                ch_l "Yeah, I guess?"                                    
                        $ Line = "sex"
                    else:
                        #if you were a dick and she's not ok with that
                        call AnyFace(Party[0],"angry",B=1) 
                        if Party[0] == "Rogue":
                                ch_r "Well not when you're rude to me."                
                                ch_r "You can polish yourself off."     
                        elif Party[0] == "Kitty":
                                ch_k "You can't walk that one back!"
                                ch_k "You can take care of that yourself."
                        elif Party[0] == "Emma":
                                ch_e "Not with your attitude."
                                ch_e "I think you can manage to finish this yourself."
                        elif Party[0] == "Laura":
                                ch_l "No."  
            "Not when I'm just waking up.":
                        call AnyFace(Party[0],"angry",B=1)  
                        if Party[0] == "Rogue":
                                ch_r "Fine, whatever!"
                                $R_Eyes = "side"
                                ch_r "[[mumbles] Girl tries to do a favor. . ."     
                        elif Party[0] == "Kitty":
                                ch_k "Aw. . ."
                                $K_Eyes = "side"
                                ch_k "Last time I do you a favor. . ."
                        elif Party[0] == "Emma":
                                ch_e "Hmph. . ."
                                $E_Eyes = "side"
                                ch_e "It's not as though that was for my benefit. . ."
                        elif Party[0] == "Laura":
                                ch_l "Tsk. . ."
                                $newgirl["Laura"].Eyes = "side"
                                ch_l "\"No free blowjobs,\" got it. . ."                                    
                        $ Line = "no"
        #end second question phase
                    
                       
        if Line == "no" or Line == "sex":
                call AnyFace(Partner,"sexy") 
                if Party[0] == "Rogue":      
                        $ R_RecentActions.remove("blanket") 
                        call Rogue_BJ_Reset
                elif Party[0] == "Kitty":
                        $ K_RecentActions.remove("blanket")           
                        call Kitty_BJ_Reset
                elif Party[0] == "Emma":
                        $ E_RecentActions.remove("blanket")           
                        call Emma_BJ_Reset
                elif Party[0] == "Laura":
                        $ newgirl["Laura"].RecentActions.remove("blanket")           
                        call Laura_BJ_Reset                
                if len(Party) >= 2:
                    if Party[1] == "Rogue":       
                            show Rogue:
                                ease 1 pos (700,50)
                            show Rogue:
                                pos (700,50)
                    elif Party[1] == "Kitty":     
                            show Kitty_Sprite:
                                ease 1 pos (700,50)
                            show Kitty_Sprite:
                                pos (700,50)
                    elif Party[1] == "Emma":      
                            show Emma_Sprite:
                                ease 1 pos (700,50)
                            show Emma_Sprite:
                                pos (700,50)
                    elif Party[1] == "Laura":     
                            show Laura_Sprite:
                                ease 1 pos (700,50)  
                            show Laura_Sprite:
                                pos (700,50)  
                        
                
                if Line == "no":     
                        if bg_current == "bg player":               
                            call AnyLine(Party[0],"I'm out of here.")  
                            call AnyLine(Partner,"Yeah, me too.")  
                        else:
                            call AnyLine(Party[0],"Oh, get out of here already.")  
                        
                        call AnyOutfit(Party[0],6) #sets to OutfitDay
                        call AnyOutfit(Partner,6) #sets to OutfitDay
                        $ Party = []
                        $ Partner = 0
                        $ renpy.pop_call()
                        jump Return_Player
                        
                elif Line == "sex":
                        #shift to other sex stuff with her
                        $ Situation = "shift"
        else: 
                #continue with the BJ
                $ Line = 0
                $ Speed = 1
                $ Situation = "blow"
                if Partner:
                    $ Trigger4 = "blow"
        return
    
# end Event Morning Wood /////////////////////////////////////////////////////    

label Morning_Partner: 
        #Called from sex act menu
        call AnyFace(Partner,"sexy") 
        if Partner == "Rogue":       
                show Rogue:
                    ease 1 pos (700,50)
                show Rogue:
                    pos (700,50)
        elif Partner == "Emma":      
                show Emma_Sprite:
                    ease 1 pos (700,50)
                show Emma_Sprite:
                    pos (700,50)
        elif Partner == "Kitty":     
                show Kitty_Sprite:
                    ease 1 pos (700,50)  
                show Kitty_Sprite:
                    pos (700,50) 
        elif Partner == "Laura":     
                show Laura_Sprite:
                    ease 1 pos (700,50)  
                show Laura_Sprite:
                    pos (700,50) 
        return
    
    
# start Morning Wood Check/////////////////////////////////////////////////////    

label Morningwood_Check(Girls=[0,-3],Line=0,D20=0):                
        #This element sends player to the Morningwood event or returns them
        #it is called from Sleepover_Morning
        
        $ D20 = renpy.random.randint(0,3)  
        $ Line = 0
        
        if len(Party) >= 2:
                #builds a modifier for how the girls like each other
                if GirlLikeCheck(Party[0],Party[1]) >= 900:
                        # If the first girl really likes the second
                        $ Girls[0] = 2
                elif GirlLikeCheck(Party[0],Party[1]) >= 750:
                        # If the first girl kinda likes the second
                        $ Girls[0] = 0
                elif GirlLikeCheck(Party[0],Party[1]) <= 400:
                        # If the first girl really hates the second
                        $ Girls[0] = 2
                else:
                        $ Girls[0] = 0
                    
                if GirlLikeCheck(Party[1],Party[0]) >= 900:
                        # If the second girl really likes the first
                        $ Girls[1] = 2
                elif GirlLikeCheck(Party[1],Party[0]) >= 750:
                        # If the second girl kinda likes the first
                        $ Girls[1] = 0
                elif GirlLikeCheck(Party[1],Party[0]) <= 400:
                        # If the second girl really hates the first
                        $ Girls[1] = -5
                else:
                        $ Girls[1] = -3
        else:
                $ Girls[0] -= 2
        
        if Party[0] == "Rogue":
                #checks if Rogue wants to do it
                if R_Blow >= 5 or ApprovalCheck("Rogue", 900, "I"):  
                        $ Girls[0] += 3
                elif R_Blow and ApprovalCheck("Rogue", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Rogue", 1400):
                        $ Girls[0] += 2
                elif R_Blow or ApprovalCheck("Rogue", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in R_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if R_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if R_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1                        
        elif Party[0] == "Kitty":
                #checks if Kitty wants to do it
                if K_Blow >= 5 or ApprovalCheck("Kitty", 900, "I"):  
                        $ Girls[0] += 3
                elif K_Blow and ApprovalCheck("Kitty", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Kitty", 1400):
                        $ Girls[0] += 2
                elif K_Blow or ApprovalCheck("Kitty", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in K_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if K_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if K_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1                            
        elif Party[0] == "Emma":
                #checks if Emma wants to do it
                if E_Blow >= 5 or ApprovalCheck("Emma", 900, "I"):  
                        $ Girls[0] += 3
                elif E_Blow and ApprovalCheck("Emma", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Emma", 1400):
                        $ Girls[0] += 2
                elif E_Blow or ApprovalCheck("Emma", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in E_Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if E_Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if E_SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1
        elif Party[0] == "Laura":
                #checks if Laura wants to do it
                if newgirl["Laura"].Blow >= 5 or ApprovalCheck("Laura", 900, "I"):  
                        $ Girls[0] += 3
                elif newgirl["Laura"].Blow and ApprovalCheck("Laura", 900):
                        $ Girls[0] += 2
                elif ApprovalCheck("Laura", 1400):
                        $ Girls[0] += 2
                elif newgirl["Laura"].Blow or ApprovalCheck("Laura", 900):
                        $ Girls[0] += 1
                        
                if "hungry" in newgirl["Laura"].Traits and D20 >= 2:
                        #if she likes cum and gets a 50-70 result
                        $ Girls[0] += 2
                if newgirl["Laura"].Lust >= 50:
                        #if she's horny
                        $ Girls[0] += 1
                if newgirl["Laura"].SEXP <= 15:
                        #if she's inexperienced
                        $ Girls[0] -= 1
        #end first girls
        
        if Girls[1] >= 0:
                # if the other girl quite likes her
                $ Girls[0] += 1
                
        #minimum: -1 likely: 3 maximum: 9
        if Girls[0] >= D20:
                $ Line = "yes"  
                
        #end first girl check, Girls[0] maybe "yes," maybe 0
        
        if len(Party) >= 2:
            if Party[1] == "Rogue":
                    #checks if Rogue wants to do it
                    if R_Blow >= 5 or ApprovalCheck("Rogue", 900, "I"):  
                            $ Girls[1] += 3
                    elif R_Blow and ApprovalCheck("Rogue", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Rogue", 1400):
                            $ Girls[1] += 2
                    elif R_Blow or ApprovalCheck("Rogue", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in R_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if R_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if R_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
                            
            elif Party[1] == "Kitty":
                    #checks if Kitty wants to do it
                    if K_Blow >= 5 or ApprovalCheck("Kitty", 900, "I"):  
                            $ Girls[1] += 3
                    elif K_Blow and ApprovalCheck("Kitty", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Kitty", 1400):
                            $ Girls[1] += 2
                    elif K_Blow or ApprovalCheck("Kitty", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in K_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if K_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if K_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2    
            elif Party[1] == "Emma":
                    #checks if Emma wants to do it
                    if E_Blow >= 5 or ApprovalCheck("Emma", 900, "I"):  
                            $ Girls[1] += 3
                    elif E_Blow and ApprovalCheck("Emma", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Emma", 1400):
                            $ Girls[1] += 2
                    elif E_Blow or ApprovalCheck("Emma", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in E_Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if E_Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if E_SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
            elif Party[1] == "Laura":
                    #checks if Laura wants to do it
                    if newgirl["Laura"].Blow >= 5 or ApprovalCheck("Laura", 900, "I"):  
                            $ Girls[1] += 3
                    elif newgirl["Laura"].Blow and ApprovalCheck("Laura", 900):
                            $ Girls[1] += 2
                    elif ApprovalCheck("Laura", 1400):
                            $ Girls[1] += 2
                    elif newgirl["Laura"].Blow or ApprovalCheck("Laura", 900):
                            $ Girls[1] += 1
                            
                    if "hungry" in newgirl["Laura"].Traits and D20 >= 2:
                            #if she likes cum and gets a 50-70 result
                            $ Girls[1] += 2
                    if newgirl["Laura"].Lust >= 50:
                            #if she's horny
                            $ Girls[1] += 1
                    if newgirl["Laura"].SEXP <= 15:
                            #if she's inexperienced
                            $ Girls[1] -= 2
            #end second girls
                            
            if Girls[0] >= 0:
                    # if the other girl quite likes her
                    $ Girls[1] += 1
                    
            #minimum: -6 likely: 2 maximum: 9
            if Girls[1] >= (D20 + 1):# 1-4
                    if Line == "yes": #if the first girl agreed
                            $ Line = "double"  
                    else:
                            $ Line = "other"  
            elif Girls[1] <= -1:
                    $ Line = "no"  
            #else: stays "yes"
                            
            if Line == "other" and GirlLikeCheck(Party[0],Party[1]) >= 500:
                # If Girl 1 wasn't into it, but liked girl 2 and girl 2 was, swap them                            
                $ Party.reverse() 
                $ Girls[0] = "yes"
                $ Girls[1] = 0
                        
        #End second girl check, Girls[1] maybe "double," maybe "no", maybe 0
        
        if Line:
            # if Line has changed from 0
            if Line == "no":
                        # second girl ruins it
                        "You hear a little commotion as you start to wake up."
                        if Party[1] == "Rogue":
                                ch_r "You get'cher head out of there, [Party[0]]!"   
                        elif Party[1] == "Kitty":
                                "You hear a thump and feel a small woosh as something heavy drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Serves you right, [Party[0]]."
                        elif Party[1] == "Emma":
                                ch_e "Step away from [Playername], [Party[0]]."
                        elif Party[1] == "Laura":
                                ch_l "Back it up, [Party[0]]."     
                                
                        if Party[0] == "Rogue":
                                ch_r "I didn't mean no harm, [Party[1]]."   
                        elif Party[0] == "Kitty":
                                "You hear a thump and feel a small woosh as something drops under the bed."                                   
                                call AnyLine(Party[0],"Ow!")
                                ch_k "Spoilsport."
                        elif Party[0] == "Emma":
                                ch_e "Don't be a bore, dear."
                        elif Party[0] == "Laura":
                                ch_l "Fine, whatever."
                        return
            elif Line == "double":
                        # it's a threesome
                        $ Trigger4 = "blow"
                        if Party[1] == "Rogue":     
                                $ R_RecentActions.append("blow")           
                                $ R_DailyActions.append("blow")                          
                                $ R_DailyActions.append("morningwood")  
                        elif Party[1] == "Kitty":     
                                $ K_RecentActions.append("blow")           
                                $ K_DailyActions.append("blow")                          
                                $ K_DailyActions.append("morningwood")  
                        elif Party[1] == "Emma":                            
                                $ E_RecentActions.append("blow")           
                                $ E_DailyActions.append("blow")                          
                                $ E_DailyActions.append("morningwood")   
                        elif Party[1] == "Laura":     
                                $ newgirl["Laura"].RecentActions.append("blow")           
                                $ newgirl["Laura"].DailyActions.append("blow")                          
                                $ newgirl["Laura"].DailyActions.append("morningwood")     
            # it's a solo act with girl 1
            if Party[0] == "Rogue":
                    call Rogue_SexAct("morningwood")   
            elif Party[0] == "Kitty":
                    call Kitty_SexAct("morningwood")
            elif Party[0] == "Emma":
                    call Emma_SexAct("morningwood")
            elif Party[0] == "Laura":
                    call Laura_SexAct("morningwood")
            call Sex_Over(0)
            #end "yes"
            
        else: #Girls[0] = 0
            #neither girl was interested 
            pass
            
        return


# end Morning Wood Check///////////////////////////////////////////////////// 


    
    
    
## start Poly _Start//////////////////////////////////////////////////////////
label Poly_Start(Newbie=0,Round2=0):
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version. 
        # Newbie will be the new girl
        $ Line = 0
                
        if not P_Harem:            
            return
        if len(P_Harem) >= 2:
            call Harem_Start(Newbie,Round2)
            return
            
        if "polystart" in P_DailyActions:
                return                
        $ P_DailyActions.append("polystart")
        
        $ Party = [P_Harem[0]]
        call Shift_Focus(P_Harem[0])
        call Set_The_Scene
            
        if Round2:
                "You pull [Party[0]] aside for a moment."
                ch_p "Hey, have you changed your mind about [Newbie] lately?"
        else:
                call AnyFace(Party[0],"bemused")
                "[Party[0]] pulls you aside and wants to talk about something."
                
                #Line 1
                if Party[0] == "Rogue":                 
                        ch_r "I've seen you were getting pretty cozy with [Newbie]."
                elif Party[0] == "Kitty":      
                        ch_k "You look kinda close with [Newbie] lately."
                elif Party[0] == "Emma":      
                        ch_e "I've noticed that [Newbie] and yourself have been spending time together."
                elif Party[0] == "Laura":     
                        ch_l "You've been all over [Newbie] lately."
                #end Line 1
        
        
        if GirlLikeCheck(Party[0],Newbie) >= 800:
                call AnyFace(Party[0],"sly")  
        elif GirlLikeCheck(Party[0],Newbie) >= 600:
                pass
        else:
                # neither likes her much
                call AnyFace(Party[0],"angry",Mouth="normal")  
                
        # We like her or not
        if Party[0] == "Rogue":       
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "She is pretty sexy, I guess."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "I like her just fine, I was just wondering where it was headed."               
                else:
                        # neither likes her much
                        ch_r "I'm not really a fan'a hers."                    
        elif Party[0] == "Kitty":    
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, I get that. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but I'm not sure. . ."
                else:
                        # neither likes her much
                        ch_k "I don't really like her much." 
        elif Party[0] == "Emma":     
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think she's quite the catch."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "I do like her, but have some concerns."
                else:
                        # neither likes her much
                        ch_e "I don't really approve."
        elif Party[0] == "Laura":   
                if GirlLikeCheck(Party[0],Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, I get it."
                elif GirlLikeCheck(Party[0],Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                else:
                        # neither likes her much
                        ch_l "I don't like her."
        #end line 2
        
        
        #Line 3
        if Party[0] == "Rogue":                 
                ch_r "I don't know how I feel about sharing you with some other girl."
                ch_r "So did you plan to get serious with her?"
        elif Party[0] == "Kitty":      
                ch_k "I don't know about sharing my boyfriend with somebody else."
                ch_k "So are you[K_like]trying to date her?"
        elif Party[0] == "Emma":      
                ch_e "I can be a bit. . . possessive with my partners."
                ch_e "Is this getting serious with her?"
        elif Party[0] == "Laura":     
                ch_l "I don't play well with others."
                ch_l "Are you two getting serious?"
        #end Line 3
                
        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"
            
        if Line == "y":     
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they like her a lot
                    $ Line = "yy"
                    call Statup(Party[0], "Love", 90, 5)
                    call Statup(Party[0], "Obed", 50, 5)
                    call Statup(Party[0], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ Line = "ym"
                    call Statup(Party[0], "Obed", 50, 5) 
            elif ApprovalCheck(Party[0], 1500) and GirlLikeCheck(Party[0],Newbie) >= 500:
                    # if they like her well enough
                    $ Line = "ym"
            else:
                    # neither likes her much
                    $ Line = "yn"  
                    call Statup(Party[0], "Love", 90, -10)
        #end Line = y
        if Line == "m":
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and GirlLikeCheck(Party[0],Newbie) >= 600:
                    # if they both like her well enough
                    $ Line = "mm"
            else:
                    # neither likes her much
                    $ Line = "mn" 
        #end Line = m  
        if Line == "n":
            if GirlLikeCheck(Party[0],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    call Statup(Party[0], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and GirlLikeCheck(Party[0],Newbie) >= 500:
                    # if they both like her well enough
                    $ Line = "nm"
                    call Statup(Party[0], "Love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ Line = "nn"
                    call Statup(Party[0], "Love", 90, 10)
        #end Line = n      
            
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        if Line == "yn" or Line == "mn" or Line == "nn":
                call AnyFace(Party[0],"angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                call AnyFace(Party[0],"sexy")
        else:
                call AnyFace(Party[0],"bemused")
                
        #Line 5
        if Party[0] == "Rogue":       
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess I can live with that."                        
                elif Line == "nm":
                        # if you said no but they both like her well enough                      
                        ch_r "Hmm, not that I would have minded."
                                
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think I'm really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."
                        
        elif Party[0] == "Kitty":        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."     
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with me!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"                        
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, I can[K_like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, I would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with me."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == "Emma":          
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose I can make do then."            
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_e "You could do a lot worse."
                        
                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."
                        
        elif Party[0] == "Laura":        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, I can work with that."            
                elif Line == "nm":
                        # if you said no but they both like her well enough   
                        ch_l "Ok. I'm cool with it if you do though." 
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."
        #end Line 5
        
        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                    #They were generally favorable, so you agreed
                    $ Line = "yy"
                    call AnyFace(Party[0],"smile")
                    call Statup(Party[0], "Love", 90, 10)
                    call Statup(Party[0], "Obed", 50, 10)
                    if Party[0] == "Rogue":       
                                    ch_r "Great, sounds fun."                 
                    elif Party[0] == "Kitty":        
                                    ch_k "Cool, sounds fun."                                        
                    elif Party[0] == "Emma":          
                                    ch_e "Lovely. . ."                                   
                    elif Party[0] == "Laura":        
                                    ch_l "Nice."   
                
                "Well then, I guess I'll stop." if Line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it. 
                    $ Line = "nn"
                    call AnyFace(Party[0],"smile")
                    call Statup(Party[0], "Love", 90, 10) 
                    if Party[0] == "Rogue":       
                                    ch_r "Good to hear."                        
                    elif Party[0] == "Kitty":        
                                    ch_k "Good, that wouldn't have been cool."                        
                    elif Party[0] == "Emma":       
                                    ch_e "Probably for the best."                        
                    elif Party[0] == "Laura":        
                                    ch_l "Good."
                
                "I'm asking her in anyway." if Line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass
                    
                "Well, I'm going to pass anyway." if Line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ Line = "nn"
                    call AnyFace(Party[0],"sad")
                    call Statup(Party[0], "Obed", 70, 5) 
                    if Party[0] == "Rogue":       
                                    ch_r "Oh, ok."                        
                    elif Party[0] == "Kitty":        
                                    ch_k "That's fine."                        
                    elif Party[0] == "Emma": 
                                    ch_e "If you insist."                        
                    elif Party[0] == "Laura":        
                                    ch_l "Ok."
                                                
        #end player response to their feedback
            
        if Line == "mn" or Line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway 
                                 
                if ApprovalCheck(Party[0], 1600) and GirlLikeCheck(Party[0],Newbie) >= 500:
                            call AnyFace(Party[0],"sadside")
                            call Statup(Party[0], "Love", 90, -5)
                            call Statup(Party[0], "Obed", 50, 15)
                            if Party[0] == "Rogue":                 
                                    ch_r "Fine, she's in."
                            elif Party[0] == "Kitty":      
                                    ch_k "Geeze, ok."
                            elif Party[0] == "Emma":      
                                    ch_e "I suppose we'll make room."
                            elif Party[0] == "Laura":     
                                    ch_l "Whatever."
                            $ Line = "yy"
                else:
                            call AnyFace(Party[0],"angry",Eyes="side")
                            call Statup(Party[0], "Love", 90, -25)
                            call Statup(Party[0], "Inbt", 90, 10) 
                            if Party[0] == "Rogue":                 
                                    ch_r "I just don't like you that much, [R_Petname]."
                                    ch_r "I'm out."                                    
                                    if "dating" in R_Traits:
                                        $ R_Traits.remove("dating")
                                    $ R_Traits.append("ex")
                                    $ R_Break[0] = 5 + R_Break[1] + R_Cheated
                            elif Party[0] == "Kitty":      
                                    ch_k "You aren't that cute, [K_Petname]."
                                    ch_k "I'm done."
                                    if "dating" in K_Traits:
                                        $ K_Traits.remove("dating")
                                    $ K_Traits.append("ex")
                                    $ K_Break[0] = 5 + K_Break[1] + K_Cheated
                            elif Party[0] == "Emma":      
                                    ch_e "Don't overestimate yourself, [E_Petname]."
                                    ch_e "We're done."
                                    if "dating" in E_Traits:
                                        $ E_Traits.remove("dating")
                                    $ E_Traits.append("ex")
                                    $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                            elif Party[0] == "Laura":     
                                    ch_l "Too far, [newgirl[Laura].Petname]."
                                    ch_l "I'm out of here."
                                    if "dating" in newgirl["Laura"].Traits:
                                        $ newgirl["Laura"].Traits.remove("dating")
                                    $ newgirl["Laura"].Traits.append("ex")
                                    $ newgirl["Laura"].Break[0] = 5 + newgirl["Laura"].Break[1] + newgirl["Laura"].Cheated
                                    
                            $ P_Harem.remove(Party[0])
                            call Remove_Girl(Party[0])
        #end "she said no but you insisted"        
                   
        $ Party = []
        if Line == "yy":
                $Count = Newbie + "No"
                if Count in P_Traits:                   
                        $ P_Traits.remove(Count)
                $Count = Newbie + "Yes"
                $ P_Traits.append(Count)
                "You should give [Newbie] a call."   
        else:
                $Count = Newbie + "No"
                $ P_Traits.append(Count)
                    
                         
        return
        
## end Poly _Start//////////////////////////////////////////////////////////



## start Harem _Start//////////////////////////////////////////////////////////
label Harem_Start(Newbie=0,Round2=0):    
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back. 
        # Newbie will be the new girl
        
        if "harem" in P_DailyActions:
                return                
        $ P_DailyActions.append("harem")
        $ Line = 0
        
        if len(P_Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                return
                
        $ Party = [P_Harem[0],P_Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_Check        
        $ Party = [P_Harem[0],P_Harem[1]]
        call Shift_Focus(P_Harem[0])
        call Set_The_Scene            
        
        call AnyFace(Party[0],"bemused")
        call AnyFace(Party[1],"bemused")
        if Round2:
                "You call [Party[0] and [Party[1]] over."
                ch_p "I was wondering if you'd changed your mind about [Newbie]."
        else:
                "[Party[0]] pulls you aside and wants to talk about something."
                #Line 1
                
                if Party[0] == "Rogue":       
                        ch_r "Hey, so me and [Party[1]] have been talk'in."                 
                elif Party[0] == "Kitty":    
                        ch_k "So[K_like]me and [Party[1]] had a little chat."   
                elif Party[0] == "Emma":     
                        ch_e "[Party[1]] and I have been discussing a few things."   
                elif Party[0] == "Laura":   
                        ch_l "I had a little chat with [Party[1]]. . ." 
                #end Line 1
                
                #Line 2
                if Party[1] == "Rogue":                 
                        ch_r "We hear that you were getting pretty cozy with [Newbie]."
                elif Party[1] == "Kitty":      
                        ch_k "We hear that you're kind close with [Newbie] lately."
                elif Party[1] == "Emma":      
                        ch_e "We've hear that [Newbie] and yourself have been spending time together."
                elif Party[1] == "Laura":     
                        ch_l "You've been all over [Newbie] lately."
                #end Line 2
                
        # We like her or not Line 3
        
        if GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                pass
        elif GirlLikeCheck(Party[0],Newbie) >= 700:
                # only first girl likes her
                call AnyFace(Party[1],"angry",Mouth="normal")
        elif GirlLikeCheck(Party[1],Newbie) >= 700:
                # only second girl likes her
                call AnyFace(Party[0],"angry",Mouth="normal")
        else:
                # neither likes her much
                call AnyFace(Party[0],"angry",Mouth="normal") 
                call AnyFace(Party[1],"angry",Mouth="normal")    
                
        if Party[0] == "Rogue":       
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Now we like her just fine, and we can't say we don't like the idea much."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Now we like her just fine, but we don't know about share'in."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Now I like her just fine, but [Party[1]] ain't so sure."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Now [Party[1]] seems to like her, but I'm not so sure."
                else:
                        # neither likes her much
                        ch_r "Neither'a us is really cool with that."                    
        elif Party[0] == "Kitty":    
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, we get that. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but we're not sure. . ."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_k "I like her, but I don't know about [Party[1]]."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1]] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_k "We don't really like her much." 
        elif Party[0] == "Emma":     
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think we agree that she's a nice catch."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "We do like her, but we have some concerns."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1]] doesn't really approve."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1]] seems to think she's acceptable."
                else:
                        # neither likes her much
                        ch_e "We don't really approve."
        elif Party[0] == "Laura":   
                if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, we get it."
                elif GirlLikeCheck(Party[0],Newbie) >= 600 and GirlLikeCheck(Party[1],Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                elif GirlLikeCheck(Party[0],Newbie) >= 700:
                        # only first girl likes her
                        ch_l "She's fine, but [Party[1]] doesn't like her."
                elif GirlLikeCheck(Party[1],Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1]] likes her. I don't."
                else:
                        # neither likes her much
                        ch_l "We don't like her."
        #end line 3
        
        #Line 4
        if Party[1] == "Rogue":                 
                ch_r "So did you plan to get serious with her?"
        elif Party[1] == "Kitty":      
                ch_k "So are you[K_like]trying to date her?"
        elif Party[1] == "Emma":      
                ch_e "Is this getting serious with her?"
        elif Party[1] == "Laura":     
                ch_l "Are you two getting serious?"
        #end Line 4
        
        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"
            
        if Line == "y":     
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "yy"                       
                    call Statup(Party[0], "Love", 90, 5)
                    call Statup(Party[0], "Obed", 50, 5)
                    call Statup(Party[0], "Inbt", 90, 10) 
                    call Statup(Party[1], "Love", 90, 5)
                    call Statup(Party[1], "Obed", 50, 5)
                    call Statup(Party[1], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "ym"
                    call Statup(Party[0], "Obed", 50, 10)
                    call Statup(Party[1], "Obed", 50, 10)
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if GirlLikeCheck(Party[0],Newbie) >= 500 and GirlLikeCheck(Party[1],Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "ym"
                            call Statup(Party[0], "Obed", 80, 15) 
                            call Statup(Party[1], "Obed", 80, 15) 
                    else:
                            # if they don't like her well enough
                            $ Line = "yn"
                            call Statup(Party[0], "Love", 90, -5)
                            call Statup(Party[0], "Obed", 50, -5)
                            call Statup(Party[1], "Love", 90, -5)
                            call Statup(Party[1], "Obed", 50, -5)
            else:
                            # neither likes her much
                            $ Line = "yn"  
                            call Statup(Party[0], "Love", 90, -10)
                            call Statup(Party[0], "Obed", 50, -5)
                            call Statup(Party[1], "Love", 90, -10)
                            call Statup(Party[1], "Obed", 50, -5)
        #end Line = y
        if Line == "m":
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    call Statup(Party[0], "Inbt", 90, 5) 
                    call Statup(Party[1], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if GirlLikeCheck(Party[0],Newbie) >= 600 or GirlLikeCheck(Party[1],Newbie) >= 600:
                            # if they both like her well enough
                            $ Line = "mm"
                    else:
                            # if they don't like her well enough
                            $ Line = "mn"
            else:
                            # neither likes her much
                            $ Line = "mn" 
        #end Line = m  
        if Line == "n":
            if GirlLikeCheck(Party[0],Newbie) >= 800 and GirlLikeCheck(Party[1],Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    call Statup(Party[0], "Inbt", 90, 10) 
                    call Statup(Party[1], "Inbt", 90, 10) 
            elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    call Statup(Party[0], "Inbt", 90, 5) 
            elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
                    if GirlLikeCheck(Party[0],Newbie) >= 500 and GirlLikeCheck(Party[1],Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "nm"
                    else:
                            # if they don't like her well enough
                            $ Line = "nn"
                            call Statup(Party[0], "Love", 90, 5)
                            call Statup(Party[0], "Inbt", 90, 5) 
                            call Statup(Party[1], "Love", 90, 5)
                            call Statup(Party[1], "Inbt", 90, 5) 
            else:
                            # neither likes her much
                            $ Line = "nn" 
                            call Statup(Party[0], "Love", 90, 5)
                            call Statup(Party[0], "Inbt", 90, 5) 
                            call Statup(Party[1], "Love", 90, 5)
                            call Statup(Party[1], "Inbt", 90, 5) 
        #end Line = n      
                                                  
            
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                
        if Line == "yn" or Line == "mn" or Line == "nn":
                call AnyFace(Party[0],"angry")
                call AnyFace(Party[1],"angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                call AnyFace(Party[0],"sexy")
                call AnyFace(Party[1],"sexy")
        else:
                call AnyFace(Party[0],"bemused")
                call AnyFace(Party[1],"bemused")   
                
        #Line 5
        if Party[0] == "Rogue":       
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess we can live with that."                        
                elif Line == "nm":
                        # if you said no but they both like her well enough                      
                        ch_r "Hmm, not that we would have minded."
                                
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think we're really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."
                        
        elif Party[0] == "Kitty":        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."     
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with us!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"                        
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, we can[K_like]live with that."              
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_k "Ok, we would have been ok with it though."
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with us."                          
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."
                        
        elif Party[0] == "Emma":          
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose we can make do then."            
                elif Line == "nm":
                        # if you said no but they both like her well enough    
                        ch_e "You could do a lot worse."
                        
                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."
                        
        elif Party[0] == "Laura":        
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."
                        
                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, we can work with that."            
                elif Line == "nm":
                        # if you said no but they both like her well enough   
                        ch_l "Ok. We're cool with it if you do though." 
                        
                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."
        #end Line 5
        
        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                        #They were generally favorable, so you agreed
                        $ Line = "yy"
                        call AnyFace(Party[0],"smile")
                        call AnyFace(Party[1],"smile")   
                        call Statup(Party[0], "Obed", 80, 5)
                        call Statup(Party[0], "Inbt", 90, 10) 
                        call Statup(Party[1], "Obed", 80, 5)
                        call Statup(Party[1], "Inbt", 90, 10) 
                        if Party[0] == "Rogue":       
                                    ch_r "Great, sounds fun."                 
                        elif Party[0] == "Kitty":        
                                    ch_k "Cool, sounds fun."                                        
                        elif Party[0] == "Emma":          
                                    ch_e "Lovely. . ."                                   
                        elif Party[0] == "Laura":        
                                    ch_l "Nice."                     
                "Well then, I guess I'll stop." if Line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it. 
                        $ Line = "nn"
                        call AnyFace(Party[0],"normal")
                        call AnyFace(Party[1],"normal")  
                        call Statup(Party[0], "Love", 90, 5)
                        call Statup(Party[0], "Inbt", 90, 5)  
                        call Statup(Party[1], "Love", 90, 5)
                        call Statup(Party[1], "Inbt", 90, 5)                                
                        if Party[0] == "Rogue":       
                                        ch_r "Good to hear."                        
                        elif Party[0] == "Kitty":        
                                        ch_k "Good, that wouldn't have been cool."                        
                        elif Party[0] == "Emma":       
                                        ch_e "Probably for the best."                        
                        elif Party[0] == "Laura":        
                                        ch_l "Good."                    
                "I'm asking her in anyway." if Line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass
                    
                "Well, I'm going to pass anyway." if Line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ Line = "nn"
                        call AnyFace(Party[0],"sad")
                        call AnyFace(Party[1],"sad")  
                        call Statup(Party[0], "Obed", 50, 5) 
                        call Statup(Party[1], "Obed", 50, 5) 
                        if Party[0] == "Rogue":       
                                        ch_r "Oh, ok."                        
                        elif Party[0] == "Kitty":        
                                        ch_k "That's fine."                        
                        elif Party[0] == "Emma": 
                                        ch_e "If you insist."                        
                        elif Party[0] == "Laura":        
                                        ch_l "Ok."
            #end player response to their feedback
            
            if Line == "yy" or Line == "nn":
                                pass
            elif len(P_Harem) >= 3:
                                call AnyFace(Party[0],"smile",Eyes="side")
                                call AnyFace(Party[1],"smile",Eyes="side") 
                                call Statup(Party[0], "Obed", 90, 5)
                                call Statup(Party[0], "Inbt", 90, 5) 
                                if Party[0] == "Rogue":                 
                                        ch_r "Oh, what's one more."
                                elif Party[0] == "Kitty":      
                                        ch_k "We're building a real \"pride\" here."
                                elif Party[0] == "Emma":      
                                        ch_e "I suppose one more can't hurt."
                                elif Party[0] == "Laura":     
                                        ch_l "Whatever."
                                $ Line = "yy"
            elif Line == "mn" or Line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway 
                    $Count = 0
                    while Count < 2:
                        if ApprovalCheck(Party[Count], 1600) and GirlLikeCheck(Party[Count],Newbie) >= 500:
                                # She likes you enough to roll over
                                call AnyFace(Party[Count],"sadside")
                                call Statup(Party[Count], "Love", 90, -5)
                                call Statup(Party[Count], "Obed", 90, 10)
                                if Party[Count] == "Rogue":                 
                                        ch_r "Fine, she's in."
                                elif Party[Count] == "Kitty":      
                                        ch_k "Geeze, ok."
                                elif Party[Count] == "Emma":      
                                        ch_e "I suppose we'll make room."
                                elif Party[Count] == "Laura":     
                                        ch_l "Whatever."
                                $ Line = "yy"
                        else:
                                # She doewsn't like you enough to roll over
                                call AnyFace(Party[Count],"angry",Eyes="side")
                                call Statup(Party[Count], "Love", 90, -25)
                                call Statup(Party[Count], "Inbt", 90, 10) 
                                if Party[Count] == "Rogue":                 
                                        ch_r "I just don't like you that much, [R_Petname]."
                                        ch_r "I'm out."
                                        if "dating" in R_Traits:
                                            $ R_Traits.remove("dating")
                                        $ R_Traits.append("ex")
                                        $ R_Break[0] = 5 + R_Break[1] + R_Cheated
                                elif Party[Count] == "Kitty":      
                                        ch_k "You aren't that cute, [K_Petname]."
                                        ch_k "I'm done."
                                        if "dating" in K_Traits:
                                            $ K_Traits.remove("dating")
                                        $ K_Traits.append("ex")
                                        $ K_Break[0] = 5 + K_Break[1] + K_Cheated
                                elif Party[Count] == "Emma":      
                                        ch_e "Don't overestimate yourself, [E_Petname]."
                                        ch_e "We're done."
                                        if "dating" in E_Traits:
                                            $ E_Traits.remove("dating")
                                        $ E_Traits.append("ex")
                                        $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                                elif Party[Count] == "Laura":     
                                        ch_l "Too far, [newgirl[Laura].Petname]."
                                        ch_l "I'm out of here."
                                        if "dating" in newgirl["Laura"].Traits:
                                            $ newgirl["Laura"].Traits.remove("dating")
                                        $ newgirl["Laura"].Traits.append("ex")
                                        $ newgirl["Laura"].Break[0] = 5 + newgirl["Laura"].Break[1] + newgirl["Laura"].Cheated
                                        
                                $ P_Harem.remove(Party[Count])
                                call Remove_Girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"
        
        if Line == "yy":
                $Count = Newbie + "No"
                if Count in P_Traits:                   
                        $ P_Traits.remove(Count)
                $Count = Newbie + "Yes"
                $ P_Traits.append(Count)
                "You should give [Newbie] a call."   
        else:
                $Count = Newbie + "No"
                $ P_Traits.append(Count)
                
        $ Party = []
        $Count = 0
                         
        return
        
        
        
label Harem_Initiation:  
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other. 
    if "Rogue" in P_Harem:
            if "Kitty" in P_Harem:
                if "poly Kitty" not in R_Traits:
                    $ R_Traits.append("poly Kitty")
            if "Emma" in P_Harem:
                if "poly Emma" not in R_Traits:
                    $ R_Traits.append("poly Emma")
            if "Laura" in P_Harem:
                if "poly Laura" not in R_Traits:
                    $ R_Traits.append("poly Laura")    
    if "Kitty" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in K_Traits:
                    $ K_Traits.append("poly Rogue")
            if "Emma" in P_Harem:
                if "poly Emma" not in K_Traits:
                    $ K_Traits.append("poly Emma")
            if "Laura" in P_Harem:
                if "poly Laura" not in K_Traits:
                    $ K_Traits.append("poly Laura") 
    if "Emma" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in E_Traits:
                    $ E_Traits.append("poly Rogue")
            if "Kitty" in P_Harem:
                if "poly Kitty" not in E_Traits:
                    $ E_Traits.append("poly Kitty")
            if "Laura" in P_Harem:
                if "poly Laura" not in E_Traits:
                    $ E_Traits.append("poly Laura") 
    if "Laura" in P_Harem:
            if "Rogue" in P_Harem:
                if "poly Rogue" not in newgirl["Laura"].Traits:
                    $ newgirl["Laura"].Traits.append("poly Rogue")
            if "Kitty" in P_Harem:
                if "poly Kitty" not in newgirl["Laura"].Traits:
                    $ newgirl["Laura"].Traits.append("poly Kitty")
            if "Emma" in P_Harem:
                if "poly Emma" not in newgirl["Laura"].Traits:
                    $ newgirl["Laura"].Traits.append("poly Emma")
    return
## end Harem _Start//////////////////////////////////////////////////////////


#start study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Study_Session:                       
            #study events, girl is the lead girl in the scene
            $ Party = []
            if R_Loc == bg_current:
                    $ Party.append("Rogue")
            if K_Loc == bg_current:
                    $ Party.append("Kitty")
            if E_Loc == bg_current:
                    $ Party.append("Emma")
            if newgirl["Laura"].Loc == bg_current:
                    $ Party.append("Laura")
            if not Party:
                "There's nobody here to study with."
                return
                
            $ renpy.random.shuffle(Party)
            
            if Current_Time == "Night":                        
                if "Emma" in Party:
                        ch_e "It's a little late for a study session, maybe tomorrow."
                elif Party[0] == "Rogue":
                        ch_r "It's a little late for studying, maybe tomorrow."
                elif Party[0] == "Kitty":
                        ch_k "It's kinda late for studying. . . Tomorrow?"
                elif Party[0] == "Laura":
                        ch_l "It's late. Maybe tomorrow."
                $ Party = []
                return
            elif Round <= 30:         
                if "Emma" in Party:
                        ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
                elif Party[0] == "Rogue":
                        ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
                elif Party[0] == "Kitty":
                        ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
                elif Party[0] == "Laura":
                        ch_l "I was about to take a break, maybe wait a bit."                        
                $ Party = []
                return
                
            elif "Emma" in Party and len(Party) >= 2: 
                ch_e "I suppose you could both use some work."
            else:
                if "Emma" in Party:
                        ch_e "Very well."
                elif Party[0] == "Rogue":
                        ch_r "Sure."
                elif Party[0] == "Kitty":
                        ch_k "Sure."
                elif Party[0] == "Laura":
                        ch_l "Fine." 
                        
            
            $ P_RecentActions.append("study")
            $ P_XP += 5
            $ Trigger = 0
            $ Line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.", 
                    "You study up for the mutant biology test.", 
                    "You study for the math quiz.",
                    "You get bored and discuss student gossip instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test.",
                    "You study for the game design course."]) 
            "[Line]"       
            $ Line = 0
            
            call Statup(Party[0], "Love", 80, 2)
            if len(Party) >= 2:
                call Statup(Party[1], "Love", 80, 2)
                call GirlLikesGirl(Party[0],Party[1],70,5,1)
                call GirlLikesGirl(Party[1],Party[0],70,5,1)
                #raises both girl's likes of each other by 5 if they are under 70 
            
            $ D20 = renpy.random.randint(1, 20)   
            
            #There might be sexy time
            if len(Party) >= 2 and "Emma" in Party and "three" not in E_History:
                $ Line = "no"
                                                             
            if Line != "no" and D20 >= 10: 
                call Frisky_Study             
            else:
                # if there is no frisky stuff
                if "Emma" in Party:
                        ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
                elif Party[0] == "Rogue":
                        ch_r "It's getting a bit late, we should wrap this up. . ."
                elif Party[0] == "Kitty":
                        ch_k "It's kinda late, we should probably stop. . ."
                elif Party[0] == "Laura":
                        ch_l "I'm bored now."            
                $ P_XP += 5  
            $ Line = 0
            $ Party = []
            call Wait 
            call Girls_Location
            return
#End Study session  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


#Start Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Frisky_Study(Prime_Bonus=0,Second=0,Line=0,Second_Bonus=0):
            # Second is a potential second girl, (make sure to set if no second girl)
            # Prime_Bonus,Second_Bonus=0 is needed by the Datebreak code but does nothing   
            # Prime_Bonus is reappropriated to denote a second pass through
            
            call Shift_Focus(Party[0])
            
            if len(Party) >= 2:
                $ Second = Party[1]                  
            
            if Party[0] == "Rogue":
                        if D20 > 17 and ApprovalCheck("Rogue", 1000) and R_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Rogue", 1000) and R_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Rogue", 1300) or (R_Mast and ApprovalCheck("Rogue", 1000))) and R_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Rogue", 1200) and R_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Rogue", 700) and R_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Rogue", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Kitty":
                        if D20 > 17 and ApprovalCheck("Kitty", 1000) and K_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Kitty", 1000) and K_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Kitty", 1300) or (K_Mast and ApprovalCheck("Kitty", 1000))) and K_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Kitty", 1200) and K_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Kitty", 700) and K_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Kitty", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Emma":
                        if Second and ("three" not in E_History or "taboo" not in E_History):
                                #if there's a second girl and Emma doesn't do threesomes yet
                                "Emma starts to lean close to you, but then notices [Second]."                                
                                call EmmaFace("sly",1,Eyes="side")
                                "She stops immediately and looks a bit embarrassed."
                        elif D20 > 17 and ApprovalCheck("Emma", 1000) and E_Blow > 5:
                                $ Line = "blow"
                        elif D20 > 14 and ApprovalCheck("Emma", 1000) and E_Hand >= 5:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Emma", 1300) or (E_Mast and ApprovalCheck("Emma", 1000))) and E_Lust >= 70:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Emma", 1200) and E_Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Emma", 700) and E_Kissed > 1:
                                $ Line = "kissing"
                        elif ApprovalCheck("Emma", 500):        
                                $ Line = "snuggle" 
            elif Party[0] == "Laura":
                        if D20 > 16 and ApprovalCheck("Laura", 1000) and newgirl["Laura"].Blow > 1:
                                $ Line = "blow"
                        elif D20 > 13 and ApprovalCheck("Laura", 1000) and newgirl["Laura"].Hand >= 1:
                                $ Line = "hand"
                        elif D20 > 10 and (ApprovalCheck("Laura", 1300) or (newgirl["Laura"].Mast and ApprovalCheck("Laura", 1000))) and newgirl["Laura"].Lust >= 50:
                                $ Line = "masturbate" 
                        elif D20 > 10 and ApprovalCheck("Laura", 1200) and newgirl["Laura"].Lust >= 30:   
                                $ Line = "strip"
                        elif ApprovalCheck("Laura", 500): 
                                if ApprovalCheck("Laura", 700,"L"):
                                        $ Line = "snuggle" 
                                else:
                                        "Laura briefly rests against your shoulder, but then shakes herself and pulls back."
                                        $ Line = 0 
                        elif ApprovalCheck("Laura", 700) and newgirl["Laura"].Kissed > 1:
                                $ Line = "kissing"
            # End first phase
                                                
            if not Line and len(Party) >= 2 and not Prime_Bonus:
                        # this sends it back to the start if there is a second girl
                        # it swaps their order to give the second girl a chance
                        $ Party.reverse()
                        call Frisky_Study(1)               
                        return
            elif not Line or Line == "strip":    
                        pass
            elif Line == "blow":
                        call AnyFace(Party[0],"sly")
                        if Party[0] == "Kitty":
                                "Kitty reaches her hand through your textbook and you can feel it in your lap."
                                "She unzips you pants and pulls your dick out, stroking it slowly."
                                "She then dives her head under the book, and starts to lick it."   
                        else:
                                "[Party[0]] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and pops it into her mouth."    
            elif Line == "hand":
                        call AnyFace(Party[0],"sly")
                        if Party[0] == "Kitty":
                                "Kitty reaches her hand through your textbook and you can feel it in your lap."
                                "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
                                "She unzips you pants and pulls your dick out, stroking it slowly."  
                        else:
                                "[Party[0]] get predatory grin, and begins to unzip your pants."
                                "She pulls your dick out and begins to slowly stroke it."    
            elif Line == "masturbate":   
                        call AnyFace(Party[0],"sly", Eyes="side")
                        "[Party[0]] leans back a bit and starts to rub herself." 
                        $ Trigger = "masturbation"  
            elif Line == "kissing":
                        "[Party[0]] leans close to you, and leans in for a kiss."  
            elif Line == "snuggle":
                        "[Party[0]] leans close to you and you spend the rest of the study session nuzzled close."                        
                                                  
            
            if Line == "strip":
                    if "Emma" in Party and ApprovalCheck("Emma", 1200) and E_Lust >= 30:   
                            # Emma always takes priority
                            call Emma_Strip_Study_Intro              
                    elif Party[0] == "Rogue":
                            call Rogue_Strip_Study   
                    elif Party[0] == "Kitty":
                            call Kitty_Strip_Study   
                    elif Party[0] == "Laura":
                            call Laura_Strip_Study             
            elif Line and len(Party) < 2:
                    #if sex stuff is happening but only one girl
                    if Party[0] == "Rogue":
                            call Rogue_SexAct(Line) 
                    elif Party[0] == "Kitty":
                            call Kitty_SexAct(Line) 
                    elif Party[0] == "Emma":
                            call Emma_SexAct(Line) 
                    elif Party[0] == "Laura":
                            call Laura_SexAct(Line) 
            elif Line:
                    #if something sexual is happening, checks if other girl is cool
                    
                    if Line == "snuggle":
                                call Date_Sex_Break(Party[0],Second,2)
                                if _return == 3:
                                        "[Second] glowers at you a bit."  
                                        call GirlLikesGirl(Party[0],Second,70,5,1)
                                        call GirlLikesGirl(Second,Party[0],70,5,1)
                    else:
                                call Date_Sex_Break(Party[0],Second)
                                
                    if _return == 4:
                            if Line == "blow":
                                    "[Party[0]] lets your dick fall out of her mouth."
                                    "You zip your pants back up." 
                            elif Line == "hand":
                                    "[Party[0]] lets your dick drop into your lap"
                                    "You zip your pants back up." 
                            else:                                
                                    "[Party[0]] stops what she's doing."
                                    
                            call AnyFace(Party[0],"sad")
                            if Party[0] == "Rogue":
                                    ch_r "Buzzkill."
                            elif Party[0] == "Kitty":
                                    ch_k "Booo."
                            elif Party[0] == "Emma":
                                    ch_e "Oh, very well." 
                            elif Party[0] == "Laura":
                                    ch_l "Be that way."                                           
                    elif Line != "snuggle":
                        #Plays if you didn't refuse to stop
                        #either the other girl left, or it just continues with both
                        if Party[0] == "Rogue":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_r "Mind if I continue?"
                                        "Go ahead.":
                                                ch_r "Nice."
                                        "We should stop.":
                                                ch_r "Hmph."
                                                return
                                call Rogue_SexAct(Line) 
                        elif Party[0] == "Kitty":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_k "I can keep going?"
                                        "Go ahead.":
                                                ch_k "Cool."
                                        "We should stop.":
                                                ch_k "Lame."
                                                return
                                call Kitty_SexAct(Line) 
                        elif Party[0] == "Emma":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_e "You don't mind if I continue?"
                                        "Go ahead.":
                                                ch_e "Lovely."
                                        "We should stop.":
                                                ch_e "Spoil sport."
                                                return
                                call Emma_SexAct(Line) 
                        elif Party[0] == "Laura":
                                if _return == 3:
                                    #if the other girl took off. . .
                                    menu:
                                        ch_l "Keep going?"
                                        "Go ahead.":
                                                ch_l "Un."
                                        "We should stop.":
                                                ch_l "Grr."
                                                return
                                call Laura_SexAct(Line)
                    if len(Party) >= 2:                        
                        call GirlLikesGirl(Party[0],Party[1],90,10,1)
                        call GirlLikesGirl(Party[1],Party[0],90,10,1)
                        #if still two girls, raise both likes by 10
            else:
                        #if nothing sexy happened. . .
                        return
                
            if "Rogue" in Party and "frisky" not in R_History:
                    $ R_History.append("frisky")
            if "Kitty" in Party and "frisky" not in K_History:
                    $ K_History.append("frisky")
            if "Emma" in Party and "frisky" not in E_History:
                    $ E_History.append("frisky")
            if "Laura" in Party and "frisky" not in newgirl["Laura"].History:
                    $ newgirl["Laura"].History.append("frisky")
                    
            "Well that was certainly a productive use of your study time. . ."    
            return
            
#end Frisky study session / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#start Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

label Group_Strip(Girl=0,Tempmod = Tempmod,Tempmod0=0,Tempmod1=0): 
    #Note, this event would break during a date, since it manipulates Adjacent. Perhaps use unique list?
    $ Adjacent = []
    if R_Loc == bg_current:
            $ Adjacent.append("Rogue")
    if K_Loc == bg_current:
            $ Adjacent.append("Kitty")
    if E_Loc == bg_current:
            $ Adjacent.append("Emma")
    if newgirl["Laura"].Loc == bg_current:
            $ Adjacent.append("Laura")
    if not Adjacent:
            "Nobody's here."
            "You dance alone."
            return    
              
    while len(Adjacent) > 2:  
            #culls out extra members
            call Remove_Girl(Adjacent[2])
#            $ Adjacent.remove(Adjacent[2])
                
    if len(Adjacent) == 2:                    
        $ renpy.random.shuffle(Adjacent)
        if Girl and Adjacent[0] != Girl:
                $ Party.reverse()  
        elif ApprovalCheck(Adjacent[0],Check=1) <= ApprovalCheck(Adjacent[1],Check=1):
                # If second one likes you more, pick her
                $ Adjacent.reverse()   
    
    call Shift_Focus(Adjacent[0])
    
    $ Round -= 5 if Round > 5 else (Round-1)
    call Set_The_Scene(1,0,0,0)
        
    call AnyFace(Adjacent[0],"sexy",1)  
    if len(Adjacent) >= 2:
            call AnyFace(Adjacent[1],"sexy",1)  
        
    if "Rogue" in Adjacent: 
        if not ApprovalCheck("Rogue", 600, TabM = 1):
                if not ApprovalCheck("Rogue", 400):
                    ch_r "I'm just some sort'a gogo dancer now?"
                elif Taboo:
                    ch_r "I don't think this is the best place for dance'n."            
                else:
                    ch_r "I dont feel it right now."                  
                $ Adjacent.remove("Rogue")
    if "Kitty" in Adjacent:    
        if not ApprovalCheck("Kitty", 600, TabM = 1):
                if not ApprovalCheck("Kitty", 400):
                    ch_k "Like I would just dance for you?"
                elif Taboo:
                    ch_k "I don't know, this really isn't a good place for it?"            
                else:
                    ch_k "I don't know, I don't really feel like dancing right now."
                $ Adjacent.remove("Kitty")
    if "Emma" in Adjacent: 
        if not ApprovalCheck("Emma", 650, TabM = 2) or (Taboo and "taboo" not in E_History):
                #she won't dance if she's in public and not cool with that
                if not ApprovalCheck("Emma", 400):
                    ch_e "Oh, you think I'll dance to your tune?"
                elif Taboo:
                    ch_e "You must be joking. Here?"            
                else:
                    ch_e "I don't really feel like dancing at the moment."          
                $ Adjacent.remove("Emma")
    if "Laura" in Adjacent: 
        if not ApprovalCheck("Laura", 600, TabM = 0):
                # Laura does not care about being in public at all. 
                if not ApprovalCheck("Laura", 400):
                    ch_l "I don't dance."     
                else:
                    ch_l "I don't feel like it."       
                $ Adjacent.remove("Laura")
            
    if not Adjacent:
            return
    
    
    if Adjacent[0] == "Rogue": 
        if "stripping" in R_DailyActions and ApprovalCheck(Adjacent[0], 500, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Kitty": 
        if "stripping" in K_DailyActions and ApprovalCheck(Adjacent[0], 500, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Emma": 
        if "stripping" in E_DailyActions and ApprovalCheck(Adjacent[0], 600, TabM = 3):
            $ Line = "daily"
    elif Adjacent[0] == "Laura": 
        if "stripping" in newgirl["Laura"].DailyActions and ApprovalCheck(Adjacent[0], 550, TabM = 3):
            $ Line = "daily"
            
    if Line == "daily":        
            $ Line = renpy.random.choice(["You liked the show earlier?",       
                "Didn't get enough earlier?",
                "You're going to wear me out."]) 
    else:
            $ Line = renpy.random.choice(["Ok, that sounds fun.",       
                "I could get into that.",
                "Yeah, ok."]) 
    call AnyLine(Adjacent[0],Line)   
    $ Line = 0
    
    call AllReset("All")
    
    if "Rogue" in Adjacent: 
            show Rogue at Rogue_Dance1()
            $ R_RecentActions.append("stripping")                      
            $ R_DailyActions.append("stripping") 
            $ R_Strip += 1 
            $ R_Action -= 1    
            $ Count = Tempmod
            if R_SeenChest or R_SeenPussy:              
                #You've seen her tits.
                $ Count += 20
            if R_SeenPanties:                           
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in R_Traits:
                $ Count += (4*Taboo)
            if ("dating" in R_Traits or "sex friend" in R_Petnames or "Rogue" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in R_Traits:
                $ Count -= 40 
            elif R_ForcedCount and not R_Forced:
                $ Count -= 5 * R_ForcedCount
            if Adjacent[0] == "Rogue":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count  
    if "Kitty" in Adjacent:    
            show Kitty_Sprite at Kitty_Dance1()
            $ K_RecentActions.append("stripping")                      
            $ K_DailyActions.append("stripping") 
            $ K_Strip += 1 
            $ K_Action -= 1    
            $ Count = Tempmod
            if K_SeenChest or K_SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if K_SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in K_Traits:
                $ Count += (4*Taboo)
            if ("dating" in K_Traits or "sex friend" in K_Petnames or "Kitty" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in K_Traits:
                $ Count -= 40 
            elif K_ForcedCount and not K_Forced:
                $ Count -= 5 * K_ForcedCount
            if Adjacent[0] == "Kitty":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count                
    if "Emma" in Adjacent: 
            show Emma_Sprite at Emma_Dance1()
            #fix fill in
            $ E_RecentActions.append("stripping")                      
            $ E_DailyActions.append("stripping") 
            $ E_Strip += 1 
            $ E_Action -= 1    
            $ Count = Tempmod
            if E_SeenChest or E_SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if E_SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in E_Traits:
                $ Count += (4*Taboo)
            if ("dating" in E_Traits or "sex friend" in E_Petnames or "Emma" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in E_Traits:
                $ Count -= 40 
            elif E_ForcedCount and not E_Forced:
                $ Count -= 5 * E_ForcedCount
            if Adjacent[0] == "Emma":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count   
    if "Laura" in Adjacent: 
            show Laura_Sprite at Laura_Dance1()
            #fix fill in
            $ newgirl["Laura"].RecentActions.append("stripping")                      
            $ newgirl["Laura"].DailyActions.append("stripping") 
            $ newgirl["Laura"].Strip += 1 
            $ newgirl["Laura"].Action -= 1    
            $ Count = Tempmod
            if newgirl["Laura"].SeenChest or newgirl["Laura"].SeenPussy:             
                #You've seen her tits.
                $ Count += 20
            if newgirl["Laura"].SeenPanties:                          
                #You've seen her panties.
                $ Count += 5
            if "exhibitionist" in newgirl["Laura"].Traits:
                $ Count += (4*Taboo)
            if ("dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames or "Laura" in P_Harem) and not Taboo:
                $ Count += 15
            elif "ex" in newgirl["Laura"].Traits:
                $ Count -= 40 
            elif newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:
                $ Count -= 5 * newgirl["Laura"].ForcedCount
            if Adjacent[0] == "Laura":
                #sets the tempmod relative to the girl in question
                $ Tempmod0 = Count
            else:
                $ Tempmod1 = Count   
            
    if len(Adjacent) >= 2:
            "They start to dance."
            $ Partner = Adjacent[1]
            $ Count2 = 1
    else:
            "She starts to dance." 
            $ Count2 = 0
            $ Partner = 0
    
    #this portion adds back in girls who dropped out, but sets their "stop" flag.
    if R_Loc == bg_current and "Rogue" not in Adjacent:
            $ Adjacent.append("Rogue")
            if "stopdancing" not in R_RecentActions:
                    $ R_RecentActions.append("stopdancing")
    if K_Loc == bg_current and "Kitty" not in Adjacent:
            $ Adjacent.append("Kitty")
            if "stopdancing" not in K_RecentActions:
                    $ K_RecentActions.append("stopdancing")
    if E_Loc == bg_current and "Emma" not in Adjacent:
            $ Adjacent.append("Emma")
            if "stopdancing" not in E_RecentActions:
                    $ E_RecentActions.append("stopdancing")
    if newgirl["Laura"].Loc == bg_current and "Laura" not in Adjacent:
            $ Adjacent.append("Laura")
            if "stopdancing" not in newgirl["Laura"].RecentActions:
                    $ newgirl["Laura"].RecentActions.append("stopdancing")
            
    
    $ Tempmod = Tempmod0
    $ Trigger = "strip"
    $ Count = 1
    
    while Count and Round >=10:
            #Loops endlessly until you do something.
            $ Round -= 2 if Round > 2 else Round
            call GirlLikesGirl(Adjacent[0],Partner,600,1,1)
            if len(Adjacent) >= 2:            
                call GirlLikesGirl(Adjacent[1],Adjacent[0],600,1,1)
            menu:
                "Continue":
                        pass
                "Would you kindly take off some clothes?":
                        #add checks here
                        call AnyLine(Adjacent[0],"Hmm?")  
                        $ Count = 0
                "Stop":
                        jump Group_Strip_End
                
    
    
label Group_Stripping:    
    while Round >= 10 and Adjacent: 
        $ Round -= 2 if Round > 2 else Round
        
        
        if Adjacent[Count] == "Rogue": 
                call R_Stripping
        elif Adjacent[Count] == "Kitty": 
                call K_Stripping
        elif Adjacent[Count] == "Emma": 
                call E_Stripping
        elif Adjacent[Count] == "Laura": 
                call Laura_Stripping
        
        $ Trigger = "strip"
        
        if not Adjacent:
                #If everyone leaves, quit out
                jump Group_Strip_End
                
        if len(Adjacent) >= 2:     
            call GirlLikesGirl(Adjacent[Count],Partner,800,2,1)
            call GirlLikesGirl(Adjacent[Count2],Adjacent[Count],800,2,1)
                            
        if len(Adjacent) >= 2:
                # Flips the numbers if in a group
                if Count == 0:
                    $ Count = 1
                    $ Count2 = 0
                    $ Tempmod1 = Tempmod
                    $ Tempmod = Tempmod0
                elif Count == 1:
                    $ Count = 0
                    $ Count2 = 1
                    $ Tempmod0 = Tempmod
                    $ Tempmod = Tempmod1
                $ Partner = Adjacent[Count2]
                
                call Activity_Check(Adjacent[Count],Partner)                
                                    
        if len(Adjacent) < 2:
                #Plays if only one girl
                if Count == 0:
                        $ Tempmod = Tempmod0
                else:
                        $ Tempmod = Tempmod1   
                        $ Tempmod0 = Tempmod1               
                $ Count = 0
                $ Count2 = 0
                $ Partner = 0   
                
                call Activity_Check(Adjacent[Count],Partner)
            
                if "stopdancing" in R_RecentActions: 
                        jump Group_Strip_End      
                if "stopdancing" in K_RecentActions: 
                        jump Group_Strip_End                  
                if "stopdancing" in E_RecentActions: 
                        jump Group_Strip_End                  
                if "stopdancing" in newgirl["Laura"].RecentActions: 
                        jump Group_Strip_End 
        #ends loop
    if Adjacent and Round <=15:        
            call AnyLine(Adjacent[0],"It's getting late, we should probably take a break.") 
   
label Group_Strip_End:  
    #add like-ups here. . .
    if "stopdancing" in R_RecentActions:
                $ R_RecentActions.remove("stopdancing")
    if "keepdancing" in R_RecentActions:
                $ R_RecentActions.remove("keepdancing")
                
    if "stopdancing" in K_RecentActions:
                $ K_RecentActions.remove("stopdancing")
    if "keepdancing" in K_RecentActions:
                $ K_RecentActions.remove("keepdancing")
                
    if "stopdancing" in E_RecentActions:
                $ E_RecentActions.remove("stopdancing")
    if "keepdancing" in E_RecentActions:
                $ E_RecentActions.remove("keepdancing")
                
    if "stopdancing" in newgirl["Laura"].RecentActions:
                $ newgirl["Laura"].RecentActions.remove("stopdancing")
    if "keepdancing" in newgirl["Laura"].RecentActions:
                $ newgirl["Laura"].RecentActions.remove("keepdancing")
    
    call Set_The_Scene(1,0,0,0)    
    $ Count = 0
    $ Count2 = 0
#    $ renpy.pop_call()
    return
    
#end Dancing/Stripping / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
