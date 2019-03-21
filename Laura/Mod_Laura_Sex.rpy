# Laura_SexMenu //////////////////////////////////////////////////////////////////////
label Laura_SexAct(Act = 0):    
    call Shift_Focus("Laura")    
    if Act == "SkipTo":
        $ renpy.pop_call() #causes it to skip past the Trigger Swap
        $ renpy.pop_call() #causes it to skip past the cycle you were in before
        $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
        call SkipTo("Laura")
    elif Act == "switch":
        $ renpy.pop_call() #causes it to skip past call here from Sex_Menu_Threesome
        $ renpy.pop_call() #causes it to skip past call to Sex_Menu_Threesome
        # drops through to sex menu
    elif Act == "masturbate":         
        call LM_Prep
        if not Situation:
            return    
    elif Act == "lesbian":         
        call Laura_Les_Prep
        if not Situation:
            return       
    elif Act == "morningwood":
        # This action is called for by the label Laura_Morning and returns to there
        $ newgirl["Laura"].RecentActions.append("blow")           
        $ newgirl["Laura"].DailyActions.append("blow")                          
        $ newgirl["Laura"].DailyActions.append("morningwood")  
        call Sleepover_MorningWood
#        call Laura_MorningWood
        if Situation == "blow": 
            #If you selected to continue the BJ, then it calls the BJ actions
            $ Situation = 0
            call Laura_BJ_Prep
        $ Trigger4 = 0
        call Morning_Partner
        if not Situation:
            return
    elif Act == "kissing":        
        call Laura_KissPrep
        if not Situation:
            return   
    elif Act == "breasts":        
        call Laura_Fondle_Breasts
        if not Situation:
            return  
    elif Act == "blow":        
        call Laura_BJ_Prep
        if not Situation:
            return  
    elif Act == "hand":        
        call Laura_HJ_Prep
        if not Situation:
            return   
    elif Act == "sex":        
        call Laura_SexPrep
        if not Situation:
            return   

label Laura_SexMenu:     
    call Shift_Focus("Laura")
    $ Trigger = 0    
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Situation = 0
    call Laura_Hide    
    $ newgirl["Laura"].Arms = 1
    call Set_The_Scene(1,0,0,0,1)
    if not P_Semen:
        "You're a little out of juice at the moment, you might want to wait a bit." 
    if P_Focus >= 95:
        "You're practically buzzing, the slightest breeze could set you off."
    if not newgirl["Laura"].Action:
        "Laura's looking a bit tired out, maybe let her rest a bit."
    
    if "caught" in newgirl["Laura"].RecentActions or "angry" in newgirl["Laura"].RecentActions:  
        ch_l "You really don't want to try me right now."
        call LauraOutfit        
        call DrainWord("Laura","caught",1,0)
        return
        
    if Round < 5:
        ch_l "You're looking a bit worn out, maybe take a break."   
        return
    menu Laura_SMenu:  
        ch_l "What did you want to do?"
        "Do you want to make out?":
            if newgirl["Laura"].Action:
                call Laura_Makeout
            else:
                ch_l "Maybe in a minute, I need a break." 
        
        "Could I touch you?":
                if newgirl["Laura"].Action:
                    $ newgirl["Laura"].Mouth = "smile"                    
                    menu:
                        ch_l "Yeah? Like where?"                      
                        "Could I give you a massage?":
                                call Laura_Massage                        
                        "Your breasts?":
                                call Laura_Fondle_Breasts
                        "Your thighs?":
                                call Laura_Fondle_Thighs
                        "Your pussy?":
                                call Laura_Fondle_Pussy
                        "Your Ass?":
                                call Laura_Fondle_Ass
                        "Never mind [[something else]":
                                jump Laura_SMenu
                else:
                    ch_l "Maybe in a minute, I need a break."
                    
        "Could you take care of something for me? [[Your dick, you mean your dick]":        
                if P_Semen and newgirl["Laura"].Action:                
                    menu:
                        ch_l "Oh? Like what?"
                        "Could you give me a handjob?":
                            call Laura_Handjob
                        "Could you give me a titjob?":
                            ch_l "I'm not really ready for that sort of thing [[not in yet]." #fix, remove when ready
                            jump Laura_SMenu
                            call Laura_Titjob         
                        "Could you suck my cock?":
                            call Laura_Blowjob 
                        "Could use your feet?":
                            ch_l "I'm not really ready for that sort of thing [[not in yet]." #fix, remove when ready
                            jump Laura_SMenu
                            call Laura_Footjob 
                        "Never mind [[something else]":
                            jump Laura_SMenu
                elif not newgirl["Laura"].Action:
                        ch_l "Maybe in a minute, I need a break." 
                else:
                        "You really don't have it in you, maybe take a break." 
                
        "Could you put on a show for me?":
                    menu:
                        ch_l "What kind of show are you thinking?"
                        "Dance for me?":
                                if newgirl["Laura"].Action:
                                    call Group_Strip("Laura") 
                                else:
                                    ch_l "Maybe in a minute, I need a break."
                                
                        "Could you undress for me?": 
                                    call Laura_Undress  
                                            
                        "You've got a little something. . . [[clean-up]" if newgirl["Laura"].Spunk:
                                    ch_l "What?"
                                    call Laura_Cleanup("ask")
                                    
                        "Could I watch you get yourself off? [[masturbate]":
                                if newgirl["Laura"].Action:
                                    call Laura_Masturbate           
                                else:
                                    ch_l "Maybe in a minute, I need a break."
                        
                        "Maybe make out with Rogue?" if R_Loc == bg_current:
                                call Laura_LesScene
                        "Maybe make out with Kitty?" if K_Loc == bg_current:
                                call Laura_LesScene
                        "Maybe make out with Emma?" if E_Loc == bg_current:
                                call Laura_LesScene

                        "Never mind [[something else]":
                                jump Laura_SMenu
                          
                
        "Could we maybe?. . . [[fuck]":
                ch_l "I'm not really ready for that sort of thing [[not in yet]." #fix, remove when ready
                jump Laura_SMenu
                
                if newgirl["Laura"].Action:
                    menu:
                        "What did you want to do?"
                        "Lean back, I've got something in mind. . .":
                                if P_Semen:
                                    call Laura_Sex_H   
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."
                        "Fuck your pussy.":    
                                if P_Semen:                    
                                    call Laura_Sex_P  
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised."          
                        "Fuck your ass.":     
                                if P_Semen:                   
                                    call Laura_Sex_A    
                                else:
                                    "The spirit is apparently willing, but the flesh is spongy and bruised." 
                        "How about some toys? [[Pussy]":                        
                                call Laura_Dildo_Pussy     
                        "How about some toys? [[Anal]":                        
                                call Laura_Dildo_Ass   
                        "Never mind [[something else]":
                                jump Laura_SMenu
                else:
                        ch_l "Maybe in a minute, I need a break."
                        
        # "Hey, do you want in on this? [[Threesome]" if not Partner:
        #             call Sex_Menu_Threesome("Laura")
        #             jump Laura_SMenu

        "Cheat Menu" if config.developer:                                                   #Remove
            call Laura_Cheat_Menu
        "Never mind. [[exit]":         
                if newgirl["Laura"].Lust >= 50 or newgirl["Laura"].Addict >= 50:
                        call LauraFace("sad")
                        if newgirl["Laura"].Action and newgirl["Laura"].SEXP >= 15 and Round > 20:
                                if "round2" not in newgirl["Laura"].RecentActions:  
                                    ch_l "Are you sure, [newgirl[Laura].Petname]? I wasn't exactly. . . finished."                
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)
                                elif newgirl["Laura"].Addict >= 50:                        
                                    ch_l "I need more countact." 
                                else:
                                    ch_l "Aren't you forgetting something?"                          
                                menu:
                                    extend ""
                                    "Yeah, I'm done for now." if P_Semen and "round2" not in newgirl["Laura"].RecentActions:                 
                                        if "unsatisfied" in newgirl["Laura"].RecentActions and not newgirl["Laura"].OCount:                                
                                            call LauraFace("angry")
                                            $ newgirl["Laura"].Eyes = "side" 
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2)
                                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -4)
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 1)
                                            ch_l "You'll regret that one."
                                        else:                               
                                            call LauraFace("bemused", 1)
                                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)   
                                            ch_l "Selfish. . ."  
                                    "I gave it a shot." if "round2" in newgirl["Laura"].RecentActions:                 
                                        if "unsatisfied" in newgirl["Laura"].RecentActions and not newgirl["Laura"].OCount:                                
                                            call LauraFace("angry")
                                            $ newgirl["Laura"].Eyes = "side"                                 
                                            ch_l "Not a very good one."
                                        else:                               
                                            call LauraFace("bemused", 1) 
                                            ch_l "Selfish. . ."  
                                    "Hey, I did my part." if newgirl["Laura"].OCount > 2:      
                                        call LauraFace("sly", 1) 
                                        ch_l "Well. . . yeah, but. . ."  
                                    "I'm tapped out for the moment, let's try again later." if not P_Semen:
                                        call LauraFace("normal")                        
                                        ch_l "Well, you could always try something else. . ."
                                    "Ok, we can try something else." if MultiAction and "round2" not in newgirl["Laura"].RecentActions:
                                        call LauraFace("smile")
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1) 
                                        ch_l "Good. . ."                            
                                        $ newgirl["Laura"].RecentActions.append("round2")                      
                                        $ newgirl["Laura"].DailyActions.append("round2") 
                                        jump Laura_SexMenu
                                    "Again? Ok, fine." if MultiAction and "round2" in newgirl["Laura"].RecentActions:
                                        call LauraFace("sly")
                                        ch_l "Always. . ."           
                                        jump Laura_SexMenu  
                                #End "if Laura is still up for more"
                        else:  
                                call LauraFace("bemused", 1)
                                ch_l "Yeah, you look like you've had enough. We can take a break. . ."   
                                ch_l ". . .for now."
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 1)    
                        call LauraFace
                else:
                    ch_l "Ok, fine."
                    
                call Sex_Over  
                return
    if newgirl["Laura"].Loc != bg_current:
        call Set_The_Scene
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    if not MultiAction:    
        call Set_The_Scene
        ch_l "That's all. . . for now at least."
        $ newgirl["Laura"].OCount = 0
        $ Trigger = 0    
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        return
    call GirlsAngry
    jump Laura_SexMenu
# end Laura_SexMenu //////////////////////////////////////////////////////////////////////            

label Laura_Cheat_Menu:
    menu:
        "Level-Up":
            $ newgirl["Laura"].Hand += 5
            $ newgirl["Laura"].Blow += 5
            $ newgirl["Laura"].Swallow += 5
            $ newgirl["Laura"].Hand += 5
            $ newgirl["Laura"].Slap += 5
            $ newgirl["Laura"].Tit += 5
            $ newgirl["Laura"].Sex += 5
            $ newgirl["Laura"].Anal += 5
            $ newgirl["Laura"].Hotdog += 5
            $ newgirl["Laura"].Mast += 5
            $ newgirl["Laura"].Org += 5
            $ newgirl["Laura"].FondleB += 5
            $ newgirl["Laura"].FondleT += 5
            $ newgirl["Laura"].FondleP += 5
            $ newgirl["Laura"].FondleA += 5
            $ newgirl["Laura"].DildoP += 5
            $ newgirl["Laura"].DildoA += 5
            $ newgirl["Laura"].Plug += 5
            $ newgirl["Laura"].SuckB += 5
            $ newgirl["Laura"].InsertP += 5
            $ newgirl["Laura"].InsertA += 5
            $ newgirl["Laura"].LickP += 5    
            $ newgirl["Laura"].LickA += 5
            $ newgirl["Laura"].Blow += 5
            $ newgirl["Laura"].Swallow += 5
            $ newgirl["Laura"].CreamP += 5
            $ newgirl["Laura"].CreamA += 5
            $ newgirl["Laura"].SeenChest = 1
            $ newgirl["Laura"].SeenPanties = 1
            $ newgirl["Laura"].SeenPussy = 1
            "Hand [newgirl[Laura].Hand], Blow [newgirl[Laura].Blow], Swallow [newgirl[Laura].Swallow]"
        "Level Reset":
            $ newgirl["Laura"].Hand = 0
            $ newgirl["Laura"].Blow = 0
            $ newgirl["Laura"].Swallow = 0
            "Hand [newgirl[Laura].Hand], Blow [newgirl[Laura].Blow], Swallow [newgirl[Laura].Swallow]"
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
                $ newgirl["Laura"].Love = 1000
                $ newgirl["Laura"].Inbt = 1000
                $ newgirl["Laura"].Obed = 1000
                $ newgirl["Laura"].Lust = 50
                $ newgirl["Laura"].Addict = 0 #how addicted she is
                $ newgirl["Laura"].Addictionrate = 0 #How faster her addiciton rises
                $ newgirl["Laura"].Kissed = 1 #How many times they've kissed
                $ newgirl["Laura"].Swallow = 0
        "50\%":
                $ newgirl["Laura"].Love = 500
                $ newgirl["Laura"].Inbt = 500
                $ newgirl["Laura"].Obed = 500
                $ newgirl["Laura"].Lust = 65
                $ newgirl["Laura"].Addict = 0 #how addicted she is
                $ newgirl["Laura"].Addictionrate = 10 #How faster her addiciton rises
                $ newgirl["Laura"].Kissed = 10 #How many times they've kissed
                $ newgirl["Laura"].Swallow = 0
        "25\%":
                $ newgirl["Laura"].Love = 250
                $ newgirl["Laura"].Inbt = 250
                $ newgirl["Laura"].Obed = 250
                $ newgirl["Laura"].Lust = 85
                $ newgirl["Laura"].Addict = 10 #how addicted she is
                $ newgirl["Laura"].Addictionrate = 50 #How faster her addiciton rises
                $ newgirl["Laura"].Kissed = 10 #How many times they've kissed
                $ newgirl["Laura"].Swallow = 0
        "Juice up":
            $ P_Semen += 5
            $ newgirl["Laura"].Action = 10
        "Cold Shower":
            $ P_Focus = 0
        "Exit":
            return
    jump Laura_Cheat_Menu
  
label Laura_Jackin(Cnt = 0, TempVar = 0):
    if "unseen" in newgirl["Laura"].RecentActions:
            $ P_RecentActions.append("cockout") 
            $ Trigger2 = "jackin"
            "You whip out your cock and start working it." 
    else:
            if not P_Semen:
                "You don't think that would accomplish much, the poor thing is napping." 
                return
                
            if "cockout" in P_RecentActions:
                    "You start working your cock."
            else:
                    "You whip out your cock and start working it." 
                    $ P_RecentActions.append("cockout")
                    call Seen_First_Peen("Laura",Partner) 
            
            $ Trigger2 = "jackin"
            if "jackin" in newgirl["Laura"].RecentActions:
                return            
            $ newgirl["Laura"].RecentActions.append("jackin")
            $ newgirl["Laura"].DailyActions.append("jackin") 
            
            if newgirl["Laura"].SEXP < 10:
                    call LauraFace("surprised", 1,Brows="confused") 
                    $ newgirl["Laura"].Eyes = "down"
                    "Laura seems perplexed that you would do something like that."  
                    call LauraFace("angry", 1) 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 50, 5) 
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")  
                    $ renpy.pop_call()
                    return
            elif newgirl["Laura"].SEXP <= 15:            
                    call LauraFace("surprised", 2) 
                    $ newgirl["Laura"].Eyes = "down"
                    "Laura looks down at your cock with surprise."
                    call LauraFace("perplexed", 1) 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 60, 8)
                    return
            elif ApprovalCheck("Laura", 1200, TabM = 3):
                    call LauraFace("surprised", 1) 
                    $ newgirl["Laura"].Eyes = "down"
                    "Laura looks down at your cock."            
                    call LauraFace("sly", 1) 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 8)
            elif ApprovalCheck("Laura", 500, "I", TabM=2):
                    call LauraFace("surprised", 1) 
                    $ newgirl["Laura"].Eyes = "down"
                    "Laura glances at it, but just smiles in amusement."        
                    call LauraFace("sly", 1) 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 10)
            else:
                    call LauraFace("angry", 1) 
                    $ newgirl["Laura"].Eyes = "down"
                    "Laura glances down at your cock with a scowl."        
                    $ newgirl["Laura"].Eyes = "sexy"                
                    $ newgirl["Laura"].RecentActions.append("angry")
                    $ newgirl["Laura"].DailyActions.append("angry")  
                    return
            
            if newgirl["Laura"].Action:
                $ Options = ["none"]
                
                if newgirl["Laura"].Hand >= 5 and ApprovalCheck("Laura", 1200, TabM = 3):
                        $ Cnt = newgirl["Laura"].Hand - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("hand") 
                            $ Cnt -= 1
                if newgirl["Laura"].Blow >= 5 and ApprovalCheck("Laura", 1400, TabM = 3):
                        $ Cnt = newgirl["Laura"].Blow - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if "hungry" in newgirl["Laura"].Traits else 0
                        while Cnt:
                            $ Options.append("blow") 
                            $ Cnt -= 1
                if newgirl["Laura"].Tit >= 5 and ApprovalCheck("Laura", 1300, TabM = 5):
                        $ Cnt = newgirl["Laura"].Tit - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        while Cnt:
                            $ Options.append("Tit") 
                            $ Cnt -= 1
                if newgirl["Laura"].Sex >= 5 and ApprovalCheck("Laura", 1500, TabM = 5):
                        $ Cnt = newgirl["Laura"].Sex - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if newgirl["Laura"].Lust >= 70 else 0
                        while Cnt:
                            $ Options.append("sex") 
                            $ Cnt -= 1
                if newgirl["Laura"].Anal >= 5 and ApprovalCheck("Laura", 1700, TabM = 5):
                        $ Cnt = newgirl["Laura"].Anal - 4
                        $ Cnt = 10 if Cnt > 10 else Cnt
                        $ Cnt += 5 if newgirl["Laura"].Lust >= 70 and newgirl["Laura"].Loose else 0
                        while Cnt:
                            $ Options.append("anal") 
                            $ Cnt -= 1
                    
                $ renpy.random.shuffle(Options) 
                                
                $ TempVar = Options[0]  
                $ del Options[:]  
                
                if TempVar == "hand":
                        ch_l "Did you want some help with that?"
                elif TempVar == "blow":
                        ch_l "Well that looks tasty. . ."
                elif TempVar == "tit":
                        ch_l "I could use my tits. . ."
                elif TempVar == "sex":
                        ch_l "Well that's getting me wet. . ."
                elif TempVar == "anal":
                        ch_l "Why don't you stick that in me. . ."
                else:
                        ch_l "Prrrr. . ."
                        return
                    
                menu:
                    extend ""
                    "No thanks, I've got this in hand.":
                        ch_l "Can't say I didn't offer."
                        return
                    "Hmm, sounds like a plan.": 
                        $ Situation = "shift"
                
                $ Trigger2 = 0
                    
                #Close out what you were doing 
                if Trigger == "strip":
                        call Group_Strip_End
                elif Trigger == "masturbation":
                        $ newgirl["Laura"].Action -= 1
                        $ newgirl["Laura"].Mast += 1    
                        call Checkout
                else:
                        call CloseOut("Laura")
                
                show blackscreen onlayer black
                hide blackscreen onlayer black
                if TempVar == "hand":                
                        jump Laura_HJ_Prep
                elif TempVar == "blow":
                        jump Laura_BJ_Prep
                elif TempVar == "tit":
                        jump Laura_TJ_Prep
                elif TempVar == "sex":
                        jump Laura_SexPrep
                elif TempVar == "anal":
                        jump Laura_AnalPrep
    return
# End Laura "jackin it" action / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label Laura_TouchCheek:  
    call Shift_Focus("Laura")
    call LauraFace("surprised", 1) 
    if "no cheek" in newgirl["Laura"].DailyActions:
        "You reach out to brush Laura's face with your hand, but she slaps it away."
        call LauraFace("angry")
        ch_l "Hands off, dickbag."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
        return
    else:
        "You reach out and brush Laura's face with your hand."
    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)    
    if "addict laura" in P_Traits:
        $ newgirl["Laura"].Addict -= 2            
        $ newgirl["Laura"].Addictionrate += 1 if newgirl["Laura"].Addictionrate < 5 else newgirl["Laura"].Addictionrate 
        $ newgirl["Laura"].Addictionrate = 3 if newgirl["Laura"].Addictionrate < 3 else newgirl["Laura"].Addictionrate 
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)
    else:
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 5)
        
    if ApprovalCheck("Laura", 1000):
        call LauraFace("sexy", 1)
        ch_l "Hmmm, what were you thinking, [newgirl[Laura].Petname]?"
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
    elif ApprovalCheck("Laura", 800) or ApprovalCheck("Laura", 700, "L"):
        call LauraFace("smile", 1)
        ch_l "Sweet. . ."      
    elif "cheek" in newgirl["Laura"].DailyActions:        
        call LauraFace("angry", 1)
        ch_l "Hey, I warned you, [newgirl[Laura].Petname]."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
        $ newgirl["Laura"].DailyActions.append("no cheek")
    elif ApprovalCheck("Laura", 400):
        $ newgirl["Laura"].Mouth = "smile"
        $ newgirl["Laura"].Brows = "normal"
        ch_l "Um, that was weird."
    else:
        call LauraFace("angry", 1)
        ch_l "Back off, weirdo."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
    
    if "no cheek" in newgirl["Laura"].DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Laura", 300):
                    call LauraFace("sexy", 1)
                    ch_l "Yeah, stop being weird."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Uh-huh."                 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Laura", 400, "OI") or ApprovalCheck("Laura", 800):
                    call LauraFace("normal", 1)
                    $ newgirl["Laura"].Eyes = "squint"
                    ch_l "I don't know that I did. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -1) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                else:
                    call LauraFace("angry", 2)
                    $ newgirl["Laura"].Eyes = "squint"
                    ch_l "You wish."  
                    $ newgirl["Laura"].Blush = 1
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -3) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Laura", 850, "LI"):
                    call LauraFace("sexy", 1)
                    ch_l "There better be more where that came from."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                elif ApprovalCheck("Laura", 500, "LI"):
                    call LauraFace("smile", 1)
                    ch_l "I'm not the only one looking cute, [newgirl[Laura].Petname]."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Too cute for you."                 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)   
                    
            "You had a fly on you.":
                if ApprovalCheck("Laura", 700, "LI"):
                    call LauraFace("sexy", 1)
                    ch_l "Oh? Sorry. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, 1)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1)
                elif ApprovalCheck("Laura", 700):
                    call LauraFace("normal")
                    ch_l "A fly, right. . ."
                else:
                    call LauraFace("angry", 1)
                    ch_l "Riiiight, just don't touch me." 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)    
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Laura", 850):
                    call LauraFace("sexy", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Maybe if there were more to it. . ."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 1)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1)
                elif ApprovalCheck("Laura", 500, "OI"):
                    call LauraFace("normal", 1)
                    ch_l "Well. . . I guess, maybe. . . no, quit it."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Not interested."   
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -3)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)   
            
    $ newgirl["Laura"].RecentActions.append("cheek")
    $ newgirl["Laura"].DailyActions.append("cheek")
    return
    

label Laura_Headpat:  
    call Shift_Focus("Laura")
    call LauraFace("surprised", 1) 
    if "no headpat" in newgirl["Laura"].DailyActions:
        "You reach out to pat Laura on the head, but she slaps it away."
        call LauraFace("angry")
        ch_l "Seriously, hands off."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
        return
    else:
        "You reach out and pat Laura on the head."
    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)    
        
    if ApprovalCheck("Laura", 1000):
        call LauraFace("sexy", 1)
        ch_l "Mmmmm. . ."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 85, 1)
    elif ApprovalCheck("Laura", 800) or ApprovalCheck("Laura", 700, "L"):
        call LauraFace("smile", 1)
        ch_l "Mmmmmm. . ."      
    elif "headpat" in newgirl["Laura"].DailyActions:        
        call LauraFace("angry", 1)
        ch_l "I warned younot to do that."
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
        $ newgirl["Laura"].DailyActions.append("no headpat")
    elif ApprovalCheck("Laura", 400):
        $ newgirl["Laura"].Mouth = "smile"
        $ newgirl["Laura"].Brows = "normal"
        ch_l "Um, that was weird."
    else:
        call LauraFace("angry", 1)
        "She flails her arms around, knocking your hand away." 
        ch_l "Get away from me."   
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -3)
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 1)
    
    if "no headpat" in newgirl["Laura"].DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck("Laura", 300):
                    call LauraFace("sexy", 1)
                    ch_l "Yeah, stop being weird."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Uh-huh."                 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck("Laura", 400, "OI") or ApprovalCheck("Laura", 800):
                    call LauraFace("normal", 1)
                    $ newgirl["Laura"].Eyes = "squint"
                    ch_l "Um. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -1) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                else:
                    call LauraFace("angry", 2)
                    $ newgirl["Laura"].Eyes = "squint"
                    ch_l "Did not!"  
                    $ newgirl["Laura"].Blush = 1
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -3) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
        
    else:
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck("Laura", 850, "LI"):
                    call LauraFace("sexy", 1)
                    "She leans into it."
                    ch_l "Mmmmm. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)  
                    $ Count = 7
                elif ApprovalCheck("Laura", 500, "LI"):
                    call LauraFace("smile", 1)
                    ch_l "I'm not cute."
                    ch_l "But continue." 
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                    $ Count = 4
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "This cutie might bite your hand off."                 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1) 
                    $ Count = 1  
                    
            "You had a loose hair going on.":
                if ApprovalCheck("Laura", 700, "LI"):
                    call LauraFace("sexy", 1)
                    ch_l "Oh? Whatever. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, 1)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1)
                    $ Count = 4
                elif ApprovalCheck("Laura", 700):
                    call LauraFace("normal")
                    ch_l "A hair, right. . ."
                    $ Count = 3
                else:
                    call LauraFace("angry", 1)
                    ch_l "Uhuh, just don't touch me." 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ Count = 1  
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck("Laura", 850):
                    call LauraFace("sexy", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Well. . . yeah. . ."
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 1)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 1)
                    $ Count = 4
                elif ApprovalCheck("Laura", 500, "OI"):
                    call LauraFace("normal", 1)
                    ch_l "Well. . . I guess, maybe. . . no, quit it."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -1)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    $ Count = 2
                else:
                    call LauraFace("angry", 1)
                    $ newgirl["Laura"].Eyes = "side"
                    ch_l "Grrrr. . ."   
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -3)
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 3)                        
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                    $ Count = 1
        while Count and Round >= 10:
            $ Count -= 1 if Count < 5 else 0
            $ Round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of Laura's head, rubbing it softly."                    
                    if not Count:
                        if ApprovalCheck("Laura", 800):
                            call LauraFace("bemused", 2)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)                       
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                            ch_l "Ok, that's enough of that for now. . ."
                            "She ducks out from under your hand."
                            call LauraFace("bemused", 1)
                        else:
                            call LauraFace("angry", 2)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -5)                       
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 3)
                            ch_l "Ok, enough, enough. . ."
                            "She knocks your hand away."
                            call LauraFace("angry", 1)
                    elif Count == 1:
                        if ApprovalCheck("Laura", 800):
                            call LauraFace("bemused", 1)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)                        
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                            ch_l "We should probably do something else. . ."
                        else:
                            call LauraFace("angry", 2)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -2)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 2)  
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)  
                            ch_l "You aiming to lose that hand?"
                    else:
                        if ApprovalCheck("Laura", 800):
                            call LauraFace("bemused", 2,Eyes="closed")
                            if Count > 5:
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1) 
                            ch_l "Mmmmm. . ."
                        else:
                            call LauraFace("angry", 1)
                            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, -1)
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)  
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)                        
                            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2)
                            ch_l "Um. . ."
                "No":
                    $ Count = 0
    $ Count = 0                
    $ newgirl["Laura"].RecentActions.append("headpat")
    $ newgirl["Laura"].DailyActions.append("headpat")
    return
    
# Slap Ass

label Laura_Slap_Ass:
    call Shift_Focus("Laura")
    # fix add sound here?
    if renpy.showing("Laura_SexSprite"):
            show Laura_SexSprite #fix, test this
            with vpunch
    elif renpy.showing("Laura_BJ_Animation"):           #fix, make this animation work better when paused for this effect.
            show Laura_BJ_Animation
            with vpunch
    elif renpy.showing("Laura_TJ_Animation"):
            show Laura_TJ_Animation  
            with vpunch
    elif renpy.showing("Laura_HJ_Animation"):
            show Laura_HJ_Animation  
            with vpunch
    else:
            show Laura_Sprite
            with vpunch
    $ newgirl["Laura"].Slap += 1                               #add in slap-base obedience        
    if ApprovalCheck("Laura", 400, "O", TabM=1):   
        call LauraFace("sexy", 1)  
        $ newgirl["Laura"].Mouth = "surprised"
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 51, 3, 1)
        if Action_Check("Laura", "recent", "slap") < 4:
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2) if newgirl["Laura"].Slap <= 5 else newgirl["Laura"].Obed
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1) if newgirl["Laura"].Slap <= 10 else newgirl["Laura"].Obed
        $ Line = "You slap her ass and she jumps with pleasure"
    elif ApprovalCheck("Laura", 700, TabM=1):                
        call LauraFace("surprised", 1)        
        if Action_Check("Laura", "recent", "slap") < 4:
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)        
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1)
        $ Line = "You slap her ass and she looks back at you a bit startled"  
    else:                
        call LauraFace("angry", 1)        
        if Action_Check("Laura", "recent", "slap") < 4:
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 3)        
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -2)
        $ Line = "You slap her ass and she looks back at you"  
    
    if Taboo:    
        "[Line]."
        if not ApprovalCheck("Laura", 900, TabM=2):
            if newgirl["Laura"].Slap <= 5:
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)  
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)      
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2)    
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 50, -1)
            call LauraFace("angry", 1)   
            $ Line = "She looks pretty mad too"  
        elif not ApprovalCheck("Laura", 1500, TabM=2):
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 2) if newgirl["Laura"].Slap <= 5 else newgirl["Laura"].Obed
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -1)
            $ Line = "She looks a bit annoyed"  
        else:                         #Over 1500
            call LauraFace("sexy")
            $ newgirl["Laura"].Mouth = "smile"
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 1) if newgirl["Laura"].Slap <= 5 else newgirl["Laura"].Obed
            $ Line = "She gives you a naughty grin" 
        $ newgirl["Laura"].Blush = 1
        
    if not Trigger:
        "[Line]."
        $ Line = 0
        
    $ newgirl["Laura"].RecentActions.append("slap") if Action_Check("Laura", "recent", "slap") < 4 else newgirl["Laura"].RecentActions
    $ newgirl["Laura"].DailyActions.append("slap") if Action_Check("Laura", "daily", "slap") < 10 else newgirl["Laura"].DailyActions
        
    return
    
# Tag end ////////////////////////////////////////////////////////////////////////


# newgirl["Laura"].Makeout //////////////////////////////////////////////////////////////////////
label Laura_Makeout:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    
    $ Approval = ApprovalCheck("Laura", 700, TabM=1) # 50, 65, 80, Taboo -40(90)
    
    if Approval > 1 and not newgirl["Laura"].Kissed and not newgirl["Laura"].Forced:        
        call LauraFace("sexy")
        $ newgirl["Laura"].Eyes = "side"
        ch_l "Worth a shot. . ."
    if Approval and not newgirl["Laura"].Kissed:        
        call LauraFace("sexy")
        $ newgirl["Laura"].Eyes = "side"
        ch_l "If you insist. . ."   
    elif Approval and "kissing" in newgirl["Laura"].RecentActions:
            call LauraFace("sexy", 1)
            ch_l "Mmmm. . ."
            jump Laura_KissPrep
    elif Approval and "kissing" in newgirl["Laura"].DailyActions:
        call LauraFace("sexy", 1)
        $ Line = renpy.random.choice(["Mmmmmm.",       
            "Didn't we kiss enough earlier?",
            "Get over here."]) 
        ch_l "[Line]"            
    elif Approval > 1 and newgirl["Laura"].Love > newgirl["Laura"].Obed:       
        call LauraFace("sexy")
        ch_l "Mmmmm. . ."            
    elif ApprovalCheck("Laura", 500, "O") and newgirl["Laura"].Obed > newgirl["Laura"].Love:
        call LauraFace("normal")
        ch_l "If you want."
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
    elif ApprovalCheck("Laura", 300, "O") and ApprovalCheck("Laura", 200, "L"):
        call LauraFace("sexy")
        #ch_l "Ok, fine."
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
    elif newgirl["Laura"].Addict >= 50:
        call LauraFace("sexy")
        $newgirl["Laura"].Eyes = "manic"
        ch_l "I have to."    
    elif Approval:       
        call LauraFace("bemused")
        ch_l "Sure." 
    else:        
        call LauraFace("normal") # Else
        $ newgirl["Laura"].Mouth = "sad"
        ch_l "No."
        $ newgirl["Laura"].RecentActions.append("no kissing")                      
        $ newgirl["Laura"].DailyActions.append("no kissing") 
        return    
        
label Laura_KissPrep:    
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 10, 1)
    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 20, 1)
    call Laura_Kissing_Launch("kiss you")
    if newgirl["Laura"].Kissed >= 10 and newgirl["Laura"].Inbt >= 300:
        call LauraFace("sucking")
    elif newgirl["Laura"].Kissed > 1 and newgirl["Laura"].Addict >= 50:
        call LauraFace("sucking")
    else:
        call LauraFace("kiss")
    "You and Laura make out for a while."    
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no kissing")
    $ newgirl["Laura"].RecentActions.append("kissing")                      
    $ newgirl["Laura"].DailyActions.append("kissing") 
    if not newgirl["Laura"].Kissed: 
        $ newgirl["Laura"].Addict -= 5       
        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 70, 5)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, 25)            
        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 20)
        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 30, 20)
        jump Laura_Kiss_After
    $ Trigger = "kiss you"
    $ Line = 0
    $ Cnt = 0
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0  
     
label Laura_KissCycle:
    while Round >=0:
        call Shift_Focus("Laura")
        call Laura_Kissing_Launch("kiss you")       
        call LauraLust   
            
        $ P_Focus -= 10 if P_FocusX and P_Focus > 50 else 0
                  
        if  P_Focus < 100:                                                    
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                pass                
                        "Slap her ass":                     
                                    call Laura_Slap_Ass  
                                    $ Cnt += 1
                                    $ Round -= 1                                      
                                    jump Laura_KissCycle  
                        
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                        
                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                call Laura_Jackin                        
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                "You stop jack'in it."
                                $ Trigger2 = 0
                                
                        "Other options":
                                menu:   
                                    "Offhand action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                
                                    "Shift primary action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                    menu:  
                                                        "Move a hand to her breasts. . ." if newgirl["Laura"].Kissed >= 5 and MultiAction:
                                                                if newgirl["Laura"].Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Laura_Kiss_After
                                                                    call Laura_Fondle_Breasts                          
                                                                    if Trigger == "fondle breasts": 
                                                                        $ Trigger2 = "kiss you"                                   
                                                                        call Laura_FB_Prep   
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    ch_l "Maybe we could finish this up for now?"  
                                                        "Move a hand to her thighs. . ." if newgirl["Laura"].Kissed >= 5 and MultiAction:
                                                                if newgirl["Laura"].Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Laura_Kiss_After
                                                                    call Laura_Fondle_Thighs   
                                                                    if Trigger == "fondle thighs": 
                                                                        $ Trigger2 = "kiss you"      
                                                                        call Laura_FT_Prep 
                                                                    else: 
                                                                        $ Trigger = "kiss you"     
                                                                else:
                                                                    "As your hands creep downwards, she grabs your wrists."
                                                                    ch_l "Maybe we could finish this up for now?" 
                                                        "Never Mind":
                                                                jump Laura_KissCycle
                                            else:
                                                ch_l "Maybe we could finish this up for now?" 
                                    "Threesome actions (locked)" if not Partner: 
                                        pass
                                    "Threesome actions" if Partner:   
                                        menu:
                                            "Ask Laura to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Laura_Les_Change
                                            "Ask Laura to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura")   
                                                        
                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0                                                            
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0    
                                                        
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump Laura_KissCycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump Laura_KissCycle 
                                            "Never mind":
                                                        jump Laura_KissCycle 
                                    "Undress Laura":
                                            call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump Laura_KissCycle 
                        
                        "Back to Sex Menu" if MultiAction and newgirl["Laura"].Kissed >= 5:  
                                ch_p "Let's try something else." 
                                $ Situation = "shift"
                                $ Line = 0
                                jump Laura_Kiss_After
                        "End Scene": 
                                ch_p "Let's stop for now."
                                $ Line = 0
                                jump Laura_Kiss_After
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
        
        $ Cnt += 1
        $ Round -= 1  
        
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up     
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100:      
                    #If either of you could cum   
                    if P_Focus >= 100: 
                            #If you can cum:
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                    $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                    $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            
                            if P_Focus > 80:
                                jump Laura_Kiss_After 
                            $ Line = "came"
     
                    if newgirl["Laura"].Lust >= 100:       
                            #If you're still going at it and Laura can cum
                            call Laura_Cumming
                            if Situation == "shift" or "angry" in newgirl["Laura"].RecentActions:
                                jump Laura_Kiss_After            
                    
                    #If you came
                    if Line == "came":
                            if not P_Semen:
                                "You're pretty wiped, better stop for now."
                            $ Line = 0
                            jump Laura_Kiss_After                 
                
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")            
        #End orgasm
        
        if Round == 10:
            ch_l "You're looking like you could use a break."  
        elif Round == 5:
            ch_l "Five minutes, maybe."        
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    ch_l "Ok, [newgirl[Laura].Petname], that's enough of that for now."
    
label Laura_Kiss_After:
    call LauraFace("sexy") 
    
    $ newgirl["Laura"].Kissed += 1
    $ newgirl["Laura"].Action -=1
    $ newgirl["Laura"].Addictionrate += 1
    if "addictive" in P_Traits:
        $ newgirl["Laura"].Addictionrate += 1        
    
    call Partner_Like("Laura",1)
    
    if "kissing" not in newgirl["Laura"].RecentActions:
        if newgirl["Laura"].Love > 300:
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 60, 4)
        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 1)
        $ newgirl["Laura"].RecentActions.append("kissing")                      
        $ newgirl["Laura"].DailyActions.append("kissing") 
     
    if newgirl["Laura"].Kissed > 10: 
            pass        
    elif newgirl["Laura"].Kissed == 10:
            call LauraFace("smile", 1)        
            ch_l "I could do this every day."
    elif newgirl["Laura"].Kissed == 5:
            ch_l "You're really talented. . ." 
    elif newgirl["Laura"].Kissed == 1:    
            $ newgirl["Laura"].SEXP += 1 
        
    if not Situation and newgirl["Laura"].Kissed > 5 and newgirl["Laura"].Lust > 50 and ApprovalCheck("Laura", 950):
            call LauraFace("sexy", 1)
            $newgirl["Laura"].Brows = "sad"
            ch_l "Huh, that's all there is to it?"  
     
    $ Tempmod = 0  
    if Situation:
        ch_l "Oh? So what else did you have in mind?"
    else:
        call Laura_Pos_Reset  
    call Checkout
    return


# end Makeout //////////////////////////////////////////////////////////////////////

            

##  newgirl["Laura"].Masturbating //////////////////////////////////////////////////////////////////////
# Cnt 1 means she's seen you, Cnt 0 means she hasn't.
label Laura_Masturbate: #(Situation = Situation):
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Laura")
    if newgirl["Laura"].Mast:
        $ Tempmod += 10
    if newgirl["Laura"].SEXP >= 50:
        $ Tempmod += 25
    elif newgirl["Laura"].SEXP >= 30:
        $ Tempmod += 15
    elif newgirl["Laura"].SEXP >= 15:
        $ Tempmod += 5
    if newgirl["Laura"].Lust >= 90:
        $ Tempmod += 20
    elif newgirl["Laura"].Lust >= 75:
        $ Tempmod += 5
    if "exhibitionist" in newgirl["Laura"].Traits:      
        $ Tempmod += (3*Taboo) 
    if "dating" in newgirl["Laura"].Traits or "sex friend" in newgirl["Laura"].Petnames:
        $ Tempmod += 10
    elif "ex" in newgirl["Laura"].Traits:
        $ Tempmod -= 40  
    if newgirl["Laura"].ForcedCount and not newgirl["Laura"].Forced:        
        $ Tempmod -= 5 * newgirl["Laura"].ForcedCount   
        
    $ Approval = ApprovalCheck("Laura", 1300, TabM = 2) # 120, 135, 150, Taboo -80(200)
    
    call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
    
    if Situation == "join":       # This triggers if you ask to join in        
                if Approval > 1 or (Approval and newgirl["Laura"].Lust >= 50):
                    menu:        
                        extend ""
                        "Would you like some help? I could lend some helping hands. . ."  if P_Semen and newgirl["Laura"].Action:
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                call LauraFace("sexy")
                                ch_l "Huh. Well I guess you could work the top?"                  
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                                $ Trigger2 = "fondle breasts"
                                $ newgirl["Laura"].Mast += 1
                                jump LM_Cycle
                        "Would you like some help? I could. . . up to you, I guess." if P_Semen and newgirl["Laura"].Action:
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                                call LauraFace("sexy")
                                ch_l "Yeah, I guess? . ."                
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1)
                                $ D20 = renpy.random.randint(1, 20)
                                if D20 > 10:
                                    $ Trigger2 = "fondle breasts"
                                else:
                                    $ Trigger2 = "suck breasts"
                                $ newgirl["Laura"].Mast += 1
                                jump LM_Cycle
                        "Why don't we take care of each other?" if P_Semen and newgirl["Laura"].Action:
                                call LauraFace("sexy")
                                ch_l "Like what?"                    
                                $ renpy.pop_call()          #removes the call to this label 
                                return                      #returns to sexmenu=
                        "You look like you have things well in hand. . .":
                                if newgirl["Laura"].Lust >= 50:
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)      
                                    call LauraFace("sexy")
                                    ch_l "I am getting pretty close. . ."                    
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 3)
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 5)  
                                    jump LM_Cycle
                                elif ApprovalCheck("Laura", 1200):
                                    call LauraFace("sly")                        
                                    ch_l "Yeah. . . but I can take a break. . ."
                                else:
                                    call LauraFace("angry")
                                    ch_l "-until you messed it up."
                                    
                #else: You've failed all checks so she kicks you out.
                $ newgirl["Laura"].Girl_Arms = 1  
                call LauraOutfit  
                $ newgirl["Laura"].Action -= 1
                $ P_Focus = Statupdate("Laura", "Focus", P_Focus, 50, 30)
                call Checkout(1)
                $ Line = 0
                $ Situation = 0      
                $ renpy.pop_call()          #removes the call to this label 
                if Approval:     
                        call LauraFace("bemused", 2)
                        if bg_current == "bg laura":
                            ch_l "Why are you in my room?"   
                        else:
                            ch_l "I wasn't expecting company. . ." 
                        $ newgirl["Laura"].Blush = 1
                else:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)
                        call LauraFace("angry")
                        $ newgirl["Laura"].RecentActions.append("angry")
                        $ newgirl["Laura"].DailyActions.append("angry")  
                        if bg_current == "bg laura":
                            ch_l "I was kinda busy, so get out."
                            "Laura kicks you out of her room."
                            $ renpy.pop_call()
                            jump Campus_Map  
                        else:
                            ch_l "I'm getting out of here, but maybe knock next time."
                            hide Laura with easeoutbottom
                            call Remove_Girl("Laura")
                return                      #returns to sexmenu, which returns to original    
    #End of "Join" option
    
    
    
    if Situation == "Laura":                                                                  #Laura auto-starts   
                if Approval > 2:                                                      # fix, add laura auto stuff here
                        if newgirl["Laura"].Legs == "skirt":
                            "Laura's hand snakes down her body, and hikes up her skirt."
                            $ newgirl["Laura"].Upskirt = 1
                        elif newgirl["Laura"].Legs == "pants":
                            "Laura slides her hand down her body and into her jeans."  
                        elif HoseNum("Laura") >= 5:
                            "Laura's hand slides down her body and under her [newgirl[Laura].Hose]."
                        elif newgirl["Laura"].Panties:                
                            "Laura's hand slides down her body and under her [newgirl[Laura].Panties]."
                        else:
                            "Laura's hand slides down her body and begins to caress her pussy."
                        $ newgirl["Laura"].SeenPanties = 1
                        "She starts to slowly rub herself."
                        menu:
                            "What do you do?"
                            "Nothing.":                    
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3) 
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 2)
                                    "Laura begins to masturbate."
                            "Go for it.":       
                                    call LauraFace("sexy, 1")                    
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 3) 
                                    ch_p "That is so sexy, [newgirl[Laura].Pet]."
                                    call Laura_Namecheck
                                    "You lean back and enjoy the show."
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                            "Ask her to stop.":
                                    call LauraFace("surprised")       
                                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 1) 
                                    ch_p "Let's not do that right now, [newgirl[Laura].Pet]."
                                    call Laura_Namecheck
                                    "Laura pulls her hands away from herself."
                                    call LauraOutfit
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 30, 2)
                                    return            
                        jump LM_Prep
                else:                
                        $ Tempmod = 0                               # fix, add laura auto stuff here
                        $ Trigger2 = 0
                return            
    #End if Laura intitiates this action
    
    #first time
    if not newgirl["Laura"].Mast:                                                                
            call LauraFace("surprised", 1)
            $ newgirl["Laura"].Mouth = "kiss"
            ch_l "So you want me to masterbate while you watch?"
            if newgirl["Laura"].Forced:
                call LauraFace("sad")
                ch_l "And you {i}just{/i} want to watch. . ."
            
            
    #First time dialog             
    if not newgirl["Laura"].Mast and Approval:                                                      
            if newgirl["Laura"].Forced: 
                call LauraFace("sad")
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
            elif newgirl["Laura"].Love >= newgirl["Laura"].Obed and newgirl["Laura"].Love >= newgirl["Laura"].Inbt:
                call LauraFace("sexy")
                $ newgirl["Laura"].Brows = "sad"
                $ newgirl["Laura"].Mouth = "smile" 
                ch_l "I don't know, are you sure?"          
            elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                call LauraFace("normal")
                ch_l "If that's what you're into. . ."            
            else: # Uninhibited 
                call LauraFace("sad")
                $ newgirl["Laura"].Mouth = "smile"             
                ch_l "I do have some free time. . ."     
    
    
    #Second time+ initial dialog
    elif Approval:                                                                       
            if newgirl["Laura"].Forced: 
                call LauraFace("sad")
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -3, 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 20, -2, 1)
                ch_l "Hmm, again?"  
            elif Approval and "masturbation" in newgirl["Laura"].RecentActions:
                call LauraFace("sexy", 1)
                ch_l "I have built up some more tension. . ."    
                jump LM_Prep
            elif Approval and "masturbation" in newgirl["Laura"].DailyActions:
                call LauraFace("sexy", 1)
                $ Line = renpy.random.choice(["Did you enjoy that?",       
                    "Didn't get enough earlier?",
                    "I liked having an audience. . ."]) 
                ch_l "[Line]"            
            elif newgirl["Laura"].Mast < 3:        
                call LauraFace("sexy", 1)
                $ newgirl["Laura"].Brows = "confused"
                ch_l "Did you. . . like it last time?"       
            else:       
                call LauraFace("sexy", 1)
                $ newgirl["Laura"].Girl_Arms = 2
                $ Line = renpy.random.choice(["You like to watch.",                 
                    "Again?",                 
                    "You really like to watch me.",
                    "You want me to masturbate again?"]) 
                ch_l "[Line]"
                $ Line = 0
    #End second time+ initial dialog
    
    #If she's into it. . .  
    if Approval >= 2:                                                                                
            if newgirl["Laura"].Forced:
                call LauraFace("sad")
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 1)
                ch_l "Whatever. . ." 
            else:
                call LauraFace("sexy", 1)
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 50, 3) 
                $ Line = renpy.random.choice(["Huh. Ok.",                 
                    "Couldn't hurt. . .",
                    "Allright.", 
                    "Sure.",
                    "Heh, ok."]) 
                ch_l "[Line]"
                $ Line = 0
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 20, 1)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 60, 1)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2) 
            jump LM_Prep   
            
    #If she's not into it, but maybe. . .    
    else:                                                                                       
        menu:
            ch_l "I don't know that I want to do that right now."
            "Maybe later?":
                    call LauraFace("sexy", 1)  
                    if newgirl["Laura"].Lust > 70:                        
                        ch_l "I probably will be, but not with an audience."
                    else:
                        ch_l "Hmm, maybe. . ."
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, 2)
                    $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 2)               
                    return
            "You look like you could use it. . .":             
                    if Approval:
                        call LauraFace("sexy")     
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 70, 3) 
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 40, 2) 
                        $ Line = renpy.random.choice(["Huh. Ok.",                 
                                "Couldn't hurt. . .",
                                "Allright.", 
                                "Sure.",
                                "Heh, ok."]) 
                        ch_l "[Line]"
                        $ Line = 0                   
                        jump LM_Prep
                    else:   
                        pass
                    
            "Just get at it already.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Laura", 450, "OI", TabM = 2) # 45, 60, 75, -80(125)
                    if Approval > 1 or (Approval and newgirl["Laura"].Forced):
                        call LauraFace("sad")
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5, 1)
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5)                 
                        ch_l "Whatever."  
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 80, 4)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 1) 
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 60, 3)  
                        $ newgirl["Laura"].Forced = 1  
                        jump LM_Prep
                    else:                              
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -20)     
                        $ newgirl["Laura"].RecentActions.append("angry")
                        $ newgirl["Laura"].DailyActions.append("angry")
    # end of asking her to do it
    
    #She refused all offers.
    $ newgirl["Laura"].Girl_Arms = 1                
    if newgirl["Laura"].Forced:
            call LauraFace("angry", 1)
            ch_l "This is just too weird for me."
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)         
            if newgirl["Laura"].Love > 300:
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -2)
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -2)    
            $ newgirl["Laura"].RecentActions.append("angry")
            $ newgirl["Laura"].DailyActions.append("angry")   
            $ newgirl["Laura"].RecentActions.append("no masturbation")                      
            $ newgirl["Laura"].DailyActions.append("no masturbation") 
            return
    elif Taboo:                             # she refuses and this is too public a place for her
            call LauraFace("angry", 1)          
            $ newgirl["Laura"].DailyActions.append("tabno") 
            ch_l "I couldn't do that in public."     
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)  
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, -3)    
            return                
    elif newgirl["Laura"].Mast:
            call LauraFace("sad") 
            ch_l "I'm not into it right now."     
    else:
            call LauraFace("normal", 1)
            ch_l "Um, no."  
    $ newgirl["Laura"].RecentActions.append("no masturbation")                      
    $ newgirl["Laura"].DailyActions.append("no masturbation") 
    $ Tempmod = 0 
    return

label LM_Prep: 
    $ newgirl["Laura"].Upskirt = 1    
    $ newgirl["Laura"].PantiesDown = 1 
    call Set_The_Scene(Dress=0)   
    
    #if she hasn't seen you yet. . .
    if "unseen" in newgirl["Laura"].RecentActions:
            call LauraFace("sexy")
            $ newgirl["Laura"].Eyes = "closed"
            $ newgirl["Laura"].Girl_Arms = 2
            "You see Laura leaning back, masturbating. You don't think she's noticed you yet."
    else:    
            call LauraFace("sexy")
            $ newgirl["Laura"].Girl_Arms = 2
            "Laura lays back and starts to toy with herself."
            if not newgirl["Laura"].Mast:#First time        
                    if newgirl["Laura"].Forced:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -20)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 45)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 35) 
                    else:
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 15)
                        $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 35)
                        $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 80, 40)  
        
    
    $ Trigger = "masturbation"   
    if Situation:     
        $ renpy.pop_call() 
        $ Situation = 0 
    $ Line = 0
    if Taboo:
        call DrainWord("Laura","tabno")
    call DrainWord("Laura","no masturbation")
    $ newgirl["Laura"].RecentActions.append("masturbation")                      
    $ newgirl["Laura"].DailyActions.append("masturbation") 
            
label LM_Cycle:      
    if Situation == "join":
        $ renpy.pop_call() 
        $ Situation = 0 
        
    while Round >=0:  
        call Laura_Pos_Reset("masturbation")
        call Shift_Focus("Laura") 
        call LauraLust  
        if "unseen" in newgirl["Laura"].RecentActions:  
                $ newgirl["Laura"].Eyes = "closed"
                if newgirl["Laura"].ScentTimer >= 3:
                        $ newgirl["Laura"].ScentTimer = 0
                        "Laura's nose twitches and she seems to be sniffing the air."
                        jump LM_Interupted
                $ newgirl["Laura"].ScentTimer += 1
        
        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0
            
        if  P_Focus < 100:                                                    
                    #Player Command menu                                        
                    menu:
                        "Keep Watching.":
                                pass
                                
                        "Laura. . .[[jump in]" if "unseen" not in newgirl["Laura"].RecentActions:                 
                                "Laura slows what she's doing with a sly grin."
                                ch_l "Are you enjoying this?"
                                $ Situation = "join"
                                call Laura_Masturbate               
                        "\"Ahem. . .\"" if "unseen" in newgirl["Laura"].RecentActions:  
                                jump LM_Interupted    
                                                   
                        "Start jack'in it." if Trigger2 != "jackin":
                                call Laura_Jackin                   
                        "Stop jack'in it." if Trigger2 == "jackin":
                                $ Trigger2 = 0    
                                            
                        "Slap her ass":    
                                if "unseen" in newgirl["Laura"].RecentActions:
                                        "You smack Laura firmly on the ass!"
                                        jump LM_Interupted                                          
                                else:
                                        call Laura_Slap_Ass                                        
                                        $ Cnt += 1
                                        $ Round -= 1    
                                        jump LM_Cycle  
                           
                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."                
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."                
                                    $ P_FocusX = 0
                                    
                        "Change what I'm doing":
                                menu:
                                    "Offhand action":
                                            if newgirl["Laura"].Action and MultiAction:
                                                call Laura_Offhand_Set
                                                if Trigger2:
                                                     $ newgirl["Laura"].Action -= 1
                                            else:
                                                ch_l "Maybe we could finish this up for now?"  
                                                           
                                    "Threesome actions (locked)" if not Partner or "unseen" in newgirl["Laura"].RecentActions: 
                                        pass
                                    "Threesome actions" if Partner and "unseen" not in newgirl["Laura"].RecentActions:   
                                        menu:
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Laura")   
                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Laura")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump LM_Cycle 
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump LM_Cycle 
                                            "Never mind":
                                                        jump LM_Cycle 
                                    "Undress Laura":
                                            if "unseen" in newgirl["Laura"].RecentActions:
                                                    ch_p "Oh, yeah, take it off. . ."
                                                    jump LM_Interupted
                                            else:                                        
                                                    call Laura_Undress   
                                    "Clean up Laura (locked)" if not newgirl["Laura"].Spunk:
                                            pass  
                                    "Clean up Laura" if newgirl["Laura"].Spunk:
                                            if "unseen" in newgirl["Laura"].RecentActions:
                                                    ch_p "You've got a little something on you. . ."
                                                    jump LM_Interupted
                                            else:                      
                                                    call Laura_Cleanup("ask")                                         
                                    "Never mind":
                                            jump LM_Cycle                               
                         
                        "Back to Sex Menu" if MultiAction: 
                                    ch_p "Let's try something else."
                                    call Laura_Pos_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump LM_Interupted
                        "End Scene" if not MultiAction: 
                                    ch_p "Let's stop for now."
                                    call Laura_Pos_Reset
                                    $ Line = 0
                                    jump LM_Interupted
        #End menu (if Line)
        
        call Shift_Focus("Laura")  
        call Sex_Dialog("Laura",Partner)
                
        #If either of you could cum 
        
        $ Cnt += 1
        $ Round -= 1
    
        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        
        if P_Focus >= 100 or newgirl["Laura"].Lust >= 100:   
                    #If you can cum:
                    if P_Focus >= 100:
                        if "unseen" not in newgirl["Laura"].RecentActions: 
                            #if she knows you're there
                            call PLaura_Cumming
                            if "angry" in newgirl["Laura"].RecentActions:  
                                call Laura_Pos_Reset
                                return    
                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                            if 100 > newgirl["Laura"].Lust >= 70 and newgirl["Laura"].OCount < 2:             
                                $ newgirl["Laura"].RecentActions.append("unsatisfied")                      
                                $ newgirl["Laura"].DailyActions.append("unsatisfied") 
                            $ Line = "came"
                        else: #If she wasn't aware you were there
                            "You grunt and try to hold it in."
                            $ P_Focus = 95
                            jump LM_Interupted
     
                    #If Laura can cum
                    if newgirl["Laura"].Lust >= 100:                                               
                        call Laura_Cumming
                        jump LM_Interupted
                       
                    if Line == "came": 
                        $ Line = 0
                        if not P_Semen:
                            "You're emptied out, you should probably take a break."
                            
                            
                        if "unsatisfied" in newgirl["Laura"].RecentActions:#And Laura is unsatisfied,  
                            "Laura still seems a bit unsatisfied with the experience."
                            menu:
                                "Finish her?"
                                "Yes, keep going for a bit." if P_Semen:
                                    $ Line = "You get back into it" 
                                    jump LM_Cycle  
                                "No, I'm done.":
                                    "You pull back."
                                    return
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Laura")                            
        #End orgasm
        
        if "unseen" in newgirl["Laura"].RecentActions:
                if Round == 10:
                    "It's getting a bit late, Laura will probably be wrapping up soon."  
                elif Round == 5:
                    "She's definitely going to stop soon."
        else:
                if Round == 10:
                    ch_l "We might want to wrap this up, it's getting late."  
                    $ newgirl["Laura"].Lust += 10
                elif Round == 5:
                    ch_l "Five minutes, maybe."     
                    $ newgirl["Laura"].Lust += 25   
    
    #Round = 0 loop breaks
    call LauraFace("bemused", 0)
    $ Line = 0
    if "unseen" not in newgirl["Laura"].RecentActions:
        ch_l "Ok, I'm kinda done for now, I need a break."
    
label LM_Interupted:
    
    # If she hasn't noticed you're there before cumming
    if "unseen" in newgirl["Laura"].RecentActions:                         
                call LauraFace("surprised", 2)
                "Laura stops what she's doing with a start, eyes wide."
                call Laura_First_Bottomless(1) 
                call LauraFace("surprised", 2)
                
                #If you've been jacking it
                if Trigger2 == "jackin":
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        $ newgirl["Laura"].Eyes = "down"
                        menu:
                            ch_l "And um. . . you have your penis out. . . "
                            "A while back, it was an excellent show.":   
                                    call LauraFace("sexy",1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                    ch_l "Really? Weird. . ."
                                    if newgirl["Laura"].Love >= 800 or newgirl["Laura"].Obed >= 500 or newgirl["Laura"].Inbt >= 500:
                                        $ Tempmod += 10
                                        $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)
                                        ch_l "I um. . . you're not so bad yourself. . ."  
                                    
                            "I. . . just got here?":
                                    call LauraFace("angry",1)                   
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                    "She looks pointedly at your cock,"
                                    ch_l "Long enough to whip that out?"   
                                    if newgirl["Laura"].Love >= 800 or newgirl["Laura"].Obed >= 500 or newgirl["Laura"].Inbt >= 500:
                                            $ Tempmod += 10
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)
                                            call LauraFace("bemused", 1)
                                            ch_l "It was really that interesting?"   
                                    else:
                                            $ Tempmod -= 10
                                            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, -5)
                        call Seen_First_Peen("Laura",Partner) 
                                    
                #you haven't been jacking it                    
                else:         
                        ch_l "Huh."
                        ch_l "When did you get here?"
                        menu:
                            extend ""
                            "A while back.":   
                                    call LauraFace("sexy", 1)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 3)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)
                                    ch_l "I must have put on a show. . ."
                            "I just got here.":
                                    call LauraFace("bemused", 1)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, 2)
                                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 1)                    
                                    ch_l "Uh-huh. . ."   
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 50, 2)
                                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 70, 2)    
                                
                call DrainWord("Laura","unseen",1,0) #She sees you, so remove unseens
                $ newgirl["Laura"].Mast += 1
                if Round <= 10:
                    ch_l "I kinda needed a break anyway. . ."
                    return
                $ Situation = "join"        
                call Laura_Masturbate
                "error: report this if you see it."
                return #should be redundant
    #End Unseen
    
    #else, if She's seen you already    
    $ newgirl["Laura"].Action -= 1
    $ newgirl["Laura"].Mast += 1    
    call Checkout
    if Situation == "shift":        
        $ Situation = 0
        return
    $ Situation = 0
        
    if Partner == "Emma":
        call Partner_Like("Laura",3)
    else:
        call Partner_Like("Laura",2)
                    
    if Round <= 10:
            ch_l "I need a minute here. . ."
            return
    call LauraFace("sexy", 1)
    if newgirl["Laura"].Lust < 20:
        ch_l "I guess that worked out, how about you?"
    else:
        ch_l "So, what next?"
    menu:
        extend ""
        "Well, I have something you could take care of. . ." if P_Semen and newgirl["Laura"].Action:
                $ Situation = "shift"
                return   
        "You could just keep going. . ." if P_Semen:
                call LauraFace("sly")
                if newgirl["Laura"].Action and Round >= 10:
                    ch_l "Ok. . ."
                    jump LM_Cycle
                else:
                    ch_l "I need a minute here. . ."
        "I'm good here. [[Stop]":  
                if newgirl["Laura"].Love < 800 and newgirl["Laura"].Inbt < 500 and newgirl["Laura"].Obed < 500:
                    call LauraOutfit
                call LauraFace("normal")
                $ newgirl["Laura"].Brows = "confused"
                ch_l "Ok."
                $ newgirl["Laura"].Brows = "normal" 
        "You should probably stop for now." if newgirl["Laura"].Lust > 30:
                call LauraFace("angry")
                ch_l "Hrmm."
    return
    
## end newgirl["Laura"].Masturbating ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# Laura_Offhand function //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


label Laura_Offhand(TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    
    $ D20 = renpy.random.randint(1, 20)                                                                 # Taboo caught check
                    
    if not Trigger2: #If there are no offhand options set, return
        return    
    
    if Trigger2 == "kiss you":
                $ Line = renpy.random.choice([" Your lips gently slide across hers.", 
                        " Her lips part as you hold her close.",    
                        " You nibble her neck as she groans in pleasure.",
                        " You squeeze her tightly as your tongues jostle.",
                        " Her tongue dances around yours.",
                        " She bites your ear as her hands slide across your back.",
                        " Your hands slide down her body as your lips press hers.",
                        " You kiss her passionately.", 
                        " Your tongues swirl around each other's."])
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 75, 1) if newgirl["Laura"].Love >= 300 else newgirl["Laura"].Love
                $ PrimaryLust += 2 if newgirl["Laura"].Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                $ Line = renpy.random.choice([" You reach out and massage her pert breasts.", 
                        " You pass your hands gently over her warm breasts.", 
                        " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                        " She gasps as you lightly thumb her tight nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if newgirl["Laura"].Chest:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You tease her nipples with your tongue through her top.",
                    " You slowly lick her nipples through her moist top.", 
                    " you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples, poking through her top."])            
            else:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You gently nibble at her nipples as you suck on them.",
                    " You tease her nipples with your tongue.",
                    " You slowly lick around, and then blow across her nipples.", 
                    " You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < newgirl["Laura"].Lust < 80 else 2  
            $ TempFocus += 3 if P_Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            
            $ Line = renpy.random.choice([" You put your hand against her mound and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < newgirl["Laura"].Lust < 90 else 2        
            $ TempFocus += 4 if P_Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if newgirl["Laura"].Legs != "pants" and not newgirl["Laura"].Panties:  
                $ Line = renpy.random.choice([" You slide your tongue into her pussy and flick the roof with deft strokes.", 
                    " You spread the lips back and she gasps as you slide your tongue between them.", 
                    " You can feel her twitching as you grind your tongue against her clit.",
                    " She gasps as you suck on her clit.",
                    " You rub her clit with your thumb as you dive into her pussy with your tongue.",
                    " With a little nibble, you tug on her lower lips.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([" You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.", 
                    " She gasps as you suck on her clit through the fabric.",
                    " You rub her clit with your thumb as you press against her pussy with your tongue.",
                    " You put your hand against her mound and lick the juice that's collected.", 
                    " With a little nibble, you tug back the fabric.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if newgirl["Laura"].Lust > 50 else 2       
            $ TempFocus += 4 if P_Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            if newgirl["Laura"].Legs != "pants" and not newgirl["Laura"].Panties: 
                $ Line = renpy.random.choice([" You reach out and brush your hands across her bare ass.", 
                        " You put your hand against her firm rear and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " She gasps as you reach under her and lightly stroke her ass.",
                        " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            else:
                $ Line = renpy.random.choice([" You reach out and brush your hands across her ass.", 
                        " You put your hand against her firm rear and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " She gasps as you reach under her and lightly stroke her ass.",
                        " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if newgirl["Laura"].Lust < 50 else 1
            $ TempFocus += 1 if P_Focus < 50 else 0  
            $ TempFocus += 1 if P_Focus < 80 else 0   
        
    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([" You reach out and slide a finger into her ass.", 
                    " You slide a finger into her asshole and stroke the roof of it.", 
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.", 
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])       
            $ PrimaryLust += 3 if newgirl["Laura"].Lust > 70 and newgirl["Laura"].Loose else 1
            $ TempFocus += 2 if P_Focus < 90 else 0 
        
    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = " You stroke your cock as you watch her go."
            elif Trigger == "lesbian":
                    $ Line = " You stroke your cock as you watch them."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you polish the knob a bit.", 
                            " You help.",
                            " Your hand bumps into hers occasionally."])     
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you work the shaft a bit.", 
                            " Your fingers brush her lips.",
                            " Her lips brush your hand occasionally."])    
            else:
                    $ Line = renpy.random.choice([" With your other hand, you stroke your shaft.", 
                            " You stroke your cock with your other hand.", 
                            " As you do, you stoke yourself."])            
            if "unseen" not in newgirl["Laura"].RecentActions:
                $ PrimaryLust += 3 if 20 < newgirl["Laura"].Lust < 70 else 2
                $ TempFocus += 1 if P_Focus < 70 else 0            
            $ TempFocus += 5
               
    return                      #End Laura_Offhand check
    


label Laura_Offhand_Set(Situation = Situation, TempTrigger = Trigger2):
    
    if Situation == "shift focus":        
            if TempTrigger:      
                $ Trigger2 = 0  
#                $ Situation = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump Laura_FB_Prep
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump Laura_SB_Prep
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump Laura_FP_Prep
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump Laura_LP_Prep
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump Laura_FA_Prep
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump Laura_IA_Prep
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump Laura_KissPrep                
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."     
            return
    # End "shift" situation    
        
    if Trigger:
        $ Situation = "auto"                 
        menu:  
            "Also kiss her." if Trigger in ("fondle breasts", "fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal", "foot"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kiss you"
                    
            "Also fondle her breasts." if Trigger in ("fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle breasts"
                    call Laura_Fondle_Breasts
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "suck breasts"
                    call Laura_Suck_Breasts
                    
            "Also fondle her pussy." if Trigger in ("fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal", "foot"):
                    $ Trigger2 = "fondle pussy"
                    call Laura_Fondle_Pussy
                    
            "Also fondle her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call Laura_Fondle_Ass
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "dildo pussy", "foot"):
                    $ Trigger2 = "insert ass"
                    call Laura_Insert_Ass
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call Laura_Jackin
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Laura_Offhand function ////////////////////////////////////////////////////////////////////////


label Laura_ShameIndex:   
    $ newgirl["Laura"].ShameLevel = 0
    
    if Trigger == "kiss you":
        $ newgirl["Laura"].ShameLevel += 2
        
    elif Trigger in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Laura"].ShameLevel += 6
        
    elif Trigger in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ newgirl["Laura"].ShameLevel += 10
        
    elif Trigger in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand", "blow", "titjob", "masturbation"):
        $ newgirl["Laura"].ShameLevel += 15
    
    elif Trigger in ("sex",  "anal"):
        $ newgirl["Laura"].ShameLevel += 20
    
    
    if not Trigger2:
        pass
    if Trigger2 == "kiss you":
        $ newgirl["Laura"].ShameLevel += 2
        
    elif Trigger2 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Laura"].ShameLevel += 6
        
    elif Trigger2 in ("fondle pussy", "insert ass", "suck breasts", "hotdog"):
        $ newgirl["Laura"].ShameLevel += 10
        
    elif Trigger2 in ("lick pussy", "dildo pussy", "lick ass", "dildo anal", "hand"):
        $ newgirl["Laura"].ShameLevel += 15    
        
        
    if not Trigger3:
        pass
    elif Trigger3 == "kiss you":
        $ newgirl["Laura"].ShameLevel += 2
    elif Trigger3 == "kiss girl":
        $ newgirl["Laura"].ShameLevel += 3
    elif Trigger3 == "kiss both":
        $ newgirl["Laura"].ShameLevel += 4
        
    elif Trigger3 in ("fondle breasts", "fondle thighs", "fondle ass"):
        $ newgirl["Laura"].ShameLevel += 6
        
    elif Trigger3 in ("fondle pussy"):
        $ newgirl["Laura"].ShameLevel += 10
        
    elif Trigger3 in ("dildo pussy", "dildo anal", "hand"):
        $ newgirl["Laura"].ShameLevel += 15
    
    
    $ newgirl["Laura"].ShameLevel += newgirl["Laura"].Shame #adds clothing based shame
    
    return
            
label Laura_Taboo(Cnt= 1):    
    
    $ Cnt = Action_Check("Laura", "recent", "spotted") if "spotted" in newgirl["Laura"].RecentActions else 1
    $ Cnt = 4 if Cnt > 4 else Cnt   
    
    $ D20 = renpy.random.randint(1, 20)  
        
    if D20 < 10:               
        #if you're at the point where the girls would notice you. . .  
        if Taboo > 20:
            if (Trigger == "kiss you" and not Trigger2 and not Trigger3):
                pass
            elif "Laura" not in Rules:
                #if Xavier is looking. . .
                call LauraFace("surprised", 1)
                if Trigger == "blow" or Trigger == "hand" or Trigger == "titjob":
                    "Laura stops what she's doing with a startled look."                
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!" 
                call AllReset("Laura")
                $ renpy.pop_call()        
                $ renpy.pop_call()
                call Laura_Caught
                return
            else:
                #if you've disabled Xavier's looking
                ch_x "Hmmm. . ."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2) 
                $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 3) 
                
        if bg_current == "bg classroom" and E_Loc == "bg teacher":
            #If you're in class and emma's there as a teacher. . .
            call Emma_Teacher_Caught("Laura")
        call Girls_Noticed("Laura")
            
    if Taboo <= 20:
            #This is a private space with others around.
            call Girls_Noticed("Laura")
            return        
    elif Cnt < 4:        
            call LauraFace("surprised", 2)                                              
            #if this has happened less than 4 times within the current cycle of events
                  #if this has happened less than 4 times within the current cycle of events
            if "spotted" not in newgirl["Laura"].RecentActions:
                "Some of the other students notice you and Laura."
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 2)               
                $ newgirl["Laura"].Rep -= 2                         
                $ P_Rep -= 2             
            elif Cnt < 3:
                "A few more students notice you and Laura."   
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 2)               
                $ newgirl["Laura"].Rep -= 1                    
                $ P_Rep -= 1  
            elif Cnt == 3:
                "You've got quite an audience."               
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 200, 3)               
                $ newgirl["Laura"].Rep -= 1                    
                $ P_Rep -= 1  
                
            if "exhibitionist" in newgirl["Laura"].Traits:                
                    call LauraFace("sexy", 0)                     
                    if "spotted" not in newgirl["Laura"].RecentActions:
                        ch_l "Well, let's give'em what they want."                          
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 5) 
                    $ Line = "A"
            elif ApprovalCheck("Laura", 750, "I", TabM=Cnt):            
                    #not an exhibitionist but very uninhibited       
                    call LauraFace("sexy", 1)                    
                    $ newgirl["Laura"].Brows = "sad"                           
                    if "spotted" not in newgirl["Laura"].RecentActions:                        
                        ch_l "How do you want to play this?" 
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 4)   
                    $ Line = "B"
            elif ApprovalCheck("Laura", 1000, "OI", TabM=Cnt):     
                    #not an exhibitionist but obedient/uninhibited          
                    call LauraFace("surprised", 2)
                    "Laura looks a bit uncomfortable."
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 200, 4)
                    $ Line = "C"
            else:  
                    # She fails her inhibition checks
                    call LauraFace("surprised", 2)
                    if "spotted" not in newgirl["Laura"].RecentActions:    
                        "Laura bolts up with an embarassed look. She grabs her clothes and bolts through the nearest door."  
                        $ newgirl["Laura"].Rep -= 3 if newgirl["Laura"].Rep >= 30 else newgirl["Laura"].Rep            
                    else:
                        "With a sudden embarrassed start, Laura panics. She bolts through the nearest door."
                        $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -15) 
                    "You head back to your room."                    
                    $ Line = "stop"
                
            if Line != "stop":
                menu:
                    "What would you like to do?"
                    "Let them watch. . ." if "spotted" not in newgirl["Laura"].RecentActions:   
                        if Line == "A":                
                                call LauraFace("sexy", 0) 
                                ch_l "I can handle that."             
                        elif Line == "B":            
                                #not an exhibitionist but very uninhibited       
                                call LauraFace("sexy", 1)
                                $ newgirl["Laura"].Brows = "sad"               
                                ch_l "Ok."    
                        elif Line == "C":     
                                call LauraFace("sexy",2)
                                if newgirl["Laura"].Obed > newgirl["Laura"].Inbt:
                                    $ newgirl["Laura"].Eyes = "side"
                                    ch_l "I guess."
                                else:          
                                    $ newgirl["Laura"].Mouth = "smile"
                                    $ newgirl["Laura"].Brows = "sad"
                                    ch_l "Whatever. . ."                        
                                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5)                       
                        "You get back to it." 
                        $ newgirl["Laura"].Blush = 1
                    "Continue" if "spotted" in newgirl["Laura"].RecentActions:
                        if Line == "C":          
                            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 200, 5) 
                    "Ok, let's stop.":   
                        if Line == "A":                            
                                call LauraFace("sad")
                                ch_l "Sissy."                                         
                        elif Line == "B":            
                                call LauraFace("sad")
                                ch_l "Probably a good call." 
                        elif Line == "C":     
                                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 10)          
                                call LauraFace("smile")
                                ch_l "Yeah, thanks." 
                        "You both run back to your rooms."
                        $ Line = "stop"
                        
            if Line == "stop":            
                    $ newgirl["Laura"].RecentActions.append("caught")
                    $ newgirl["Laura"].DailyActions.append("caught")     
                    show blackscreen onlayer black 
                    call AllReset("Laura")
                    hide Laura_Sprite with easeoutright  
                    call Remove_Girl("Laura")
                    call LauraOutfit
                    hide blackscreen onlayer black 
                    $ renpy.pop_call()          
                    $ renpy.pop_call()       
                    $ renpy.pop_call()                    
                    jump Player_Room             
    elif "exhibitionist" not in newgirl["Laura"].Traits:     
        call LauraFace("sly")   
        $ newgirl["Laura"].Traits.append("exhibitionist") 
        "Laura seems to have become something of an exhibitionist."
    elif D20 > 15:
        call LauraFace("sexy")
        "The crowd cheers."
        
    $ newgirl["Laura"].RecentActions.append("spotted") if Cnt < 4 else newgirl["Laura"].RecentActions
    $ newgirl["Laura"].DailyActions.append("spotted")  if "spotted" not in newgirl["Laura"].DailyActions else newgirl["Laura"].DailyActions
    return
    
    
label Laura_Noticed(Other = "Rogue", Silent=0, B = 0):
    if "threesome" in newgirl["Laura"].RecentActions:
            return
    if Partner == "Laura" and "noticed " + Other in newgirl["Laura"].RecentActions:
            return
#    if Partner == "Laura" and "noticed Rogue" in newgirl["Laura"].RecentActions and Other == "Rogue":
#            return
#    if Partner == "Laura" and "noticed Kitty" in newgirl["Laura"].RecentActions and Other == "Kitty":
#            return     
#    if Partner == "Laura" and "noticed Emma" in newgirl["Laura"].RecentActions and Other == "Emma":
#            return     
    
#    if "noticed Rogue" in newgirl["Laura"].RecentActions and Other == "Rogue":
#        if Partner == "Laura": 
#                return
#        else:
#                $ Silent = 1            
#    if "noticed Emma" in newgirl["Laura"].RecentActions and Other == "Emma":
#        if Partner == "Laura": 
#                return
#        else:
#                $ Silent = 1
            
    
    if not Silent and Partner != "Laura":
            call LauraFace("surprised", 1)           
            "Laura noticed what you and [Other] are up to."
    
    $ newgirl["Laura"].RecentActions.append("noticed " + Other)
    if "poly " + Other in newgirl["Laura"].Traits or (Other in P_Harem and "Laura" in P_Harem):
            #if they already have a relationship. . .
            $ B = (1000-(20*Taboo))  
    else:             
            #if they don't have a relationship. . .
            if Other == "Rogue":    
                    $ B = (newgirl["Laura"].LikeRogue - 500)  
            elif Other == "Kitty":    
                    $ B = (newgirl["Laura"].LikeKitty - 500)  
            elif Other == "Emma":    
                    $ B = (newgirl["Laura"].LikeEmma - 500)  
            if "dating" in newgirl["Laura"].Traits or "Laura" in P_Harem:
                    #if they already have a relationship. . .
                    $ B -= 200
          
#    if Other == "Rogue":       
#            $ R_RecentActions.append("noticed Laura")
#            if "poly Rogue" in newgirl["Laura"].Traits:
#                $ B = (1000-(20*Taboo))  
#            else:
#                $ B = (newgirl["Laura"].LikeRogue - 500)               
#                if "dating" in newgirl["Laura"].Traits or "Laura" in P_Harem:
#                    $ B -= 200
#    elif Other == "Kitty":            
#            $ newgirl["Laura"].RecentActions.append("noticed Kitty")
#            $ K_RecentActions.append("noticed Laura")
#            if "poly Kitty" in newgirl["Laura"].Traits:
#                $ B = (1000-(20*Taboo))  
#            else:
#                $ B = (newgirl["Laura"].LikeKitty - 500)               
#                if "dating" in newgirl["Laura"].Traits or "Laura" in P_Harem:
#                    $ B -= 200
#    elif Other == "Emma":            
#            $ newgirl["Laura"].RecentActions.append("noticed Emma")
#            $ E_RecentActions.append("noticed Laura")
#            if "poly Emma" in newgirl["Laura"].Traits:
#                $ B = (1000-(20*Taboo))  
#            else:
#                $ B = (newgirl["Laura"].LikeEmma - 500)               
#                if "dating" in newgirl["Laura"].Traits or "Laura" in P_Harem:
#                    $ B -= 200
                    
    $ newgirl["Laura"].SpriteLoc = StageFarRight  
    call Display_Laura(0,0) 
    $ Partner = "Laura"
    $ Line = 0
    if ApprovalCheck("Laura", 2000, TabM=2, Bonus = B) or ApprovalCheck("Laura", 950, "L", TabM=2, Bonus = (B/3)): 
            #if she's very loose or really likes you
            call LauraFace("sexy", 1)
            if not Silent:
                    "She decides to join you."                                      
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 5)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 3) 
            
            if "poly " + Other not in newgirl["Laura"].Traits: 
                    $ newgirl["Laura"].Traits.append("poly " + Other) 
                    
#            if Other == "Rogue" and "poly Rogue" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Rogue") 
#            elif Other == "Kitty" and "poly Kitty" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Kitty") 
#            elif Other == "Emma" and "poly Emma" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Emma") 
            call Laura_Threeway_Set(Mode="start",ActiveGirl=Other) 
    elif (ApprovalCheck("Laura", 650, "O", TabM=2) and ApprovalCheck("Laura", 450, "L", TabM=1)) or ApprovalCheck("Laura", 800, "O", TabM=2, Bonus = (B/3)): 
            #if she likes you, but is very obedient
            call LauraFace("sexy")
            if not Silent:
                    "She sits down patiently off to the side and watches."          
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5) 
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 5)  
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 2)  
            if "poly " + Other not in newgirl["Laura"].Traits: 
                    $ newgirl["Laura"].Traits.append("poly " + Other) 
                    
#            if Other == "Rogue" and "poly Rogue" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Rogue") 
#            elif Other == "Kitty" and "poly Kitty" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Kitty") 
#            elif Other == "Emma" and "poly Emma" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Emma") 
            call Laura_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif (ApprovalCheck("Laura", 650, "I", TabM=2) and ApprovalCheck("Laura", 450, "L", TabM=1)) or ApprovalCheck("Laura", 800, "I", TabM=2, Bonus = (B/3)):
            #if she likes you, but is very uninhibited
            call LauraFace("sexy")
            if not Silent:
                    "She sits down and watches you with a hungry look."             
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 5) 
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2)     
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5) 
            if "poly " + Other not in newgirl["Laura"].Traits: 
                    $ newgirl["Laura"].Traits.append("poly " + Other) 
#            if Other == "Rogue" and "poly Rogue" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Rogue") 
#            elif Other == "Kitty" and "poly Kitty" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Kitty") 
#            elif Other == "Emma" and "poly Emma" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("poly Emma") 
            call Laura_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Laura", 1500, TabM=2, Bonus = B):
            call LauraFace("perplexed", 1)
            if not Silent:
                    "She looks a little confused at what's happening, but she stays put and watches."
            if newgirl["Laura"].Love >= newgirl["Laura"].Obed and newgirl["Laura"].Love >= newgirl["Laura"].Inbt:
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 2)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2)                     
            elif newgirl["Laura"].Obed >= newgirl["Laura"].Inbt:
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2) 
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2)   
            else:
                $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, 2) 
                $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, 1)
                $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 1) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 90, 5)
            call Laura_Threeway_Set("watch",Mode="start",ActiveGirl=Other) 
    elif ApprovalCheck("Laura", 650, "L", TabM=1) or ApprovalCheck("Laura", 400, "O", TabM=2):
            #if she likes you or is obedient, but not enough
            call LauraFace("angry", 2)                
            if bg_current == "bg laura": 
                    "She looks annoyed, and kicks you both out of the room."
            else:
                    "She looks annoyed, and storms out of the room."                   
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 200, -5) 
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 80, -5) 
            $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 70, -5) 
            $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, -5)
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 89, 10) 
            if "saw with " + Other not in newgirl["Laura"].Traits: 
                    $ newgirl["Laura"].Traits.append("saw with " + Other) 
                    
#            if Other == "Rogue" and "saw with Rogue" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("saw with Rogue") 
#            elif Other == "Kitty" and "saw with Kitty" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("saw with Kitty") 
#            elif Other == "Emma" and "saw with Emma" not in newgirl["Laura"].Traits: 
#                    $ newgirl["Laura"].Traits.append("saw with Emma") 
            $ Partner = 0
            if bg_current == "bg laura": #Kicks you out if in Laura's room
                    $ newgirl["Laura"].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Laura")
    else:
            #if she doesn't like you much
            call LauraFace("surprised", 2)
            $ newgirl["Laura"].Inbt = Statupdate("Laura", "Inbt", newgirl["Laura"].Inbt, 90, 2) 
            $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 40, 20)
            if Trigger != "kiss you":
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -10) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, -5)
                    $ newgirl["Laura"].Lust = Statupdate("Laura", "Lust", newgirl["Laura"].Lust, 80, 10)
            if bg_current == "bg laura":
                    $ newgirl["Laura"].Love = Statupdate("Laura", "Love", newgirl["Laura"].Love, 90, -5) 
                    $ newgirl["Laura"].Obed = Statupdate("Laura", "Obed", newgirl["Laura"].Obed, 90, -5)
                    "She looks uncomfortable with this, and shoves you both out of the room."                 
            elif Trigger != "kiss you":
                    "She looks uncomfortable with this, and stalks out of the room." 
            else:
                    "She looks a bit disgusted and walks away."                                  
            $ Partner = 0       
            if bg_current == "bg laura": #Kicks you out if in Laura's room
                    $ newgirl["Laura"].RecentActions.append("angry")
                    call GirlsAngry
            call Remove_Girl("Laura")
            
    if Line:
        # This plays a line from a threesome action, if there is one. 
        "[Line]."          
        $ Line = 0
    return
    