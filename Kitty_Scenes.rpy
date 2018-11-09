# start KittyMeet //////////////////////////////////////////////////////////

label KittyMeet:    
    $ bg_current = "bg campus"   
    call CleartheRoom("All",0,1)
    $ K_Loc = "bg kitty"  
    $ K_Love = 400        
    $ K_Obed = 100            
    $ K_Inbt = 0  
    call Shift_Focus("Kitty")    
    call Set_The_Scene(0)
    $ K_SpriteLoc = StageCenter
    $ K_Petname = Playername[:1]     
        
    "As you rush to class, you see another student running straight at you."
    "You try to move aside, but aren't fast enough to get out of her way,"
    "She crashes into you at a full jog, and you both fall to the ground."
    "You scramble to your feet and offer the girl a hand up."
    show Kitty_Sprite at SpriteLoc(K_SpriteLoc) with vpunch       
    $ K_Loc = "bg campus" 
    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -25) 
    call KittyFace("surprised")
    $ K_Arms = 1
    ch_u "Hey!"
    $ K_Brows = "angry"
    ch_u "What the hell was that?"
    $ Cnt = 1
    
    menu:
        extend ""
        "You crashed into me!":
            call KittyFace("confused", 2)   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 20)         
            ch_u "Wha! Well, yeah. . ."
            $ K_Blush = 1
            $ Cnt = 0
        "Sorry about that.":
            call KittyFace("bemused", 1) 
            $ K_Eyes = "side"
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 25) 
            ch_u "Well, I guess it[K_like]wasn't entirely your fault. . ."
        "A meet-cute?":
            call KittyFace("surprised", 2) 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)           
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 10) 
            ch_u "  !  "
            call KittyFace("bemused", 1) 
            ch_u "Hmm. . . maybe. . ."
    
    
    ch_p "My name's [Playername], by the way." 
    if Cnt:
        call KittyFace("smile", 1)
        ch_k "Mine's Kitty! Kitty Pryde. Nice to meet you!"
    else:
        call KittyFace("sadside", 1)
        ch_k "Um, mine's Kitty." 
    call KittyFace("normal", 1)
    $ K_Mouth = "sad"
    ch_k "I just[K_like]didn't expect to bounce off you like that. Normally I can phase through things." 
    
    menu:                                                               # + 5-10
        extend ""
        "Losing your touch?":
            call KittyFace("confused", 0)           
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5) 
            ch_k "I don't {i}think{/i} that's it. . ." 
            ch_p "Just kidding. . ."
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
        "Was I too distracting?":
            call KittyFace("angry", 1, Brows = "normal")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -2)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 8)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 4) 
            ch_k "Like, no."
            ch_p "Heh, I guess not."
        "It must be my powers." :
            call KittyFace("confused", 0) 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
            ch_k "Oh?"
            
    ch_p "I have the ability to negate mutant powers, so you can't phase through me." 
    call KittyFace("perplexed", 0)    
    ch_k "Oh! Wow, that's an interesting power. So if you grab me, I can't get away?"
    
    menu:                                                               # +10
        extend ""
        "Want to give it a try?":
            call KittyFace("perplexed", 0) 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 5) 
            ch_k "I'm definitely curious."
        "I guess so.":
            call KittyFace("sadside", 0, Mouth = "lipbite")         
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 3)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 7) 
            ch_k "I'd like to give it a try."
        "Does that turn you on?":            
            call KittyFace("surprised", 2)         
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5) 
            ch_k "What?! No! . ."   
            call KittyFace("bemused", 1)          
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 5) 
            $ K_Eyes = "side"
            ch_k ". . . no."
            $ K_Eyes = "sexy"            
            ch_k "But it is[K_like]worth testing."
            
    ch_p "Ok, let's give it a shot."
    "You reach out and grab her wrist."
    call KittyFace("angry", 1, Eyes = "down")
    "She struggles for a few moments to shake you free, but you hold firm."
    $ Cnt = 0
    while Cnt < 3:
        menu:
            extend ""
            "Let her go.":  
                if not Cnt:                                     #you let go instantly
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 7)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, -2)    
                elif Cnt == 1:                                  #she just asked you to let go
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10) 
                else:                                           #you let go after a pause
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)            
                "You release her arm and step back."
                $ Cnt = 4
            "Hold on.":
                "You continue to hold onto her arm and she fidgets uncomfortably."
                if not Cnt:
                    $ K_Eyes = "sexy"                      
                    ch_k "Are you[K_like]going to let go of my arm any time soon?"
                elif Cnt == 2:
                    ch_k "Ok, that's enough!"
                    $ K_Eyes = "sexy"  
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, -5)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 10) 
                    "She reaches over and pries your hand loose."
                    $ Cnt = 4
                else: 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -1)          
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 2) 
                    "Um. . ." 
                $ Cnt += 1
            "Pull her in for a hug.":
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5) 
                call KittyFace("surprised", 2)
                ch_k "Hey! Like, not cool!"                
                call KittyFace("angry", 1)
                show Kitty_Sprite at SpriteLoc(K_SpriteLoc) with vpunch   
                "She elbows you in the ribs and shoves herself back a few steps."          
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 10) 
                ch_k "My powers may not work on you, but I have[K_like]a few years of combat experience on you."
                ch_k "And don't you forget it!"
                $ Cnt = 10
    
    
    if Cnt > 3:       
        $ K_Eyes = "side"  
        ch_k "Still though, that was an interesting experience. . ."
    else:
        call KittyFace("bemused", 1, Eyes = "side")
        ch_k "That was an interesting experience. . ."   
    $ K_Eyes = "sexy"  
    $ K_Mouth = "lipbite"
    ch_k "Kinda tingly. . ."
    #$ K_Addictionrate = 5 #fix, add this back in once fully functional addiction
    
    $ Cnt = 0
    call KittyFace("surprised", Mouth = "kiss")
    ch_k "Oh! I[K_like]totally forgot, I have to get to a briefing!"
    if Cnt < 5:
        call KittyFace("smile")
        ch_k "I'll see you later though! Like, bye!"
    else:
        call KittyFace("normal")
        ch_k "I'll see you around I guess. Like, bye!"        
    
    $ K_Loc = "bg kitty"         
    call Set_The_Scene
    
    "She jogs off down the path, and you continue on to class."
    $ K_History.append("met")
    $ bg_current = "bg classroom"            
    $ Round -= 10      
    call Shift_Focus("Rogue")
    return
            
# end KittyMeet //////////////////////////////////////////////////////////            
           
# Event Kitty Sleepover /////////////////////////////////////////////////////  
label Kitty_Sleepover(sleepover = 0):
            #This event gets called from the Location menus when time passes in the Night timeframe.
            call Shift_Focus("Kitty")
            if bg_current == "bg kitty":
                    ch_k "I'm getting kinda tired. . ."
            else:
                    ch_k "It's late, I'm thinking of heading out. . ."  
            if Day <= 14:        
                ch_k "It's nice hanging out, but we've just met, so, see you tomorrow."  
            else:      
                call KittyFace("sexy", 1)
                if K_Sleep >= 3 and ApprovalCheck("Kitty", 800):                                 #You've slept over several times and she still likes you
                        if bg_current == "bg kitty":
                                ch_k "So, you staying over?"
                        else:
                                ch_k "Can I sleep over?"
                        $ sleepover = 1
                    
                elif K_Sleep < 3 and ApprovalCheck("Kitty", 1100, "LI"):                        #You haven't slept over much, but she wants you to
                        call KittyFace("bemused", 1)
                        if bg_current == "bg kitty":
                            ch_k "So[K_like]did you want to stay over?"  
                        else:
                            ch_k "So[K_like]could I stay over?"
                        $ sleepover = 1    
                    
                elif K_Sleep < 3 or not ApprovalCheck("Kitty", 600):                            #She doesn't especially want you there.  
                        if bg_current == "bg kitty":
                            ch_k "[K_Like]could you head out? I'll see you tomorrow." 
                        else:
                            ch_k "I should[K_like]get going. . ."
                        
                else: #If she's uninterested
                        if bg_current == "bg kitty":
                            ch_k "You should[K_like]head out." 
                        else:
                            ch_k "See ya tomorrow, [K_Petname]."
                                              
                menu:
                    extend ""
                    "Sure." if sleepover:
                            if K_Sleep <= 5:
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 5) if K_Love >= 500 else K_Love
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 25)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 25, 25) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                            ch_k "Great! I'll get changed."
                        
                    "No, sorry." if sleepover:                  
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 30, 6)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 40, 4)
                            $ K_Brows = "sad"
                            ch_k "Alright. . . see you tomorrow. . ."
                            $ sleepover = 0
                            
                    "Ok, I'll head out. Good night." if not sleepover and bg_current == "bg kitty":                        
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 25, 2)            
                            call KittyFace("smile")
                            ch_k "Ok, good night. . ."
                    "Ok, see you later then. Good night." if not sleepover and bg_current != "bg kitty":                        
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 3)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 25, 2)            
                            call KittyFace("smile")
                            ch_k "Yeah, 'night, [K_Petname]. . ."
                        
                    "Are you sure I can't stay the night? . ." if not sleepover and not K_Sleep and bg_current == "bg kitty": 
                            if ApprovalCheck("Kitty", 1000) or ApprovalCheck("Kitty", 700, "L") or ApprovalCheck("Kitty", 500, "O"):
                                call KittyFace("bemused", 1)                   
                                ch_k "Well, Maaaybeee. . ."
                                $ sleepover = 1 
                            else:                    
                                call KittyFace("smile")
                                $ K_Brows = "confused"
                                ch_k "Ehhhh. . . no, not tonight, [K_Petname]. Sorry." 
                    "Are you sure you can't stay? . ." if not sleepover and not K_Sleep and bg_current != "bg kitty": 
                            if ApprovalCheck("Kitty", 1000) or ApprovalCheck("Kitty", 700, "L") or ApprovalCheck("Kitty", 500, "O"):
                                call KittyFace("bemused", 1)                   
                                ch_k "Well, Maaaybeee. . ."
                                $ sleepover = 1 
                            else:                    
                                call KittyFace("smile")
                                $ K_Brows = "confused"
                                ch_k "Ehhhh. . . no, not tonight, [K_Petname]. Sorry." 
                                
                    "That's not what you said the other night . ." if not sleepover and K_Sleep: #if she wants you gone  
                            if ApprovalCheck("Kitty", 900)or ApprovalCheck("Kitty", 700, "L") or ApprovalCheck("Kitty", 500, "O"):
                                call KittyFace("bemused", 1)                  
                                ch_k "and that went pretty well. . ."
                                $ sleepover = 1
                            else:                    
                                call KittyFace("smile")
                                $ K_Brows = "confused"
                                if bg_current == "bg kitty":
                                    ch_k "Um, no, 'fraid not. Scoot." 
                                else:                        
                                    ch_k "Um, no, 'fraid not. I'll see ya." 
                    
            if sleepover: #If she agreed
                    if K_SEXP < 10 and not ApprovalCheck("Kitty", 600, "I") and not ApprovalCheck("Kitty", 600, "O"):
                            ch_k "Just keep your hands to yourself. . ."        
                    jump Kitty_Morning
            jump Return_Player    
    
label Kitty_Morning:
            #This label is jumped too from Kitty Sleepover if you successfully stay the night
            call Shift_Focus("Kitty")
            call KittyOutfit("sleep")
            "Kitty changes into her sleepwear."
            ch_k "Ah, that's better."
            ch_k "Night, [K_Petname]"                                               #fix add sex option here
            show blackscreen onlayer black    
            pause 2
            call Wait(Lights = 0) 
            $ K_Loc = bg_current
            call KittyOutfit("sleep")
            
            $ D20 = renpy.random.randint(40, 70)                                #This element sends player to the Morningwood event        
            if "hungry" in K_Traits and D20 > 50:
                    $ Cnt = 1
            elif D20 >= K_Lust:
                    $ Cnt = 0     
            elif K_SEXP <= 15:
                    $ Cnt = 0         
            elif K_Blow >= 5 or ApprovalCheck("Kitty", 900, "I"):
                    $ Cnt = 1
            elif K_Blow and ApprovalCheck("Kitty", 900):
                    $ Cnt = 1
            elif ApprovalCheck("Kitty", 1400): # Trinity < 1400
                    $ Cnt = 1
            else:
                    $ Cnt = 0 
                 
            if Cnt:   
                    call Kitty_SexAct("morningwood") 
                    ch_k "Hmmm. . ."
                                    
            call KittyFace("smile")
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            ch_k "G'morning . . ."
            menu:
                extend ""
                "It's always nice sleeping with you." if K_Sleep: 
                        if K_Sleep < 5:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 8)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 8)    
                        $ K_Blush = 1
                        ch_k "And that's always nice to hear."
                        ch_k "We'll have to keep this up."
                "I loved sleeping next to you." if not K_Sleep:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)            
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 10)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 12)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 12)  
                        $ K_Blush = 2
                        ch_k "Yeah, I. . [K_like]I had fun too."
                        $ K_Blush = 1
                        ch_k "I wouldn't[K_like]mind doing it again."   
                        $ K_Blush = 2
                        ch_k "You know, some other time. . . "
                        $ K_Blush = 1
                "It was fun.":
                        if not K_Sleep:                    
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)            
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 8)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 15)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 15) 
                        elif K_Sleep < 5:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 8)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 35, 8)             
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 8)
                        if K_Love >= 800:
                            call KittyFace("bemused")
                        else:
                            call KittyFace("confused")
                        ch_k "Yeah, I mean I guess it was. . ."
                "You were constantly tossing around.":            
                        $ K_Blush = 1
                        if ApprovalCheck("Kitty", 800, "L"):
                            call KittyFace("bemused")
                        else:
                            call KittyFace("angry")
                        if K_Sleep < 5:
                            ch_k "!"
                            ch_k "I don't make a habit out of it. . ."                       
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 60, -8)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 22)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 22)  
                        else:
                            ch_k "Yeah, well. . . you should be used to that!"
                "You need to learn to stick to your side.":  
                        if K_Sleep < 5:
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, -8) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 40)  
                        if ApprovalCheck("Kitty", 500, "O"):
                            call KittyFace("normal")
                            ch_k "Fine, whatever."
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 8) if K_Sleep < 5 else K_Obed
                        else:
                            call KittyFace("angry")
                            ch_k "That's not how you get me to come back." 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 35, 20) if K_Sleep < 5 else K_Inbt  
                        
            #fix add sex option here
            $ K_Blush = 0
            $ K_Sleep += 1    
            call Kitty_Schedule
            call RogueFace("normal")
            if K_Outfit != "sleep":
                "Kitty changes out of her sleepwear."
            call KittyOutfit
            call Girls_Location
            return
    
# end Event Sleepover /////////////////////////////////////////////////////
# start Event Morning Wood /////////////////////////////////////////////////////

label Kitty_MorningWood:
            # this label is called from the Kitty_SexAct("morningwood"), 
            # which was called from Kitty_Sleepover, which was called from a Location.
            call Shift_Focus("Kitty")
            $ P_Focus = 30
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 5)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5) 
            $ K_RecentActions.append("blanket")           
            call Kitty_BJ_Launch
            "You feel a pleasant sensation. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 5)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5)
            "It's somewhere below your waist. . ."
            ch_u "\"Slurp, slurp, slurp.\""
            $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 10)
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5)
            $ Trigger = "blow"
            $ K_Eyes = "down"
            "You open your eyes. . ."
            hide NightMask onlayer nightmask  
            hide blackscreen onlayer black
            $ Speed = 3
            $ Count = 3
            $ Line = 0
            call Kitty_First_Peen(1)
            while Count > 0:
                    #Looping portion
                    $ P_Focus = Statupdate("Kitty", "Focus", P_Focus, 80, 10)
                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 5)
                    menu:
                        extend ""
                        "Stay Quiet":
                            if Count >2:
                                "You just let her do her thing and pretend to still be asleep."
                            elif Count:
                                "It does feel nice. . ."
                            elif not Count:
                                "You wouldn't want to disturb her. . ."
                            ch_k "\"Slurp, slurp, slurp.\""
                        "Um, [K_Pet]? What're you doing?":
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
            $ K_Blush = 1
            "She pulls back with a pop."
            if Line == "question":
                    call KittyFace("smile")
                    ch_k "I wasn't[K_like]being subtle about it, [K_Petname]." 
            elif Line == "praise":
                    call KittyFace("smile")
                    ch_k "Mmm, hehe."
            elif Line == "no":
                    $ Speed = 0
                    call KittyFace("angry")
                    $K_Brows = "confused"
                    ch_k "{i}That's{/i} the thanks I get?!"
            else:
                    ch_k "You can stop faking it, [K_Petname]. . ."
                    ch_k "This guy's telling me you're awake now."
                
            menu:
                extend ""
                "So, um, you want to get back to it?":
                        if Line != "no":
                            call KittyFace("smile")
                            ch_k "Hehe, mmmm. . ."
                        elif Line == "no" and ApprovalCheck("Kitty", 1750):
                            call KittyFace("bemused")
                            ch_k "Wha? Well. . . I guess. . ."
                            $ Line = "maybe"
                        else:
                            call KittyFace("angry")
                            ch_k "You can't walk that one back!"
                            ch_k "You can take care of that yourself."
                "Were you more interested in something else?":
                        if Line != "no":
                            call KittyFace("sexy")
                            ch_k "Maaaybee. . . like what?"
                            $ Line = "sex"
                        elif Line == "no" and ApprovalCheck("Kitty", 1650):
                            call KittyFace("bemused")
                            ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                            ch_k "Like what?"
                            $ Line = "sex"
                        else:
                            call KittyFace("angry")
                            ch_k "Well not anymore!"   
                            ch_k "You can take care of that yourself."
                "Sorry, sorry, please continue." if Line == "no":
                        if (K_Love + K_Obed + K_Inbt) >= 1450:
                            call KittyFace("bemused")
                            ch_k "I guess I can forgive you. . ."
                            $ Line = "maybe"
                        else:
                            call KittyFace("angry")
                            ch_k "As if."
                "Sorry, but we could do something else." if Line == "no":
                        if ApprovalCheck("Kitty", 1350):
                            call KittyFace("sexy")
                            ch_k "I guess, maybe. . ."
                            ch_k "Like what?"
                            $ Line = "sex"
                        else:
                            call KittyFace("angry")
                            ch_k "As if."
                "Not when I'm just waking up.":
                        call KittyFace("angry")
                        ch_k "Aw. . ."
                        $K_Eyes = "side"
                        ch_k "Last time I do you a favor. . ."
                        $ Line = "no"
                        
            $ K_RecentActions.remove("blanket") 
            if Line == "no":
                    call Kitty_BJ_Reset
                    if bg_current == "bg player":  
                        ch_k "I'm out of here."
                    else:
                        ch_k "Get out of my face."
                    call KittyOutfit
                    $ renpy.pop_call()
                    jump Return_Player
            elif Line == "sex":
                    call Kitty_BJ_Reset
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



# Event Kitty_Caught_Masturbating  /////////////////////////////////////////////////////  

#Not updated

label Kitty_Caught_Masturbating:
            #This label is called from a Location
            call Shift_Focus("Kitty")
            "You hear some odd noises coming from Kitty's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call KittyOutfit(Changed=1)    
            $ K_Upskirt = 1
            $ K_PantiesDown = 1
            $ K_Loc = bg_current
            call Set_The_Scene(0)
            call Display_Kitty(0)
            call KittyFace("sexy")
            $ K_Eyes = "closed"
            $ Kitty_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ K_DailyActions.append("unseen")
            $ K_RecentActions.append("unseen")    
            call Kitty_SexAct("masturbate")
            if "angry" in K_RecentActions:
                return
        
#After caught masturbating. . .
            $ K_Eyes = "sexy"
            $ K_Brows = "confused"
            $ K_Mouth = "smile"
            if K_Mast == 1:        
                    $ K_Mouth = "kiss"
                    ch_k "So[K_like]I wasn't expecting company. . ."
                    $ K_Eyes = "side"
                    $ K_Mouth = "lipbite"        
                    ch_k "but I didn't exactly mind it either. . ."
                    $ K_Eyes = "sexy"
                    $ K_Brows = "normal"         
                    $ K_Mouth = "smile"
                    ch_k "Maybe knock next time?" 
            else:
                    ch_k "You seem to be making a habit of dropping in."            
            $ Kitty_Arms = 1  
            call KittyOutfit      
            return
    
# end Kitty_Caught_Masturbating/////////////////////////////////////////////////////

# Event Kitty_Key /////////////////////////////////////////////////////  

#Not updated

label Kitty_Key:
            call Shift_Focus("Kitty")
            call Set_The_Scene
            call KittyFace("bemused")
            $ Kitty_Arms = 2
            ch_k "So you've[K_like]been dropping by a lot lately, I figured you might want a key. . ."
            ch_p "Thanks."
            $ Kitty_Arms = 1    
            $ Keys.append("Kitty")
            $ K_Event[0] = 1
            return
# end Event Kitty_Key /////////////////////////////////////////////////////


# Event Kitty_Caught /////////////////////////////////////////////////////  

#Not updated

label Kitty_Caught:
    call Shift_Focus("Kitty")
    call Checkout
    ch_k "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call KittyOutfit
    if R_Loc == bg_current:         
        $ R_Loc = "bg study"
    if E_Loc == bg_current:                
        $ E_Loc = "bg study"        
    $ bg_current = "bg study"  
    $ K_Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    show Kitty_Sprite at SpriteLoc(StageRight) with ease
    if E_Loc == bg_current:         
        show Emma_Sprite at SpriteLoc(StageFarRight) with ease
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call KittyFace("sad")
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
    
    if K_Shame >= 40:
        ch_x "Kitty, my dear, you're practically naked! At least throw a towel on!"
        "He throws Kitty the towel."
        show blackscreen onlayer black 
        $ K_Over = "towel"         
        hide blackscreen onlayer black
    elif K_Shame >= 20:
        ch_x "Kitty, my dear, that attire is positively scandalous."
    
    if K_Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1)
        $ R_Eyes = "side"
        
    $ Count = K_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if K_Caught < 5:
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 10)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, -25)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -10) 
            call XavierFace("happy")  
            if K_Caught:
                ch_x "But you know you've done this before. . . at least [K_Caught] times. . ." 
            elif R_Caught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [R_Caught] times. . ." 
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
            
        "Just having a little fun, right [K_Pet]?":
            call Kitty_Namecheck
            call KittyFace("bemused")         
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 10)   
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10) 
            call XavierFace("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 20)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, -20)   
            ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Kappa, Kitty!" if "Xavier's photo" in P_Inventory and P_Lvl >= 5:
            if ApprovalCheck("Kitty", 1500, TabM=1, Loc="No"):                   
                    jump Plan_Kappa
            elif ApprovalCheck("Kitty", 1000, TabM=1, Loc="No"):
                    call KittyFace("perplexed") 
                    $ K_Brows = "sad"
                    ch_k "You know. . . I really don't think that's a good idea. . ."
                    menu:
                        "Dammit Kitty. . .":
                                call KittyFace("angry")
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5) 
                        "Yeah, I guess you're right. . .":
                                call KittyFace("bemused") 
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
            else:
                    call KittyFace("confused") 
                    ch_k "Wait, Plan what??"
                    ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                    ch_k "I have no {i}idea{/i} what you're talking about."
                    ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                    call KittyFace("bemused") 
            call XavierFace("angry")
            $ Count += 10
            ch_x "I have no idea what that was about, but it sounds like you haven't learned."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."                
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, -10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -5)   
            ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call KittyFace("surprised")
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 25)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 40)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!" 
            if K_Inbt > 50:
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 15)             
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 30, -20)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -10)    
            ch_x "Now get out of my sight."
            
    $ PunishmentX += Count            
    $ K_Caught += 1
    $ K_RecentActions.append("caught")
    $ K_DailyActions.append("caught") 
    call Remove_Girl("All")  
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Kappa:
    call KittyFace("sly")         
    "As you say this, a sly grin crosses Kitty's face."
    $ K_Arms = 0
    $ Kitty_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."    
    $ K_Arms = 2
    show Kitty_Sprite at SpriteLoc(StageLeft+100,150) with ease
    $ K_SpriteLoc = StageCenter
    "Kitty moves in sits on his lap, pinning his arms to the chair."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    call XavierFace("angry")
    
    if "Kappa" in P_Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
    else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the photo you found earlier in his study."
            ch_p "I have here a rather. . . compromising photo of you and Mystique."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "Kitty here's set it to distribute to every computer in school, every day."
            ch_p "And only I know the password." 
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ." 
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 40)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 30)
    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    while Count:
        $ Count -= 1
        menu:
            ch_k "Well, [K_Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if Rules:
                    ch_x "Very well. . . I could offer you some. . . discretion. . ."
                    $ Rules = 0
            "You know, it's kinda fun dodging you, catch us if you can." if not Rules:
                    ch_x "If you. . . want me to, I suppose. . ."
                    $ Rules = 1
            "Raise my stipend." if P_Income < 30 and "Kappa" not in P_Traits:    
                    ch_x "Very well. . . but I can only raise it by so much. . ."        
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Kappa" in P_Traits:           
                    pass
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            ch_x "Fine, although you don't seem to need it. . ."  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            ch_x "I. . . suppose I could do that. . ."  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Kitty's room." if "Kitty" not in Keys:  
                            ch_x "Couldn't she provide it? Oh, never mind, here. . ."  
                            $ Keys.append("Kitty")
                    "Give me the key to Kitty's room.[[Owned] (locked)" if "Kitty" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_x "Very well, that should conlude our business. Please leave." 
    if "Kappa" not in P_Traits:
        $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 90, 10)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 70, 10)
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
        $ P_Traits.append("Kappa")
    $ Kitty_Arms = 1
    "You return to your room"
    jump Player_Room
                              
# end Kitty_Caught/////////////////////////////////////////////////////

# start Kitty_BF//////////////////////////////////////////////////////////

#Not updated
label Kitty_BF:
    call Shift_Focus("Kitty")
    
    if K_Loc != bg_current and "Kitty" not in Party:
        "Kitty approaches you and asks if the two of you can talk."
        "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."    
                
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call Taboo_Level
    call CleartheRoom("Kitty")
    $ K_DailyActions.append("relationship")
    call KittyFace("bemused", 1)
    ch_k "So, [K_Petname], we've[K_like]been hanging for a while, right?"
    ch_k ". . ."
    $ K_Eyes = "sexy"
    menu:
        ch_k "Right?"
        "Yeah. And it's been amazing.":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
        "Yeah, I guess":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 10)
        "Uhm. . .maybe?":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
    if K_SEXP >= 10:
        ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if K_SEXP >= 15:
        ch_k "You know[K_like]. . .in the {i}bedroom{/i}. . ."
    if "dating" in R_Traits and "dating?" in K_Traits:    
        ch_k "I know you're kinda[K_like]Rogue's boyfriend and all. . . but she and I were talking and[K_like]. . ."
    elif "dating" in K_Traits:
        ch_k "I know you're kinda[K_like]Rogue's boyfriend and all. . ."
    if not K_Event[5]:
        ch_k "So, uhm. . ."
        ch_k "It’s not like I[K_like]haven’t gone out with guys before."
        ch_k "I just[K_like]..wow, this is so awkward.  I really like you a lot and. . ."
        ch_k "I mean. . . do you wanna[K_like]be my boyfriend?"
        ch_k "[K_Like]maybe we could make it official?"
    elif "dating?" in K_Traits: 
        ch_k "Rogue said it’d totally be cool if we were[K_like]dating, too." 
    elif "dating" in R_Traits: 
        ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:        
        ch_k "I wish you weren’t[K_like]such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_k "I wanna be your girlfriend[K_like]officially."
    $ K_Event[5] += 1
    menu: 
        extend ""
        "Are you kidding?  I'd love to!":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30)
            $ K_Petnames.append("boyfriend")
            $ K_Traits.append("dating")
            "Kitty wraps her arms around you and starts kissing you passionately."
            call KittyFace("kiss") 
            $ K_Kissed += 1
        "Uhm[K_like]okay.":
            $ K_Petnames.append("boyfriend")
            $ K_Traits.append("dating")
            $K_Brows = "confused"
            "Kitty seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."    
        "I'm with Rogue now." if "dating" in R_Traits:             
            call KittyFace("sad",1)    
            ch_k "I know.  I just[K_like]. . . I thought maybe you could go out with me, too, maybe?"
            menu:
                extend ""
                "Yes.  Absolutely.":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30)
                    $ K_Petnames.append("boyfriend")
                    $ K_Traits.append("dating")
                    "Kitty wraps her arms around you and starts kissing you passionately."
                    call KittyFace("kiss") 
                    $ K_Kissed += 1
                "I'm sorry, but. .  .no.":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                    ch_k "Well. . . okay. I get it." 
                "No way.":
                    jump Kitty_BF_Jerk
        "Not really.":
            jump Kitty_BF_Jerk
    call KittyFace("sexy")    
    ch_k "Now. . . boyfriend. . . how about you and I[K_like]celebrate, huh?"
    $ Tempmod = 10
    call Kitty_SexMenu
    $ Tempmod = 0
    return
    
label Kitty_BF_Jerk:
    call KittyFace("angry", 1)
    ch_k "Fine![K_Like]. . .be that way!" 
    $ Count = (20* K_Event[5])
    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 40)
    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, Count)
    if K_Event[5] >= 3:
        call KittyFace("sad")
        ch_k "Yeah?  Well. . .[K_like]I don’t care what you want!  We’re dating!  Deal."   
        $ K_Petnames.append("boyfriend")
        $ K_Traits.append("dating")
        $ Achievements.append("I am not your Boyfriend!")
        ch_k "I. . .uhm. . .think I need to[K_like]be alone for a little while."
        $ bg_current = "bg player"  
        call Remove_Girl("Kitty")   
        call Set_The_Scene
        return        
    if K_Event[5] > 1:
        ch_k "It was such a mistake asking you again.  You’re[K_like]still such a jerk!"          
    $ Count = (50* K_Event[5])                                  #fix test to see if negatives can work here.
    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -Count)
    ch_k "Get out, you big jerk!"
    $ bg_current = "bg player"  
    call Remove_Girl("Kitty")  
    $ renpy.pop_call()
    jump Player_Room
    
## end Kitty_BF//////////////////////////////////////////////////////////

## start Kitty_Love//////////////////////////////////////////////////////////
label Kitty_Love:
    call Shift_Focus("Kitty")  
    if K_Event[6]:
            #on repeat attempts
            "Kitty seems kind of shy and shuffles up to you, as if working up her nerve."
    elif bg_current != "bg kitty":
        if K_Loc == bg_current or "Kitty" in Party:
            "Suddenly, Kitty says she wants to talk to you in her room and drags you over there."
        else:
            "Kitty shows up, hurridly says she wants to talk to you in her room and drags you over there."
        $ bg_current = "bg kitty"
    else:
            "Kitty suddenly stares at you very intently."
        
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call CleartheRoom("Kitty")
    call Taboo_Level
    $ K_DailyActions.append("relationship")
    call KittyFace("bemused", 1)
    $ K_Eyes = "side"    
    $ Line = 0
    $ K_Event[6] += 1
    if K_Event[6] == 1:
            if "dating" in K_Traits:
                ch_k "We've[K_like]been together for a while now, and I've been thinking. . ."
            else:
                ch_k "We've[K_like]know each other for a while now, and I've been thinking. . ."
            ch_k "It's been[K_like]kinda hard for me to really get invested in anyone. . ."
            $ K_Eyes = "down"
            ch_k ". . . to[K_like]be comfortable with who they are and be myself. . ."
            $ K_Eyes = "sly"
            ch_k "I just feel like sometimes you. . ."
            $ K_Eyes = "side"
            ch_k "and me[K_like] . ."
            call KittyFace("perplexed", 2)
            $ K_Eyes = "surprised"
            ch_k "Never mind!"
            "Kitty dashes off and phases through the nearest wall."
            hide Kitty_Sprite with easeoutright
            call Remove_Girl("Kitty")
            return
    if K_Event[6] == 2:
        ch_k "Sorry about before, I don't think I was ready maybe. . ."
        ch_k ". . . but I was kind of thinking-"   
    elif K_Event[6] >= 5:
        ch_k "Um. . ."
        $ K_Eyes = "sly"
        ch_k "You know, it's time to stop running. I think I love you."
        $ K_Eyes = "side"
        ch_k "You don't have to say it back, but I do."
        $ K_Petnames.append("lover")
        ch_k "Um, that's all."
    else:
        ch_k "Um. . ."
    if "lover" not in K_Petnames: 
            menu:
                "She turns and makes a break for the nearest wall."
                "Catch her":
                    call KittyFace("perplexed", 2)
                    $ K_Eyes = "surprised"
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 10) 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 15) 
                    "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
                "Let her go":
                    "She dashes through the nearest wall and vanishes from view."
                    jump Kitty_Love_End    
            $ K_Blush = 1
            menu:
                extend ""
                "Pull her close":
                    call KittyFace("smile", 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 20) 
                    "You draw her into an embrace, arms wrapped tightly around her waist."
                    $ Line = "hug"
                "Stay like this":
                    $ K_Eyes = "down"
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 10) 
                    "You keep hold of her wrist."
                    $ Line = "wrist"
                "Let her go":
                    if 1 < K_Event[6] < 4:
                        "You immediately release her wrist."
                        $ K_Eyes = "down"
                        "She dashes through the nearest wall and vanishes from view."
                        jump Kitty_Love_End
                    else:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 10) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 20)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)  
                        "You release her wrist and she takes a step back."
                        
            ch_k "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in K_Petnames:        
            # If she hasn't confessed yet
            ch_k "I thought maybe if I let myself get too close. . ."
            ch_k "I'd fall. . ."
            menu:
                extend ""
                "I'll never let go." if Line:
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 20) 
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)  
                    "She melts into your arms."
                "I'd always catch you.":
                    call KittyFace("smile")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 20) 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 15)
                    "She smiles and shifts a bit uncomfortably."
                "Yeah, you should watch out for that.":
                    call KittyFace("angry", 1)
                    $ K_RecentActions.append("angry")
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20) 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)  
                    "She shoves you away and then stomps through the nearest wall."                        
                    jump Kitty_Love_End
                    
                "So get going. [[Give her a shove]":
                    call KittyFace("surprised", 1)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -50) 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)  
                    "You shove her through the nearest wall and then continue on you way."
                    $ K_RecentActions.append("angry")
                    hide Kitty_Sprite with easeoutbottom
                    jump Kitty_Love_End
                    
    if "lover" in K_Petnames: 
        #if she made the first move
        menu:
            extend "" #"I love you."
            "I love you too.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 40) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 50)  
                        call KittyFace("smile")
            "You love me?":
                call KittyFace("confused", 2)
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 60)  
                        call KittyFace("smile")
                    "I mean, a little?": 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 20)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -10)  
                        ch_k "That's not a \"yes.\" . ."
                        $ Line = "awkward"
                    "Not really.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 30)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -30)  
                        call KittyFace("angry", 2)
                        ch_k "Huh?!"
                        $ Line = "awkward"
            "Huh.":
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -20)  
                menu:
                    ch_k "Huh?!"
                    "I mean, I love you too!":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)  
                        call KittyFace("smile")
                        ch_k "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 30)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -20)  
                        call KittyFace("angry", 2)
                        $ Line = "awkward"
            "Well that's awkward.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 40)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -20)  
                        call KittyFace("perplexed", 2)
                        $ Line = "awkward"
    else:
        menu:
            extend ""
            "I love you, Kitty.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 50) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30)  
                        call KittyFace("smile")
                        $ Line = "love"
            "I think you're pretty great.":
                call KittyFace("confused")
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 30) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)  
                        call KittyFace("smile")
                    "I mean, a little?":
                        if ApprovalCheck("Kitty", 1200, "OI"):
                            call KittyFace("sad")
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 20)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)  
                            ch_k "But[K_like]not \"nothing\". . ."
                        else:
                            $ Line = "awkward"
                    "Not really.":     
                        call KittyFace("sad")                   
                        if ApprovalCheck("Kitty", 1500, "OI"):
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 30)
                            ch_k "Ouch. . ."
                        else:
                            $ Line = "awkward"
            "I was thinking something more casual. . .":
                        call KittyFace("sad")
                        if ApprovalCheck("Kitty", 1200, "OI") or ApprovalCheck("Kitty", 700, "I"):
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 20)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 30)  
                            ch_k "Close enough."
                        else:  
                            $ Line = "awkward"
                            
    if Line == "awkward":   
        if ApprovalCheck("Kitty", 700, "O"):   
            ch_k "Fine, this doesn't have to be love."
        elif ApprovalCheck("Kitty", 700, "I"):
            ch_k "Fine, just sex it is."            
        elif ApprovalCheck("Kitty", 1200, "OI"):
            ch_k "Fine, I can work with that."
        else:
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -50) 
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 95, 50)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -50)  
            ch_k "Oh, well I mean if you don't love me-"
            ch_k "You don't have to love me, that's ok."
            ch_k "I'll, um. . . never mind."
            $ K_RecentActions.append("angry")
        $ K_Event[6] = 20 #this means it shuts down future attempts
    else:
        if Line:
            # If you're holding her
            "She squeezes you even tighter and makes a little whimper."
        else:
            "She dives into your arms with a little squeek."
        if "lover" not in K_Petnames:
            ch_k "I love you too. . ."
            ch_k "I think I have for a while now."
            $ K_Petnames.append("lover")
    
label Kitty_Love_End:    
    if Line == "awkward" or "lover" not in K_Petnames:
            hide Kitty_Sprite with easeoutright
            call Remove_Girl("Kitty")
            return
    if not K_Sex:
        ch_k "So I was thinking. . . did you want to . . ."
        if bg_current != "bg player" and bg_current != "bg kitty":
                ch_k "Wait, let's take this someplace more private. . ."
                $ bg_current = "bg kitty"
                $ K_Loc = bg_current
                call Set_The_Scene
                call CleartheRoom("Kitty")
                call Taboo_Level
                ch_k "Ok, so like I was saying. . ."
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 10)
        menu:
            extend ""
            "Yeah, let's do this. . . [[have sex]":      
                $ K_Inbt = Statupdate("Kitty", "K_Inbt", K_Inbt, 30, 30) 
                ch_k "Hmm. . ."  
                call Kitty_SexAct("sex")
            "I have something else in mind. . .[[choose another activity]":
                $ K_Brows = "confused"
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 70, 20)
                ch_k "Something like. . ."    
                $ Tempmod = 20
                call Kitty_SexMenu     
    return
    
label Kitty_Love_Redux:
    #this is for if you rejected her but want a second chance
    $ Line = 0
    $ K_DailyActions.append("relationship")
    if K_Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgeven me, I still love you."
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 10) 
            if ApprovalCheck("Kitty", 950, "L"):
                $ Line = "love"
            else:
                call KittyFace("sad")   
                ch_k "You've dug too deep a hole, [K_Petname]."
                ch_k "Keep trying though." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            call KittyFace("perplexed",1)   
            ch_k "Um, YEAH?!"
            menu:
                "I'm sorry, I didn't mean it.":
                    $ K_Eyes = "surprised"
                    ch_k "Well, if you. . . so wait, you {i}do{/i} love me?"
                    ch_p "Yeah. I mean, yes, I love you, Kitty."
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 10) 
                    if ApprovalCheck("Kitty", 950, "L"):
                        $ Line = "love"
                    else:
                        call KittyFace("sadside")   
                        ch_k "Well, I don't know how I feel at this point. . ."                        
                "I've changed my mind, so. . .":
                    if ApprovalCheck("Kitty", 950, "L"):
                        $ Line = "love"
                        $ K_Eyes = "surprised"
                        ch_k "Really?!"
                    else:
                        $ K_Mouth = "sad"
                        ch_k "Oh, you've changed your mind. Wonderful."
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 10) 
                        call KittyFace("sadside")    
                        ch_k "Maybe I have too. . ."
                "Um, never mind.":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)  
                    call KittyFace("angry")   
                    ch_k "Seriously?"
                    $ K_RecentActions.append("angry")
    if Line == "love":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 40) 
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, 10)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 90, 10) 
            call KittyFace("smile")    
            ch_k "I[K_like]love you too!"
            if K_Event[6] < 25:             
                call KittyFace("sly")   
                "She slugs you in the arm"
                ch_k "Took you long enough."
            $ K_Petnames.append("lover")                
    $ K_Event[6] = 25
    return
## end Kitty_Love//////////////////////////////////////////////////////////


# start Kitty_Sub//////////////////////////////////////////////////////////

label Kitty_Sub:    
    call Shift_Focus("Kitty")
    if K_Loc != bg_current and "Kitty" not in Party:
        "Suddenly, Kitty shows up and says she needs to talk to you."
    
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call CleartheRoom("Kitty")
    call Taboo_Level
    $ K_DailyActions.append("relationship")
    call KittyFace("bemused", 1)
    
    $ Line = 0
    ch_k "So, uhm. . .you've really kinda[K_like]taken control in our relationship lately."
    menu:    
        extend ""        
        "I guess. That's just kind of what comes naturally for me.":   
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
        "Sorry. I didn't mean to come off like that.":
                call KittyFace("startled", 2)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 5)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -5)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -5)
                ch_k "No!  Don't get the wrong idea!  I just. . ." 
        "Yup. Deal with it.": 
                if ApprovalCheck("Kitty", 1000, "LO"):
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 20)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                        ch_k "Um, yeah. . ."
                else:
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                        call KittyFace("angry")
                        ch_k "I {i}was{/i} going to tell you I kinda liked it.  But I didn't think you'd be[K_like]a {i}jerk{/i} about it!" #(Loss of points)
                        menu:        
                            extend ""
                            "Guess you don't know me so well, huh?":
                                    ch_k "I guess not."
                                    $ Line = "rude"
                            "Sorry.  I kind of thought you were getting into me being like that.": 
                                    call KittyFace("sexy", 2)
                                    $ K_Eyes = "side"
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 5)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 5)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                    ". . ."
     
    $ K_Blush = 1       
    if not Line:
            # She's advancing to the next stage            
            ch_k "Well, I've, uhm. . . never had a guy be like that with me before. . ."
            call KittyFace("sly", 2)
            ch_k "I think I kinda like it."
            call KittyFace("smile", 1)
            menu:
                extend ""
                "Good. If you wanna be with me, that's how it'll be.":
                        if ApprovalCheck("Kitty", 1000, "LO"):
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 15)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                            ch_k "I guess I walked into that one. . ."                        
                        else:
                            call KittyFace("sadside", 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)                      
                            ch_k "You don't have to do it[K_like]{i}all{/i} the time.  You could still be nice once in a while."
                            menu:      
                                extend ""
                                "Whatever.  That's how it is.  Take it or leave it.":
                                        call KittyFace("angry")
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 5)
                                        ch_k "Y'know, you're such a jerk, [Playername]!" 
                                        $ Line = "rude"
                                "I think I could maybe do that." : 
                                        call KittyFace("bemused", 2)
                                        $ K_Eyes = "side"
                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 5)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 3)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                        ch_k "Uhm. . .yeah.  It's[K_like]. . kinda hot."
                                
                "Yeah?  You think it's sexy?":
                            call KittyFace("bemused", 2)
                            $ K_Eyes = "side"
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 5)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                            ch_k "Uhm. . .yeah.  It's[K_like]. . kinda hot."
                        
                "You sure you don't want me to back off a little?":  
                        call KittyFace("startled", 1)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -5)
                        menu:
                            ch_k "Only if you think it might be[K_Like]weird. But I think it's kinda hot."
                            "Only if you're okay with it.":
                                call KittyFace("bemused", 2)
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 10)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":                                
                                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -5)
                                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -10)
                                $ Line = "embarrassed"
                        
                "I don't really care what you like.  I do what I want.":
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 15)
                            call KittyFace("angry")
                            ch_k "Y'know, you're such a jerk, [Playername]!" 
                            $ Line = "rude"
                                        
    if not Line:
        call KittyFace("bemused", 1)
        $ K_Eyes = "down"
        ch_k "Cool.  So. . .just so you know. . .I don't mind[K_like]you being in control."
        if "256 Shades of Grey" in K_Inventory:
                ch_k "Like in that '256 Shades of Grey' book."
        menu Kitty_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -15)
                    $ Line = "embarrassed"
            "I think I could get used to that kinda thing.":
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 5)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                    call KittyFace("smile", 1)
                    $ Line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in K_Inventory and Line != "grey":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 5)
                    call KittyFace("sly", 1)
                    ch_k "You think I wouldn't read something you bought me?  I think you {i}maybe{/i} don't realize how much I like you."
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                    ch_k "Well, I {i}did{/i} read it.  And. . .it turns out it kinda[K_like]. . {i}really{/i} turned me on."
                    ch_k "So. . .what d'you think?  Think[K_like]maybe you'd like that?"
                    $ Line = "grey"
                    jump Kitty_Sub_Choice

    if not Line:
        call KittyFace("smile", 1)
        ch_k "Awesome.  So. . .if you wanted me to, I could[K_like]call you {i}sir{/i} or something."
        call KittyFace("sly", 2)
        ch_k "Think you'd like that?"        
        $ K_Blush = 1  
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 95, 5)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 15)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                    ch_k "Okay, then. . .{i}sir{/i}."              
                    $ K_Petname = "sir"
            "I think I'd rather stick with what we've got going.":
                call KittyFace("startled", 2)
                ch_k "Oh!"
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -5)
                call KittyFace("sadside", 1)
                menu:
                    ch_k ". . . Well. . . maybe you can still kinda[K_Like]be in control, anyway?"
                    "I like that idea.":
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                            call KittyFace("smile", 1)
                            ch_k "You're so awesome, [K_Petname]."
                    "This is getting really weird.":
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -50)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -15)
                            $Line = "embarrassed"
        
#Kitty_Sub_Bad_End:
    $ K_History.append("sir")
    if not Line:
            $ K_Blush = 1  
            "She gives you a piece of paper with the password for her cellphone calender."
            "Apparently, whatever you enter into it, she intends to do. . . within reason."
            $ K_Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":        
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl("Kitty")
            $ renpy.pop_call()
            "Kitty phases through the floor in a huff, leaving you alone."
    elif Line == "embarrassed":
            call KittyFace("sadside", 2)
            ch_k "Oh!  Uhm, yeah! [K_Like]I mean. . .."
            $ K_Mouth = "smile"
            ch_k "I was just kidding.  I[K_like]. . yeah.  That's kinda weird."
            ch_k "I should go.  I think I hear Professor Xavier calling me."
            $ K_Blush = 1            
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl("Kitty")
            $ renpy.pop_call()
            "Kitty phases through the floor, leaving you alone. It didn't look like she could get away fast enough."
    return

label Kitty_Sub_Asked:
    $ Line = 0
    call KittyFace("sadside", 1)
    ch_k "Yeah.  And I also[K_like]remember what a {i}jerk{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in K_Petnames and ApprovalCheck("Kitty", 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck("Kitty", 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        ch_k "Well maybe {i}I'm{/i}[K_like]over that. . ." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 10)
                        call KittyFace("sly", 1)
                        ch_k "Well. . .okay.  I {i}did{/i} think that was pretty hot.  Also, you're super-cute when you apologize." 
                        #Blushing expression.  Kitty kisses player and big addition of points
                        ch_k "Okay.  We can[K_like]try again." 

        "Listen. . .I know it's what you want.  Do you want to try again, or not?":
                call KittyFace("bemused", 1)
                if "sir" in K_Petnames and ApprovalCheck("Kitty", 850, "O"): 
                        ch_k "Ok, fine."
                elif ApprovalCheck("Kitty", 600, "O"): 
                        ch_k "Um, ok."
                else: 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        call KittyFace("sadside", 1) 
                        ch_k "You're[K_like]totally impossible."
                        $ K_Eyes = "squint"
                        ch_k "Maybe you're right.  But I still think you should[K_like] apologize for being a jerk to me."
                        menu:
                            extend ""
                            "Okay, I'm sorry I was mean about it.":
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                                    call KittyFace("bemused", 1)
                                    $ K_Eyes = "side"
                                    ch_k "That's all you had to say."
                            "Not gonna happen.":
                                    if "sir" in K_Petnames and ApprovalCheck("Kitty", 900, "O"): 
                                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                                            ch_k ". . ."
                                    elif ApprovalCheck("Kitty",650, "O"):  
                                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -5)
                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                                            ch_k "I, um. . ."    
                                    else: #if it failed both those things,     
                                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, -10)
                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -10)
                                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -15)                       
                                            "Kitty sighs and rolls her eyes."
                                            call KittyFace("angry", 1)
                                            $ K_Eyes = "side"
                                            ch_k "You really don't learn, do you?"    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                    call KittyFace("angry", 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 90, -10)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -10)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -15)
                                    ch_k "Y'know, if you're gonna throw that in my face, forget it."
                                    ch_k "I should've[K_like]expected you'd be like that."
                                    $ Line = "rude"
    
    $ K_RecentActions.append("asked sub")   
    $ K_DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl("Kitty")
            $ K_RecentActions.append("angry")
            $ renpy.pop_call()
            "Kitty phases through the floor, leaving you alone.  She looked pretty upset."
    elif "sir" in K_Petnames:
            #it didn't fail and "sir" was covered
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 50)
            $ K_Petnames.append("master")  
            $ K_Petname = "master"
            $ K_Eyes = "sly"
            ch_k ". . . master. . ."
    else:
            #it didn't fail
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 30)
            $ K_Petnames.append("sir")  
            $ K_Petname = "sir"
            $ K_Eyes = "sly"
            ch_k ". . . sir."
    return

# end Kitty_Sub//////////////////////////////////////////////////////////


# start Kitty_Master//////////////////////////////////////////////////////////

label Kitty_Master: 
    call Shift_Focus("Kitty")
    if K_Loc != bg_current and "Kitty" not in Party:
        "Suddenly, Kitty shows up and says she needs to talk to you."
    
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call CleartheRoom("Kitty")
    $ K_DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call KittyFace("bemused", 1)
    ch_k "[K_Petname], if you don't mind me saying so. . ."
    ch_k "I think having you be[K_like]in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
                call KittyFace("sly", 1)
                ch_k "Cool.  Maybe we could[K_like]kick it up a notch?"
                menu:
                    extend ""
                    "Nah.  This is just about perfect.":
                            call KittyFace("sad", 1)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -15)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                            ch_k "Oh.  Well, okay, I guess."     
                            $ Line = "fail"                      
                    "What'd you have in mind?":
                            $ K_Eyes = "side"
                            ch_k "I dunno. I was thinking[K_like]maybe I could start calling you. . . {i}master{/i}?"
                            $ K_Eyes = "squint"
                            ch_k "Would you like that?  I think that'd be kinda[K_like]hot."
                            menu:
                                extend ""
                                "Oh, yeah.  I'd like that.":
                                        ch_k "Cool. . ."
                                "Uhm. . .nah.  That's too much.":
                                        call KittyFace("sad", 1)
                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -15)
                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                        ch_k "Oh.  Well, okay, I guess."
                                        $ Line = "fail"

                    "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                            call KittyFace("sly", 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 15)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -10)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 10)
                            ch_k "Aw, I guess I can't get mad about that. . ."
                            $ Line = "fail"
                            
                    "Actually, let's stop that. It's creeping me out.":
                            call KittyFace("perplexed", 2)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -50)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -15)
                            ch_k "Oh.  Sorry.  I guess I got[K_like]carried away with it."
                            $ K_Blush = 1
                            $ Line = "embarrassed"
                            
        "As if I care what you think, slut.":
                call KittyFace("sad", 1)
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20)
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -10)
                menu:
                    extend ""
                    "Sorry. I just don't care what you want.":
                            if ApprovalCheck("Kitty", 1400, "LO"): 
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                                    ch_k "That's so. . ." 
                                    call KittyFace("sly", 1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 20)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 15)
                                    ch_k ". . .{i}mean!{/i}" 
                            else:
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -15)
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -10)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                                    call KittyFace("angry", 1)
                                    ch_k "!!!"
                                    $ Line = "rude"

                    "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 10)
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 10)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)
                            ch_k "Oh, okay.  Just. . .try not to be so[K_like]mean about it, 'kay?" 

        "Not me.  It's kind of creepy.":
                    call KittyFace("sad", 2)
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, -20)
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -25)
                    ch_k "Oh.  Uhm. . .never mind, then."
                    $ Line = "embarrassed"
    
    $ K_History.append("master")
    if Line == "rude":
            $ K_RecentActions.append("angry")
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl("Kitty")
            $ renpy.pop_call()
            "Kitty phases through the floor in a huff.  She might have been crying."
    elif Line == "embarrassed":    
            hide Kitty_Sprite with easeoutbottom                     
            call Remove_Girl("Kitty")
            $ renpy.pop_call()
            "Kitty phases through the floor, leaving you alone.  She looked really embarrassed."
    elif Line != "fail":
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 200, 50)
            $ K_Petnames.append("master")
            $ K_Petname = "master"
            ch_k ". . .master."
    return

# end Kitty_Master//////////////////////////////////////////////////////////


# start Kitty_Sexfriend//////////////////////////////////////////////////////////

label Kitty_Sexfriend:  
    $ K_Loc = bg_current
    call Set_The_Scene(0)
    call Display_Kitty
    call CleartheRoom("Kitty")
    $ K_DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call KittyFace("bemused", 1)
    ch_k "So, [K_Petname]. . .you[K_like]got a second?" #blushing expression
    menu:
            extend ""
            "Not really.":
                call KittyFace("angry", 1)
                ch_k "You're such a jerk, [Playername]!" #Angry expression.  Loss of points                
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20) 
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 3)           
                $ Line = "rude"

            "This doesn't sound good.":
                call KittyFace("perplexed", 1)
                ch_k "I promise.  It's nothing[K_like]bad." 
                    
            "Yeah.  What's up?":
                pass
                
    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck("Kitty", 850, "L"):                  
                    call KittyFace("bemused", 1)
                    ch_k "Well. . . I really like you.  You know that, right?" #Sexy expression.  This is Kitty's "High Like" response
                    menu:
                        extend ""
                        "I was kinda hoping.":
                            call KittyFace("sexy", 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 10) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5)    
                            ch_k "I was {i}really{/i} hoping you'd say that [K_Petname]." #Blushing expression
                
                        "Really?":
                            ch_k "Uhm. . . [K_like]yeah.  I really do." #Blushing expression

                        "Ugh.  Gross":
                            call KittyFace("angry", 1)
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -5)   
                            ch_k "Y'know, you're such an ass, [Playername]!" #Angry expression.  Big loss of points
                            $ Line = "rude"
                            
            elif ApprovalCheck("Kitty", 1000, "LI"): 
                    call KittyFace("sexy", 1)
                    ch_k "I just wanted to tell you. . .I think you're[K_like]kinda cute." 
                    menu:
                        extend ""
                        "That's really nice of you to say.":
                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 5) 
                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5)   
                            ch_k "Well, I really mean it." #Blushing expression

                        "Me?  You really think so?":
                            ch_k "Yeah.  I {i}really{/i} do." #Blushing expression
                
                        "Are you going somewhere with this?":
                            call KittyFace("angry")
                            ch_k "Well not anymore, I'm not!" #Angry expression.  Loss of points
                            $ Line = "rude"
                            
            else: #if it reaches this block, it's because it failed the "like" check above.                    
                    $ K_Mouth = "smile"
                    $ K_Brows = "sad"
                    $ K_Eyes = "side"
                    ch_k "This is gonna sound[K_like]really weird."
                    menu:
                        extend ""
                        "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                            ch_k "Promise you won't think[K_like]{i}badly{/i}of me?"  #Nervous expression
                            menu:
                                extend ""
                                "Kitty. . . I really like you.  I promise.":
                                    call KittyFace("smile")
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 10) 
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 5)    
                                    ch_k "Well. . . okay."  #Blushing expression.  Gain of points.

                                "Uhm. . . okay?":
                                    ch_k "Well. .  ." #Nervous expression

                                "No promises.":
                                    call KittyFace("perplexed",2)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -5)  
                                    ch_k "Uhm. . . never mind, then."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                            call KittyFace("angry",1)
                            ch_k "Fine. [K_Like]whatever."
                            $ Line = "rude"
                                
    if not Line: #again, if the Line has been changed to "rude" or "embarrassed" then it skips past here.                          
            ch_k "Anyway. . . I was[K_like]kinda thinking. . . we get along pretty well, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call KittyFace("perplexed",2)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -10)  
                        ch_k "Sorry.  I knew this was a mistake." #Embarrassed expression.  Minor loss of points
                        $ Line = "embarrassed"
                    
    if not Line:                
            ch_k "And we've[K_like]known each other for a little while, right?"
            menu:
                extend ""
                "Right. . . ":
                        pass
                "Okay.  Just stop.  You're creeping me out.":
                        call KittyFace("perplexed",2)
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -10)  
                        ch_k "Sorry.  I knew this was a mistake." 
                        $ Line = "embarrassed"
    if not Line:            
            ch_k "Well. . . I was just kinda thinking. . . [K_like]we could take our relationship a little further, if you wanted to."
            menu:
                extend ""
                "You mean. . . like, being {i}friends with benefits{/i}?":
                        ch_k "Kinda, yeah.  Whaddya think?" #Blushing expression
                        menu:
                            extend ""
                            "Sounds amazing!  Count me in.":
                                    call KittyFace("smile",1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 80, 10) 
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 200, 50)             
                                    $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 200, 5) 
                                    "Kitty leans in and gives you a gentle kiss on the cheek."
                                    ch_k "I can't wait to get started, [K_Petname]."

                            "That may be the sluttiest thing I've ever heard in my life.":
                                    call KittyFace("angry",1)
                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -30) 
                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 10)
                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -40)  
                                    ch_k "You're the biggest asshole[K_like]ever, [K_Petname]!" #Angry expression.  HUGE loss of points
                                    $ Line = "rude"

                "Uhm, to be honest, I'd rather not.":
                        call KittyFace("sadside",2)
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 15)
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -15)  
                        ch_k "Oh.  Okay."  #Sad expression
                        ch_k "I[K_like]think I should go now.  I've got[K_like]stuff to do."
                        $ Line = "sad"

    if Line == "rude":    
            call KittyFace("angry",1)
            $ K_RecentActions.append("angry")
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20) 
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -10) 
            hide Kitty_Sprite with easeoutleft   
            $ K_RecentActions.append("angry")
            "Kitty storms off in a huff.  She seemed pretty mad at you."
    elif Line == "embarrassed":
            call KittyFace("perplexed",1)
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 50, 5)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, -20)   
            hide Kitty_Sprite with easeoutbottom
            "Kitty phases through the floor leaving you alone.  That was very strange."
    elif Line == "sad":    
            hide Kitty_Sprite with easeoutbottom
            "Kitty phases through the floor leaving you alone.  You think you may have hurt her feelings."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ K_Petnames.append("sex friend")             
            call KittyFace("sly",2)
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 10)             
            $ K_Lust = Statupdate("Kitty", "Lust", K_Lust, 80, 10)   
            "Kitty leans in and passes her hand across body."
            "As she does so, she phases her hand through your jeans, so her fingers slide along your bare skin."
            $ K_Blush = 1
            ch_k "I'll definitely be seeing {i}you{/i} later, [K_Petname]."  
            hide Kitty_Sprite with easeoutright
            "She passes through a nearby wall. "            
    call Remove_Girl("Kitty")
    return
    
# end Kitty_Sexfriend//////////////////////////////////////////////////////////


# start Kitty_Fuckbuddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Fuckbuddy:  
    $ K_DailyActions.append("relationship")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear,"
    ch_k "Any time, just let me know. . ."
    "-and suddenly the pressure is gone." 
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on Kitty later. . ."
    $ K_Petnames.append("fuck buddy")  
    $ K_Event[10] += 1
    return
# end Kitty_Fuckbuddy//////////////////////////////////////////////////////////

# start Kitty_Daddy//////////////////////////////////////////////////////////

#Not updated

label Kitty_Daddy:      
    $ K_DailyActions.append("relationship")
    call Shift_Focus("Kitty")
    ch_k ". . ."
    if "dating" in K_Traits:
        ch_k "You know, even though we've been dating,"  
    else:    
        ch_k "Even though we've been hanging out," 
    if K_Love > K_Obed and K_Love > K_Inbt:
        ch_k "and you're really sweet to me. . ."
    elif K_Obed > K_Inbt:
        ch_k "and you know what I need. . ."
    else:
        ch_k "and I've really been spreading my wings. . ."        
    ch_k "So I was thinking, could I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
            call KittyFace("smile") 
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 20)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 10)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 30) 
            ch_k "Squee!"            
        "What do you mean by that?": 
            call KittyFace("bemused") 
            ch_k "I just sort of get turned on by it, you know, being your baby girl. . ."
            ch_k "I'd like to call you that."
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                    call KittyFace("smile") 
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 15)          
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 60, 20)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 25) 
                    ch_k "Great! . . daddy."  
                "Could you not, please?":             
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5)
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 40)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 20)  
                    call KittyFace("sad") 
                    ch_k "   . . .   "
                    ch_k "Well, ok."
                "No, that creeps me out.":    
                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -10)          
                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 45)            
                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 5)  
                    call KittyFace("angry") 
                    ch_k "Hrmph." 
        "No, that creeps me out.":
            $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, -5)          
            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 40)            
            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 70, 10) 
            call KittyFace("angry") 
            ch_k "Hrmph."  
    $ K_Petnames.append("daddy")
    return

# end Kitty_Daddy//////////////////////////////////////////////////////////

# Start KittyBreakup //////////////////////////////////////////////////////////  

label Kitty_Cheated(Other = "Rogue", Resolution = 0, B = 0):  #Other is the other girl, Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
    #Scene for if Kitty catches you with Rogue and confronts you about it. 
    $ K_DailyActions.append("relationship")
    $ Line = 0
    call KittyFace("angry")
    
    if Other == "Rogue":
        if K_LikeRogue >= 900:
            $ Resolution += 2
        elif K_LikeRogue >= 800:
            $ Resolution += 1
        $ B = int((K_LikeRogue - 500)/2)
    
    $ Resolution -= K_Cheated if K_Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
    
    if K_Cheated:
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -50) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, -25)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -50)   
    else:
        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -120) 
        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, -30)
        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, -20)  
        
    "Kitty stomps up to you and stares you down for a moment."
    ch_k "Well?!" 
    ch_k "Wanna tell me what that was all about?"
    menu:
        extend ""
        "Uhm. . .sorry?":
                ch_k "Is that {i}really{/i} all you have to say for yourself?"
                ch_p "I don't know? It would kinda help if I knew what you were upset about."
                if ApprovalCheck("Kitty", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Line = "angry"
        "I have no idea what you're talking about.":
                ch_k "I can't believe you just said that. I gave you[K_like]a lot more credit than that."
                ch_p "[K_Pet], I'm being serious. Why're you so upset?"
                if ApprovalCheck("Kitty", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Resolution -= 2
                    $ Line = "angry"
        "Could you chill out and tell me what you mean?":
                call KittyFace("sad",2)                
                $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 40, 5, 1) 
                ch_k "I didn't like what happened already. How much[K_like]worse can it get?"
                ch_p "You'd better start making some sense, or you're gonna find out."
                if ApprovalCheck("Kitty", 500, "O"):
                    $ Resolution += 1  
                elif ApprovalCheck("Kitty", 1200, "LO"):
                    $ Resolution -= 1    
                else:
                    $ Resolution -= 3
                    $ Line = "angry"
                    
    if not Line:
            #this section only triggers if you didn't trigger the "angry" response in the previous section
            call KittyFace("angry",2)
            if Other == "Rogue":
                ch_k "I {i}saw{/i} you and Rogue! I can't[K_like]believe you'd do that, [K_Petname]."
            else:
                ch_k "I {i}saw{/i} you with her! I can't[K_like]believe you'd do that, [K_Petname]."
            ch_k "I thought we had something. . . [K_like]{i}special{/i} going on."
            menu:
                extend ""
                "I'm sorry. . . ":
                        $ Resolution += 1                        
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 90, 5) 
                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)  
                        if not ApprovalCheck("Kitty", 900, "L"):
                                #if love is less than 900
                                $ Line = "sad"
                        else:
                                call KittyFace("sad")
                                ch_k "Me too. I thought you. . . "
                                call KittyFace("sadside")
                                ch_k ". . . I thought you maybe loved me."
                                menu:
                                    extend ""
                                    "You weren't wrong, [K_Pet].":
                                            $ Resolution += 1                                            
                                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 5) 
                                            $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)   
                                            call KittyFace("embarrassed")
                                            ch_k "[K_Like]. . . really?"
                                            menu:
                                                extend ""
                                                "[K_Like]really.":
                                                        call KittyFace("embarrassed")
                                                        if Other == "Rogue":
                                                            ch_k "Then. . .[K_like]why did you do that with {i}Rogue?{/i} You had to know that would[K_like]hurt me."
                                                        else:
                                                            ch_k "Then. . .[K_like]why did you do that with {i}her?{/i} You had to know that would[K_like]hurt me."                                                        
                                                        menu:
                                                            extend ""
                                                            "It was a mistake. And I promise I'll never do it again.":
                                                                    $ Resolution += 2                                                                    
                                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, 5)
                                                                    $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)   
                                                                    call KittyFace("happy",2)
                                                                    ch_k "Okay. I understand. Just. . .[K_like]remember how much I care about you, 'kay?"
                                                                    ch_k "I can forgive you[K_like]this time."
                                                                    ch_k "Because I'm[K_like]in love with you, too."
                                                                    call K_Kissing_Launch("kissing")
                                                                    call K_Pos_Reset
                                                            "I was trying to maybe include her in what we have going.":
                                                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                                                    $ Line = "maybe"
                                                            "I don't know, seemed fun at the time.":
                                                                    $ Resolution -= 1
                                                                    $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                                                                    $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, -5)
                                                                    $ Line = "angry"          
                                                "Had you going, there, didn't I? {i}Hell{/i}, no, I don't!":
                                                        $ Resolution -= 3
                                                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -20) 
                                                        $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)
                                                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)   
                                                        $ Line = "angry"                                                                   
                                    "Yeah, well. .  . I don't.":
                                            $ Resolution -= 1
                                            $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                                            $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 5)   
                                            $ Line = "sad"  
                        #end "sorry."
                "Whatever.":
                        $ K_Love = Statupdate("Kitty", "Love", K_Love, 200, -10) 
                        $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 50, 5)   
                        if ApprovalCheck("Kitty", 900, "L") and not ApprovalCheck("Kitty", 500, "O"):
                                $ Resolution -= 2
                                $ Line = "angry"
                        else:
                                $ K_Obed = Statupdate("Kitty", "Obed", K_Obed, 80, 10) 
                                $ Resolution -= 1
                                $ Line = "sad"
                "We do. And now, it can be even {b}more{/b} special.":
                                $ Resolution += 1
                                $ Line = "maybe"
            #end "questioning", for long blocks like this, it helps to put a comment at the end to explain what was going on, so I don't get lost. ;)
            
    if Line == "maybe":
            # Maybe threesome?            
            if ApprovalCheck("Kitty", 1250):
                    call KittyFace("confused")
                    ch_k "What're you even[K_like]{i}talking{/i} about?"
                    if Other == "Rogue":
                        ch_p "Look. . .be totally honest with me for a second. Rogue's your best friend, right?"
                    else:
                        ch_p "Look. . .be totally honest with me for a second. She's kinda hot, right?"
                    ch_k "Yeah. . ."
                    ch_p "Right. And when you saw us together. . . you have to admit, you thought it was pretty hot on some level, right?"
                    call KittyFace("angry")
                    ch_k "No. It pissed me off is what it did."
                    ch_p "C'mon, [K_Pet]. Haven't you ever thought about it?"
                    call KittyFace("confused")
                    ch_k "Thought about what?"
                    if Other == "Rogue":
                        ch_p "Thought about what it might be like if we invited Rogue into what we have together."
                    else:
                        ch_p "Thought about what it might be like if we invited her into what we have together."                    
                    if ApprovalCheck("Kitty", 1500) and Resolution >= 3:
                            call KittyFace("embarrassed")
                            ch_k "You mean[K_like]. . .a {i}threesome{/i}?"
                            call KittyFace("sly")
                            ch_k "I can't believe I'm saying this but. . . I'm[K_like]vaguely intrigued."
                            if Other == "Rogue":
                                ch_k "Assuming I'm interested. . . how're you going to convince Rogue?"
                            else:
                                ch_k "Assuming I'm interested. . . how're you going to convince her?"
                            ch_p "If you see us together again, just play it cool."
                            ch_p "Make sure she notices that you're watching us, but don't give her the impression it puts you off."
                            call KittyFace("sly",1)
                            ch_k ". . . which should[K_like]make her wonder what's up."
                            ch_p "Right. Eventually, she'll ask me what our arrangement is."
                            ch_k "By then, with any luck, she'll be comfortable enough with me that I can ask her how she feels about it."
                            call KittyFace("sly",2)
                            ch_k "Gotta admit, [K_Petname]. . . you're pretty smooth."
                            ch_k "Consider me[K_like]on board with that plan."
                            ch_k "Just be sure to be careful with her. She's still my friend."
                            #have Kitty kiss the Player here.
                            ch_k "And remember, you're still {i}my{/i} guy."                            
                            $ K_Traits.append("poly rogue")
                            $ K_Traits.append("ask rogue")
                            $ Line = 0
            if Line:
                    #this section will only trigger if the "maybe" line above triggered BUT both of the stat checks above failed. 
                    #If you don't even ask about a threesome then this check gets skipped, and if you ask, but succeed both checks,
                    #then this section gets skipped. 
                    call KittyFace("angry")
                    if Other == "Rogue":
                        ch_k "So, you're telling me[K_like]you being with Rogue like that was your way of seeing if I'd be up for a threesome?"
                    else:
                        ch_k "So, you're telling me[K_like]you being with her like that was your way of seeing if I'd be up for a threesome?"
                    ch_p "Pretty much. I. . .take it you're not down with that?"
                    $ Line = "angry"
            # End "maybe threesome?"
    
    elif Resolution >= 4:
        if Other == "Rogue" and K_LikeRogue >= 800:
                $ K_Inbt = Statupdate("Kitty", "Inbt", K_Inbt, 80, 25)   
                ch_k "Well, maybe Rogue and I can work something out. . ."                            
                $ K_Traits.append("poly rogue")
                $ K_Traits.append("ask rogue")                
        
    $ K_Cheated += 1
    if "saw with rogue" in K_Traits: 
            #Clean up the trait for this event
            $ K_Traits.remove("saw with rogue")
            if "poly rogue" not in K_Traits:
                $ K_LikeRogue -= 50
            
    if not Line:
            #a neutral ending if you wrap things up without really effecting much
            pass                
    elif Line == "angry":
            #Angry ending
            call KittyFace("angry",2)
            ch_k "You are {b}SUCH{/b} an asshole, [K_Petname]!"
            ch_k "I never wanna see you again, as long as I live!"
            "Kitty phases through the floor leaving you standing alone."
            "Whatever you once had is over now, for sure."     
            $ K_RecentActions.append("angry")
            $ K_Break[0] = 7 + K_Break[1] + K_Cheated
            $ K_Traits.remove("dating")
            $ K_Traits.append("ex")         
    elif Line == "sad":
            # Sad ending
            call KittyFace("sad",2)
            "Kitty phases through the floor leaving you standing alone."
            "You're pretty sure she was crying as she left."
            "You're also pretty sure you seriously damaged your relationship with her."
            if Resolution <= 3:
                $ K_Break[0] = 5 + K_Break[1] + K_Cheated
                $ K_Traits.remove("dating")
                $ K_Traits.append("ex")                
    return

# end KittyBreakup //////////////////////////////////////////////////////////    

# ch_r, Rogue, rogue, R_

    
        
        

#label Kitty_Sub_SecondChance:
#    $ Line = 0
#    ch_k "So, [K_Petname], I was remembering. . .[K_like]how much I liked the way things used to be.  Y'know[K_like]when you were really in control in our relationship.  I miss that."
#    ch_k "The way it ended. . .kinda hurt my feelings.  But I was thinking, maybe, we could try that again?  Whaddya think?"
#    menu:
#        extend ""
#        "I think you should learn how to take a hint.":
#                ch_k "You could've just[K_like]said {i}no{/i}.  But instead, you had to be a jerk!" #Angry expression.  Big loss of points
#                "Kitty phases through the floor, leaving you alone.  She looked super pissed off!"
#                $ Line = "rude"

#        "Yeah, I suppose we could see how it works out.":
#                ch_k "Awesome.  I was hoping you'd say that." #Blushing expression and sir petname opened again
#                ch_k "Y'know, though. . .you were[K_like]really mean about it before.  Maybe there's something you should say?"
#                menu:
#                    extend ""
#                    "You're right.  I was out of line before and I'm sorry I was a jerk.":
#                            ch_k "It's okay.  It takes guts to say that.  I totally[K_like]accept your apology."  #this ends sequence
#                            $ Line = 0
                            
#                    "Not exactly.  You told me I should be more in control.  So I was.  You just took it all wrong.":
#                            ch_k "Oh!  I, uhm. . .maybe I should be the one saying they're[K_like]sorry?" #Blushing expression
#                            menu:
#                                extend ""
#                                "Yeah, I think you should.":
#                                    ch_k "I'm really[K_like]sorry.  Like you said, I wanted you to be more in control.  I guess I should[K_like]expect you to be that way, huh?" #Sad expression
#                                    menu:
#                                        extend ""
#                                        "It's cool, [K_Pet].  I understand.":
#                                                ch_k "You're[K_like]amazing, [K_Petname]" #Sexy expression leading to Kitty giving Player a kiss
#                                        "Uncool, [K_Pet].":
#                                                "Kitty phases through the floor, leaving you by yourself.  She looked totally embarrassed."
#                                                $ Line = "embarrassed"

#                                "Naah, it's cool.  I understand.":
#                                        ch_k "You're[K_like]amazing, [K_Petname]" #Sexy expression leading to Kitty giving Player a kiss #I'm unsure here what code to use here to transition to a new scene.  Also I'm not sure how to "call back" to the place in this scene where I used this same response before

#                                "To tell you the truth, it kind of pissed me off.":
#                                        "I'm really sorry, [K_Petname].  I would never[K_like]do anything to hurt you."
#                                        "Kitty phases through the floor, leaving you by yourself.  She looked totally embarrassed." #See my earlier note about "calling back"
#                                        $ Line = "embarrassed"

#                    "You're right. . .there is.  How about:  {i}Fuck you, I'm not apologizing for shit{/i}?":
#                            ch_k "You're[K_like]the biggest asshole ever!" #Angry expression.  Super-big loss of points
#                            "Kitty phases through the floor, leaving you alone.  She looked super pissed off!"
#                            $ Line = "rude"


#    return


#label Combine_BroachThreesome1:
#	$ Line = 0
#        if R_LikeKitty >= 850 and K_LikeRogue >= 850:
#                #Kitty and Rogue Approach Player Wanting Approval Section
#                call RogueFace("manic",1)
#                call KittyFace("sly")
#                "Both Rogue and Kitty approach you. It's clear from their expressions that they have something important to say to you."
#                "Though Kitty seems at ease, Rogue looks nervous. Even though it's obvious you're alone, she looks around to make sure of it."
#                ch_r "Uhm. . .Kitten, how about you do most of the talking, here? You always seem to know just what to say."
#                menu:
#                        extend ""
#                        "I'm not gonna like this, am I?":
#                                call KittyFace("bemused")
#                                ch_k "Relax, [K_Petname]. This is[K_like]totally a good thing."
#                                pass
#                        "If this is more drama, I really don't have time for it.":
#                                $ Line = "ScrewedThePooch1"
            
#                if not Line:
#                        call KittyFace("sly",1)
#                        ch_k "So . . . Rogue and I were[K_like]talking the other night, right?"
#                        call KittyFace("sly",2)
#                        ch_k "We were talking about how we both like you."
#                        call RogueFace("sly",2)
#                        ch_r "{i}Really{/i} like you."
#                        call KittyFace("smile",1)
#                        ch_k "[K_Like]{i}really{/i} really like you."
#                        "The two girls laugh between each other for a moment before composing themselves again."
#                        call KittyFace("sly")
#                        ch_k "Anyway . . . ever since Rogue came to the Mansion, we've been[K_like]total besties."
#                        ch_k "We basically do[K_like]just about everything together."
#                        ch_k "There's basically nobody in the world I feel more comfortable around."
#                        call RogueFace("smile",1)
#                        ch_r "And I feel exactly the same way about Kitty."
#                        call KittyFace("smile",1)
#                        ch_k "So, like I said, we were talking . . . and we started talking about how we both have[K_like]something going on with you."
#                        ch_k "I told Rogue how happy you made me."
#                        ch_r "And I said almost exactly the same thing about you, [R_Petname]."
#                        call KittyFace("down")
#                        ch_k "And we basically came to the conclusion that[K_like]for one of us, it was gonna have to end."
#                        ch_k "And, even though we're really close, neither of us wanted to give you up. Even[K_like]for our bestie."
#                        call RogueFace("sly",2)
#                        ch_r "So . . . Kitty came up with this crazy idea."
#                        call KittyFace("startled")
#                        ch_k "Huh?"
#                        call KittyFace("smile",1)
#                        ch_k "We[K_like]{b}both{/b} came up with it."
#                        ch_k "Anyway, I'll spare you the[K_like]girl talk, but we had a long discussion about the whole thing."
#                        ch_k "When we were done, we both admitted that[K_like]the only person either of us were attracted to as much as you was . . ."
#                        "Kitty looks over at Rogue, waiting for her to finish her sentence."
#                        call RogueFace("sly",2)
#                        ch_r " . . . Was each other."
#                        call KittyFace("smile",2)
#                        ch_k "So[K_like]we talked it over and decided that, if you were cool with it, we {i}both{/i} want you."
#                        ch_r ". . . At the same time."
#                        menu:
#                                extend ""
#                                "You mean, like, a threesome?":
#                                        call RogueFace("sly",2)
#                                        call KittyFace("sly",1)
#                                        ch_k "Basically . . . yeah."
#                                        "Kitty shrugs slightly."
#                                        ch_k "We're both a little . . . {i}curious{/i}. It's[K_like]a great compromise. So we'd like to see how it would work out."
#                                        call RogueFace("surprised")
#                                        ch_r "We're not, like, lezzies or anything."
#                                        call RogueFace("sly",2)
#                                        ch_r "We're just . . . close. And comfortable. And we think this could be amazing, if it works out."
#                                        call RogueFace ("confused")
#                                        ch_r "What do {i}you{/i} think? This we could maybe try it?"
#                                        menu:
#                                                extend ""
#                                                "I think that sounds amazing! Let's do it!":
#                                                        call RogueFace("smile")
#                                                        call KittyFace("smile")
#                                                        "Both girls look like they could walk on air."
#                                                        "(In Kitty's case, she actually {i}{b}is{/b}{/i})"
#                                                        #Both girls kiss the Player
#                                                        call KittyFace("sly",1)
#                                                        "Kitty looks at Rogue and smirks."
#                                                        ch_k "See? Toldja he'd be[K_like]totally cool with it."
#                                                        call RogueFace("smile",1)
#                                                        ch_r "You were right. I should have doubted {i}either{/i} of you."
#                                                        $ Line = "ItsAMagicNumber1"
#                                                "That sounds really . . . {i}awkward{/i}. I don't think so.":
#                                                        $ Line = "Threejected1"
#                                "You said all that just to tell me you're lesbians?":
#                                        $ Line = "ScrewedThePooch1"
                                    
#        elif R_LikeKitty >= 850 and 849 >= K_LikeRogue >= 500:
#                #Rogue Likes Kitty, Wants Player to Give Nudge Section
#                call RogueFace("sly",1)
#                call KittyFace("smile")
#                "Rogue and Kitty approach you. Both are clearly happy to see you."
#                "You notice that while Kitty looks totally at ease, Rogue has a wry grin on her face."
#                "It's not hard to tell that she has something on her mind -- something Kitty isn't privy to."
#                ch_k "Heya, [K_Petname]!"
#                "Kitty looks at Rogue and arches a curious brow."
#                ch_k "Okay, here he is. So[K_like]what's this all about now?"
#                "You have absolutely no idea what she's talking about."
#                call RogueFace("sly",2)
#                "Rogue looks around to make sure you're alone. Only when she's convinced you have some privacy does she speak."
#                ch_r "Uhm, so . . . I was telling Kitty I wanted to find you so maybe we could all have a little talk, [R_Petname]."
#                call KittyFace("perplexed")
#                ch_k "Right . . ."
#                call RogueFace("smile",1)
#                ch_r "Well, [R_Petname], you know how I told you Kitty and I were best friends, right?"
#                ch_r "Ever since I first came to the Mansion, my powers all out of control, she's stood by me."
#                ch_r "She's always been there when I needed a friend or a shoulder to cry on . . . or basically anything."
#                ch_r "Honestly . . . there's nobody in the world I feel more comfortable around."
#                call KittyFace("smile",2)
#                ch_k "Aww . . ."
#                ch_k "That's[K_like]{i}so{/i} sweet, Rogue!"
#                call KittyFace("smile")
#                ch_k "I love you, too! You're[K_like]the {i}best{/i} bestie!"
#                ch_r "Well . . . maybe I am, but [R_Petname] is the best boyfriend ever."
#                call RogueFace("sly",2)
#                ch_r "And that's why I was . . . well . . ."
#                ch_r ". . . I was hoping we could share him, Kitten."
#                call KittyFace("startled",1)
#                ch_r "C'mon, Kitty. You {i}{b}told{/b}{/i} me you thought [R_Petname] was hot."
#                ch_r "And I {i}know{/i} you check out Kitty, [R_Petname]. I've caught you doing it, now and again."
#                call KittyFace("sly",1)
#                ch_r "I just thought . . . well . . . I've always kind of been curious, Kitty."
#                ch_r "And since we all get along really well . . . I thought if we could {i}all{/i} be together, it could be really amazing."
#                call KittyFace("sly",2)
#                ch_k "Well[K_like]I dunno . . ."
#                ch_k "[K_Petname] {i}is{/i} kinda cute. And I guess we do kinda get along . . ."
#                call KittyFace("sly",1)
#                ch_k "I dunno. [K_Like]what's your thoughts on it?"
#                menu:
#                        extend ""
#                        "A threesome with the two of you? HELL, YES.":
#                                call RogueFace("smile",1)
#                                call KittyFace("sly",1)
#                                ch_k "Pretty enthusiastic about the idea, huh, [K_Petname]?"
#                                call RogueFace("perplexed")
#                                ch_r "Well, what about you, Kitten? Do . . . you want to try?"
#                                ch_k "Are you kidding me?"
#                                call KittyFace("sly",2)
#                                ch_k "You're not the only one that's been {i}kinda curious{/i}."
#                                ch_k "And I've been[K_like]checking out [K_Petname] just as much as he's been checking me out."
#                                ch_k "So, yeah. I'm[K_Like]totally in."
#                                $ Line = "ItsAMagicNumber1"
#                        "I'm not sure. I wouldn't want it to wreck what we have, [R_Pet].":
#                                call RogueFace("smile")
#                                call KittyFace("smile")
#                                ch_k "You're right, Rogue. [K_Like]best boyfriend ever."
#                                ch_k "Well . . . it'd be[K_like]different, I'm sure. But I promise, I'd never get between the two of you."
#                                call KittyFace("sly",2)
#                                ch_k "Not unless you[K_like]asked really nicely."
#                                call RogueFace("smile",1)
#                                ch_r "So . . . good enough for you, [R_Petname]?"
#                                menu:
#                                        extend ""
#                                        "Good enough for me.":
#                                                #Have Kitty and Rogue kiss the Player.
#                                                call RogueFace("smile")
#                                                call KittyFace("smile")
#                                                ch_k "I promise not to make you[K_like]regret this, [K_Petname]."
#                                                $ Line = "ItsAMagicNumber1"
#                                        "I'm sorry. I just don't want to risk it.":
#                                                $ Line = "Threejected1"
#                        "Count me out. That's just too awkward for me.":
#                                $ Line = "Threejected1"
                                
#        elif K_LikeRogue >= 850 and 849 >= R_LikeKitty >= 500:
#                #Kitty Likes Rogue, Wants Player to Give Nudge Section
#                call RogueFace("smile")
#                call KittyFace("sly",1)
#                "Rogue and Kitty approach you. Both are clearly happy to see you."
#                "You notice that while Rogue looks totally at ease, Kitty has a wry grin on her face."
#                "It's not hard to tell that she has something on her mind -- something Rogue isn't privy to."
#                ch_k "Heya, [K_Petname]! {i}Just{/i} who we've been looking for!"
#                call RogueFace("perplexed")
#                ch_r "Okay . . . he's here. Now, what's this all about, Kitty?"
#                ch_k "What this is about is[K_like]about me and [K_Petname] . . ."
#                call KittyFace("sexy",1)
#                ch_k ". . . And {i}you{/i}."
#                call RogueFace("startled")
#                ch_r "Wha -- ?"
#                call KittyFace("smile")
#                "Kitty interrupts her before she can finish the thought."
#                ch_k "[K_Petname], be[K_like]totally honest with me for a second, okay?"
#                ch_k "You think Rogue's[K_like]kinda hot, right?"
#                menu:
#                        extend ""
#                        "Of course . . . but not as hot as you.":
#                                call RogueFace("sly",1)
#                                call KittyFace("smile",1)
#                                ch_r "I can see why you keep him around, Kitten."
#                                ch_k "Yeah, he can be pretty damn adorable."
#                                call KittyFace("smile")
#                                pass
#                        "Well, yeah!":
#                                call RogueFace("sly",1)
#                                call KittyFace("smile")
#                                ch_k "I {i}thought{/i} I saw you checking her out before!"
#                                call KittyFace("sly",1)
#                                ch_k "You're[K_like]lucky that in this case -- that's a {b}good{/b} thing."
#                                pass
#                        "Uhm, to be honest . . . not so much.":
#                                call RogueFace("down")
#                                call KittyFace("down")
#                                ch_k "Oh. Well . . . that kind of shoots {i}that{/i} down, huh?"
#                                "You're not really sure what she means by that, but you get the impression a big opportunity might have just passed you by."
#                                $ Line = "Threejected1"

#            if not Line:
#                    call RogueFace("sly",1)
#                    call KittyFace("smile")
#                    ch_k "Anyway, we've established that[K_like]you think Rogue's pretty hot."
#                    call KittyFace("sly",1)
#                    ch_k "Well . . . you're not the {i}{b}only{/b}{/i} one."
#                    call RogueFace("startled")
#                    ch_k "C'mon, Rogue . . . we're besties, right?"
#                    ch_k "We've been through so much together."
#                    ch_k "And you're absolutely {i}gorgeous{/i}."
#                    ch_k "I'm not going to lie: I'm kinda . . . {i}curious{/i} about you."
#                    ch_k "And I'm lucky enough to have[K_like]the best boyfriend in the world."
#                    ch_k "[K_Petname], so . . . would you be cool with bringing Rogue into what we have?"
#                    ch_k "I mean, I'm totally in love with you. But I think this might even make it better."
#                    ch_k "What d'you think?"
#                    menu:
#                            extend ""
#                            "I'm down . . . but shouldn't we ask Rogue, first?":
#                                    pass
#                            "I'm not sure. I wouldn't want it to wreck what we have, [K_Pet].":
#                                    ch_k "It's[K_like]totally sweet of you to think that way . . . but I think this could only be a good thing -- if we give it a chance."
#                                    ch_k "Are you[K_like]willing to give it a try?"
#                                    menu:
#                                            extend ""
#                                            "If you're sure . . .":
#                                                    call KittyFace("smile")
#                                                    ch_k "I'm sure."
#                                                    pass
#                                            "No. I'm sorry. This is too . . . odd for me.":
#                                                    $ Line = "Threejected1"
#                            "That's just . . . ugh.  No.  No way.":
#                                    $ Line = "Threejected1"
                                    
#        if not Line:
#                ch_k "Rogue? What d'you think? You're always telling me how cute you think [K_Petname] is."
#                call RogueFace("sly",2)
#                ch_r "Well . . . yeah.  That's true, I guess."
#                ch_k "And you know how happy he makes me. You could have a chance at that, too!"
#                "Rogue seems to think about it for a moment, biting her lower lip."
#                "Finally, she takes a deep breath and lets in out in a sigh."
#                ch_r "If y'all don't think I'd get in the way . . . yeah. I'd . . . I'd love to be a part of it."
#                call KittyFace("smile",2)
#                ch_k "So it's settled! We're not a couple anymore! We're[K_like]a trio!"
#                $ Line = "ItsAMagicNumber1"
        
#        else:
#                #Girls Giggle Implication Section
#                call RogueFace("sly",1)
#                call KittyFace("sly",1)
#                "Both Rogue and Kitty approach you. The two of them are whispering between one other as they do."
#                "Once they're within clear earshot, they stop their conversation abruptly."
#                "You have a feeling that you're definitely the subject of the conversation."
#                "You also have a feeling that, whatever they're talking about, they're not going to let you in on it."
#                "It's definitely something for you to file away in your memory."

#	elif Line == "ScrewedThePooch1":
#		call RogueFace("smile")
#		call KittyFace("smile")
#		"Both girls look absolutely furious with your response."
#		"Neither one of them says anything as they turn and storm away from you."
#		"You think you might have heard them mutter something between each other, but they're too far gone to hear exactly what it was."
#		"Given their reaction, you can only imagine."
#		#Major loss of Love & Lust points from both girls

#	elif Line == "ItsAMagicNumber1":
#		call RogueFace("smile")
#		call KittyFace("smile")
#		"Both girls seem really happy with the way things worked out."
#		"For your part, you have a good feeling about the whole arrangement."
#		"In any case . . . it seems like coming to the Institute was the best thing that ever happened to you!"
#		#Major gain of Love & Lust points from both girls

#	elif Line == "Threejected1":
#		call RogueFace("down")
#		call KittyFace("down")
#		"Both girls seem pretty disappointed by your response."
#		ch_k "I guess it was[K_like]too much to ask for, huh?"
#		ch_r "I'm really sorry we made things . . . {i}weird{/i} for you, [R_Petname]."
#		ch_k "Maybe we can just[K_like]forget it ever happened, huh?"
#		"The three of you just kind of stand there in awkward silence until, at last, both girls sort of slink away."
#		"{i}Weird{/i}.  That was about the perfect word for it."
#		#Minor loss of Love & Lust points from both girls
#        return

image CircleTest: 
    contains:
        subpixel True
        "images/Clockbase.png"   
        anchor (0.5,0.5)
#        rotate 180
        yzoom -1
        
    contains:
         ConditionSwitch(
            "Round>= 50", "ClockWhite", 
            "True",Null(),
            ),  
    contains:
         ConditionSwitch(
            "Round<= 50", "ClockRed", 
            "True",Null(),
            ),  
    contains:
        subpixel True
        "images/Clockface.png" 
        anchor (0.5,0.5) 
    
image ClockWhite:
    contains:
        subpixel True
        "images/Clockwhite.png"  
        anchor (0.5,0.5)
        rotate -(int(Round *3.6))
    
image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"  
        anchor (0.5,0.5)
        rotate -(int(Round *3.6-180))
        
        
        
#        zoom .6
#        pos (220,640)#(220,635)
#        anchor (0.5,0.5)
#        alpha 0.5
#        rotate 200
#        block:
#            choice: #fast rub
#                ease .75 rotate 210 pos (220,645)
#                ease .5 rotate 195 
#                ease .75 rotate 210 
#                ease .5 rotate 195 
#            choice: #slow rub
#                ease .5 rotate 210 pos (220,645)
#                ease 1 rotate 195
#                pause .25
#                ease .5 rotate 210
#                ease 1 rotate 195
#                pause .25
#            choice: #slow stroke
#                ease .5 rotate 205 pos (220,655)
#                ease .75 rotate 200 pos (220,660)
#                ease .5 rotate 205 pos (220,655)
#                ease .75 rotate 200 pos (220,660)
#            choice: #Fast stroke
#                ease .3 rotate 205 pos (220,655)
#                ease .3 rotate 200 pos (220,665)
#                ease .3 rotate 205 pos (220,655)
#                ease .3 rotate 200 pos (220,665)
           # repeat